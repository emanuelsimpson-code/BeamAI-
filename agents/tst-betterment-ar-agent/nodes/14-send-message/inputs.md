# 14-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `1530cdde-4111-4023-b0f7-574b95aef92b` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `a3f635d2-ffbc-433a-9981-bd6e95f67ec2` |
| 2 | `text` | linked | yes | string |  | `13-create-slack-ticket-message.output.slack_message` | Send a message notifying about the newly created Zendesk ticket. Format it exactly like this, with each field on its own line:<br><br>New Zendesk Ticket:<br>Ticket ID: [ticket id]<br>Subject: [subject]<br>Requester: [requester name/email]<br>Priority: [priority level]<br>Status: [status]<br>Description: [brief description from the email]<br>Extract all details from the email that generated the ticket.<br><br>Use emoji if applicable | param `df3b68cf-99dc-4517-a72b-b16f95bc2c87`<br>output `3461038b-867f-439e-a320-560a6b889f0f` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `4db1688e-8a7c-4a5b-b338-6abb5a535293` |
| 4 | `post_at` | ai_fill |  | string |  |  | This is not required please leave it empty | param `17ac8575-fa85-4b59-9c78-86e01ba1eb15` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `7a94f8e8-3209-41be-b696-52fcdd1efa38` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `70a732c7-b078-42c7-8f03-6b381d92d283` |
| 7 | `username` | ai_fill |  | string |  |  | This is not required please leave it empty | param `14b9d62e-21b2-4cab-81ba-8a49b648d6b5` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | This is not required please leave it empty | param `8b751dfa-9c2e-4126-8595-ae8323ac0929` |
| 9 | `icon_url` | ai_fill |  | string |  |  | The icon URL, found in Slack Bot configuration or previous node outputs and formatted as a URL (e.g., `https://example.com`). | param `89b2c265-251a-4677-bdaa-3deba1218889` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `9513fcd8-4d63-47fb-9192-87c3253fdd69` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | This is not required please leave it empty | param `94b2aea8-d0b7-487e-943c-dfed6b741342` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `f70ecb22-dac3-4ce7-9809-e1656653e84b` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `40409891-2424-433a-bb77-616c3d45484f` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | This is not required please leave it empty | param `18c17f60-62b8-400a-9065-6b038318ca4a` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | This is not required please leave it empty | param `720219dd-385d-4d43-b036-011ca7acddb8` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `ec8c8b3d-cb49-40b1-b4aa-b783f3d7ebf6` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `c440bdf3-603f-4352-a41b-fd19a961a18c` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `bea6b894-0829-42e3-b2a8-fc9c5beceedc` |
