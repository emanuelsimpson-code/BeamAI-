# 22-partial-payment-email-generator: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `invoices_outstanding` | ai_fill | yes | string |  |  | Verify node: array of  outstanding invoice objects:                                                               <br>         id: Stripe invoice ID                  <br>         amount_remaining:  dollars (already converted)   | param `c284c59a-4778-4000-8aa4-2be37b93be2b` |
| 1 | `invoice_count_outstanding` | ai_fill | yes | string |  |  | Verify node: number of invoices still open | param `33b346c8-f5e9-4e43-aac8-b1bbdd263681` |
| 2 | `total_amount_remaining` | ai_fill | yes | string |  |  | Verify node: sum of all outstanding invoices in dollars  | param `15df2610-e423-4768-99eb-e0c71b7718c9` |
| 3 | `total_amount_paid` | ai_fill | yes | string |  |  | Verify node: sum of all paid invoices in dollars | param `0c0ae5ca-4d85-48cc-80d4-71fc6b1954c7` |
| 4 | `requester_name` | linked | yes | string |  | `01-trigger.output.requester_email` | client name from the task query | param `5ea429ce-f7dc-4742-a7b7-6d3dc5b04c2c`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
