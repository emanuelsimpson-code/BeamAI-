# 10-verify-partial-payment: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `invoice_data` | linked | yes | string |  | `06-loop.output.data` | complete invoice data coming from the stripe | param `a7aedbd7-46c0-4953-ae75-656d8daca3d8`<br>output `325cd901-dd5e-41d6-92d9-0c1d3f8bb510` |
| 1 | `customer_reply` | ai_fill | yes | string |  |  | The complete email from the customer reply | param `a7e0a10c-8ae6-43b7-b321-438a8278b8e3` |
