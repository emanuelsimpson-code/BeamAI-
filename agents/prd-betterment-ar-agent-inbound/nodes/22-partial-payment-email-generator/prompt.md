# 22-partial-payment-email-generator: Partial Payment Email Generator

- Node ID: `1a5742c2-3ba6-4b11-898f-eae05bfc7385`
- Tool: `GPTAction_Custom_PartialPaymentEmailGenerator` (custom_gpt_tool)
- Model: `GPT4_1`, fallbacks: `GEMINI_3_1_PRO,GPT4_1,CLAUDE_4_SONNET`

## Objective

```text
create the email for the client acknowledging the partial payment
```

## Prompt

Source: `toolConfiguration.prompt`

````text
Generate the subject line and HTML email body for a partial payment acknowledgement.         
                                                                                               
  **Input Parameters (sources):**                                                              
  - requester_name: ```{requester_name}```                    ← Extract the requester name from the email
  - total_amount_paid:  ```{total_amount_paid}```             ← Verify node: sum of all
   paid invoices in dollars                   
  - total_amount_remaining:  ```{total_amount_remaining}```   ← Verify node: sum of all
   outstanding invoices in dollars                                                             
  - invoice_count_outstanding: ```{invoice_count_outstanding}```   ← Verify node: number of invoices still open                                                                
  - invoices_outstanding: ```{invoices_outstanding}```        ← Verify node: array of  
  outstanding invoice objects:                                                               
         id: Stripe invoice ID                  
         amount_remaining:  dollars (already converted)                                                                
                                                                                               
  ---                                                                                        
                                                                                               
  ## Output Format                                                                           
                                                                                               
  First line: SUBJECT: [subject line here]    
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text    
                                                                                             
  ---                                                                                          
   
  ## Invoice List Block                                                                        
                                                                                             
  IF invoice_count_outstanding == 1:                                                           
    <p>Invoice #[id] — $[amount_remaining]</p>                                               
                                              
  IF invoice_count_outstanding > 1:                                                            
    <p>
    Invoice #[id_1] — $[amount_remaining_1]<br>                                                
    Invoice #[id_2] — $[amount_remaining_2]<br>                                              
    ... (one line per outstanding invoice)                                                     
    </p>                                                                                     
                                                                                               
  ---
                                                                                               
  ## Template — Partial Payment Acknowledgement                                              
                                                                                               
  SUBJECT: Re: Outstanding Balance — Partial Payment Received                                
                                          
  <p>Hi [customer_first_name],</p>
                                                                                               
  <p>Thank you for your recent payment. We wanted to let you know that we have applied
  it to your account; however, a remaining balance of                                          
  <strong>$[total_amount_remaining]</strong>                                                 
  is still outstanding.</p>               

  <p>Please see the open invoice(s) below:</p>                                                 
   
  [invoice_list_block]                                                                         
                                                                                             
  <p>Please reply to this message or remit payment at your earliest convenience.
  If you believe you are receiving this email in error, please email us at <a                  
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                               
  <p>Best,<br>                                                                               
  Betterment Accounts Receivable Team</p>
                                                                                               
  ---                                         
                                                                                               
  ## Formatting Rules                                                                        
                                                                                               
  1. Currency: always $X,XXX.XX — e.g. $1,500.00 not 1500 or 1500.0
  2. invoice_list_block: render ONLY invoices from invoices_outstanding array                  
  3. customer_first_name: first name only — e.g. "Michael" from "Michael Torres"             
  4. HTML only: no markdown, no plain text                                                     
  5. No wrappers: do not add <html>, <body>, or <div> — start with <p>
  6. amount_remaining is already in dollars — do NOT divide by 100                             
  7. Strictly follow the template above                                                        
  8. Do NOT mention invoices that have already been paid
````

## Tool template prompt

Source: `toolConfiguration.originalTool.prompt` (differs from the node prompt)

