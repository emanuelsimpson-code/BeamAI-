# 03-intent-classifier: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` |  | param `d2a751cc-1839-4dfa-a624-2607c5a37f28`<br>output `e2edd3c2-6437-4ca3-aa38-a3d06241e90b` |
| 1 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | the entire email body received from the trigger | param `6e344d23-ff2b-4f79-9e8d-1e88358924c2`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
