# 17-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `59b2fff2-463a-4560-be61-3637aaf73748` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `1b64c723-cf4a-4e2f-bc1d-c5ebca15d979` |
| 2 | `text` | linked | yes | string |  | `13-slack-msg-dispute.output.slack_message` | Generate a Slack alert format exactly as:<br>"🚨 DISPUTE — {requester_name} ({requester_email})<br>  Invoice amount: ${invoice_amount}                 <br>  Reply: [first 200 characters of ticket_latest_comment]                                                                                        <br>  Ticket: {ticket_id}                                   <br>  Action: Do not reply to customer. Manual review required." | param `45261e71-165c-4007-9884-ad07224810ce`<br>output `87de3c73-1ee2-452e-bde9-7b95de4f3dc1` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `60fe69a7-f9ec-436e-a79a-caf3058dac2e` |
| 4 | `post_at` | ai_fill |  | string |  |  | This is not required please leave it empty | param `94fba960-98d4-4058-a886-52ec3eb98d58` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `e5849aa8-f6e8-43d0-8697-a38c6555af10` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `e473fa3b-e4fd-4387-9c3d-0f652dbc6092` |
| 7 | `username` | ai_fill |  | string |  |  | This is not required please leave it empty | param `0a3fbd5b-fe27-4f71-8a1e-f80e8e2670aa` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | This is not required please leave it empty | param `f900e4bb-1ae6-41aa-aa7b-f5c59da28145` |
| 9 | `icon_url` | ai_fill |  | string |  |  | This is not required please leave it empty | param `2bb4809d-f6d4-4d22-8d68-e31a2131ef9a` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `00928c9a-95a7-4ea1-ac31-c28127b9f946` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | This is not required please leave it empty | param `e624ba2e-78db-4589-bf87-22ead927154a` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `a39eaaaa-6fe0-4d36-84b7-989afad0d64b` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `3b849f0d-dc52-45c9-9694-265fdcbbc05f` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | This is not required please leave it empty | param `da6478df-b405-48ba-809f-e189cbc2b37f` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | This is not required please leave it empty | param `40e283a4-bbc7-41ea-8cda-ee5dd7025bd6` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `dd28c51b-9239-4bad-ba93-fc580ccdfc29` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `3fcd8f44-d0c0-4917-a0e8-964650d3ddb6` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `e7c39ada-84ad-4fba-a02e-db815c028581` |
