# Design skill family plan

## Problem

The current `ui-design` skill combines several layers of design guidance:

- principles that apply across visual media,
- rules specific to interactive application interfaces,
- direction-setting for new or substantially changed visual systems,
- and review guidance for evaluating finished work.

That combination makes the skill useful but strongly biased toward restrained application UI. It does not provide a clean foundation for future medium-specific skills such as Typst document design, and adding more workflows directly would make it harder to retrieve and maintain.

The goal is a composable family modeled after `core-writing` and its focused expansions. Shared guidance belongs in a small core. Medium and workflow skills add only the rules needed for their job.

## Chosen approach

Create three skills and refactor the existing one:

```text
core-design
├── ui-design
├── visual-direction
└── design-review

Future:
├── typst-design
├── promotional-design
├── editorial-design
└── portfolio-design
```

The arrows represent dependency on `core-design`, not mandatory loading of every sibling. `core-design` should point agents toward relevant companion skills, while each specialized skill declares `requires: [core-design]`.

This separates four concerns:

1. shared design judgment,
2. medium-specific implementation,
3. establishment or replacement of a visual direction,
4. evaluation of the rendered result.

## Skill contracts

### `core-design`

**Role:** Provide the medium-independent baseline for designing or evaluating a visual artifact.

**Include:**

- Identify the audience, purpose, context, and required outcome before styling.
- Distinguish refinement from redesign. Refinement preserves established identity and out-of-scope behavior; redesign deliberately replaces a visual direction while preserving factual and functional truth.
- Establish information structure, hierarchy, composition, typography, color roles, rhythm, and emphasis before decoration.
- Respect established systems and medium conventions unless the task explicitly calls for replacement.
- Use representative content and conditions rather than idealized samples.
- Check whether the result belongs to its subject or could be reused unchanged for an unrelated one.
- Treat legibility, inclusion, and relevant accessibility constraints as initial design inputs.
- Review the produced artifact, not only its source or design intentions.
- Direct agents toward a medium skill and, when applicable, `visual-direction` or `design-review`.

**Exclude:**

- HTML, component, control, breakpoint, or pointer-specific guidance.
- A default preference for restrained application UI.
- Formal critique templates, severity systems, or implementation checklists.
- Brand strategy, marketing strategy, or document-engine syntax.

Keep this comparable in role to `core-writing`: compact, broadly applicable, and insufficient by itself when a relevant specialized skill exists.

### `ui-design`

**Role:** Apply the shared design baseline to interactive, repeated-use application interfaces.

**Dependency:** `requires: [core-design]`.

**Preserve:**

- task-first hierarchy,
- low visual overhead,
- restrained geometry and color,
- conventional controls,
- forms and navigation guidance,
- user control and recovery,
- content resilience,
- state design,
- responsive restructuring,
- interaction accessibility,
- rendered review and subtraction.

**Add or strengthen:**

- Preserve established identity, behavior, factual copy, terminology, and out-of-scope areas during refinement.
- Test narrow, intermediate, and wide layouts rather than only mobile and desktop endpoints.
- After responsive reordering, confirm that visual order, DOM order, reading order, and keyboard focus order agree.
- Account for RTL layouts, direction-sensitive icons, locale-aware dates, numbers, currencies, and pluralization.
- Distinguish first use, no results, active filters, missing permission, and load failure rather than treating all empty regions alike.
- Reuse applicable default, hover, focus, active, disabled, loading, error, and success treatments across repeated controls.
- Exercise the primary task from arrival through completion and recovery with relevant input methods.
- Make contrast guidance testable with WCAG AA thresholds where applicable.
- Check that the interface uses product-specific content, workflow, terminology, data, and established visual language instead of generic decoration.

**Boundary:** Keep the restrained application default. Promotional, editorial, portfolio, and document-design work belongs in future medium skills rather than broadening `ui-design`.

Remove or shorten guidance that becomes an exact duplicate of `core-design`, but preserve UI-specific consequences and examples.

### `visual-direction`

**Role:** Establish a coherent visual direction for a new artifact, an incomplete system, or a substantial redesign.

**Dependency:** `requires: [core-design]`.

**Trigger when:**

- the user asks for a new look or visual identity,
- the current direction is intentionally being replaced,
- the artifact lacks a coherent visual system,
- or the work needs deliberate exploration before implementation.

**Workflow:**

1. Confirm the subject, audience, purpose, medium, constraints, existing commitments, and real content or assets.
2. Decide whether to preserve, extend, or replace the current direction.
3. Identify the qualities the result should communicate without relying on canned style categories.
4. When a meaningful choice remains, propose a small number of structurally distinct directions with consequences and risks.
5. Develop the selected direction across composition, typography, color, imagery, form, texture, and motion only where the medium supports them.
6. Translate the result into a concise set of durable visual rules and explicit exceptions.
7. Verify that the direction is specific to the subject, feasible in the target medium, accessible, and coherent under representative content.

**Guardrails:**

- Do not change factual claims or product behavior to make the concept work.
- Do not confuse added effects with stronger direction.
- Do not prescribe a bold or restrained register before understanding the artifact.
- Do not generate a large tournament of cosmetic variants.
- Do not create repository artifacts or design-system files unless the user asks.

### `design-review`

**Role:** Evaluate a rendered artifact against its purpose, audience, medium, constraints, and established visual system, then prioritize improvements.

**Dependency:** `requires: [core-design]`.

**Workflow:**

