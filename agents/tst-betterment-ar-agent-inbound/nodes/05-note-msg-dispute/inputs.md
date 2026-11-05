# 05-note-msg-dispute: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `1ce7fccc-42b2-4a91-8a53-3a853457c314`<br>output `89443dd2-ac87-424b-94ce-4633066a4a75` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `db550fd4-dc39-48d5-8a1c-2cc1aba2692b`<br>output `724f5c20-95f4-4798-a6c0-cacc58a3dd09` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `7ea3de87-16ae-4061-a445-df4275b3a12a`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `9c880a52-f70e-4403-a35b-34c1e3d7f692`<br>output `01ed1fda-94ee-461d-b0fa-886d52bf769f` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `731cb81e-7cee-4ff2-bce7-5d4cc84f09a3`<br>output `93a93aaf-5c88-4fdd-8c57-e4f20904c626` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `ad381cc1-5c8d-4077-928e-5c6c68e9912a`<br>output `33fddae4-3c3b-42ea-976b-6e1693d6ad71` |
