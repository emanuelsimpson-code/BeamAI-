# 02-find-open-case: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `q` | ai_fill | yes | string |  |  | SELECT Id, CaseNumber, Status, Stripe_Customer_Id__c FROM Case WHERE Stripe_Customer_Id__c = '{stripe_customer_id}' AND RecordTypeId = '012QK000000bp1xYAA' AND IsClosed = false LIMIT 1<br><br>replace the stripe_customer_id with the real customer_id from the task payload recieved | param `8d4a595a-b153-4fb5-9cd2-e778f9543227` |
