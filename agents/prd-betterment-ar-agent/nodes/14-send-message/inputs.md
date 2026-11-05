# 14-send-message: inputs

| # | Param | Fill type | Required | Type | Static value | Linked source | Description / question | IDs |
|---|---|---|---|---|---|---|---|---|
| 0 | `metadata_event_payload` | static |  | string | null |  | This is not required please leave it empty | param `f4d3ce7c-e86c-4660-93c6-8bf16cd4308a` |
| 1 | `metadata_event_type` | static |  | string | null |  | This is not required please leave it empty | param `eefd0731-a485-4936-9f5c-2502848dccd4` |
| 2 | `thread_broadcast` | static |  | boolean | false |  | This is not required please leave it empty | param `8e23c204-fd08-4f97-bc4c-39c7bbb5803d` |
| 3 | `thread_ts` | static |  | string | null |  | This is not required please leave it empty | param `ae28f76e-4657-49be-af8e-f1c4eef5c3a9` |
| 4 | `icon_url` | static |  | string | null |  | leave it empty | param `66d4abfc-6dae-4319-b3af-5d11ec11ba01` |
| 5 | `icon_emoji` | static |  | string | null |  | This is not required please leave it empty | param `2eee9f34-530a-42b0-af08-d2c1494f4646` |
| 6 | `username` | static |  | string | null |  | This is not required please leave it empty | param `49730391-a2e5-4fdd-bb91-54812d9dd942` |
| 7 | `post_at` | static |  | string | null |  | This is not required please leave it empty | param `bea5ff08-7a2f-46e6-a2ec-97c36aed0669` |
| 8 | `mrkdwn` | static |  | boolean | true |  | This is not required please leave it empty | param `5e0a4f7a-ff90-4d7f-91cf-04c7964f9968` |
| 9 | `channelType` | static | yes | string | Channels |  | The channel type, found in Slack Bot configuration or workflow context (e.g., `slack-bot-channeltype`). | param `ba8c4c5c-700f-41c3-9ff8-b31b0318bcf5` |
| 10 | `text` | linked | yes | string |  | `13-create-slack-ticket-message.output.slack_message` | Send a message notifying about the newly created Zendesk ticket. Format it exactly like this, with each field on its own line:<br><br>New Zendesk Ticket:<br>Ticket ID: [ticket id]<br>Subject: [subject]<br>Requester: [requester name/email]<br>Priority: [priority level]<br>Status: [status]<br>Description: [brief description from the email]<br>Extract all details from the email that generated the ticket.<br><br>Use emoji if applicable | param `bcffbccc-02db-4957-b4ca-f2cac1ac48b0`<br>output `c3214e86-c6b5-4eff-afb1-44fcfea9f898` |
| 11 | `conversation` | static | yes | string | C0ATZVCSZ29 |  | The conversation, found in Slack Bot configuration or workflow context (e.g., `slack-bot-conversation`). | param `90b90488-4539-4dab-ae6c-d70945dd1cb4` |
| 12 | `unfurl_media` | static |  | boolean | false |  | This is not required please leave it empty | param `8a31d261-1bdc-484f-9606-4ff60f116452` |
| 13 | `unfurl_links` | static |  | boolean | false |  | This is not required please leave it empty | param `99e49f66-8e2d-4b38-a461-3144ffaaf548` |
