#!/usr/bin/env python3
"""Phase 1 discovery for BeamAI workflows (read-only).

Run through 1Password so credentials never touch disk or the terminal:

    op run --env-file=.env.tpl -- .venv/bin/python scripts/discover.py inventory
    op run --env-file=.env.tpl -- .venv/bin/python scripts/discover.py pull <agentId>

Nothing is written if any response contains personal data; the script prints the
JSON paths and kinds of what it found (never the values) and exits with code 3.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any, Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
from beam_safety import BeamClient, PiiHit, ScrubReport, redact_samples, scan_pii, scrub  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DISCOVERY = ROOT / "discovery"
log = logging.getLogger("discover")


def slugify(name: str) -> str:
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "agent"


def assign_folders(agents: List[Dict[str, Any]]) -> Dict[str, str]:
    """agentId -> folder name, adding the first 8 chars of the ID on collisions."""
    by_slug: Dict[str, List[str]] = {}
    for a in agents:
        by_slug.setdefault(slugify(a.get("name") or ""), []).append(a["id"])
    out: Dict[str, str] = {}
    for slug, ids in by_slug.items():
        for agent_id in ids:
            out[agent_id] = slug if len(ids) == 1 else f"{slug}-{agent_id[:8].lower()}"
    return out


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + "\n")


def report_pii(hits: List[Tuple[str, PiiHit]]) -> None:
    print("\nPERSONAL DATA DETECTED - nothing was written to disk.", file=sys.stderr)
    print("Locations (values not shown):", file=sys.stderr)
    for source, h in hits:
        print(f"  {source}  {h.path}  kind={h.kind}  {h.note}", file=sys.stderr)


def list_agents(client: BeamClient) -> List[Dict[str, Any]]:
    agents: List[Dict[str, Any]] = []
    page = 1
    while True:
        data = client.get("/agent", params={"pageNum": page, "pageSize": 100})
        batch = data.get("agents") or []
        agents.extend(batch)
        total = data.get("count")
        log.info("page %s: %s agents (count=%s)", page, len(batch), total)
        if not batch or (isinstance(total, (int, float)) and len(agents) >= total) or len(batch) < 100:
            break
        page += 1
    return agents


def graph_summary(graph_resp: Dict[str, Any]) -> Dict[str, Any]:
    g = graph_resp.get("graph") or {}
    nodes = g.get("nodes") or []
    edges = {e.get("id") for n in nodes for e in (n.get("childEdges") or [])}
    return {
        "graphId": g.get("id"),
        "isActive": g.get("isActive"),
        "isDraft": g.get("isDraft"),
        "isPublished": g.get("isPublished"),
        "isEdited": g.get("isEdited"),
        "publishedAt": g.get("publishedAt"),
        "nodeCount": len(nodes),
        "edgeCount": len(edges),
        "nodeTypes": sorted({n.get("nodeType") or "?" for n in nodes}),
    }


def cmd_inventory(client: BeamClient) -> int:
    report = ScrubReport()
    raw_agents = list_agents(client)
    agents = scrub(raw_agents, report, client.sensitive_values)
    hits = [("agent-list", h) for h in scan_pii(agents)]

    folders = assign_folders(agents)
    rows: List[Dict[str, Any]] = []
    for a in agents:
        row: Dict[str, Any] = {
            "id": a["id"], "name": a.get("name"), "type": a.get("type"),
            "category": (a.get("category") or {}).get("title"), "folder": folders[a["id"]],
        }
        try:
            graph = scrub(client.get(f"/agent-graphs/{a['id']}"), report, client.sensitive_values)
            row.update(graph_summary(graph))
        except Exception as exc:  # keep going; record the failure
            row["error"] = str(exc)
        rows.append(row)

    if hits:
        report_pii(hits)
        return 3
    write_json(DISCOVERY / "agents.json", agents)
    write_json(DISCOVERY / "inventory.json", rows)
    write_json(DISCOVERY / "secrets-found.inventory.json", report.placeholders)
    for r in rows:
        print(json.dumps(r, ensure_ascii=False))
    return 0


def summarize_pii(hits: List[Tuple[str, PiiHit]]) -> None:
    """Aggregate hits by field pattern and kind (no values, no node IDs)."""
    from collections import Counter
    counts: Counter = Counter()
    for source, h in hits:
        field_pattern = re.sub(r"\[\d+\]", "[]", h.path).replace("$.graph.nodes[]", "$")
        src = "graph" if not source.startswith("nodes/") else "node-detail"
        counts[(h.kind, h.note, field_pattern, src)] += 1
    print(f"SCAN ONLY - nothing written. {len(hits)} hits.")
    for (kind, note, fp, src), n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"{n:5d}  {kind:32s} {note:34s} {src:11s} {fp}")


def cmd_pull(client: BeamClient, agent_id: str, folder: str, scan_only: bool = False) -> int:
    report = ScrubReport()
    collected: Dict[str, Any] = {}
    collected["graph.json"] = client.get(f"/agent-graphs/{agent_id}")
    collected["graph-lite.json"] = client.get(f"/agent-graphs/{agent_id}/nodes/lite")
    nodes = (collected["graph.json"].get("graph") or {}).get("nodes") or []
    for n in nodes:
        collected[f"nodes/{n['id']}.json"] = client.get(f"/agent-graphs/{agent_id}/nodes/{n['id']}")
    lite_graph_id = collected["graph-lite.json"].get("graphId")
    full_graph_id = (collected["graph.json"].get("graph") or {}).get("id")
    if lite_graph_id and lite_graph_id != full_graph_id:
        collected["graph-by-lite-graphId.json"] = client.get(
            f"/agent-graphs/{agent_id}", params={"graphId": lite_graph_id})
    try:
        collected["preferred-models.json"] = client.get("/custom-tool/preferred-models")
    except Exception as exc:
        log.warning("preferred-models not available: %s", exc)

    cleaned = {name: redact_samples(scrub(data, report, client.sensitive_values))
               for name, data in collected.items()}
    # Betterment addresses in workflow config are kept (decision 2026-11-05, Q3).
    hits = [(name, h) for name, data in cleaned.items() for h in scan_pii(data)
            if not (h.kind == "email" and h.note == "internal domain")]
    if scan_only:
        summarize_pii(hits)
        return 3 if hits else 0
    if hits:
        report_pii(hits)
        return 3

    out = DISCOVERY / folder
    for name, data in cleaned.items():
        write_json(out / name, data)
    write_json(out / "secrets-found.json", report.placeholders)
    print(f"Wrote {len(cleaned)} files to {out.relative_to(ROOT)}")
    print(f"nodes={len(nodes)} placeholders={sorted(report.placeholders)}")
    return 0


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("inventory", help="list all agents with graph summaries")
    p = sub.add_parser("pull", help="pull one agent's graph and node details")
    p.add_argument("agent_id")
    p.add_argument("--folder", help="output folder under discovery/ (default: from inventory)")
    p.add_argument("--scan-only", action="store_true", help="fetch and scan for personal data; write nothing")
    args = ap.parse_args()

    client = BeamClient()
    if args.cmd == "inventory":
        return cmd_inventory(client)
    folder = args.folder
    if not folder:
        inv = json.loads((DISCOVERY / "inventory.json").read_text())
        folder = next((r["folder"] for r in inv if r["id"] == args.agent_id), None) or args.agent_id
    return cmd_pull(client, args.agent_id, folder, scan_only=args.scan_only)


if __name__ == "__main__":
    sys.exit(main())
