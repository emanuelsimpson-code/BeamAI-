# 12-score-the-open-pos: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `invoice` | linked | yes | object |  | `01-trigger.output.invoice` |  | param `9b3685b7-6503-484d-bb5e-bfc64a346da5`<br>output `260bab81-bfe0-4407-9b18-0977c083bed0` |
| 1 | `open_pos` | linked | yes | object |  | `05-code-executor.output.open_pos` |  | param `eab38a2e-fff3-444f-a330-d20d945c0c92`<br>output `7b66bb2d-287b-4fe6-a7f0-d92736758cfc` |
| 2 | `requester_history` | linked |  | object |  | `05-code-executor.output.requester_history` |  | param `67736b50-8d83-4a03-92f4-31d8cbea0c49`<br>output `7999c5b8-b2d5-40ea-a40d-bf0cbc42ebe2` |
| 3 | `zip_suggested_po` | linked |  | string |  | `05-code-executor.output.zip_suggested_po` |  | param `958cc98a-e7be-480e-95df-cb8969a1e58e`<br>output `e6d080ca-a0c8-45ae-84fd-4c5291d2c875` |
| 4 | `vendor_rules` | linked |  | string |  | `08-read-the-vendor-rules.output.vendor_rules` |  | param `11a87568-1f92-4801-be75-ac920e9f6e66`<br>output `1acf5293-81ba-4856-ad17-6b62450b8126` |
| 5 | `printed_po_number` | linked |  | string |  | `01-trigger.output.printed_po_number` |  | param `c5edd5a1-dcc7-4e99-897f-eddddeebe406`<br>output `ce4df05a-823d-4364-96d6-ab8f7f474c4a` |
| 6 | `printed_po_reliable` | linked |  | boolean |  | `08-read-the-vendor-rules.output.printed_po_reliable` |  | param `96ead0b0-0504-4aca-b68e-a9723a82717b`<br>output `edf70983-5116-4f4b-ad9d-da5d66ee4e25` |
