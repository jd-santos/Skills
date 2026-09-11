---
name: ship
description: >-
  Recovers repository context, reviews local work, creates readable commits,
  chooses an appropriate branch, pushes eligible branches, and creates or
  updates pull requests. Use when the repository state is uncertain, finishing
  development work, preparing branch changes, or when the user says "ship
  this", "commit and push", or "review this branch".
version: 1.1.0
author: jdwork
category: workflow
requires:
  - commit-message-writer
  - changelog-writer
---

# Skill: Ship

## Description

Turn coherent local work into a readable Git history, then deliver it through
the branch and pull request flow that fits the repository. Recover context from
the current session when available and from Git when it is not.

Commits, non-`main` pushes, and pull request creation do not need separate user
confirmation. Always ask before pushing directly to `main`.

## Prerequisites

- A Git repository and `git` on PATH.
- Optional: GitHub CLI (`gh`) for repository metadata and pull requests.
- The `commit-message-writer` and `changelog-writer` skills.

If the companion skills are unavailable, use Scoped Commits in the form
`scope: short imperative description` and Keep a Changelog conventions for
notable changes.

## Instructions

### 1. Inventory the repository

Before changing anything:

1. Load and follow `commit-message-writer` and `changelog-writer`.
2. Find the repository root with `git rev-parse --show-toplevel` and work from
   there.
3. Inspect:
   - `git status --short --branch`, including every untracked path
   - current branch, upstream, remotes, and remote default branch
   - local and remote branches with tracking state
   - `git worktree list --porcelain`
   - recent decorated history across branches and the current branch's
     divergence from its upstream and likely base
   - staged and unstaged diff summaries
   - an existing pull request for the current branch, when `gh` is available
4. If the harness exposes active-agent or task status, inspect status metadata
   for work that may still be running. Do not read another agent's transcript.
5. Use `gh repo view --json isPrivate,defaultBranchRef` when available. In a
   public repository, warn before committing personal identifiers, internal
   URLs, machine-specific private configuration, or work-specific settings.
6. Never read secret-looking files. Treat `.env*`, `*credentials*`,
   `*secrets*`, `*token*`, `*.key`, `*.pem`, private SSH keys, and cloud
   credential files as content-blocked. `.env.schema` and `.env-schema` are
   allowed only when they contain schema information rather than literal
   secrets.

### 2. Establish work ownership and scope

Use the current session as the strongest intent signal:

- After development in the same session, focus on changes related to that work.
  Describe unrelated or unclear changes and offer to commit, leave, or otherwise
  handle them.
- With little session context, inspect all non-sensitive changes and treat every
  coherent, ready change as potentially in scope.
- Always account for staged, unstaged, and untracked work. Do not assume an
  untracked file is disposable or unrelated.

Treat signs of concurrent work as a safety boundary. Dirty sibling worktrees,
very recent commits outside the known session, unexpected file activity, or an
active agent may mean someone else is working in the repository. Use those
signals when choosing scope and branches. If shipping could interfere, stop and
ask the user. Sibling worktrees are inspection-only: do not stage, commit,
stash, reset, switch, or clean them.

### 3. Evaluate the branch situation

Make branch choice a dedicated decision before committing:

1. Identify the current branch, its upstream, the remote default branch,
   divergence, related branches, sibling worktrees, and any existing PR.
2. Infer repository convention from recent history. Few active topic branches
   plus history dominated by direct `main` commits supports a small direct
   commit. Frequent merges or PR branches supports a topic branch.
3. Call out an obviously wrong branch, including work that belongs to an
   existing branch or a branch already checked out in another worktree. Ask
   before moving work when ownership or destination is unclear.
4. On `main`, recommend creating a topic branch when the work is large,
   multi-commit, risky, experimental, or easier to review as a PR, even if the
   repository often commits directly to `main`.
5. Do not switch branches with a dirty worktree unless the move is understood
   and safe. Never guess when remotes, bases, or branch ownership conflict.

### 4. Review and group the work

1. Review targeted diffs for tracked, non-sensitive files. Read files only when
   needed to understand intent.
