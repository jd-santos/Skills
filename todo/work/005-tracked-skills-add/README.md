# Add tracked-skill registration

Status: Ready for review.

## Purpose

Add a safe, repeatable `tracked-skills add` workflow and use it to register and install Herdr's upstream skill without committing upstream skill text.

## Acceptance criteria

- `tracked-skills add` supports guided registration of an upstream skill with an exact commit pin and validated source and license metadata.
- Existing registry entries and generated directories are not overwritten without explicit approval.
- Herdr is registered with attribution, ignored as generated content, installed, and verified.
- Documentation and focused tests describe and validate the command.
- The Dotfiles submodule pointer is not advanced as part of this task.

## Work

- [x] Design and implement the registration command with validation and confirmation before registry writes.
- [x] Add focused tests for entry validation, duplicate handling, and registration behavior.
- [x] Document the command and Herdr attribution; add its generated destination to `.gitignore`.
- [x] Register and install Herdr, then verify the generated install and review the diff.

## Decisions

- Use a guided add command rather than only hand-editing registry files.
- Keep upstream skill content out of the repository. The utility pins the reviewed commit and installs generated local content.
- Leave the Dotfiles submodule pointer unchanged.

## Validation

- `python3 -m unittest discover -s tests -v` (8 passed)
- `python3 -m py_compile scripts/tracked-skills.py tests/test_tracked_skills.py`
- `./scripts/tracked-skills install herdr` and `verify herdr`
- `git diff --check` and LSP diagnostics on both Python files

The initial registration work installed the skill in this checkout and left the
Dotfiles pointer unchanged. Advancing that pointer is a separate delivery step.

## Supporting material

- [Tracked skills workflow](../../../docs/tracked-skills.md)
- [Tracked-skill registry](../../../tracked-skills.json)
