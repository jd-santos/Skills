# Task workbench

Status: Ready for merge. Implementation and validation complete. Check Git and
PR history for delivery state; this record does not assert merge or release.
Scope: Workflow skills in this repository and matching Pi instructions, handoff
advisory wording, and regression tests in the parent Dotfiles repository.

## Goal

Separate the live priority queue, working material, and development history.
Give parallel agents independent work records without turning Markdown into a
homegrown task service. Keep useful evidence while removing misleading guidance
and duplicate agent output through reviewed cleanup.

## Agreed design

- Use root-level `todo/README.md`, `todo/TODO.md`, and `todo/DONE.md`.
- Use P0: Rush, P1: Essential, P2: High, P3: Low, and P4: Minor headings.
- Keep small task checklists in TODO. Delegate larger execution checklists to
  stable `todo/work/<descriptive-name>/README.md` paths, linked from TODO.
- Create supporting plans, research, evidence, and asset directories only when
  useful. Do not duplicate checklists or move folders when status changes.
- Treat ownership notes as coordination hints, not locks across worktrees.
- Check completed work in place. Remove only the ready scope from the live
  queue during reviewed pre-merge closeout, preserving unfinished work.
- Use Git and PRs for development history, `CHANGELOG.md` for maintained release
  notes, and retained work records for scoped historical evidence.
- Make DONE a navigation page, not a growing task ledger. Optional major release
  highlights link to the changelog rather than copying it.
- Propose file deletions for approval. Consolidate competing plans into final
  decisions and label retained evidence with its historical scope.
- Keep post-merge branch and worktree housekeeping separate from tracked-file
  cleanup. Do not invent a branch-deletion workflow in this change.

## Alternatives not selected

- A central detailed checklist increases conflicts between concurrent agents.
- A generated task index adds schemas and tooling before they are needed.
- Moving folders between active and archived directories causes link and merge
  churn. Stable paths plus explicit status are sufficient for this workflow.
- A Done task ledger duplicates Git history and adds recurring bookkeeping.

## Execution checklist

- [x] Rewrite todo-manager with lifecycle, navigation, concurrency, and migration rules.
- [x] Connect planning, ship, commit, and changelog skills without duplicate ownership.
- [x] Align project-issue-note with workbench conventions where one exists.
- [x] Update Pi instructions, planning prompt, and handoff advisory, plus their reference docs.
- [x] Adopt the workbench in this Skills repository and update its README and changelog.
- [x] Validate links, metadata, consistency, and representative workflow scenarios.

## Acceptance criteria

- New projects get one P0–P4 priority index and no Done task section.
- Legacy locations are discovered without silently creating a second queue.
- Parallel agents primarily edit separate work records; shared edits and
  overlapping ownership require reconciliation.
- Partial shipping cannot close unfinished tasks or treat a checkbox as proof
  of validation, delivery, or merge.
- Active plans have one authoritative version. Historical evidence is clearly
  scoped and is not loaded wholesale as current instructions.
- Release notes remain in the existing changelog location. DONE is optional
  navigation and selected highlights, not a second changelog.
- No automatic pruning, branch deletion, external API automation, or new runtime
  dependencies are introduced.

## Cleanup defaults

- DONE uses links, with optional selected major-release highlights.
- File deletions require explicit approval, including apparent scratch files.

## Validation

- `git diff --check` passed in Skills and Dotfiles during implementation and
  shipping preflight.
- A read-only Node check passed for 18 Markdown files, six skill manifests and
  prompt frontmatter, 44 local links, priority heading order, the legacy
  redirect, and the absence of a task ledger in DONE. This was a one-off static
  check, not a new project dependency or behavioral agent test suite.
- The existing installed skill and Pi instruction paths resolve to the edited
  tracked files. Reload Pi to refresh the loaded prompt and context resources.
- `node --test pi/.pi/agent/extensions/tests/context-planner.test.mjs` passed
  all four tests in Dotfiles: threshold boundaries, handoff wording and write
  restrictions, unavailable telemetry, and message preservation/session reset.
- A fresh read-only reviewer checked migration, parallel ownership, partial
  delivery, failure recovery, cleanup approval, stale plans, standalone notes,
  and history ownership. Its saved-versus-committed-plan ambiguity was corrected.
  Shipping discovery was also clarified for a clean checkout after a failed push.
- Active LSP checks found the new test clean. The advisory module has four
  inferred-project warnings: an unresolved globally installed Pi type import
  and three resulting implicit-any callback parameters. Its runtime test passes;
  authoritative project-wide type checking was not established in this change.

## Shipping notes

This change spans the Skills submodule and its parent Dotfiles checkout. Publish
the Skills scope first, then pin that reviewed revision with the matching Pi
changes. Merge the Skills PR before the Dotfiles PR. If the Skills merge rewrites
commits, refresh the parent pin to the resulting main-branch revision before
merging Dotfiles. Unrelated local work is outside this change's scope.

The former `docs/TODO.md` is a redirect, not a live queue. Its two completed UI
design entries were already committed and remain recoverable with
`git log -p -- docs/TODO.md`. No artifact files were deleted. The parent
Dotfiles task queue was not migrated.
