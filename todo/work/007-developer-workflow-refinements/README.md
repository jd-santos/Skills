---
status: complete
---

# Developer workflow refinements

## Purpose

Make the developer workflow useful in ordinary work without an adoption ceremony. Separate local repository preparation from delivery, make grilling explicit, and explain installation and migration clearly.

## Agreement and acceptance criteria

- `repo-commit` owns local inventory, review, validation, branch choice, and authorized staging/commits. Review-only requests do not authorize mutation. It never pushes or creates PRs.
- `ship` owns explicitly requested remote delivery and PR creation/update. It composes `repo-commit` for outstanding local work and can deliver an already-committed branch without manufacturing changes.
- `todo-manager` owns task lifecycle rules; `repo-commit` applies verified closeout in local commits, and `ship` checks delivery-boundary requirements. Required human review comes from actual project or user requirements, not a generic workflow gate.
- Grilling is invoked only when requested by name or when the user clearly requests that full interview. Once invoked, its full decision space is available. Otherwise routine implementation choices belong to the agent, with ordinary clarification for consequential unknowns.
- The README explains the developer workflow, companion installation, optional capabilities, and the task workbench without prescribing mandatory stages.
- A linked migration guide maps old instructions to current responsibilities, preserves historical evidence and existing trackers, and reconciles selected work against actual evidence. No bulk migration or manual adoption trial is required.

## Decisions

Use `repo-commit` for the local role and keep `ship` for delivery. A migration guide complements existing `todo-manager` migration rules; a temporary skill would duplicate them without demonstrated need. This change provides a strategy, not permission to migrate other repositories. The long-running session catalog is not a defect.

## Work

- [x] Split local preparation and delivery, and align lifecycle references.
- [x] Make grilling explicit in routing and contract synthesis.
- [x] Reorganize the README and explain companion installation.
- [x] Document targeted migration without changing historical records.
- [x] Update instruction-contract tests and validate links, metadata, and whitespace.
- [x] Review correctness and design, resolve findings, and record actual validation.

## Validation approach

Run the Python suite and Markdown link checks. Inspect scenarios for review-only use, local commits without delivery, shipping an already-committed branch, explicit grilling versus ordinary clarification, and migration of a partially delivered record. These are instruction checks and source reasoning, not proof of live agent behavior.

## Validation results

Parent checks: all 43 Python tests pass; `git diff --check` passes; the reviewed
grilling pin verifies unchanged. Active LSP checks found no diagnostics in the
three changed Python files. The touched Markdown check resolved 64 local links
and 11 anchors across 13 files, and skill names/work metadata were consistent.
Existing records `001`–`006` are unchanged. Local closeout marks this agreed
scope complete; Git records commit/delivery state. No other project is migrated.

Fresh correctness and design reviewers inspected source but could not inspect
Git state or run commands. Correctness found no source defect; design found that
migration steps sounded mandatory for an instruction-only update. The guide now
makes work-record reconciliation and tracker changes conditional, with a
regression check. These reviews and wording tests do not establish live agent
behavior, branch/index handling at runtime, or cross-host parity.

## Supporting material

- [Earlier planning/execution redesign](../006-agent-workflow-integration/README.md)
- [Current workflow](../../../README.md#development-workflow)
