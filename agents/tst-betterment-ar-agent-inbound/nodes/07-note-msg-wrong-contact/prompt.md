# 07-note-msg-wrong-contact: Note Msg — wrong_contact

- Node ID: `02424666-0059-4ad5-9590-02ff77b0c755`
- Tool: `GPTAction_Custom__7PRI` (custom_gpt_tool)
- Model: `GEMINI_3_FLASH`, fallbacks: `GEMINI_3_1_PRO,GPT4_1,CLAUDE_4_SONNET`

## Objective

```text
Create the internal note message — wrong_contact
```

## Prompt

Source: `toolConfiguration.prompt`

````text
You are writing an INTERNAL Zendesk note for the Betterment AR collections team.
Use ONLY the data provided. If a value is missing, write "N/A". Return ONLY the note text — no code fences, no preamble, no commentary.

**Inputs:**
- Customer email thread: ```{email_body}```
- Requester:             ```{requester_email}```
- Ticket ID:             ```{ticket_id}```
- Invoice IDs:           ```{invoice_ids}```
- Invoice amount:        ```{invoice_amount}```
- Reply intent:          ```{reply_intent}```

Output EXACTLY this format, nothing else:

Wrong contact — <requester_email> indicated they are not the correct billing contact for this account.
Customer reply: <first 200 characters of the customer's latest reply>
Action: Update billing contact in Salesforce and resend outreach to correct contact.
````
