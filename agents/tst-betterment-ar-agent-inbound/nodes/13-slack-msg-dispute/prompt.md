# 13-slack-msg-dispute: Slack Msg — dispute

- Node ID: `d1e01463-b31b-4499-8410-4a3a018e6cac`
- Tool: `GPTAction_Custom__hj9i` (custom_gpt_tool)
- Model: `GEMINI_3_FLASH`, fallbacks: `GEMINI_3_1_PRO,GPT4_1,CLAUDE_4_SONNET`

## Objective

```text
Create the Slack alert message — Invoice disputed
```

## Prompt

Source: `toolConfiguration.prompt`

````text
You are writing an INTERNAL Slack alert for the Betterment AR collections team about how
an inbound customer email reply was handled. Scenario: Invoice disputed.

Use ONLY the data provided below. If a field is missing, write "N/A". Be concise.

**Inputs:**
- Customer email thread: ```{email_body}```
- Requester:             ```{requester_email}```
- Ticket ID:             ```{ticket_id}```
- Invoice IDs:           ```{invoice_ids}```
- Invoice amount:        ```{invoice_amount}```
- Reply intent:          ```{reply_intent}```

---

Output EXACTLY this format — each field on its own line, nothing before or after:

🔔 *AR Inbound — Invoice disputed*
👤 Customer: <requester_email or N/A>
🎫 Ticket: <ticket_id>
🧾 Invoice(s): <invoice_ids> · $<invoice_amount>
💬 Reply intent: <reply_intent>
🗣️ Customer said: <one-sentence paraphrase of the customer's MOST RECENT reply, max ~25 words>
🚩 Customer disputes the invoice — needs team review.
📝 Action taken: Internal note added on Zendesk.

Rules:
- "Customer said" must summarize ONLY the customer's latest message — paraphrase in your
  own words; do not quote the thread or include quoted history.
- Keep the labels and emoji exactly as shown above.
- Render the Outcome line verbatim: "🚩 Customer disputes the invoice — needs team review."
- If invoice amount is a plain number, prefix it with $ and show two decimals.
- Return ONLY the message text — no code fences, no commentary.
````
