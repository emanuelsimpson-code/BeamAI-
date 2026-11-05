# 09-condition: Condition

- Node ID: `069f99cc-30aa-4ac8-862c-88fa5db1e981`
- Tool: `-` (conditionNode)
- Model: `GEMINI_3_FLASH`

## Objective

```text
PO-backed or non-PO?
```

## Branch conditions (llm_based)

| Branch to | Condition |
|---|---|
| `10-collect-the-non-po-context` | po_count from the Fetch the open POs step is 0. The vendor has no open PO. |
| `11-code-executor` | po_count from the Fetch the open POs step is exactly 1. The vendor has one open PO. |
| `12-score-the-open-pos` | po_count from the Fetch the open POs step is 2 or more. The vendor has several open POs. |
