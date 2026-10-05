# Writing skill system

Status: Ready for review.
Scope: A compact baseline writing skill, a focused technical-writing extension, skill discovery, and Pi agent guidance.

## Purpose

Extract JD's general prose style into a small `core-writing` skill that applies to copyable text across contexts. Keep `technical-writing` focused on technical accuracy, useful structure, and operational detail.

## Agreed design

- Add `core-writing` as the baseline for all prose and copyable text.
- Keep the core concise enough to load frequently.
- Rename `technical-writing-style` to `technical-writing` and make it depend on `core-writing`.
- Use references to help agents select another communication or format-specific skill without embedding those skills.
- Add a Communication group to the skills README for `core-writing` and `technical-writing`.
- Make `commit-message-writer` and `changelog-writer` depend on the core while keeping them under Workflows.
- Keep other operational skills categorized by their workflow purpose.
- Update Pi's standing prose guidance to use the new skill names.

## Acceptance criteria

- `core-writing` defines the shared voice, editing principles, and restrained formatting rules in roughly 30–50 lines.
- `technical-writing` contains only technical-writing guidance and declares its dependency on `core-writing`.
- Skill descriptions support reliable selection for general prose and technical content.
- The README has a Communication group without moving operational workflow skills.
- Maintained instructions contain no stale `technical-writing-style` references.
- The requested follow-up communication skills are recorded in the task index.
- Unrelated work remains untouched.

## Work

- [x] Add `core-writing`.
- [x] Rename and narrow `technical-writing`.
- [x] Update skill discovery and Pi agent guidance.
- [x] Record future communication skills.
- [x] Validate frontmatter, links, references, and Markdown.

## Decisions

Use a dependency-based composition model. Specialized skills add format or
domain rules to `core-writing`; they do not copy the baseline or become nested
subskills. Keep operational skills categorized by their workflow purpose rather
than by the fact that they produce text.

## Validation

- A focused Python check passed for required frontmatter, README links,
  dependency declarations, the renamed directory, and stale README references.
- `git diff --check` passed in both the Skills repository and the parent
  Dotfiles repository.
- Active diagnostics reported no findings across the eight changed Markdown
  files.
- A fresh read-only reviewer confirmed the skill boundaries, dependencies,
  README grouping, follow-up tasks, and Pi guidance with no findings.
- The unrelated existing change in
  `skills/marimo-pair/scripts/execute-code.sh` was not modified as part of this
  work.
