# 13-slack-msg-dispute: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `67aa47f7-dfbd-460f-99de-6eb5b8891c99`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `391937e5-47b6-41e8-941c-f5928f394f3a`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `a1b6925e-4f17-41fe-8d29-fb7b3fed09f9`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `76c14450-c6f1-4e68-99e1-cd925adc26b7`<br>output `fa9553fb-d222-4709-9438-47371969eea6` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `913ff774-3286-4871-bc97-f59ca18266ff`<br>output `e2edd3c2-6437-4ca3-aa38-a3d06241e90b` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `27ebf1d4-8ea6-4cb0-9325-f1e27a70b93c`<br>output `7d2c43a3-977e-4168-8b58-2b7d90e4165b` |
