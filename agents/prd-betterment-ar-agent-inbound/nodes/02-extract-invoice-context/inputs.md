# 02-extract-invoice-context: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_data` | linked | yes | string |  | `01-trigger.output.all_comments` | the entire email received in the payload | param `e2d58579-5bb0-4ef7-8e05-b98c356a7f12`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
| 1 | `stripe_invoice_ids` | linked | yes | string |  | `01-trigger.output.stripe_invoice_id` | The stripe_invoice_ids coming from the task query | param `6cbd4dd3-030e-4f8b-b133-e74387fd9340`<br>output `20846bbb-ad5a-487f-b1d0-458e8639c827` |
