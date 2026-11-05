# 06-create-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket.custom_fields` | linked |  | array |  | `04-code-executor.output.custom_fields` | [<br>  {<br>    "id": "{{number}} \| value for ${id} \| Required: false",<br>    "value": "{{string}} \| value for ${value} \| Required: false"<br>  }<br>] | param `ed8ea190-9b2c-4b40-825f-d9c52f951861`<br>output `fcd05466-6586-451b-9894-d0caee280734` |
| 1 | `ticket.subject` | linked |  | string |  | `05-generate-email.output.email_subject` | value for ${subject} | param `7d70e278-981b-4ed6-9851-3619586af044`<br>output `78d87402-7e08-4db8-886d-85c2863fd940` |
| 2 | `ticket.comment.html_body` | linked |  | string |  | `05-generate-email.output.email_body` | value for ${html_body} | param `0d760833-b697-4b0c-90ca-b75137b51efa`<br>output `6302463b-b185-4398-950b-c169fd53caee` |
| 3 | `ticket.comment.public` | static |  | boolean | false |  | false | param `1ecd9514-6896-4ae8-ba82-71f4977c22b6` |
| 4 | `ticket.priority` | static |  | string | normal |  | value for ${priority} | param `9344c183-234b-4818-bffe-aa3d05904766` |
| 5 | `ticket.status` | static |  | string | open |  | value for ${status} | param `49d59073-e1d2-41c6-8d17-11ac9f29fe89` |
| 6 | `ticket.requester.locale_id` | static |  | number | 1 |  | value for ${locale_id} | param `432c6647-352b-443f-8d2a-0396ff48ae25` |
| 7 | `ticket.requester.name` | linked |  | string |  | `04-code-executor.output.customer_name` | name of the client from the task query | param `b3dc1d1d-7752-47ec-9f9f-56ae4f61a0ef`<br>output `34561367-314e-44df-add1-f26a2b294c3c` |
| 8 | `ticket.requester.email` | linked |  | string |  | `04-code-executor.output.customer_email` | email of the client from the task query | param `417d6335-99db-487e-8f46-8c28088f4099`<br>output `6cb0855a-5c7b-4a5e-aa91-c1da2ff7c239` |
| 9 | `ticket.organization_id` | static |  | number | 16020485248 |  | value for ${organization_id} | param `c4162a2b-0b78-41cb-999e-cf22e7a5255a` |
| 10 | `ticket.group_id` | static |  | number | 5465785715739 |  | value for ${group_id} | param `a91b8177-e743-40bb-affa-71109f93f8da` |
| 11 | `ticket.ticket_form_id` | static |  | number | 5466269453723 |  | value for ${ticket_form_id} | param `e06c5286-3425-4a73-b35f-1db1ea11b0d5` |
| 12 | `ticket.custom_status_id` | static |  | number | 4721089 |  | value for ${custom_status_id} | param `c35c72c8-920d-4343-8d97-e5ec05c74bab` |
| 13 | `ticket.tags` | static |  | array | ["b4b_participant", "b4b_user", "betterment.com", "cash_reserve_user", "current_employee", "intent__billing__request_pay__invoice_settlement", "intent_confidence__high", "investing_customer", "investing_user", "proactive_ticket", "sf_webhook", "beamai"] |  | {{string[]}} \| value for ${tags-[0]} \| Required: false | param `18a335ef-2718-421d-853f-f63154931061` |
