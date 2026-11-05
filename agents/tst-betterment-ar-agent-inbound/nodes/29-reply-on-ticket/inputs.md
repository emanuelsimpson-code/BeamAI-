# 29-reply-on-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | ticket id of zendesk from the task query | param `d3263119-5d9c-4ca5-b615-d98ca148f73c`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 1 | `ticket.status` | static |  | string | pending |  | value for ${status} | param `6c43f30e-029b-416e-8089-7b19826e63ad` |
| 2 | `ticket.comment.html_body` | linked |  | string |  | `23-payment-discrepancy-email.output.email_body` | value for ${html_body} | param `6146b5a5-fd06-4882-a3dc-1f781c95920f`<br>output `a2753434-1fe1-4ddf-a31b-ecf9a78efe5c` |
| 3 | `ticket.comment.public` | static |  | boolean | true |  | value for ${public} | param `28d5615b-b054-4426-be31-bc9e49e4ce38` |
| 4 | `ticket.comment.author_id` | static |  | number | 1900263981784 |  | value for ${author_id} | param `d3058097-a67d-4fa5-b184-f42498f13f26` |
