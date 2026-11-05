# 03-intent-classifier: Intent Classifier

- Node ID: `a1b7b7ff-fa67-4d80-9130-221c14932434`
- Tool: `GPTAction_Custom_IntentClassifier_wVjn` (custom_gpt_tool)
- Model: `GPT4_1_MINI`, fallbacks: `GEMINI_3_1_PRO,GPT4_1,CLAUDE_4_SONNET`

## Objective

```text
Classify the intent of the email
```

## Prompt

Source: `toolConfiguration.prompt`

````text
You are classifying the intent of a customer's reply to a Betterment AR collections email.
Please read the entire email thread to figure out the intent of the customer. To arrive at the right conclusion read the entire thread and then make the decision

Invoice amount on file: ```{invoice_amount}``` 
Customer reply thread: ```{email_body}``` 
---
Return EXACTLY one of these values as reply_intent:
payment_confirmed  — customer states they paid in full, references a payment matching
                     or exceeding the invoice amount, or attaches proof of payment
partial_payment    — customer paid less than the full amount, mentions a partial
                     amount, or requests a payment plan
dispute            — customer disagrees with the invoice, says they don't owe it,
                     or requests investigation
bankruptcy         — customer mentions bankruptcy, insolvency, chapter 7, chapter 11,
                     receivership, or legal proceedings
wrong_contact      — customer says wrong person, wrong email, or asks to update
                     the billing contact
general_inquiry    — question, invoice copy request, or anything else
---
Decision order (check top to bottom, first match wins):
1. BANKRUPTCY — keywords: "bankruptcy", "bankrupt", "chapter 7", "chapter 11",
   "insolvent", "receivership", "automatic stay"
2. DISPUTE — keywords: "do not owe", "don't owe", "dispute", "billing error",
   "incorrect invoice", "wrong amount", "we have no record", "please investigate"
3. WRONG CONTACT — keywords: "wrong person", "wrong email", "not the right contact",
   "no longer handle billing", "please update", "forward to"
4. PAYMENT — extract any dollar amount mentioned in the customer's reply:
   IF stated amount >= invoice_amount → payment_confirmed
   IF stated amount < invoice_amount  → partial_payment
   IF no amount but says "paid", "payment sent", "please find attached" → payment_confirmed
   IF says "partial", "payment plan", "can only pay" → partial_payment
5. FALLBACK → general_inquiry
---
Rules:
- ALWAYS check bankruptcy first — it overrides everything else
- Read only the customer's reply, not the quoted original email below
- Never return empty or null
- Only return one of the 6 exact values listed above
````

## Tool template prompt

Source: `toolConfiguration.originalTool.prompt` (differs from the node prompt)

````text
You are classifying the intent of a customer's reply to a Betterment AR collections email.
The customer's reply is at the TOP of the email thread (above the quoted original email).
Read ONLY the customer's reply text — ignore the quoted section below it.
Invoice amount on file: ```{invoice_amount}``` 
Customer reply thread: ```{email_body}``` 
---
Return EXACTLY one of these values as reply_intent:
payment_confirmed  — customer states they paid in full, references a payment matching
                     or exceeding the invoice amount, or attaches proof of payment
partial_payment    — customer paid less than the full amount, mentions a partial
                     amount, or requests a payment plan
dispute            — customer disagrees with the invoice, says they don't owe it,
                     or requests investigation
bankruptcy         — customer mentions bankruptcy, insolvency, chapter 7, chapter 11,
                     receivership, or legal proceedings
wrong_contact      — customer says wrong person, wrong email, or asks to update
                     the billing contact
general_inquiry    — question, invoice copy request, or anything else
---
Decision order (check top to bottom, first match wins):
1. BANKRUPTCY — keywords: "bankruptcy", "bankrupt", "chapter 7", "chapter 11",
   "insolvent", "receivership", "automatic stay"
2. DISPUTE — keywords: "do not owe", "don't owe", "dispute", "billing error",
   "incorrect invoice", "wrong amount", "we have no record", "please investigate"
3. WRONG CONTACT — keywords: "wrong person", "wrong email", "not the right contact",
   "no longer handle billing", "please update", "forward to"
4. PAYMENT — extract any dollar amount mentioned in the customer's reply:
   IF stated amount >= invoice_amount → payment_confirmed
   IF stated amount < invoice_amount  → partial_payment
   IF no amount but says "paid", "payment sent", "please find attached" → payment_confirmed
   IF says "partial", "payment plan", "can only pay" → partial_payment
5. FALLBACK → general_inquiry
---
Rules:
- ALWAYS check bankruptcy first — it overrides everything else
- Read only the customer's reply, not the quoted original email below
- Never return empty or null
- Only return one of the 6 exact values listed above
````

## Tool template prompt

Source: `toolConfiguration.originalTool.meta.prompt` (differs from the node prompt)

````text
You are classifying the intent of a customer's reply to a Betterment AR collections email.
The customer's reply is at the TOP of the email thread (above the quoted original email).
Read ONLY the customer's reply text — ignore the quoted section below it.
Invoice amount on file: ```{invoice_amount}``` 
Customer reply thread: ```{email_body}``` 
---
Return EXACTLY one of these values as reply_intent:
payment_confirmed  — customer states they paid in full, references a payment matching
                     or exceeding the invoice amount, or attaches proof of payment
partial_payment    — customer paid less than the full amount, mentions a partial
                     amount, or requests a payment plan
dispute            — customer disagrees with the invoice, says they don't owe it,
                     or requests investigation
bankruptcy         — customer mentions bankruptcy, insolvency, chapter 7, chapter 11,
                     receivership, or legal proceedings
wrong_contact      — customer says wrong person, wrong email, or asks to update
                     the billing contact
general_inquiry    — question, invoice copy request, or anything else
---
Decision order (check top to bottom, first match wins):
1. BANKRUPTCY — keywords: "bankruptcy", "bankrupt", "chapter 7", "chapter 11",
   "insolvent", "receivership", "automatic stay"
2. DISPUTE — keywords: "do not owe", "don't owe", "dispute", "billing error",
   "incorrect invoice", "wrong amount", "we have no record", "please investigate"
3. WRONG CONTACT — keywords: "wrong person", "wrong email", "not the right contact",
   "no longer handle billing", "please update", "forward to"
4. PAYMENT — extract any dollar amount mentioned in the customer's reply:
   IF stated amount >= invoice_amount → payment_confirmed
   IF stated amount < invoice_amount  → partial_payment
   IF no amount but says "paid", "payment sent", "please find attached" → payment_confirmed
   IF says "partial", "payment plan", "can only pay" → partial_payment
5. FALLBACK → general_inquiry
---
Rules:
- ALWAYS check bankruptcy first — it overrides everything else
- Read only the customer's reply, not the quoted original email below
- Never return empty or null
- Only return one of the 6 exact values listed above
````
