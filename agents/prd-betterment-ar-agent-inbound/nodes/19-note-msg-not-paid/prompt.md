# 19-note-msg-not-paid: Note Msg — not_paid

- Node ID: `a9e562a1-23bb-410c-9100-e9f2c329beb9`
- Tool: `GPTAction_Custom__LA2E` (custom_gpt_tool)
- Model: `GEMINI_3_1_PRO`, fallbacks: `GEMINI_3_1_PRO,GPT4_1,CLAUDE_4_SONNET`

## Objective

```text
Create the internal note message — not_paid
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
- Verification result:   ```{verification_output}```

Output EXACTLY this format (substitute values from verification_output):

Customer <requester_email> replied confirming payment but Stripe shows $<total_amount_remaining> still outstanding across <invoice_count> invoice(s).

Stripe status: <verification_status>
Invoices checked: <invoices>

Manual review required before closing ticket.
````
