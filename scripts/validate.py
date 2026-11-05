#!/usr/bin/env python3
"""Validate an exported agent folder against its raw API responses (no network).

    .venv/bin/python scripts/validate.py agents/<folder> [...]

Checks:
  1. Node and edge counts in generated files match raw/graph.json.
  2. Every code node has a non-empty code.<ext>; every LLM node has a prompt.md
     with a Prompt or Branch-conditions section (objective-only is reported).
  3. Every linked input points to a node and output that exist in the graph.
  4. Every raw node has a raw/nodes/<id>.json detail file.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import List

sys.path.insert(0, str(Path(__file__).resolve().parent))
from export import AgentModel  # noqa: E402


def validate(folder: Path) -> List[str]:
    problems: List[str] = []
    notes: List[str] = []
    graph = json.loads((folder / "raw" / "graph.json").read_text())
    details = {p.stem: json.loads(p.read_text()) for p in (folder / "raw" / "nodes").glob("*.json")}
    m = AgentModel(graph, details, folder.name)
    raw_nodes = graph["graph"]["nodes"]
    raw_edges = {e["id"] for n in raw_nodes for e in (n.get("childEdges") or [])}
    raw_parent_edges = {e["id"] for n in raw_nodes for e in (n.get("parentEdges") or [])}

    # 1. counts
    node_dirs = sorted(p.name for p in (folder / "nodes").iterdir() if p.is_dir())
    readme = (folder / "README.md").read_text()
    edge_rows = len(re.findall(r"^\| `\d\d-[^`]+` \| `\d\d-[^`]+` \|", readme, flags=re.M))
    mermaid_edges = len(re.findall(r"^    n\d\d -->", readme, flags=re.M))
    meta = json.loads((folder / "export.json").read_text())
    checks = {
        "raw nodes": len(raw_nodes), "node folders": len(node_dirs), "README node rows": len(re.findall(r"^\| \d\d \| \[", readme, flags=re.M)),
        "export.json nodeCount": meta["nodeCount"],
    }
    if len(set(checks.values())) != 1:
        problems.append(f"node count mismatch: {checks}")
    echecks = {"raw childEdges": len(raw_edges), "raw parentEdges": len(raw_parent_edges), "README edge rows": edge_rows,
               "Mermaid edges": mermaid_edges, "export.json edgeCount": meta["edgeCount"]}
    if len(set(echecks.values())) != 1:
        problems.append(f"edge count mismatch: {echecks}")
    notes.append(f"nodes: {checks}")
    notes.append(f"edges: {echecks}")

    # 4. detail coverage
    missing = [n["id"] for n in raw_nodes if n["id"] not in details]
    if missing:
        problems.append(f"missing node detail files: {missing}")

    # 2. code / prompt presence
    for nid in m.order:
        nd = folder / "nodes" / m.label[nid]
        tc = m.tool(nid)
        if tc.get("codeLanguage") or (m.tool_type(nid) == "code_executor_tool"):
            codes = list(nd.glob("code.*"))
            if not codes or not codes[0].read_text().strip():
                problems.append(f"{m.label[nid]}: code node without non-empty code file")
            elif codes[0].read_text() != tc.get("code"):
                problems.append(f"{m.label[nid]}: code file differs from raw toolConfiguration.code")
            else:
                notes.append(f"{m.label[nid]}: {codes[0].name} matches raw ({len(tc.get('code'))} chars)")
        if m.is_llm(nid):
            pm = nd / "prompt.md"
            text = pm.read_text() if pm.exists() else ""
            if "## Prompt" in text or "## Branch conditions" in text:
                if tc.get("prompt") and tc["prompt"] not in text:
                    problems.append(f"{m.label[nid]}: prompt.md does not contain the full raw prompt")
            elif "## Objective" in text:
                notes.append(f"{m.label[nid]}: LLM node has no prompt in BeamAI; prompt.md holds the objective only")
            else:
                problems.append(f"{m.label[nid]}: LLM node without prompt.md content")

    # 3. linked inputs
    out_owner = {}
    for nid, n in m.nodes.items():
        for op in (m.tool(nid).get("outputParams") or []):
            out_owner[op["id"]] = nid
    linked = 0
    for nid in m.order:
        for ip in m.tool(nid).get("inputParams") or []:
            link = ip.get("linkParamOutputId")
            if ip.get("fillType") == "linked" or link:
                linked += 1
                if link not in out_owner:
                    problems.append(f"{m.label[nid]}.input.{ip.get('paramName')}: linked output {link} not found")
                elif out_owner[link] not in m.nodes:
                    problems.append(f"{m.label[nid]}.input.{ip.get('paramName')}: source node missing")
        inputs_md = folder / "nodes" / m.label[nid] / "inputs.md"
        if inputs_md.exists() and "UNRESOLVED" in inputs_md.read_text():
            problems.append(f"{m.label[nid]}: inputs.md has UNRESOLVED links")
    notes.append(f"linked inputs checked: {linked}")

    for n in notes:
        print(f"  info  {n}")
    for p in problems:
        print(f"  FAIL  {p}")
    return problems


def main() -> int:
    failed = 0
    for arg in sys.argv[1:]:
        print(f"== {arg}")
        failed += bool(validate(Path(arg)))
    print("RESULT:", "FAIL" if failed else "PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
