# 26-reply-on-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | value for ${ticket_id} | param `23cc65f9-d681-4d1e-8789-1ad8ded88cc9`<br>output `cec5bc48-50ea-4e68-89ab-073682f22964` |
| 1 | `ticket.status` | static |  | string | solved |  | value for ${status} | param `d1eaf22c-0475-4649-89fb-71234a0f14ee` |
| 2 | `ticket.comment.html_body` | linked |  | string |  | `20-payment-acknowledgement-generator.output.email_body` | value for ${html_body} | param `85e42be8-1710-4050-914a-8c297a8f5fdf`<br>output `80700036-2604-4429-be9e-91038f25866e` |
| 3 | `ticket.comment.public` | static |  | boolean | true |  | value for ${public} | param `70e3dbea-84de-4d38-8539-25a461de4e7c` |
| 4 | `ticket.comment.author_id` | static |  | number | 51883313273755 |  | value for ${author_id} | param `d112a580-8e07-48b5-b6b2-6a11bd579c4a` |
