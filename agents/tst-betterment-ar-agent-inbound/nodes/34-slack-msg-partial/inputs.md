# 34-slack-msg-partial: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `a153ceec-5393-4743-b562-dca71207f399`<br>output `89443dd2-ac87-424b-94ce-4633066a4a75` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `8be97227-d273-48c8-ac16-dc648eef902b`<br>output `724f5c20-95f4-4798-a6c0-cacc58a3dd09` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `b87b64df-5f5e-4c6f-91e5-97619e9c9fef`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `eec2fb0f-dd04-4a76-94c6-fb391c6d555d`<br>output `01ed1fda-94ee-461d-b0fa-886d52bf769f` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `e27f7492-c5d8-4664-8990-3899ea961b13`<br>output `93a93aaf-5c88-4fdd-8c57-e4f20904c626` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `08be8121-343c-4ab8-aab1-4b5527257fd4`<br>output `33fddae4-3c3b-42ea-976b-6e1693d6ad71` |
| 6 | `verification_output` | linked | yes | object |  | `12-verify-complete-payment.output.verification_output` | Linked upstream output | param `54bcce15-a01b-42ce-92c6-90280b8dfca5`<br>output `61c905fe-6ca4-484f-a2aa-137b3ec10bcf` |
