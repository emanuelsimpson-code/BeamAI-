# 11-add-internal-note: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket.comment.body` | linked |  | string |  | `07-note-msg-wrong-contact.output.internal_note` | Format exactly as:<br>  "Wrong contact — {requester_name} ({requester_email}) indicated they are not the correct billing contact for this account.<br>  Customer reply: [first 200 characters of ticket_latest_comment]<br>  Action: Update billing contact in Salesforce and resend outreach to correct contact." | param `65510c34-b90d-4702-a314-be24d2e8ede8`<br>output `ed009c20-0bb4-44ed-a59b-0791615d0010` |
| 1 | `ticket_id` | ai_fill | yes | string |  |  | The ticket id recieved in the task query | param `d0faefe5-3c52-40e2-9fb5-c8542695b43b` |
| 2 | `ticket.status` | static |  | string | pending |  | pending | param `c9f72065-07d0-404d-bde5-ef1b2943241c` |
| 3 | `ticket.comment.public` | static |  | boolean | false |  | value for ${public} | param `39a9adbf-2f54-4c91-b2b2-f7a2b176a025` |
