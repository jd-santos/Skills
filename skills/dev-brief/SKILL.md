---
name: dev-brief
description: Edits notes, docs, threads, or drafts down into a short brief for a developer or other technical reader, either an actionable ask or a readable explanation of a technical decision or architecture. Use when sharing context with an engineer, writing a Slack message, PR comment, ticket description, or handoff note, or when user says "trim this for a dev", "make this dev-friendly", "cut this down", "explain this decision to the team", "what does the engineer need", "tl;dr for the team", or "dev brief".
metadata:
  version: "1.1.0"
  author: jdwork
  category: documentation
  requires: core-writing, technical-writing
---

# Skill: Dev Brief

## Description

Turns long or messy source material (meeting notes, investigation logs, AI output, chat threads, product docs) into a message-sized brief for a technical reader. Briefs come in two kinds:

- **Ask briefs:** the developer needs to do something. Lead with the ask, give the specifics, cut the story.
- **Explanation briefs:** the developer needs to understand a technical decision or architecture. Lead with the conclusion, keep the reasoning that makes it trustworthy, cut the rest. A few short paragraphs is fine here.

This skill cuts. `shareable-doc-writer` keeps every fact and reorganizes a full document. Use this one when the output is a message, comment, or short ticket. Use that one when the output is a document people will keep and come back to.

## Instructions

### 1. Pre-flight checks

1. **Load the writing baseline**: Apply `core-writing` for voice and `technical-writing` for technical accuracy.
2. **Find the purpose**: Decide whether this is an ask (build, fix, review, decide, answer) or an explanation (why we chose X, how Y fits together). If the source doesn't make it clear, ask. The purpose drives every cut.
3. **Know the channel**: Slack/DM, PR or review comment, Jira ticket, email, or handoff note. This sets length and formatting (see the table below).
4. **Know the reader's context**: Do they already know the system? Have they seen the earlier thread? Cut context they already have.
5. **Protect sensitive data**: Strip credentials, customer data, and personal details the task doesn't need.

### 2. Workflow

1. **Pull out the load-bearing facts**:
   - The ask, or the decision and its conclusion
   - Concrete specifics: file paths, endpoints, error text, IDs, versions, commands, ticket keys
   - Constraints: deadlines, things they must not break, compatibility requirements
   - Evidence: repro steps, logs, what was already tried and the result
   - For explanations: the two or three reasons that decided it and the tradeoff accepted
   - Open questions that block the work

2. **Cut everything else**, especially:
   - Investigation narrative ("first we looked at X, then we thought Y")
   - Explanations of concepts the reader already knows
   - Rejected ideas, unless the dev is likely to propose the same thing
   - Hedging, pleasantries, restated context, summaries of the summary
   - Background that only explains why the conversation happened

3. **Lead with the point.** For an ask, the first line says what you need and by when. For an explanation, the first line states the decision or the shape of the architecture. Context follows.

4. **Be concrete instead of descriptive.**
   - "the login thing is broken" → "`POST /auth/token` returns 500 since deploy `a1b2c3`"
   - "the config" → `config/prod.yaml` and the key name
   - Paste exact errors and commands in code blocks. Don't paraphrase them.

5. **Separate fact from guess.** Label hypotheses ("I think it's the cache, not confirmed"). A developer will act on anything stated as fact.

6. **Say what's settled and what's open.** Settled decisions are stated as settled so nobody reopens them. Anything that needs the reader's call is named plainly.

7. **For explanation briefs, keep the reasoning readable.** Use short paragraphs, not a bullet pile, when the ideas depend on each other. Say what the decision means for the reader's code or work. Stop there and link the full design doc.

8. **Fit the channel.**

   | Channel | Shape |
   |---|---|
   | Slack / DM ask | Ask in line one, 2 to 6 lines, code block for errors, link out for the rest |
   | Slack / DM explanation | Decision in line one, 2 or 3 short paragraphs, link to the full doc |
   | PR / review comment | One issue per comment, point to the line, suggest the fix |
   | Jira ticket | Goal, acceptance criteria, repro or example, links. No narrative |
   | Handoff note | Current state, what's next, gotchas, where things live |
   | Email | Point in the subject or first sentence, short sections |

9. **Link instead of including.** If the dev might want the full background, link it with one line on what's there.

10. **Final pass from the reader's seat:**
    - Could they act, or explain the decision to someone else, without replying to ask what you meant?
    - Would they miss each sentence if it were gone?
    - Are names, paths, and errors exact?
    - Is anything stated as fact that's really a guess?

### 3. Error handling

- **No clear purpose in the source**: Don't invent an ask. Ask the user what they want from the developer. If it's FYI, say so up front ("FYI, no action needed").
- **User says it's too terse**: Add back the one or two facts the reader needs to trust or act on the brief, usually why it matters or what was already tried. Don't bring back the narrative.
- **Source is too vague to make concrete**: List the missing specifics (error text, path, environment) and ask for them instead of writing around the gap.
- **Content really needs to be a doc** (several features, a long-lived reference, mixed audiences): Say so and suggest `shareable-doc-writer`. A brief can then link to that doc.

## Examples

### Example: Investigation notes to a Slack ask

**User:** "Trim this down to send to the backend dev" + a page of debugging notes about failed PDF exports.

**Result:**

> Can you look at PDF export failing for reports with more than 50 charts? Not urgent, but it's blocking the Q3 customer report.
>
> Repro: `POST /reports/{id}/export?format=pdf` on report `r_8812` times out after 30s.
> ```
> RenderTimeoutError: page.pdf exceeded 30000ms
> ```
> With the timeout raised to 120s locally it finishes in about 70s, so I think it's render time, not a crash. Not confirmed on staging.
>
> Full notes: [link]

### Example: Architecture decision to a Slack explanation

**User:** "Write a blurb for the team on why we're moving report rendering to a queue."

**Result:**

> We're moving PDF rendering out of the API request and onto a worker queue. Export endpoints will return a job ID instead of the file.
>
> Large reports take 60s or more to render, which is past the gateway timeout, and retries were piling duplicate renders onto the same pods. A queue lets us cap concurrency and retry safely. The cost is that clients now poll `GET /jobs/{id}` (or get a webhook) instead of waiting on one request.
>
> If you call the export endpoints, plan for the async response. Old behavior stays behind `?sync=true` until the end of the quarter. Design doc: [link]

## Cross-Reference

- `core-writing`: shared voice (required)
- `technical-writing`: technical accuracy and terminology (required)
- `shareable-doc-writer`: full documents where detail is kept and reorganized, not cut
- `commit-message-writer`, `changelog-writer`: those specific formats
