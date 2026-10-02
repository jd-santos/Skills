---
name: work-routing
description: Routes uncertain or multi-step software work to the shortest useful process. Use when the user asks how to approach work, several consequential decisions are unsettled, or a task may need discovery, domain modeling, a spec, or implementation slices.
version: 1.1.0
author: jdwork
category: workflow
---

# Work Routing

Choose the smallest workflow that fits the user's request. This skill is a routing aid, not a required preamble to every task and not a substitute for the skills it recommends.

## Instructions

### 1. Respect the request

- Follow explicit user direction. If the requested outcome and constraints are clear, do the work directly instead of inserting a planning ritual.
- Keep purely exploratory or unrelated discussion read-only unless the user asks to save it. For a substantial project-specific deliverable, even an answer-only one, check whether it belongs in the established backlog without waiting for the word TODO. An explicit read-only request still forbids task writes.
- Ask about the route only when repository conventions and the request still leave a meaningful choice unresolved. Do not ask the user to discover facts that can be checked safely in the repository or tools.
- For multi-step work, TODO requests, or a substantial project-fit deliverable that may need backlog capture, load `todo-manager`. Follow the project's established task source: use a `todo/` workbench only if the project has one or authorizes adopting it. Preserve other trackers until migration is authorized.

### 2. Choose the shortest useful route

| Situation | Route |
| --- | --- |
| Clear, bounded change | Work directly. Skip grilling, a plan file, and optional synthesis skills. |
| Pure exploration or an unrelated question | Answer in chat. Do not create or update files unless asked. |
| Several consequential decisions remain open | Use the available `grilling` skill. Ask only the decision frontier that can be answered now, recommend an option, and wait for the user's decisions before asking dependent questions. |
| Domain terms, relationships, or boundaries are unclear or contested | Pair grilling with an available, locally adapted domain-modeling skill. Compare terminology with code and maintained project docs, then test it with concrete scenarios. If that adapted skill is unavailable, say so and ask before doing equivalent modeling by hand. |
| A substantial behavior contract needs to travel across sessions | Use the available local `to-spec` skill only when it adds value; small contracts stay in the established work record. If that skill is unavailable in the current agent, name the gap and ask before producing a formal spec by hand. |
| Work needs independent implementation slices | Start with one vertical-slice checklist in the project's established task source and note real blockers. Split records when backlog readability or independent ownership and delivery require them. |
| A very large effort still has no clear destination | Mention Wayfinder only as a possible future route if the user wants it. It is not part of the default workflow and must not introduce another tracker. |

Do not recommend every route in sequence. Stop when the current route resolves the need. `grilling`, domain modeling, spec synthesis, and Wayfinder are distinct capabilities, not synonyms for planning.

### 3. Use grilling without adding an approval ritual

When using `grilling`, follow that skill's question and confirmation instructions. The agent owns fact-finding; the user owns unresolved decisions. After the user confirms the shared understanding, continue with the next action they already requested without asking for a second conversational build approval. Normal tool permissions, read-only requests, safety rules, and delivery safeguards still apply.

A suggested route does not authorize file writes, task migration, deletion, installation, commits, or delivery. Do not infer an unanswered decision or permission from silence.

### 4. Keep one source of truth

- If the project uses or adopts a `todo/` workbench, put substantial work in its existing work record. That README owns status, concise acceptance criteria, and the only detailed execution checklist. Add a linked `plan.md` for substantial design, or `spec.md` for a durable behavior contract, only when the detail needs room. Keep optional documents linked and avoid duplicate checklists.
- During authorized development, capture settled working decisions as they emerge. Do not commit each answer or rewrite the whole discussion as a transcript.
- Keep tentative terms and scenarios in the project's established task source. Promote vocabulary to existing maintained domain docs only when it is adopted or verified beyond the effort. Create a glossary only when several reusable terms need one home.
- Record a major, agreed domain or architectural tradeoff in the project's existing ADR convention only when it is consequential, hard to reverse, and surprising without context. State clearly when a decision is proposed rather than implemented.
- Do not create a new tracker, glossary, ADR, spec, or ticket tree merely because a recommended skill expects one. Follow the project's established paths.

### 5. Respect capabilities and safeguards

- Check whether a recommended skill is available in the current agent. Name it and the missing capability if it is not. Ask before substituting a manual process.
- Do not assume that skill composition or invocation works the same way in every host. Use only mechanisms verified for the current agent.
- Keep the current parent responsible for any delegation and integration. A skill recommendation does not authorize a child agent to spawn more agents.
- Preserve secret-file protections, read-only modes, ordinary permission prompts, deletion approval, review requirements, and the project's shipping workflow.
- Discovery and documentation skills never create automatic commits or push changes.

## Examples

- A user asks for a small, fully specified typo fix: make the edit directly.
- A user asks for a substantial project-specific comparison without mentioning TODO: answer the question and check whether its agreed follow-up belongs in the established backlog. An explicitly read-only discussion remains read-only.
- A user asks to compare two approaches with unresolved product tradeoffs: use `grilling`, then act only after the shared understanding is confirmed.
- A user asks to rename a domain concept whose meaning differs across code paths: recommend grilling with the adapted domain-modeling skill, if available, and keep working notes in the project's task source.
- A user describes a large build with settled behavior but many independent slices: keep one authoritative task record and split its checklist only as much as ownership requires.
