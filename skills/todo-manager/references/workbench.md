# Workbench templates and closeout

## Minimal project workbench

Create these files only when task tracking or migration is authorized. Adapt the
text to the project rather than leaving placeholders and empty example folders.

### `todo/README.md`

```markdown
# Project workbench

[TODO](TODO.md) is the live priority queue, mostly for agents.
[DONE](DONE.md) points to development history and retained evidence.

## How to work here

- P0: Rush, P1: Essential, P2: High, P3: Low, P4: Minor.
- Small checklists stay in TODO. Larger efforts link to a work README under
  `work/<descriptive-name>/`, which owns their detailed checklist.
- Read the relevant work README before its supporting files. Historical records
  explain past work; they are not current implementation instructions.
- Agree on ownership before starting. Parallel workers use separate worktrees
  and primarily edit their own records. Ownership notes are not locks.
- Check completed steps in place. Shipping reconciles the ready scope and
  removes it from the queue, without adding a Done task ledger.
- Preserve useful evidence. Propose deletions and resolve obsolete guidance
  before merge. Post-merge branch housekeeping is a separate operation.
```

Add a short map to existing work areas or maintained project docs when useful.
Do not enumerate every artifact here; work READMEs own their local maps. A
high-level focus paragraph is optional, but needs a review date and an owner to
avoid becoming another stale status report.

### `todo/TODO.md`

```markdown
# TODO

## P0: Rush

## P1: Essential

## P2: High

## P3: Low

## P4: Minor
```

### `todo/DONE.md`

```markdown
# Done

The story lives in Git, not another completed-task list.

- Use `git log` for the development history.
- Follow the relevant work record for retained decisions and evidence.
```

Link the existing changelog using its actual path. Add verified repository
history and merged-PR links only when the host and repository are known and safe
to publish. Do not make GitHub or PR use a requirement. If no work folders exist,
explain the convention rather than creating an empty archive or broken link.

Optional recent highlights contain at most three major releases, with a short
blurb and a link to each release's changelog section or release page. This is
curation, not a mandatory ship-time log. Links to live PR queries are preferable
to copied tables; existing generated reports can be linked without building a
new generator.

### `todo/work/<descriptive-name>/README.md`

```markdown
# Work title

Status: Planned.

## Purpose

The problem and intended outcome.

## Acceptance criteria

The observable conditions that make this slice complete.

## Work

- [ ] First concrete step

## Supporting material

Link only files that exist and help this work.
```

Replace instructional prose with actual content. Add active ownership and scope
when work starts. Add validation, decisions, blockers, or handoff notes when
needed; omit empty sections. If a separate plan owns the design, link it instead
of copying it. The work README still owns the execution checklist.

## Reviewed pre-merge closeout

Review only the shipping scope. Read-only reviewers can recommend changes but
cannot prune files or close tasks. The shipping agent:

1. Matches tasks and acceptance criteria to the actual diff and validation.
2. Inventories associated artifacts and classifies them:
   - **Keep:** useful evidence, research, screenshots, or validation results.
   - **Consolidate:** repeated summaries, handoffs, and overlapping notes.
   - **Resolve:** competing plans or claims no longer true. Preserve significant
     alternatives and rejection reasons in the final decision record.
   - **Promote:** enduring guidance that belongs in maintained project docs.
   - **Propose removal:** scratch output, empty scaffolding, or redundant drafts.
3. Presents proposed file deletions by path and reason, including apparently
   temporary files. Apply only after explicit approval. Deletion is not implied
   by "ship" or "mark done." Never clean unrelated or concurrently owned work.
4. Updates retained material and navigation. A stale plan's header must say it is
   historical or superseded and link to the final decision/current guidance.
   Clearly distinguish observations at the time from claims about current code.
   For non-text evidence, put provenance and scope in its linked README.
5. Checks for unique rationale, unresolved questions, evidence, and inbound links
   before consolidating. Do not discard unique information without approval.
6. Fixes links after approved changes and preserves original evidence where it
   is useful. If deletion is declined or unanswered, keep the file, label any
   known obsolete guidance, and report pending cleanup instead of blocking safe
   unrelated delivery. Sensitive material remains a shipping blocker.
7. Updates the changelog for notable behavior or workflow changes. Existing
   location and release conventions win; default to root `CHANGELOG.md` only
   when creating one. Do not relocate it into `todo/`.
8. Carries purpose, consequential decisions, validation, migration notes, and
   limitations into commit bodies and PR descriptions where relevant. Preserve
   the story even if commits will be squashed. Do not copy the whole checklist.
9. Removes only the ready scope from the priority index in its closeout commit.
   Preserve unfinished parent tasks and unrelated or concurrent work. Retain
   useful work records at their stable paths with accurate delivery status.

Pre-merge plans and evidence can be committed as plans and evidence. They must
not present proposed behavior as already delivered product documentation.

## After merge

Branch/worktree cleanup requires a separate authorized workflow. Verify merge
using the host's PR state or Git history as appropriate; squash merges may not
preserve branch commit ancestry. Verify clean state, ownership, and active-agent
status before removing anything. Never delete a sibling or active worktree as a
side effect of task closeout.

If a tracked record still says Ready for merge, a later verified reconciliation
can mark it as retained historical evidence. Do not require a ceremonial
post-merge commit solely to update status. Treat an unverified state as unknown,
not evidence that work is still unmerged. If the work resumes, re-check delivery
and add a new slice to the index rather than executing the old plan blindly.

## Legacy migration

Migration is a deliberate change, not a side effect of adding a task:

1. Inventory root `TODO.md`, `docs/TODO.md`, existing work notes, and their inbound
   links. If more than one queue is live, ask which owns the work.
2. Agree on scope, priorities, and ownership. Old In Progress/Up Next/Backlog
   sections express status or ordering, not P0–P4 urgency. Preserve that context
   in the relevant work record; ask about material priority ambiguities.
3. Preserve all unfinished work, nested steps, and checked state. Split detailed
   records only where useful. Leave unrelated `docs/` material where it is.
4. Retire the old Done section only after checking that its unique information
   is committed and recoverable or retained in an appropriate record. Never
   assume uncommitted Done entries already exist in Git history.
5. Create the new queue and entry points, repair affected links, and retire the
   old live queue. With deletion approval, remove it; otherwise replace it with
   a redirect-only note. Never leave two independently editable queues.
6. Update relevant agent instructions and planning/shipping references within
   the authorized scope. Report other conflicting instructions rather than
   silently changing unrelated repositories.
