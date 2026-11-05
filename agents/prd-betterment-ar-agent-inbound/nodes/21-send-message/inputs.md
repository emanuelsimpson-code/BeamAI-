# 21-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `text` | linked | yes | string |  | `15-slack-msg-wrong-contact.output.slack_message` | Format exactly as:<br>  "📋 WRONG CONTACT — {requester_name} ({requester_email})<br>  Reply: [first 150 characters of ticket_latest_comment]<br>  Ticket: {ticket_id}<br>  Action: Update billing contact in Salesforce and resend outreach." | param `74b93a39-ef9d-4102-98d6-e91e9a2692e3`<br>output `23e9dda0-caec-49c1-923e-a7890c676c42` |
| 1 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `1d0cf548-dd28-4493-9ebc-8ecfee8476f9` |
| 2 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `c842cb1f-33c1-4428-adbf-f325207414a1` |
| 3 | `unfurl_media` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `f2f301bf-4b90-4bc0-9629-4931711c0a6d` |
| 4 | `unfurl_links` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `22274c82-ffd2-4d10-a868-4bb3aa1f1c74` |
| 5 | `metadata_event_payload` | ai_fill |  | string |  |  | This is not required please leave it empty | param `67fa1bc6-f4c7-437e-af84-c25272f6855b` |
| 6 | `metadata_event_type` | ai_fill |  | string |  |  | This is not required please leave it empty | param `cd6895b1-0a37-4bf1-ac2d-b1dbea744374` |
| 7 | `thread_broadcast` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `8ec538c7-fb9b-4d58-b214-ac6118e4cf25` |
| 8 | `thread_ts` | ai_fill |  | string |  |  | This is not required please leave it empty | param `45e57d87-03e1-447e-9a7f-cd770687e2a2` |
| 9 | `icon_url` | ai_fill |  | string |  |  | This is not required please leave it empty | param `c058d36e-9ee6-4be4-bb3e-275d700ea28c` |
| 10 | `icon_emoji` | ai_fill |  | string |  |  | This is not required please leave it empty | param `1b5ebdde-7223-4e8c-ad70-a9f8d3ac8409` |
| 11 | `username` | ai_fill |  | string |  |  | This is not required please leave it empty | param `670f878a-8b2d-4699-83b9-26eb70b4a02f` |
| 12 | `include_sent_via_pipedream_flag` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `b17fc79d-ab67-4e42-abfe-c6f794b2ff8f` |
| 13 | `post_at` | ai_fill |  | string |  |  | This is not required please leave it empty | param `0f20d9e7-b90b-4ed5-93a4-45fa9adfc9f3` |
| 14 | `mrkdwn` | ai_fill |  | boolean |  |  | This is not required please leave it empty | param `180a292a-b3ad-475b-a734-4cbb348b4d19` |
