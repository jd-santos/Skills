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
| [`work-routing`](skills/work-routing/) | Choose the shortest useful workflow for discovery and implementation. |
| [`work-contract`](skills/work-contract/) | Reconcile behavior decisions and define useful implementation outcomes in the existing work record. |
| [`ship`](skills/ship/) | Review, commit, push, and open pull requests. |
| [`todo-manager`](skills/todo-manager/) | Create and maintain task entries, work records, metadata, and lifecycle rules. |
| [`commit-message-writer`](skills/commit-message-writer/) | Write concise, scope-first commit messages. |
| [`changelog-writer`](skills/changelog-writer/) | Write changelog entries and release notes. |
| [`offgrid-review`](https://github.com/jd-santos/offgrid-review) | Move complex decisions into a portable review workbench. |

### Communication

| Skill | Purpose |
| --- | --- |
| [`core-writing`](skills/core-writing/) | Apply JD's baseline voice to prose and copyable text. |
| [`technical-writing`](skills/technical-writing/) | Write accurate, useful technical material. |

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

### Learning

| Skill | Purpose |
| --- | --- |
| [`adaptive-teaching`](skills/adaptive-teaching/) | Teach efficiently with adaptive lessons and client-aware presentation. |
| [`i-am-baby`](skills/i-am-baby/) | Guide development when the language or stack is unfamiliar. |
| [`learning-opportunities`](https://github.com/DrCatHicks/learning-opportunities) | Practice concepts through opt-in exercises during development. |
| [`study-lyrics`](skills/study-lyrics/) | Study lyrics through translation and cultural context. |
| [`study-cards`](skills/study-cards/) | Create sourced, Mochi-compatible study cards from learning materials. |

### Languages and tools

| Skill | Purpose |
| --- | --- |
| [`swift-code-writer`](skills/swift-code-writer/) | Guide idiomatic Swift implementation. |
| [`marimo`](skills/marimo/) | Work with reactive Python notebooks. |
| [`marimo-pair`](skills/marimo-pair/) | Build inside a running marimo kernel. |

## Install

### Recommended: copy and adapt

Start with the skills that fit your workflow. Copy them into your own Agent
Skills directory, then change the instructions to suit how you work.

```bash
git clone --depth 1 https://github.com/jd-santos/Skills.git jd-skills
mkdir -p ~/.agents/skills
cp -R jd-skills/skills/work-routing ~/.agents/skills/
```

Replace `work-routing` with another skill from the list and repeat as needed.
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
installs the reviewed external skills, including `grilling` and
Offgrid Review from their pinned commits.

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

Reload the relevant tool after installing or changing skills. If `grilling`
is absent from the host's catalog, the router can check the installed source at
`skills/grilling/SKILL.md` in this collection (normally
`~/.agents/skills/grilling/SKILL.md`). Install/repair it with
`./scripts/tracked-skills install grilling`, then verify it with
`./scripts/tracked-skills verify grilling`. Direct file retrieval is not proof
of automatic discovery or cross-agent parity.

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
| `herdr` | Herdr by herdrdev | Apache 2.0 | [Herdr skill](https://github.com/herdrdev/herdr/tree/master/skills/herdr) |
| `grilling` | Matt Pocock Skills by Matt Pocock | MIT | [Pinned grilling skill](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/grilling) |

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

## Task workbench

Start at [todo/README.md](todo/README.md) for the human introduction and map.
Agents use [todo/TODO.md](todo/TODO.md) as a P1–P5 priority index; larger tasks
keep their execution checklist and supporting evidence in stable work folders.
Parallel agents primarily edit separate records and reconcile the shared queue
during integration. Ownership notes are not cross-worktree locks.

`work-routing` selects useful capabilities without requiring users to name a
skill or follow a mandatory pipeline. Each capability can also be invoked
directly. Clear requests proceed directly; unresolved consequential decisions
can use `grilling`. `todo-manager` finds or creates the authoritative work record
once authorized work warrants a durable home; its contract need not be settled.
`work-contract` reconciles behavior, defines acceptance criteria and validation,
and decomposes work only when useful. Consequential changes to scope, delivery
order, or dependencies require the user's decision. Execution follows the
agreement and updates the existing checklist rather than silently changing the
contract to match the build.

The work README holds the full contract, including substantial or multi-session
work. Subject-named attachments are optional for independently useful reading
or evidence, not because a contract is long. New or explicitly migrated work
READMEs use YAML `status` with optional `pr`, `blocked_by`, `parent`, `child`, and
`tags`; priority stays in TODO. Tags can describe useful subjects or subsystems
without a required taxonomy. No deadline or Git-derived audit fields are required.
Hierarchy does not imply dependencies or mirrored child progress. Existing
record formats and standalone notes remain valid until migration is authorized.
Shipping checks task claims against the diff, preserves unfinished work, and
prepares `status: complete` only for verified whole-record completion in the
pre-merge closeout commit, without claiming merge or release. It proposes
artifact pruning before merge; file deletions require explicit approval.
Completed work does not accumulate in a Done task section.

[DONE](todo/DONE.md) points to Git history, PRs, and retained records.
[CHANGELOG.md](CHANGELOG.md) holds release notes. DONE may highlight a few major
releases, but does not duplicate the changelog. Older projects keep their
existing task location until a migration is authorized.

## Repository layout

```text
.
├── docs/
├── scripts/
│   ├── tracked-skills
│   └── tracked-skills.py
├── skills/
│   └── <maintained-skill>/
├── todo/
│   ├── README.md
│   ├── TODO.md
│   ├── DONE.md
│   └── work/
├── CHANGELOG.md
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
