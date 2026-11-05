# 05-generate-email: Generate Email

- Node ID: `e1b98969-8978-4e42-9cf2-239ed53e65aa`
- Tool: `GPTAction_Custom_GenerateEmail` (custom_gpt_tool)
- Model: `GEMINI_3_FLASH`, fallbacks: `GEMINI_3_1_PRO,GPT4_1,CLAUDE_4_SONNET`

## Objective

```text
generate email to put on zendesk
```

## Prompt

Source: `toolConfiguration.prompt`

````text
Generate the subject line and HTML email body for an overdue invoice reminder.                                                    
   
 
 **Input Parameters (sources):**                                                                                                   
  - reminder_count: ```{reminder_count}```             ← Salesforce: Task_Index__c of next open Task on the Case
  - customer_first_name: ```{customer_name}```    ← Stripe: object.customer_name (extract first name only)
  - invoice_count: ```{invoice_count}```                 ← number of overdue invoices for this entity                                       
  - total_amount_due: ```{total_amount_due}```          ← sum of amount_due across all invoices             
  - invoices: ```{invoices}```                          ← array of objects, one per invoice:                                               
                                                      invoice_number: human-readable invoice number (e.g. SKB18OAG-0002)                       
                                                      days_overdue: integer                                                         
                                                      invoice_url: Stripe hosted_invoice_url
                                                                                                                                 
  ---                                                                                                                               
   
  ## Output Format                                                                                                                  
                  
  First line: SUBJECT: [subject line here]                                                                                          
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text
                                                                                                                                    
  ---             
                                                                                                                                    
  ## Decision Logic

    0        → First Notice    (action required, provide payment date)                                                              
    1         → Second Notice   (immediate payment required, deduction warning)
    2        → Final Notice    (urgent, 10 business days, deduction warning)                                                                                             
  ---                                                                                                                               
                                                                                                                                    
  ## Invoice List Block

  For all templates, render the invoices list as:                                                                                   
   
  IF invoice_count == 1:                                                                                                            
    <p>Invoice #[invoice_number] — <a href="[invoice_url]”>Stripe Payment Link</a></p>
                                                                                                                                    
  IF invoice_count > 1:                                                                                                             
    <p>                                                                                                                             
    Invoice #[invoice_number_1] — <a href="[invoice_url_1]">Stripe Payment Link</a><br>                                                  
    Invoice #[invoice_number_2] — <a href="[invoice_url_2]">Stripe Payment Link</a><br>                                                  
    ... (one line per invoice)
    </p>                                                                                                                            
                  
  ---                                                                                                                               
                  
  ## TEMPLATE 1: reminder_count == 0 — First Overdue Notice

  SUBJECT: Reminder: Regarding your outstanding Betterment invoice(s)                                                               
   
  <p>Hi [customer_first_name],</p>                                                                                                  
                  
  <p>According to our records, your Betterment invoice(s) totaling <strong>$ [total_amount_due]</strong> are overdue. Immediate      
  action is required. Confirm receipt of this email and provide a definitive date for when we can expect payment. If your plan is on
   Autopay, your payment method on file has failed. You must update your payment method and settle your invoice immediately using   
  the payment link(s) below or by accessing it within your plan sponsor dashboard:</p>

  [invoice_list_block]

  <p>If there is a better email for billing correspondence or further questions, please let us know at <a                           
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                                                                    
  <p>Best,<br>    
  Betterment Accounts Receivable Team</p>

  ---                                                                                                                               
   
  ## TEMPLATE 2: reminder_count == 1 — Second Overdue Notice                                                                   
                  
  SUBJECT: Second Notice: Regarding your outstanding Betterment invoice(s)

  <p>Hi [customer_first_name],</p>                                                                                                  
   
  <p>According to our records, your Betterment invoice(s) totaling <strong>$[total_amount_due]</strong> are overdue. Immediate      
  payment is required. Confirm receipt of this email and provide a payment date. If your plan is on Autopay, your payment method on
  file has failed. You must update your payment method and settle your invoice immediately using the payment link(s) below or by    
  accessing it within your plan sponsor dashboard:</p>

  [invoice_list_block]

  <p>Betterment will deduct the fees from plan assets in a per capita amount from each Participant if we do not hear from you. Refer
   to Section A (Service Fees) of your Betterment for Business Statement of Work for details.</p>
                                                                                                                                    
  <p>If there is a better email for billing correspondence or further questions, please let us know at <a                           
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                                                                    
  <p>Best,<br>    
  Betterment Accounts Receivable Team</p>

  ---

  ## TEMPLATE 3: reminder_count == 2 — Final Notice

  SUBJECT: Final Notice: Regarding your outstanding Betterment invoice(s)                                                           
   
  <p>Hi [customer_first_name],</p>                                                                                                  
                  
  <p>Your plan has <strong>[invoice_count] outstanding invoice(s) totaling $[total_amount_due]</strong>. We have reached out several
   times and have not yet received payment in regards to the invoice(s) that have been unpaid for [days_overdue] days or more.</p>
                                                                                                                                    
  <p>You have <strong>10 business days</strong> to reply to this message. Failure to pay will result in Betterment deducting fees   
  from plan assets in a per capita amount from each Participant. Please refer to Section A (Service Fees) of the Betterment for
  Business Statement of Work within your Betterment for Business Master Services Agreement for more details.</p>                    
                  
  [invoice_list_block]

  <p>If there is a better email for billing correspondence or further questions, please let us know at <a                           
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                                                                    
  <p>Best,<br>    
  Betterment Accounts Receivable Team</p>
                                                                                                                                    
  ---

  ## Formatting Rules

  1. Currency: always $X,XXX.XX — e.g. $649.04 not 64904 or 649                                                                     
  2. invoice_list_block: render using the Invoice List Block rules above — one line per invoice with Stripe Payment Link as a
  hyperlink                                                                                                                         
  3. customer_first_name: first name only — e.g. "Govind" from "Govind Balu - Employer"
  4. HTML only: no markdown, no plain text                                                                                          
  5. No wrappers: do not add <html>, <body>, or <div> — start with <p>
  6. amount_due from Stripe is in cents — divide by 100 before displaying                                                           
  7. Use invoice_number for invoice references (e.g. SKB18OAG-0002)                                           
  8. If invoice_count == 1: omit "totaling $[total_amount_due]" and use singular "invoice" throughout
  9. Please DONT forget to add the total_amount_due in the email.
  10. Strictly follow the templates
