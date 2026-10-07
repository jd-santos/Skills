# Todo workbench

This directory uses the
[`todo-manager`](https://github.com/jd-santos/Skills/tree/main/skills/todo-manager)
workflow from [jd-santos/Skills](https://github.com/jd-santos/Skills). It gives
unfinished work a small, readable home without turning Markdown into a second
issue tracker.

The workflow separates three things that are easy to mix together:

- the work that needs attention now,
- the plans and evidence needed to finish larger efforts,
- the history of work that has already shipped.

That separation keeps the live list useful while preserving context worth
returning to later.

## How it is organized

- [TODO](TODO.md) is the live priority list. Small tasks can stay there as
  checklists. Larger tasks link to their own folder under [`work/`](work/).
- [`work/`](work/) contains the record for substantial work. Each folder starts
  with a creation-order number and a descriptive name, such as
  `006-agent-workflow-integration`. Its README covers the goal, status,
  checklist, and relevant supporting material. Work that fits in a couple of
  sentences, especially a loose future idea, stays as a checkbox in TODO.
- [DONE](DONE.md) points to completed work in Git, merged pull requests, the
  changelog, and retained work records. It is a map to history, not a second
  task list.

This follows the core idea of the todo-manager skill: keep one short priority
index, give substantial work a stable home, and let Git tell the finished story.

## Work records

- [Task workbench](work/001-task-workbench/README.md)
- [Learner-aware development guidance](work/002-i-am-baby/README.md)
- [Writing skill system](work/003-writing-skill-system/README.md)
- [Composable design skill family](work/004-design-skill-family/README.md)
- [Tracked-skill registration command](work/005-tracked-skills-add/README.md)
- [Planning and execution workflow](work/006-agent-workflow-integration/README.md)
- [Developer workflow refinements](work/007-developer-workflow-refinements/README.md)

Each work record owns its status; this map does not mirror it. New or explicitly
migrated records use YAML `status` with optional `pr`, `blocked_by`, `parent`,
`child`, and `tags`. Existing plaintext status remains valid until migration is authorized.
Hierarchy is optional and does not imply dependencies. Do not move folders when
status changes.

## Priorities

Tasks use five priority levels:

1. **P1: Rush** for work that needs immediate attention.
2. **P2: High** for important work that should happen next.
3. **P3: Essential** for required work without immediate urgency.
4. **P4: Low** for useful work that can wait.
5. **P5: Minor** for small improvements and optional polish.

Priority describes urgency, not progress. The task or its work README records
whether it is planned, active, blocked, ready for review, or ready to ship.

## Using the workbench

Add a short task directly to TODO. If the work needs a detailed checklist or
supporting files, create `work/<NNN-descriptive-name>/README.md` using the next
unused creation-order number and link it from the TODO entry. Keep each number
stable across priority or status changes and never reuse a gap. Keep one detailed
checklist so progress does not drift between files.

The work README holds the full contract and decisions by default. Add linked,
subject-named detail only for independently useful reading or evidence, or an
explicit request; length alone does not require a plan or spec.

During reviewed local/pre-merge closeout, `repo-commit` removes only ready scope
from the live list using task-management rules; `ship` checks requirements due at
remote delivery.
A YAML record may become `complete` when its whole scope and required checks are
verified; that does not claim its PR merged. Partial parents stay open, and no
post-merge status-only commit is needed. Keep work records that explain
important decisions or preserve useful evidence. Git and pull requests remain
the source of truth for what changed, while the [changelog](../CHANGELOG.md)
records notable releases and user-visible changes.

The [local todo-manager skill](../skills/todo-manager/SKILL.md) contains the full
workflow. The [task-workbench record](work/001-task-workbench/README.md) explains how
this particular workbench was introduced.
