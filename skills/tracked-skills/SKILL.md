---
name: tracked-skills
description: Installs, verifies, and reviews updates for external agent skills pinned in tracked-skills.json. Use when hydrating a Skills checkout, checking external skill integrity, reviewing upstream changes, or changing an external skill pin.
version: 2.0.0
author: jd-santos
category: workflow
---

# Skill: Tracked Skills

## Description

Manage external skills registered in `../../tracked-skills.json`. The registry
pins exact reviewed commits while the installer generates ignored local copies
under `../../skills/`. Upstream skill text is not committed to this repository.

## Instructions

### 1. Read the registry and workflow

Before changing external skills:

1. Read `../../tracked-skills.json`.
2. Read `../../docs/tracked-skills.md`.
3. Confirm the source project, author, license, commit, and source path.
4. Do not replace a local skill directory without reviewing the installer's
   warning.

### 2. Install pinned skills

From this repository, run:

```bash
./scripts/tracked-skills install
./scripts/tracked-skills verify
```

Install or verify selected entries by passing their names after the command.
Installation uses the exact commits recorded in the registry.

### 3. Review updates

Run:

```bash
./scripts/tracked-skills update
```

Review the commit log, diff summary, and full patch before approving a new pin.
After approval:

1. Inspect the changed `tracked-skills.json`.
2. Run `./scripts/tracked-skills verify`.
3. Confirm `git status` contains no generated skill content.
4. Commit only the registry and intentional documentation changes.

### 4. Add a source

Version 0.1 uses explicit registry edits rather than an interactive add command.
Follow the checklist in `../../docs/tracked-skills.md`, including visible README
attribution and a matching `.gitignore` entry.

## Safety

- Never install an unpinned branch tip.
- Never treat generated external skill text as repository-owned content.
- Preserve upstream source, author, and license information.
- Refuse unexpected source paths, symbolic links, unmanaged destinations, and
  locally modified generated copies.
- Use `--force` only after the user approves replacing the destination.

## References

- Workflow: `../../docs/tracked-skills.md`
- Registry: `../../tracked-skills.json`
- Utility: `../../scripts/tracked-skills`
