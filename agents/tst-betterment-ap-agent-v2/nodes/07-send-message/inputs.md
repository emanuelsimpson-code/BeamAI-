# 07-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `text` | linked | yes | string |  | `04-code-executor.output.archive_note` | Message text | param `e7d966fd-9109-4783-b260-c1d0ab0ff531`<br>output `114de811-874d-4dc1-a4e5-60a9662c7dc5` |
| 1 | `mrkdwn` | static |  | boolean | true |  |  | param `5ca08cbc-64fc-43b1-b572-3e7e999c31ee` |
| 2 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | TODO (O6): AP review channel ID. Now the demo channel beamai-outreach. | param `d7d78425-fc38-4b0f-beb3-2de3f222b8de` |
| 3 | `channelType` | static | yes | string | Channels |  | Public or private channel | param `207147d9-e535-4b6d-aa2c-8536fd48cb1a` |
