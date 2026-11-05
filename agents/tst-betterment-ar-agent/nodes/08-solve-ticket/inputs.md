# 08-solve-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `06-create-ticket.output.data.audit.ticket_id` | The id of the ticket created | param `aa27b4d1-535c-4503-9c66-8e486962c269`<br>output `2a6fa0ad-cb7c-41be-8f68-6e394113ef57` |
| 1 | `ticket.status` | static |  | string | solved |  | value for ${status} | param `c02076b6-1ccd-4c11-ad5e-6737e15e6411` |
| 2 | `ticket.comment.html_body` | linked |  | string |  | `05-generate-email.output.email_body` | value for ${html_body} | param `0344de76-a97e-48f3-a7c3-2098dda674da`<br>output `b7fca3c6-0605-48bd-909e-8d4dfe1f3eb8` |
| 3 | `ticket.comment.public` | static |  | boolean | true |  | value for ${public} | param `408cbc85-d928-4636-80a6-f68c6057e1cd` |
| 4 | `ticket.comment.author_id` | static |  | number | 1900263981784 |  | value for ${author_id} | param `c8bc5456-37d9-4671-bd55-b7e6963cc92d` |
