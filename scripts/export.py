#!/usr/bin/env python3
"""Export BeamAI agent workflows into this repository (read-only against BeamAI).

Usage (credentials come from 1Password and are never printed or written):

    op run --env-file=.env.tpl -- .venv/bin/python scripts/export.py --agent <agentId>
    op run --env-file=.env.tpl -- .venv/bin/python scripts/export.py --all

For each agent this writes ``agents/<folder>/``:

    raw/graph.json            GET /agent-graphs/{agentId}, credentials and sample values removed only
    raw/nodes/<nodeId>.json   GET /agent-graphs/{agentId}/nodes/{nodeId}, same treatment
    graph.json                raw graph with keys sorted, timestamps and canvas coordinates removed
    export.json               export metadata (used to build the root README and manifests)
    README.md                 summary, Mermaid flow, node and edge tables
    nodes/<NN>-<name>/        node.json, code.<ext>, prompt.md, inputs.md

and refreshes ``README.md``, ``shared/integrations/*.json`` and ``secrets.manifest.yaml``
from every exported agent. Everything outside ``raw/`` is generated from ``raw/``.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import logging
import re
import shutil
import sys
import unicodedata
from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
from beam_safety import BeamClient, ScrubReport, redact_samples, scan_pii, scrub  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / "agents"
SHARED_INTEGRATIONS = ROOT / "shared" / "integrations"
log = logging.getLogger("export")

VOLATILE_KEYS = {"createdAt", "updatedAt", "deletedAt", "publishedAt", "testStartedAt",
                 "xCoordinate", "yCoordinate"}
CODE_EXTENSIONS = {"javascript": "js", "js": "js", "typescript": "ts", "ts": "ts",
                   "python": "py", "py": "py", "bash": "sh", "shell": "sh", "sql": "sql"}
DEFAULT_NODE_NAMES = {"entryNode": "trigger", "exitNode": "end", "conditionNode": "condition",
                      "loopingNode": "loop", "waitingNode": "wait"}
LLM_TOOL_TYPES = {"custom_gpt_tool", "gpt_tool"}


class PersonalDataFound(Exception):
    pass


# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def dump_raw(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def dump_sorted(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def strip_volatile(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: strip_volatile(v) for k, v in obj.items() if k not in VOLATILE_KEYS}
    if isinstance(obj, list):
        return [strip_volatile(v) for v in obj]
    return obj


def md_cell(value: Any) -> str:
    if value is None or value == "":
        return ""
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\r", "").replace("\n", "<br>")


def fence(text: str, lang: str = "text") -> str:
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    ticks = "`" * max(3, longest + 1)
    return f"{ticks}{lang}\n{text}\n{ticks}"


def one_line(text: Optional[str], limit: int = 140) -> str:
    line = " ".join((text or "").split())
    return line if len(line) <= limit else line[: limit - 1] + "…"


def mermaid_label(text: str, limit: int = 70) -> str:
    text = one_line(text, limit)
    return text.replace('"', "#quot;").replace("|", "#124;").replace("[", "#91;").replace("]", "#93;")


# --------------------------------------------------------------------------- #
# Fetch
# --------------------------------------------------------------------------- #

def list_agents(client: BeamClient) -> List[Dict[str, Any]]:
    agents: List[Dict[str, Any]] = []
    page = 1
    while True:
        data = client.get("/agent", params={"pageNum": page, "pageSize": 100})
        batch = data.get("agents") or []
        agents.extend(batch)
        total = data.get("count")
        if not batch or len(batch) < 100 or (isinstance(total, (int, float)) and len(agents) >= total):
            return agents
        page += 1


def assign_folders(agents: List[Dict[str, Any]]) -> Dict[str, str]:
    by_slug: Dict[str, List[str]] = {}
    for a in agents:
        by_slug.setdefault(slugify(a.get("name") or "") or "agent", []).append(a["id"])
    folders: Dict[str, str] = {}
    for slug, ids in by_slug.items():
        for agent_id in ids:
            folders[agent_id] = slug if len(ids) == 1 else f"{slug}-{agent_id[:8].lower()}"
    return folders


def fetch_agent(client: BeamClient, agent_id: str) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Dict[str, Any]], ScrubReport]:
    """Return (graph, lite, nodeDetails, scrubReport), credentials and samples removed.

    Raises PersonalDataFound (and nothing is written) if customer data is detected.
    """
    report = ScrubReport()  # placeholder name -> ["<raw file>|<json path>", ...]

    def clean(data: Any, raw_file: str) -> Any:
        part = ScrubReport()
        out = redact_samples(scrub(data, part, client.sensitive_values))
        for name, paths in part.placeholders.items():
            for p in paths:
                report.add(name, f"{raw_file}|{p}")
        return out

    graph = clean(client.get(f"/agent-graphs/{agent_id}"), "raw/graph.json")
    lite = clean(client.get(f"/agent-graphs/{agent_id}/nodes/lite"), "lite")
    details: Dict[str, Dict[str, Any]] = {}
    for node in graph["graph"]["nodes"]:
        details[node["id"]] = clean(client.get(f"/agent-graphs/{agent_id}/nodes/{node['id']}"),
                                    f"raw/nodes/{node['id']}.json")

    sources = [("raw/graph.json", graph)] + [(f"raw/nodes/{k}.json", v) for k, v in details.items()]
    hits = [(name, h) for name, data in sources for h in scan_pii(data)
            if not (h.kind == "email" and h.note == "internal domain")]  # Betterment addresses kept (NOTES Q3)
    if hits:
        for name, h in hits:
            log.error("personal data: %s %s kind=%s %s", name, h.path, h.kind, h.note)
        raise PersonalDataFound(f"{len(hits)} personal-data hits; nothing written for agent {agent_id}")
    return graph, lite, details, report


# --------------------------------------------------------------------------- #
# Model built from raw/
# --------------------------------------------------------------------------- #

class AgentModel:
    def __init__(self, graph_resp: Dict[str, Any], details: Dict[str, Dict[str, Any]], folder: str) -> None:
        self.graph = graph_resp["graph"]
        self.details = details
        self.folder = folder
        self.nodes: Dict[str, Dict[str, Any]] = {n["id"]: n for n in self.graph["nodes"]}
        edges: Dict[str, Dict[str, Any]] = {}
        for n in self.graph["nodes"]:
            for e in n.get("childEdges") or []:
                edges.setdefault(e["id"], e)
        self.order = self._execution_order()
        pos = {nid: i for i, nid in enumerate(self.order)}
        self.edges: "OrderedDict[str, Dict[str, Any]]" = OrderedDict(sorted(
            edges.items(), key=lambda kv: (pos.get(kv[1]["sourceAgentGraphNodeId"], 1e9),
                                           pos.get(kv[1]["targetAgentGraphNodeId"], 1e9), kv[0])))
        self.label: Dict[str, str] = {}      # nodeId -> "NN-name"
        self.title: Dict[str, str] = {}      # nodeId -> human title
        for i, nid in enumerate(self.order, start=1):
            n = self.nodes[nid]
            tool_name = (n.get("toolConfiguration") or {}).get("toolName") or ""
            name = slugify(tool_name) or DEFAULT_NODE_NAMES.get(n.get("nodeType"), "node")
            if n.get("isExitNode") and not tool_name:
                name = "end"
            self.label[nid] = f"{i:02d}-{name}"
            self.title[nid] = tool_name or name.replace("-", " ").title()
        self.id_names = self._id_names()

    def _execution_order(self) -> List[str]:
        entries = [n["id"] for n in self.graph["nodes"] if n.get("isEntryNode") or n.get("nodeType") == "entryNode"]
        seen: List[str] = []
        queue = list(entries)
        while queue:
            nid = queue.pop(0)
            if nid in seen or nid not in self.nodes:
                continue
            seen.append(nid)
            queue.extend(e["targetAgentGraphNodeId"] for e in self.nodes[nid].get("childEdges") or [])
        rest = sorted((n for n in self.nodes if n not in seen),
                      key=lambda x: ((self.nodes[x].get("toolConfiguration") or {}).get("toolName") or "", x))
        return seen + rest

    def _id_names(self) -> Dict[str, str]:
        names: Dict[str, str] = {}
        for nid, n in self.nodes.items():
            names[nid] = self.label[nid]
            if n.get("customId"):
                names[n["customId"]] = self.label[nid]
            tc = n.get("toolConfiguration") or {}
            if tc.get("id"):
                names[tc["id"]] = f"{self.label[nid]}.tool"
            for op in tc.get("outputParams") or []:
                names[op["id"]] = f"{self.label[nid]}.output.{op.get('paramPath') or op.get('paramName')}"
            for ip in tc.get("inputParams") or []:
                names[ip["id"]] = f"{self.label[nid]}.input.{ip.get('paramName')}"
        for eid, e in self.edges.items():
            names[eid] = f"{self.label.get(e['sourceAgentGraphNodeId'], '?')} -> {self.label.get(e['targetAgentGraphNodeId'], '?')}"
        return names

    # -- per-node views -------------------------------------------------- #
    def tool(self, nid: str) -> Dict[str, Any]:
        return (self.details.get(nid) or self.nodes[nid]).get("toolConfiguration") or {}

    def node_conf(self, nid: str) -> Dict[str, Any]:
        return (self.details.get(nid) or self.nodes[nid]).get("nodeConfigurations") or {}

    def tool_type(self, nid: str) -> str:
        return (self.tool(nid).get("originalTool") or {}).get("type") or ""

    def model(self, nid: str) -> Tuple[str, str]:
        tc, nc = self.tool(nid), self.node_conf(nid)
        if self.nodes[nid].get("nodeType") == "conditionNode":
            return nc.get("llmModel") or "", nc.get("fallbackModels") or ""
        return tc.get("preferredModel") or "", tc.get("fallbackModels") or ""

    def integration(self, nid: str) -> Optional[Dict[str, Any]]:
        integ = (self.tool(nid).get("originalTool") or {}).get("integration")
        return integ if isinstance(integ, dict) and integ.get("id") else None

    def is_llm(self, nid: str) -> bool:
        n = self.nodes[nid]
        if n.get("nodeType") == "conditionNode":
            return self.node_conf(nid).get("conditionType") == "llm_based"
        return self.tool_type(nid) in LLM_TOOL_TYPES

    def edge_condition(self, e: Dict[str, Any]) -> str:
        parts = []
        if (e.get("condition") or "").strip():
            parts.append(e["condition"].strip())
        for gi, grp in enumerate(e.get("conditionGroups") or []):
            rules = []
            for r in grp.get("rules") or []:
                src = self.id_names.get(r.get("sourceAgentToolConfigurationOutputParamsId"), r.get("sourceAgentToolConfigurationOutputParamsId"))
                cmp_ = r.get("comparisonValue") if r.get("comparisonValueType") == "static" else \
                    self.id_names.get(r.get("comparisonAgentToolConfigurationOutputParamsId"), r.get("comparisonAgentToolConfigurationOutputParamsId"))
                rules.append(f"{src} {r.get('operator')} {cmp_!r}" + (f" {r['nextRuleOperator']}" if r.get("nextRuleOperator") else ""))
            if rules:
                parts.append("(" + " ".join(rules) + ")" + (f" {grp['nextGroupOperator']}" if grp.get("nextGroupOperator") else ""))
        return " ".join(parts)


# --------------------------------------------------------------------------- #
# Derived files
# --------------------------------------------------------------------------- #

def annotate_ids(obj: Any, names: Dict[str, str]) -> Any:
    """Add ``<key>__readable`` next to every value that is a known internal ID."""
    if isinstance(obj, dict):
        out: Dict[str, Any] = {}
        for k, v in obj.items():
            out[k] = annotate_ids(v, names)
            if k != "id" and isinstance(v, str) and v in names:
                out[f"{k}__readable"] = names[v]
        return out
    if isinstance(obj, list):
        return [annotate_ids(v, names) for v in obj]
    return obj


def integration_file(integ: Dict[str, Any]) -> str:
    return f"{slugify(integ.get('name') or integ['id'])}.json"


def build_node_json(m: AgentModel, nid: str, depth_to_root: int) -> Dict[str, Any]:
    graph_node = m.nodes[nid]
    detail = json.loads(json.dumps(m.details.get(nid) or graph_node))
    detail.pop("agentGraph", None)  # agent-level settings; see the agent README
    # Overlay graph-only fields so node.json is complete.
    gtc, dtc = graph_node.get("toolConfiguration") or {}, detail.get("toolConfiguration") or {}
    for key in ("description", "iconSrc"):
        if key in gtc and key not in dtc:
            dtc[key] = gtc[key]
    g_inputs = {ip["id"]: ip for ip in gtc.get("inputParams") or []}
    for ip in dtc.get("inputParams") or []:
        if "linkedOutputParamRules" not in ip and ip.get("id") in g_inputs:
            ip["linkedOutputParamRules"] = g_inputs[ip["id"]].get("linkedOutputParamRules")
    for side in ("childEdges", "parentEdges"):
        g_edges = {e["id"]: e for e in graph_node.get(side) or []}
        for e in detail.get(side) or []:
            if "conditionGroups" not in e and e.get("id") in g_edges:
                e["conditionGroups"] = g_edges[e["id"]].get("conditionGroups")
    # Integrations are stored once in shared/integrations/.
    integ = m.integration(nid)
    if integ:
        dtc.setdefault("originalTool", {})["integration"] = {
            "$ref": "../" * depth_to_root + f"shared/integrations/{integration_file(integ)}",
            "id": integ.get("id"), "name": integ.get("name"),
        }
    detail["toolConfiguration"] = dtc
    detail = strip_volatile(detail)
    detail["_export"] = {
        "folder": m.label[nid],
        "executionOrder": m.order.index(nid) + 1,
        "rawGraph": "../../raw/graph.json",
        "rawDetail": f"../../raw/nodes/{nid}.json",
    }
    return annotate_ids(detail, m.id_names)


def build_prompt_md(m: AgentModel, nid: str) -> Optional[str]:
    n, tc = m.nodes[nid], m.tool(nid)
    detail = m.details.get(nid) or n
    model, fallbacks = m.model(nid)
    sections: List[str] = []
    if (detail.get("objective") or "").strip():
        sections.append("## Objective\n\n" + fence(detail["objective"]))
    if (tc.get("prompt") or "").strip():
        sections.append("## Prompt\n\nSource: `toolConfiguration.prompt`\n\n" + fence(tc["prompt"]))
    ot = tc.get("originalTool") or {}
    for label, text in (("originalTool.prompt", ot.get("prompt")),
                        ("originalTool.meta.prompt", (ot.get("meta") or {}).get("prompt") if isinstance(ot.get("meta"), dict) else None)):
        if isinstance(text, str) and text.strip() and text != tc.get("prompt"):
            sections.append(f"## Tool template prompt\n\nSource: `toolConfiguration.{label}` (differs from the node prompt)\n\n" + fence(text))
    if n.get("nodeType") == "conditionNode":
        lines = [f"| Branch to | Condition |", "|---|---|"]
        for e in n.get("childEdges") or []:
            lines.append(f"| `{m.label.get(e['targetAgentGraphNodeId'], '?')}` | {md_cell(m.edge_condition(e))} |")
        sections.append(f"## Branch conditions ({m.node_conf(nid).get('conditionType')})\n\n" + "\n".join(lines))
    if (detail.get("autoRetryDescription") or "").strip():
        sections.append("## Auto-retry instructions\n\n" + fence(detail["autoRetryDescription"]))
    if detail.get("evaluationCriteria"):
        sections.append("## Evaluation criteria\n\n" + fence(json.dumps(detail["evaluationCriteria"], indent=2, ensure_ascii=False), "json"))
    if not sections:
        return None
    header = [f"# {m.label[nid]}: {m.title[nid]}", "",
              f"- Node ID: `{nid}`",
              f"- Tool: `{tc.get('toolFunctionName') or '-'}` ({m.tool_type(nid) or n.get('nodeType')})"]
    if model or fallbacks:
        header.append(f"- Model: `{model or '-'}`" + (f", fallbacks: `{fallbacks}`" if fallbacks else ""))
    if tc.get("llmThinkingLevels"):
        header.append(f"- Thinking level: `{tc['llmThinkingLevels']}`")
    return "\n".join(header) + "\n\n" + "\n\n".join(sections) + "\n"


def build_inputs_md(m: AgentModel, nid: str) -> Optional[str]:
    params = sorted(m.tool(nid).get("inputParams") or [], key=lambda p: (p.get("position") or 0, p.get("paramName") or ""))
    if not params:
        return None
    rows = ["| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |",
            "|---|---|---|---|---|---|---|---|---|"]
    for p in params:
        link = p.get("linkParamOutputId")
        source = f"`{m.id_names.get(link, 'UNRESOLVED')}`" if link else ""
        desc = p.get("question") if p.get("fillType") == "user_fill" else p.get("paramDescription")
        ids = f"param `{p.get('id')}`" + (f"<br>output `{link}`" if link else "")
        rows.append("| " + " | ".join([
            str(p.get("position", "")), f"`{p.get('paramName')}`", p.get("fillType") or "",
            "yes" if p.get("required") else "", md_cell(p.get("dataType")),
            md_cell(p.get("staticValue")), source, md_cell(desc), ids]) + " |")
    return f"# {m.label[nid]}: inputs\n\n" + "\n".join(rows) + "\n"


def build_agent_readme(m: AgentModel, meta: Dict[str, Any], detail_agent: Dict[str, Any]) -> str:
    g, agent = m.graph, m.graph.get("agent") or {}
    out: List[str] = [f"# {agent.get('name')}", ""]
    out += [
        "_Generated by `scripts/export.py` from `raw/`. Don't edit by hand._", "",
        "| | |", "|---|---|",
        f"| Agent ID | `{agent.get('id')}` |",
        f"| Graph ID | `{g.get('id')}` |",
        f"| Graph status | {meta['status']} (isDraft={g.get('isDraft')}, isPublished={g.get('isPublished')}) |",
        f"| Type / category | {agent.get('type') or detail_agent.get('type') or '-'} / {(agent.get('category') or {}).get('title') or '-'} |",
        f"| Nodes / edges | {meta['nodeCount']} / {meta['edgeCount']} |",
        f"| Last export | {meta['lastExported']} |",
        "",
    ]
    if (agent.get("description") or "").strip():
        out += ["## Description", "", agent["description"].strip(), ""]

    out += ["## Trigger", "",
            "The BeamAI API doesn't return trigger configuration (provider, event, filters, webhook). "
            f"The entry node is `{m.label[m.order[0]]}`. Record the trigger from the Beam UI in `NOTES.md`.", ""]

    # Mermaid
    out += ["## Flow", "", "```mermaid", "flowchart TD"]
    for nid in m.order:
        n = m.nodes[nid]
        text = mermaid_label(f"{m.label[nid][:2]} · {m.title[nid]}", 60)
        integ = m.integration(nid)
        if integ:
            text += "<br/>" + mermaid_label(integ.get("name") or "", 40)
        mid = f"n{m.label[nid][:2]}"
        shape = {"conditionNode": ('{"', '"}'), "entryNode": ('(["', '"])'), "loopingNode": ('[["', '"]]'),
                 "waitingNode": ('[/"', '"/]')}.get(n.get("nodeType"), ('["', '"]'))
        if n.get("isExitNode") and n.get("nodeType") not in ("conditionNode",):
            shape = ('(["', '"])')
        out.append(f"    {mid}{shape[0]}{text}{shape[1]}")
    for e in m.edges.values():
        s, t = m.label.get(e["sourceAgentGraphNodeId"]), m.label.get(e["targetAgentGraphNodeId"])
        cond = m.edge_condition(e)
        arrow = f' -->|"{mermaid_label(cond)}"| ' if cond else " --> "
        out.append(f"    n{s[:2]}{arrow}n{t[:2]}")
    out += ["```", ""]

    # Node table
    out += ["## Nodes", "", "| # | Node | Type | Tool | Model (fallbacks) | What it does |", "|---|---|---|---|---|---|"]
    for nid in m.order:
        n, tc = m.nodes[nid], m.tool(nid)
        model, fb = m.model(nid)
        detail = m.details.get(nid) or n
        what = detail.get("objective") or ""
        if n.get("nodeType") == "conditionNode":
            what = "Branches: " + "; ".join(m.edge_condition(e) for e in n.get("childEdges") or [])
        if n.get("nodeType") == "loopingNode":
            var = m.node_conf(nid).get("linkedVariableId")
            what = f"Loops over {m.id_names.get(var, var or '?')}" + (f" ({what})" if what and what != "Loop" else "")
        integ = m.integration(nid)
        tool = f"`{tc.get('toolFunctionName')}`" if tc.get("toolFunctionName") else ""
        if integ:
            tool += f"<br>[{md_cell(integ.get('name'))}](../../shared/integrations/{integration_file(integ)})"
        out.append(f"| {m.label[nid][:2]} | [{md_cell(m.title[nid])}](nodes/{m.label[nid]}/) | {n.get('nodeType')}"
                   f"{' / ' + m.tool_type(nid) if m.tool_type(nid) else ''} | {tool} | "
                   f"{('`' + model + '`') if model else ''}{(' (' + md_cell(fb) + ')') if fb else ''} | {md_cell(one_line(what))} |")
    out.append("")

    # Edge table
    out += ["## Edges", "", "| From | To | Condition | Edge ID |", "|---|---|---|---|"]
    for eid, e in m.edges.items():
        out.append(f"| `{m.label.get(e['sourceAgentGraphNodeId'])}` | `{m.label.get(e['targetAgentGraphNodeId'])}` | "
                   f"{md_cell(m.edge_condition(e))} | `{eid}` |")
    out.append("")

    # Integrations
    integrations = sorted({(i.get("name"), integration_file(i)) for i in (m.integration(n) for n in m.order) if i})
    if integrations:
        out += ["## Integrations", ""] + [f"- [{name}](../../shared/integrations/{f})" for name, f in integrations] + [""]

    # Agent-level settings (node-detail only)
    settings = detail_agent.get("settings") or {}
    filled = {k: v for k, v in settings.items() if v not in (None, "", [], {})}
    out += ["## Agent settings", "", "Source: `raw/nodes/*.json` → `agentGraph.agent.settings`, plus `reasoningEffort` and the governance fields.", ""]
    for k in ("reasoningEffort", "governanceEnabled", "governanceModel"):
        if detail_agent.get(k) not in (None, ""):
            out.append(f"- `{k}`: `{detail_agent.get(k)}`")
    for k in sorted(settings):
        v = settings[k]
        if k in filled and isinstance(v, str) and len(v) > 80:
            out += [f"- `{k}`:", "", fence(v), ""]
        else:
            out.append(f"- `{k}`: {('`' + json.dumps(v, ensure_ascii=False) + '`') if k in filled else '(empty)'}")
    out.append("")

    out += ["## Files", "",
            "- `raw/graph.json`, `raw/nodes/<nodeId>.json`: API responses, with credentials and sample values removed only.",
            "- `graph.json`: the raw graph with keys sorted, timestamps and canvas coordinates removed.",
            "- `nodes/<NN>-<name>/`: `node.json` (internal IDs get a `__readable` partner key), `code.<ext>`, `prompt.md`, `inputs.md`.",
            ""]
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Export one agent
# --------------------------------------------------------------------------- #

def raw_hash(folder: Path) -> str:
    h = hashlib.sha256()
    for p in sorted((folder / "raw").rglob("*.json")):
        h.update(p.relative_to(folder).as_posix().encode())
        h.update(p.read_bytes())
    return h.hexdigest()


def export_agent(client: BeamClient, agent_id: str, folder: str, today: str) -> Dict[str, Any]:
    graph_resp, _lite, details, report = fetch_agent(client, agent_id)
    out = AGENTS_DIR / folder
    previous = json.loads((out / "export.json").read_text()) if (out / "export.json").exists() else {}

    # raw/ is fully regenerated so removed nodes do not linger.
    for sub in ("raw", "nodes"):
        shutil.rmtree(out / sub, ignore_errors=True)
    write(out / "raw" / "graph.json", dump_raw(graph_resp))
    for nid, d in details.items():
        write(out / "raw" / "nodes" / f"{nid}.json", dump_raw(d))

    # Everything below is generated from raw/ (re-read from disk to guarantee that).
    graph_resp = json.loads((out / "raw" / "graph.json").read_text())
    details = {p.stem: json.loads(p.read_text()) for p in (out / "raw" / "nodes").glob("*.json")}
    m = AgentModel(graph_resp, details, folder)

    write(out / "graph.json", dump_sorted(strip_volatile(graph_resp)))
    for nid in m.order:
        nd = out / "nodes" / m.label[nid]
        write(nd / "node.json", dump_sorted(build_node_json(m, nid, depth_to_root=4)))
        tc = m.tool(nid)
        if (tc.get("code") or "").strip():
            lang = (tc.get("codeLanguage") or "txt").lower()
            write(nd / f"code.{CODE_EXTENSIONS.get(lang, lang)}", tc["code"])
        for name, text in (("prompt.md", build_prompt_md(m, nid)), ("inputs.md", build_inputs_md(m, nid))):
            if text:
                write(nd / name, text)

    h = raw_hash(out)
    g = m.graph
    meta: Dict[str, Any] = {
        "agentId": agent_id,
        "agentName": (g.get("agent") or {}).get("name"),
        "folder": folder,
        "graphId": g.get("id"),
        "status": "published" if g.get("isPublished") else "draft",
        "nodeCount": len(m.nodes),
        "edgeCount": len(m.edges),
        "rawSha256": h,
        "lastExported": previous.get("lastExported") if previous.get("rawSha256") == h else today,
        "integrations": {},
        "secrets": {},
    }
    for nid in m.order:
        integ = m.integration(nid)
        if integ:
            meta["integrations"].setdefault(integration_file(integ), []).append(m.label[nid])
    for name, paths in sorted(report.placeholders.items()):
        meta["secrets"][name] = sorted({_secret_file(p, m) for p in paths})
    write(out / "export.json", dump_sorted(meta))

    detail_agent = next((d.get("agentGraph") or {}).get("agent") or {} for d in details.values()) if details else {}
    write(out / "README.md", build_agent_readme(m, meta, detail_agent))
    _write_integrations(m, folder)
    log.info("exported %s -> agents/%s (%d nodes, %d edges)", meta["agentName"], folder, meta["nodeCount"], meta["edgeCount"])
    return meta


def _secret_file(location: str, m: AgentModel) -> str:
    """Map "<raw file>|<json path>" to a file name plus the node it belongs to."""
    raw_file, _, json_path = location.partition("|")
    mt = re.match(r"\$\.graph\.nodes\[(\d+)\]", json_path)
    if raw_file == "raw/graph.json" and mt:
        return f"raw/graph.json ({m.label[m.graph['nodes'][int(mt.group(1))]['id']]})"
    node_id = raw_file[len("raw/nodes/"):-len(".json")] if raw_file.startswith("raw/nodes/") else ""
    if node_id in m.label:
        return f"{raw_file} ({m.label[node_id]})"
    return raw_file


def _write_integrations(m: AgentModel, folder: str) -> None:
    """Write each integration definition once; keep usage info from other agents."""
    found: Dict[str, Dict[str, Any]] = {}
    for nid in m.order:
        integ = m.integration(nid)
        if not integ:
            continue
        fname = integration_file(integ)
        ot = m.tool(nid).get("originalTool") or {}
        entry = found.setdefault(fname, {"definition": integ, "actions": {}})
        entry["actions"][m.tool(nid).get("toolFunctionName") or m.label[nid]] = {
            "toolName": m.tool(nid).get("toolName"),
            "httpMethod": ot.get("httpMethod"),
            "url": ot.get("url"),
        }
    for fname, entry in found.items():
        path = SHARED_INTEGRATIONS / fname
        existing = json.loads(path.read_text()) if path.exists() else {}
        definition = {k: v for k, v in strip_volatile(entry["definition"]).items() if k != "actions"}
        actions = dict(existing.get("actionsUsed") or {})
        actions.update(entry["actions"])
        doc = {
            "_generated": "by scripts/export.py from agents/*/raw/nodes/*.json; credentials are {{SECRET:...}} placeholders",
            "definition": definition,
            "actionsUsed": actions,
        }
        write(path, dump_sorted(doc))


# --------------------------------------------------------------------------- #
# Repo-level files (built from every agents/*/export.json)
# --------------------------------------------------------------------------- #

def all_metas() -> List[Dict[str, Any]]:
    return sorted((json.loads(p.read_text()) for p in AGENTS_DIR.glob("*/export.json")),
                  key=lambda m: (m.get("agentName") or "").lower())


def write_root_readme(metas: List[Dict[str, Any]]) -> None:
    lines = ["# BeamAI workflows", "",
             "A version-controlled copy of our BeamAI agent workflows, and the spec for migrating off BeamAI.",
             "Generated by `scripts/export.py`. See `NOTES.md` for decisions and `inventory.md` for every agent in the workspace.", "",
             "## Agents", "",
             "| Agent | Folder | Agent ID | Status | Nodes | Last export |", "|---|---|---|---|---|---|"]
    for m in metas:
        lines.append(f"| {md_cell(m['agentName'])} | [agents/{m['folder']}/](agents/{m['folder']}/) | `{m['agentId']}` | "
                     f"{m['status']} | {m['nodeCount']} | {m['lastExported']} |")
    integ: Dict[str, List[str]] = {}
    for m in metas:
        for f in m.get("integrations") or {}:
            integ.setdefault(f, []).append(m["folder"])
    lines += ["", "## Shared integrations", "", "| Integration file | Used by |", "|---|---|"]
    for f in sorted(integ):
        lines.append(f"| [shared/integrations/{f}](shared/integrations/{f}) | {', '.join(f'`{x}`' for x in sorted(integ[f]))} |")
    lines += ["", "## Running the export", "", "```bash",
              "op run --env-file=.env.tpl -- .venv/bin/python scripts/export.py --agent <agentId>",
              "```", "",
              "Credentials come from 1Password. Never commit `.env`, `.env.tpl` or `discovery/`.", ""]
    write(ROOT / "README.md", "\n".join(lines))


def write_secrets_manifest(metas: List[Dict[str, Any]]) -> None:
    names: Dict[str, List[Tuple[str, List[str]]]] = {}
    for m in metas:
        for name, files in (m.get("secrets") or {}).items():
            names.setdefault(name, []).append((m["folder"], files))
    lines = ["# Secret placeholders used in this repository: names only, never values.",
             "# Real values live in 1Password or in the source systems.",
             "# Generated by scripts/export.py.", "secrets:"]
    for name in sorted(names):
        lines.append(f"  - name: {name}")
        lines.append(f"    placeholder: \"{{{{SECRET:{name}}}}}\"")
        lines.append("    used_by:")
        for folder, files in sorted(names[name]):
            lines.append(f"      - agent: {folder}")
            lines.append("        files:")
            lines += [f"          - \"{f}\"" for f in files]
    write(ROOT / "secrets.manifest.yaml", "\n".join(lines) + "\n")


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--agent", action="append", metavar="AGENT_ID", help="agent to export (repeatable)")
    g.add_argument("--all", action="store_true", help="export every agent in the workspace")
    args = ap.parse_args()

    client = BeamClient()
    agents = list_agents(client)
    folders = assign_folders(agents)
    ids = [a["id"] for a in agents] if args.all else args.agent
    unknown = [i for i in ids if i not in folders]
    if unknown:
        log.error("unknown agent id(s): %s", ", ".join(unknown))
        return 2
    today = dt.date.today().isoformat()
    failed = 0
    for agent_id in ids:
        try:
            export_agent(client, agent_id, folders[agent_id], today)
        except PersonalDataFound as exc:
            log.error("%s", exc)
            failed += 1
    metas = all_metas()
    write_root_readme(metas)
    write_secrets_manifest(metas)
    return 3 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
