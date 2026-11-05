# 18-code-executor: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `decision` | linked | yes | object |  | `14-code-executor.output.decision` |  | param `e7badd3a-cc98-452f-af91-5b303e1fb9f6`<br>output `6e58df4c-7e90-4091-8568-82e9870649ec` |
| 1 | `bill` | linked | yes | object |  | `14-code-executor.output.bill` |  | param `17345f1d-ed48-4816-b814-180a555ffd23`<br>output `f64750fb-f35e-44ba-8bf0-f471e9d57392` |
| 2 | `invoice_id` | linked |  | string |  | `01-trigger.output.invoice_id` |  | param `9ac7f097-e10d-4e48-91e2-cc3b9be99f80`<br>output `dbb84095-2c3f-43cd-bfba-533e1ff22784` |
| 3 | `write_enabled` | static |  | boolean | false |  | Write switch. Keep false until Phase 2 (D3, O10). | param `9b09a8ba-b6f4-4f35-b70b-22b9e7b4def0` |
