# 32-find-the-next-task: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `q` | ai_fill | yes | string |  |  | SELECT Id, Subject, Status, Task_Index__c, Description FROM Task WHERE WhatId='{case_id}' AND Completed_by_Beam_ai__c=true ORDER BY Task_Index__c DESC LIMIT 1<br><br>use the case Id from the previous find-case step | param `20dd8180-95a7-443d-b50c-8d6c1b2a4d89` |