1. Resolve the artifact, intended audience, primary outcome, relevant states or variants, and source of design authority.
2. Inspect the actual output at representative sizes or output conditions. Use source files only as supporting evidence.
3. Review hierarchy, composition, clarity, legibility, consistency, accessibility, resilience, and subject-specific character.
4. Exercise important interactions or output paths when the medium supports them.
5. Separate findings into usability, accessibility, system consistency, resilience, visual craft, and preference.
6. Prioritize by user or reader impact. Include concrete evidence, consequences, and the smallest useful next step.
7. Identify what already works and should be preserved.
8. Route follow-up work to the applicable medium skill or `visual-direction` when the underlying direction, rather than execution, is the problem.

**Guardrails:**

- Do not require numeric scoring.
- Do not turn every observation into a high-priority issue.
- Do not present personal taste as a defect.
- Do not infer quality from clean source code or automated checks alone.
- Keep ordinary reviews concise. Expand into a formal report only when requested.

## Composition and retrieval

Descriptions should make each skill independently retrievable while preventing unnecessary overlap:

- `core-design` covers shared visual-design reasoning and should be loaded by specialized design skills.
- `ui-design` names application interfaces, forms, dashboards, controls, responsive interaction, and UI implementation.
- `visual-direction` names new visual direction, redesign, art direction, visual identity, and concept exploration.
- `design-review` names critique, design review, visual audit, hierarchy review, and evaluation of a rendered artifact.

Avoid making `core-design` trigger on every request containing the word “design” when the task is purely technical. Specialized descriptions should state both what they do and when to use them.

## Terminology and source independence

The skill family may adopt general ideas learned during the Impeccable review, but it must use its own organization, decision rules, and prose.

Do not reproduce Impeccable’s:

- command taxonomy,
- named surface modes,
- branded anti-pattern vocabulary,
- detector rules or output formats,
- context-file workflow,
- scoring templates,
- or distinctive checklist wording.

Prefer ordinary terms already used in this repository, such as purpose, audience, medium, hierarchy, visual direction, rendered artifact, representative content, resilience, and priority.

Add one brief attribution near the bottom of the repository README:

> The design skill family was informed in part by [Impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus, licensed under Apache 2.0. These skills use independent wording and structure and do not include or require Impeccable’s tooling.

Adjust the final wording if needed, but keep the attribution in one place rather than repeating it across skills.

## Repository changes

Expected files:

- `skills/core-design/SKILL.md` (new)
- `skills/visual-direction/SKILL.md` (new)
- `skills/design-review/SKILL.md` (new)
- `skills/ui-design/SKILL.md` (refactor and metadata update)
- `README.md` (skill list and attribution)
- `CHANGELOG.md` (notable unreleased change)
- `todo/TODO.md` and this work record (progress tracking)

Do not add scripts, commands, generated files, browser integrations, or external dependencies.

## Implementation sequence

1. Write `core-design` first and compare every rule against the medium-independent boundary.
2. Refactor `ui-design` against the core, retaining UI-specific detail and adding the agreed resilience and verification guidance.
3. Write `visual-direction` as a direction-setting workflow, not a collection of aesthetic recipes.
4. Write `design-review` as a review workflow, not a scoring system or automated audit.
5. Review all four descriptions together for retrieval collisions and missing triggers.
6. Update README and changelog, including the single attribution.
7. Validate the family as a composed system and each skill as a copied standalone package with declared dependencies.

Use one writer for the skill family so shared language and boundaries remain consistent. Independent read-only review can check retrieval, duplication, and source independence after the first complete draft.

## Validation

### Static checks

- Parse every changed skill’s YAML frontmatter.
- Confirm each directory name matches its `name` field.
- Confirm `ui-design`, `visual-direction`, and `design-review` declare `requires: [core-design]`.
- Check all repository-relative Markdown links.
- Run `git diff --check`.
- Confirm no external command, runtime, or project-file dependency was introduced.

### Content checks

- Each shared principle has one authoritative home.
- Each specialized skill remains understandable when copied with `core-design`.
- `ui-design` remains application-focused.
- `visual-direction` does not default to maximalism, branding work, or decorative effects.
- `design-review` distinguishes consequential findings from preference and avoids false precision.
- All agreed small UI improvements are present in either `core-design` or `ui-design`, with UI consequences retained where needed.
- The README contains one attribution and the skills do not repeat it.
- A source-independence review finds no copied paragraphs, distinctive command vocabulary, or mirrored document structure.

### Routing scenarios

Check the descriptions against representative requests:

- “Design a settings screen” loads `ui-design` with `core-design`.
- “Give this product a new visual direction” loads `visual-direction` with `core-design` and adds a medium skill when known.
- “Review this dashboard and prioritize the problems” loads `design-review`, `ui-design`, and `core-design`.
- “Improve this existing form without changing the product style” loads `ui-design` and `core-design`, not `visual-direction`.
- “Design a Typst report” does not route to `ui-design`; it remains future `typst-design` work.

## Alternatives not selected

### Only `core-design` and `design-review`

This has the smallest file count, but new-direction guidance would either bloat the core or remain scattered across medium skills. It would not cleanly represent the difference between applying a system and establishing one.

### Add a generic `design-hardening` skill

Resilience is important, but its concrete rules differ by medium. UI hardening includes interaction states, input methods, localization, and network conditions; document hardening includes pagination, font embedding, print/export behavior, and long-form flow. Keep shared review principles in `design-review` and put medium-specific resilience in the medium skills.

### Expand `ui-design` to cover every visual medium

This would preserve one entry point at the cost of conflicting defaults. Repeated-use software, editorial documents, promotional pages, and portfolios need different assumptions. A shared core plus medium skills keeps those differences explicit.

## Deferred work

The following are intentionally outside this implementation and remain separate tasks in `todo/TODO.md`:

- `typst-design`
- promotional design
- editorial design
- portfolio design

Create each only when its medium-specific workflow and retrieval triggers are clear. Do not preemptively place their rules in `core-design` or `ui-design`.
