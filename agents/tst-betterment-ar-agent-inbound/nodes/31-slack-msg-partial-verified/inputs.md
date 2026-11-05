# 31-slack-msg-partial-verified: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `8e022003-9792-4ba1-a5bf-50ef97ac84a9`<br>output `89443dd2-ac87-424b-94ce-4633066a4a75` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `b48eb46a-c1a8-4a5e-8411-a1dab121246a`<br>output `724f5c20-95f4-4798-a6c0-cacc58a3dd09` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `635b2be2-81a4-4705-b437-7552758fc622`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `0404b899-04e0-45b2-98b0-01c63258e934`<br>output `01ed1fda-94ee-461d-b0fa-886d52bf769f` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `674a89ed-088f-46ed-8c45-b80ad0a18d4e`<br>output `93a93aaf-5c88-4fdd-8c57-e4f20904c626` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `34122385-0c57-43e0-af42-bb2415f87767`<br>output `33fddae4-3c3b-42ea-976b-6e1693d6ad71` |
| 6 | `verification_output` | linked | yes | object |  | `10-verify-partial-payment.output.verification_output` | Linked upstream output | param `803ce7f1-f044-426c-96e3-ae130b5053a7`<br>output `4cf6421b-b617-4241-80ff-0d74802f26f9` |
