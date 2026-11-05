# Notes: decisions and open questions

## Decisions

- **2026-11-05: Python runs in `.venv/`.** The system Python is 3.9.6 and doesn't have `requests`. `.venv/` and `__pycache__/` are in `.gitignore`.
- **2026-11-05: Discovery uses `scripts/discover.py` and `scripts/beam_safety.py`.** They're separate from `scripts/export.py`, which comes in Phase 2.
  - `beam_safety.BeamClient` sends only GET requests, and only to these endpoints: `/agent`, `/agent-graphs/{agentId}`, `/agent-graphs/{agentId}/nodes/lite`, `/agent-graphs/{agentId}/nodes/{nodeId}` and `/custom-tool/preferred-models`. Any other path is refused before a request is made.
  - Before anything is written, credential-like keys (including the whole `customAuthParameters` subtree) and known token formats (Stripe, Slack, GitHub, AWS, JWT, Bearer/Basic, private keys, credentials in URLs) are replaced with `{{SECRET:<name>}}`. The exact API key and workspace ID values are also replaced wherever they appear.
  - The responses are checked for personal data: emails, phone numbers, SSN-like and IBAN-like strings, card numbers that pass the Luhn check, and Stripe `cus_`/`pm_`/`card_`/`acct_` IDs. If anything is found, nothing is written. The script prints only the JSON path and the kind of data, never the value.
  - It can't reliably detect people's names. Those need a manual check.
- **The workspace ID is treated as a secret.** It comes from 1Password, so responses show `{{SECRET:beam_workspace_id}}` instead of the real value.

## Confirmed from the docs and OpenAPI spec (docs.beam.ai, 2026-11-05)

- Base URL: `https://api.beamstudio.ai`. Authentication is the `x-api-key` header, and most endpoints also need `current-workspace-id`.
- `GET /agent`: list agents. Paginated with `pageNum` and `pageSize` (100 at most). Optional filters: `type` (`beam-os`, `user-agent` or `pre-configured-agent`), `searchQuery` and `agentCategoryId`.
- `GET /agent-graphs/{agentId}`: the full graph. Optional `graphId`.
- `GET /agent-graphs/{agentId}/nodes/lite`: the graph ID and its nodes, without configuration.
- `GET /agent-graphs/{agentId}/nodes/{nodeId}`: node detail. According to the spec, it adds `inputParamsData` (with `linkParams`), `originalTool.httpMethod`/`bodyParams`, and `integration.actions`.
- **There's no trigger endpoint.** The docs say triggers are set up on the Trigger node in the Flow. The spec only shows trigger filter groups in `nodeConfigurations.conditions` (`AgentTriggerConfigurationFiltersGroup`).
- **There's no node-level `prompt` field in either GET schema.** Only `originalTool.prompt` and the node `objective` are documented, and `PATCH .../prompt` writes a `prompt`. We need to check whether the live responses include it.

- **2026-11-05: The API host is `https://api.enterprise.beamstudio.ai`.** Our workspace is on the enterprise instance (`app.enterprise.beam.ai`). The workspace key returns 401 on `api.beamstudio.ai` and 200 on the enterprise host. This host isn't in the public docs, and you approved it. `beam_safety.py` accepts only these two hosts. The default is the enterprise one, and `BEAM_BASE_URL` overrides it.
- **2026-11-05: The personal-data detector ignores UUIDs, hex IDs and epoch-millisecond timestamps** before checking for card, phone and SSN patterns. The first run flagged UUID digit runs as card numbers. Emails are grouped as Betterment, example/test, or other domain.
- **`discover.py pull --scan-only` fetches and scans without writing.** It prints counts by field, never values.

## Phase 2 decisions (2026-11-05)

- **PRD_Betterment_AR_Agent is the dunning agent.** Its Code Executor sets the dunning stage (`reminder_count`: 0 = first notice, 1 = second, 2 = final), and Generate Email writes the reminder. PRD_Betterment_AR_Agent_Inbound handles customer replies to those emails; it's started by a webhook.
- **Node folder names come from `toolConfiguration.toolName`, not `customId`.** In this workspace `customId` is a UUID. The UUID is kept in `node.json`. Nodes without a tool are named by type: `trigger`, `condition`, `end`, `loop`, `wait`.
- **Execution order** is breadth-first from the entry node, following `childEdges` in API order. Any unreachable nodes go last, sorted by name.
- **Readable IDs:** wherever a value in `node.json` is a known internal ID (node, `customId`, tool config, input or output param, edge), a `<key>__readable` partner key is added next to it, for example `linkParamOutputId__readable: "04-code-executor.output.invoices"`.
- **`node.json` is built from the node-detail response**, plus the fields only the graph response has (`conditionGroups`, `linkedOutputParamRules`, `description`, `iconSrc`). `agentGraph`, the agent-level duplicate, is dropped; agent settings are in the agent README. Timestamps and coordinates are removed.
- **Integrations** are written once to `shared/integrations/<integration-name>.json`, and nodes point to them with `$ref`. `actionsUsed` keeps actions from other agents when a single agent is re-exported. Actions an agent no longer uses aren't removed automatically yet.
- **"Last export" changes only when `raw/` changes.** `export.json` stores a SHA-256 of `raw/`, so re-running with no BeamAI changes produces no diff.
- **Root `README.md` replaces GitHub's initial README** ("# BeamAI- / Workflow documentation for agent"). It's rebuilt from `agents/*/export.json` on every run.
- **Secret scan:** the local git hook `.git/hooks/pre-commit` runs `gitleaks git --pre-commit --staged` and blocks a commit on any finding. It isn't committed, so each clone needs to install it. The only finding in the folder is the `your-api-key-here` example in gitignored `discovery/docs/authentication.md`.
- **Validation:** `scripts/validate.py agents/<folder>` checks node and edge counts, code and prompt presence, and linked inputs against `raw/`, offline.
- **Trigger configuration:** not available from the API. Copy it from the Beam UI into this file (the trigger type, Stripe event and filters for the outbound agent).

