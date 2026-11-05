# 07-update-ticket: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `ticket_id` | linked | yes | string |  | `06-create-ticket.output.data.audit.ticket_id` | The id of the ticket created in the previous step | param `36df9fd4-63a0-4c7f-9b37-560cf1807c46`<br>output `05bbe9d0-60b1-41b0-aabb-2ba819419b38` |
| 1 | `ticket.group_id` | static |  | number | 5465785715739 |  | value for ${group_id} | param `3bedbfd2-63e7-45d0-97dc-eb8b428977bd` |
| 2 | `ticket.brand_id` | static |  | number | 3465826 |  | value for ${brand_id} | param `afcb366e-9b88-45a2-9f57-cc38b14233e9` |
