# Plan: tracked-skills add command

## Problem

The external-skill utility can install and update pinned entries, but adding a source requires manual registry, ignore, and attribution edits. Add a guided command that validates a new upstream skill and its metadata, pins an exact commit, and only writes after confirmation.

## Chosen approach

Implement `tracked-skills add <repository> <source-path>` as an interactive workflow. Derive the candidate commit from the repository's default HEAD, prompt for the install name and attribution/license fields with safe defaults where possible, validate the source and configured license file at the pinned commit, show the proposed entry, and require confirmation before appending it to `tracked-skills.json`. Fail on duplicate names, invalid paths, missing skill content, or invalid registry fields. Keep installation as an explicit subsequent command, matching the existing documented flow.

After registering Herdr, add its generated path to `.gitignore`, add an attribution row to README, and run install and verify. Do not edit the Dotfiles submodule pointer or its unrelated dirty files.

## Tradeoffs

- A guided command is more useful than a one-off manual registry edit, while keeping a small explicit confirmation boundary.
- Prompting for attribution avoids guessing author or license from ambiguous repository metadata.
- Registry, README, and ignore updates remain separate responsibilities for now, matching the current documented add workflow and avoiding brittle automatic Markdown edits.
- Installing remains separate from registering, so the user can review the proposed registry change first.

## Acceptance criteria

See [work README](README.md). Tests cover validation and non-overwrite behavior. Run script help, focused tests, Herdr install, verification, and a final diff/status review.