````

## Tool template prompt

Source: `toolConfiguration.originalTool.prompt` (differs from the node prompt)

````text
Generate the subject line and HTML email body for an overdue invoice reminder.                                                    
   
 
 **Input Parameters (sources):**                                                                                                   
  - reminder_count: ```{reminder_count}```             ← Salesforce: Task_Index__c of next open Task on the Case
  - customer_first_name: ```{customer_name}```    ← Stripe: object.customer_name (extract first name only)
  - invoice_count: ```{invoice_count}```                 ← number of overdue invoices for this entity                                       
  - total_amount_due: ```{total_amount_due}```          ← sum of amount_duacross all invoices ÷ 100 (cents → dollars)                    
  - invoices: ```{invoices}```                          ← array of objects, one per invoice:                                               
                                                      bill_name: Salesforce Bill__c.Name (e.g. DB5FB8E5-0004)                       
                                                      days_overdue: integer                                                         
                                                      invoice_url: Stripe hosted_invoice_url
                                                                                                                                 
  ---                                                                                                                               
   
  ## Output Format                                                                                                                  
                  
  First line: SUBJECT: [subject line here]                                                                                          
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text
                                                                                                                                    
  ---             
                                                                                                                                    
  ## Decision Logic

    0        → First Notice    (action required, provide payment date)                                                              
    1         → Second Notice   (immediate payment required, deduction warning)
    2        → Final Notice    (urgent, 10 business days, deduction warning)                                                                                             
  ---                                                                                                                               
                                                                                                                                    
  ## Invoice List Block

  For all templates, render the invoices list as:                                                                                   
   
  IF invoice_count == 1:                                                                                                            
    <p>Invoice #[bill_name] — <a href="[invoice_url]”>Stripe Payment Link</a></p>
                                                                                                                                    
  IF invoice_count > 1:                                                                                                             
    <p>                                                                                                                             
    Invoice #[bill_name_1] — <a href="[invoice_url_1]">Stripe Payment Link</a><br>                                                  
    Invoice #[bill_name_2] — <a href="[invoice_url_2]">Stripe Payment Link</a><br>                                                  
    ... (one line per invoice)
    </p>                                                                                                                            
                  
  ---                                                                                                                               
                  
  ## TEMPLATE 1: reminder_count == 0 — First Overdue Notice

  SUBJECT: Reminder: Regarding your outstanding Betterment invoice(s)                                                               
   
  <p>Hi [customer_first_name],</p>                                                                                                  
                  
  <p>According to our records, your Betterment invoice(s) totaling <strong>$ [total_amount_due]</strong> are overdue. Immediate      
  action is required. Confirm receipt of this email and provide a definitive date for when we can expect payment. If your plan is on
   Autopay, your payment method on file has failed. You must update your payment method and settle your invoice immediately using   
  the payment link(s) below or by accessing it within your plan sponsor dashboard:</p>

  [invoice_list_block]

  <p>If there is a better email for billing correspondence or further questions, please let us know at <a                           
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                                                                    
  <p>Best,<br>    
  Betterment Accounts Receivable Team</p>

  ---                                                                                                                               
   
  ## TEMPLATE 2: reminder_count == 1 — Second Overdue Notice                                                                   
                  
  SUBJECT: Second Notice: Regarding your outstanding Betterment invoice(s)

  <p>Hi [customer_first_name],</p>                                                                                                  
   
  <p>According to our records, your Betterment invoice(s) totaling <strong>$[total_amount_due]</strong> are overdue. Immediate      
  payment is required. Confirm receipt of this email and provide a payment date. If your plan is on Autopay, your payment method on
  file has failed. You must update your payment method and settle your invoice immediately using the payment link(s) below or by    
  accessing it within your plan sponsor dashboard:</p>

  [invoice_list_block]

  <p>Betterment will deduct the fees from plan assets in a per capita amount from each Participant if we do not hear from you. Refer
   to Section A (Service Fees) of your Betterment for Business Statement of Work for details.</p>
                                                                                                                                    
  <p>If there is a better email for billing correspondence or further questions, please let us know at <a                           
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                                                                    
  <p>Best,<br>    
  Betterment Accounts Receivable Team</p>

  ---

  ## TEMPLATE 3: reminder_count == 2 — Final Notice

  SUBJECT: Final Notice: Regarding your outstanding Betterment invoice(s)                                                           
   
  <p>Hi [customer_first_name],</p>                                                                                                  
                  
  <p>Your plan has <strong>[invoice_count] outstanding invoice(s) totaling $[total_amount_due]</strong>. We have reached out several
   times and have not yet received payment in regards to the invoice(s) that have been unpaid for [days_overdue] days or more.</p>
                                                                                                                                    
  <p>You have <strong>10 business days</strong> to reply to this message. Failure to pay will result in Betterment deducting fees   
  from plan assets in a per capita amount from each Participant. Please refer to Section A (Service Fees) of the Betterment for
  Business Statement of Work within your Betterment for Business Master Services Agreement for more details.</p>                    
                  
  [invoice_list_block]

  <p>If there is a better email for billing correspondence or further questions, please let us know at <a                           
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                                                                    
  <p>Best,<br>    
  Betterment Accounts Receivable Team</p>
                                                                                                                                    
  ---

  ## Formatting Rules

  1. Currency: always $X,XXX.XX — e.g. $649.04 not 64904 or 649                                                                     
  2. invoice_list_block: render using the Invoice List Block rules above — one line per invoice with Stripe Payment Link as a
  hyperlink                                                                                                                         
  3. customer_first_name: first name only — e.g. "Govind" from "Govind Balu - Employer"
  4. HTML only: no markdown, no plain text                                                                                          
  5. No wrappers: do not add <html>, <body>, or <div> — start with <p>
  6. amount_due from Stripe is in cents — divide by 100 before displaying                                                           
  7. Use Bill__c.Name for invoice references (e.g. DB5FB8E5-0004) — NOT Stripe in_xxx IDs                                           
  8. If invoice_count == 1: omit "totaling $[total_amount_due]" and use singular "invoice" throughout
  9. Please DONT forget to add the total_amount_due in the email.
  10. Strictly follow the templates
