# 03-intent-classifier: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` |  | param `8c4ae978-4ced-4414-8e2a-d5f8a408af6e`<br>output `93a93aaf-5c88-4fdd-8c57-e4f20904c626` |
| 1 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | the entire email body received from the trigger | param `846852da-550b-4f3d-af94-d29c6ac43ca0`<br>output `89443dd2-ac87-424b-94ce-4633066a4a75` |
