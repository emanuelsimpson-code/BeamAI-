# 09-complete-task-prod: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `task_id` | linked | yes | string |  | `04-code-executor.output.target_task_id` | task id received from the salesforce | param `618983dd-3843-4ab7-a95a-a0a070848cc9`<br>output `20ccfa68-96bf-4670-8794-88638c23dbb6` |
| 1 | `Status` | static |  | string | Completed |  | Completed | param `d9db557e-12c4-4e68-a085-f1266a4f6e7a` |
| 2 | `Completed_by_Beam_ai__c` | static |  | boolean | true |  | true | param `69cd966e-0c74-4868-bdc8-706aad5a056a` |
| 3 | `Description` | ai_fill |  | string |  |  | Append one line to the Task's existing description. NEVER replace or drop existing lines.<br><br>Start from target_existing_description (from "create the necessary inputs for the email").<br>It may be empty. Output it verbatim, then a newline, then this new line:<br><br>[<today YYYY-MM-DD>] invoice <invoice_number>, stage <reminder_count>, Zendesk #<zendesk_ticket_id><br><br>Use the real Zendesk ticket id created in the Create Ticket step. If<br>target_existing_description is empty, output only the new line with no leading newline.<br><br>Sibling invoices at the same stage land on the same Task, so this field accumulates one<br>line per outreach. | param `d30f00de-e22a-41bb-a237-c87e9c2f65c8` |
