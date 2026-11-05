# 12-verify-partial-payment: Verify Partial Payment

- Node ID: `38bd8599-0fe7-4570-9ad5-90bebc878430`
- Tool: `GPTAction_Custom_VerifyPartialPayment` (custom_gpt_tool)
- Model: `GPT4_1`, fallbacks: `GEMINI_3_1_PRO,CLAUDE_4_SONNET`

## Objective

```text
verify if the customer claimed invoices are paid
```

## Prompt

Source: `toolConfiguration.prompt`

````text
You are verifying a partial payment claim for a Betterment AR customer.                      
                                                                                               
  The customer replied saying they paid some invoices.                                         
  Stripe invoice data: ```{invoice_data}```         
  Customer reply: ```{customer_reply}```       
                                                                                               
  The data structure is: array → [index]["1"]["data"] for each invoice.
  Amount fields are in cents — divide by 100 for dollars.                                      
                                                                                               
  For each invoice extract: id, status, amount_due, amount_paid, amount_remaining (all ÷ 100). 
                                                                                               
  Return ONLY this JSON:                                                                       
  {                                                                                            
    "verification_status": "partial_verified" | "nothing_paid" | "all_paid",                   
    "invoices_paid": [{ "id": "...", "amount_paid": ... }],                                    
    "invoices_outstanding": [{ "id": "...", "amount_remaining": ... }],                        
    "total_amount_paid": <dollars>,                                    
    "total_amount_remaining": <dollars>,  
    "invoice_count_paid": <number>,                                                            
    "invoice_count_outstanding": <number>,                                                     
    "reasoning": "<one sentence>"                                                              
  }                                                                                            
                                          
  Rules:                                                                                       
  - "partial_verified" → at least one invoice paid AND at least one still open                 
  - "nothing_paid"     → all invoices still show amount_remaining > 0         
  - "all_paid"         → every invoice has amount_remaining = 0                                
  - Never return null or empty
````

## Tool template prompt

Source: `toolConfiguration.originalTool.prompt` (differs from the node prompt)

```text
You are verifying a partial payment claim for a Betterment AR customer.                      
                                                                                               
  The customer replied saying they paid some invoices.                                         
  Stripe invoice data:         
  Customer reply:       
                                                                                               
  The data structure is: array → [index]["1"]["data"] for each invoice.
  Amount fields are in cents — divide by 100 for dollars.                                      
                                                                                               
  For each invoice extract: id, status, amount_due, amount_paid, amount_remaining (all ÷ 100). 
                                                                                               
  Return ONLY this JSON:                                                                       
  {                                                                                            
    "verification_status": "partial_verified" | "nothing_paid" | "all_paid",                   
    "invoices_paid": [{ "id": "...", "amount_paid": ... }],                                    
    "invoices_outstanding": [{ "id": "...", "amount_remaining": ... }],                        
    "total_amount_paid": <dollars>,                                    
    "total_amount_remaining": <dollars>,  
    "invoice_count_paid": <number>,                                                            
    "invoice_count_outstanding": <number>,                                                     
    "reasoning": "<one sentence>"                                                              
  }                                                                                            
                                          
  Rules:                                                                                       
  - "partial_verified" → at least one invoice paid AND at least one still open                 
  - "nothing_paid"     → all invoices still show amount_remaining > 0         
  - "all_paid"         → every invoice has amount_remaining = 0                                
  - Never return null or empty
```

## Tool template prompt

Source: `toolConfiguration.originalTool.meta.prompt` (differs from the node prompt)

```text
You are verifying a partial payment claim for a Betterment AR customer.                      
                                                                                               
  The customer replied saying they paid some invoices.                                         
  Stripe invoice data:         
  Customer reply:       
                                                                                               
  The data structure is: array → [index]["1"]["data"] for each invoice.
  Amount fields are in cents — divide by 100 for dollars.                                      
                                                                                               
  For each invoice extract: id, status, amount_due, amount_paid, amount_remaining (all ÷ 100). 
                                                                                               
  Return ONLY this JSON:                                                                       
  {                                                                                            
    "verification_status": "partial_verified" | "nothing_paid" | "all_paid",                   
    "invoices_paid": [{ "id": "...", "amount_paid": ... }],                                    
    "invoices_outstanding": [{ "id": "...", "amount_remaining": ... }],                        
    "total_amount_paid": <dollars>,                                    
    "total_amount_remaining": <dollars>,  
    "invoice_count_paid": <number>,                                                            
    "invoice_count_outstanding": <number>,                                                     
    "reasoning": "<one sentence>"                                                              
  }                                                                                            
                                          
  Rules:                                                                                       
  - "partial_verified" → at least one invoice paid AND at least one still open                 
  - "nothing_paid"     → all invoices still show amount_remaining > 0         
  - "all_paid"         → every invoice has amount_remaining = 0                                
  - Never return null or empty
```
