# Skills

The agent skills I use across Pi, Claude Code, OpenCode, and other tools that
support the [Agent Skills](https://agentskills.io) format.

Most of these skills are meant to be read, copied, and adapted. They reflect how
I work, but the useful version is the one tuned to your tools, constraints, and
preferences.

## Skills I maintain

### Workflows and communication

| Skill | What it does |
| --- | --- |
| [`planning-first`](skills/planning-first/) | Runs a two-round planning process before non-trivial implementation. |
| [`ship`](skills/ship/) | Recovers repository context, reviews local work, creates focused commits, and handles pushes and pull requests. |
| [`todo-manager`](skills/todo-manager/) | Maintains a structured `TODO.md` with active work, upcoming tasks, backlog, and completed work. |
| [`project-issue-note`](skills/project-issue-note/) | Creates Markdown project, feature, and issue notes with consistent frontmatter. |
| [`commit-message-writer`](skills/commit-message-writer/) | Writes concise commit messages using a scope-first format. |
| [`changelog-writer`](skills/changelog-writer/) | Writes readable changelog entries and release notes using Keep a Changelog sections. |
| [`technical-writing-style`](skills/technical-writing-style/) | Keeps technical prose direct, useful, and free of corporate or generated-sounding filler. |
| [`offgrid-review`](https://github.com/jd-santos/offgrid-review) | Moves complex decisions into a portable review workbench with a separate verified apply pass. Maintained in its own repository. |

### Agent and skill tooling

| Skill | What it does |
| --- | --- |
| [`tracked-skills`](skills/tracked-skills/) | Installs external skills from reviewed commits and shows upstream changes before advancing pins. |
| [`create-skill`](skills/create-skill/) | Creates focused Agent Skills packages with useful retrieval descriptions and supporting files. |
| [`create-agents-md`](skills/create-agents-md/) | Creates repository guidance files that give coding agents durable project context. |
| [`add-pi-feature`](skills/add-pi-feature/) | Adds Pi extensions, skills, prompts, themes, commands, and related configuration. |
| [`example-skill`](skills/example-skill/) | Provides a small reference implementation of the skill format. |

### Swift and notebooks

| Skill | What it does |
| --- | --- |
| [`swift-code-writer`](skills/swift-code-writer/) | Guides idiomatic Swift implementation using current project settings and Apple documentation. |
| [`swift-mentor`](skills/swift-mentor/) | Teaches Swift, SwiftUI, and SwiftData with explanations of design choices and modern patterns. |
| [`marimo`](skills/marimo/) | Covers reactive notebook structure, data work, widgets, SQL, export, and deployment. |
| [`marimo-pair`](skills/marimo-pair/) | Works inside a running marimo kernel to execute code and build notebooks as artifacts. |

### Language study

| Skill | What it does |
| --- | --- |
| [`study-lyrics`](skills/study-lyrics/) | Studies user-provided lyrics through translation, language notes, and sourced cultural context. |

## Install

### Recommended: copy and adapt

I recommend copying the skills you want into your own Agent Skills directory,
then editing them to match your workflow. That gives you a stable local version
without inheriting changes from this repository.

Copy one skill:

```bash
git clone --depth 1 https://github.com/jd-santos/Skills.git /tmp/jd-skills
mkdir -p ~/.agents/skills
cp -R /tmp/jd-skills/skills/planning-first ~/.agents/skills/
rm -rf /tmp/jd-skills
```

Replace `planning-first` with any standalone skill from the table above.
Supporting files inside the skill directory are part of the skill and should be
copied with it. The `tracked-skills` skill is the exception because it depends
on the registry and scripts in a full repository checkout.

To use all of the standalone skills as a starting point:

```bash
git clone --depth 1 https://github.com/jd-santos/Skills.git /tmp/jd-skills
mkdir -p ~/.agents/skills
for skill in /tmp/jd-skills/skills/*; do
  [ "${skill##*/}" = "tracked-skills" ] || cp -R "$skill" ~/.agents/skills/
done
rm -rf /tmp/jd-skills
```

This copies only files committed to this repository and skips the
checkout-specific management skill. It does not download the third-party skills
listed later in this README.

### Track this repository directly

If you want to follow this collection as it changes, clone it at the shared
Agent Skills location:

```bash
git clone https://github.com/jd-santos/Skills.git ~/.agents
~/.agents/scripts/tracked-skills install
```

The first command installs the skills maintained in this repository. The second
installs the reviewed external skills and Offgrid Review from their pinned
commits.

Update maintained skills without advancing external pins:

```bash
cd ~/.agents
git pull --ff-only
./scripts/tracked-skills install
```

### Dotfiles submodule

This repository is also designed to be checked out as the `agents/.agents`
submodule in [jd-santos/Dotfiles](https://github.com/jd-santos/Dotfiles). GNU
Stow then exposes the checkout at `~/.agents`:

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

## External work and attribution

Some of the skills in my personal setup come from other authors. Their projects
remain the canonical sources, and their work is not committed to this
repository.

| Installed skill | Project and author | License | Source |
| --- | --- | --- | --- |
| `informed-patient` | Informed Patient by Dr. Cat Hicks | CC BY 4.0 | [DrCatHicks/informed-patient](https://github.com/DrCatHicks/informed-patient) |
| `learning-opportunities` | Learning Opportunities by Dr. Cat Hicks | CC BY 4.0 | [DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities) |
| `orient` | Orient by Dr. Michael Mullarkey | CC BY 4.0 | [DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities/tree/main/orient) |

The local installer preserves each upstream license and records the source
repository and exact installed commit. See
[`tracked-skills.json`](tracked-skills.json) for the reviewed pins.

Offgrid Review uses the same pinned installation mechanism because its canonical
source is a separate repository, but it is my own project.

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
part of this repository's committed source. If you distribute modified copies,
follow the license terms that apply to those files.
