# 30-slack-msg-nothing-paid: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `1a1b27eb-4f93-4651-81a9-5556d3470cb8`<br>output `89443dd2-ac87-424b-94ce-4633066a4a75` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `5b88fdb8-29e4-4d6a-b319-232ebfd44f47`<br>output `724f5c20-95f4-4798-a6c0-cacc58a3dd09` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `a10ce1a6-c0f5-4e83-adbb-b919391fd428`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `92b327f6-a5ff-4718-b70a-a274cbb4234f`<br>output `01ed1fda-94ee-461d-b0fa-886d52bf769f` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `f39dd7ed-e785-47c9-84e7-b6aa926eee60`<br>output `93a93aaf-5c88-4fdd-8c57-e4f20904c626` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `6c32db07-2a04-49ca-9bea-2a27ddc9d082`<br>output `33fddae4-3c3b-42ea-976b-6e1693d6ad71` |
| 6 | `verification_output` | linked | yes | object |  | `10-verify-partial-payment.output.verification_output` | Linked upstream output | param `8c89f377-3daa-4ec8-902e-3b1eb2b90b50`<br>output `4cf6421b-b617-4241-80ff-0d74802f26f9` |