````

## Tool template prompt

Source: `toolConfiguration.originalTool.meta.prompt` (differs from the node prompt)

````text
Generate the subject line and HTML email body for an overdue invoice reminder.                                                    
   
 
 **Input Parameters (sources):**                                                                                                   
  - reminder_count: ```{reminder_count}```             ← Salesforce: Task_Index__c of next open Task on the Case
  - customer_first_name: ```{customer_name}```    ← Stripe: object.customer_name (extract first name only)
  - invoice_count: ```{invoice_count}```                 ← number of overdue invoices for this entity                                       
  - total_amount_due: ```{total_amount_due}```          ← sum of amount_duacross all invoices ÷ 100 (cents → dollars)                    
  - invoices: ```{invoices}```                          ← array of objects, one per invoice:                                               
                                                      bill_name: Salesforce Bill__c.Name (e.g. DB5FB8E5-0004)                       
                                                      days_overdue: integer                                                         
                                                      invoice_url: Stripe hosted_invoice_url
                                                                                                                                 
  ---                                                                                                                               
   
  ## Output Format                                                                                                                  
                  
  First line: SUBJECT: [subject line here]                                                                                          
  Remaining lines: HTML body only — pure HTML starting with <p>, no markdown, no plain text
                                                                                                                                    
  ---             
                                                                                                                                    
  ## Decision Logic

    0        → First Notice    (action required, provide payment date)                                                              
    1         → Second Notice   (immediate payment required, deduction warning)
    2        → Final Notice    (urgent, 10 business days, deduction warning)                                                                                             
  ---                                                                                                                               
                                                                                                                                    
  ## Invoice List Block

  For all templates, render the invoices list as:                                                                                   
   
  IF invoice_count == 1:                                                                                                            
    <p>Invoice #[bill_name] — <a href="[invoice_url]”>Stripe Payment Link</a></p>
                                                                                                                                    
  IF invoice_count > 1:                                                                                                             
    <p>                                                                                                                             
    Invoice #[bill_name_1] — <a href="[invoice_url_1]">Stripe Payment Link</a><br>                                                  
    Invoice #[bill_name_2] — <a href="[invoice_url_2]">Stripe Payment Link</a><br>                                                  
    ... (one line per invoice)
    </p>                                                                                                                            
                  
  ---                                                                                                                               
                  
  ## TEMPLATE 1: reminder_count == 0 — First Overdue Notice

  SUBJECT: Reminder: Regarding your outstanding Betterment invoice(s)                                                               
   
  <p>Hi [customer_first_name],</p>                                                                                                  
                  
  <p>According to our records, your Betterment invoice(s) totaling <strong>$ [total_amount_due]</strong> are overdue. Immediate      
  action is required. Confirm receipt of this email and provide a definitive date for when we can expect payment. If your plan is on
   Autopay, your payment method on file has failed. You must update your payment method and settle your invoice immediately using   
  the payment link(s) below or by accessing it within your plan sponsor dashboard:</p>

  [invoice_list_block]

  <p>If there is a better email for billing correspondence or further questions, please let us know at <a                           
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                                                                    
  <p>Best,<br>    
  Betterment Accounts Receivable Team</p>

  ---                                                                                                                               
   
  ## TEMPLATE 2: reminder_count == 1 — Second Overdue Notice                                                                   
                  
  SUBJECT: Second Notice: Regarding your outstanding Betterment invoice(s)

  <p>Hi [customer_first_name],</p>                                                                                                  
   
  <p>According to our records, your Betterment invoice(s) totaling <strong>$[total_amount_due]</strong> are overdue. Immediate      
  payment is required. Confirm receipt of this email and provide a payment date. If your plan is on Autopay, your payment method on
  file has failed. You must update your payment method and settle your invoice immediately using the payment link(s) below or by    
  accessing it within your plan sponsor dashboard:</p>

  [invoice_list_block]

  <p>Betterment will deduct the fees from plan assets in a per capita amount from each Participant if we do not hear from you. Refer
   to Section A (Service Fees) of your Betterment for Business Statement of Work for details.</p>
                                                                                                                                    
  <p>If there is a better email for billing correspondence or further questions, please let us know at <a                           
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                                                                    
  <p>Best,<br>    
  Betterment Accounts Receivable Team</p>

  ---

  ## TEMPLATE 3: reminder_count == 2 — Final Notice

  SUBJECT: Final Notice: Regarding your outstanding Betterment invoice(s)                                                           
   
  <p>Hi [customer_first_name],</p>                                                                                                  
                  
  <p>Your plan has <strong>[invoice_count] outstanding invoice(s) totaling $[total_amount_due]</strong>. We have reached out several
   times and have not yet received payment in regards to the invoice(s) that have been unpaid for [days_overdue] days or more.</p>
                                                                                                                                    
  <p>You have <strong>10 business days</strong> to reply to this message. Failure to pay will result in Betterment deducting fees   
  from plan assets in a per capita amount from each Participant. Please refer to Section A (Service Fees) of the Betterment for
  Business Statement of Work within your Betterment for Business Master Services Agreement for more details.</p>                    
                  
  [invoice_list_block]

  <p>If there is a better email for billing correspondence or further questions, please let us know at <a                           
  href="mailto:ar@betterment.com">ar@betterment.com</a>.</p>
                                                                                                                                    
  <p>Best,<br>    
  Betterment Accounts Receivable Team</p>
                                                                                                                                    
  ---

  ## Formatting Rules

  1. Currency: always $X,XXX.XX — e.g. $649.04 not 64904 or 649                                                                     
  2. invoice_list_block: render using the Invoice List Block rules above — one line per invoice with Stripe Payment Link as a
  hyperlink                                                                                                                         
  3. customer_first_name: first name only — e.g. "Govind" from "Govind Balu - Employer"
  4. HTML only: no markdown, no plain text                                                                                          
  5. No wrappers: do not add <html>, <body>, or <div> — start with <p>
  6. amount_due from Stripe is in cents — divide by 100 before displaying                                                           
  7. Use Bill__c.Name for invoice references (e.g. DB5FB8E5-0004) — NOT Stripe in_xxx IDs                                           
  8. If invoice_count == 1: omit "totaling $[total_amount_due]" and use singular "invoice" throughout
  9. Please DONT forget to add the total_amount_due in the email.
  10. Strictly follow the templates
````
