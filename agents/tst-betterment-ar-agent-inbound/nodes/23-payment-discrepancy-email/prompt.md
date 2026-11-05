# 23-payment-discrepancy-email: Payment Discrepancy Email

- Node ID: `d751fb4a-f223-4da1-ac60-8f372fbdd92f`
- Tool: `GPTAction_Custom_PaymentDiscrepancyEmail` (custom_gpt_tool)
- Model: `GPT4_1`, fallbacks: `GEMINI_3_1_PRO,GPT4_1,CLAUDE_4_SONNET`

## Objective

```text
send email to the client saying that partial payment has been made
```

## Prompt

Source: `toolConfiguration.prompt`

````text
Generate the subject line and HTML email body for a partial payment acknowledgement.
                                                                                               
  **Input Parameters (sources):**         
  - requester_name: ```{requester_name}```           ← Extract the requester name from the email
   name (first name only)                                                                      
  - total_amount_remaining:  ```{total_amount_remaining}```   ← Verify node: sum of all
  outstanding invoice balances (already in dollars)                                            
  - invoice_count:     ```{invoice_count}```        ← Verify node: total number of     
  invoices checked                            
  - invoices:     ```{invoices}```                  ← Verify node: array of invoice    
  objects:                                    
                                                                id: Stripe invoice ID          
                                                                status: paid | open
                                                                amount_due: dollars            
                                                                amount_paid: dollars
                                                                amount_remaining: dollars      
                                              
  ---                                                                                          
                  
  ## Output Format                                                                             
   
  First line: SUBJECT: [subject line here]                                                     
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text
                                              
  ---                                     

  ## Invoice List Block                                                                        
  Render ONLY invoices where amount_remaining > 0.
                                                                                               
  IF outstanding invoices == 1:           
    <p>Invoice #[id] — $[amount_remaining]</p>
                                                                                               
  IF outstanding invoices > 1:                
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
  2. invoice_list_block: render ONLY invoices where amount_remaining > 0
  3. customer_first_name: first name only — e.g. "Michael" from "Michael Torres"
  4. HTML only: no markdown, no plain text                                      
  5. No wrappers: do not add <html>, <body>, or <div> — start with <p>                         
  6. amount_remaining is already in dollars — do NOT divide by 100    
  7. Strictly follow the template above
````

## Tool template prompt

Source: `toolConfiguration.originalTool.prompt` (differs from the node prompt)

````text
Generate the subject line and HTML email body for a partial payment acknowledgement.
                                                                                               
  **Input Parameters (sources):**         
  - requester_name: ```{requester_name}```           ← Zendesk webhook: ticket requester
   name (first name only)                                                                      
  - total_amount_remaining:  ```{total_amount_remaining}```   ← Verify node: sum of all
  outstanding invoice balances (already in dollars)                                            
  - invoice_count:     ```{invoice_count}```        ← Verify node: total number of     
  invoices checked                            
  - invoices:     ```{invoices}```                  ← Verify node: array of invoice    
  objects:                                    
                                                                id: Stripe invoice ID          
                                                                status: paid | open
                                                                amount_due: dollars            
                                                                amount_paid: dollars
                                                                amount_remaining: dollars      
                                              
  ---                                                                                          
                  
  ## Output Format                                                                             
   
  First line: SUBJECT: [subject line here]                                                     
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text
                                              
  ---                                     

  ## Invoice List Block                                                                        
  Render ONLY invoices where amount_remaining > 0.
                                                                                               
  IF outstanding invoices == 1:           
    <p>Invoice #[id] — $[amount_remaining]</p>
                                                                                               
  IF outstanding invoices > 1:                
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
  2. invoice_list_block: render ONLY invoices where amount_remaining > 0
  3. customer_first_name: first name only — e.g. "Michael" from "Michael Torres"
  4. HTML only: no markdown, no plain text                                      
  5. No wrappers: do not add <html>, <body>, or <div> — start with <p>                         
  6. amount_remaining is already in dollars — do NOT divide by 100    
  7. Strictly follow the template above
````

## Tool template prompt

Source: `toolConfiguration.originalTool.meta.prompt` (differs from the node prompt)

````text
Generate the subject line and HTML email body for a partial payment acknowledgement.
                                                                                               
  **Input Parameters (sources):**         
  - requester_name: ```{requester_name}```           ← Zendesk webhook: ticket requester
   name (first name only)                                                                      
  - total_amount_remaining:  ```{total_amount_remaining}```   ← Verify node: sum of all
  outstanding invoice balances (already in dollars)                                            
  - invoice_count:     ```{invoice_count}```        ← Verify node: total number of     
  invoices checked                            
  - invoices:     ```{invoices}```                  ← Verify node: array of invoice    
  objects:                                    
                                                                id: Stripe invoice ID          
                                                                status: paid | open
                                                                amount_due: dollars            
                                                                amount_paid: dollars
                                                                amount_remaining: dollars      
                                              
  ---                                                                                          
                  
  ## Output Format                                                                             
   
  First line: SUBJECT: [subject line here]                                                     
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text
                                              
  ---                                     

  ## Invoice List Block                                                                        
  Render ONLY invoices where amount_remaining > 0.
                                                                                               
  IF outstanding invoices == 1:           
    <p>Invoice #[id] — $[amount_remaining]</p>
                                                                                               
  IF outstanding invoices > 1:                
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
  2. invoice_list_block: render ONLY invoices where amount_remaining > 0
  3. customer_first_name: first name only — e.g. "Michael" from "Michael Torres"
  4. HTML only: no markdown, no plain text                                      
  5. No wrappers: do not add <html>, <body>, or <div> — start with <p>                         
  6. amount_remaining is already in dollars — do NOT divide by 100    
  7. Strictly follow the template above
````
