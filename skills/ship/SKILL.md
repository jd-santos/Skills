---
name: ship
description: Delivers committed work through pushes and pull requests, using repo-commit for outstanding local changes. Use when the user explicitly asks to ship, push, open a PR, or commit and push. Inspection, branch review, and local commit requests do not authorize delivery.
version: 2.0.0
author: jdwork
category: workflow
requires:
  - repo-commit
  - todo-manager
  - core-writing
  - technical-writing
---

# Skill: Ship

## Description

Deliver requested work to the right remote branch and create or update its pull request. Use `repo-commit` for local preparation, not a second inventory and commit procedure here. An already-committed branch can be shipped without new commits.

Invoke delivery only when requested. A review or local commit request stays within that scope. Within an authorized shipping request, eligible topic-branch pushes and PR creation need no separate confirmation. Always ask before pushing directly to `main` or another remote default branch. Shipping does not authorize merge, release, deployment, deletion, or post-merge branch/worktree cleanup.

## Prerequisites

- A Git repository and `git` on PATH.
- `repo-commit` and `todo-manager` for local review and closeout.
- Optional: authenticated GitHub CLI (`gh`) for PR delivery.
- `core-writing` and `technical-writing` for PR prose.

If `repo-commit` is unavailable, name the gap and do not substitute a local commit procedure silently. If `todo-manager` is unavailable, report closeout as pending; do not invent migration or pruning rules. Report missing PR tooling and provide copyable PR text when needed.

## Instructions

### 1. Establish delivery scope and prepare local work

1. Confirm the requested operation: push, PR creation/update, or full shipping. A push-only request does not authorize PR creation; a PR-only request does not authorize unrelated local commits. Follow explicit branch, base, remote, and scope constraints.
2. Load `repo-commit` and apply its read-only inventory and review to establish repository root, work ownership, branch history, tracking, local state, public/private status, and relevant task records. Follow its secret-file and concurrent-work safeguards, including inspection-only sibling worktrees.
3. For a full shipping or commit-and-push request, use `repo-commit` to validate and commit relevant ready local groups. Leave unclear, unrelated, unfinished, sensitive, or concurrently owned work untouched. Local commit permission comes from this delivery request, not from loading a skill.
4. For already-committed work, review the actual destination range and validation evidence rather than assuming a clean checkout proves readiness. Recover relevant work-record links/trailers even if an earlier local closeout removed the TODO entry. Do not manufacture an empty commit or recreate a task to deliver it.
5. Check required review or deployment gates due at the requested delivery boundary using `todo-manager`. Surface outstanding requirements; never manufacture signoff. Generic manual adoption review is not a prerequisite. If task evidence needs an authorized correction commit, use `repo-commit`; if committing is excluded, report the pending correction instead.

### 2. Verify destination and push only requested work

1. Identify branch, upstream, remote default branch, divergence, related worktrees, and existing PR. Use `repo-commit`'s branch decision rules if local preparation needs a branch change. Never guess when branch ownership, base, or remotes conflict.
2. Show the commits to be delivered and final local status. Account for all commits in the push range, not just those created in this session. Stop if the range includes unapproved or uncertain work, diverges unexpectedly, or belongs to another writer. Ask when the request does not settle scope.
3. For a direct push to `main` or the remote default branch, summarize exactly what will be pushed and wait for confirmation. Otherwise push the authorized topic branch without another confirmation. Set an upstream only when remote/branch mapping is unambiguous. Never force-push, rewrite shared history, or delete a remote branch without explicit authorization.
4. For a PR-only request on a branch not published remotely, explain that a push is needed and ask before performing it. A full shipping request already includes the necessary topic-branch push.
5. On push failure, preserve local commits and verified work completion and report pending delivery. Do not manufacture merge or release evidence or reopen complete work solely because delivery failed.

### 3. Create or update the requested PR

Use the repository's default branch as the base unless the request, history, or an existing PR establishes another base. Check the full PR range, including any stacked-branch changes, before describing its scope.

- If an existing PR has no new work, return its link without rewriting it, unless the user specifically requests a description update.
- For new work, derive title/body from the entire PR range. Summarize what changed, why it matters, validation actually performed, and useful limitations. Keep implementation history and problem-solving detours out unless they explain a consequential tradeoff for reviewers.
- Use relevant work records as intent and supporting evidence, verified against the diff. Link useful retained detail rather than pasting the task checklist. Do not equate a checked box, `status: complete`, or a successful push with merge or release.
- Preserve human-written context when updating a PR. If the description cannot be merged safely, return proposed copyable text with the PR link rather than discarding it.
- If PR creation succeeds but its body cannot be populated, keep the PR and return the intended text. If tooling or permissions prevent creation, report the blocker and provide a compare/creation URL when safely derivable.

### 4. Report delivery

Report commits pushed, PR link or creation blocker, validation/limitations, and remaining local or unrelated work. Keep it short; an unchanged PR with nothing else needing attention can be reported by link alone.

Merge and post-merge cleanup require separate authorization. Verify merge through host state or Git evidence when later requested; squash merges may not preserve commit ancestry. No ceremonial status-only commit is needed to record a merge. Reconcile selected stale records only when needed, using task-management rules.

## Error handling

- Missing repository, ambiguous ownership/destination, or unexpected divergence: stop affected delivery and ask.
- Potential secret or private data in the delivery range: do not read blocked files or publish the data; report the path and safety issue.
- Git command or tool permission failure: report it; do not bypass the gate or retry with a more destructive strategy.
- Missing GitHub tooling: report whether pushing succeeded and return proposed PR text separately.
- Dirty worktree after delivery: identify what remains without implying it was delivered.

## Examples

- **"Ship whatever is ready":** compose `repo-commit` for relevant ready work, push the eligible topic branch, and create/update its PR. Ask before direct default-branch pushes.
- **"Open a PR for these committed changes":** review the full branch range and published state, then create the PR. Ask before a necessary push if it was not authorized.
- **"Push these commits":** check the destination and range, then push only. Do not open a PR or commit unrelated local work.
- **"Review this branch":** use `repo-commit` in read-only mode, not delivery.
