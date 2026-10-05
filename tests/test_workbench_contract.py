"""Instruction-contract checks, not proof of live agent or host behavior."""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANAGER = (ROOT / "skills/todo-manager/SKILL.md").read_text()
REFERENCE = (ROOT / "skills/todo-manager/references/workbench.md").read_text()
ROUTER = (ROOT / "skills/work-routing/SKILL.md").read_text()
CONTRACT = (ROOT / "skills/work-contract/SKILL.md").read_text()
SHIP = (ROOT / "skills/ship/SKILL.md").read_text()
COMMIT = (ROOT / "skills/repo-commit/SKILL.md").read_text()
MANAGER_TEXT = " ".join(MANAGER.split())
CONTRACT_TEXT = " ".join(CONTRACT.split())


class WorkbenchContractTests(unittest.TestCase):
    def test_metadata_schema_is_lean_and_scoped(self):
        schema = REFERENCE.split("### Work-record YAML\n", 1)[1]
        schema = schema.split("\n## ", 1)[0].split("\n### ", 1)[0]
        fields = re.findall(r"^\| `([a-z_]+)` \|", schema, re.MULTILINE)
        self.assertEqual(fields, ["status", "pr", "blocked_by", "parent", "child", "tags"])
        for requirement in (
            "Required string",
            "Optional string",
            "Optional nonempty list",
            "Omit unused fields",
            "repository-root-relative",
            "new or explicitly migrated",
            "not the workbench introduction",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, REFERENCE)
        self.assertIn("Respect existing metadata and plaintext records", MANAGER)

    def test_new_record_template_has_only_required_metadata(self):
        template = re.search(
            r"```markdown\n---\n(.*?)\n---\n\n# Work title", REFERENCE, re.DOTALL
        )
        if template is None:
            self.fail("missing minimal work-record YAML template")
        self.assertEqual(template.group(1), "status: planned")

    def test_hierarchy_does_not_duplicate_dependency_or_progress(self):
        for requirement in (
            "containment; `blocked_by` expresses dependency",
            "One direction of a hierarchy link is enough",
            "keep them consistent",
            "hierarchy cycles, or dependency cycles",
            "without mirroring child checkboxes/status",
            "including required\nchild outcomes",
            "outside authorized scope",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, REFERENCE)

    def test_substantial_contracts_default_to_readme(self):
        self.assertIn("Substantial or multi-session work still defaults", ROUTER)
        self.assertIn("For substantial or multi-session behavior, default", CONTRACT)
        self.assertIn("Length alone does not require", ROUTER)
        self.assertIn("not size-triggered defaults", CONTRACT)
        self.assertNotIn("that needs detail, write `spec.md`", CONTRACT)
        for source in (" ".join(ROUTER.split()), CONTRACT_TEXT):
            self.assertIn("independently useful reading or evidence purpose", source)
            self.assertIn("Move detail rather than mirror it", source)

    def test_pre_merge_completion_is_not_delivery(self):
        for source in (MANAGER, REFERENCE, COMMIT):
            with self.subTest(source=source.splitlines()[0]):
                self.assertIn("pre-merge", source)
                self.assertIn("status: complete", source)
                self.assertIn("whole", source)
        self.assertIn("not that a PR merged or a release occurred", MANAGER)
        self.assertIn("Failed delivery is reported separately", REFERENCE)
        self.assertIn("failed validation or new scope reopens", " ".join(COMMIT.split()))
        self.assertIn("No ceremonial post-merge status commit", MANAGER)

    def test_router_delegates_metadata_and_lifecycle(self):
        self.assertIn("Use `todo-manager` for work-record YAML", ROUTER)
        self.assertIn("At task entry reconcile only the selected record", ROUTER)
        self.assertIn("Let `todo-manager` own YAML metadata", CONTRACT)
        self.assertIn("Do not define a second task schema", COMMIT)
        self.assertIn("using task-management rules", SHIP)

    def test_retired_skills_have_no_wrapper_or_active_router_reference(self):
        for name in ("to-spec", "project-issue-note"):
            with self.subTest(name=name):
                self.assertFalse((ROOT / "skills" / name).exists())
                self.assertNotIn(name, ROUTER)
                self.assertNotIn(name, CONTRACT)
                self.assertNotIn(name, (ROOT / "README.md").read_text())

    def test_useful_record_creation_guidance_is_owned_by_manager(self):
        for requirement in (
            "Before creation, search the index",
            "Reuse a matching record",
            "purpose and current scope can be stated honestly",
            "settled contract is not a prerequisite",
            "exploratory conversation alone does not authorize task writes",
            "Preserve existing standalone notes",
            "unknown non-sensitive metadata",
            "user's decision before creating",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, MANAGER_TEXT)

    def test_optional_tags_do_not_reintroduce_the_old_tracker_schema(self):
        schema = REFERENCE.split("### Work-record YAML\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn("unique, nonempty strings", schema)
        self.assertIn("No mandatory taxonomy", schema)
        self.assertIn("omit empty or duplicate tags", schema)
        self.assertIn("Git provides change history", " ".join(schema.split()))
        self.assertNotIn("next_actions:", MANAGER)
        self.assertNotIn("ai-model:", MANAGER)
        self.assertIn("Tags are an optional nonempty list", MANAGER_TEXT)

    def test_grilling_pointer_has_reviewed_installation_source(self):
        self.assertRegex(ROUTER, r"\]\(\.\./grilling/SKILL\.md\)")
        self.assertIn("read the actual source before using it", ROUTER)
        self.assertIn("ask before installation or substitution", ROUTER)
        self.assertIn("not automatic discovery or cross-agent parity", ROUTER)
        registry = json.loads((ROOT / "tracked-skills.json").read_text())
        grilling = next(
            entry for entry in registry["tracked_skills"] if entry["name"] == "grilling"
        )
        self.assertRegex(grilling["commit"], r"^[0-9a-f]{40}$")
        self.assertEqual(grilling["license"], "MIT")
        self.assertIn("/skills/grilling/", (ROOT / ".gitignore").read_text())

    def test_navigation_does_not_mirror_record_status(self):
        navigation = (ROOT / "todo/README.md").read_text()
        record_map = navigation.split("## Work records\n", 1)[1].split(
            "## Priorities\n", 1
        )[0]
        self.assertNotIn("### Active", record_map)
        self.assertNotRegex(record_map, r"\)\s*[—–]\s*(Planned|In progress|Ready)")
        for target in re.findall(r"\]\((work/[^)]+/README\.md)\)", record_map):
            with self.subTest(target=target):
                self.assertTrue((ROOT / "todo" / target).is_file())


if __name__ == "__main__":
    unittest.main()
