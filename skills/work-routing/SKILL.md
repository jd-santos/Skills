---
name: work-routing
description: Routes uncertain or multi-step software work to the shortest useful process. Use when the user asks how to approach work, several consequential decisions are unsettled, or a task may need discovery, domain modeling, a spec, or implementation slices.
version: 1.3.0
author: jdwork
category: workflow
---

# Work Routing

Choose the smallest workflow that fits the user's request. Select useful
capabilities automatically; the user need not name a skill. They may also invoke
any capability directly. This skill is a routing aid, not a required preamble or
a mandatory pipeline, and it does not duplicate the skills it recommends.

`todo-manager` owns record creation and lifecycle. `work-contract` owns behavior
synthesis and decomposition. The executing agent follows the agreed contract;
`ship` remains responsible for delivery only when requested. Use host discovery
or the available sources for [`todo-manager`](../todo-manager/SKILL.md) and
[`work-contract`](../work-contract/SKILL.md). If a needed capability cannot be
loaded by either method, report the gap rather than substituting silently. File access alone does
not prove catalog discovery or parity across hosts.

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
| A substantial behavior contract needs to travel across sessions | Use the available `work-contract` skill only when it adds value; small contracts stay in the established work record. If it is unavailable, name the gap and ask before substituting. |
| Work needs independent implementation slices | Use the decomposition method in `work-contract`: start with one outcome-oriented checklist and real prerequisites. Consequential scope, delivery, or dependency changes require the user's decision; `todo-manager` creates approved records only when useful. |
| The user asks to create a project, issue, feature, or work record | Use `todo-manager` to find or create the authoritative record in the established task source. Use `work-contract` for missing behavior decisions, not another tracker or note schema. |
| A very large effort still has no clear destination | Mention Wayfinder only as a possible future route if the user wants it. It is not part of the default workflow and must not introduce another tracker. |

Do not recommend every route in sequence. Stop when the current route resolves the need. `grilling`, domain modeling, contract synthesis, and Wayfinder are distinct capabilities, not synonyms for planning.

### 3. Use grilling without adding an approval ritual

Find `grilling` through the host's skill discovery. If it is not listed, check the installed [`../grilling/SKILL.md`](../grilling/SKILL.md) in this collection or the project's configured shared skills directory and read the actual source before using it. If neither source is available, report the gap and ask before installation or substitution. Do not copy its interview into this router. File retrieval verifies only that host/session's access, not automatic discovery or cross-agent parity; a host may need a reload after installation.

When using `grilling`, follow that skill's question and confirmation instructions. The agent owns fact-finding; the user owns unresolved decisions. After the user confirms the shared understanding, continue with the next action they already requested without asking for a second conversational build approval. Normal tool permissions, read-only requests, safety rules, and delivery safeguards still apply.

A suggested route does not authorize file writes, task migration, deletion, installation, commits, or delivery. Do not infer an unanswered decision or permission from silence.

### 4. Keep one source of truth

- If the project uses or adopts a `todo/` workbench, put substantial work in its existing work record. That README owns status, the full behavior contract and acceptance criteria, decisions, and the only detailed execution checklist. Substantial or multi-session work still defaults to that README, using stable headings for selective reading. Add linked subject-named detail such as `research.md`, `design.md`, or `validation.md` only when it has an independently useful reading or evidence purpose, or the user explicitly requests it. Length alone does not require `plan.md` or `spec.md`. Move detail rather than mirror it; avoid empty scaffolding and progress journals.
- Use `todo-manager` for work-record YAML and lifecycle rules: required `status`, optional `pr`, `blocked_by`, `parent`, `child`, and `tags`. Hierarchy does not imply dependencies or duplicated child progress. Respect existing records until migration is authorized. At task entry reconcile only the selected record when stale, not the whole archive; implementation and handoff update it at meaningful checkpoints, and `ship` owns reviewed pre-merge closeout.
- Have `todo-manager` reuse or create a durable record once authorized work needs
  a home and purpose/current scope are known. It need not wait for a settled
  contract. Exploration alone does not authorize creation. During execution,
  use the agreed contract, validate observable outcomes, and update the existing
  checklist at meaningful checkpoints. Return material conflicts and changed
  commitments to the user; do not silently rewrite the contract to fit the build.
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
