# 04-condition: Condition

- Node ID: `8e4ba4b0-86d6-409e-bdca-2d4499026b8b`
- Tool: `-` (conditionNode)
- Model: `GEMINI_3_FLASH`

## Branch conditions (llm_based)

| Branch to | Condition |
|---|---|
| `05-note-msg-dispute` | if reply_intent is dispute |
| `06-loop` | if reply_intent is partial_payment |
| `07-note-msg-wrong-contact` | if reply_intent is wrong_contact |
| `08-loop` | If reply_intent is payment_confirmed |
