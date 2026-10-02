# Composable design skill family

Status: Planned.
Priority: P3: Essential.

## Purpose

Refactor the current UI-focused design guidance into a composable skill family. A medium-independent core will provide the shared design principles, while focused skills will cover application interfaces, visual-direction work, and structured design review.

The family should follow the same dependency pattern as the writing skills: specialized skills require the core, while the core stays small and points agents toward the applicable specialization.

## Acceptance criteria

- `core-design` provides concise, medium-independent design guidance without assuming a web interface.
- `ui-design` requires `core-design` and remains focused on repeated-use application interfaces.
- `visual-direction` handles new visual languages and substantial redesigns without becoming a branding or marketing catch-all.
- `design-review` provides a rendered-artifact review workflow without mandatory scoring, external tooling, or command-specific behavior.
- The small improvements identified during the Impeccable review are incorporated into the appropriate layer of the family.
- Skill descriptions and cross-references make composition predictable without loading every design skill for every task.
- The skills use original terminology, organization, and prose. They do not depend on Impeccable commands, detectors, hooks, or project files.
- The repository README lists the new skills and includes one brief attribution near the bottom.
- Future medium-specific design skills remain separate tracked work rather than expanding `ui-design` beyond application interfaces.
- Frontmatter, Markdown links, descriptions, dependencies, and repository documentation pass focused validation.

## Work

- [ ] Finalize the skill contracts and dependency graph from the [agreed plan](plan.md). [context: small]
- [ ] Create `core-design` with the shared design baseline and composition guidance. [context: medium]
- [ ] Refactor `ui-design` to require `core-design`, preserve its application focus, and add the agreed UI-specific improvements. [context: medium]
- [ ] Create `visual-direction` for new direction and substantial redesign work. [context: medium]
- [ ] Create `design-review` for evidence-based review of rendered artifacts. [context: medium]
- [ ] Update the skill index, add one attribution, and record the notable change in the changelog. [context: small]
- [ ] Validate metadata, dependencies, links, wording independence, and representative skill-routing scenarios. [context: small]

## Supporting material

- [Plan](plan.md)
- [Impeccable](https://github.com/pbakaus/impeccable), reviewed as an external influence
- [Current UI design skill](../../../skills/ui-design/SKILL.md)
- [Core writing composition pattern](../../../skills/core-writing/SKILL.md)
