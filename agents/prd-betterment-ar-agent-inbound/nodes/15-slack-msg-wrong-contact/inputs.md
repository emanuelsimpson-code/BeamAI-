# 15-slack-msg-wrong-contact: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `6de2592f-d791-4f35-9e43-b5a7992637a7`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `6233a28f-5446-481e-83c9-92b51b74503f`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
| 2 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `bf485cf1-a0d4-4415-b986-3c9bbc091f50`<br>output `e2edd3c2-6437-4ca3-aa38-a3d06241e90b` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `95a24b9d-42bc-4bf6-b6bf-60bd18b9362e`<br>output `fa9553fb-d222-4709-9438-47371969eea6` |
| 4 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `99b68952-f384-4077-962c-0da9dcd0a356`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `e89d9a92-2f22-4b0b-9444-526f2bdb991f`<br>output `7d2c43a3-977e-4168-8b58-2b7d90e4165b` |
