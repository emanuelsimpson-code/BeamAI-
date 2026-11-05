# 26-find-open-case: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `q` | ai_fill | yes | string |  |  | SELECT Id, CaseNumber FROM Case WHERE Entity__c IN (SELECT Entity__c FROM Bill__c WHERE Stripe_Invoice_Id__c = '{invoice_id}') AND RecordTypeId='012QK000000bp1xYAA' AND IsClosed=false LIMIT 1<br><br>replace invoice_id with any one invoice_id received in the task query | param `62576b30-ea50-4acc-8812-4cb04eb206c1` |
