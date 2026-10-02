# Integrate Matt Pocock's skills with the task workbench

Status: In progress. The `grilling` pin is installed and verified, the portable `work-routing` and local `to-spec` skills are implemented, and `planning-first` and Pi's `/plan` prompt are retired. Live trials and optional adaptations remain open.
Priority: P4: Low (provisional; priority was not specified).

## Purpose

Try Matt Pocock's decision-making skills without creating a second issue tracker or documentation layout. Retire the mandatory `planning-first` rounds in favor of a pinned `grilling` skill and a small cross-agent router that recommends the shortest useful path. Keep this repository's `todo/` workbench and its Git, changelog, safety, and delivery responsibilities. Plan for Pi, Hermes Agent, Zed, Codex, Claude Code, and other supported agents from the start.

The [agreed implementation plan](plan.md) records the artifact and routing contract. The conversation trialed grilling from its reviewed upstream source; the exact reviewed commit is now pinned, installed, and verified. The installed skill still needs an interactive trial, and cross-agent retrieval is not yet validated. The initial Skills delivery added the portable router. A separate Dotfiles change retires Pi's old planning prompt and instructions. Correctness and design reviews found cache and executable-bit safety gaps in the tracked-skills utility, plus a router assumption about adopted task workbenches. Those were fixed and covered by focused tests; legacy generated state needs a one-time reinstall before its new hash can verify.

## Acceptance criteria

- One live task queue and one stable, creation-order-numbered work record per substantial effort remain authoritative; no parallel `.scratch/` or hosted-issue workflow is introduced by default.
- Domain-modeling notes generated during development live in the work record. Existing maintained docs take precedence for reusable vocabulary; create a glossary only when several shared terms justify it. Reserve `docs/adr/` (or an existing convention) for consequential, agreed tradeoffs, distinguishing decisions from shipped behavior.
- The conversation grilling trial is recorded honestly; the installed grilling interaction and cross-agent routing behavior remain explicit validation steps.
- The replacement for `planning-first` removes mandatory conversational rounds and its separate save/build approvals. One confirmation of shared understanding precedes the requested next step, subject to tool permissions, secret protection, human decisions, and Git delivery safeguards.
- A portable router recommends the shortest useful sequence, follows explicit user direction, asks when the route remains unclear, and can pair grilling with domain modeling when the model itself needs work. It reserves a future Wayfinder branch without adopting Wayfinder yet.
- Cross-agent routing works without relying on one harness's `Skill` tool, slash-command behavior, or private configuration; Pi's `/plan` template is removed, not replaced with another Pi tool.
- Every upstream candidate has an explicit pin, adapt, or defer decision; `to-tickets` is evaluated only after the grilling and spec workflow has been exercised. Git commits group coherent decisions, documentation, and code rather than recording every grilling answer.
- Existing `ship`, `todo-manager`, `commit-message-writer`, and `changelog-writer` remain the owners of delivery and task closeout. PR descriptions retain their detailed reasoning and validation, with relevant screenshots, short excerpts, or diagrams added when they clarify the change.

## Work

