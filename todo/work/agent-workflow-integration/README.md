# Integrate Matt Pocock's skills with the task workbench

Status: Planned.
Priority: P4: Low (provisional; priority was not specified).

## Purpose

Try Matt Pocock's decision-making skills without creating a second issue tracker or documentation layout. Replace the mandatory `planning-first` rounds with an optional, deeper grilling workflow; keep this repository's `todo/` workbench and its Git, changelog, safety, and delivery responsibilities. Plan for Pi, Hermes Agent, Zed, Codex, Claude Code, and other supported agents from the start.

The [proposed hybrid](plan.md) fixes artifact ownership and directory conventions before any upstream skill is installed or invoked. It distinguishes skills that can be pinned unchanged, skills that need a maintained local adaptation, and skills to defer.

## Acceptance criteria

- One live task queue and one stable work record per substantial effort remain authoritative; no parallel `.scratch/` or hosted-issue workflow is introduced by default.
- Enduring domain language and rare architectural decisions have defined homes outside work records, without moving existing project documentation automatically.
- An interactive grilling trial can happen before the broader workflow changes, without creating a conflicting file layout or silently starting implementation.
- The replacement for `planning-first` removes mandatory conversational rounds and its separate save/build approvals. It leaves tool permissions, secret protection, human decisions, and Git delivery safeguards intact.
- Cross-agent routing works without relying on one harness's `Skill` tool, slash-command behavior, or private configuration.
- Every upstream candidate has an explicit pin, adapt, or defer decision; `to-tickets` is evaluated only after the grilling and spec workflow has been exercised.
- Existing `ship`, `todo-manager`, `commit-message-writer`, and `changelog-writer` remain the owners of delivery and task closeout. PR descriptions retain their detailed reasoning and validation, with relevant screenshots, short excerpts, or diagrams added when they clarify the change.

## Work

- [ ] Agree on the artifact contract and agent entry points in the [proposed hybrid](plan.md), including how existing documentation conventions take precedence. [context: medium]
- [ ] Pin only `grilling` for the first interactive trial; review its behavior and record what helped or hindered without changing the task layout. [context: small]
- [ ] Design and implement a cross-agent, locally maintained grilling-to-work-record flow; retire mandatory `planning-first` behavior and its references only after routing and permission checks pass. [context: medium]
- [ ] Adapt `to-spec` as an optional synthesis step using the existing work record and, where justified, a linked `spec.md`; do not publish to a tracker by default. [context: medium]
- [ ] Adapt domain modeling to the agreed documentation paths and promotion rules; try it on a real domain ambiguity before creating a glossary or ADR. [context: medium]
- [ ] Evaluate `to-tickets` using at least one actual multi-slice effort; decide whether blocker and vertical-slice guidance belongs in work records, a focused local skill, or a tracker integration. [context: medium]
- [ ] Assess later candidates such as `code-review` and `tdd` against uncommitted diffs, existing reviewers, and `ship`; adopt only distinct value. [context: medium]
- [ ] Adapt the upstream `pr` skill's selective screenshots, excerpts, diff sketches, and diagrams within `ship`'s detailed PR descriptions; test on a real visual or architectural PR without replacing the current PR structure. [context: small]
- [ ] Update relevant repository and agent instructions, README, changelog, and focused cross-agent routing checks as each decision is implemented; preserve unrelated changes. [context: medium]

## Boundaries

This record authorizes a proposal, not installation, skill replacement, changes to the Pi permission gate, tracker migration, or Git delivery. Do not treat a successful grilling trial as proof that `to-spec` or `to-tickets` is ready to adopt. Substantial implementation and documentation changes should receive the usual separate correctness and design reviews.

## Supporting material

- [Proposed hybrid and adoption sequence](plan.md)
- [Current task workbench](../../README.md) and [live priorities](../../TODO.md)
- [Planning skill being reconsidered](../../../skills/planning-first/SKILL.md)
- [Task workbench skill](../../../skills/todo-manager/SKILL.md)
- [Tracked external skills workflow](../../../docs/tracked-skills.md)
- [Matt Pocock's skills, reviewed at `c55ee460`](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7) and [catalog grouping](https://www.aihero.dev/skills)
