---
name: create-skill
description: Creates new skills (SKILL.md files) for repeatable workflows. Use when building a new skill, writing skill instructions, or when user says "create a skill" or "make a new skill".
version: 1.2.0
author: jdwork
category: meta
---

# Skill: Create Skill

## Description

Creates well-structured agent skills (`SKILL.md`) for repeatable workflows and actions, following the [Agent Skills](https://agentskills.io) open standard. Skills live under `.agents/skills/` and are shared across Claude Code, pi, and OpenCode. They are retrieved by agents when needed, making them ideal for specific procedures rather than general knowledge.

## When to Create a Skill

**DO create a skill for:**
- Deployment procedures
- Database migrations
- Running test suites with specific setup
- Code generation workflows
- Audits (accessibility, security, performance)
- Complex refactoring procedures

**DON'T create a skill for:**
- General framework knowledge → use AGENTS.md
- Coding conventions → use AGENTS.md
- Project structure documentation → use AGENTS.md

**Rule of thumb:** If it's a repeatable *action* with specific steps → Skill. If it's *knowledge* the agent should always have → AGENTS.md (use `create-agents-md` skill).

## Where Skills Live — Directory Structure (READ FIRST, MUST FOLLOW)

**Every skill MUST be saved under an `.agents/skills/` tree. You MUST NOT create it under `.claude/skills/`.**

| Scope | Exact path to create |
|-------|----------------------|
| Personal / reusable (default) | `~/.agents/skills/<skill-name>/SKILL.md` |
| Project-specific | `<repo-root>/.agents/skills/<skill-name>/SKILL.md` |

**Why this is a hard rule — not a preference:** `.agents/` is the single canonical source of truth for skills, and every agent tool reads from it — Claude Code, pi, and OpenCode. At the personal level, Claude Code's `~/.claude/skills` is a **symlink into `~/.agents/skills`**, so a skill saved there is discovered by all three tools automatically (Claude Code picks it up on next restart). The `.agents/` path is what keeps one skill working everywhere instead of three copies drifting apart.

For a **project-specific** skill, still author it in `<repo-root>/.agents/skills/`. If that repo also needs Claude Code to auto-discover it, create the same one-time symlink in the repo (`ln -s ../.agents/skills <repo-root>/.claude/skills`) — author once in `.agents/`, never maintain a second copy under `.claude/`.

**Do NOT write to `.claude/skills/` or `~/.claude/skills/`.** That location is only a symlink target, not a place to author files. Writing a real file or directory there:

- forks a second copy that silently drifts out of sync with `.agents/`,
- is invisible to pi and OpenCode,
- can shadow or collide with the symlinked tree and corrupt discovery.

If the target `.agents/skills/` directory does not exist yet, **create it** (`mkdir -p`). Do not "fall back" to `.claude/` because it happens to exist.

**Verify before you finish (do not skip):** the full path of the file you wrote MUST contain `/.agents/skills/` and MUST NOT contain `/.claude/skills/`. If it contains `/.claude/skills/`, you placed it wrong — move it into `.agents/skills/` and confirm again.

## Instructions

### 1. Required Frontmatter

Every skill must have YAML frontmatter:

```yaml
---
name: kebab-case-skill-name
description: What it does + when to use it. Claude uses this to decide when to load the skill.
version: 1.0.0
author: [optional]
category: [optional - category from list below]
requires: [optional - other skill names this depends on]
---
```

**Note:** Skip `tags` - they don't help retrieval. Put searchable keywords in the description instead.

### 2. Category Options

Use one of these standard categories:

| Category | Use For |
|----------|---------|
| `automation` | CI/CD, deployments, builds, scheduled tasks |
| `code-quality` | Linting, formatting, refactoring, code review |
| `database` | Migrations, queries, schema changes, backups |
| `documentation` | Docs generation, README updates, API docs |
| `meta` | Skills about skills, templates, tooling setup |
| `security` | Audits, vulnerability scanning, secrets management |
| `testing` | Test execution, coverage, fixtures, mocking |
| `workflow` | Multi-step procedures that span categories |

### 3. Write Descriptions for Retrieval

**Claude uses the description to decide when to load a skill.** Descriptions need two parts:

1. **What it does** (verb-first)
2. **When to use it** (trigger scenarios, user phrases)

```yaml
# Good - what + when
description: Runs database migrations with backup and rollback support. Use when applying schema changes, updating database structure, or when user says "migrate" or "run migrations".

# Good - includes trigger phrases
description: Writes git commit messages using Conventional Commits format. Use when committing code, writing commit messages, or when user asks for help with commits.

# Bad - no trigger context
description: Helps with database stuff.

# Bad - what only, no when
description: Runs database migrations safely.
```

**Tips:**
- Start with action verb (Creates, Runs, Audits, Generates, Deploys)
- Include technology keywords users might say (PostgreSQL, React, Docker)
- Add "Use when..." with specific scenarios
- Include phrases users actually type ("help me write", "how do I", etc.)

### 4. Structure the Skill Body

Required sections:

```markdown
# Skill: [Human-Readable Name]

## Description
[1-2 sentences on what this does and when to use it]

## Instructions

### 1. Pre-flight Checks
[What to verify before running]

### 2. Main Workflow
[Numbered steps to execute]

### 3. Error Handling
[What to do when things fail]

## Examples
[At least one usage example]
```

Optional sections:
- `## Prerequisites` - Required tools, setup, or context
- `## Notes` - Caveats, edge cases, tips
- `## Cross-Reference` - Related skills or AGENTS.md

### 5. Write Pre-flight Checks

Explicit checks prevent errors:

```markdown
### 1. Pre-flight Checks

Before running this skill:

1. **Verify environment**: Check that `.env` exists and has required variables
2. **Confirm target**: Ask user to confirm the target environment (dev/staging/prod)
3. **Check dependencies**: Run `which docker` to ensure Docker is installed
4. **Backup state**: If modifying data, note current state for rollback
```

### 6. Define Error Handling

Tell the agent what to do on failure:

```markdown
### 3. Error Handling

If the migration fails:
1. Read the error log at `./logs/migration-error.log`
2. Do NOT retry automatically—report the error to the user
3. If in production, immediately run the rollback script
4. Check the `migrations/` folder for the failed migration file
```

### 7. Add Examples

Show realistic usage with expected behavior:

```markdown
## Examples

### Example: Running in Development

**User:** "Use the migrate-db skill to run pending migrations"

**Workflow:**
1. Check environment → `.env` shows `DATABASE_URL` is set
2. Confirm target → User confirms "development"
3. Run migrations → `prisma migrate dev`
4. Report results → "Applied 3 migrations successfully"
```

## Skill Composition

For complex skills, split into smaller skills and use `requires`:

```yaml
---
name: full-deploy
requires: [run-tests, build-app, deploy-to-cloud]
---
```

Keep individual skills under 200 lines when possible. If a skill grows too large, extract sub-workflows into separate skills.

## Anti-Patterns

- **God skills:** One skill that does everything → Split into focused skills
- **Micro skills:** Skill for trivial single commands → Just document in AGENTS.md
- **Knowledge skills:** General "how to" information → Use AGENTS.md instead
- **Missing error handling:** No guidance on failures → Always include recovery steps

## Template

> Save this file to `~/.agents/skills/<skill-name>/SKILL.md` (personal) or `<repo-root>/.agents/skills/<skill-name>/SKILL.md` (project). Never `.claude/skills/`. See [Where Skills Live](#where-skills-live--directory-structure-read-first-must-follow).

```markdown
---
name: skill-name
description: [What it does]. Use when [trigger scenarios] or when user [phrases they might say].
version: 1.0.0
category: [category]
---

# Skill: [Human Name]

## Description

[What this skill does and when to use it.]

## Instructions

### 1. Pre-flight Checks

Before running:
- [ ] Check [requirement 1]
- [ ] Verify [requirement 2]

### 2. Workflow

1. **Step one**: [action]
2. **Step two**: [action]
3. **Step three**: [action]

### 3. Error Handling

If the skill fails:
1. [Recovery action]
2. [Fallback behavior]

## Examples

### Basic Usage

**User:** "[example request]"
**Result:** [expected outcome]

## Notes

[Optional caveats or tips]
```

## Cross-Reference

For project knowledge and conventions that agents should always have, create an AGENTS.md file instead using the `create-agents-md` skill.

**Placement reminder:** the finished skill goes under `.agents/skills/`, never `.claude/skills/` — see [Where Skills Live](#where-skills-live--directory-structure-read-first-must-follow).
