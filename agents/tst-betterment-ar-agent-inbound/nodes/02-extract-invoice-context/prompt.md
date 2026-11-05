# 02-extract-invoice-context: Extract invoice context

- Node ID: `76913c5b-6a4f-4cc4-98c7-4937a3293679`
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
Stripe Invoice Ids:
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
