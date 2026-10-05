---
name: todo-manager
description: Creates and maintains task entries and work records with a P1–P5 priority index, metadata, and lifecycle rules. Use when tracking work, preparing handoffs, managing todos, or when the user asks to create a project, issue, feature, or work record in the established task source.
version: 2.4.0
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
   Write the README as the human-facing introduction to the workbench, not as
   agent instructions. Explain its purpose, credit and link the todo-manager
   workflow, summarize the live-index/work-record/Git-history model, and map
   the local files. Adapt the wording to the project instead of copying a
   generic rules list.
6. Respect read-only planning gates. Loading this skill does not authorize
   writing tasks, migration, pruning, commits, or delivery. In a project with a
   different established tracker, follow its conventions rather than installing
   a workbench or a second standalone-note schema.

Read the index and the relevant work record, then follow selected links. Do not
load all retained work as current context. Never read secret-looking artifacts,
including during cleanup; keep private logs and sensitive assets out of Git.

### 2. Keep one priority index

Use these headings in order:

| Heading | Meaning |
| --- | --- |
| `## P1: Rush` | Immediate interruption or emergency work. |
| `## P2: High` | Important work to prioritize next. |
| `## P3: Essential` | Required or blocking an agreed outcome. |
| `## P4: Low` | Useful work without near-term urgency. |
| `## P5: Minor` | Small improvements or optional polish. |

Priority is not execution status. Do not create In Progress, Backlog, or Done
sections alongside these headings. Preserve user-assigned priorities. If no
priority can be inferred, use P4 provisionally and say so; ask when placement
would materially affect scheduling. Do not infer urgency from task size.

- Use `- [ ]` and `- [x]`, with two-space indentation for nested checkboxes.
- Keep small tasks and their steps inline. A task that fits in one or two
  sentences, especially a loosely defined future idea, belongs in TODO even if
  it may later grow. Create a work record only when detailed planning,
  coordination, evidence, or a multi-step checklist would make the index hard
  to use. Link those larger tasks to `work/<NNN-descriptive-name>/README.md`.
- Put each detailed checklist in one place. A top-level index checkbox can
  summarize a linked slice, but must not duplicate its steps.
- In a new workbench, number work folders by creation order as
  `work/001-descriptive-name/`, `work/002-next-effort/`, and so on. Use the next
  unused number for a new record; do not renumber on priority or status changes
  or reuse gaps. The prefix is a browsing aid, not a second priority scale.
  Respect an existing project's naming convention until migration is authorized.
- Nest clearly related work. Ask when parentage or a matching task is ambiguous.
- Preserve unchecked work and checked state when reprioritizing.
- Suggest only genuinely high-priority issues discovered in related work,
  normally no more than one or two per session. Ask before adding speculative work.

### 3. Give substantial work a stable home

Use `todo/work/<NNN-descriptive-name>/README.md` only for substantial work that
needs a durable home beyond its TODO checkbox. Do not create a folder merely
because an item is in TODO. Prefer lowercase hyphenated descriptive names with
this workbench's stable creation-order prefix, not dates, opaque IDs, or process
jargon. Do not move folders between active and archive directories when their
status changes.

This skill owns record discovery and creation, not the behavior decisions that
fill it. Create a record when authorized work needs a durable home and its
purpose and current scope can be stated honestly; a settled contract is not a
prerequisite. Capture open questions without inventing acceptance criteria or
creating empty scaffolding. Small work stays inline; exploratory conversation
alone does not authorize task writes.

Before creation, search the index and relevant records for the same work. Reuse
a matching record rather than creating a duplicate. Infer a readable title from
agreed intent; ask only when the title, scope, priority, or authority is materially
ambiguous. Preserve existing standalone notes and unknown non-sensitive metadata
until migration is authorized; link useful evidence instead of copying it.

The work README owns purpose, the full behavior contract, decisions, acceptance
criteria, the execution checklist, and links to supporting material. Substantial
and multi-session work still defaults to that README. Use a compact current
summary and stable headings for selective reading, not dated progress journals.
Use `work-contract` when synthesis or decomposition needs substantive reasoning;
it supplies content while this skill owns layout, metadata, and lifecycle.

