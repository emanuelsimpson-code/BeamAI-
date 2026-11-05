# 11-condition: Condition

- Node ID: `02fb2eaf-f004-4606-873f-6f6c4409d921`
- Tool: `-` (conditionNode)
- Model: `GEMINI_3_1_PRO`, fallbacks: `GPT5`

## Branch conditions (llm_based)

| Branch to | Condition |
|---|---|
| `12-end` | If value of invoice is less than 500 usd |
| `13-create-slack-ticket-message` | If value of invoice is greater than or equal to 500 usd |
