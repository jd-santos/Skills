# Skills

The agent skills I use across Pi, Claude Code, OpenCode, and other tools that
support the [Agent Skills](https://agentskills.io) format.

The repository contains skills I maintain and a pinned registry for selected
skills maintained by other authors. External skill text is downloaded locally
from its canonical repository. It is not committed here.

## External work and attribution

Several important skills in my setup come from other public projects:

| Installed skill | Project and author | License | Source |
| --- | --- | --- | --- |
| `informed-patient` | Informed Patient by Dr. Cat Hicks | CC BY 4.0 | [DrCatHicks/informed-patient](https://github.com/DrCatHicks/informed-patient) |
| `learning-opportunities` | Learning Opportunities by Dr. Cat Hicks | CC BY 4.0 | [DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities) |
| `orient` | Orient by Dr. Michael Mullarkey | CC BY 4.0 | [DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities/tree/main/orient) |
| `offgrid-review` | Offgrid Review by JD Santos | GPL-3.0 | [jd-santos/offgrid-review](https://github.com/jd-santos/offgrid-review) |

Those projects remain the canonical sources. The local installer preserves each
upstream license and records the source repository and exact installed commit.
See [`tracked-skills.json`](tracked-skills.json) for the reviewed pins.

## Repository layout

```text
.
├── docs/
├── scripts/
│   ├── tracked-skills
│   └── tracked-skills.py
├── skills/
│   └── <maintained-skill>/
├── tracked-skills.json
└── LICENSE
```

Generated external skills also appear directly under `skills/` after
installation. Their directories and local installation state are ignored by
Git.

## Install

### Direct installation

Clone the repository at the shared Agent Skills location:

```bash
git clone https://github.com/jd-santos/Skills.git ~/.agents
~/.agents/scripts/tracked-skills install
```

The first command installs the maintained skills. The second installs the
reviewed external skills from their pinned commits.

To update the maintained skills without advancing external pins:

```bash
cd ~/.agents
git pull --ff-only
./scripts/tracked-skills install
```

### Dotfiles submodule

This repository is also designed to be checked out as the `agents/.agents`
submodule in [jd-santos/Dotfiles](https://github.com/jd-santos/Dotfiles).
GNU Stow then exposes the checkout at `~/.agents`:

```bash
git submodule update --init --recursive
stow agents
agents/.agents/scripts/tracked-skills install
```

The Dotfiles repository pins a reviewed Skills commit. Pulling Dotfiles does not
silently advance this repository or any external skill pin.

## Discovery

Installed skills live at `~/.agents/skills/`. That path is used by:

- Pi through its configured `skills` path
- Claude Code through the `.agents` compatibility path
- OpenCode through its global Agent Skills path
- Other tools that implement the Agent Skills format

Reload the relevant tool after installing or changing skills.

## Maintained skills

### Workflow

- `planning-first`: two-round planning before non-trivial implementation
- `ship`: branch review, commits, push, and pull request workflow
- `todo-manager`: structured `TODO.md` task tracking
- `project-issue-note`: Markdown project and issue notes
- `commit-message-writer`: concise scoped commit messages
- `changelog-writer`: Keep a Changelog release entries
- `technical-writing-style`: direct, casual-professional technical prose
- `tracked-skills`: pinned installation and reviewed updates for external skills

### Skill and agent tooling

- `create-skill`: create Agent Skills-compatible skill packages
- `create-agents-md`: create repository guidance for coding agents
- `add-pi-feature`: add Pi skills, extensions, prompts, themes, and commands
- `example-skill`: minimal skill structure example

### Language and notebook work

- `swift-code-writer`: idiomatic Swift implementation guidance
- `swift-mentor`: explanatory Swift, SwiftUI, and SwiftData guidance
- `marimo`: reactive notebook concepts and references
- `marimo-pair`: work with a running marimo notebook kernel
- `study-lyrics`: translation and language study for user-provided lyrics

## External skill installation

List configured sources:

```bash
./scripts/tracked-skills list
```

Install or repair all pinned skills:

```bash
./scripts/tracked-skills install
./scripts/tracked-skills verify
```

Install one configured skill:

```bash
./scripts/tracked-skills install informed-patient
```

Review upstream changes before advancing pins:

```bash
./scripts/tracked-skills update
```

The update command shows commits and a diff summary, offers the full diff, and
asks for approval before changing `tracked-skills.json`. See
[`docs/tracked-skills.md`](docs/tracked-skills.md) for safety and recovery
details.

## Adding a maintained skill

Create a directory containing an uppercase `SKILL.md`:

```text
skills/my-skill/
├── SKILL.md
├── reference/
└── scripts/
```

At minimum, `SKILL.md` needs `name` and `description` frontmatter:

```yaml
---
name: my-skill
description: What the skill does and when an agent should load it.
---
```

Keep required references and helper scripts inside the skill directory so the
skill works when copied independently.

## License

Skills and code committed to this repository are licensed under GPL-3.0. Skills
installed from external repositories retain their upstream licenses and are not
part of this repository's committed source.
