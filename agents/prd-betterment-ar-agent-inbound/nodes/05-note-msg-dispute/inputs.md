# 05-note-msg-dispute: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `c45159ae-fc76-4af5-999e-036c103edd01`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `b29b80e8-9886-4478-87f1-3485b583dd95`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `2b9a9409-91b1-4e11-9678-82141029477b`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `b7a474ab-ebe3-40c4-beb3-56841fdc0416`<br>output `fa9553fb-d222-4709-9438-47371969eea6` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `9a54a425-89bd-469f-b6fb-14a1c34d6299`<br>output `e2edd3c2-6437-4ca3-aa38-a3d06241e90b` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `413def91-fff7-482b-8c5a-031be8dfddfb`<br>output `7d2c43a3-977e-4168-8b58-2b7d90e4165b` |
