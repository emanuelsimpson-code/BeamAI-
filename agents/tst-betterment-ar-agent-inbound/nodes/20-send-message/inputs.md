# 20-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `087beb1e-d5f8-4ffd-a325-631c669be0d4` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `e46567b3-85dc-42dc-8793-ba9924563a84` |
| 2 | `text` | linked | yes | string |  | `15-slack-msg-wrong-contact.output.slack_message` | Format exactly as:<br>  "📋 WRONG CONTACT — {requester_name} ({requester_email})<br>  Reply: [first 150 characters of ticket_latest_comment]<br>  Ticket: {ticket_id}<br>  Action: Update billing contact in Salesforce and resend outreach." | param `04968d6e-263d-41ef-832c-77a07bce1cb6`<br>output `b5bb796c-d248-48e2-886d-14653e8ddb60` |
| 3 | `mrkdwn` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `44a9d197-4239-44c8-94c9-c892cd22c87e` |
| 4 | `post_at` | ai_fill |  | string |  |  | This is not required please leave it empty | param `da936ce4-5afa-4ba0-88ad-a54d32a124c0` |
| 5 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `b1171c60-dc7e-4323-9cf1-def5155ac605` |
| 6 | `customizeBotSettings` | static |  | boolean |  |  | The customize bot settings, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `66f2725b-9e17-4283-b06c-1f8dbb29e6b6` |
| 7 | `username` | ai_fill |  | string |  |  | This is not required please leave it empty | param `858ee9ff-fd77-434e-a2ae-8246fd18c19c` |
| 8 | `icon_emoji` | ai_fill |  | string |  |  | This is not required please leave it empty | param `261b97ec-ae27-43d3-9efa-f4bf1e8ba053` |
| 9 | `icon_url` | ai_fill |  | string |  |  | This is not required please leave it empty | param `1e061637-e338-4fa2-874f-0769ecb7d67c` |
| 10 | `replyToThread` | static |  | boolean |  |  | The reply to thread, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `30aff9ed-7989-4ac2-b4ae-951a5f4df465` |
| 11 | `thread_ts` | ai_fill |  | string |  |  | This is not required please leave it empty | param `5c3096d8-3b43-4971-8027-2fe0c476a13d` |
| 12 | `thread_broadcast` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `e1c4993d-ecb4-47e8-9be5-d8c4e5653fe6` |
| 13 | `addMessageMetadata` | static |  | boolean |  |  | The add message metadata, found in Slack Bot refresh responses or previous node outputs and set to true or false (e.g., `false`). | param `78b5fb95-f2b6-4d8c-8b16-9ac8702b650e` |
| 14 | `metadata_event_type` | ai_fill |  | string |  |  | This is not required please leave it empty | param `70c616da-ffb1-4fab-9f58-4a1d7efbf807` |
| 15 | `metadata_event_payload` | ai_fill |  | string |  |  | This is not required please leave it empty | param `3e1c59af-dd99-4d53-a1fd-9377b5a4924a` |
| 16 | `configureUnfurlSettings` | static |  | boolean |  |  | The configure unfurl settings, found in Slack Bot refresh responses or previous node outputs and formatted as a URL (e.g., `false`). | param `993413d9-ca0f-42d7-9efd-ff94d100eb7b` |
| 17 | `unfurl_links` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `1691505d-d844-4c48-96a0-3f8ac43e680d` |
| 18 | `unfurl_media` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `0ea54924-3db5-43c8-a040-9c0847afc29d` |
