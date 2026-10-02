---
name: to-spec
description: Synthesizes an agreed behavior contract from the conversation and project evidence. Use when the user asks for a spec or when substantial behavior needs a durable contract across sessions.
version: 1.0.0
author: jdwork
category: workflow
---

# To Spec

Turn settled discussion into a usable behavior contract without restarting the interview. Use the shortest artifact that preserves the agreement; a spec is optional even for a large task. This local workflow was inspired by [Matt Pocock's to-spec skill](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/to-spec/SKILL.md), not copied from its issue-tracker procedure.

## Instructions

### 1. Locate the authority

1. Follow the user's requested output and write permissions. A read-only request stays read-only. Do not infer authorization to implement behavior, publish issues, commit, or push from a request for a spec.
2. Find the project's established task source, agent instructions, and relevant maintained docs. Use `todo-manager` when a `todo/` workbench exists; otherwise keep the project's existing tracker and documentation convention. If `todo-manager` is unavailable, name that gap and ask before replacing its task workflow by hand. Do not create a second queue or migrate one without authorization.
3. Read the current conversation, relevant work record or plan, and affected code and tests. Check existing terms and decisions in maintained docs. Do not read secret-looking files, even as background research. When context is missing, identify the gap instead of inventing an agreement.

### 2. Reconcile what is known

- Separate agreed behavior from proposals, present behavior, and open contract questions. Compare conversation claims with current code, tests, and maintained docs. Surface material conflicts to the user before calling the contract settled; record non-blocking uncertainty as an open question.
- Ask only for a decision that blocks a useful contract or materially changes behavior. Do not replay already settled questions or require a fixed interview round. If domain terms themselves are disputed, suggest the available domain-modeling route rather than silently choosing definitions.
- Inspect the project's existing test seams and similar tests. Prefer tests of observable behavior at an existing, high-enough seam over new seams or implementation-detail assertions. Discuss a testing seam with the user only when that choice materially changes scope, cost, or confidence. Say when evidence for a testing approach is missing.

### 3. Choose the smallest durable artifact

- For a bounded contract, update the existing work record's concise acceptance criteria, or the project's equivalent task entry. Do not create `spec.md` solely because this skill was loaded.
- For substantial or multi-session behavior that needs detail, write `spec.md` in the existing `todo/work/<NNN-effort>/` folder and link it from the work README. If no work record exists and substantial work warrants one, use the project's workbench convention and next unused number. In a project with a different task source, follow its existing artifact convention or ask where the contract should live. Never require a root spec, hosted issue, triage label, or new tracker.
- The work README owns status, concise acceptance criteria, and the **only execution checklist**. The spec elaborates scope, behavior, scenarios or edge cases when useful, relevant decisions, testing approach, and unresolved contract questions. Link to the README's criteria rather than repeating their checkboxes. A plan owns design alternatives, not a competing checklist. Mark proposed behavior as proposed, not shipped.
- Keep stories optional and few enough to clarify the behavior. Prefer concrete scenarios or examples when they reveal ambiguity; do not manufacture an exhaustive actor-story list.

### 4. Check and hand off

1. Confirm that each material requirement is traceable to a user decision, maintained source, or explicitly marked assumption. Make consequential conflicts and open decisions visible before treating the document as agreed.
2. Check that the README link resolves, the spec and README do not duplicate checklists, and the testing approach fits the evidence. Update only the files the request authorizes.
3. Summarize the contract and remaining questions to the user. A spec does not authorize a build or add a second approval gate for implementation already requested. Preserve ordinary tool permissions, review requirements, secret protection, and the project's shipping process. Do not create automatic commits.

## When synthesis cannot finish

If a material conflict remains, leave a clearly labeled draft or answer in chat, depending on write permissions, and ask the smallest blocking question. Do not publish an apparently agreed spec. If the repo lacks a clear task authority, ask before choosing an artifact path.

## Example

The user has already decided how import failures should be reported, and the repository has `todo/work/007-import-errors/README.md`. Examine the existing import behavior and nearby tests. Keep the README's concise completion criteria and checklist; add a linked `spec.md` only if retry cases and error boundaries need durable detail. Record a conflicting error code as an open question and ask about it before claiming the contract is final. Do not create an issue or begin implementing the import change just because the spec is written.
