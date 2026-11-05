# 23-payment-discrepancy-email: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `requester_name` | linked | yes | string |  | `01-trigger.output.requester_email` | ticket requester name from task query | param `9fe5faf3-c82f-4141-9adc-d135c134950f`<br>output `724f5c20-95f4-4798-a6c0-cacc58a3dd09` |
| 1 | `total_amount_remaining` | ai_fill | yes | string |  |  | Verify node: sum of all outstanding invoice balances (already in dollars) | param `71a004c8-9818-4b3a-8bde-3cc726be77aa` |
| 2 | `invoice_count` | ai_fill | yes | string |  |  | Verify node: total number of invoices checked | param `c0192f22-1981-4eef-a470-4546cf42e100` |
| 3 | `invoices` | ai_fill | yes | string |  |  | Verify node: array of invoice    <br>  objects:                                    <br>id: Stripe invoice ID          <br>status: paid \| open<br>amount_due: dollars            <br>amount_paid: dollars<br>amount_remaining: dollars | param `b39554bc-e1c1-4d5a-9001-4c81dd4142ed` |
