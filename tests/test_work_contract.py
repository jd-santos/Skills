"""Instruction-contract checks, not proof of agent execution behavior."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "skills/work-contract/SKILL.md").read_text()
TEXT = " ".join(SKILL.split())


class WorkContractSkillTests(unittest.TestCase):
    def test_metadata_matches_directory_and_describes_retrieval(self):
        frontmatter = re.match(r"---\n(.*?)\n---\n", SKILL, re.DOTALL)
        if frontmatter is None:
            self.fail("missing Agent Skills frontmatter")
        metadata = frontmatter.group(1)
        self.assertRegex(metadata, r"(?m)^name: work-contract$")
        self.assertIn("Use when", metadata)
        self.assertIn("write a spec", metadata)
        self.assertIn("break work into tasks", metadata)

    def test_preserves_the_task_source_and_delegates_record_creation(self):
        for requirement in (
            "project's existing tracker",
            "let `todo-manager` create it",
            "next unused number",
            "before the contract is ready to implement",
            "Do not duplicate its creation rules",
            "Do not create a second tracker",
            "If `todo-manager` is unavailable",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, TEXT)

    def test_substantial_contracts_stay_in_the_authoritative_readme(self):
        for requirement in (
            "For substantial or multi-session behavior, default to the work README",
            "only execution checklist",
            "Do not create `spec.md` solely",
            "independently useful reading or evidence purpose",
            "not size-triggered defaults",
            "Move detail rather than mirror it",
            "Let `todo-manager` own YAML metadata",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, TEXT)

    def test_synthesis_is_reconciliation_not_transcription(self):
        for requirement in (
            "current code, tests, and maintained docs",
            "material conflicts",
            "Do not replay already settled questions",
            "failure/recovery behavior",
            "acceptance criteria",
            "existing test seams",
            "scope, cost, or confidence",
            "consequential behavior is settled",
            "Routine implementation choices may remain open",
            "unknown blocks the affected scope",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, TEXT)

    def test_decomposition_is_proportional_and_does_not_authorize_new_work(self):
        for requirement in (
            "one readable checklist",
            "independently verifiable outcomes",
            "Do not manufacture dependencies",
            "expand-contract steps",
            "user's decision before becoming commitments",
            "A decomposition proposal does not authorize new work",
            "Have `todo-manager` create and link approved records",
            "without duplicating their detailed checklists",
            "separate spec file is not a prerequisite",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, TEXT)
        self.assertNotIn("to-tickets", SKILL)

    def test_execution_uses_the_agreement_without_an_extra_approval_ritual(self):
        for requirement in (
            "implementation is already authorized",
            "without a second build-approval ritual",
            "follow the agreed contract and checklist",
            "meaningful checkpoints",
            "Do not rewrite the contract to match whatever was built",
            "Verify outcomes against acceptance criteria",
            "Partial execution does not complete a parent",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, TEXT)

    def test_permissions_conflicts_and_delivery_are_not_inferred(self):
        for requirement in (
            "read-only request stays read-only",
            "Do not infer authorization to implement",
            "Do not create an issue or begin implementing merely",
            "Do not create automatic commits",
            "Do not publish an apparently agreed contract",
            "If the repo lacks a clear task authority",
            "according to write permissions",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, TEXT)
        self.assertNotIn("ready-for-agent", SKILL)
        self.assertNotIn("mattpocock", SKILL)


if __name__ == "__main__":
    unittest.main()
