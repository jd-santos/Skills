# Changelog

Notable changes to the Skills collection, using
[Keep a Changelog](https://keepachangelog.com/) sections. Release dates are used
unless the project adopts a versioning policy.

## Unreleased

### Added

- Add `core-writing` as the shared voice for prose and copyable text, with
  lightweight routing to focused writing skills.

### Changed

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
