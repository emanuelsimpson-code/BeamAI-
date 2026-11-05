# 02-extract-invoice-context: Extract invoice context

- Node ID: `f797e381-f62f-40a8-87c9-ba0fa862dc7c`
- Tool: `GPTAction_Custom_Extractinvoicecontext` (custom_gpt_tool)
- Model: `GEMINI_3_5_FLASH_LITE`, fallbacks: `GEMINI_3_1_PRO,GPT4_1,CLAUDE_4_SONNET`

## Objective

```text
Extract the invoice context
```

## Prompt

Source: `toolConfiguration.prompt`

````text
You are extracting invoice data from a Betterment AR collections email thread.
The original outreach email is quoted in the thread and always contains:
- "totaling $X,XXX.XX" — the invoice amount

Extract the following two fields from the email thread provided:
1. invoice_amount — the dollar amount as a number (no $ sign, e.g. 1000.00)
2. stripe_invoice_id — the ID string as in_XXXXXX

Please extract all stripe invoice ids and output them as list of strings as:
["Stripe_invoice_id_1", "Stripe_invoice_id_2", ....]
Input email thread:
```{email_data}``` 

stripe_invoice_ids:
```{stripe_invoice_ids}``` 
````

## Tool template prompt

Source: `toolConfiguration.originalTool.prompt` (differs from the node prompt)

````text
You are extracting invoice data from a Betterment AR collections email thread.
The original outreach email is quoted in the thread and always contains:
- "totaling $X,XXX.XX" — the invoice amount
- "Invoice #[ID] — Stripe Payment Link" — the Salesforce invoice ID
Extract the following two fields from the email thread provided:
1. invoice_amount — the dollar amount as a number (no $ sign, e.g. 1000.00)
2. salesforce_invoice_id — the ID string after "Invoice #" and before " — "
Input email thread:
```{email_data}``` 
````

## Tool template prompt

Source: `toolConfiguration.originalTool.meta.prompt` (differs from the node prompt)

````text
You are extracting invoice data from a Betterment AR collections email thread.
The original outreach email is quoted in the thread and always contains:
- "totaling $X,XXX.XX" — the invoice amount
- "Invoice #[ID] — Stripe Payment Link" — the Salesforce invoice ID
Extract the following two fields from the email thread provided:
1. invoice_amount — the dollar amount as a number (no $ sign, e.g. 1000.00)
2. salesforce_invoice_id — the ID string after "Invoice #" and before " — "
Input email thread:
```{email_data}``` 
````

## Evaluation criteria

```json
[
  "The 'invoice_amount' field must contain a string representing a numeric value corresponding exactly to the dollar amount specified in the email's 'totaling $X,XXX.XX' phrase, with no currency symbols, commas, or extraneous characters; the value must be a valid decimal number and match the amount in the email when parsed.",
  "The 'invoice_ids' field must contain a list of strings, each matching the pattern 'in_' followed by exactly six alphanumeric characters, extracted from the email, and include all such IDs present; the list must be complete, with no missing IDs, and each ID must conform to the specified format."
]
```
