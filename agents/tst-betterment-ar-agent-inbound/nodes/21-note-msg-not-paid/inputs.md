# 21-note-msg-not-paid: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `1bb2c9c1-dd04-4ec7-a94c-1ed47a03aa2e`<br>output `89443dd2-ac87-424b-94ce-4633066a4a75` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `1f5c1376-dce4-4935-a6ea-8334ae348e0c`<br>output `724f5c20-95f4-4798-a6c0-cacc58a3dd09` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `46769110-3051-4049-87c7-3e997cfe48e9`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `ed56acdf-2658-4213-a720-36c1154128d6`<br>output `01ed1fda-94ee-461d-b0fa-886d52bf769f` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `bae5f181-ec6b-49d6-84c4-c077dc20abc3`<br>output `93a93aaf-5c88-4fdd-8c57-e4f20904c626` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `ce0a3edf-2539-4e18-a35c-22420fe08d5b`<br>output `33fddae4-3c3b-42ea-976b-6e1693d6ad71` |
| 6 | `verification_output` | linked | yes | object |  | `12-verify-complete-payment.output.verification_output` | Linked upstream output | param `82a8a28a-d0d6-429b-914e-607a5ef77f06`<br>output `61c905fe-6ca4-484f-a2aa-137b3ec10bcf` |
