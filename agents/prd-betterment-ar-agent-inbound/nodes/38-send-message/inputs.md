# 38-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `bf819624-8349-4d8f-9845-660944cda698` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `3e5a369a-bdad-4bdd-835d-abee5bc6bccb` |
| 2 | `text` | linked | yes | string |  | `33-slack-msg-partial-verified.output.slack_message` | Please send the slack message in the following format:<br><br>PARTIAL PAYMENT — {requester_name} ({requester_email})                                   <br>  Paid: ${total_amount_paid}                                                                   <br>  Still owed: ${total_amount_remaining}       <br>  Invoices cleared: {invoice_count_paid} \| Still open: {invoice_count_outstanding}             <br>  Outstanding: [list invoice IDs from invoices_outstanding, comma separated]      <br>  Ticket: {ticket_id}                                                                          <br>  Action: Monitor for remaining payment.<br><br><br>Use emojis where applicable | param `f65dbc2f-e02c-4556-a513-7bab116882e2`<br>output `75f13083-8524-4a65-942f-6da45fd9354c` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | Please leave these empty | param `cf891321-7f05-4095-903d-2c089e453b0a` |
| 4 | `post_at` | ai_fill |  | string |  |  | Please leave these empty | param `bda465a6-6c5e-45a8-9a29-e1f10d9f2e43` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | Please leave these empty | param `4b46dd4f-c0c9-487f-9275-5e4de11b34cd` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `e5cec95e-9a47-4344-9486-e3a22872a903` |
| 7 | `username` | ai_fill |  | string |  |  | Please leave these empty | param `96033891-df6a-4306-9875-18034e56ea7a` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | Please leave these empty | param `a5bc8806-f255-41eb-a7ae-95ecd8547804` |
| 9 | `icon_url` | ai_fill |  | string |  |  | Please leave these empty | param `652d58dc-a3db-491b-9394-c4f2ecbc334a` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `b6e62b38-9add-4636-891a-72362114c170` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | Please leave these empty | param `248ec214-c5ca-4fae-9e35-30492aaca0ea` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | Please leave these empty | param `b12278b3-d22b-4d72-8b9b-347b2c34a3e5` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `bb382276-3202-4ffa-a2f8-7a8ea31b5bf7` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | Please leave these empty | param `729c802a-df27-4954-b618-80a1f0f72f2f` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | Please leave these empty | param `5d948db1-bca4-4b99-adbc-8d97d543d5ae` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `100097a7-2724-4624-89dd-8f2b7c5936e1` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | Please leave these empty | param `85f2ea25-98c7-4de8-b005-7366cbe10b71` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | Please leave these empty | param `625defd7-280d-433d-bcfb-c63750ece5d3` |
