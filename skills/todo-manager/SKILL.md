---
name: todo-manager
description: Manages a root-level todo workbench with a P0–P4 priority index, independent work records, and reviewed shipping cleanup. Use when managing tasks, tracking progress, preparing handoffs, or when the user mentions todos, task cleanup, or completed work.
version: 2.0.0
category: workflow
---

# Skill: Task Workbench

## Description

Keep live tasks in `todo/TODO.md`, substantial work in stable work folders, and
history in Git and PRs. Keep useful evidence without maintaining a Done task
ledger or feeding obsolete plans into future agents' context.

## Instructions

### 1. Locate the workbench

1. Find the project root. In Git, use `git rev-parse --show-toplevel`; do not
   mistake a package directory or a parent repository for this project's root.
2. Read applicable agent instructions and locate `todo/README.md` and
   `todo/TODO.md`. Check legacy root `TODO.md` and `docs/TODO.md` before creating
   anything. Follow explicit project conventions.
3. If multiple live queues exist, ask which owns the work. Follow redirect-only
   files; do not treat them as competing queues.
4. If only a legacy queue exists, maintain it until migration is authorized.
   Do not silently create a second queue or reorganize unrelated records.
5. For an authorized new workbench, use the templates in
   [references/workbench.md](references/workbench.md). Create `todo/README.md`,
   `todo/TODO.md`, and `todo/DONE.md`. Create work folders only when needed.
6. Respect read-only planning gates. Loading this skill does not authorize
   writing tasks, migration, pruning, commits, or delivery.

Read the index and the relevant work record, then follow selected links. Do not
load all retained work as current context. Never read secret-looking artifacts,
including during cleanup; keep private logs and sensitive assets out of Git.

### 2. Keep one priority index

Use these headings in order:

| Heading | Meaning |
| --- | --- |
| `## P0: Rush` | Immediate interruption or emergency work. |
| `## P1: Essential` | Required or blocking an agreed outcome. |
| `## P2: High` | Important work to prioritize next. |
| `## P3: Low` | Useful work without near-term urgency. |
| `## P4: Minor` | Small improvements or optional polish. |

Priority is not execution status. Do not create In Progress, Backlog, or Done
sections alongside these headings. Preserve user-assigned priorities. If no
priority can be inferred, use P3 provisionally and say so; ask when placement
would materially affect scheduling. Do not infer urgency from task size.

- Use `- [ ]` and `- [x]`, with two-space indentation for nested checkboxes.
- Keep small tasks and their steps inline. Link larger tasks to
  `work/<descriptive-name>/README.md` from the index.
- Put each detailed checklist in one place. A top-level index checkbox can
  summarize a linked slice, but must not duplicate its steps.
- Nest clearly related work. Ask when parentage or a matching task is ambiguous.
- Preserve unchecked work and checked state when reprioritizing.
- Suggest only genuinely high-priority issues discovered in related work,
  normally no more than one or two per session. Ask before adding speculative work.

### 3. Give substantial work a stable home

Use `todo/work/<descriptive-name>/README.md` as its local entry point. Prefer
lowercase hyphenated names, not dates, opaque IDs, or process jargon. Do not move
folders between active and archive directories when their status changes.

The work README owns purpose, execution status, current ownership when active,
acceptance criteria, the execution checklist, and links to supporting material.
Use plain language such as Planned, In progress, Blocked, Ready for review,
Ready for merge, or Retained record. Distinguish implementation from delivery;
include a known PR or commit reference without inventing one.

- Add `plan.md` only when the design no longer fits comfortably in the README.
- Name other files for their purpose, such as `research.md`, `validation.md`,
  or `migration-notes.md`. Use `assets/` for supporting images and other files.
- Add a subdirectory only when a real cluster needs grouping, with a descriptive
  name and a link from the work README. Avoid empty scaffolding and deep trees.
- Every retained artifact needs a reason to exist and an entry-point link.
- Keep one current plan. Preserve consequential rejected alternatives and their
  reasons as decisions, not competing executable plans.
- Put enduring project instructions and current architecture in maintained
  project docs. Link to them rather than treating old work records as manuals.

### 4. Coordinate concurrent agents

Before starting, inspect available task/agent status, the work record, and Git
worktree metadata. Record an agreed role or branch and bounded scope without
personal identifiers or machine-specific paths.

- Use the coordinating session to assign disjoint work where available.
- Keep one writer per checkout. Use separate worktrees for concurrent writers.
- Let each worker primarily update its own work record. Assign shared TODO
  edits to the coordinator or integrator where possible.
- Re-read the shared index before targeted edits. Reconcile it during integration;
  do not overwrite other agents' progress or reorder unrelated items.
- Ownership text and checkboxes are not locks across worktrees. If ownership
  overlaps, is stale, or cannot be established safely, ask before changing it.
- Sibling worktrees remain inspection-only unless separately authorized.

A handoff updates the existing work README with remaining steps, blockers,
validation performed, and relevant links. Do not generate a new timestamped
handoff file for every session. For an inline task, keep the handoff inline.

### 5. Complete a slice without manufacturing history

1. Check completed steps in place. Check a parent only when its whole scope and
   acceptance criteria are satisfied. A checkbox is not proof of tests or merge.
2. Keep checked entries in the live index until a reviewed closeout. Do not move
   them to a Done section or compress them into a parallel completion ledger.
3. At shipping, reconcile the record with actual diffs and checks. Remove only
   the ready scope from the live index in the same commit as that scope's
   closeout. For partial shipping, retain the parent and all unfinished work.
4. Set retained records to the actual state, such as Ready for merge, not Merged.
   Record merge or release only when verified. Direct-to-main delivery and local
   commits also need explicit, accurate delivery status.
5. If commit or delivery fails, preserve the record and report the pending state.
   Do not claim shipment or erase unfinished work. Reconcile on the next attempt.

See the shipping and cleanup rules in
[references/workbench.md](references/workbench.md). `ship` owns review and
closeout, `commit-message-writer` owns commit prose, and `changelog-writer` owns
release notes. Those skills must not manufacture delivery evidence from tasks.

### 6. Keep DONE useful and small

`todo/DONE.md` points to Git history, merged PRs when available, the existing
`CHANGELOG.md`, and retained work records. It is not a second changelog.

It may include up to three selected major release highlights with verified
release references and links to the real release notes. Do not add one entry per
task, call unreleased work a release, or require updates on every ship.

Prefer links to live PR lists or existing generated tables. Create no generation
script unless requested. Any saved table must state its source, generation date,
and refresh method; label it a snapshot rather than a current source of truth.

### 7. Handle errors and migration

- Missing or duplicate task: suggest likely matches and ask; do not guess.
- Conflicting ownership or merge conflicts: stop changes to the affected scope.
- Existing alternative plans: identify the authoritative one before consolidation.
- Broken links or unknown delivery: report uncertainty, never fabricate references.
- Legacy migration: follow the preservation and link-repair checklist in the
  reference. Never equate an old section name with a new priority automatically.

## Examples

### Small task

```markdown
## P3: Low

- [ ] Clarify setup instructions
  - [x] Verify the command
  - [ ] Update the example
```

### Larger task with concurrent work

```markdown
## P1: Essential

- [ ] [Improve import reliability](work/import-reliability/README.md)
- [ ] [Add search filters](work/search-filters/README.md)
```

Assign separate workers and worktrees. Each maintains its own detailed checklist;
the integrator reconciles this index before shipping.

### Partial delivery

The import fix is ready, but its migration tool is unfinished. Commit the fix and
its validation evidence. Keep the work item unchecked with the migration step
open. Do not label the whole effort complete or prune another worker's draft.
