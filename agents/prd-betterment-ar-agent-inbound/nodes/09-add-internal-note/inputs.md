# 09-add-internal-note: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | value for ${ticket_id} | param `7f87f53c-a0e0-4b6b-b1e9-f87fbabfaaec`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 1 | `ticket.status` | static |  | string | open |  | value for ${status} | param `73abe361-e0d3-4195-ae01-327278095b10` |
| 2 | `ticket.comment.body` | linked |  | string |  | `05-note-msg-dispute.output.internal_note` | write an internal note for AR team format exactly as:                                                                                                                            <br>"DISPUTE — {requester_name} ({requester_email}) has disputed invoice(s)<br>totaling ${invoice_amount}.                                                                                                                   <br>Customer reply: [first 200 characters of ticket_latest_comment]"<br><br>please dont add any other text | param `fe988ad7-1b6d-47b4-a1da-373d9f6eb24c`<br>output `9ec4b37c-822a-490d-b5a4-3b7c001dd837` |
| 3 | `ticket.comment.public` | static |  | boolean | false |  | value for ${public} | param `d7b70857-abd7-41c3-91f7-80c18f51939f` |
