# 25-reply-on-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | The ticket id from the task query | param `9a2da2cb-cdf9-4070-871c-3d77145e68fa`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 1 | `ticket.comment.author_id` | static |  | number | 1900263981784 |  | value for ${author_id} | param `8adbbae7-36ac-40bf-beb1-13d506fb52f8` |
| 2 | `ticket.comment.public` | static |  | boolean | true |  | value for ${public} | param `b67a0075-06a4-427d-8ae2-63d9d8ee2835` |
| 3 | `ticket.status` | static |  | string | pending |  | value for ${status} | param `bae46146-27fc-4abd-82df-0cdec3803791` |
| 4 | `ticket.comment.html_body` | linked |  | string |  | `19-partial-payment-email-generator.output.email_body` | value for ${html_body} | param `e946fe8d-78b1-4c75-8d78-c6219a6585b1`<br>output `ad20c0c3-8521-4c4a-937a-12a6126f7722` |
