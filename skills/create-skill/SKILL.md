---
name: create-skill
description: Creates and revises agent skills (SKILL.md packages) for repeatable workflows and on-demand knowledge. Use when building a new skill, rewriting or slimming an existing one, fixing a skill that fails to trigger, or when user says "create a skill" or "make a new skill".
metadata:
  version: "2.0.0"
  author: jdwork
  category: meta
---

# Create Skill

A skill is a folder with a `SKILL.md` that an agent loads only when its
description matches the task. The description is always in context; the body
and any bundled files load on demand. Write for a capable agent: include only
what it would otherwise get wrong or have to rediscover.

## 1. Decide whether it should be a skill

| Need | Put it in |
| --- | --- |
| A repeatable procedure, or knowledge needed only for some tasks | Skill |
| A fact every task in a repo needs (commands, constraints, gotchas) | `AGENTS.md` (see `create-agents-md`) |
| A rule that must hold every time (format, lint, blocked paths) | Hook, linter, or CI check |
| A deterministic, fragile sequence | Script, invoked from a skill |

Agents can fail to load skills they would benefit from. Vercel's evals found an
unprompted skill was skipped in over half of runs, while a compact docs index in
`AGENTS.md` was always present. If the agent must have the knowledge on nearly
every task, prefer always-on context.

Before writing, ask for or collect two or three real tasks the skill should
handle. They drive the description, the body, and the tests.

## 2. Save it under `.agents/skills/`

| Scope | Path |
| --- | --- |
| Personal (default) | `~/.agents/skills/<skill-name>/SKILL.md` |
| Project | `<repo-root>/.agents/skills/<skill-name>/SKILL.md` |

`.agents/skills/` is the single source that Claude Code, pi, and OpenCode all
read. `~/.claude/skills` is a symlink into it, so a skill written under
`.claude/skills/` becomes a second copy that drifts and that pi and OpenCode
never see. Create `.agents/skills/` if it is missing rather than falling back to
`.claude/`. For Claude Code discovery in a project, link it once:
`ln -s ../.agents/skills <repo-root>/.claude/skills`.

Before finishing, confirm the written path contains `/.agents/skills/`.

## 3. Write the frontmatter

Use only the fields in the [Agent Skills spec](https://agentskills.io/specification)
so the skill loads everywhere:

```yaml
---
name: kebab-case-name          # 1-64 chars, a-z 0-9 and hyphens, matches the folder
description: ...               # 1-1024 chars, no XML tags
metadata:                      # optional, string values only
  version: "1.0.0"
  author: jdwork
  category: workflow
  requires: "core-writing"     # informational only; see step 6
license: ...                   # optional
compatibility: ...             # optional, e.g. required tools or network access
---
```

Keep custom keys such as `version`, `author`, `category`, and `requires` under
`metadata`. The reference validator and claude.ai reject unknown top-level keys.
Use host-specific fields (for example Claude Code's `disable-model-invocation`,
`allowed-tools`, or `paths`) only in skills meant for that host.

Categories: `automation`, `code-quality`, `database`, `documentation`,
`education`, `git`, `meta`, `security`, `testing`, `workflow`.

## 4. Write the description for retrieval

The description is the only text the agent sees when deciding whether to load
the skill. Write it in the third person, with two parts:

1. **What it does.** Start with a verb: Creates, Runs, Audits, Writes.
2. **When to use it.** A `Use when...` clause naming the situations, the
   technology keywords, and the phrases users actually type.

```yaml
# Good
description: Runs database migrations with backup and rollback support. Use when applying schema changes, updating database structure, or when user says "migrate" or "run migrations".

# Bad: no trigger context
description: Runs database migrations safely.
```

- Put the main use case first. Some hosts truncate long descriptions.
- Agents tend to undertrigger, so list adjacent situations where the skill
  helps even when the user does not name it.
- Be specific, not loud. `Use when...` works; `ALWAYS use this skill...`
  causes overtriggering on newer models.
- Skip tags. Put searchable words in the description.

## 5. Write the body

There is no required section layout. Use the structure the task needs.

- **Add only what the agent lacks.** Cut explanations of general concepts,
  restated defaults, and anything a strong model already does well.
- **Match freedom to fragility.** Give goals and judgment criteria for
  heuristic work. Give exact commands, ordered steps, or a script for
  operations that break or destroy data when done slightly wrong.
- **Explain why instead of shouting.** A short reason generalizes better than
  `MUST` or `NEVER`. Reserve emphasis for one rule you have seen agents break.
- **Cover failure where it matters.** Add checks and recovery steps for
  destructive, irreversible, or environment-sensitive steps. Skip the
  boilerplate error-handling section otherwise.
- **Show, briefly.** One concrete input and output example usually beats a
  paragraph of description.
- **Use imperative language** and one term per concept.

## 6. Use progressive disclosure

- Keep `SKILL.md` under 500 lines (about 5,000 tokens). Aim much lower.
- Move detail into `references/`, deterministic helpers into `scripts/`, and
  templates or static files into `assets/`.
- Link each bundled file directly from `SKILL.md` and say when to read it.
  Keep references one level deep; agents may only skim files linked from other
  linked files.
- Add a short table of contents to reference files over about 100 lines.
- Keep everything the skill needs inside its folder so it works when copied.

No loader resolves dependencies between skills. If a skill builds on another,
say so in the body, for example "Apply `core-writing` first", and record it in
`metadata.requires` for humans.

## 7. Test and iterate

1. Run the real tasks from step 1 without the skill and note what goes wrong.
2. Write the smallest skill that fixes those failures.
3. Run the same tasks with a fresh agent that has the skill. Watch which files
   it reads, which it skips, and where it hesitates.
4. Check triggering with a few prompts that should load the skill and a few
   near misses that should not.
5. Revise from what you observed, not from what seems thorough. Delete
   instructions that change nothing.

Test with the weakest model the skill must support. What is enough for a large
model may be too little for a small one.

## Template

```markdown
---
name: skill-name
description: [Does what]. Use when [situations], or when user says "[phrase]".
metadata:
  version: "1.0.0"
  author: jdwork
  category: [category]
---

# Skill Name

[One or two sentences: the outcome and any key boundary.]

## Workflow

1. [Step, with the exact command if it is fragile]
2. [Step]
3. [How to verify the result]

## Notes

[Only the gotchas the agent would otherwise hit.]
```
