# 24-add-internal-note: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | Ticket id from the task query | param `c91d65b6-c78b-4063-85b7-f8ffa5973e13`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 1 | `ticket.status` | static |  | string | pending |  |  | param `8395c3ac-52e3-4dad-91e6-a99ceb6a43df` |
| 2 | `ticket.comment.body` | linked |  | string |  | `18-note-msg-nothing-paid.output.internal_note` | use the following template strictly<br><br>Customer {requester_name} claimed partial payment but Stripe shows no payments recorded.<br>Total still outstanding: ${total_amount_remaining} across {invoice_count_outstanding}    <br>  invoice(s).                                                                                  <br>  Invoices: [list invoice IDs]                <br>  Action: Verify payment with customer before responding.<br><br>please dont add any other text | param `7716d914-e67a-41c4-a4e4-7f5f95ceee80`<br>output `d14bf920-8c89-40ef-8076-d93c43fc9ac3` |
| 3 | `ticket.comment.public` | static |  | boolean | false |  | value for ${public} | param `0d4a6415-b423-4e5d-92a7-f96d47939f12` |
