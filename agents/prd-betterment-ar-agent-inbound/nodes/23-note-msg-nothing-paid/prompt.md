# 23-note-msg-nothing-paid: Note Msg — nothing_paid

- Node ID: `e9d924d6-f28a-48fd-8b2d-5e2daf2baa60`
- Tool: `GPTAction_Custom__B9Ts` (custom_gpt_tool)
- Model: `GEMINI_25_FLASH`, fallbacks: `GEMINI_3_1_PRO`

## Objective

```text
Create the internal note message — nothing_paid
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

Output EXACTLY this format, nothing else:

Customer <requester_email> claimed partial payment but Stripe shows no payments recorded.
Total still outstanding: $<total_amount_remaining> across <invoice_count> invoice(s).
Invoices: <list invoice IDs>
Action: Verify payment with customer before responding.
````
