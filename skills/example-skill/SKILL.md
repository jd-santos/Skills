---
name: example-skill
description: Shows a small, complete agent skill as a reference for structure and style. Use when learning how skills are put together, viewing an example skill, or starting a new skill from a working sample.
metadata:
  version: "2.0.0"
  author: jdwork
  category: meta
---

# Example Skill

This file is a sample, not a workflow to follow. The skill below,
`release-notes-from-tags`, shows the patterns `create-skill` recommends. Use
`create-skill` for the full guidance.

Save real skills under `~/.agents/skills/<name>/SKILL.md` or
`<repo-root>/.agents/skills/<name>/SKILL.md`, never `.claude/skills/`.

## The sample

````markdown
---
name: release-notes-from-tags
description: Drafts release notes from the git commits between two tags, grouped by scope. Use when preparing a release, summarizing changes since the last tag, or when user says "write release notes" or "what changed since v1.2".
metadata:
  version: "1.0.0"
  category: documentation
  requires: core-writing
---

# Release Notes from Tags

Apply `core-writing` to the final prose.

## Workflow

1. Find the range. Use the tags the user names; otherwise run
   `git describe --tags --abbrev=0` for the latest tag and compare it to `HEAD`.
2. List commits with `git log --no-merges --format='%h %s' <from>..<to>`.
3. Group by the scope before the colon (`nvim: ...`, `tmux: ...`). Put commits
   without a scope under "Other".
4. Rewrite each group as user-facing changes. Drop refactors, formatting, and
   CI-only commits unless they change behavior; readers care about effects,
   not churn.
5. Show the draft. Do not create a tag or a GitHub release unless asked,
   because both are visible to others and awkward to undo.

## Notes

- Squash-merged repos have one commit per PR; use the PR title as the entry.
- If the range is empty, say so instead of inventing entries.
````

## What it demonstrates

- **Description:** third person, verb first, then a `Use when...` clause with
  real user phrases.
- **Metadata:** custom keys sit under `metadata`, so the skill passes the Agent
  Skills spec. `requires` is a note for humans; the body line "Apply
  `core-writing`" is what gets the other skill used.
- **Body:** no boilerplate sections. Exact commands where a wrong flag gives a
  wrong answer, and judgment where judgment fits.
- **Reasons, not caps:** steps 4 and 5 say why instead of shouting `NEVER`.
- **Notes:** only the gotchas an agent would otherwise hit.
