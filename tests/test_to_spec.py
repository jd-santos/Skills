import re
import unittest
from pathlib import Path

SKILL_PATH = Path(__file__).resolve().parents[1] / "skills" / "to-spec" / "SKILL.md"
SKILL = SKILL_PATH.read_text()


class ToSpecSkillTests(unittest.TestCase):
    def test_metadata_matches_directory_and_describes_retrieval(self):
        frontmatter = re.match(r"---\n(.*?)\n---\n", SKILL, re.DOTALL)
        if frontmatter is None:
            self.fail("missing Agent Skills frontmatter")
        metadata = frontmatter.group(1)
        self.assertRegex(metadata, r"(?m)^name: to-spec$")
        self.assertRegex(metadata, r"(?m)^description: .*spec.*")
        self.assertIn("Use when", metadata)

    def test_preserves_the_existing_task_source_and_artifact_ownership(self):
        for requirement in (
            "project's existing tracker",
            "next unused number",
            "spec.md",
            "README owns status, concise acceptance criteria",
            "only execution checklist",
            "Link to the README's criteria",
            "Do not create `spec.md` solely",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, SKILL)

    def test_synthesizes_without_reopening_settled_decisions(self):
        for requirement in (
            "current conversation",
            "current code, tests, and maintained docs",
            "material conflicts",
            "Do not replay already settled questions",
            "stories optional",
            "scenarios or edge cases",
            "existing test seams",
            "scope, cost, or confidence",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, SKILL)

    def test_preserves_permissions_and_avoids_issue_tracker_publication(self):
        for requirement in (
            "read-only request stays read-only",
            "Do not infer authorization to implement",
            "Do not create automatic commits",
            "Do not create an issue",
            "no work record exists",
            "If `todo-manager` is unavailable",
            "If the repo lacks a clear task authority",
            "Do not publish an apparently agreed spec",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, SKILL)
        self.assertNotIn("ready-for-agent", SKILL)
        self.assertNotIn("/setup-matt-pocock-skills", SKILL)


if __name__ == "__main__":
    unittest.main()
