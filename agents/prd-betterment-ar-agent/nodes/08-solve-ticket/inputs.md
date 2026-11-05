# 08-solve-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `06-create-ticket.output.data.ticket.id` | The id of the ticket created | param `88badd6e-6a64-45fd-8b54-38f5fcacda2d`<br>output `d5b5b789-02f3-438d-9fc7-009a90724e3e` |
| 1 | `ticket.status` | static |  | string | solved |  | value for ${status} | param `51dcd30c-f700-4585-915c-c604cdbb9c59` |
| 2 | `ticket.comment.html_body` | linked |  | string |  | `05-generate-email.output.email_body` | value for ${html_body} | param `00247fef-2625-41ef-818e-e315b90edd8d`<br>output `6302463b-b185-4398-950b-c169fd53caee` |
| 3 | `ticket.comment.public` | static |  | boolean | true |  | value for ${public} | param `6fcbbfdd-a6ef-4c14-98db-ebe4041f342a` |
| 4 | `ticket.comment.author_id` | static |  | number | 51883313273755 |  | value for ${author_id} | param `f35e36f8-f6e8-407e-8f7f-c108dfba92ad` |
