# 14-code-executor: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `decision_single` | linked |  | object |  | `11-code-executor.output.decision` |  | param `28b4cb34-1b25-443d-9756-50038e5c2b91`<br>output `1b3cea80-7730-4314-bbfd-5771b05387a7` |
| 1 | `decision_multi` | linked |  | object |  | `12-score-the-open-pos.output.decision` |  | param `683736ce-fb4e-492a-9d25-5bb0734a0ff6`<br>output `974f00dc-f68e-4acf-b090-e68319a09fa2` |
| 2 | `open_pos` | linked | yes | object |  | `05-code-executor.output.open_pos` |  | param `75736e8d-9334-4c22-a44a-5940aafb6e11`<br>output `7b66bb2d-287b-4fe6-a7f0-d92736758cfc` |
| 3 | `invoice` | linked | yes | object |  | `01-trigger.output.invoice` |  | param `4f3b4bed-1595-4ccf-b4dc-db023ea81742`<br>output `260bab81-bfe0-4407-9b18-0977c083bed0` |
| 4 | `holidays` | static |  | string | ["2026-01-01", "2026-01-19", "2026-02-16", "2026-05-25", "2026-06-19", "2026-07-03", "2026-09-07", "2026-10-12", "2026-11-11", "2026-11-26", "2026-12-25", "2027-01-01", "2027-01-18", "2027-02-15", "2027-05-31", "2027-06-18", "2027-07-05", "2027-09-06", "2027-10-11", "2027-11-11", "2027-11-25", "2027-12-24", "2027-12-31"] |  | Business-day calendar. Default: US federal holidays. Betterment must approve it (O9). | param `72a825ed-dc77-408e-ad99-ed8071e2ec24` |
| 5 | `prepaid_threshold` | static |  | number | 10000 |  | Rule P4: total from which a long service period is a prepaid | param `413d495f-9170-4f82-b247-88b9fd0c2e37` |
