# 24-reply-on-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | ticket id of zendesk from the task query | param `2ceadcd6-7a41-46e5-a7c1-6443f3793282`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 1 | `ticket.status` | static |  | string | pending |  | value for ${status} | param `4c55efe3-9ebd-4a4e-a596-c9740fce8ea4` |
| 2 | `ticket.comment.html_body` | linked |  | string |  | `18-payment-discrepancy-email.output.email_body` | value for ${html_body} | param `d17eeeec-0613-4146-b4a3-fc7ced7b52e0`<br>output `ba245983-39e3-4e2a-a168-e2f3b64237dc` |
| 3 | `ticket.comment.public` | static |  | boolean | true |  | value for ${public} | param `85b1bd66-cd93-47f0-b3d5-12d3c5f75ab6` |
| 4 | `ticket.comment.author_id` | static |  | number | 51883313273755 |  | value for ${author_id} | param `ad0a0f7d-c87c-4081-95cd-9952ee0c5425` |
