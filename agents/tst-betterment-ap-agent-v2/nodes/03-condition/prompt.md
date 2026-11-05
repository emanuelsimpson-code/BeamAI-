# 03-condition: Condition

- Node ID: `0ddd8da3-fd70-41ab-bc74-9622699a0f7b`
- Tool: `-` (conditionNode)

## Objective

```text
What type of document is it?
```

## Branch conditions (rule_based)

| Branch to | Condition |
|---|---|
| `04-code-executor` | Not an invoice (high confidence) (02-classify-the-document.output.doc_type equals 'not_invoice') |
| `05-code-executor` | Invoice (02-classify-the-document.output.doc_type equals 'invoice') |
| `06-send-message` | Suspected fraud or unclear: route to a person (02-classify-the-document.output.doc_type not_equals 'invoice' AND 02-classify-the-document.output.doc_type not_equals 'not_invoice') |
