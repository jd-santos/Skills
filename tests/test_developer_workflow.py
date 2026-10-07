"""Instruction-boundary checks, not proof of live agent behavior."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return " ".join((ROOT / path).read_text().split())


COMMIT = source("skills/repo-commit/SKILL.md")
SHIP = source("skills/ship/SKILL.md")
ROUTER = source("skills/work-routing/SKILL.md")
CONTRACT = source("skills/work-contract/SKILL.md")
README = source("README.md")
MIGRATION = source("docs/developer-workflow-migration.md")


class DeveloperWorkflowTests(unittest.TestCase):
    def test_review_and_stage_only_do_not_authorize_commits(self):
        for rule in (
            "Inspection and review requests stay read-only",
            "Review-only requests stop with findings",
            "Do not edit documentation, close tasks, stage, or commit",
            "A stage-only request stops before committing",
            "do not sweep unrelated pre-staged work into the commit",
            "Preserve its staged state",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, COMMIT)

    def test_local_commits_are_not_delivery(self):
        self.assertIn("Never push, create or update PRs, merge, or release", COMMIT)
        self.assertIn("individual commits need no separate confirmation", COMMIT)
        self.assertIn("Finishing implementation does not automatically invoke", COMMIT)
        self.assertIn("Local commits do not authorize delivery", ROUTER)
        self.assertIn("owns explicitly requested remote delivery", CONTRACT)

    def test_ship_composes_local_work_and_handles_clean_branches(self):
        for rule in (
            "use `repo-commit` to validate and commit",
            "already-committed branch can be shipped without new commits",
            "Do not manufacture an empty commit",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, SHIP)
        self.assertIn("Recover relevant work-record links/trailers", SHIP)
        self.assertIn("all commits in the push range", SHIP)

    def test_delivery_respects_operation_and_safeguards(self):
        for rule in (
            "push-only request does not authorize PR creation",
            "PR-only request does not authorize unrelated local commits",
            "Always ask before pushing directly to `main`",
            "Never force-push",
            "Merge and post-merge cleanup require separate authorization",
            "preserve local commits and verified work completion",
            "If an existing PR has no new work, return its link",
            "Preserve human-written context",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, SHIP)
        self.assertIn("Never read secret-looking files", COMMIT)
        self.assertIn("Sibling worktrees are inspection-only", COMMIT)
        self.assertIn("do not bypass the gate", SHIP)

    def test_grilling_is_explicit_and_full_space(self):
        self.assertIn("Do not invoke grilling automatically", ROUTER)
        self.assertIn("including routine choices", CONTRACT)
        self.assertIn("not merely because work is large", ROUTER)
        self.assertIn("full decision-tree exploration", ROUTER)
        self.assertIn("do not impose a consequential-only filter", ROUTER)
        self.assertIn("ordinary consequential clarification", ROUTER)
        self.assertIn("routine implementation choices belong to the agent", CONTRACT)
        self.assertIn("not required for ordinary clarification", CONTRACT)
        self.assertNotIn("Pair grilling", ROUTER)
        self.assertNotIn("`grilling` skill when several dependent decisions", CONTRACT)

    def test_readme_installation_contains_transitive_companions(self):
        raw = (ROOT / "README.md").read_text()
        shell_loop = re.search(r"for skill in (.*?)\; do", raw, re.DOTALL)
        if shell_loop is None:
            self.fail("missing companion installation loop")
        copied = set(shell_loop.group(1).replace("\\", " ").split())
        self.assertEqual(
            copied,
            {
                "work-routing", "todo-manager", "work-contract", "repo-commit", "ship",
                "core-writing", "technical-writing", "commit-message-writer",
                "changelog-writer",
            },
        )
        for name in copied:
            with self.subTest(skill=name):
                self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file())
        self.assertIn("`grilling` is optional", README)
        self.assertIn("from a full checkout", README)
        self.assertIn("## Development workflow", README)
        self.assertIn("### Task workbench", README)

    def test_migration_is_bounded_and_preserves_partial_scope(self):
        for rule in (
            "targeted migration needs its own scope",
            "retaining its existing tracker and legacy plaintext notes",
            "Do not create a second queue",
            "Update active instructions only",
            "Do not rewrite every historical occurrence",
            "infer whole-record completion from a merged PR",
            "keep the parent open and the remaining work visible",
            "No manual adoption trial or temporary migration skill is required",
            "An instruction-only update needs no work-record reconciliation",
            "do not create a record or adoption journal just for an instruction update",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, MIGRATION)
        for name in ("planning-first", "to-spec", "project-issue-note", "repo-commit"):
            self.assertIn(name, MIGRATION)
        self.assertIn("lifecycle rules; `repo-commit` applies local review", source("skills/todo-manager/SKILL.md"))


if __name__ == "__main__":
    unittest.main()
