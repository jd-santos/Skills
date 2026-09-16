# Skills workbench

[TODO](TODO.md) is the live priority queue, mostly for agents.
[DONE](DONE.md) points to development history and retained evidence.

## How to work here

- Use P0: Rush, P1: Essential, P2: High, P3: Low, and P4: Minor. Priority is not
  execution status. Unspecified priority defaults provisionally to P3.
- Keep small checklists in TODO. Substantial efforts link to a stable work
  README under `work/<descriptive-name>/`, which owns the detailed checklist.
- Create supporting files only when needed. Name them for their purpose and
  link them from their work README; do not build empty folder hierarchies.
- Read the relevant work README before its supporting files. Retained plans and
  evidence explain past work, not necessarily the current implementation.
- Agree on bounded ownership before starting. Concurrent writers use separate
  worktrees and mostly edit their own records. The coordinator or integrator
  reconciles shared TODO edits. Ownership notes are not locks.
- Check completed steps in place. Shipping removes only ready scope from the
  queue in its closeout commit, without creating a Done task ledger.
- Keep useful evidence, resolve obsolete guidance, and propose file deletions
  for approval before merge. Branch/worktree housekeeping is separate.

## Map

- [Workbench implementation](work/task-workbench/README.md): design, checklist,
  and validation for these workflow changes.
- [Task workbench skill](../skills/todo-manager/SKILL.md): portable workflow rules.
- [Changelog](../CHANGELOG.md): notable changes and release notes.
- [Maintained project docs](../docs/): reference material, not the default place
  for working plans.

This directory belongs to the Skills repository, which can be checked out as a
Dotfiles submodule. The parent repository has its own task queue; do not merge
the two or migrate the parent's tasks as a side effect of work here.
