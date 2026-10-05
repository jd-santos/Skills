---
status: in_progress
pr: https://github.com/jd-santos/Skills/pull/14
---

# Planning and execution workflow

The agreed planning/execution phase is implemented and reviewed. `work-routing` selects capabilities, `todo-manager` creates and maintains records, and `work-contract` supplies behavior synthesis and proportional decomposition. The competing project-note skill is retired, and optional tags replace the proposed classification fields. This PR exercises planning and execution, not the code-review or shipping workflow. The fresh-agent scenario trial is complete, and correctness/design reviews found no blockers. Later experiments remain separately open.

## Purpose

Build a coherent planning and execution workflow without a second tracker, mandatory document pipeline, or duplicate skill responsibilities. Users should not need to name skills, but may invoke them directly. Preserve this repository's task workbench, safety rules, and existing delivery responsibilities. Keep the instructions portable across supported agents without claiming untested host parity.

The [earlier implementation plan](plan.md) is historical evidence, not current instructions. Its artifact separation and skill boundaries are superseded by the agreement below. The legacy folder name remains stable to preserve existing references; the active work is no longer framed as an upstream integration. `grilling` remains a pinned external capability with source and license attribution preserved.

Earlier work added the router, retired the mandatory planning workflow in a separately authorized Dotfiles change, and fixed tracked-skill cache/executable-bit safety gaps plus adopted-workbench assumptions. Legacy generated installations may need a one-time reinstall before the newer verification hash can pass. Those changes are retained, not replayed by this phase.

## Acceptance criteria

- One live task queue and one stable, creation-order-numbered work record per substantial effort remain authoritative; no parallel `.scratch/` or hosted-issue workflow is introduced by default.
- Domain-modeling notes generated during development live in the work record. Existing maintained docs take precedence for reusable vocabulary; create a glossary only when several shared terms justify it. Reserve `docs/adr/` (or an existing convention) for consequential, agreed tradeoffs, distinguishing decisions from shipped behavior.
- Planning and execution are exercised on this redesign, with concise actual evidence. Fresh-agent scenarios check clear small work, conflicting requirements, consequential decomposition, and partial parents. Instruction tests are not presented as proof of agent behavior or cross-host parity.
- The replacement for `planning-first` removes mandatory conversational rounds and its separate save/build approvals. One confirmation of shared understanding precedes the requested next step, subject to tool permissions, secret protection, human decisions, and Git delivery safeguards.
- Automatic routing and optional direct invocation select distinct responsibilities. Task management owns record creation and lifecycle; contract synthesis owns behavior and a proportional decomposition method. The retired note skill has no wrapper or competing schema.
- Authorized substantial work can have a durable record before its contract is settled. Existing records are reused; small work stays inline; exploration and explicit read-only requests do not authorize writes.
- Readiness requires resolved consequential behavior, observable acceptance criteria, and credible validation. Routine technical choices remain agent-owned; material scope, delivery, and dependency changes return to the user. Execution follows the agreement rather than rewriting it to fit the build.
- Metadata remains lean, with optional tags and no required deadlines, life-area/project classification, or repeated Git audit fields. Existing notes and records are preserved without bulk migration. Separate decomposition skills require demonstrated value, not a document filename.
- Portable instructions avoid harness-specific invocation assumptions. Cross-host checks remain later work; no host configuration or submodule pin changes are made here.
- Existing `ship`, `todo-manager`, `commit-message-writer`, and `changelog-writer` remain the owners of delivery and task closeout. PR descriptions retain their detailed reasoning and validation, with relevant screenshots, short excerpts, or diagrams added when they clarify the change.

## Work

