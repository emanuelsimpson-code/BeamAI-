# 37-reopen-task-prod: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `task_id` | linked | yes | string |  | `32-find-the-next-task.output.data.records.Id` | Linked: Salesforce Task Id of the most recent Beam-completed task from the find-task step. | param `440eddbb-378c-4dd6-b4b9-df0d661a5a7f`<br>output `27ca9c45-d0ce-4bb3-8ed5-3f7a6804cac1` |
| 1 | `Status` | static |  | string | Open |  | Open | param `e4c1c529-2e8d-464b-bb8c-c5808a233f46` |
| 2 | `Completed_by_Beam_ai__c` | static |  | boolean | false |  | false | param `55f01c36-cfc7-418f-8d25-94b8561db23a` |
| 3 | `Description` | ai_fill |  | string |  |  | "Reopened by Beam AI agent. Customer indicated wrong billing contact. Zendesk Ticket: {ticket_id}. Awaiting correct billing contact before re-sending outreach."<br><br>replace {ticket_id} with the real Zendesk ticket id from the task. Output ONLY this single note (do NOT keep or append the previous task description). | param `961351bb-9165-41d2-9049-f0eba67f7173` |
