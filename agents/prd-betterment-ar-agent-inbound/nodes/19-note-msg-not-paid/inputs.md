# 19-note-msg-not-paid: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `email_body` | linked | yes | string |  | `01-trigger.output.all_comments` | Linked upstream output | param `f3db0287-553a-4eab-b8cc-c98682740e13`<br>output `19daded6-c834-41ea-9963-4997dcd3e2ac` |
| 1 | `requester_email` | linked | yes | string |  | `01-trigger.output.requester_email` | Linked upstream output | param `524ff565-7927-4afb-9ccd-93b2bf4eb7be`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
| 2 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Linked upstream output | param `5094b12d-e5c1-49b2-aacc-4abfda829e00`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 3 | `invoice_ids` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_ids` | Linked upstream output | param `58bbff1d-f592-49ed-9b12-da425fcaa425`<br>output `fa9553fb-d222-4709-9438-47371969eea6` |
| 4 | `invoice_amount` | linked | yes | string |  | `02-extract-invoice-context.output.invoice_amount` | Linked upstream output | param `872cedf3-c11d-43ba-93b2-0fd493093971`<br>output `e2edd3c2-6437-4ca3-aa38-a3d06241e90b` |
| 5 | `reply_intent` | linked | yes | string |  | `03-intent-classifier.output.reply_intent` | Linked upstream output | param `517fb959-54c0-4935-a106-e6cb2324faba`<br>output `7d2c43a3-977e-4168-8b58-2b7d90e4165b` |
| 6 | `verification_output` | linked | yes | object |  | `10-verify-complete-payment.output.verification_output` | Linked upstream output | param `c4a47bfc-4fd2-44a5-aa54-05e2896b6add`<br>output `d85e2f99-41b5-44d8-ae6b-cd9fc32cc79e` |
