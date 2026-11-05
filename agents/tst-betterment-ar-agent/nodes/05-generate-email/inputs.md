# 05-generate-email: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `reminder_count` | linked | yes | string |  | `04-code-executor.output.reminder_count` | Dunning stage for this invoice, derived from days_overdue by the 'create the necessary inputs for the email' step (0=first notice, 1=second, 2=final). Use it verbatim - do not re-derive from Salesforce. | param `0dec62b7-39b9-4364-b05f-5637fff6a045`<br>output `c1caafd9-8b46-44e2-b3a3-217003c977d9` |
| 1 | `customer_name` | ai_fill | yes | string |  |  | customer name from the task payload | param `502bdf69-d5f5-4683-9986-dcbb8a71312d` |
| 2 | `invoice_count` | ai_fill | yes | string |  |  | number of overdue invoices for this entity | param `cb10e7a3-6542-48f2-bf96-8a497b62f605` |
| 3 | `total_amount_due` | ai_fill | yes | string |  |  | sum of amount_due across all invoices | param `53ac80d6-2681-4f5c-b92f-d26d66caae77` |
| 4 | `invoices` | ai_fill | yes | string |  |  | array of objects, one per invoice containing invoice_id, days_overdue, stripe hosted invoice url | param `dd1bb4a3-4aa5-43bd-811a-52736bea762b` |