## Phase 3 decisions (2026-11-05)

- **All 5 agents are exported** with `scripts/export.py --all`. The pilot folder came out unchanged.
- **Beam rate-limits node-detail requests** (HTTP 429) when exporting many agents in a row. `BeamClient` retries with backoff (1, 2, 4 and 8 s), and every request succeeded.
- **The personal-data check skips long digit runs in an ID parameter's `staticValue`** when the value is only digits and the parameter name ends in `id`. This is the 14-digit Zendesk `ticket.ticket_form_id` on TST_Betterment AR Agent's Create Ticket node. Emails and Stripe IDs are still checked in those values.
- **New shared integrations:** `stripe-sandbox.json` (used by the AR Inbound agents' Fetch Invoice node: `GET https://api.stripe.com/v1/invoices/{{invoice_id}}`), `salesforce-custom.json` and `zendesk-custom.json` (used by the TST agents).
- **Your decision: keep the encrypted credential fields as is.** Beam stores `provider.credentials.user` and `authenticationMeta.clientId` as long encrypted hex strings:
  - Zendesk `user`: 96 hex characters.
  - Salesforce `clientId`: 192 hex characters.
  - Stripe Sandbox `user`: 224 hex characters. With Stripe's basic auth this is most likely the encrypted API key.

  They aren't readable without Beam's encryption key and stay in the repo unredacted. The paired `password` and `clientSecret` remain placeholders. This replaces the earlier description of these fields as "an email/username" and "a consumer key".
- **Loop nodes:** `nodeConfigurations.linkedVariableId` is the list the loop iterates over (for example `02-extract-invoice-context.output.invoice_ids`), and `alias` is the loop's label. The README node table says what each loop iterates over.

## Resolved

- ~~401 "Invalid API key"~~: caused by calling the wrong host (see above).
- **2026-11-05, your answers:**
  - **Q2:** PRD_Betterment_AR_Agent_Inbound runs when a customer replies to the outbound email sent by **PRD_Betterment_AR_Agent**. It's started by an API webhook trigger on its entry node. The API doesn't return that webhook configuration (gap report, Trigger row).
  - **Q3:** Keep the Betterment email addresses in prompts, as part of the workflow logic.
  - **Q4:** The draft graph is what's running in production. Exporting the default (draft) graph is correct.
  - **Q1:** Keep the shape of `outputExample`, drop its values. `beam_safety.redact_samples` replaces every `outputExample` with a skeleton of type names (`<string>`, `<number>`, `<boolean>`). JSON strings stay JSON strings, and arrays keep one element. So `raw/` is "an exact copy, minus credentials and sample values".
  - **Pilot agent:** PRD_Betterment_AR_Agent (`c8a3e542-cb80-4f89-b0ba-b64e685284d1`), the outbound email agent. Its folder follows the folder rules: `agents/prd-betterment-ar-agent/`.
- **2026-11-05, your decision: keep the Salesforce `authenticationMeta.clientId` and the Zendesk `provider.credentials.user` unredacted.** They're identifiers, not secrets. The paired `clientSecret` and `password` stay replaced with placeholders. The placeholder names stay as generated (`custom_client_secret`, `custom_password`).
- **2026-11-05: The personal-data check ignores numbers written as `id: <digits>`.** The only remaining hits were two 14-digit Zendesk custom field IDs (in the code node and the CreateTicket payload). They're configuration, not customer data.
- **2026-11-05: The outbound agent's graph is saved in `discovery/prd-betterment-ar-agent/`.** That's 17 files: the graph, lite, 14 node details, preferred models and the placeholder list. gitleaks 8.30.1 found no leaks.

## Open questions

Questions 1–4 below were answered on 2026-11-05 (see Resolved). Question 5 is still open: the API doesn't return the trigger configuration. For now, Phase 2 will note in the agent README that it isn't exported.

### Original list

1. **Which agent is the dunning agent?** None of the 5 agents is named "dunning", and PRD_Betterment_AR_Agent_Inbound doesn't match the brief:
   - It has no Stripe trigger. The entry node is an LLM tool with no trigger configuration.
   - It has no code nodes.
   - It reads and replies to tickets, which points to inbound customer email.

   PRD_Betterment_AR_Agent (14 nodes) may be the outbound dunning flow. Also, should the folder be `dunning-agent` as in the layout, or `prd-betterment-ar-agent-inbound` as the folder rules give?
2. **`outputExample` contains customer data.** These are sample values Beam captured from runs, and they include emails, Stripe customer IDs and phone numbers. Options:
   - **(a) Recommended:** before writing anything, replace every `outputExample` value with a type-only skeleton that keeps keys and data types and drops the values. `raw/` would then be "exact copy, minus credentials and sample data".
   - (b) Drop `outputExample` entirely.
   - (c) Remove only the detected values. Not recommended: names can't be detected.
3. **Betterment email addresses in 6 prompts.** Keep them (they're probably team mailboxes, and part of the workflow logic) or replace them with placeholders?
4. **Published graph.** The API returns only the draft graph, and no read endpoint gives the published graph's ID. Is the draft what's live? If not, can someone copy the published graph ID from the Beam UI (version history)? `?graphId=` would then fetch it.
5. **Trigger configuration isn't in the API.** For the agent that is Stripe-triggered, we'll need to record the trigger (provider, event, filters) by hand from the UI in NOTES, or ask Beam support for an endpoint.
