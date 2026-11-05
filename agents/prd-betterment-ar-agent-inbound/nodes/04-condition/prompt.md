# 04-condition: Condition

- Node ID: `b91aeddb-52cf-4da8-8572-48e71d90a025`
- Tool: `-` (conditionNode)
- Model: `GEMINI_3_FLASH`

## Branch conditions (llm_based)

| Branch to | Condition |
|---|---|
| `05-note-msg-dispute` | if reply_intent is dispute |
| `06-loop` | If reply_intent is payment_confirmed |
| `07-note-msg-wrong-contact` | if reply_intent is wrong_contact |
| `08-loop` | if reply_intent is partial_payment |
