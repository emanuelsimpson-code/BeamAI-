# 18-note-msg-nothing-paid: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `58ca8f37-c94a-433d-a50e-0051faad8113`<br>output `89443dd2-ac87-424b-94ce-4633066a4a75` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `bbdb1571-f5ea-4676-8e39-43e22ffd9b90`<br>output `724f5c20-95f4-4798-a6c0-cacc58a3dd09` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `f2f1a856-c589-4d1d-b14a-7783071de397`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `90a4e35b-eba5-448c-8690-9078a47e99c9`<br>output `01ed1fda-94ee-461d-b0fa-886d52bf769f` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `a0959521-1f36-4dd7-a433-aa3c12cbaeb7`<br>output `93a93aaf-5c88-4fdd-8c57-e4f20904c626` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `c34b342f-8b58-401a-9467-178f4c4b919b`<br>output `33fddae4-3c3b-42ea-976b-6e1693d6ad71` |
| 6 | `verification_output` | linked | yes | object |  | `10-verify-partial-payment.output.verification_output` | Linked upstream output | param `7e818efd-39b8-42ba-a8de-e5495a8a38f3`<br>output `4cf6421b-b617-4241-80ff-0d74802f26f9` |
