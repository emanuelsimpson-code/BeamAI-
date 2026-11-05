# 03-find-the-next-task: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `q` | ai_fill | yes | string |  |  | SELECT Id, Subject, Status, Task_Index__c, Completed_by_Beam_ai__c, Description FROM Task WHERE WhatId = '{case_id}' ORDER BY Task_Index__c ASC | param `e65a0dcb-42b8-4f80-9c36-8f5ce19c69c4` |
