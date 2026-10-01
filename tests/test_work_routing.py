import re
import unittest
from pathlib import Path

SKILL_PATH = (
    Path(__file__).resolve().parents[1] / "skills" / "work-routing" / "SKILL.md"
)
SKILL = SKILL_PATH.read_text()


class WorkRoutingSkillTests(unittest.TestCase):
    def test_agent_skills_metadata_matches_directory(self):
        frontmatter = re.match(r"---\n(.*?)\n---\n", SKILL, re.DOTALL)
        if frontmatter is None:
            self.fail("missing Agent Skills frontmatter")
        metadata = frontmatter.group(1)
        self.assertRegex(metadata, r"(?m)^name: work-routing$")
        self.assertRegex(metadata, r"(?m)^description: .+")

    def test_route_matrix_covers_the_agreed_workflows(self):
        for route in (
            "Clear, bounded change",
            "Discussion or exploration only",
            "Several consequential decisions remain open",
            "Domain terms, relationships, or boundaries are unclear or contested",
            "A substantial behavior contract needs to travel across sessions",
            "Work needs independent implementation slices",
            "A very large effort still has no clear destination",
        ):
            with self.subTest(route=route):
                self.assertIn(route, SKILL)

    def test_explicit_direction_confirmation_and_safety_are_preserved(self):
        for requirement in (
            "Follow explicit user direction",
            "keep the session read-only",
            "confirms the shared understanding",
            "Normal tool permissions",
            "Ask before substituting",
            "never create automatic commits",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, SKILL)

    def test_existing_project_task_conventions_are_preserved(self):
        self.assertIn("If the project uses or adopts a `todo/` workbench", SKILL)
        self.assertIn("Preserve other trackers until migration is authorized", SKILL)

    def test_router_does_not_depend_on_host_specific_invocation(self):
        self.assertNotIn("Skill tool", SKILL)
        self.assertNotIn("/plan", SKILL)
        self.assertIn("mechanisms verified for the current agent", SKILL)


if __name__ == "__main__":
    unittest.main()
