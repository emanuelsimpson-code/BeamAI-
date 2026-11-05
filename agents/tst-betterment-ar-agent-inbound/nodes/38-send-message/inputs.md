# 38-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `8aed37e2-04ec-4e4c-947f-4f36bc59e5ca` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `8952cb6a-b467-4718-9d81-f3afdc356119` |
| 2 | `text` | linked | yes | string |  | `33-slack-msg-not-paid.output.slack_message` | Write a Slack alert using this exact format:<br>                                                                                               ⚠️  PAYMENT DISCREPANCY<br>Customer: {requester_name} ({requester_email})<br>Claimed: Payment confirmed                    <br>Stripe shows: ${total_amount_remaining} still outstanding<br>Ticket: {ticket_id}                                                                          <br>Action: Review and close manually. | param `29a77626-411e-4a12-a615-b521bb2bb312`<br>output `af2a23e8-ec77-4aea-bb1e-62d799ec4fb1` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `d56fff5c-94fd-4d7c-8a0c-698f29d15a15` |
| 4 | `post_at` | ai_fill |  | string |  |  | This is not required please leave it empty | param `f52ff047-606b-4ef9-8338-58297a2f390c` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `b487edd8-a6ed-4dd2-9e84-58f52750e6e8` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `e57c88fd-078b-4abe-9e86-ef5dc4c794de` |
| 7 | `username` | ai_fill |  | string |  |  | This is not required please leave it empty | param `ac8db75c-f24a-4574-a2dd-b57a131a25d4` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | This is not required please leave it empty | param `bdb1ae93-7c72-4d03-b0db-92d7f4c82fb1` |
| 9 | `icon_url` | ai_fill |  | string |  |  | This is not required please leave it empty | param `83e41d4b-1aae-45a4-92a1-fd94ba338e58` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `72d3fccd-3eed-48d4-b9f5-3eaa2f69a463` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | This is not required please leave it empty | param `bc86a073-e19e-41c5-b40f-ce22736c23dd` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `51eb8ed8-689d-44ce-8400-dee525ec80a5` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `9a79ebec-d77c-4916-ae16-2736c8b97e21` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | This is not required please leave it empty | param `4685965b-2ee1-45dd-89d5-83b85dc3d657` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | This is not required please leave it empty | param `e7261c1a-46e6-4b8e-bd96-2c59e3a1459f` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `65144da1-e989-4a42-8b72-258b3d7341de` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `99153c32-580f-4a1a-9193-5d8bcaae22ce` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `f0c9a878-4b2d-4f72-8f59-45dff7c31474` |
