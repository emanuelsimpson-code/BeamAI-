# 25-add-internal-note: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | ticket id from the task query | param `5272fdd9-de10-49f1-bc26-21e81d430540`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 1 | `ticket.status` | static |  | string | pending |  | value for ${status} | param `5213f729-dedc-4f0f-9d7a-4c966172649e` |
| 2 | `ticket.comment.body` | linked |  | string |  | `19-note-msg-not-paid.output.internal_note` | Customer {customer_name from the task query} replied confirming payment but Stripe shows                       <br>  ${total_amount_remaining} still outstanding across {invoice_count} invoice(s).<br>                                                                                <br>  Stripe status: {verification_status}                                                         <br>  Invoices checked: {invoices}                                                                 <br>                                                                                               <br>  Manual review required before closing ticket. | param `e76c9f93-8819-4431-9e3a-89142760be1e`<br>output `4fd328fd-c5d5-4e21-83a4-d94bd50dec58` |
| 3 | `ticket.comment.public` | static |  | boolean | false |  | value for ${public} | param `033afc55-b494-4fc2-99fb-b67eaad04569` |
