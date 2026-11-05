# 19-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `text` | linked | yes | string |  | `16-code-executor.output.slack_message` | Message text | param `fcb7d6ad-7a6c-4c04-94e6-681630d82749`<br>output `8cc8a1cc-47ab-4a36-a60e-1351b1d000ef` |
| 1 | `mrkdwn` | static |  | boolean | true |  |  | param `f9f75717-822e-4c16-8694-afbeb63f025a` |
| 2 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | TODO (O6): AP review channel ID. Now the demo channel beamai-outreach. | param `cd916636-6965-4de3-8e95-d38169848e91` |
| 3 | `channelType` | static | yes | string | Channels |  | Public or private channel | param `86a9d85d-7707-406b-ab45-de6eb8d6643c` |
