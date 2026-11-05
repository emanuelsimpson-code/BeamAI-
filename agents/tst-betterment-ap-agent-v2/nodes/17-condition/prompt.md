# 17-condition: Condition

- Node ID: `dc5cff47-8c5d-45ae-9461-85dfcb12f089`
- Tool: `-` (conditionNode)
- Model: `GEMINI_3_FLASH`

## Objective

```text
Proceed or route to a person?
```

## Branch conditions (llm_based)

| Branch to | Condition |
|---|---|
| `18-code-executor` | route from the Check the confidence step is exactly proceed. |
| `19-send-message` | route from the Check the confidence step is human, or any value that is not proceed. |
