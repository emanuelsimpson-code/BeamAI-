# 17-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `a3b2941c-f63d-47ee-99cf-460c894986e2` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `a67250ac-9f1d-4720-9604-5156baadc899` |
| 2 | `text` | linked | yes | string |  | `13-slack-msg-dispute.output.slack_message` | Generate a Slack alert format exactly as:<br>"🚨 DISPUTE — {requester_name} ({requester_email})<br>  Invoice amount: ${invoice_amount}                 <br>  Reply: [first 200 characters of ticket_latest_comment]                                                                                        <br>  Ticket: {ticket_id}                                   <br>  Action: Do not reply to customer. Manual review required." | param `2a647cc9-1afd-46f6-aee4-7ab997a40078`<br>output `7cb46466-a85a-484f-bdc7-296f6c4eab2d` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `2966eadb-bb0e-4019-b691-56404c08a95a` |
| 4 | `post_at` | ai_fill |  | string |  |  | This is not required please leave it empty | param `f8b92f09-f657-4b8a-845b-4c57ed2311f4` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `2b0307d9-85c1-443a-abdd-087a4afb3142` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `e3d44c04-2a95-46c4-b36f-64164e0707db` |
| 7 | `username` | ai_fill |  | string |  |  | This is not required please leave it empty | param `e39db845-5cee-4ca6-baa6-ecc2d87006b6` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | This is not required please leave it empty | param `0fd9befd-c900-4617-a8c0-eca67f9244b5` |
| 9 | `icon_url` | ai_fill |  | string |  |  | This is not required please leave it empty | param `3b2a8a84-19a3-40b1-8444-0b467ec0304e` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `7dc7b591-0c8c-41d8-bc3a-e034278b8dd5` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | This is not required please leave it empty | param `992027ba-6d7a-465f-a5ce-274ceb1ddf6a` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `6442b1a6-844d-4bf7-8558-6f00ae975c28` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `763b3a81-f2a7-4d90-9ba0-dc10a34c6edd` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | This is not required please leave it empty | param `fd9d61da-04a6-4c2d-9b12-b32aa31d373b` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | This is not required please leave it empty | param `3897000f-ba4e-40a8-a446-68be2fa6362c` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `b2287fc3-e659-4217-9453-1159b0054b93` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `cbec0e01-356e-474c-a4bd-c1385b3cd398` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `8a221dbf-0dd5-41b3-bcd8-0f7d6f72ca5d` |
