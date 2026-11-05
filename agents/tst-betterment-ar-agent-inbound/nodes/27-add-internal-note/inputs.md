# 27-add-internal-note: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | ticket id from the task query | param `c267b6fe-c66d-4e00-84ad-c37fe7cc54a1`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 1 | `ticket.status` | static |  | string | pending |  | value for ${status} | param `34aab1e4-66ed-4b2b-930f-711ad743a717` |
| 2 | `ticket.comment.body` | linked |  | string |  | `21-note-msg-not-paid.output.internal_note` | Customer {customer_name from the task query} replied confirming payment but Stripe shows                       <br>  ${total_amount_remaining} still outstanding across {invoice_count} invoice(s).<br>                                                                                <br>  Stripe status: {verification_status}                                                         <br>  Invoices checked: {invoices}                                                                 <br>                                                                                               <br>  Manual review required before closing ticket. | param `35b0ce6c-c683-41bc-9189-72c14bb7ec1b`<br>output `1299340d-e5f6-4ccd-85af-468e45bd946d` |
| 3 | `ticket.comment.public` | static |  | boolean | false |  | value for ${public} | param `1ee73707-c566-4a70-b077-bd15294f8c26` |
