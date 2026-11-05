# 23-note-msg-nothing-paid: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `42eeb175-fea3-465d-a7cf-bf725556c60b`<br>output `7d2c43a3-977e-4168-8b58-2b7d90e4165b` |
| 1 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `4e384927-2032-4837-9bbc-65f0d281d96f`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
| 2 | `verification_output` | linked | yes | object |  | `12-verify-partial-payment.output.verification_output` | Linked upstream output | param `459d4c71-683e-4cfc-b6c9-4b457194271d`<br>output `0aefe64b-ae11-439e-801e-b8f512f63c2a` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `2fbdffbf-404b-4117-95f0-64b2146407a3`<br>output `fa9553fb-d222-4709-9438-47371969eea6` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `3658ad9b-cc87-4c96-a725-ffb2fb614c77`<br>output `e2edd3c2-6437-4ca3-aa38-a3d06241e90b` |
| 5 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `f1ad37f3-20ea-482d-bda5-9c14e46839f0`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
| 6 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `549d86a5-8664-4fe8-a487-82a06e5f89de`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
