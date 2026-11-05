# 15-code-executor: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `decision` | linked | yes | object |  | `14-code-executor.output.decision` |  | param `9df0cb1e-ddb2-41cf-b108-ad6ab19f742e`<br>output `6e58df4c-7e90-4091-8568-82e9870649ec` |
| 1 | `bill` | linked | yes | object |  | `14-code-executor.output.bill` |  | param `8851a206-d4d1-4062-82c4-69b75e37cb9a`<br>output `f64750fb-f35e-44ba-8bf0-f471e9d57392` |
| 2 | `open_pos` | linked | yes | object |  | `05-code-executor.output.open_pos` |  | param `ffdae0e9-296c-41f1-aa0e-c1d5367f6da5`<br>output `7b66bb2d-287b-4fe6-a7f0-d92736758cfc` |
| 3 | `invoice` | linked | yes | object |  | `01-trigger.output.invoice` |  | param `43c2bec2-b68e-448b-be43-daf471f75f59`<br>output `260bab81-bfe0-4407-9b18-0977c083bed0` |
| 4 | `invoice_id` | linked |  | string |  | `01-trigger.output.invoice_id` |  | param `b7c67731-eb6b-49e6-8182-cd862b16ee06`<br>output `dbb84095-2c3f-43cd-bfba-533e1ff22784` |
| 5 | `vendor_id` | linked |  | string |  | `01-trigger.output.vendor_id` |  | param `117095ec-3f09-47a5-8da4-6a5604b6a32b`<br>output `ee8af913-9b76-4fa6-8cac-6cb6ea3cc903` |
| 6 | `vendor_name` | linked | yes | string |  | `01-trigger.output.vendor_name` |  | param `8720924c-266b-4ecf-b0f0-a42829f5de67`<br>output `52313821-47a3-4a8e-899c-f3e18ddd0294` |
| 7 | `subsidiary` | linked |  | string |  | `01-trigger.output.subsidiary` |  | param `d9f89291-12b6-4b7b-81a9-e87a3c745dd9`<br>output `747cfe6e-729e-46e7-b35e-9842eb22c940` |
| 8 | `printed_po_number` | linked |  | string |  | `01-trigger.output.printed_po_number` |  | param `88948d14-bd1f-4a39-9519-93a223e2812f`<br>output `ce4df05a-823d-4364-96d6-ab8f7f474c4a` |
| 9 | `requires_printed_po` | linked |  | boolean |  | `08-read-the-vendor-rules.output.requires_printed_po` |  | param `e210d5af-f2fe-474e-87b5-8e06aecfd18a`<br>output `94708c11-d4e6-405a-9a0a-41e77f7be123` |
| 10 | `printed_po_reliable` | linked |  | boolean |  | `08-read-the-vendor-rules.output.printed_po_reliable` |  | param `c8bfc063-bdd9-4ce3-8521-28b5d9b761e3`<br>output `edf70983-5116-4f4b-ad9d-da5d66ee4e25` |
| 11 | `prepaid_candidate` | linked |  | boolean |  | `14-code-executor.output.prepaid_candidate` |  | param `e2a15b58-a877-43a6-a674-d342321988a1`<br>output `452d3c90-77b6-4a40-96d9-52007ed79fa1` |
| 12 | `unmapped_lines` | linked |  | string |  | `14-code-executor.output.unmapped_lines` |  | param `ba209067-83bb-49e3-b87f-c211569b03c9`<br>output `d8fd8401-1c67-4609-9252-6298f4bc5b10` |
| 13 | `tolerance` | static |  | number | 0 |  | Rule H3: amount by which the invoice can exceed the PO balance | param `9dac2e83-ead8-451b-b79f-86bc34b0e680` |
