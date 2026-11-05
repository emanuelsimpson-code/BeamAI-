# 29-add-internal-note: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Ticket id from the task query | param `86f07d41-658b-4bff-99c9-c6498944a76b`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 1 | `ticket.status` | static |  | string | pending |  |  | param `2ee3c773-4ef0-4167-83d1-d1b1dfa6cd97` |
| 2 | `ticket.comment.body` | linked |  | string |  | `23-note-msg-nothing-paid.output.internal_note` | use the following template strictly<br><br>Customer {requester_name} claimed partial payment but Stripe shows no payments recorded.<br>Total still outstanding: ${total_amount_remaining} across {invoice_count_outstanding}    <br>  invoice(s).                                                                                  <br>  Invoices: [list invoice IDs]                <br>  Action: Verify payment with customer before responding.<br><br>please dont add any other text | param `25ac651a-de0d-4f49-958f-4cfcd1c0b6cb`<br>output `7588e913-0067-4c9c-a7ea-e3378f1fcc98` |
| 3 | `ticket.comment.public` | static |  | boolean | false |  | value for ${public} | param `463164a1-33a7-461b-8971-ac07c48851e6` |
