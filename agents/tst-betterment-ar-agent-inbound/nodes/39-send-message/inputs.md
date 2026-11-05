# 39-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `255868f4-262c-40b1-bf2c-b974a94e8059` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `2e85d867-907b-4eb1-a59b-eb94973cc9c6` |
| 2 | `text` | linked | yes | string |  | `34-slack-msg-partial.output.slack_message` | use the exact slack message template<br><br>⚠️  PAYMENT DISCREPANCY — {requester_name} ({requester_email})                               <br>  Customer claimed full payment but Stripe shows partial.<br>  Paid: ${total_amount_paid}                                                                   <br>  Still owed: ${total_amount_remaining}   <br>  Outstanding invoices: [list IDs where amount_remaining > 0]<br>  Ticket: {ticket_id}                                                                          <br>  Action: Review and contact customer before closing.<br><br>use emojis where ever applicable | param `93f532eb-b9eb-4160-8736-d607a40c1c13`<br>output `7c7973a2-93ee-4d59-b10f-8b56e7bbf0ab` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `1dff3c04-f145-4690-a286-9ef028b41e4c` |
| 4 | `post_at` | ai_fill |  | string |  |  | This is not required please leave it empty | param `ff87f7b3-8f9b-4455-a397-83763131ee59` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `2edf5a84-5aeb-49bf-b94b-a454aeba39a5` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `462aa643-b9b1-4be1-999c-86887f43db3e` |
| 7 | `username` | ai_fill |  | string |  |  | This is not required please leave it empty | param `c928e4ed-999b-42ae-bfa3-879ab1af6f8a` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | This is not required please leave it empty | param `8ba50e29-d245-49e3-bcb9-a2d9d3474db0` |
| 9 | `icon_url` | ai_fill |  | string |  |  | This is not required please leave it empty | param `254a7dd7-95ef-46bd-82b7-b6d06bcced7a` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `b536f85e-1122-4659-a894-1cf7a0d5e1de` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | This is not required please leave it empty | param `10e0024c-3ef7-4fa1-adbb-5e7b53631ca6` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `020dc546-408c-4176-a1d4-c5d8acb0da7c` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `04cb70fd-6216-49fb-bf94-6067be5e4778` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | This is not required please leave it empty | param `53f32991-15cf-46d1-9e0a-f13811d0279c` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | This is not required please leave it empty | param `e93fa951-3e4f-437e-951c-517564c8ed50` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `91c5ba6d-99fe-47e1-9e6a-3c73c0e831b6` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `937aa03a-7e00-497a-afa5-01ff9c8db33e` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `f4966da7-3f46-4c81-94aa-96b02a6e85b2` |
