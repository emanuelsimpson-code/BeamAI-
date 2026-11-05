# 34-slack-msg-partial: Slack Msg — partial

- Node ID: `b4f846dd-79f4-4be9-a8b4-2c9b06952f5c`
- Tool: `GPTAction_Custom__JQdE` (custom_gpt_tool)
- Model: `GEMINI_3_FLASH`, fallbacks: `GEMINI_3_1_PRO,GPT4_1,CLAUDE_4_SONNET`

## Objective

```text
Create the Slack alert message — Payment claimed — only partial found
```

## Prompt

Source: `toolConfiguration.prompt`

````text
You are writing an INTERNAL Slack alert for the Betterment AR collections team about how
an inbound customer email reply was handled. Scenario: Payment claimed — only partial found.

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

🔔 *AR Inbound — Payment claimed — only partial found*
👤 Customer: <requester_email or N/A>
🎫 Ticket: <ticket_id>
🧾 Invoice(s): <invoice_ids> · $<invoice_amount>
💬 Reply intent: <reply_intent>
🗣️ Customer said: <one-sentence paraphrase of the customer's MOST RECENT reply, max ~25 words>
🟡 Customer claimed full payment, but only a partial payment was found — discrepancy emailed to client.
📝 Action taken: Discrepancy email sent to client.

Rules:
- "Customer said" must summarize ONLY the customer's latest message — paraphrase in your
  own words; do not quote the thread or include quoted history.
- Keep the labels and emoji exactly as shown above.
- Render the Outcome line verbatim: "🟡 Customer claimed full payment, but only a partial payment was found — discrepancy emailed to client."
- If invoice amount is a plain number, prefix it with $ and show two decimals.
- Return ONLY the message text — no code fences, no commentary.
````
