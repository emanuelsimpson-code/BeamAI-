# 16-condition: Condition

- Node ID: `b9f0de6a-d79c-4a11-b50a-2490d2b19e87`
- Tool: `-` (conditionNode)
- Model: `GEMINI_3_FLASH`

## Branch conditions (llm_based)

| Branch to | Condition |
|---|---|
| `21-note-msg-not-paid` | if the verification_status is not_paid |
| `22-payment-acknowledgement-generator` | if the verification_status is fully_paid |
| `23-payment-discrepancy-email` | if the verification_status partial |
