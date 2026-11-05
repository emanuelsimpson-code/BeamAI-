# 07-update-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `06-create-ticket.output.data.audit.ticket_id` | The id of the ticket created in the previous step | param `5cd00991-770c-4a75-917e-0deb3c4b81e2`<br>output `2a6fa0ad-cb7c-41be-8f68-6e394113ef57` |
| 1 | `ticket.group_id` | static |  | number | 45472631317019 |  | value for ${group_id} | param `e47659fd-d4cf-491b-8184-4f403c7dcd1c` |
| 2 | `ticket.brand_id` | static |  | number | 45472631271067 |  | value for ${brand_id} | param `f02e3d5c-3808-488f-b0c7-6e03cf948c16` |
