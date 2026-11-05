# 30-slack-msg-partial: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `49cbdb0d-3446-4a39-ae2d-62c48a495dfd`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `043b6f07-b6bd-45b9-8683-d17e7d2aae79`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `2087593d-0a56-4de4-9c2c-7b7b998e6823`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `9ad4e566-6da8-4158-a9f4-c7dcf14f94f3`<br>output `fa9553fb-d222-4709-9438-47371969eea6` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `899aacf5-35d4-47ef-8fda-3898f216af93`<br>output `e2edd3c2-6437-4ca3-aa38-a3d06241e90b` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `b15a500c-c772-4910-8fc4-c9c58765b21e`<br>output `7d2c43a3-977e-4168-8b58-2b7d90e4165b` |
| 6 | `verification_output` | linked | yes | object |  | `10-verify-complete-payment.output.verification_output` | Linked upstream output | param `69e38230-da44-4cfa-a596-1f578e0e664c`<br>output `d85e2f99-41b5-44d8-ae6b-cd9fc32cc79e` |
