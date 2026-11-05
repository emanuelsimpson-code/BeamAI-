# 33-slack-msg-partial-verified: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `verification_output` | linked | yes | object |  | `12-verify-partial-payment.output.verification_output` | Linked upstream output | param `f34773d8-cb24-4f55-ac5f-f197cf0c594a`<br>output `0aefe64b-ae11-439e-801e-b8f512f63c2a` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `a8a90f5d-700e-4dbd-a554-1f6acd7d074a`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
| 2 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `0be8257b-27a7-4103-a5bf-d69c8e5e602d`<br>output `fa9553fb-d222-4709-9438-47371969eea6` |
| 3 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `9459f314-a5b5-4720-b3ad-fb6ddcd067a5`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 4 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `fa663d04-af9b-4cb0-bb28-eeef8d2b56ee`<br>output `7d2c43a3-977e-4168-8b58-2b7d90e4165b` |
| 5 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `d88b9411-cc58-49cb-9c71-609f6df5b46d`<br>output `e2edd3c2-6437-4ca3-aa38-a3d06241e90b` |
| 6 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `5427863d-6a11-47f9-a719-010c091146c3`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
