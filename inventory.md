# BeamAI agent inventory

Pulled on 2026-11-05 from the enterprise workspace (`https://api.enterprise.beamstudio.ai`) with `GET /agent`. The workspace has 5 agents.

| Agent name | Agent ID | Type | Category | Graph status | Nodes | Edges | Node types | Folder |
|---|---|---|---|---|---|---|---|---|
| PRD_Betterment_AR_Agent_Inbound | `56180518-a836-4998-b63b-fefc179cd0b6` | pre-configured-agent | Blank Agent | draft (see note) | 41 | 38 | entry, execution, condition, looping | `prd-betterment-ar-agent-inbound` |
| PRD_Betterment_AR_Agent | `c8a3e542-cb80-4f89-b0ba-b64e685284d1` | pre-configured-agent | Blank Agent | draft (see note) | 14 | 13 | entry, execution, condition | `prd-betterment-ar-agent` |
| TST_Betterment AR Agent - Inbound | `ca09ff3c-4dc0-488d-9415-3b4666301e94` | pre-configured-agent | Blank Agent | draft (see note) | 41 | 38 | entry, execution, condition, looping | `tst-betterment-ar-agent-inbound` |
| TST_Betterment AR Agent | `a693caf9-5be5-4b81-87a6-0f2cecc0734f` | pre-configured-agent | Blank Agent | draft (see note) | 14 | 13 | entry, execution, condition | `tst-betterment-ar-agent` |
| TST_Betterment_AP_Agent_v2 | `f2bd02dc-6f1a-4f46-8f6e-7193ccadad4d` | pre-configured-agent | Finance & Accounting | draft (see note) | 20 | 20 | entry, execution, condition | `tst-betterment-ap-agent-v2` |

**Graph status note:** `GET /agent-graphs/{agentId}` returns the **draft** graph for every agent (`isDraft=true`, `isPublished=false`, `isActive=false`, `publishedAt=null`). No read endpoint lists an agent's graph versions, so we can't get a published graph's ID to request it with `?graphId=`. See the gap report and NOTES.md.

**Folder names** follow the folder rules: lowercase, with runs of spaces and symbols replaced by a single hyphen. No two agents get the same folder name, so none need the ID suffix.

**None of these agents is named "dunning".** Which agent is the dunning agent is an open question in NOTES.md.
