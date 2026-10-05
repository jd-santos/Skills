# Workbench templates and closeout

## Minimal project workbench

Create these files only when task tracking or migration is authorized. Adapt the
text to the project rather than leaving placeholders and empty example folders.

### `todo/README.md`

Write this as the front page for a person encountering the workbench, not as an
agent rule sheet. It should answer four questions:

1. What is this workbench for?
2. Which todo-manager concepts shape it?
3. What belongs in TODO, `work/`, and DONE?
4. Where can someone read the full workflow?

Credit and link the upstream
[`todo-manager`](https://github.com/jd-santos/Skills/tree/main/skills/todo-manager)
skill. If the project also carries a local copy, link that as the version agents
actually load. Keep operational details such as worktree coordination, artifact
cleanup, and migration rules in the skill unless project users need them here.

```markdown
# Todo workbench

This directory follows the
[`todo-manager`](https://github.com/jd-santos/Skills/tree/main/skills/todo-manager)
workflow from [jd-santos/Skills](https://github.com/jd-santos/Skills). It keeps
unfinished work readable without turning Markdown into a second issue tracker.

The workflow keeps current priorities, detailed working material, and shipped
history separate:

- [TODO](TODO.md) is the live P1–P5 priority list.
- [`work/`](work/) gives substantial efforts a stable home for their checklist,
  decisions, and supporting material.
- [DONE](DONE.md) points to Git history and retained evidence. It is not another
  completed-task list.

## Priorities

1. **P1: Rush** for work that needs immediate attention.
2. **P2: High** for important work that should happen next.
3. **P3: Essential** for required work without immediate urgency.
4. **P4: Low** for useful work that can wait.
5. **P5: Minor** for small improvements and optional polish.

## Using the workbench

Keep short tasks in TODO. Give larger efforts a creation-order-numbered,
descriptive folder under `work/`, with one README that owns the detailed
checklist. During verified local closeout, remove only ready scope from the live
list. Git, pull requests, and the project's changelog tell the finished story;
local completion does not claim remote delivery.
```

Adapt the title and opening to the project. Add links to the actual changelog,
project docs, local skill, or important work areas when useful. Do not enumerate
every artifact here; work READMEs own their local maps. Avoid volatile status
summaries. If a current-focus paragraph is truly useful, include a review date
and owner so it does not silently become stale.

### `todo/TODO.md`

```markdown
# TODO

## P1: Rush

## P2: High

## P3: Essential

## P4: Low

## P5: Minor
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

### `todo/work/<NNN-descriptive-name>/README.md`

```markdown
---
status: planned
---

# Work title

## Purpose

The problem and intended outcome.

## Acceptance criteria

The observable conditions that make this slice complete.

## Work

- [ ] First concrete step

## Supporting material

Link only files that exist and help this work.
```

Replace instructional prose with actual content. Keep the full agreement,
behavior contract, decisions, and sole execution checklist in the README by
default, including for substantial work. Use stable headings for selective
reading and targeted edits. Add validation, blockers, or handoff notes only when
needed. Attach subject-named detail only for independently useful reading or
evidence, or an explicit user request; length alone does not require a separate
plan or spec. Move detail rather than mirror it. Preserve existing evidence.
For a record created before contract readiness, state its actual purpose/current
scope and open questions; omit unsettled criteria instead of filling headings
with `TBD` or pretending behavior is agreed. `planned` records are not inherently
ready to implement. Contract readiness is established by the agreement and
validation approach, not inferred from a metadata value.

### Work-record YAML

Apply this schema to new or explicitly migrated `todo/work/*/README.md` files,
not the workbench introduction, supporting documents, skills, or unrelated
project READMEs. Existing record formats remain valid until an authorized
migration; never bulk-convert the archive at task entry.

| Field | Type and meaning |
| --- | --- |
| `status` | Required string: `planned`, `in_progress`, `blocked`, `awaiting_human_review`, `ready_for_review`, `ready_for_merge`, or `complete`. This describes work, not merge or release. |
| `pr` | Optional string: a real PR URL relevant to this record. Its presence does not prove delivery or cover every remaining slice. |
| `blocked_by` | Optional nonempty list of work-record paths or external issue/PR URLs that are actual prerequisites. For an unresolved human decision without a record, use the relevant question/review section and `blocked` status instead of inventing a record. |
| `parent` | Optional string: the containing work record's repository-root-relative README path. |
| `child` | Optional nonempty list of subordinate work-record README paths, each repository-root-relative. The singular field name is intentional. |
| `tags` | Optional nonempty list of unique, nonempty strings for useful subjects or subsystems. No mandatory taxonomy or tagging requirement. |

Omit unused fields rather than writing empty values. Keep priority in TODO; do
not require timestamps, harness/model details, owner fields, or per-session logs.
Do not add deadlines, life-area/project classification, or a separate subsystem
field by default. Use tags only when useful; omit empty or duplicate tags. Git
provides change history, not a reason to repeat audit metadata in each record.
The header is the sole metadata authority. The body owns decisions and the next
actions checklist, not copies of header values. Navigation links may repeat a
path for usability but not volatile status.

Use hierarchy only when separate records improve independent ownership or
delivery, not merely to split a long README. `parent` and `child` express
containment; `blocked_by` expresses dependency. Neither containment nor a PR
link automatically blocks work. Each record owns its own detailed checklist;
a parent references child outcomes without mirroring child checkboxes/status.

One direction of a hierarchy link is enough; do not require reciprocal lists.
When both sides exist, keep them consistent in the same authorized change.
Check that referenced records exist and relationships contain no duplicates,
self-links, hierarchy cycles, or dependency cycles. Do not create placeholders
or modify an unowned relative merely to fill a field. If a referenced record is
outside authorized scope, report any inconsistency instead of silently editing
it. A parent reaches `complete` only when its agreed scope, including required
child outcomes, is verified complete; hierarchy alone does not define which
outcomes are required.

At task entry reconcile only a selected stale record using actual evidence;
implementation and handoff update that record at meaningful checkpoints.
`repo-commit` applies reviewed local/pre-merge closeout under these lifecycle
rules; `ship` checks requirements due at remote delivery. Set `status: complete` and remove only ready
scope from TODO in the closeout commit once the whole record's scope and required
checks/review at that boundary are satisfied. This does not claim merge or
release, so it needs no post-merge status commit. Keep a partial parent open.
Failed delivery is reported separately from completed work; failed validation or
new scope reopens the record. Never infer merge from a checkbox or `pr` field.

Add `## Human review` only when the slice requires a human decision, visual
check, deployment check, or signoff. Do not copy an empty heading into every
record. Make required and optional review distinct, state when it is due, and
include enough guidance to carry out the check:

```markdown
## Human review

- [ ] **Required before merge:** Confirm the settings flow
  - **How:** Open Settings, change each option, then restart the app.
  - **Look for:** Values persist and labels match the product language.
- [ ] **Optional after deployment:** Check the first production run
  - **How:** Use the normal workflow with a real account.
  - **Look for:** Unexpected errors, confusing copy, or slow responses.
```

Use `Awaiting human review` only when a required item blocks the next closeout
step. The item, not the status, states whether review is due before merge,
before deployment, or after deployment.

## Reviewed pre-merge closeout

Review only the authorized closeout scope. Read-only reviewers can recommend
changes but cannot prune files or close tasks. `repo-commit` performs local
closeout when commits are requested; `ship` composes it when delivery needs local
preparation and checks requirements due at delivery. No generic human-review or
manual adoption step is required. The agent performing closeout:

1. Matches tasks and acceptance criteria to the actual diff and validation.
2. Checks the applicable `Human review` section. Surface outstanding required
   items to the user when the relevant review boundary is reached, including
   readiness for merge, shipping, or deployment. Required items block only the
   closeout step they name. Optional items remain visible without blocking safe
   delivery. Never mark review complete without user confirmation.
3. Inventories associated artifacts and classifies them:
   - **Keep:** useful evidence, research, screenshots, or validation results.
   - **Consolidate:** repeated summaries, handoffs, and overlapping notes.
   - **Resolve:** competing plans or claims no longer true. Preserve significant
     alternatives and rejection reasons in the final decision record.
   - **Promote:** enduring guidance that belongs in maintained project docs.
   - **Propose removal:** scratch output, empty scaffolding, or redundant drafts.
4. Presents proposed file deletions by path and reason, including apparently
   temporary files. Apply only after explicit approval. Deletion is not implied
   by "commit", "ship", or "mark done." Never clean unrelated or concurrently owned work.
5. Updates retained material and navigation. A stale plan's header must say it is
   historical or superseded and link to the final decision/current guidance.
   Clearly distinguish observations at the time from claims about current code.
   For non-text evidence, put provenance and scope in its linked README.
6. Checks for unique rationale, unresolved questions, evidence, and inbound links
   before consolidating. Do not discard unique information without approval.
7. Fixes links after approved changes and preserves original evidence where it
   is useful. If deletion is declined or unanswered, keep the file, label any
   known obsolete guidance, and report pending cleanup instead of blocking safe
   unrelated delivery. Sensitive material remains a shipping blocker.
8. Updates the changelog for notable behavior or workflow changes. Existing
   location and release conventions win; default to root `CHANGELOG.md` only
   when creating one. Do not relocate it into `todo/`.
9. Carries useful purpose, consequential decisions, validation, migration notes,
   and limitations into commit bodies. `ship` uses that evidence for concise PR
   descriptions, not a transcript of the problem-solving process. Do not copy
   the whole checklist.
10. Removes only the ready scope from the priority index in its closeout commit.
    Preserve unfinished parent tasks and unrelated or concurrent work. Retain
    useful work records at their stable paths. Set `status: complete` only for
    verified whole-record completion, not partial parent work or unverified merge.
    Respect legacy formats until an authorized migration.

Pre-merge plans and evidence can be committed as plans and evidence. They must
not present proposed behavior as already delivered product documentation.

## After merge

Branch/worktree cleanup requires a separate authorized workflow. Verify merge
using the host's PR state or Git history as appropriate; squash merges may not
preserve branch commit ancestry. Verify clean state, ownership, and active-agent
status before removing anything. Never delete a sibling or active worktree as a
side effect of task closeout.

A YAML record already marked `complete` needs no ceremonial post-merge commit.
For legacy records still saying Ready for merge, a later verified reconciliation
can identify retained evidence without an unauthorized format migration. Treat
unverified delivery as unknown, not evidence that work is still unmerged. If the work resumes, re-check delivery
and add a new slice to the index rather than executing the old plan blindly.

## Legacy migration

Migration is a deliberate change, not a side effect of adding a task:

1. Inventory root `TODO.md`, `docs/TODO.md`, existing work notes, and their inbound
   links. If more than one queue is live, ask which owns the work.
2. Agree on scope, priorities, and ownership. Old In Progress/Up Next/Backlog
   sections express status or ordering, not P1–P5 urgency. Preserve that context
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
