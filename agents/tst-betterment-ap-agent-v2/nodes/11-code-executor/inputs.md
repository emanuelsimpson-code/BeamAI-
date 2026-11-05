# 11-code-executor: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `open_pos` | linked | yes | object |  | `05-code-executor.output.open_pos` |  | param `82d9823f-d949-47e0-a823-e324140c03ae`<br>output `7b66bb2d-287b-4fe6-a7f0-d92736758cfc` |
| 1 | `invoice` | linked | yes | object |  | `01-trigger.output.invoice` |  | param `22cda067-fa8c-4a50-84ed-060c3e20e231`<br>output `260bab81-bfe0-4407-9b18-0977c083bed0` |
| 2 | `subsidiary` | linked |  | string |  | `01-trigger.output.subsidiary` |  | param `8ee462c4-f0c9-4f90-b70f-309ec4de9b9a`<br>output `747cfe6e-729e-46e7-b35e-9842eb22c940` |
| 3 | `printed_po_number` | linked |  | string |  | `01-trigger.output.printed_po_number` |  | param `31975bc4-ba4b-4efc-a8e6-8d108288d19d`<br>output `ce4df05a-823d-4364-96d6-ab8f7f474c4a` |
| 4 | `printed_po_reliable` | linked |  | boolean |  | `08-read-the-vendor-rules.output.printed_po_reliable` |  | param `56acbc6a-fd52-41b6-b738-0f7d626b6224`<br>output `edf70983-5116-4f4b-ad9d-da5d66ee4e25` |
