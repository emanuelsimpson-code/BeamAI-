# 28-reply-on-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | The ticket id from the task query | param `3081ca58-85c5-4e17-a54d-ddfd10c21576`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 1 | `ticket.comment.author_id` | static |  | number | 51883313273755 |  | value for ${author_id} | param `ef68c3e5-e27b-493b-9035-3bf3494b1982` |
| 2 | `ticket.comment.public` | static |  | boolean | true |  | value for ${public} | param `7e98925a-14b5-437b-9d3d-a6a32d27acfe` |
| 3 | `ticket.status` | static |  | string | pending |  | value for ${status} | param `70871b45-def4-4998-8220-78503e2b7480` |
| 4 | `ticket.comment.html_body` | linked |  | string |  | `22-partial-payment-email-generator.output.email_body` | value for ${html_body} | param `f8ec81f1-c141-496e-96d4-319725223b79`<br>output `8b8bd4d1-44a5-43b9-bee9-99e00c70ab5d` |
