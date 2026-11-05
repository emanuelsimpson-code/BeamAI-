# 35-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `1774e69c-b635-423d-92fd-8e3ec7e1cc9e` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `743badc8-4da3-4025-b4e4-1dcf31fa745a` |
| 2 | `text` | linked | yes | string |  | `30-slack-msg-nothing-paid.output.slack_message` | use exactly the following template:<br><br>🚨 PAYMENT DISCREPANCY — {requester_name} ({requester_email})<br>  Claimed: Partial payment sent                                                                <br>  Stripe shows: $0 paid, ${total_amount_remaining} fully outstanding<br>  Ticket: {ticket_id}                                                                          <br>  Action: Contact customer to verify payment before responding.<br><br>use emojis where applicable | param `0f5bac1c-a620-4e87-b15a-d62c395024cf`<br>output `a9c80e32-b408-4e7a-8e91-76af93563063` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | Not required please leave it empty | param `3939f48a-a646-4c4a-9d00-d16663f7020e` |
| 4 | `post_at` | ai_fill |  | string |  |  | Not required please leave it empty | param `48f8d9cb-7103-4678-b3be-88200ed5fabd` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | Not required please leave it empty | param `8e6a0696-2f8f-46de-acaa-0a66d81692d7` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `978ce2de-6244-4d25-8ad4-dd5a2018168a` |
| 7 | `username` | ai_fill |  | string |  |  | Not required please leave it empty | param `4f0f1c3e-71ad-46bd-92d8-d9c4db1b85c7` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | Not required please leave it empty | param `d1fc7791-904a-4ca7-aa9d-bdf110949d55` |
| 9 | `icon_url` | ai_fill |  | string |  |  | Not required please leave it empty | param `4541da47-8022-4b99-be5c-8eb328db7bca` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `8673d5b1-5212-46b1-806f-69d97a28e1eb` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | Not required please leave it empty | param `efd5c978-5ff0-46ac-962d-67e69dc7d279` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | Not required please leave it empty | param `50d17c1d-b923-4097-ae3d-da1fdf46b239` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `bd7a77ab-d970-4858-a923-39f52f0cf84a` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | Not required please leave it empty | param `275514e4-47ec-4e76-9c0e-e902912c09e6` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | Not required please leave it empty | param `2a0d6637-109d-4aab-9abd-c7b1937e3db5` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `203554ab-1dc4-45fd-9491-e0596250147d` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | Not required please leave it empty | param `6afc6ae6-48f1-48a4-9507-65c9bc1a5d6b` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | Not required please leave it empty | param `7af0bd01-b976-41e4-a3a5-6e228232b86e` |
