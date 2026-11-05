# 02-extract-invoice-context: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `stripe_invoice_ids` | linked | yes | string |  | `01-trigger.output.stripe_invoice_id` |  | param `839ab0f9-89a8-435a-ac32-1c7be54ec399`<br>output `e172e57c-a31c-42b7-a52c-fc03202be2b2` |
| 1 | `email_data` | linked | yes | string |  | `01-trigger.output.all_comments` | the entire email received in the payload | param `642fc13f-de76-4607-8f9a-c1a992a2d06a`<br>output `89443dd2-ac87-424b-94ce-4633066a4a75` |
