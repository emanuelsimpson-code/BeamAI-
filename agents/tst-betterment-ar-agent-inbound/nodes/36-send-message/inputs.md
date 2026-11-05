# 36-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `2e0a1c7f-4758-4a6d-889e-974f09567486` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `028cbbab-65c4-40af-96b9-4f4ffdcf7cc8` |
| 2 | `text` | linked | yes | string |  | `31-slack-msg-partial-verified.output.slack_message` | Please send the slack message in the following format:<br><br>PARTIAL PAYMENT — {requester_name} ({requester_email})                                   <br>  Paid: ${total_amount_paid}                                                                   <br>  Still owed: ${total_amount_remaining}       <br>  Invoices cleared: {invoice_count_paid} \| Still open: {invoice_count_outstanding}             <br>  Outstanding: [list invoice IDs from invoices_outstanding, comma separated]      <br>  Ticket: {ticket_id}                                                                          <br>  Action: Monitor for remaining payment.<br><br><br>Use emojis where applicable | param `2e93a760-90ae-4088-a119-e33d2fa72dcd`<br>output `0800a69b-c561-4482-9b1a-2eab2e1ebffc` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | Please leave these empty | param `0cde928f-cc57-4757-a75c-ef649c760747` |
| 4 | `post_at` | ai_fill |  | string |  |  | Please leave these empty | param `28e97915-5f50-4d26-81d8-3d12c9198f3d` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | Please leave these empty | param `ff6b5224-3e0a-4940-807a-093059a33272` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `fbf03338-933c-4469-b6c4-c673a8c92da5` |
| 7 | `username` | ai_fill |  | string |  |  | Please leave these empty | param `9f6e0ee9-0668-48a6-88c4-f83c17d7013f` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | Please leave these empty | param `9e9b9e1e-4321-45d9-8222-462b92b7dbbb` |
| 9 | `icon_url` | ai_fill |  | string |  |  | Please leave these empty | param `3942c922-8bcb-468e-a776-2abacc99a60c` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `c1444271-f631-4562-a95f-d2164476655e` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | Please leave these empty | param `49924544-6254-4888-88c0-5c5125cabdf4` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | Please leave these empty | param `e65ce0e1-1603-4e96-94c7-e2ddb70e6e1e` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `66cc8e53-27cc-4176-8083-36e257c10d31` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | Please leave these empty | param `0d4ad07d-49cd-4546-a8bb-882af23376ab` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | Please leave these empty | param `dc99319c-6d32-43de-851c-f5cd8e83433f` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `a2c2eb16-45c8-4127-b2f5-f0ab378a135e` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | Please leave these empty | param `b3755ebc-cb6f-4c17-a1ed-275d90beeb38` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | Please leave these empty | param `56a52d6f-7ca0-44cc-bde1-83dd5e0c0d43` |
