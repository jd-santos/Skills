---
name: shareable-doc-writer
description: Creates and revises technical documents meant for sharing with teammates, mixed technical audiences, Jira epics, implementation handoffs, plans, and proposals. Use when a user says a doc is too dense, stilted, hard to share, needs better information architecture, needs examples near requirements, or needs to explain concepts without over-teaching.
version: 1.1.0
author: jdwork
category: documentation
requires: [core-writing, technical-writing]
---

# Skill: Shareable Doc Writer

## Description

Creates and revises technical documents for real readers, not just complete notes. Use this when a document needs to be shared with teammates, attached to Jira work, handed to implementers, or made easier for a mixed technical audience to understand.

This skill builds on `core-writing` and `technical-writing`, and adds document architecture: what belongs in the main body, what belongs near a task, what belongs in an appendix, and how to make dense technical ideas easier to parse without watering them down.

## Instructions

### 1. Pre-flight checks

Before writing or rewriting:

1. **Load the writing baseline**: Apply `core-writing` for voice and `technical-writing` for technical accuracy.
2. **Confirm it's a document**: If the reader needs a message, comment, or short ticket rather than a doc they'll keep, use `dev-brief` instead.
3. **Identify the sharing context**: Ask who will read the doc, what they need to do after reading it, and where it will live.
4. **Protect sensitive information**: If the doc is in a public repo or may be shared outside the team, avoid internal URLs, credentials, personal identifiers, client data, and private operational details.
5. **Preserve facts**: Do not delete factual details just because they are dense. Move them to an appendix or a more specific section when they are not needed in the main flow.
6. **Respect user edits**: If the user says they made changes, read the current file and avoid reverting their wording unless it conflicts with the goal.

Useful clarification questions:

- Who is the reader: implementer, reviewer, leadership, product, or mixed technical team?
- What should the reader do after reading: approve, build, create Jira tasks, review risks, or understand a plan?
- Is this a plan, a proposal, an API handoff, a Jira breakdown, or reference material?
- Which details are required for implementation, and which are just investigation history?
- Are there concepts that need explanation because they imply new logic?

### 2. Main workflow

1. **Separate the document's jobs**
   - Identify whether the doc is trying to explain a plan, ask for implementation, record investigation notes, define API contracts, or preserve open questions.
   - If one section is doing several jobs, split it by reader need.

2. **Choose an information architecture**
   - For a plan: lead with goal, ownership split, flow, first build, key concepts, handoff, success criteria, open questions.
   - For Jira: make top-level sections map to feature tasks. Put examples and context inside the relevant task, not in one large shared appendix.
   - For an API or backend handoff: organize by capability. Each capability should include why it matters, needed behavior, request example, response expectations, and open questions.
   - For investigation-heavy docs: move observations, rejected approaches, constraints, and detailed schemas into appendices.

3. **Write for comprehension, not minimal word count**
   - Use short paragraphs to connect ideas before listing details.
   - Avoid staccato bullet piles where the reader has to infer the relationship between items.
   - Keep concise wording, but add connective tissue when it reduces mental effort.
   - Explain why a concept matters when it implies implementation work.

4. **Place examples where they are used**
   - Put request/response examples next to the specific capability they illustrate.
   - Put diagrams near the flow or decision they explain.
   - Put edge cases near the task they affect.
   - Avoid dumping all examples into a distant section unless the doc is a pure reference.

5. **Use appendices deliberately**
   - Move supporting detail out of the main body when it interrupts the reader's path.
   - Good appendix material includes storage observations, validation constraints, rejected approaches, detailed file trees, state object schemas, and long field lists.
   - Link or mention the appendix from the main section only when the reader needs to know it exists.

6. **Tune density with structure**
   - If the doc feels dense, do not only cut words. Re-group ideas, add headings, convert some bullets to prose, and put implementation examples next to their tasks.
   - Use tables for ownership, tradeoffs, status, and feature/task breakdowns.
   - Use diagrams when they replace a long procedural explanation, but keep them printable and small.

7. **Review from the reader's path**
   - Can a reviewer understand the proposal without reading the appendix?
   - Can an implementer create tickets from the relevant sections?
   - Are concepts explained where they first matter?
   - Are examples close to the requirements they illustrate?
   - Did the rewrite preserve factual detail?
   - Did the rewrite remove investigation chatter that no longer helps?

### 3. Useful section patterns

#### Plan pattern

```markdown
## What we are building

[Goal in plain language. Include the first useful slice and what success looks like.]

## How the pieces fit together

[Ownership table or short prose explaining responsibilities.]

## Flow

[Small diagram or short step sequence.]

## First build

[What must exist for the first useful run.]

## Concepts that matter for implementation

[Explain only the concepts that affect implementation decisions.]

## Handoff

[What another team needs to provide or review.]

## Success criteria

[Observable outcomes.]

## Open questions

[Decisions still needed.]
```

#### Jira feature task pattern

```markdown
## Feature: [task name]

### Why this matters

[One short paragraph explaining why this task exists.]

### Needed behavior

- [Implementation-facing requirement]
- [Implementation-facing requirement]

### Example

[Short request, response, config, or user flow example.]

### Open questions

- [Only questions that affect this feature]
```

#### Concept explanation pattern

```markdown
### [Concept]

[What it is in one or two sentences.]

[Why it matters for this project.]

For implementation, this means:

- [Concrete behavior]
- [Concrete behavior]
- [What not to assume]
```

### 4. Error handling

If the document still feels dense:

1. Do not automatically make it shorter.
2. Identify whether the problem is ordering, missing transitions, too many bullets, unexplained concepts, or details in the wrong place.
3. Move supporting detail into appendices or feature-specific sections.
4. Add short connective paragraphs where the reader currently has to infer intent.
5. Ask the user which reader is getting stuck if the fix is not obvious.

If the user says a rewrite lost important detail:

1. Restore the factual detail.
2. Decide whether it belongs in the main flow, next to a feature task, or in an appendix.
3. Explain where it moved and why.

If the user says the doc is over-explaining:

1. Remove background that only explains the conversation that produced the doc.
2. Keep implementation implications.
3. Keep examples that help someone build or review the work.

## Examples

### Example: Making a plan easier to share

**User:** "This plan is too dense for a mixed technical team. It needs to explain concepts better without becoming longer."

**Workflow:**
1. Identify the reader and purpose.
2. Move file trees, state schemas, and detailed constraints to appendices.
3. Keep the main body focused on goal, ownership, flow, first build, important concepts, handoff, and success criteria.
4. Rewrite terse bullets into short paragraphs where the connection between ideas matters.
5. Preserve technical details in appendices.

### Example: Reworking requirements for Jira

**User:** "These backend requirements need to become Jira feature tasks. Put examples next to the relevant bits."

**Workflow:**
1. Convert each top-level capability into `Feature: ...` sections.
2. For each feature, add `Why this matters`, `Needed behavior`, `Example`, and `Open questions` when needed.
3. Move shared examples into the feature that uses them.
4. Keep later/non-blocking items in a final backlog section.

## Notes

Good shareable docs are not always shorter. They are easier to follow because the structure matches the reader's job, concepts are explained where they matter, and details are parked where they do not interrupt the main path.

## Cross-Reference

- `core-writing`: shared voice (required)
- `technical-writing`: technical accuracy and terminology (required)
- `dev-brief`: message-sized briefs for developers. It cuts hard where this skill preserves and reorganizes
