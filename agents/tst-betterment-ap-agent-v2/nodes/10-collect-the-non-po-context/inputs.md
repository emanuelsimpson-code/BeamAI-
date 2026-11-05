# 10-collect-the-non-po-context: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `invoice` | linked | yes | object |  | `01-trigger.output.invoice` |  | param `7c6b07e7-3453-4178-a794-f21e8d339436`<br>output `260bab81-bfe0-4407-9b18-0977c083bed0` |
| 1 | `vendor_name` | linked | yes | string |  | `01-trigger.output.vendor_name` |  | param `1775ed86-f923-4ebd-8e53-deb01e619dca`<br>output `52313821-47a3-4a8e-899c-f3e18ddd0294` |
| 2 | `requester_history` | linked |  | object |  | `05-code-executor.output.requester_history` |  | param `3b18adf5-3c94-468c-b259-ae821dc7c2a6`<br>output `7999c5b8-b2d5-40ea-a40d-bf0cbc42ebe2` |
| 3 | `vendor_rules` | linked |  | string |  | `08-read-the-vendor-rules.output.vendor_rules` |  | param `9da8e507-0bda-4d8a-a810-d160b3479fb9`<br>output `1acf5293-81ba-4856-ad17-6b62450b8126` |
| 4 | `zip_url` | linked |  | string |  | `01-trigger.output.zip_url` |  | param `a99c70c5-a6c7-4642-b72a-0568baa46f88`<br>output `d047adb0-383e-44e5-8601-b33c56c3de38` |
