# 39-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `e3a6b7ac-d42a-4428-b512-495b916ad829` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `fa460753-beaf-4a0f-9be9-c95b93ef7545` |
| 2 | `text` | linked | yes | string |  | `34-slack-msg-nothing-paid.output.slack_message` | use exactly the following template:<br><br>🚨 PAYMENT DISCREPANCY — {requester_name} ({requester_email})<br>  Claimed: Partial payment sent                                                                <br>  Stripe shows: $0 paid, ${total_amount_remaining} fully outstanding<br>  Ticket: {ticket_id}                                                                          <br>  Action: Contact customer to verify payment before responding.<br><br>use emojis where applicable | param `d3c2c94b-47c5-43be-adf2-6cabf1f1cfc3`<br>output `28ff8ef2-4741-4b03-9d0d-06cb02fec447` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | Not required please leave it empty | param `c3431062-71a0-41d0-9b85-9e1b3b00ac6f` |
| 4 | `post_at` | ai_fill |  | string |  |  | Not required please leave it empty | param `975b5124-3a05-4afe-a1af-856d2d45afa7` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | Not required please leave it empty | param `51c1ee09-4113-4257-9c2e-a2a62c7fbe45` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `4cc700d2-cbe0-4c27-bedf-408fa12660be` |
| 7 | `username` | ai_fill |  | string |  |  | Not required please leave it empty | param `d86d5765-fa39-4cef-b612-24cb0123c835` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | Not required please leave it empty | param `80ae3468-ef9c-48aa-9c07-9013f78de5ba` |
| 9 | `icon_url` | ai_fill |  | string |  |  | Not required please leave it empty | param `6c3f8f24-3804-40bd-8e54-348af6d0a50d` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `e821b8d0-95b4-4c0e-b2c1-be77acfcc987` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | Not required please leave it empty | param `bf3edfda-6c41-4eba-94a8-a42978e3bbee` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | Not required please leave it empty | param `ef67ec44-efc0-4921-8d23-a0f064a6dfd4` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `7c410577-3aa0-45c6-a19f-818cb4079313` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | Not required please leave it empty | param `34eb5b4b-97bd-4c7b-9587-47230355f74b` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | Not required please leave it empty | param `8f380f3c-ed8b-4346-9a4b-20076a2ce10e` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `afa08691-21fe-461e-a6f4-d89bb90bf727` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | Not required please leave it empty | param `c261b716-900e-473e-b0d7-2a223894ea7e` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | Not required please leave it empty | param `3b20aed2-ccf7-4db6-a991-d5aa48e8e126` |
