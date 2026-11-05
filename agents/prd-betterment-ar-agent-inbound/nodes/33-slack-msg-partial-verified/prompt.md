# 33-slack-msg-partial-verified: Slack Msg — partial_verified

- Node ID: `516e7a52-9d39-4f21-81ca-bf82cbff3d9f`
- Tool: `GPTAction_Custom__3Tig` (custom_gpt_tool)
- Model: `GEMINI_25_FLASH`, fallbacks: `GEMINI_3_1_PRO`

## Objective

```text
Create the Slack alert message — Partial payment confirmed
```

## Prompt

Source: `toolConfiguration.prompt`

````text
You are writing an INTERNAL Slack alert for the Betterment AR collections team about how
an inbound customer email reply was handled. Scenario: Partial payment confirmed.

Use ONLY the data provided below. If a field is missing, write "N/A". Be concise.

**Inputs:**
- Customer email thread: ```{email_body}```
- Requester:             ```{requester_email}```
- Ticket ID:             ```{ticket_id}```
- Invoice IDs:           ```{invoice_ids}```
- Invoice amount:        ```{invoice_amount}```
- Reply intent:          ```{reply_intent}```
- Verification result:   ```{verification_output}```

---

Output EXACTLY this format — each field on its own line, nothing before or after:

🔔 *AR Inbound — Partial payment confirmed*
👤 Customer: <requester_email or N/A>
🎫 Ticket: <ticket_id>
🧾 Invoice(s): <invoice_ids> · $<invoice_amount>
💬 Reply intent: <reply_intent>
🗣️ Customer said: <one-sentence paraphrase of the customer's MOST RECENT reply, max ~25 words>
🟡 Partial payment confirmed against Stripe — acknowledged to client.
📝 Action taken: Acknowledgement email sent to client.

Rules:
- "Customer said" must summarize ONLY the customer's latest message — paraphrase in your
  own words; do not quote the thread or include quoted history.
- Keep the labels and emoji exactly as shown above.
- Render the Outcome line verbatim: "🟡 Partial payment confirmed against Stripe — acknowledged to client."
- If invoice amount is a plain number, prefix it with $ and show two decimals.
- Return ONLY the message text — no code fences, no commentary.
````
