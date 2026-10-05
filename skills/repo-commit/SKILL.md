---
name: repo-commit
description: Reviews staged, unstaged, and untracked repository work and commits ready changes when authorized. Use when the repository state is uncertain, reviewing local work or a branch, or when the user says "commit this" or "commit whatever is ready". Does not push or create pull requests.
version: 1.0.0
category: workflow
requires:
  - commit-message-writer
  - changelog-writer
  - todo-manager
---

# Skill: Repo Commit

## Description

Recover repository context, review local work, and turn ready changes into readable local commits. Inspection and review requests stay read-only. A request to stage or commit authorizes only that local operation and its necessary preparation, not remote delivery.

Use `ship` for explicitly requested pushes and PRs. Finishing implementation does not automatically invoke either skill. Once local commits are requested, individual commits need no separate confirmation, subject to ordinary tool permissions and repository safeguards.

## Prerequisites

- A Git repository and `git` on PATH.
- Optional: GitHub CLI (`gh`) for repository and PR metadata.
- `commit-message-writer`, `changelog-writer`, and `todo-manager`.

Load the companions. If prose skills are unavailable, use Scoped Commits (`scope: short imperative description`) and Keep a Changelog conventions. If `todo-manager` is unavailable, report task closeout as pending rather than inventing migration or pruning rules.

## Instructions

### 1. Inventory without changing anything

1. Find the root with `git rev-parse --show-toplevel`. Do not mistake a parent repository for the selected submodule or package.
2. Inspect `git status --short --branch`, including every untracked path; staged and unstaged diff summaries; branch/upstream/remotes; remote default branch; local and remote tracking state; recent decorated history and divergence; and `git worktree list --porcelain`. Inspect an existing PR when relevant and tooling is available.
3. Read the established task index and relevant work records through `todo-manager`. Follow work-record links or trailers in the commits under review; do not load the whole archive or create a workbench just to commit.
4. Respect concurrent work. Use available lifecycle notices or status metadata without polling active agents or reading their transcripts. Dirty sibling worktrees, unexpected recent commits, or active writers require scope/ownership checks. Sibling worktrees are inspection-only: do not stage, commit, stash, reset, switch, or clean them.
5. Before committing, verify public/private status with `gh repo view --json isPrivate,defaultBranchRef` when available. Follow public-repository restrictions; warn before including potentially private identifiers, internal URLs, or machine/work-specific configuration. If visibility cannot be verified, treat it as unknown, not permission to expose private data.
6. Never read secret-looking files, including `.env*`, `*credentials*`, `*secrets*`, `*token*`, `*.key`, `*.pem`, private SSH keys, or cloud credential files. Only `.env.schema` and `.env-schema` are exceptions when they contain schema information, not literal secrets. Stop handling a file if literal secrets appear in an allowed schema.

### 2. Establish intent, ownership, and branch

Use the session as the strongest intent signal. After development, focus on related work and identify unrelated or unclear changes. With little session context, review all non-sensitive changes as potentially relevant, not automatically authorized to commit. Account for staged, unstaged, and untracked work; an untracked file is not disposable.

Classify each change as ready, unfinished, uncertain, unrelated, concurrently owned, or potentially sensitive. Ask when scope or ownership remains ambiguous. Do not take over another agent's work or assume the existing index is yours to replace.

Before any authorized commit:

- Identify upstream, default branch, likely base, divergence, related branches, worktrees, and existing PRs.
- Infer branch conventions from recent history. Recommend a topic branch for substantial, risky, experimental, or multi-commit work even when small changes normally go directly to the default branch.
- Handle a detached checkout or an obviously wrong branch deliberately. Ask before moving work when destination or ownership is unclear. Never switch a dirty checkout unless the move is understood and safe.
- For review-only requests, report the branch recommendation without creating or switching branches.

### 3. Validate and group ready work

1. Read targeted diffs and source needed to understand intent. Group ready changes by outcome and reviewability, not just file path. Each group must leave the repository coherent.
2. Run the narrowest relevant checks and follow actual project review requirements. Report checks not run and limitations honestly. Do not introduce a generic required human-review step.
3. Use `changelog-writer` for notable user-facing, workflow, compatibility, or maintainer-visible changes. Skip formatting-only or tiny internal changes unless they matter outside the diff.
4. Include accurate current documentation with the corresponding work. Split future-facing text by hunk when practical; leave inseparable unapproved future claims untouched. Clearly labeled plans and historical evidence may be committed as such, not as delivered behavior.
5. Review-only requests stop with findings, proposed groups, checks, and remaining uncertainty. Do not edit documentation, close tasks, stage, or commit merely because work looks ready.

### 4. Prepare closeout and commit only when authorized

Use `todo-manager` and its [workbench reference](../todo-manager/references/workbench.md) for lifecycle and artifact rules. This skill applies local closeout; `ship` checks remote delivery requirements. Do not define a second task schema.

- Match checked outcomes to the actual diff, acceptance criteria, and validation. Keep unfinished steps and partially complete parents open. Required review blocks only its stated boundary; optional review does not block safe work. Never claim human signoff without confirmation.
- Retain useful evidence, resolve obsolete guidance, and promote enduring docs when in scope. Propose file deletions by path and reason and wait for explicit approval. A commit request is not pruning permission. If optional cleanup is declined or unanswered, retain and label known stale guidance rather than blocking otherwise safe commits.
- In the reviewed closeout commit, remove only verified ready scope from the index. Set a YAML record to `status: complete` only when its whole agreed scope and required checks at this boundary are satisfied. This pre-merge closeout records work completion, not merge or release. Keep partial parents open; preserve legacy formats until migration is authorized.
- Keep the changelog as the release record and DONE as navigation, not another completed-task ledger.

Stage only paths or hunks for the authorized group, including applicable documentation and closeout. Inspect the full staged diff before committing; do not sweep unrelated pre-staged work into the commit. Preserve its staged state, asking before rearranging the index when selective staging cannot safely isolate the group. A stage-only request stops before committing. A commit request uses `commit-message-writer` and proceeds without a separate confirmation for each group.

Repeat for ready groups within the requested scope. Leave unfinished, unclear, sensitive, and concurrently owned work untouched. Never push, create or update PRs, merge, or release from this skill. Hand off to `ship` only when delivery is requested.

### 5. Report local results

Report findings or created commits, branch choice, checks and limitations, closeout, retained evidence, and remaining changes. Verify final status. Local commits are not delivery evidence. If commits fail, preserve verified work and report the failure; failed validation or new scope reopens affected work. Post-merge branch/worktree cleanup is separately authorized, not a side effect of closeout.

## Error handling

- Not a Git repository: stop and identify the required repository.
- Ambiguous ownership, destination, or conflicts: stop changes to affected scope and ask.
- Potential secret: stop handling the contents and report the path, not the value.
- Git command failure: report the command/error; do not retry using a more destructive strategy without approval.
- Tool permission denial: stop the blocked operation; do not bypass the gate through another tool.

## Examples

- **"Review this branch":** inspect committed and local changes, run safe checks, and report findings. Do not stage, commit, or push.
- **"Commit whatever is ready":** inspect all local states, separate ready groups, validate, choose the right branch, and create local commits. Leave unrelated or unfinished work untouched and do not push.
- **"Stage this fix":** validate and stage the requested fix, preserving unrelated index entries. Do not commit or deliver.
