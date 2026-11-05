# 37-reopen-task: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `task_id` | linked | yes | string |  | `32-find-the-next-task.output.data.records.Id` | Linked: Salesforce Task Id of the most recent Beam-completed task from the find-task step. | param `b0c15d63-4c45-4ad0-a979-2ed9b769f477`<br>output `da119986-980c-45cc-9fde-cd4d3d51255d` |
| 1 | `Status` | static |  | string | Open |  | Open | param `f7de8cce-32fc-4518-ad94-163d64b2b3a8` |
| 2 | `Completed_by_Beam_ai__c` | static |  | boolean | false |  | false | param `95b8c179-7634-45ee-b4ac-74512cbec8ef` |
| 3 | `Description` | ai_fill |  | string |  |  | "Reopened by Beam AI agent. Customer indicated wrong billing contact. Zendesk Ticket: {ticket_id}. Awaiting correct billing contact before re-sending outreach."<br><br>replace {ticket_id} with the real Zendesk ticket id from the task. Output ONLY this single note (do NOT keep or append the previous task description). | param `6610a1d8-1ca3-472f-b129-3db1e86fb1b2` |