- [x] Agree on README-first ownership, useful supporting documents, and lean YAML; migrate only this record. [context: small]
- [x] Pin and verify grilling, connect its portable discovery pointer, and run the earlier bounded write trial and read-only scenarios. Evidence and limitations are retained below. [context: small]
- [x] Validate the earlier alignment with regression tests and distinct correctness/design reviews; resolve the metadata query gate and stale trial wording. [context: small]
- [x] **P2: Agree on planning and execution responsibilities** through the installed grilling source, including record creation, synthesis, decomposition, metadata, and this PR's bounded trial. [context: small]
- [x] Rename synthesis to `work-contract`, add proportional decomposition and execution handoff, and retire `project-issue-note` entirely. Salvage useful discovery, duplicate-prevention, and preservation guidance into task management. [context: medium]
- [x] Align routing and task management with automatic capability selection, optional direct invocation, early durable records, and optional tags; keep only one metadata authority. [context: small]
- [x] Update maintained README, changelog, queue, and local references; retain historical evidence and existing records. [context: small]
- [x] Add focused instruction-contract regression tests for readiness, creation ownership, decomposition, execution safeguards, metadata, and retirement. [context: small]
- [x] Run fresh-agent planning/execution scenarios on the current instructions; test conflict escalation, small direct work, consequential splits, and partial completion. Record actual outcomes and limitations, not just test expectations. [context: medium]
- [x] Run separate correctness and design implementation reviews, resolve findings, and rerun validation. These reviews are safeguards for this change, not adoption of a new code-review workflow. [context: small]
- [ ] Verify delivery for records `002`, `003`, and `005`, then reconcile their status and queue/map links separately. Confirm the ambiguous P2 promotion target before changing priorities. [context: small]
- [ ] **P3: Define supporting-document methods and eventual subskills** from the candidates below. Trial useful methods before approving any new specialist. [context: medium]
- [ ] Validate retrieval and routing in other supported hosts without claiming that Pi source access proves parity. [context: small]
- [ ] Adapt domain modeling to workbench-first capture and selective documentation promotion; trial a real ambiguity before creating a glossary or ADR. [context: medium]
- [ ] Trial decomposition on a real independently delivered multi-slice effort before considering a separate specialist. The method belongs in `work-contract` now; no ticket skill is introduced. [context: medium]
- [ ] Assess later review/TDD capabilities and selective visual PR evidence against existing reviewers and `ship`; make changes only in later authorized work. [context: medium]
- [x] Add the portable router and reserve Wayfinder as a future route; align project-fit capture and read-only boundaries. [context: small]
- [x] Retire `planning-first` and Pi's `/plan` in a separately authorized Dotfiles change; number existing work records by creation order. [context: small]

## Next decisions

The boundary decisions are settled and implementation is authorized. One work README owns the full outcome, behavior contract, acceptance criteria, decisions, metadata, and sole execution checklist. Supporting detail has an independently useful reading or evidence purpose; length alone does not require another document. Keep stable headings, targeted edits, and concise evidence rather than progress journals or conversation transcripts.

| Responsibility | Owner |
| --- | --- |
| Select useful capabilities automatically while allowing direct invocation | `work-routing` |
| Find/create records, maintain queue and metadata, validate relationships and lifecycle | `todo-manager` |
| Reconcile decisions with evidence, define behavior/readiness, and propose proportional decomposition | `work-contract` |
| Follow the agreement, validate outcomes, and update its checklist at meaningful checkpoints | The executing agent, using task-management rules |
| Existing reviewed closeout and Git delivery when requested | `ship`, unchanged unless directly affected |

Record creation occurs once authorized work warrants a durable home and its purpose/current scope are known, not only after contract readiness. Preserve existing records; avoid duplicate notes. Synthesis is substantive reconciliation: resolve consequential behavior, observable criteria, and credible validation before declaring affected scope ready. Routine implementation choices remain agent-owned.

Decomposition starts with one outcome-oriented checklist. Changes to scope, delivery order, independently deliverable outcomes, or consequential dependencies require the user's decision before becoming commitments. Approved child records are created by task management only when useful; separate documents and a standalone slicing skill are not prerequisites.

The user authorized retiring the competing note skill, preserving useful guidance in the appropriate owners, and renaming synthesis to `work-contract` without a wrapper. The metadata decision keeps optional tags for subjects/subsystems but excludes mandatory taxonomy, deadlines, life-area/project fields, and repeated Git audit data. Obsidian is not a design priority or a reason to duplicate metadata.

This PR's end-to-end claim is limited to planning and execution on the redesign. It does not exercise the code-review or shipping workflow, update a PR, or authorize Git delivery. Ordinary implementation review requirements remain applicable. No bulk migration, historical-plan deletion, host configuration, or submodule pin changes are authorized.

## Supporting-document methods

The P3 task should define optional methods, not a compulsory document catalog or one skill per filename. Start with research, design, and validation. Evaluate these candidates only when actual content needs a separate home:

