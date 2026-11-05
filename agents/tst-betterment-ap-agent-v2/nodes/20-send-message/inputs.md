# 20-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `text` | linked | yes | string |  | `16-code-executor.output.slack_message` | Message text | param `5c48a2a0-5754-421e-a98d-d553283c71b2`<br>output `8cc8a1cc-47ab-4a36-a60e-1351b1d000ef` |
| 1 | `mrkdwn` | static |  | boolean | true |  |  | param `5172e565-2437-4e0d-b0af-5e542f55ff22` |
| 2 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | TODO (O6): AP review channel ID. Now the demo channel beamai-outreach. | param `98dc8454-1e08-4bd6-b863-a27a61ee06b9` |
| 3 | `channelType` | static | yes | string | Channels |  | Public or private channel | param `02fcab8c-7fac-4219-87de-cff69be41084` |
