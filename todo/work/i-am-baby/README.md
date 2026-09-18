# Learner-aware development guidance

Status: Ready for merge.
Scope: Skill taxonomy, a new learner-aware development skill, and retirement of the overlapping Swift mentoring skill.

## Purpose

Add a cross-stack skill for users who are unfamiliar or uncomfortable with the language, framework, or tools involved in development. The skill should preserve forward progress while explaining relevant concepts, connecting them to their parent concepts, and warning before advanced or workaround-heavy choices.

## Agreed design

- Add `i-am-baby` as a learner-aware overlay that composes with domain skills.
- Activate it when the user explicitly describes being new, unfamiliar, uncomfortable, or asks for an ELI5-style explanation.
- When basic questions only imply unfamiliarity, suggest the skill instead of silently enabling a more verbose mode.
- Give consequential decisions fuller explanations. Add brief context during routine implementation where it helps.
- Keep domain skills responsible for current APIs, project conventions, implementation, and validation.
- Compose with `adaptive-teaching` for structured explanation and offer `learning-opportunities` exercises under that skill's opt-in rules.
- Warn before advanced concepts, architectural commitments, or tricky workarounds. Distinguish necessary complexity from avoidable cleverness.
- Retire `swift-mentor`. Keep Swift implementation policy in `swift-code-writer` and direct learner-oriented Swift work to compose with `i-am-baby`.
- Split the README list into Learning and Languages and tools categories.

## Acceptance criteria

- `i-am-baby` has valid Agent Skills frontmatter and clear activation rules.
- The skill guides agents to explain concepts without blocking implementation or becoming condescending.
- The skill preserves idiomatic, maintainable implementation and warns about advanced or workaround-heavy requests.
- `adaptive-teaching` and `learning-opportunities` have distinct, non-conflicting roles.
- `swift-mentor` is removed and no maintained documentation points to it.
- The README lists `adaptive-teaching`, `i-am-baby`, `learning-opportunities`, and `study-lyrics` under Learning.
- The README lists `swift-code-writer`, `marimo`, and `marimo-pair` under Languages and tools.
- Existing unrelated work remains untouched.

## Work

- [x] Add the `i-am-baby` skill.
- [x] Update `swift-code-writer` composition guidance.
- [x] Reorganize the README skill groups.
- [x] Remove `swift-mentor`.
- [x] Validate frontmatter, links, routing scenarios, stale references, and Markdown whitespace.
- [x] Run a fresh read-only review and address accepted findings.

## Decisions

A composition-first overlay was chosen over duplicating teaching and domain guidance. This keeps technical policy in stack-specific skills and reduces drift. `learning-opportunities` remains an externally tracked, opt-in exercise skill rather than being copied into maintained content.

## Validation

- A one-off Python check passed for required frontmatter, allowed categories, retrieval phrases, required skill sections, composition rules, README grouping, local links, removed files, stale references, and prose style.
- `git diff --check` passed.
- Active diagnostics reported no findings across the changed Markdown files.
- A fresh read-only reviewer confirmed the new skill's trigger behavior, layered explanations, advanced-workaround warnings, learning-skill composition, README taxonomy, and Swift domain boundary. Its frontmatter finding for `swift-code-writer` was corrected.
- The unrelated existing change in `skills/marimo-pair/scripts/execute-code.sh` was not modified as part of this work.