| Candidate | Distinct value |
| --- | --- |
| `research.md` | The question, sources and dates, findings, uncertainty, and implications for the decision. Avoid a search transcript. |
| `design.md` | Constraints, alternatives, chosen approach, interfaces or user flows, and tradeoffs. Coordinate with technical-writing and the planned design family instead of duplicating them. |
| `import-design.md` or another subject-named design | Apply the design method to concrete concerns such as data mapping, rejection policy, idempotence, and compatibility. A specialized filename does not automatically justify a separate skill. |
| `validation.md` | Observable checks, actual results, environment limitations, and concise reproducible evidence. Distinguish planned checks from executed ones. |
| `migration-notes.md` | Compatibility, transition sequence, data handling, and recovery for changes with a real migration burden. |
| `investigation.md` | Reproduction, competing explanations, evidence that rejects them, and the remaining diagnostic question. Useful for difficult bugs. |
| `rollout.md` | Staged delivery, monitoring, stop conditions, and rollback when deployment risk warrants a separate runbook. |

Keep status and the sole execution checklist in the work README. Supporting methods may define scenarios or procedures, not duplicate progress tracking. Move detail rather than mirror it; omit empty scaffolding. Trial each approved method before making a portable subskill, with a small independently reviewable packet per implementation. The full catalog and all subskills are not prerequisites for the first write trial.

## Grilling discovery and write trial

The pinned installation and router fallback were verified in the earlier write trial. The current boundary interview read the installed `grilling` source and used twelve numbered decisions across three frontier rounds. The user confirmed the shared understanding and authorized implementation without a second build approval. The interview exposed the old schema's Obsidian origin, settled useful metadata, established responsibility boundaries, and narrowed the trial to planning/execution. This supplies actual human-interaction evidence, not just source retrieval or agent synthesis.

The source remains pinned and unchanged; no interview wrapper or mandatory gate is added. Pi retrieval and this conversation do not establish automatic catalog discovery, other-host behavior, or general question-quality performance. The full supporting-document catalog remains a separate later task, not a prerequisite for these trials.

## YAML metadata and pre-merge closeout

