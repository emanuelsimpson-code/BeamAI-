# 06-create-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket.subject` | linked |  | string |  | `05-generate-email.output.email_subject` | value for ${subject} | param `7c74d7d1-e4f1-4fa0-94b5-04683b79a86e`<br>output `adbf60cb-2d1b-4708-9e7c-cbde24cc2a36` |
| 1 | `ticket.comment.html_body` | linked |  | string |  | `05-generate-email.output.email_body` | value for ${html_body} | param `58be8561-3e61-45e9-948b-50af39e14f82`<br>output `b7fca3c6-0605-48bd-909e-8d4dfe1f3eb8` |
| 2 | `ticket.comment.public` | static |  | boolean | false |  | false | param `416f71ae-1cbf-42b5-9654-491ef3938e0c` |
| 3 | `ticket.priority` | static |  | string | medium |  | value for ${priority} | param `b708bf43-b5eb-40d2-a867-fc7b9bf78570` |
| 4 | `ticket.status` | static |  | string | open |  | value for ${status} | param `c95cb008-dcc5-4e8b-ba21-2e9370bfbd70` |
| 5 | `ticket.requester.locale_id` | static |  | number | 1 |  | value for ${locale_id} | param `f8e50170-fed5-42d5-8b32-e950295370c4` |
| 6 | `ticket.requester.name` | ai_fill |  | string |  |  | name of the client from the task query | param `b26428f4-fd58-4ca4-9bea-d3db8c02b12d` |
| 7 | `ticket.requester.email` | ai_fill |  | string |  |  | email of the client from the task query | param `30026e85-90b8-4e29-a5a1-12bca98f00f7` |
| 8 | `ticket.requester_id` | static |  | number | 45472670852251 |  | value for ${requester_id} | param `75ca0d8b-f24c-4e72-848e-7713181c4be1` |
| 9 | `ticket.organization_id` | static |  | number | 16020485248 |  | value for ${organization_id} | param `ea8b4f42-4e25-4a34-a4d7-c5c2a818375d` |
| 10 | `ticket.group_id` | static |  | number | 45472631317019 |  | value for ${group_id} | param `e5dc2296-1169-44d8-8e60-c6daeaa4e17f` |
| 11 | `ticket.ticket_form_id` | static |  | number | 45472736993435 |  | value for ${ticket_form_id} | param `2a9adc8e-01ca-452a-8dc3-6edea2dfee55` |
| 12 | `ticket.custom_status_id` | static |  | number | 4721089 |  | value for ${custom_status_id} | param `6c4f4671-c077-41ff-ae19-e3c87981f719` |
| 13 | `ticket.tags` | static |  | array | [<br>  "b4b_participant",<br>  "b4b_user",<br>  "betterment.com",<br>  "cash_reserve_user",<br>  "current_employee",<br>  "intent__billing__request_pay__invoice_settlement",<br>  "intent_confidence__high",<br>  "investing_customer",<br>  "investing_user",<br>  "proactive_ticket",<br>  "sf_webhook",<br>  "beamai"<br>] |  | {{string[]}} \| value for ${tags-[0]} \| Required: false | param `f4efc593-33f4-41c9-a0b2-5ede13e47e44` |
| 14 | `ticket.custom_fields` | linked |  | array |  | `04-code-executor.output.custom_fields` | [<br>  {<br>    "id": "{{number}} \| value for ${id} \| Required: false",<br>    "value": "{{string}} \| value for ${value} \| Required: false"<br>  }<br>] | param `73569517-5355-4da2-bbc0-753d6dfb3391`<br>output `c4506fce-bf67-4c0f-b19f-441791e3f7bf` |
