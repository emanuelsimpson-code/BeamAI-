# 36-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `c8a390fe-ec03-4704-8809-5869f095e96f` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `c983aecd-9c72-4909-8d6e-5f2e967fd633` |
| 2 | `text` | linked | yes | string |  | `31-slack-msg-not-paid.output.slack_message` | Write a Slack alert using this exact format:<br>                                                                                               ⚠️  PAYMENT DISCREPANCY<br>Customer: {requester_name} ({requester_email})<br>Claimed: Payment confirmed                    <br>Stripe shows: ${total_amount_remaining} still outstanding<br>Ticket: {ticket_id}                                                                          <br>Action: Review and close manually. | param `0ec65828-bba7-4e1b-932c-1b8e89fe9afb`<br>output `94742433-6b4b-4a50-a61d-ca2cf505d3f4` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `ae254255-72bf-44a2-a727-b8ea542b88dd` |
| 4 | `post_at` | ai_fill |  | string |  |  | This is not required please leave it empty | param `9ff8c1bd-d7a1-4691-b4c5-19dba21addff` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `1c555dcf-d02f-476f-bf17-26a3a9569fc4` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `e12ba821-e59b-4e2e-9d12-76953312a8a5` |
| 7 | `username` | ai_fill |  | string |  |  | This is not required please leave it empty | param `fd01a306-f204-4b7a-8c89-5f366c5495d8` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | This is not required please leave it empty | param `deda1d08-c2be-412c-858d-8b96b2b1cbbb` |
| 9 | `icon_url` | ai_fill |  | string |  |  | This is not required please leave it empty | param `4d96dd7e-8492-4bf7-8bf3-63096456b163` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `b7f1e733-52ac-462f-a2ee-b8f4619a8801` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | This is not required please leave it empty | param `ddde9c12-d29b-491e-9552-76c98161fc72` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `8ce7cb2f-e618-4471-8e61-d05ddc7ea0e6` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `bb3da318-16d7-4fba-bd7c-036eb51b09c5` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | This is not required please leave it empty | param `e6c01eed-c11d-4ccd-89ad-8eccb27fb2a7` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | This is not required please leave it empty | param `fa14d484-5583-42c1-bd62-7e3a6091ff68` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `30bed3ef-787d-4954-a341-19833185b7bc` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `6d0b955c-838d-4aaa-8121-b1c78f2ed462` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `6e6bf65c-1f0e-4a36-a938-ab844fc8e83b` |