For new or explicitly migrated `todo/work/*/README.md` records, keep metadata in
YAML frontmatter: required `status`, optional `pr`, `blocked_by`, `parent`,
`child`, and `tags`. Omit absent fields. Tags are an optional nonempty list for
useful subjects or subsystems, not a required classification exercise. Do not
mirror status or next actions in the body or navigation map; priority belongs in TODO. Do not require timestamps, model,
harness, owner, or session logs. Use the schema and relationship rules in
[references/workbench.md](references/workbench.md). Do not put this schema on
supporting documents, `todo/README.md`, skill READMEs, or unrelated project docs.
Respect existing metadata and plaintext records until migration is authorized.

Use `awaiting_human_review` only when a required signoff blocks the next closeout
step. `complete` means the record's entire agreed scope and required checks are
verified complete, not that a PR merged or a release occurred. Record a real PR
reference when known; never invent delivery evidence. Reconcile only the selected
record at task entry when stale, update it at meaningful implementation/handoff
checkpoints. `repo-commit` applies reviewed local/pre-merge closeout when
commits are requested; `ship` checks requirements due at remote delivery.

- Routine checklist organization stays within authorized scope. Changes to
  agreed scope, delivery order, independently deliverable outcomes, or
  consequential dependencies require the user's decision before creating the
  corresponding records or treating those changes as commitments.
- Add subject-named supporting detail only when it has an independently useful
  reading or evidence purpose, or the user explicitly requests it. Length alone
  does not require `plan.md` or `spec.md`; move detail rather than mirror it.
  Preserve useful existing documents without unauthorized migration.
- Add a `## Human review` section only when a human decision, visual check,
  deployment check, or signoff is needed. Make each item a checkbox labeled
  Required or Optional and its timing, such as Required before merge. Include
  concise `How` and `Look for` guidance so the reviewer can execute the check.
  Do not add an empty section to records without review requirements.
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
3. At each relevant boundary, such as readiness for merge, shipping, or
   deployment, surface outstanding required human-review items in chat. Do not
   claim a review happened or check its box unless the user confirms it.
4. At authorized local closeout, reconcile the record with actual diffs and checks. Required
   review blocks its stated closeout step; optional review does not block safe
   delivery. Remove only the ready scope from the live index in the same commit
   as that scope's closeout. For partial completion, retain the parent and all
   unfinished work.
5. In the pre-merge closeout commit, set a YAML record to `status: complete` only
   when its whole agreed scope and required checks, including review due at that
   boundary, are satisfied. Keep partially complete parents open. Respect a
   legacy record's existing format until migration is authorized. Record merge
   or release only when verified; completion is not Git delivery.
6. If commit or delivery fails, preserve verified work completion and report the
   pending delivery separately; do not manufacture merge evidence. Reopen the
   record when scope or validation fails. Keep unfinished work in the index and
   reconcile on the next attempt. No ceremonial post-merge status commit is needed.

See the closeout and cleanup rules in
[references/workbench.md](references/workbench.md). This skill owns lifecycle
rules; `repo-commit` applies local review and commit closeout, `ship` owns remote
delivery, `commit-message-writer` owns commit prose, and `changelog-writer` owns
release notes. None may manufacture delivery evidence from tasks. Loading a skill
for inspection does not authorize closeout. Human review is required only when
an actual project or user requirement makes it due, not as an adoption ceremony.

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
## P4: Low

- [ ] Clarify setup instructions
  - [x] Verify the command
  - [ ] Update the example
```

### Larger task with concurrent work

```markdown
## P3: Essential

- [ ] [Improve import reliability](work/001-import-reliability/README.md)
- [ ] [Add search filters](work/002-search-filters/README.md)
```

Assign separate workers and worktrees. Each maintains its own detailed checklist;
the integrator reconciles this index before shipping.

### Partial delivery

The import fix is ready, but its migration tool is unfinished. Commit the fix and
its validation evidence. Keep the work item unchecked with the migration step
open. Do not label the whole effort complete or prune another worker's draft.
