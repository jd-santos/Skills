import argparse
import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "tracked-skills.py"
SPEC = importlib.util.spec_from_file_location("tracked_skills", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
tracked_skills = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = tracked_skills
SPEC.loader.exec_module(tracked_skills)


class AddEntryTests(unittest.TestCase):
    def setUp(self):
        self.manifest = {"version": 1, "tracked_skills": []}
        self.args = argparse.Namespace(
            repo="https://github.com/example/skills.git",
            source_path="skills/example",
            name="example",
            project="Example Project",
            author="Example Org",
            license_id="Apache-2.0",
            license_path="LICENSE",
            source_url="https://github.com/example/skills/tree/main/skills/example",
        )

    def test_add_records_validated_exact_commit_after_confirmation(self):
        with (
            patch.object(
                tracked_skills, "load_manifest", return_value=(self.manifest, [])
            ),
            patch.object(
                tracked_skills,
                "resolve_remote_head",
                return_value=("main", "a" * 40),
            ),
            patch.object(tracked_skills, "validate_add_source") as validate_source,
            patch.object(tracked_skills, "confirm", return_value=True),
            patch.object(tracked_skills, "save_json") as save_json,
            contextlib.redirect_stdout(io.StringIO()),
        ):
            tracked_skills.add_entry(self.args)

        entry = self.manifest["tracked_skills"][0]
        self.assertEqual(entry["name"], "example")
        self.assertEqual(entry["commit"], "a" * 40)
        self.assertEqual(entry["ref"], "main")
        validate_source.assert_called_once_with(
            self.args.repo, "a" * 40, "skills/example", "LICENSE"
        )
        save_json.assert_called_once_with(tracked_skills.MANIFEST_PATH, self.manifest)

    def test_declined_confirmation_does_not_write_registry(self):
        with (
            patch.object(
                tracked_skills, "load_manifest", return_value=(self.manifest, [])
            ),
            patch.object(
                tracked_skills,
                "resolve_remote_head",
                return_value=("main", "b" * 40),
            ),
            patch.object(tracked_skills, "validate_add_source"),
            patch.object(tracked_skills, "confirm", return_value=False),
            patch.object(tracked_skills, "save_json") as save_json,
            contextlib.redirect_stdout(io.StringIO()),
        ):
            tracked_skills.add_entry(self.args)

        self.assertEqual(self.manifest["tracked_skills"], [])
        save_json.assert_not_called()

    def test_duplicate_name_is_rejected_before_remote_access(self):
        existing = {"name": "example"}
        with (
            patch.object(
                tracked_skills,
                "load_manifest",
                return_value=(self.manifest, [existing]),
            ),
            patch.object(tracked_skills, "resolve_remote_head") as resolve,
            self.assertRaisesRegex(
                tracked_skills.TrackedSkillsError, "already exists"
            ),
        ):
            tracked_skills.add_entry(self.args)
        resolve.assert_not_called()

    def test_repository_url_rejects_credentials_and_url_parameters(self):
        urls = (
            "https://user:secret@example.com/repo.git",
            "https://example.com/repo.git?token=secret",
            "https://example.com/repo.git#secret",
        )
        for url in urls:
            with self.subTest(url=url):
                with (
                    patch.object(tracked_skills, "run") as run,
                    self.assertRaisesRegex(
                        tracked_skills.TrackedSkillsError, "without credentials"
                    ) as raised,
                ):
                    tracked_skills.resolve_remote_head(url)
                self.assertNotIn("secret", str(raised.exception))
                run.assert_not_called()

    def test_source_path_rejects_symlink_components(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / "real"
            target.mkdir()
            link = root / "linked"
            link.symlink_to(target, target_is_directory=True)
            with self.assertRaisesRegex(
                tracked_skills.TrackedSkillsError, "unsupported symlink"
            ):
                tracked_skills.assert_safe_path(root, link)

    def test_missing_interactive_input_reports_a_cli_option(self):
        with (
            patch.object(tracked_skills, "input", side_effect=EOFError),
            self.assertRaisesRegex(
                tracked_skills.TrackedSkillsError, "Interactive input is required"
            ),
        ):
            tracked_skills.prompt_value("Installed skill name", None, "example")

    def test_invalid_license_syntax_is_rejected_before_remote_access(self):
        self.args.license_id = "not a license"
        with (
            patch.object(
                tracked_skills, "load_manifest", return_value=(self.manifest, [])
            ),
            patch.object(tracked_skills, "resolve_remote_head") as resolve,
            self.assertRaisesRegex(
                tracked_skills.TrackedSkillsError, "Invalid SPDX license identifier"
            ),
        ):
            tracked_skills.add_entry(self.args)
        resolve.assert_not_called()

    def test_invalid_source_path_is_rejected_before_remote_access(self):
        self.args.source_path = "../outside"
        with (
            patch.object(
                tracked_skills, "load_manifest", return_value=(self.manifest, [])
            ),
            patch.object(tracked_skills, "resolve_remote_head") as resolve,
            self.assertRaisesRegex(
                tracked_skills.TrackedSkillsError, "Invalid source_path"
            ),
        ):
            tracked_skills.add_entry(self.args)
        resolve.assert_not_called()


if __name__ == "__main__":
    unittest.main()
