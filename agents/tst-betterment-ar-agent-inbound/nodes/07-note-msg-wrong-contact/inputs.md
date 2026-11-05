# 07-note-msg-wrong-contact: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `da2918b1-77fb-4ff3-a7dc-620e4241591d`<br>output `93a93aaf-5c88-4fdd-8c57-e4f20904c626` |
| 1 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `4b746c54-068e-4319-8483-d891b95a7e00`<br>output `33fddae4-3c3b-42ea-976b-6e1693d6ad71` |
| 2 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `d6e73750-74c5-4abf-bbc2-a8e93bcdc032`<br>output `724f5c20-95f4-4798-a6c0-cacc58a3dd09` |
| 3 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `9776922f-b076-4b0e-bd1b-d24cc7554d92`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 4 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `9cb8d913-905a-45a1-958d-a0f60307ef79`<br>output `01ed1fda-94ee-461d-b0fa-886d52bf769f` |
| 5 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `2e248240-0025-45c0-9cf7-b39987b3b346`<br>output `89443dd2-ac87-424b-94ce-4633066a4a75` |
