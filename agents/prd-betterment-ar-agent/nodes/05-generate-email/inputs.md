# 05-generate-email: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `total_amount_due` | linked | yes | string |  | `04-code-executor.output.total_amount_due` | sum of amount_due across all invoices | param `0e9025a4-69ca-4753-97b7-1b81ad915b18`<br>output `cfc5520f-a0ca-4b2a-a6d9-862c68807a60` |
| 1 | `invoice_count` | linked | yes | string |  | `04-code-executor.output.invoice_count` | number of overdue invoices for this entity | param `b0078fa6-8567-4b73-9e01-6fe4bafe81ad`<br>output `fc720831-60db-4446-91d4-2d93cee067f8` |
| 2 | `invoices` | linked | yes | string |  | `04-code-executor.output.invoices` | array of objects, one per invoice containing invoice_id, days_overdue, stripe hosted invoice url | param `d13ff3e4-f804-4cf7-89db-d0e6e7102100`<br>output `9a49aa19-319b-469e-877c-2f4a67807b6b` |
| 3 | `customer_name` | linked | yes | string |  | `04-code-executor.output.customer_name` | customer name from the task payload | param `ea1d0b5d-be7c-4f90-b497-ea43511fa2d2`<br>output `34561367-314e-44df-add1-f26a2b294c3c` |
| 4 | `reminder_count` | linked | yes | string |  | `04-code-executor.output.reminder_count` | Dunning stage for this invoice, derived from days_overdue by the 'create the necessary inputs for the email' step (0=first notice, 1=second, 2=final). Use it verbatim - do not re-derive from Salesforce. | param `7676784c-3d61-490c-b6f6-c8a097ea7d9c`<br>output `90b898f3-561a-427f-be61-4219606285a9` |
