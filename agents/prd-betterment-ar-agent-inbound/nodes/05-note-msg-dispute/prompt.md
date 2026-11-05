# 05-note-msg-dispute: Note Msg — dispute

- Node ID: `9d47a599-a93e-4a21-a309-f7c7723a715c`
- Tool: `GPTAction_Custom__j9TT` (custom_gpt_tool)
- Model: `GEMINI_25_FLASH`, fallbacks: `GEMINI_3_1_PRO`

## Objective

```text
Create the internal note message — dispute
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

DISPUTE — <requester_email> has disputed invoice(s) totaling $<invoice_amount>.
Customer reply: <first 200 characters of the customer's latest reply>
````
