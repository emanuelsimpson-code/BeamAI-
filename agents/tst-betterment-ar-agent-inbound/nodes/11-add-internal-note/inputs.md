# 11-add-internal-note: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket.comment.body` | linked |  | string |  | `07-note-msg-wrong-contact.output.internal_note` | Format exactly as:<br>  "Wrong contact — {requester_name} ({requester_email}) indicated they are not the correct billing contact for this account.<br>  Customer reply: [first 200 characters of ticket_latest_comment]<br>  Action: Update billing contact in Salesforce and resend outreach to correct contact." | param `e7b278bf-7b05-46a6-af8f-80fd2da493c0`<br>output `ac5566f6-194f-487f-bd7e-57cdb382bdf6` |
| 1 | `ticket_id` | ai_fill | yes | string |  |  | The ticket id recieved in the task query | param `c0deee09-beaf-46e0-a055-6322eec6bae4` |
| 2 | `ticket.status` | static |  | string | pending |  | pending | param `cabf8b77-fa58-4445-91b6-da7e85a465e6` |
| 3 | `ticket.comment.public` | static |  | boolean | false |  | value for ${public} | param `5937442f-b1d2-493b-9bca-18f7e2240282` |
