# 22-payment-acknowledgement-generator: Payment Acknowledgement Generator

- Node ID: `67fe208c-f277-41ad-83a9-1a17ae3e289b`
- Tool: `GPTAction_Custom_PaymentAcknowledgementGenerator` (custom_gpt_tool)
- Model: `GEMINI_3_FLASH`, fallbacks: `GEMINI_3_1_PRO,GPT4_1,CLAUDE_4_SONNET`

## Objective

```text
Generate the email to be sent for acknowledgement of the completed paymenr
```

## Prompt

Source: `toolConfiguration.prompt`

````text
Generate the subject line and HTML email body for a full payment acknowledgement.
                                                                                   
  **Input Parameters (sources):**                                                                                                               
  - requester_name: ```{requester_name}```     ← Extract the requester name from the email
                                                                                                                                                
  ---                                                                                                                                           
                                                                                                                                                
  ## Output Format                                                                                                                              
                                                                                                                                                
  First line: SUBJECT: [subject line here]
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text                                                     
                                                                                           
  ---                                         
                                                                                                                                                
  ## Template — Full Payment Acknowledgement
                                                                                                                                                
  SUBJECT: Re: Outstanding Balance — Payment Confirmed
                                                                                                                                                
  <p>Hi [customer_first_name],</p>        
                                  
  <p>Thank you for your recent payment. Your account is currently up to date and no further action is required.</p>                             
                                                                                                                   
  <p>If you believe you are receiving this email in error, please email us at <a href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>     
                                                                                                                                           
  <p>Best,<br>                                                                                                                                  
  Betterment Accounts Receivable Team</p>
                                                                                                                                                
  ---             
                                                                                                                                                
  ## Formatting Rules
                     
  1. customer_first_name: first name only — e.g. "Michael" from "Michael Torres"
  2. HTML only: no markdown, no plain text                                      
  3. No wrappers: do not add <html>, <body>, or <div> — start with <p>
  4. Strictly follow the template above — do not add or remove any lines
````

## Tool template prompt

Source: `toolConfiguration.originalTool.prompt` (differs from the node prompt)

````text
Generate the subject line and HTML email body for a full payment acknowledgement.
                                                                                   
  **Input Parameters (sources):**                                                                                                               
  - requester_name: ```{requester_name}```     ← Zendesk webhook: ticket requester full name
                                                                                                                                                
  ---                                                                                                                                           
                                                                                                                                                
  ## Output Format                                                                                                                              
                                                                                                                                                
  First line: SUBJECT: [subject line here]
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text                                                     
                                                                                           
  ---                                         
                                                                                                                                                
  ## Template — Full Payment Acknowledgement
                                                                                                                                                
  SUBJECT: Re: Outstanding Balance — Payment Confirmed
                                                                                                                                                
  <p>Hi [customer_first_name],</p>        
                                  
  <p>Thank you for your recent payment. Your account is currently up to date and no further action is required.</p>                             
                                                                                                                   
  <p>If you believe you are receiving this email in error, please email us at <a href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>     
                                                                                                                                           
  <p>Best,<br>                                                                                                                                  
  Betterment Accounts Receivable Team</p>
                                                                                                                                                
  ---             
                                                                                                                                                
  ## Formatting Rules
                     
  1. customer_first_name: first name only — e.g. "Michael" from "Michael Torres"
  2. HTML only: no markdown, no plain text                                      
  3. No wrappers: do not add <html>, <body>, or <div> — start with <p>
  4. Strictly follow the template above — do not add or remove any lines
````

## Tool template prompt

Source: `toolConfiguration.originalTool.meta.prompt` (differs from the node prompt)

````text
Generate the subject line and HTML email body for a full payment acknowledgement.
                                                                                   
  **Input Parameters (sources):**                                                                                                               
  - requester_name: ```{requester_name}```     ← Zendesk webhook: ticket requester full name
                                                                                                                                                
  ---                                                                                                                                           
                                                                                                                                                
  ## Output Format                                                                                                                              
                                                                                                                                                
  First line: SUBJECT: [subject line here]
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text                                                     
                                                                                           
  ---                                         
                                                                                                                                                
  ## Template — Full Payment Acknowledgement
                                                                                                                                                
  SUBJECT: Re: Outstanding Balance — Payment Confirmed
                                                                                                                                                
  <p>Hi [customer_first_name],</p>        
                                  
  <p>Thank you for your recent payment. Your account is currently up to date and no further action is required.</p>                             
                                                                                                                   
  <p>If you believe you are receiving this email in error, please email us at <a href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>     
                                                                                                                                           
  <p>Best,<br>                                                                                                                                  
  Betterment Accounts Receivable Team</p>
                                                                                                                                                
  ---             
                                                                                                                                                
  ## Formatting Rules
                     
  1. customer_first_name: first name only — e.g. "Michael" from "Michael Torres"
  2. HTML only: no markdown, no plain text                                      
  3. No wrappers: do not add <html>, <body>, or <div> — start with <p>
  4. Strictly follow the template above — do not add or remove any lines
````
