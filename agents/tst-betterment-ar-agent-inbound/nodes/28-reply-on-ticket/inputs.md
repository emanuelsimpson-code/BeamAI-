# 28-reply-on-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `01-trigger.output.ticket_id` | value for ${ticket_id} | param `2d355a08-58a1-49b0-a7f9-46ce74ec96e6`<br>output `773034ca-fa91-4f92-90de-12504d730747` |
| 1 | `ticket.status` | static |  | string | solved |  | value for ${status} | param `93e725d9-05fb-49be-b395-518284857755` |
| 2 | `ticket.comment.html_body` | linked |  | string |  | `22-payment-acknowledgement-generator.output.email_body` | value for ${html_body} | param `6aaa7ab8-79c4-4fd1-aed0-ff24007fa14f`<br>output `2f18f0a8-4308-4793-878d-758b910f49b6` |
| 3 | `ticket.comment.public` | static |  | boolean | true |  | value for ${public} | param `e269fc57-cfdf-495f-96ff-604ce9c905bc` |
| 4 | `ticket.comment.author_id` | static |  | number | 1900263981784 |  | value for ${author_id} | param `df038858-e8ae-454d-9027-ed782a434675` |
