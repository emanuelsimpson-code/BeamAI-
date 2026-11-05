# 18-payment-discrepancy-email: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `requester_name` | linked | yes | string |  | `01-trigger.output.requester_email` | ticket requester name from task query | param `43ee1947-732c-4d73-84f3-e165ec91270f`<br>output `81a274fd-0a33-475f-a967-48e405d693b1` |
| 1 | `total_amount_remaining` | ai_fill | yes | string |  |  | Verify node: sum of all outstanding invoice balances (already in dollars) | param `85c082fe-ce84-4482-8302-90503ea3ea04` |
| 2 | `invoice_count` | ai_fill | yes | string |  |  | Verify node: total number of invoices checked | param `008bacbf-6fd5-435c-acd1-3108a9b10990` |
| 3 | `invoices` | ai_fill | yes | string |  |  | Verify node: array of invoice    <br>  objects:                                    <br>id: Stripe invoice ID          <br>status: paid \| open<br>amount_due: dollars            <br>amount_paid: dollars<br>amount_remaining: dollars | param `3adaafd3-e4b6-4e42-9fed-e2f348214ae5` |
