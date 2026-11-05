# 35-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `03f4d798-acc0-4842-ad25-d5aeac8bd307` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `08ca55f8-0c1d-4997-bc94-c3f3bdfe6839` |
| 2 | `text` | linked | yes | string |  | `30-slack-msg-partial.output.slack_message` | use the exact slack message template<br><br>⚠️  PAYMENT DISCREPANCY — {requester_name} ({requester_email})                               <br>  Customer claimed full payment but Stripe shows partial.<br>  Paid: ${total_amount_paid}                                                                   <br>  Still owed: ${total_amount_remaining}   <br>  Outstanding invoices: [list IDs where amount_remaining > 0]<br>  Ticket: {ticket_id}                                                                          <br>  Action: Review and contact customer before closing.<br><br>use emojis where ever applicable | param `918f74ed-1c1a-49a2-9271-bd5c45403f51`<br>output `a245ee6c-0d06-49a4-9350-f5b564ac851f` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `77eb483f-12cb-4383-9f1e-d3d903817100` |
| 4 | `post_at` | ai_fill |  | string |  |  | This is not required please leave it empty | param `8b3f02b0-ca78-4261-9556-38ec352b7bdc` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `0cdf5c9b-e8d6-4416-94c4-fc43c0fa734e` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `af4ba04a-54b9-47f1-a8fa-5286c639c4a0` |
| 7 | `username` | ai_fill |  | string |  |  | This is not required please leave it empty | param `ac58d72d-447d-450a-8bc1-2ad442f2c57c` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | This is not required please leave it empty | param `13170526-b4b5-475a-b66f-f53084548ee6` |
| 9 | `icon_url` | ai_fill |  | string |  |  | This is not required please leave it empty | param `54502fe9-46fb-459a-9772-120af58e714c` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `61777c47-0ad9-4604-a260-1e6a7c36867c` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | This is not required please leave it empty | param `1c33c454-6dcd-483a-858a-8d12a919da79` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `0adbb84d-d076-479e-9eea-7de125df9793` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `b7c24048-9cd7-4c19-a9ff-5130a8f5a0d6` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | This is not required please leave it empty | param `a7d67989-814f-404c-a6ab-a4de93f31f82` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | This is not required please leave it empty | param `3c8108cf-71a0-419b-9cc9-5d02c1fb498b` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `e090a761-5581-4d1c-861d-2051fb74b36b` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `b1f65123-41aa-4577-9801-3813af516497` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `0d7a23f3-13fd-4a02-8265-fd90f5e29349` |
