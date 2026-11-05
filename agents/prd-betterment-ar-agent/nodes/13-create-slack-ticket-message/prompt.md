# 13-create-slack-ticket-message: Create Slack Ticket Message

- Node ID: `cab5e608-b20c-4977-8d1e-7b00d1331b7f`
- Tool: `GPTAction_Custom__W4CH` (custom_gpt_tool)
- Model: `GEMINI_3_FLASH`, fallbacks: `GEMINI_3_1_PRO,GPT4_1,CLAUDE_4_SONNET`

## Objective

```text
Create the Slack message announcing the newly created Zendesk ticket
```

## Prompt

Source: `toolConfiguration.prompt`

````text
You are composing a Slack notification announcing a newly created Zendesk ticket
for the Betterment AR collections agent.

Use ONLY the data provided below — do not invent values. If a field is genuinely
missing, write "N/A".

**Inputs:**
- Ticket ID:        ```{ticket_id}```
- Subject:          ```{subject}```
- Requester name:   ```{requester_name}```
- Requester email:  ```{requester_email}```
- Ticket status:    ```{ticket_status}```
- Reminder count:   ```{reminder_count}```
- Email body:       ```{email_body}```

---

**Priority — derive from the notice level (reminder_count), NOT a Zendesk priority field:**
- First notice  (reminder_count = 0) -> Medium
- Second notice (reminder_count = 1) -> High
- Final notice  (reminder_count = 2) -> Urgent
If reminder_count is 3 or higher, treat it as a Final notice -> Urgent.

**Description:** Write ONE short sentence (max ~20 words) summarizing what the email
is about — the overdue invoice, the amount, and which notice this is. Derive it from
the email body. Do NOT paste the full email.

---

Output the message EXACTLY in this format — each field on its own line, nothing
before or after:

🎫 *New Zendesk Ticket:*
🆔 Ticket ID: <ticket_id>
📝 Subject: <subject>
👤 Requester: <requester_name> (<requester_email>)
⚡ Priority: <Medium | High | Urgent>
📌 Status: <ticket_status>
📄 Description: <one-sentence summary from the email>

Rules:
- Keep the field labels exactly as shown above.
- If both requester name and email are present, format as "Name (email)". If only the
  name is available (email could not be determined), show the name alone — no parentheses.
- Use the emoji shown at the start of each line; do not add any other emoji.
- Return ONLY the message text — no code fences, no commentary.
````
