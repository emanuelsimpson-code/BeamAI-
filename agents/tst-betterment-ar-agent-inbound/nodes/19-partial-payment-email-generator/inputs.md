# 19-partial-payment-email-generator: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `invoices_outstanding` | ai_fill | yes | string |  |  | Verify node: array of  outstanding invoice objects:                                                               <br>         id: Stripe invoice ID                  <br>         amount_remaining:  dollars (already converted)   | param `ca2c8be2-4d9f-4f36-a62f-a18facf9ef80` |
| 1 | `invoice_count_outstanding` | ai_fill | yes | string |  |  | Verify node: number of invoices still open | param `c73cbab3-c3a9-4f8c-8f65-2d03bfbfb391` |
| 2 | `total_amount_remaining` | ai_fill | yes | string |  |  | Verify node: sum of all outstanding invoices in dollars  | param `575c8c20-52ba-43f1-b665-fb425a6daaaf` |
| 3 | `total_amount_paid` | ai_fill | yes | string |  |  | Verify node: sum of all paid invoices in dollars | param `4fddde0d-311b-4c91-be9b-5c74395b60ae` |
| 4 | `requester_name` | linked | yes | string |  | `01-trigger.output.requester_email` | client name from the task query | param `d0991f92-5e9e-40c7-9b62-f6ac9668d749`<br>output `724f5c20-95f4-4798-a6c0-cacc58a3dd09` |
