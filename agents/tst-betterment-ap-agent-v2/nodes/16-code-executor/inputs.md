# 16-code-executor: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `confidence_threshold` | static |  | number | 0.90 |  | Decision D6. Betterment can change it. | param `3f288046-65df-4115-8640-63a892046fcc` |
| 1 | `decision` | linked | yes | object |  | `14-code-executor.output.decision` |  | param `992e07f7-5779-405f-879d-dc33363cf88b`<br>output `6e58df4c-7e90-4091-8568-82e9870649ec` |
| 2 | `bill` | linked | yes | object |  | `14-code-executor.output.bill` |  | param `43fe86cd-9f33-426b-8e8e-d900ae7be1e3`<br>output `f64750fb-f35e-44ba-8bf0-f471e9d57392` |
| 3 | `hard_rule_hit` | linked | yes | boolean |  | `15-code-executor.output.hard_rule_hit` |  | param `08e42d8a-bc53-40f4-a8a8-b0cc7bafa12a`<br>output `41fc3378-2d17-40d8-aba0-54d3041f1d4b` |
| 4 | `hard_rule_reasons` | linked |  | string |  | `15-code-executor.output.hard_rule_reasons` |  | param `67491c3f-f32f-4bc7-8837-038b5bf4cf25`<br>output `a7b518c9-cd26-4e54-b7b3-17aa4b9f9b87` |
| 5 | `vendor_name` | linked | yes | string |  | `01-trigger.output.vendor_name` |  | param `40c5dc35-bd63-4e9a-bedc-c4a1af5b7708`<br>output `52313821-47a3-4a8e-899c-f3e18ddd0294` |
| 6 | `invoice` | linked | yes | object |  | `01-trigger.output.invoice` |  | param `fb0a454f-6b87-477c-93de-874528151e0d`<br>output `260bab81-bfe0-4407-9b18-0977c083bed0` |
| 7 | `zip_url` | linked |  | string |  | `01-trigger.output.zip_url` |  | param `737d077d-d2b4-4eef-b890-f0d5afee0d5f`<br>output `d047adb0-383e-44e5-8601-b33c56c3de38` |
| 8 | `posting_date` | linked |  | string |  | `14-code-executor.output.posting_date` |  | param `eb599f57-6b95-4ce6-ac44-1b701d752bd5`<br>output `a07333da-8aca-4aa9-8973-29ecd00ca120` |
| 9 | `posting_rule` | linked |  | string |  | `14-code-executor.output.posting_rule` |  | param `170e203a-f2f1-47d8-995d-c09ddb7d6d61`<br>output `eb6b871e-7a51-42a0-bcd5-31176a04f243` |
