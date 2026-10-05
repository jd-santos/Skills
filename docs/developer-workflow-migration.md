# Adopt the developer workflow in an existing project

Adopt the [developer workflow](../README.md#development-workflow) when touching a
project, not through a collection-wide migration campaign. Installing skills
changes available capabilities; it does not authorize changes to every project's
instructions, tracker, or artifacts. A targeted migration needs its own scope.

No manual adoption trial or temporary migration skill is required. The existing
`todo-manager` preservation rules cover record changes; this guide maps workflow
responsibilities. If repeated migrations reveal a distinct procedure that earns
a skill, extract it then rather than creating another owner now.

## Map the old responsibilities

| Old instruction or capability | Current destination |
| --- | --- |
| `planning-first`, mandatory rounds, or separate save/build approvals | `work-routing` chooses useful capabilities; clear authorized work proceeds directly. |
| `to-spec` or a mandatory separate spec | `work-contract` synthesizes behavior in the existing work record. A separate document is optional when independently useful. |
| `project-issue-note` or a competing note schema | `todo-manager` discovers/creates the authoritative record in the established tracker. |
| Monolithic `ship` for review, staging, and local commits | `repo-commit`, with read-only inspection and explicitly authorized local mutation. |
| Monolithic `ship` for pushes and PRs | `ship`, invoked for requested delivery and composed with `repo-commit` when preparation is needed. |
| Automatically grilling all substantial work | Ordinary consequential clarification. Explicit grilling invokes the full decision-space interview. |
| Progress logs, mirrored specs/checklists, or Done task ledgers | One current agreement/checklist, retained useful evidence, and Git/PR/changelog history. Consolidation needs authorization; do not delete merely to match a template. |

## Apply a bounded migration

Use only the steps relevant to the agreed scope. An instruction-only update
needs no work-record reconciliation or tracker migration.

1. **Inventory read-only and proportionally.** Identify the real repository root,
   active instructions, installed skill sources, and ownership of the files to
   change. Check local state and concurrency risk before edits. Inspect the
   tracker, selected work record, and inbound links only when that material is
   being migrated or resumed. Do not read secret-looking artifacts or another
   agent's transcript. A stale catalog in a long-running session is not evidence
   of a broken install.
2. **Agree on scope.** Distinguish adopting current routing/commit/delivery rules
   from migrating tracker paths, record formats, or artifacts. A project can use
   the workflow while retaining its existing tracker and legacy plaintext notes.
   If multiple queues are live, ask which is authoritative. Do not create a second
   queue or treat adoption permission as deletion or shipping permission.
3. **Install the companions if authorized.** Use the [README installation
   options](../README.md#install). Grilling stays optional; keep its reviewed
   source and attribution. Reload the host or start a new session after changes
   when needed. Do not require a cross-host certification exercise to start work.
4. **Update active instructions only.** Replace obsolete skill references and
   mandatory planning gates with current responsibilities. Distinguish a local
   commit request from remote delivery and an ordinary question from explicit
   grilling. Preserve project safety/review requirements. Keep historical plans
   and PR evidence as history, not executable guidance; label/link superseded
   material when necessary. Do not rewrite every historical occurrence of an old
   name or install compatibility wrappers.
5. **Reconcile in-flight work only when selected.** If adoption also resumes or
   migrates an existing work item, compare its current agreement, checked steps,
   actual code/tests, and verified Git/PR evidence. Skip this for instruction-only
   updates. Keep confirmed decisions and
   unresolved questions distinct. Reuse the existing record; do not invent new
   acceptance criteria, promote guessed work to complete, or infer whole-record
   completion from a merged PR. Put the sole current execution checklist in the
   established task source, preserving useful linked evidence and unknown
   non-sensitive metadata. Moving material or changing its schema requires
   authorization; link existing documents when preservation is sufficient.
6. **Check touched instructions and links.** Repair navigation only when it is
   affected. For an authorized tracker migration, follow `todo-manager`'s
   [legacy migration rules](../skills/todo-manager/references/workbench.md#legacy-migration):
   preserve unchecked work and checked state, fix affected links, and avoid
   conflicting live queues. Check metadata only when changed. Report unresolved
   ownership or delivery evidence rather than guessing.
7. **Resume ordinary work.** Report the result briefly in chat. If a work record
   was already needed for the migration or resumed effort, update it with useful
   results and blockers; do not create a record or adoption journal just for an
   instruction update. Existing `repo-commit` and `ship` handle local commits and
   delivery only when requested. Expand the migration to another project or
   record only with authorization.

## Example: a merged feature inside an unfinished effort

An old record says “Ready for merge,” its feature PR is merged, and recovery
validation plus a migration tool are still unchecked. Verify the PR and the
feature behavior, but keep the parent open and the remaining work visible. Do
not mark the whole effort complete, discard its plan, or rerun delivered work.
The record can keep its legacy format while its active instructions adopt the
current workflow.

## When a temporary skill would help

A temporary migration skill would be worthwhile only if several authorized
projects need the same repeatable transformation that this guide and task
management do not cover. Give it a bounded target and retirement condition,
reuse task-management lifecycle rules, and avoid another tracker or universal
approval ceremony. Until that need appears, use this guide and the existing
owners.
