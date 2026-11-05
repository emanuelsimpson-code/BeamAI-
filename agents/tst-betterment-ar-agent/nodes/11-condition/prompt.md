# 11-condition: Condition

- Node ID: `fd6975de-c12c-47e8-8501-6e51a20f04ec`
- Tool: `-` (conditionNode)
- Model: `GEMINI_3_FLASH`

## Branch conditions (llm_based)

| Branch to | Condition |
|---|---|
| `12-end` | If value of invoice is less than 500 usd |
| `13-create-slack-ticket-message` | If value of invoice is greater than or equal to 500 usd |
