# 07-note-msg-wrong-contact: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `cac278d9-1941-4eaf-a631-68cd244cf3d6`<br>output `e2edd3c2-6437-4ca3-aa38-a3d06241e90b` |
| 1 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `ca21dbd9-2581-4357-bd4e-c6d783c514ac`<br>output `fa9553fb-d222-4709-9438-47371969eea6` |
| 2 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `0a63875d-6c69-49d7-9ab9-94ff6f786c35`<br>output `7d2c43a3-977e-4168-8b58-2b7d90e4165b` |
| 3 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `14cab5c4-8fd0-4f27-827d-fa79fb2d14c8`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 4 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `6612d1ad-5386-4581-9b74-686f9049c4cd`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
| 5 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `cd66c015-8feb-4259-afcf-682a1c500a92`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
