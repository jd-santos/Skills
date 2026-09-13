# Skills

The agent skills I use across Hermes Agent, Pi, Zed, Codex, Claude Code, and
other tools that support the [Agent Skills](https://agentskills.io) format.

Most of these skills are meant to be read, copied, and adapted. They reflect how
I work, but the useful version is the one tuned to your tools, constraints, and
preferences.

## Skill list

### Workflows

| Skill | Purpose |
| --- | --- |
| [`planning-first`](skills/planning-first/) | Plan before non-trivial implementation. |
| [`ship`](skills/ship/) | Review, commit, push, and open pull requests. |
| [`todo-manager`](skills/todo-manager/) | Maintain a structured `TODO.md`. |
| [`project-issue-note`](skills/project-issue-note/) | Track projects, features, and issues in Markdown. |
| [`commit-message-writer`](skills/commit-message-writer/) | Write concise, scope-first commit messages. |
| [`changelog-writer`](skills/changelog-writer/) | Write changelog entries and release notes. |
| [`technical-writing-style`](skills/technical-writing-style/) | Keep technical prose direct and human. |
| [`offgrid-review`](https://github.com/jd-santos/offgrid-review) | Move complex decisions into a portable review workbench. |

### Design

| Skill | Purpose |
| --- | --- |
| [`ui-design`](skills/ui-design/) | Design clear, restrained, accessible application interfaces. |

### Agent tooling

| Skill | Purpose |
| --- | --- |
| [`tracked-skills`](skills/tracked-skills/) | Install and review updates for pinned external skills. |
| [`create-skill`](skills/create-skill/) | Create Agent Skills packages. |
| [`create-agents-md`](skills/create-agents-md/) | Create durable repository guidance for agents. |
| [`add-pi-feature`](skills/add-pi-feature/) | Add Pi extensions, prompts, themes, skills, and commands. |
| [`example-skill`](skills/example-skill/) | Show a minimal skill structure. |

### Languages, notebooks, and study

| Skill | Purpose |
| --- | --- |
| [`swift-code-writer`](skills/swift-code-writer/) | Guide idiomatic Swift implementation. |
| [`swift-mentor`](skills/swift-mentor/) | Teach Swift, SwiftUI, and SwiftData. |
| [`adaptive-teaching`](skills/adaptive-teaching/) | Teach efficiently with adaptive lessons and client-aware presentation. |
| [`marimo`](skills/marimo/) | Work with reactive Python notebooks. |
| [`marimo-pair`](skills/marimo-pair/) | Build inside a running marimo kernel. |
| [`study-lyrics`](skills/study-lyrics/) | Study lyrics through translation and cultural context. |

## Install

### Recommended: copy and adapt

Start with the skills that fit your workflow. Copy them into your own Agent
Skills directory, then change the instructions to suit how you work.

```bash
git clone --depth 1 https://github.com/jd-santos/Skills.git jd-skills
mkdir -p ~/.agents/skills
cp -R jd-skills/skills/planning-first ~/.agents/skills/
```

Replace `planning-first` with another skill from the list and repeat as needed.
Copy the whole directory so its references and scripts come with it.
`tracked-skills` is repository tooling and expects a full checkout.

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

Installed skills live at `~/.agents/skills/`. I use the collection with Hermes
Agent, Pi, Zed, Codex, and Claude Code. OpenCode and other tools that implement
the Agent Skills format can use the same files.

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
| `explain-diff-html` | Explain Diff by Geoffrey Litt | No license declared | [geoffreylitt/explain-diff gist](https://gist.github.com/geoffreylitt/a29df1b5f9865506e8952488eac3d524) |
| `explain-diff-notion` | Explain Diff by Geoffrey Litt | No license declared | [geoffreylitt/explain-diff gist](https://gist.github.com/geoffreylitt/a29df1b5f9865506e8952488eac3d524) |

The local installer preserves each declared upstream license and records the
source repository and exact installed commit. See
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
