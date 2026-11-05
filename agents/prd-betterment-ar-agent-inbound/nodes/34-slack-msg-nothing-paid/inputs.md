# 34-slack-msg-nothing-paid: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `fb059d64-e281-4947-9dff-c28b7c741f82`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `28c31b68-11d8-4f9e-b229-8282f3b3bbb0`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `6adfbad3-b06e-4bb0-a983-30b0ee0d8aee`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `9a7e4f3e-f3c2-45bd-9579-5cd09367e866`<br>output `fa9553fb-d222-4709-9438-47371969eea6` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `c350eb8f-2f05-427e-bb23-d743628b0e71`<br>output `e2edd3c2-6437-4ca3-aa38-a3d06241e90b` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `48155035-32ce-4cad-905f-17e962187e50`<br>output `7d2c43a3-977e-4168-8b58-2b7d90e4165b` |
| 6 | `verification_output` | linked | yes | object |  | `12-verify-partial-payment.output.verification_output` | Linked upstream output | param `df423635-76e2-4931-b549-01ecaad712d8`<br>output `0aefe64b-ae11-439e-801e-b8f512f63c2a` |