2. Classify changes as ready, uncertain, unfinished, unrelated, concurrently
   owned, or potentially sensitive.
3. Validate ready work with the narrowest relevant checks. Do not claim checks
   that were not run.
4. Decide whether `CHANGELOG.md` needs an update. Include notable user-facing,
   workflow, compatibility, release, or maintainer-visible changes. Skip tiny
   refactors and formatting-only work unless they matter outside the diff.
5. Group ready work by intent and reviewability, not merely by file path. Each
   commit should leave the repository coherent and make sense when read later
   without this conversation.
6. Handle documentation according to repository state:
   - Commit documentation that accurately describes the code in the same
     commit, or in a focused documentation commit when independently useful.
   - Split current and future-facing documentation by hunk when practical.
   - Leave inseparable future-facing text uncommitted and explain why.
   - Include such text only with explicit approval, with context in the commit
     body about the incoming implementation.
7. Stage only the paths or hunks for one group. Review the staged diff, then
   commit without asking for separate confirmation.
8. Follow `commit-message-writer` exactly. Prefer specific Scoped Commit
   subjects, use a body for motivation or non-obvious context, and split
   unrelated work. Never use vague, WIP, or type-first subjects unless the
   repository requires them.
9. Repeat until all ready groups are committed. Leave unfinished, unclear,
   sensitive, or concurrently owned work untouched and report it.

### 5. Deliver commits

1. Show final status and the commits not yet on the destination remote.
2. If delivery would push directly to `main`, summarize exactly what will be
   pushed and ask for confirmation. Do not push until the user confirms.
3. Push a non-`main` branch without another confirmation. If it has no upstream,
   set one only when the remote and branch mapping are unambiguous. Otherwise,
   ask.
4. When the branch is suitable for a PR and `gh` is authenticated and
   authorized:
   - Use the repository's default branch as the base unless history or an
     existing PR establishes another base.
   - If an existing PR has no new commits, return its link without rewriting it.
   - For new work, derive the title and body from all commits in the PR range,
     not only the latest commit. Summarize the delivered behavior and list
     validation performed.
   - Create the PR when none exists. Update an existing PR when needed, while
     preserving manually written context.
   - Never discard an existing human-written description. If it cannot be
     merged safely, return the proposed updated description as text with the PR
     link.
5. If the PR can be created but its body cannot be populated, create it when
   possible, then return the intended title and body as copyable text with the
   PR link.
6. If permissions or tooling prevent PR creation, report the blocker and return
   the proposed title and body. Include a compare or PR-creation URL when one
   can be derived safely.

### 6. Report the result

Report:

- branch decision and why it fits the repository history
- commits created and pushed
- PR link, or why no PR was created
- checks run and changelog decision
- remaining local, unrelated, uncertain, sensitive, or concurrent work

Keep the summary short. If an existing PR has no additional work and nothing
else needs attention, returning the PR link is enough.

## Error Handling

- **Not a Git repository**: Stop and say the skill requires one.
- **Concurrent or ambiguous ownership**: Do not alter the questionable work.
  Summarize the evidence and ask the user.
- **Wrong or ambiguous branch**: Stop before committing or moving work and ask.
- **Git command failure**: Show the command and error. Do not retry with a more
  destructive strategy without approval.
- **Potential secret**: Stop handling that file's contents and report its path.
- **Dirty worktree after shipping**: Explain what remains and why.
- **PR body failure**: Keep the PR, return its link, and provide the intended
  description as copyable text.

## Example

**User:** "Ship whatever is ready here."

1. Recover branch, history, worktree, PR, and repository context.
2. Use session history to separate current work from unrelated changes, or
   review all coherent work when session context is sparse.
3. Pause if a sibling worktree or recent external activity suggests concurrent
   ownership.
4. Choose the current branch, recommend a topic branch, or ask about an
   obviously wrong destination.
5. Create focused Scoped Commits and leave unfinished work alone.
6. Push a non-`main` branch and create or update its PR when authorized. Ask
   before a direct push to `main`.
