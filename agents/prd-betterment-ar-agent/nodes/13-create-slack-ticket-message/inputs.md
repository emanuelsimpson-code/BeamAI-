# 13-create-slack-ticket-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `reminder_count` | ai_fill | yes | number |  |  | Linked from data.records.Task_Index__c coming from salesforce | param `259760cc-d08d-4432-9c9d-04a9d86d8e8b` |
| 1 | `ticket_status` | linked | yes | string |  | `06-create-ticket.output.data.ticket.status` | Linked from data.ticket.status | param `fac7b0b2-eb4c-476c-9a26-53727ac1db95`<br>output `30919d9d-bb81-4aea-9b9c-ec13fcebbcec` |
| 2 | `subject` | linked | yes | string |  | `06-create-ticket.output.data.ticket.subject` | Linked from data.ticket.subject | param `da5e2c49-d09e-4722-8ac6-7e831804edd8`<br>output `eebab73f-cefe-475d-945b-f9f7c03b1e5e` |
| 3 | `requester_name` | linked | yes | string |  | `04-code-executor.output.customer_name` | Linked from customer_name | param `228cd92f-64ff-4439-801f-4d803abfdf06`<br>output `34561367-314e-44df-add1-f26a2b294c3c` |
| 4 | `requester_email` | linked |  | string |  | `04-code-executor.output.customer_email` | The requester's email address, if present in context | param `4d216b1e-99b6-4151-95d2-146c898bb899`<br>output `6cb0855a-5c7b-4a5e-aa91-c1da2ff7c239` |
| 5 | `ticket_id` | linked | yes | string |  | `06-create-ticket.output.data.ticket.id` | Linked from data.ticket.id | param `e6b8e151-66d1-4095-a4c9-048be7f951dd`<br>output `d5b5b789-02f3-438d-9fc7-009a90724e3e` |
| 6 | `email_body` | linked | yes | string |  | `05-generate-email.output.email_body` | Linked from email_body | param `5975966c-7dd5-4b57-b54e-86fe648ea5c3`<br>output `6302463b-b185-4398-950b-c169fd53caee` |
