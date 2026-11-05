# 31-slack-msg-not-paid: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `3082b865-e5b2-44b8-a5d6-5e5a6cebd85e`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `712c1c70-41ec-4946-a13f-d59ad6b6dfff`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `d04b8cf3-3599-4199-ab07-76b4667d14a3`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `3526296f-ca35-41d0-9af2-0c7ca0c64c9b`<br>output `fa9553fb-d222-4709-9438-47371969eea6` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `f59b684a-f5dd-430d-9952-3fdd02eeb725`<br>output `e2edd3c2-6437-4ca3-aa38-a3d06241e90b` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `814304b5-05e2-48c9-8629-dfb21669f019`<br>output `7d2c43a3-977e-4168-8b58-2b7d90e4165b` |
| 6 | `verification_output` | linked | yes | object |  | `10-verify-complete-payment.output.verification_output` | Linked upstream output | param `32a8301f-31ec-43c0-be12-4855fd1b32c5`<br>output `d85e2f99-41b5-44d8-ae6b-cd9fc32cc79e` |