```text
Generate the subject line and HTML email body for a partial payment acknowledgement.         
                                                                                               
  **Input Parameters (sources):**                                                              
  - requester_name:                    ← Zendesk webhook: ticket
   requester full name                        
  - total_amount_paid:              ← Verify node: sum of all
   paid invoices in dollars                   
  - total_amount_remaining:    ← Verify node: sum of all
   outstanding invoices in dollars                                                             
  - invoice_count_outstanding:   ← Verify node:      
  number of invoices still open                                                                
  - invoices_outstanding:        ← Verify node: array of  
  outstanding invoice objects:                                                               
         id: Stripe invoice ID                  
         amount_remaining:  dollars (already converted)                                                                
                                                                                               
  ---                                                                                        
                                                                                               
  ## Output Format                                                                           
                                                                                               
  First line: SUBJECT: [subject line here]    
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text    
                                                                                             
  ---                                                                                          
   
  ## Invoice List Block                                                                        
                                                                                             
  IF invoice_count_outstanding == 1:                                                           
    <p>Invoice #[id] — $[amount_remaining]</p>                                               
                                              
  IF invoice_count_outstanding > 1:                                                            
    <p>
    Invoice #[id_1] — $[amount_remaining_1]<br>                                                
    Invoice #[id_2] — $[amount_remaining_2]<br>                                              
    ... (one line per outstanding invoice)                                                     
    </p>                                                                                     
                                                                                               
  ---
                                                                                               
  ## Template — Partial Payment Acknowledgement                                              
                                                                                               
  SUBJECT: Re: Outstanding Balance — Partial Payment Received                                
                                          
  <p>Hi [customer_first_name],</p>
                                                                                               
  <p>Thank you for your recent payment. We wanted to let you know that we have applied
  it to your account; however, a remaining balance of                                          
  <strong>$[total_amount_remaining]</strong>                                                 
  is still outstanding.</p>               

  <p>Please see the open invoice(s) below:</p>                                                 
   
  [invoice_list_block]                                                                         
                                                                                             
  <p>Please reply to this message or remit payment at your earliest convenience.
  If you believe you are receiving this email in error, please email us at <a                  
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                               
  <p>Best,<br>                                                                               
  Betterment Accounts Receivable Team</p>
                                                                                               
  ---                                         
                                                                                               
  ## Formatting Rules                                                                        
                                                                                               
  1. Currency: always $X,XXX.XX — e.g. $1,500.00 not 1500 or 1500.0
  2. invoice_list_block: render ONLY invoices from invoices_outstanding array                  
  3. customer_first_name: first name only — e.g. "Michael" from "Michael Torres"             
  4. HTML only: no markdown, no plain text                                                     
  5. No wrappers: do not add <html>, <body>, or <div> — start with <p>
  6. amount_remaining is already in dollars — do NOT divide by 100                             
  7. Strictly follow the template above                                                        
  8. Do NOT mention invoices that have already been paid
```

## Tool template prompt

Source: `toolConfiguration.originalTool.meta.prompt` (differs from the node prompt)

```text
Generate the subject line and HTML email body for a partial payment acknowledgement.         
                                                                                               
  **Input Parameters (sources):**                                                              
  - requester_name:                    ← Zendesk webhook: ticket
   requester full name                        
  - total_amount_paid:              ← Verify node: sum of all
   paid invoices in dollars                   
  - total_amount_remaining:    ← Verify node: sum of all
   outstanding invoices in dollars                                                             
  - invoice_count_outstanding:   ← Verify node:      
  number of invoices still open                                                                
  - invoices_outstanding:        ← Verify node: array of  
  outstanding invoice objects:                                                               
         id: Stripe invoice ID                  
         amount_remaining:  dollars (already converted)                                                                
                                                                                               
  ---                                                                                        
                                                                                               
  ## Output Format                                                                           
                                                                                               
  First line: SUBJECT: [subject line here]    
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text    
                                                                                             
  ---                                                                                          
   
  ## Invoice List Block                                                                        
                                                                                             
  IF invoice_count_outstanding == 1:                                                           
    <p>Invoice #[id] — $[amount_remaining]</p>                                               
                                              
  IF invoice_count_outstanding > 1:                                                            
    <p>
    Invoice #[id_1] — $[amount_remaining_1]<br>                                                
    Invoice #[id_2] — $[amount_remaining_2]<br>                                              
    ... (one line per outstanding invoice)                                                     
    </p>                                                                                     
                                                                                               
  ---
                                                                                               
  ## Template — Partial Payment Acknowledgement                                              
                                                                                               
  SUBJECT: Re: Outstanding Balance — Partial Payment Received                                
                                          
  <p>Hi [customer_first_name],</p>
                                                                                               
  <p>Thank you for your recent payment. We wanted to let you know that we have applied
  it to your account; however, a remaining balance of                                          
  <strong>$[total_amount_remaining]</strong>                                                 
  is still outstanding.</p>               

  <p>Please see the open invoice(s) below:</p>                                                 
   
  [invoice_list_block]                                                                         
                                                                                             
  <p>Please reply to this message or remit payment at your earliest convenience.
  If you believe you are receiving this email in error, please email us at <a                  
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                               
  <p>Best,<br>                                                                               
  Betterment Accounts Receivable Team</p>
                                                                                               
  ---                                         
                                                                                               
  ## Formatting Rules                                                                        
                                                                                               
  1. Currency: always $X,XXX.XX — e.g. $1,500.00 not 1500 or 1500.0
  2. invoice_list_block: render ONLY invoices from invoices_outstanding array                  
  3. customer_first_name: first name only — e.g. "Michael" from "Michael Torres"             
  4. HTML only: no markdown, no plain text                                                     
  5. No wrappers: do not add <html>, <body>, or <div> — start with <p>
  6. amount_remaining is already in dollars — do NOT divide by 100                             
  7. Strictly follow the template above                                                        
  8. Do NOT mention invoices that have already been paid
```
