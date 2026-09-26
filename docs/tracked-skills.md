# Tracked external skills

The tracked-skills utility installs selected public skills without committing
copies of their text to this repository.

## Model

`tracked-skills.json` is both a source registry and a lock file. Every entry
contains:

- The installed skill name
- The canonical repository and project page
- The upstream branch or tag used when checking for updates
- An exact reviewed Git commit used for installation
- The skill path and, when available, license path inside the upstream repository
- The project, author, license, and review date used for attribution

Installation always uses the exact commit. The `ref` field is only an update
hint.

## Local files

The utility keeps upstream Git checkouts in a user cache:

- macOS: `~/Library/Caches/agent-skills/sources/`
- Linux and other systems: `~/.cache/agent-skills/sources/`
- With `XDG_CACHE_HOME`: `$XDG_CACHE_HOME/agent-skills/sources/`
- With `AGENT_SKILLS_CACHE`: `$AGENT_SKILLS_CACHE/sources/`

Generated skill directories live under `skills/`. Local installation state is
stored in `.local/tracked-skills-state.json`. All of these generated paths are
ignored by Git.

Each generated skill includes:

- The upstream skill files. A standalone Markdown skill is installed as `SKILL.md`.
- `UPSTREAM_LICENSE`, when copied from a configured upstream license
- `.tracked-source.json`, containing source and commit provenance

The installer does not edit the upstream `SKILL.md`.

## Commands

Run commands from any directory through the repository script:

```bash
/path/to/Skills/scripts/tracked-skills list
/path/to/Skills/scripts/tracked-skills add <repo> <source-path> [options]
/path/to/Skills/scripts/tracked-skills install [all|<name> ...]
/path/to/Skills/scripts/tracked-skills verify [all|<name> ...]
/path/to/Skills/scripts/tracked-skills update [all|<name> ...]
```

### Install

`install` clones missing source repositories, checks out each pinned commit, and
materializes the selected skills. Re-running it is idempotent.

The command refuses to replace:

- A destination it did not previously generate
- A generated destination changed since the previous installation
- A source that is neither a directory containing `SKILL.md` nor a standalone
  Markdown skill file
- A source or license path that escapes the cached repository
- A source tree containing symbolic links

Use `--force` only after inspecting the destination and accepting its removal.

### Verify

`verify` compares installed commits and content hashes with the local state and
registry. It does not fetch upstream changes.

### Update

`update` fetches the configured upstream ref, then shows:

1. The current and candidate commits
2. The upstream commit log
3. A diff summary
4. The full diff when requested
5. A final approval prompt

Only approved candidates update the committed registry. The utility then
materializes the approved commit. Review and commit the resulting
`tracked-skills.json` change in this repository.

Entries that share a repository, ref, and current commit are reviewed together.
For example, `learning-opportunities` and `orient` advance from one upstream
review when both are selected.

## Adding a source

Use `add` to register an external source after validating its skill and license
paths at the current default-branch commit:

```bash
./scripts/tracked-skills add https://github.com/owner/project.git skills/example \
  --name example \
  --project "Example Project" \
  --author "Example Author" \
  --license Apache-2.0 \
  --license-path LICENSE \
  --source-url https://github.com/owner/project/tree/main/skills/example
```

Only the repository and skill source path are positional. Omit metadata options
to enter them interactively. The command prints the exact commit and proposed
registry entry, then asks for confirmation before writing `tracked-skills.json`.
It accepts HTTPS repository URLs. Use `NOASSERTION` with an empty license path
when the upstream source does not declare a license. The utility checks
identifier syntax, but you must confirm the identifier is recognized by SPDX
and matches the upstream license.

Before confirming the prompt, review the displayed repository, source path,
exact commit, and attribution. Check the skill content and license at that pinned
commit; the command validates source and license paths but does not assess the
content. Decline if anything needs more review.

After registration:

1. Add `skills/<name>/` to `.gitignore` and add visible attribution to the
   README.
2. Install and verify the selected skill:

   ```bash
   ./scripts/tracked-skills install <name>
   ./scripts/tracked-skills verify <name>
   ```

The command does not install the skill or edit documentation automatically.

## Recovery

Generated skills can be deleted and recreated:

```bash
rm -rf skills/<external-name> .local/tracked-skills-state.json
./scripts/tracked-skills install
```

Deleting the source cache only causes the next installation to clone the pinned
repositories again.
