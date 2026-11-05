# 12-verify-partial-payment: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `invoice_data` | linked | yes | string |  | `08-loop.output.data` | complete invoice data coming from the stripe | param `6d919718-1d9e-4426-a8d7-9db755ae337c`<br>output `aab77db1-51a2-4d14-b3a6-c019e1b17039` |
| 1 | `customer_reply` | ai_fill | yes | string |  |  | The complete email from the customer reply | param `7322516d-cb42-4e71-a9f8-72e6bb6a13ec` |