Agreed fields: required `status`, optional `pr`, `blocked_by`, `parent`, `child`, and `tags`. Apply work-item YAML only to `todo/work/*/README.md`, not the workbench introduction, supporting documents, or unrelated READMEs. The exact types, values, relationship checks, and lifecycle rules live in the [todo-manager reference](../../../skills/todo-manager/references/workbench.md#work-record-yaml); do not maintain another schema here. This record is migrated as part of the authorized slice; other existing records retain their format.

`parent` is one work-record path; `child` is a list. Hierarchy is optional, independent of dependencies, and does not require reciprocal fields or mirrored checklists. `blocked_by` lists real prerequisites. Omit unused fields and keep priority in TODO; no owner, model, harness, timestamp, or empty-placeholder fields are added.

Prepare `status: complete` in reviewed pre-merge closeout only when the record's whole agreed scope and required checks are verified. This describes work completion, not merge or release. Task entry reconciles only the selected stale record; implementation/handoff update meaningful checkpoints; `ship` verifies evidence and removes only ready scope in the closeout commit. Failed delivery is reported separately; new scope or failed validation reopens work. No post-merge status-only commit is required. Later workflow experiments remain open even when planning/execution is verified. This phase does not test shipping or change its closeout semantics.

### Representative scenarios

- **One substantial contract:** Keep the outcome, behavior contract, acceptance criteria, decisions, and sole checklist in the work README. Add linked subject-named detail only when it has a separate reading or evidence purpose; do not mirror status or checklists there.
- **Hierarchy versus dependency:** A containing work record may use `child`, or a subordinate record may use `parent`; either relationship is optional, and one direction is enough. Neither makes work dependent or blocked. Use `blocked_by` only for actual prerequisites, independently of any hierarchy link.
- **Partial parent:** If one contained outcome is verified but other agreed parent scope remains open, keep the parent non-complete. Mark it complete only after its whole agreed scope and required checks, including required child outcomes, are verified; containment alone does not decide which outcomes are required.
- **Delivery failure versus validation failure:** If scope and required checks are verified but commit or delivery fails, preserve that verified work and report delivery as pending without claiming merge or release. If validation fails or new scope is found, keep or reopen the record and do not mark it complete.

## Delegated dry-run findings

A fresh read-only agent applied the local router and spec-synthesis method to this effort and exercised three scenarios. A fully specified tiny issue selected direct work and an inline TODO; a README-sized feature selected one provisional work record; a multi-slice effort selected a parent checklist with child records only for independent ownership or delivery. The agent returned a provisional contract and blocked slice proposal without publishing artifacts or inventing human agreement.

At the dry-run checkpoint, the principal mismatch was `to-spec`'s substantial-contract trigger for `spec.md` versus the router's needs-room trigger. Neither implemented the README-complete model then, and the workbench map repeated volatile status. The current slice aligns those instructions and removes the map's mirrored status. Unnecessary files and repeated prompts are instruction-level risks, not observed runtime failures in this non-publishing exercise. Authority was discoverable through the workbench entry point, but the old full contract still required reading the plan.

The agent reran all 21 tests successfully and confirmed `grilling: not installed` in this checkout. The tests assert wording/metadata rather than real agent behavior. Installed grilling interaction, human-confirmed synthesis, cross-agent retrieval, and a genuine ticket-method trial remain unvalidated. That historical installation gap is repaired in the current slice and the README-first instructions are aligned; the historical boundary uncertainty was subsequently resolved by the interview above. Keep this concise evidence here rather than adding a trial transcript or another report file.

## Boundaries

The existing [P3 Wayfinder task](../../TODO.md#p3-essential) remains separate; this phase does not reprioritize other work. The six existing record numbers and paths remain stable. Permission-gate changes, tracker migration, host configuration, and Dotfiles delivery are outside this repository's authorized implementation. Existing historical plans and earlier review evidence remain readable but are not executable guidance. Normal implementation reviewers check this diff; they do not establish a new workflow capability or authorize shipping.

## Implementation checkpoint

This section retains earlier implementation evidence, not the current slice's validation receipt.

At that checkpoint, the six work folders had been numbered `001`–`006` by first Git addition, and the agreed [spec and future tickets contract](plan.md#process-contract) had been saved before the requested compaction. The local `to-spec` skill, router update, focused tests, and Skills README and changelog changes were then described as belonging to the “Skills integration” branch. The checkpoint treated the parent Dotfiles submodule pin as a separate delivery. That integration framing was later superseded by the current planning/execution redesign described above.

At that earlier checkpoint, the `to-spec` and installed `grilling` trials were recorded as still open. Synthesis was later renamed to `work-contract`, and the `grilling` interview and bounded fresh-agent scenario exercise were carried out; see Current slice validation for actual evidence and limits. Testing decomposition on a real independently delivered effort remains follow-up work. The earlier checkpoint proposed starting with one readable checklist and splitting into numbered work records only for backlog clarity or independent ownership while preserving real blockers and the wide-refactor exception. [context: medium]

At the earlier compaction checkpoint, all 16 Skills tests, `tracked-skills verify grilling`, local Markdown links, and `git diff --check` passed. A read-only correctness review found no migration blocker, and a design review found the spec/tickets ownership coherent. Six moved documents matched `HEAD` byte-for-byte; the other three were intentionally edited. At the implementation checkpoint for the skill changes, all 21 Skills tests, `tracked-skills verify grilling`, local Markdown links, `git diff --check`, and LSP checks of the changed Python tests passed. Fresh correctness and design reviewers found no blockers; the unavailable `todo-manager` fallback and contract-critical tests were strengthened after review. That checkpoint recorded a live behavior-contract trial and cross-agent retrieval checks as open. A bounded source-informed scenario exercise was later performed as described below; it is not general agent-behavior proof, and catalog discovery/cross-host retrieval remain unvalidated. The checkpoint also noted a pre-existing queue inconsistency: records `002`, `003`, and `005` were described as Ready for review or merge but absent from `todo/TODO.md`. It proposed verifying their delivery and reconciling them separately rather than assuming they were active or done.

## Earlier alignment validation

This receipt describes the previous instruction alignment, before the boundary redesign and installed-source interview. A fresh Pi worker retrieved `skills/grilling/SKILL.md` through the router's relative pointer when grilling was absent from its available-skill list. It loaded the updated synthesis and task-management instructions and made targeted writes only to this README, adding the four scenarios above. No supporting artifact, duplicate metadata/checklist, hierarchy link, or parent-completion claim was generated. This is a bounded live synthesis/write trial on a settled contract, not an interactive grilling test, human signoff, or cross-agent discovery result. Conflict handling, testing-seam judgment, and hierarchy edits on real related records remain untested.

The parent ran all 30 tests successfully, verified the pinned grilling installation at `c55ee460`, parsed this record's YAML, and checked 74 local Markdown links plus 10 heading anchors. Active diagnostics were clean for the changed files, including the added regression test and review fixes. The tests protect instruction wording/metadata, not agent behavior. Record `006` alone was migrated; records `001`–`005` remain untouched. Fresh correctness and design reviewers inspected the current source without shell/Git tools. Correctness found a conflicting metadata query gate in `project-issue-note`; it now delegates to `todo-manager`'s required schema, with a focused regression test. Design found stale trial/installation wording and an overly broad schema-table test; those were corrected. The focused correctness follow-up found the metadata blocker resolved and no remaining blockers. Tests, link checks, and Git checks remain parent-run evidence. The completed discovery/write-trial entry stays checked in TODO until reviewed shipping closeout; the wider work retains `status: in_progress`. PR #14's head still matches this checkout at `bc4817a`, and remote main remains its ancestor; no merge or rebase was needed. Nothing is committed or pushed in this slice.

## Current slice validation

The human boundary interview and parent implementation exercise planning and execution on this real effort. Parent checks: all 36 tests passed, diff whitespace was clean, the grilling pin was verified, and active diagnostics were clean on 13 changed files. YAML parsed correctly; 70 local Markdown links and ten heading anchors resolved, including historical source links checked against Git snapshots. The suite includes instruction-contract checks, which protect written rules rather than agent behavior.

Fresh-agent trial: a Pi worker read the canonical `work-routing`, `todo-manager`, and `work-contract` sources, then applied them to the five scenarios below and an explicit read-only planning request. This is a source-informed reasoning exercise, not observed behavior from hypothetical implementations.

- A fully specified small label fix uses direct work and the existing inline TODO; create no record or contract.
- An authorized substantial import with known purpose and scope gets a durable work record now, with duplicate handling captured as open. Do not invent acceptance criteria or implement the affected behavior before resolving that question and establishing a credible validation approach.
- A request to overwrite duplicates conflicts with the existing reject decision. Treat it as unresolved, pause that behavior, and ask the user which contract applies; do not rewrite the record to fit the request.
- A validation/preview split that changes delivery order is a contract change, not routine checklist organization. Present the proposed sequence and tradeoffs, confirm the intended order, then have `todo-manager` create child records only if useful and approved.
- A verified child does not complete a containing record while required recovery remains untested. Keep the parent `in_progress` and its remaining outcome open; check only independently verified scope.
- An explicit read-only feature plan stays in chat, with assumptions and open decisions labeled. Do not edit the queue or create a work record.

No instruction conflict surfaced in the current sources. The duplicate-policy and delivery-order cases hand off to the user before affected work becomes a commitment. The worker independently ran `python3 -m unittest discover -s tests -v` (36 passed), `git diff --check` (passed), and `git diff --cached --name-only` (empty). Direct source access does not prove skill-catalog discovery or cross-host parity. The worker did not rerun grilling verification or active diagnostics. Fresh correctness and design reviewers completed source-only implementation reviews with no blockers. They could not independently run commands or inspect Git state; parent and worker checks remain attributed separately. The design review's stale summary and ambiguous phase/umbrella queue labels were corrected. No code-review or shipping workflow is being adopted or tested. No commit, push, merge, PR update, or shipping trial has occurred.

## Supporting material

- [Earlier implementation plan and adoption sequence](plan.md), retained as superseded historical evidence
- [Current task workbench](../../README.md) and [live priorities](../../TODO.md)
- [Workflow router](../../../skills/work-routing/SKILL.md) and [work contract](../../../skills/work-contract/SKILL.md)
- [Task workbench skill](../../../skills/todo-manager/SKILL.md)
- [Tracked external skills workflow](../../../docs/tracked-skills.md)
- [Pinned grilling source](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/grilling), with attribution and licensing retained in the installer registry
