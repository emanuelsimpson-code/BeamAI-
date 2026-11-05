# 13-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `text` | linked | yes | string |  | `10-collect-the-non-po-context.output.queue_message` | Message text | param `c6ba14a8-b98c-4855-8b1d-8e38b8bf5802`<br>output `ac8b0ce5-0ab3-42cc-995a-c4ae3e9657ff` |
| 1 | `mrkdwn` | static |  | boolean | true |  |  | param `90e819ef-ccd8-4e79-8f97-2fe6c195c196` |
| 2 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | TODO (O6): non-PO queue channel ID. Now the demo channel beamai-outreach. | param `07f3420b-bdbb-407e-a9f8-863d6e8149b0` |
| 3 | `channelType` | static | yes | string | Channels |  | Public or private channel | param `2e17db37-a83d-45ed-908f-b3922b0f120c` |
