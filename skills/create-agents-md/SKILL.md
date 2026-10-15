---
name: create-agents-md
description: Creates, audits, and slims AGENTS.md files that give coding agents the project context they cannot infer from the code. Use when setting up a repo for AI agents, when an AGENTS.md or CLAUDE.md has grown long or stale, when agents repeat the same mistake in a repo, or when user says "create an AGENTS.md" or "set up agent context".
metadata:
  version: "2.0.0"
  author: jdwork
  category: documentation
---

# Create AGENTS.md

`AGENTS.md` loads into every agent session in the repo, so every line costs
tokens and attention on every task. Keep it to what an agent cannot discover
quickly and would otherwise get wrong.

The evidence supports a short file. In a 2026 study (Gloaguen et al.),
LLM-generated context files did not improve task success and raised cost by
about 20%. Developer-written files helped slightly, and repository overviews did
not help agents find files faster. Write the file by hand, or heavily prune a
generated draft.

## 1. Inspect before writing

- Read the build, test, and lint setup (`package.json`, `Makefile`,
  `pyproject.toml`, CI workflows) to find the real commands.
- Read `README.md` and existing docs so you can point to them instead of
  copying them.
- Look for an existing `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, or
  `.github/copilot-instructions.md`. Consolidate rather than adding another file.
- Ask the user which mistakes agents keep making here. Those are the best lines.

## 2. Include only what earns its place

For each line, ask: *would removing this cause an agent to make a mistake?*

**Include:**
- Commands an agent cannot guess, with exact flags (for example, the one test
  command that works, or "run `pnpm check` before committing").
- Conventions that differ from the language or framework defaults.
- Constraints and gotchas: generated directories, files never to edit, ordering
  requirements, environment quirks.
- Pointers to deeper docs, with when to read each one.

**Leave out:**
- Project overviews and directory tours. Agents explore faster than they read.
- Anything already in the README or derivable from config files.
- Style rules a formatter or linter enforces. Run the tool instead.
- Generic advice ("write clean code", "add tests").
- Versions and other fast-changing facts.
- Multi-step procedures. Make them skills (see `create-skill`).
- Rules that must hold every time. Enforce them with hooks, CI, or permissions.

Aim for well under 100 lines. Treat 200 as a ceiling, not a target.

## 3. Structure lightly

The [AGENTS.md standard](https://agents.md/) has no required sections. Use short
headings that match the content, for example:

```markdown
# AGENTS.md

## Commands
- Test one file: `pnpm vitest run path/to/file.test.ts`
- Before committing: `pnpm check` (lint, typecheck, test)

## Conventions
- Database access goes through `packages/db`; never import Prisma in `apps/`.
- `src/generated/` is codegen output. Edit `schema.graphql` and run `pnpm gen`.

## Docs
- Read `docs/auth.md` before touching session or token code.
```

- **Monorepos:** put an `AGENTS.md` in each package that has its own rules.
  The nearest file to the edited code applies, and hosts combine it with the
  root file.
- **Framework docs the model lacks:** if the project depends on APIs newer than
  the model's training data, a compact index of local doc files can work better
  than a skill, because it is always present. Compress it to paths and topics
  and keep the full docs in a separate folder.
- **Emphasis:** use `IMPORTANT` on at most one or two lines that agents have
  been seen to skip. If many lines are emphasized, none stand out.

## 4. Connect other tools

- **Codex, Cursor, Copilot:** read `AGENTS.md` natively. Do not create
  `.cursorrules` (deprecated) or `COPILOT.md` (not a recognized name).
- **Claude Code:** reads `CLAUDE.md`, and reads `AGENTS.md` only in some setups.
  The portable option is a `CLAUDE.md` that imports the shared file, plus any
  Claude-only notes:

  ```markdown
  @AGENTS.md
  ```

  A `CLAUDE.md -> AGENTS.md` symlink also works but can check out as a plain
  file on Windows. A sentence such as "read AGENTS.md" is weaker than the
  import, because the agent may not follow it.

## 5. Maintain it

- Add a line when an agent makes the same mistake twice, not before.
- Remove lines that no longer change behavior, and update commands when the
  tooling changes.
- Review it when it passes about 100 lines. Move task-specific material into
  linked docs or skills.
