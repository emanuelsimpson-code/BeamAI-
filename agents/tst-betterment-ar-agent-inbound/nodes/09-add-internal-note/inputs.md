# 09-add-internal-note: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | value for ${ticket_id} | param `9b60106b-d3e7-4a47-933d-9094a289ef6e`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 1 | `ticket.status` | static |  | string | open |  | value for ${status} | param `c3b254be-bfdc-410b-9b8a-1945980ce6c1` |
| 2 | `ticket.comment.body` | linked |  | string |  | `05-note-msg-dispute.output.internal_note` | write an internal note for AR team format exactly as:                                                                                                                            <br>"DISPUTE — {requester_name} ({requester_email}) has disputed invoice(s)<br>totaling ${invoice_amount}.                                                                                                                   <br>Customer reply: [first 200 characters of ticket_latest_comment]"<br><br>please dont add any other text | param `df34ef9f-4a6e-42ca-b9e7-6a6c935d96c6`<br>output `c2464969-8733-4368-b0d1-b56b05e28901` |
| 3 | `ticket.comment.public` | static |  | boolean | false |  | value for ${public} | param `021dae87-59c5-4170-9c8f-5eaa1c99e6ca` |
