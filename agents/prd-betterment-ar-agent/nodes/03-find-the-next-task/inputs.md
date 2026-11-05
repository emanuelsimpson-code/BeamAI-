# 03-find-the-next-task: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `q` | ai_fill | yes | string |  |  | SELECT Id, Subject, Status, Task_Index__c, Completed_by_Beam_ai__c, Description<br>FROM Task WHERE WhatId = '{case_id}' ORDER BY Task_Index__c ASC<br><br>replace the case_id with the real case_id from the salesforce | param `31c19c19-9593-4ee8-b460-3eaa636031ce` |
