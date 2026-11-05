# 33-slack-msg-not-paid: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `40b262be-33b7-4f65-8776-21e03cb06be3`<br>output `89443dd2-ac87-424b-94ce-4633066a4a75` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `2d4e9024-cf52-4e04-8327-0daea7db5c87`<br>output `724f5c20-95f4-4798-a6c0-cacc58a3dd09` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `8dadddaa-3095-46ae-b61b-9d48c12a4ba5`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `2ba70265-5287-46b7-9c7f-dac545121071`<br>output `01ed1fda-94ee-461d-b0fa-886d52bf769f` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `581a6e43-fcdc-4790-981d-353ccc1fa7cb`<br>output `93a93aaf-5c88-4fdd-8c57-e4f20904c626` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `e2a4804a-1e4e-4644-9e04-be78d649d677`<br>output `33fddae4-3c3b-42ea-976b-6e1693d6ad71` |
| 6 | `verification_output` | linked | yes | object |  | `12-verify-complete-payment.output.verification_output` | Linked upstream output | param `fc3fa816-00e2-473a-a67c-9b9e1226e53c`<br>output `61c905fe-6ca4-484f-a2aa-137b3ec10bcf` |
