# 06-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `text` | linked | yes | string |  | `02-classify-the-document.output.handoff_message` | Message text | param `b76b598a-7aeb-4951-87ec-585e5d1f5d35`<br>output `c935cd13-1940-4194-85fa-1da50f88f691` |
| 1 | `mrkdwn` | static |  | boolean | true |  |  | param `ddf71b7b-7190-4d9e-9fec-fc169150a52b` |
| 2 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | TODO (O6): AP review channel ID. Now the demo channel beamai-outreach. | param `36d5c82e-b3f9-4e30-bf35-c63cbf10f5f9` |
| 3 | `channelType` | static | yes | string | Channels |  | Public or private channel | param `a42d6a71-1a44-45dd-b953-f4c99de27d91` |
