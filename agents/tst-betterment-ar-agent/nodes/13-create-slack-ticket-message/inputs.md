# 13-create-slack-ticket-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `06-create-ticket.output.data.ticket.id` | Linked from data.ticket.id | param `74346747-ab2b-4a8b-a124-8fb9f6c41eed`<br>output `a62feab0-3e1d-413a-998e-ebc2816b39f4` |
| 1 | `subject` | linked | yes | string |  | `06-create-ticket.output.data.ticket.subject` | Linked from data.ticket.subject | param `60ece76c-c8fc-4270-b0d7-6d4b00a39108`<br>output `39aabab3-cee2-4f01-ac30-cc7551bc2d45` |
| 2 | `requester_name` | linked | yes | string |  | `04-code-executor.output.customer_name` | Linked from customer_name | param `58f32a08-6fc7-425d-85c7-488520b8410e`<br>output `e659cd68-a1f4-4959-a126-27d1238e9440` |
| 3 | `requester_email` | ai_fill |  | string |  |  | The requester's email address, if present in context | param `086f8877-1133-4fc5-a0a0-7d71854cd008` |
| 4 | `ticket_status` | linked | yes | string |  | `06-create-ticket.output.data.ticket.status` | Linked from data.ticket.status | param `a4fa9318-aadc-4a9e-b581-37e9abe08031`<br>output `9bf2d3e1-42d9-4f7d-9c58-fbfc77190d80` |
| 5 | `reminder_count` | ai_fill | yes | number |  |  | Linked from data.records.Task_Index__c coming from salesforce | param `542fd77d-99a6-450b-95cd-2fd3b6e805fd` |
| 6 | `email_body` | linked | yes | string |  | `05-generate-email.output.email_body` | Linked from email_body | param `86b9895b-3aa0-4e63-82c1-5a180ef15fd4`<br>output `b7fca3c6-0605-48bd-909e-8d4dfe1f3eb8` |