- [x] Agree on the artifact ownership, router behavior, domain-document promotion, and retirement direction in the [implementation plan](plan.md); trial the upstream grilling questions in conversation without installing a skill. [context: medium]
- [x] Pin, install, and verify only `grilling` at the reviewed upstream commit; its license and exact source were checked. [context: small]
- [ ] Trial the installed skill on a bounded uncertainty and record question quality, user effort, and handoff into the existing work record. [context: small]
- [x] Add the portable `work-routing` skill for direct work, grilling, optional domain modeling and specs, and implementation slices; reserve Wayfinder as a future route. Add focused routing checks. [context: medium]
- [x] Retire `planning-first`, remove `/plan`, and update the Pi instructions and references as a separate Dotfiles change from the initial Skills delivery. [context: medium]
- [x] Implement a locally maintained [`to-spec` skill](../../../skills/to-spec/SKILL.md) from the [agreed synthesis contract](plan.md#process-contract). Keep concise acceptance criteria and the only checklist in the work README; put detailed behavior, flexible scenarios or stories, testing decisions, and unresolved contract questions in a linked `spec.md` only when it helps. [context: medium]
- [ ] Trial `to-spec` on a real behavior contract and record whether synthesis, contradiction checks, and test-seam guidance help without extra approval stops. [context: small]
- [ ] Adapt domain modeling to the workbench-first capture and selective documentation-promotion rules; try it on a real domain ambiguity before creating a glossary or ADR. [context: medium]
- [ ] Evaluate `to-tickets` on a real multi-slice effort using a readable work README checklist first, with real blockers and a wide-refactor exception. Use separately linked numbered records under `todo/` when backlog clarity or independent ownership/delivery calls for them. Decide whether a maintained skill adds value. [context: medium]
- [ ] Assess later candidates such as `code-review` and `tdd` against uncommitted diffs, existing reviewers, and `ship`; adopt only distinct value. [context: medium]
- [ ] Adapt the upstream `pr` skill's selective screenshots, excerpts, diff sketches, and diagrams within `ship`'s detailed PR descriptions; test on a real visual or architectural PR without replacing the current PR structure. [context: small]
- [x] Align `work-routing` and tests with project-fit TODO capture for substantial requests, including answer-only deliverables. Preserve exploratory and explicit read-only boundaries. [context: small]
- [x] Number the six existing work folders by first Git addition and update the workbench naming convention and links. [context: small]
- [ ] Update relevant repository and agent instructions, README, changelog, and focused cross-agent routing checks as each decision is implemented; preserve unrelated changes. [context: medium]

## Boundaries

The separate [P3 Wayfinder task](../../TODO.md#p3-essential) has been promoted without raising the priority of every remaining integration experiment. The `to-spec` design and later `to-tickets` path are agreed in the linked plan. The workbench's six preexisting effort folders were numbered by first Git addition; no other project's folders were migrated. The initial Skills slice pinned `grilling`, added the router, and hardened the tracked-skills installer. The user separately authorized retiring the planning-first skill and Pi's `/plan` prompt. Permission-gate changes and tracker migration remain out of scope. The installed `grilling` skill and local `to-spec` have not had live trials; `to-tickets` remains deferred. Correctness and design reviews identified the installer and router fixes covered by focused tests.

## Implementation checkpoint

The six work folders were numbered `001`–`006` by first Git addition. The agreed [spec and future tickets contract](plan.md#process-contract) was saved before the requested compaction. The local `to-spec` skill, router update, focused tests, and Skills README and changelog changes belong to the Skills integration branch. The parent Dotfiles submodule pin is delivered separately.

The live `to-spec` and installed `grilling` trials remain open. Later, test a real multi-slice effort before deciding whether to adapt `to-tickets`. Begin with one readable checklist, split into numbered work records only for backlog clarity or independent ownership, and preserve real blockers and the wide-refactor exception. [context: medium]

At the earlier compaction checkpoint, all 16 Skills tests, `tracked-skills verify grilling`, local Markdown links, and `git diff --check` passed. A read-only correctness review found no migration blocker, and a design review found the spec/tickets ownership coherent. Six moved documents matched `HEAD` byte-for-byte; the other three were intentionally edited. For the current skill changes, all 21 Skills tests, `tracked-skills verify grilling`, local Markdown links, `git diff --check`, and LSP checks of the changed Python tests passed. Fresh correctness and design reviewers found no blockers; the unavailable `todo-manager` fallback and contract-critical tests were strengthened after review. A live behavior-contract trial and cross-agent retrieval checks remain open. One pre-existing queue inconsistency remains: records `002`, `003`, and `005` say Ready for review or merge but are absent from `todo/TODO.md`. Verify their delivery and reconcile them separately rather than assuming they are active or done.

## Supporting material

- [Agreed implementation plan and adoption sequence](plan.md)
- [Current task workbench](../../README.md) and [live priorities](../../TODO.md)
- [New cross-agent router](../../../skills/work-routing/SKILL.md) and [local spec synthesis skill](../../../skills/to-spec/SKILL.md)
- [Task workbench skill](../../../skills/todo-manager/SKILL.md)
- [Tracked external skills workflow](../../../docs/tracked-skills.md)
- [Matt Pocock's skills, reviewed at `c55ee460`](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7) and [catalog grouping](https://www.aihero.dev/skills)
