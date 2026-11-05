# 09-complete-task: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `task_id` | linked | yes | string |  | `04-code-executor.output.target_task_id` | task id received from the salesforce | param `4038c623-2cfb-4387-a5c0-c14a23d1e2ec`<br>output `8869fb1e-f601-4ec9-aacf-ef427281ed72` |
| 1 | `Status` | static |  | string | Completed |  | Completed | param `6c31ee44-1b08-4fc7-ad94-622f57066af0` |
| 2 | `Completed_by_Beam_ai__c` | static |  | boolean | true |  | true | param `93cfb2c3-274e-43f9-92c9-61782a358f3e` |
| 3 | `Description` | ai_fill |  | string |  |  | Append one line to the Task's existing description. NEVER replace or drop existing lines.<br><br>Start from target_existing_description (from "create the necessary inputs for the email").<br>It may be empty. Output it verbatim, then a newline, then this new line:<br><br>[<today YYYY-MM-DD>] invoice <invoice_number>, stage <reminder_count>, Zendesk #<zendesk_ticket_id><br><br>Use the real Zendesk ticket id created in the Create Ticket step. If<br>target_existing_description is empty, output only the new line with no leading newline.<br><br>Sibling invoices at the same stage land on the same Task, so this field accumulates one<br>line per outreach. | param `5e8bb8d9-d346-4dfe-8563-4108b5612a1e` |
