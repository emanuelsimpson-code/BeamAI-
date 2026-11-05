# 13-slack-msg-dispute: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `d12d4dc7-f184-4489-98de-5ebb3268bbab`<br>output `89443dd2-ac87-424b-94ce-4633066a4a75` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `236d129d-db6e-4334-b506-f3bfed91c67e`<br>output `724f5c20-95f4-4798-a6c0-cacc58a3dd09` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `d5e2a9e1-1c5f-4b6e-a47e-bd227391f213`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `88bbe448-8379-40e6-ae10-30b4a2affe13`<br>output `01ed1fda-94ee-461d-b0fa-886d52bf769f` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `574e9993-1d55-4a04-9efb-a2ee37f648c6`<br>output `93a93aaf-5c88-4fdd-8c57-e4f20904c626` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `1b7f3ec3-a972-4dda-8508-eb2aee462808`<br>output `33fddae4-3c3b-42ea-976b-6e1693d6ad71` |
