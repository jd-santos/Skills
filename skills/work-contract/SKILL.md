---
name: work-contract
description: Defines behavior contracts and implementation slices from decisions and project evidence. Use when a substantial agreement needs to survive across sessions, when planning a feature, or when the user asks to write a spec, define acceptance criteria, or break work into tasks.
version: 1.1.0
category: workflow
---

# Skill: Work Contract

## Description

Turn discussion and evidence into an implementable agreement without restarting
settled decisions. Synthesis and decomposition are methods, not required stages
or separate document types. Use them only when they add value; a clear, bounded
change can proceed directly. This skill can be selected by `work-routing` or
invoked directly.

## Instructions

### 1. Locate the authority

1. Follow the user's requested output and write permissions. A read-only request
   stays read-only. Do not infer authorization to implement behavior, publish
   issues, commit, or push from a request for a contract.
2. Find applicable agent instructions, the project's existing tracker, relevant
   work record, and maintained docs. Read the current conversation and affected
   code and tests. Check existing terms and decisions; name missing evidence
   rather than inventing an agreement. Never read secret-looking files.
3. When a task workbench exists, load `todo-manager` for record discovery,
   creation, metadata, and lifecycle. Reuse the matching record. If no work
   record exists and authorized work warrants a durable home, let `todo-manager`
   create it using the project's convention and next unused number. It can
   capture purpose, current scope, and open questions before the contract is
   ready to implement. Do not duplicate its creation rules here.
4. If `todo-manager` is unavailable, name that gap and ask before replacing its
   task workflow by hand. Otherwise preserve the project's established task
   source and artifact convention. Do not create a second tracker or migrate
   existing notes without authorization.

### 2. Synthesize the behavior contract

- Separate user decisions, proposed behavior, present behavior, and open
  questions. Compare the discussion with current code, tests, and maintained
  docs. Surface material conflicts to the user before calling the contract
  settled; record non-blocking uncertainty openly.
- Without an explicit grilling invocation, ask only for consequential decisions
  that remain unresolved. Do not replay settled questions or require fixed
  interview rounds; routine implementation choices belong to the agent. When
  the user invokes `grilling` by name or clearly requests its full interview,
  follow its full decision-space exploration, including routine choices, and
  confirmation instructions. Do not invoke it automatically because several
  decisions are open. Clarify disputed domain terms against code and maintained
  docs; a domain-modeling specialist may help but is not required for ordinary
  clarification. Name a missing specialist when it is specifically requested.
- Define the intended outcome, scope and exclusions, externally observable
  behavior, important edge cases and failure/recovery behavior, acceptance
  criteria, and a credible validation approach. Keep stories optional; concrete
  scenarios often expose ambiguity more directly.
- Inspect existing test seams and similar tests. Prefer observable behavior at
  an existing, high-enough seam over new seams or implementation-detail tests.
  Discuss a seam only when it materially changes scope, cost, or confidence.
  Say when evidence for a testing approach is missing.
- A contract is ready to implement only when consequential behavior is settled
  and the acceptance criteria can be checked with the proposed validation.
  Routine implementation choices may remain open. A behavior-changing unknown
  blocks the affected scope, not necessarily unrelated work. A tidy document
  or a checked planning step is not evidence of readiness.

### 3. Write into the existing work record

- For bounded work, use the established task entry or concise acceptance
  criteria. Do not create `spec.md` solely because this skill was loaded.
- For substantial or multi-session behavior, default to the work README too.
  Put the full scope, behavior, scenarios or edge cases, decisions, testing
  approach, and unresolved questions under stable headings for selective
  reading. The work README owns status, concise acceptance criteria, the full
  contract, and the **only execution checklist**.
- Attach subject-named detail only for an independently useful reading or
  evidence purpose, or an explicit request. Existing or requested `spec.md`
  and `plan.md` are allowed, not size-triggered defaults. Move detail rather
  than mirror it. Link to the README's criteria instead of duplicating progress
  tracking. Preserve useful evidence; do not perform unauthorized migration.
- Let `todo-manager` own YAML metadata and lifecycle rules. Do not put work-item
  metadata on supporting documents or unrelated project READMEs. Mark proposed
  behavior as proposed, not shipped.

### 4. Decompose only when useful

1. Start with one readable checklist in the authoritative task source. Prefer
   independently verifiable outcomes that leave the project coherent, rather
   than separate tickets for database, backend, tests, and documentation layers.
2. For each proposed outcome, state its observable result, scope, validation,
   and actual prerequisites. Do not manufacture dependencies from list order
   or containment. Use expand-contract steps for a wide refactor when ordinary
   vertical slices cannot keep the project working.
3. Routine implementation steps can be organized within authorized scope.
   Changes to agreed scope, delivery order, independently deliverable outcomes,
   or consequential dependencies require the user's decision before becoming
   commitments. Present the proposed split and tradeoffs, not a silently changed
   contract. A decomposition proposal does not authorize new work.
4. Separate records only when backlog readability, independent ownership, or
   independent delivery justifies them. Have `todo-manager` create and link
   approved records; let it own relationship validation. A parent references
   child outcomes without duplicating their detailed checklists. A separate
   spec file is not a prerequisite for decomposition.

### 5. Hand off to execution

1. Check that material requirements trace to user decisions or maintained
   evidence; label assumptions and open questions. Check links, checklist
   ownership, and the validation approach before claiming readiness.
2. Summarize the contract and any blockers. If implementation is already
   authorized and the required understanding is confirmed, continue the
   requested work without a second build-approval ritual. Otherwise stop at
   the requested planning deliverable. Do not create an issue or begin
   implementing merely because the contract is written.
3. During authorized execution, follow the agreed contract and checklist.
   Update the existing record at meaningful checkpoints through `todo-manager`.
   Routine technical choices remain agent-owned; material conflicts, new scope,
   or changed delivery commitments return to the user. Do not rewrite the
   contract to match whatever was built.
4. Verify outcomes against acceptance criteria and report actual validation and
   limitations. Partial execution does not complete a parent or imply Git
   delivery. Normal review and shipping safeguards still apply. Do not create
   automatic commits or invoke `repo-commit` or `ship` merely because execution
   finished. `repo-commit` owns authorized local preparation/commits; `ship`
   owns explicitly requested remote delivery.

## Error handling

If a material conflict remains, leave a clearly labeled draft or answer in chat,
according to write permissions, and ask the smallest blocking question. Do not
publish an apparently agreed contract. If the repo lacks a clear task authority,
ask before choosing an artifact path. Preserve completed work when validation
fails, but do not check the failing outcome or claim the whole effort complete.

## Examples

- **Import failures:** Reuse the existing import work README. Resolve duplicate
  handling and partial-failure recovery before declaring that behavior ready;
  inspect existing import tests. Capture only useful scenarios, not a second spec.
- **Independent delivery:** Propose delivering import validation before an
  optional preview screen. Explain the changed delivery order and wait for the
  user's decision before committing to the split or creating child records.
- **Small correction:** A specified label fix needs direct execution and its
  existing task entry, not a contract document or decomposition exercise.
