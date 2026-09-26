# Mochi API insertion

Read this only when the user explicitly asks to create cards or decks in Mochi. Confirm current behavior in the [official API reference](https://mochi.cards/docs/api/) before writing because API details can change.

## Boundaries

- Direct insertion is optional. Generate and validate the same Markdown content used for a file bundle before sending it.
- Use an already configured API key. Never print it, include it in card files, commit it, or save it in a new plaintext file.
- An explicit request to insert cards authorizes creation in the resolved destination deck. It does not authorize updating, moving, or deleting existing cards or decks.
- Do not create a missing deck unless the user requested deck creation or confirms that choice.

## Current API shape

The base URL is `https://app.mochi.cards/api/`. Authentication uses HTTP Basic Auth with the API key as the username and an empty password.

Relevant operations:

- `GET /decks/` lists decks. Follow `bookmark` pagination when needed.
- `POST /cards/` creates one card. JSON requires `content` and `deck-id`.
- `manual-tags` optionally accepts tag strings without the leading `#`.
- Card creation is one at a time. The documented concurrency limit is one active request per account, so create cards sequentially.

Keep inline tags in `content` by default so exported Markdown remains self-describing. Use `manual-tags` only when the user wants tags stored as metadata without displaying them in the card content.

## Insertion workflow

1. Validate all card Markdown using the main skill.
2. List every deck page and resolve the requested deck by exact ID or an unambiguous name and parent path. Ask when multiple decks match.
3. Record the destination deck ID, intended card count, and filenames locally in working memory before the first write.
4. POST cards sequentially. Preserve the returned card ID for each successful creation.
5. If a request fails, stop the batch. Report the successful card IDs and the first failure. Retry only the failed and unattempted cards, never the entire batch blindly.
6. Verify successful responses contain the expected deck ID and content. Report created, skipped, and failed counts.

For attachments, create the card first, then follow the current attachment endpoint documentation and verify that its Markdown media reference resolves. Do not assume a local file reference was uploaded with the card JSON.

Do not add API credentials, generated IDs, or review history to the portable Markdown unless the user specifically requests an API-oriented manifest outside the import directory.
