# Changelog

Notable changes to the Skills collection, using
[Keep a Changelog](https://keepachangelog.com/) sections. Release dates are used
unless the project adopts a versioning policy.

## Unreleased

### Changed

- Replace the default TODO status sections and Done task ledger with a root
  `todo/` workbench: a P0–P4 priority index, human introduction, history links,
  and stable work folders for substantial efforts. Existing queues require an
  authorized migration rather than silently creating a second tracker.
- Connect planning and shipping to work records, with separate agent ownership,
  partial-delivery handling, reviewed artifact cleanup, and explicit approval
  for file deletions. Commit and PR prose carry important reasoning into Git
  history; changelogs retain their existing location and release-note role.
- Make project, issue, and feature notes reuse an existing task workbench rather
  than creating a parallel tracker with duplicate checklists.
