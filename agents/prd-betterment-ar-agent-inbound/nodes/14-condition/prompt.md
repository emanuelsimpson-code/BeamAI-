# 14-condition: Condition

- Node ID: `e30f654e-1786-4318-be37-0821f39f0a6c`
- Tool: `-` (conditionNode)
- Model: `GEMINI_3_FLASH`

## Branch conditions (llm_based)

| Branch to | Condition |
|---|---|
| `18-payment-discrepancy-email` | if the verification_status partial |
| `19-note-msg-not-paid` | if the verification_status is not_paid |
| `20-payment-acknowledgement-generator` | if the verification_status is fully_paid |
