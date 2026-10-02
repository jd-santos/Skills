# Changelog

Notable changes to the Skills collection, using
[Keep a Changelog](https://keepachangelog.com/) sections. Release dates are used
unless the project adopts a versioning policy.

## Unreleased

### Added

- Add a local `to-spec` skill that synthesizes optional behavior contracts in
  existing work records without issue-tracker publication or duplicate checklists.
- Add `work-routing` for cross-agent workflow selection and pin Matt Pocock's
  `grilling` skill at the reviewed MIT-licensed commit.
- Reject symlinked tracked-skill caches before Git cleanup and detect changes to
  installed helper executable bits during verification.
- Add `study-cards` for sourced, Mochi-compatible Markdown flashcards and
  optional direct insertion into Mochi.
- Add a confirmed `tracked-skills add` workflow that validates and pins
  external skill sources, and register Herdr with upstream attribution.
- Add `core-writing` as the shared voice for prose and copyable text, with
  lightweight routing to focused writing skills.
- Add `i-am-baby` as a cross-stack teaching overlay for explaining consequential
  concepts without replacing domain-specific skills.

### Changed

- Let `work-routing` consider substantial project-specific answer-only work for
  backlog capture while leaving exploration and read-only requests untouched.
- Number work folders by creation order, backfill the six existing records,
  and keep their IDs stable across priority or status changes.
- Clarify when TODO items need a work record, add stable active and retained
  record navigation, and document required or optional human review during
  closeout.
- Replace `technical-writing-style` with a focused `technical-writing` skill
  that builds on `core-writing`. Commit and changelog writing now use the same
  baseline while remaining operational workflows.
- Replace the default TODO status sections and Done task ledger with a root
  `todo/` workbench: a P1–P5 priority index, human introduction, history links,
  and stable work folders for substantial efforts. The todo-manager setup now
  treats `todo/README.md` as a human-facing project introduction that credits
  the workflow and explains its core concepts. Existing queues require an
  authorized migration rather than silently creating a second tracker.
- Connect planning and shipping to work records, with separate agent ownership,
  partial-delivery handling, reviewed artifact cleanup, and explicit approval
  for file deletions. Commit and PR prose carry important reasoning into Git
  history; changelogs retain their existing location and release-note role.
- Make project, issue, and feature notes reuse an existing task workbench rather
  than creating a parallel tracker with duplicate checklists.

### Removed

- Retire the mandatory `planning-first` skill in favor of optional `work-routing` and pinned `grilling` for consequential decisions.
- Remove the overlapping `swift-mentor` skill and route Swift teaching guidance
  through `i-am-baby`.
