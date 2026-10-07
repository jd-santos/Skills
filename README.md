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
| [`repo-commit`](skills/repo-commit/) | Review repository work and stage/commit ready changes when requested, without pushing. |
| [`ship`](skills/ship/) | Deliver requested work through pushes and pull requests. |
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

Copy the skills that fit your work, then adapt their instructions. For the
[developer workflow](#development-workflow), install the companion set rather
than the router alone:

```bash
git clone --depth 1 https://github.com/jd-santos/Skills.git jd-skills
mkdir -p ~/.agents/skills
for skill in work-routing todo-manager work-contract repo-commit ship \
  core-writing technical-writing commit-message-writer changelog-writer; do
  cp -R "jd-skills/skills/$skill" ~/.agents/skills/
done
```

The planning/task companions are `work-routing`, `todo-manager`, and
`work-contract`. Local commits use `repo-commit`, `commit-message-writer`, and
`changelog-writer`; delivery adds `ship`. Prose companions are `core-writing` and
`technical-writing`. Installing the set makes these capabilities available,
not mandatory stages. For an unrelated standalone skill, copy its whole
directory and any companions named in its instructions.

`grilling` is optional and used only when explicitly requested. It is not in the
maintained-source clone until installed. To use the reviewed pin, run
`./scripts/tracked-skills install grilling` from a full checkout, then copy the
installed skill directory with its attribution/license files if using the
copy-and-adapt setup. Other external capabilities are optional too.
`tracked-skills` itself is repository tooling and expects a full checkout.

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

## Development workflow

These skills form the development process I use with agents. They are cooperating
capabilities, not a required sequence. Clear requests go straight to work;
planning earns its place when it resolves uncertainty or preserves an agreement.

The agent gathers facts and makes routine implementation choices. Consequential
unknowns about behavior, scope, delivery order, or dependencies return to the
user. If you explicitly invoke `grilling`, its interview explores the full
decision space, including routine choices, before confirming shared understanding.
Ordinary clarification does not invoke that interview automatically.

For substantial work, keep the agreement and sole execution checklist in one
work README. It can begin with known purpose/scope and open questions before the
contract is ready. Execution follows the agreement, validates observable outcomes,
and updates that record instead of rewriting commitments to fit the build.

Local review, commits, and delivery are separate requests:

- **Review this branch:** inspect and report, without changing or delivering work.
- **Commit what's ready:** validate and create coherent local commits, without pushing.
- **Ship this:** prepare relevant ready local work if necessary, then push and
  create/update its PR. Already-committed branches need no extra commit.

Project review requirements still apply. There is no generic manual adoption
review, compulsory spec/ticket pipeline, or automatic delivery after implementation.
Use the workflow and refine it when real work exposes friction.

### Skill ownership and optional capabilities

| Responsibility | Owner |
| --- | --- |
| Select the smallest useful route | `work-routing` |
| Discover/create records and maintain task lifecycle | `todo-manager` |
| Reconcile behavior, acceptance criteria, validation, and useful slices | `work-contract` |
| Implement and validate the agreement | The executing agent |
| Review local work and apply authorized staging, commits, and closeout | `repo-commit` |
| Push and create/update PRs when requested | `ship` |
| Commit prose and release notes | `commit-message-writer` and `changelog-writer` |

Writing and domain-specific skills support this process without becoming new
workflow stages. `grilling` is an explicit full interview. Offgrid Review is an
optional way to compare complex human decisions outside chat, not a default gate.
Domain-modeling specialists may help where available; ordinary clarification
does not depend on installing one. Wayfinder and additional supporting-document
methods remain possible extensions, not prerequisites for using the process.

### Task workbench

[Todo's introduction](todo/README.md) maps this repository's records. Small work
stays inline in [TODO](todo/TODO.md); substantial efforts get a stable work README
with their agreement, decisions, and one checklist. Add subject-named supporting
material only when it has a separate reading or evidence purpose, not because
the README is long.

`todo-manager` owns metadata and lifecycle rules. Priority stays in the index;
new or explicitly migrated records use lean YAML. Existing trackers, standalone
notes, and record formats remain valid until migration is authorized. Parallel
writers use disjoint scopes/worktrees and reconcile the shared queue; ownership
notes are not locks.

`repo-commit` checks completion against actual diffs and validation during local
closeout, preserving unfinished parent scope. `ship` checks requirements due at
delivery. Work completion never claims merge or release, and optional cleanup
does not block safe delivery. File deletion requires explicit approval.

[DONE](todo/DONE.md) links to Git history, PRs, and retained evidence, not a Done
task ledger. [CHANGELOG](CHANGELOG.md) owns release notes. For projects using the
older planning or shipping setup, follow the [migration guide](docs/developer-workflow-migration.md)
one selected project or work item at a time.

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
