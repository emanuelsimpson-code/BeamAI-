# 02-classify-the-document: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `document_text` | linked |  | string |  | `01-trigger.output.document_text` |  | param `4ce71218-9bb9-4725-9779-470a283d799c`<br>output `3b27945b-8167-4c57-a4aa-87cdbdf01a08` |
| 1 | `invoice` | linked | yes | object |  | `01-trigger.output.invoice` |  | param `9ca9ace1-c706-41a2-b075-8e94dc28ccfa`<br>output `260bab81-bfe0-4407-9b18-0977c083bed0` |
| 2 | `vendor_name` | linked | yes | string |  | `01-trigger.output.vendor_name` |  | param `c7d599a6-7fcc-46ae-8604-4d74a760153f`<br>output `52313821-47a3-4a8e-899c-f3e18ddd0294` |
| 3 | `vendor_id` | linked |  | string |  | `01-trigger.output.vendor_id` |  | param `f53883ef-ba37-4bf0-bbfb-edc813de1cc7`<br>output `ee8af913-9b76-4fa6-8cac-6cb6ea3cc903` |
| 4 | `zip_url` | linked |  | string |  | `01-trigger.output.zip_url` |  | param `5f4766a3-9617-46c3-984c-cb03523ab0e9`<br>output `d047adb0-383e-44e5-8601-b33c56c3de38` |
