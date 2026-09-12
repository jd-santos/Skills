#!/usr/bin/env python3
"""Install and review external skills pinned in tracked-skills.json."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "tracked-skills.json"
SKILLS_DIR = ROOT / "skills"
STATE_PATH = ROOT / ".local" / "tracked-skills-state.json"
NAME_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


class TrackedSkillsError(RuntimeError):
    """A safe, user-facing tracked-skills failure."""


def run(
    *args: str,
    cwd: Path | None = None,
    capture: bool = True,
) -> str:
    result = subprocess.run(
        args,
        cwd=cwd,
        check=False,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "command failed").strip()
        raise TrackedSkillsError(f"{' '.join(args)}: {detail}")
    return (result.stdout or "").strip()


def load_json(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return default
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise TrackedSkillsError(f"Could not read {path}: {error}") from error
    if not isinstance(value, dict):
        raise TrackedSkillsError(f"Expected a JSON object in {path}")
    return value


def save_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(f"{path.suffix}.tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=False) + "\n")
    temporary.replace(path)


def relative_path(value: str, field: str) -> PurePosixPath:
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise TrackedSkillsError(f"Invalid {field}: {value!r}")
    return path


def validate_entry(raw: Any) -> dict[str, str]:
    if not isinstance(raw, dict):
        raise TrackedSkillsError("Every tracked skill entry must be an object")

    required = (
        "name",
        "repo",
        "ref",
        "commit",
        "source_path",
        "project",
        "author",
        "license",
        "license_path",
        "source_url",
        "reviewed_at",
    )
    missing = [field for field in required if not isinstance(raw.get(field), str)]
    if missing:
        raise TrackedSkillsError(
            "Tracked skill entry has missing string fields: " + ", ".join(missing)
        )

    entry = {field: raw[field] for field in required}
    if not NAME_PATTERN.fullmatch(entry["name"]):
        raise TrackedSkillsError(f"Invalid skill name: {entry['name']!r}")
    relative_path(entry["source_path"], "source_path")
    if entry["license_path"]:
        relative_path(entry["license_path"], "license_path")
    if not re.fullmatch(r"[0-9a-f]{40}", entry["commit"]):
        raise TrackedSkillsError(
            f"{entry['name']} must pin a full 40-character Git commit"
        )
    return entry


def load_manifest() -> tuple[dict[str, Any], list[dict[str, str]]]:
    manifest = load_json(MANIFEST_PATH, {})
    if manifest.get("version") != 1:
        raise TrackedSkillsError("tracked-skills.json must declare version 1")
    raw_entries = manifest.get("tracked_skills")
    if not isinstance(raw_entries, list):
        raise TrackedSkillsError("tracked_skills must be an array")

    entries = [validate_entry(raw) for raw in raw_entries]
    names = [entry["name"] for entry in entries]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise TrackedSkillsError(
            "Duplicate tracked skill names: " + ", ".join(duplicates)
        )
    return manifest, entries


def select_entries(
    entries: list[dict[str, str]], names: list[str]
) -> list[dict[str, str]]:
    if not names or names == ["all"]:
        return entries
    if "all" in names:
        raise TrackedSkillsError("Use either 'all' or explicit skill names")

    by_name = {entry["name"]: entry for entry in entries}
    unknown = sorted(set(names) - set(by_name))
    if unknown:
        raise TrackedSkillsError("Unknown tracked skills: " + ", ".join(unknown))
    return [by_name[name] for name in names]


def cache_root() -> Path:
    override = os.environ.get("AGENT_SKILLS_CACHE")
    if override:
        return Path(override).expanduser()
    xdg = os.environ.get("XDG_CACHE_HOME")
    if xdg:
        return Path(xdg).expanduser() / "agent-skills"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Caches" / "agent-skills"
    return Path.home() / ".cache" / "agent-skills"


def repo_cache(repo: str) -> Path:
    digest = hashlib.sha256(repo.encode()).hexdigest()[:16]
    return cache_root() / "sources" / digest


def repository_identity(url: str) -> str:
    """Normalize equivalent GitHub HTTPS and SSH clone URLs."""
    value = url.strip().rstrip("/").removesuffix(".git")
    github = re.fullmatch(
        r"(?:https?://github\.com/|git@github\.com:|ssh://git@github\.com/)(.+)",
        value,
        flags=re.IGNORECASE,
    )
    if github:
        return f"github.com/{github.group(1)}".lower()
    return value


def ensure_repo(entry: dict[str, str], refresh: bool = False) -> Path:
    cache = repo_cache(entry["repo"])
    cache.parent.mkdir(parents=True, exist_ok=True)
    if not cache.exists():
        print(f"Cloning {entry['repo']}")
        run("git", "clone", "--quiet", "--no-checkout", entry["repo"], str(cache))
    elif not (cache / ".git").exists():
        raise TrackedSkillsError(f"Cache path is not a Git checkout: {cache}")

    remote = run("git", "remote", "get-url", "origin", cwd=cache)
    if repository_identity(remote) != repository_identity(entry["repo"]):
        raise TrackedSkillsError(
            f"Cached origin for {entry['name']} does not match its registry entry"
        )

    commit = entry["commit"]
    has_commit = subprocess.run(
        ("git", "cat-file", "-e", f"{commit}^{{commit}}"),
        cwd=cache,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0
    if refresh:
        run("git", "fetch", "--quiet", "--tags", "--prune", "origin", cwd=cache)
    elif not has_commit:
        run("git", "fetch", "--quiet", "origin", commit, cwd=cache)

    run("git", "checkout", "--quiet", "--detach", commit, cwd=cache)
    run("git", "reset", "--quiet", "--hard", commit, cwd=cache)
    run("git", "clean", "-qfdx", cwd=cache)
    return cache


def assert_safe_tree(source: Path) -> None:
    for path in source.rglob("*"):
        if path.is_symlink():
            raise TrackedSkillsError(
                f"External skill contains an unsupported symlink: {path}"
            )


def directory_hash(directory: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(directory.rglob("*")):
        if path.is_symlink():
            raise TrackedSkillsError(f"Refusing to hash symlink: {path}")
        if path.is_file():
            relative = path.relative_to(directory).as_posix()
            digest.update(relative.encode())
            digest.update(b"\0")
            digest.update(path.read_bytes())
            digest.update(b"\0")
    return digest.hexdigest()


def materialize(
    entry: dict[str, str],
    state: dict[str, Any],
    force: bool,
) -> None:
    cache = ensure_repo(entry)
    source = cache.joinpath(*relative_path(entry["source_path"], "source_path").parts)
    license_source = None
    if entry["license_path"]:
        license_source = cache.joinpath(
            *relative_path(entry["license_path"], "license_path").parts
        )
    cache_resolved = cache.resolve()
    if not source.resolve().is_relative_to(cache_resolved):
        raise TrackedSkillsError(f"Source escapes cached repository: {source}")
    if source.is_dir() and (source / "SKILL.md").is_file():
        source_kind = "directory"
    elif source.is_file() and source.suffix.lower() == ".md":
        source_kind = "markdown"
    else:
        raise TrackedSkillsError(
            f"{entry['name']} source is not a skill directory or Markdown file: {source}"
        )
    if license_source is not None and not license_source.is_file():
        raise TrackedSkillsError(
            f"{entry['name']} license file is missing: {license_source}"
        )
    if source_kind == "directory":
        assert_safe_tree(source)
    elif source.is_symlink():
        raise TrackedSkillsError(f"External skill contains an unsupported symlink: {source}")

    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    destination = SKILLS_DIR / entry["name"]
    installed = state.setdefault("installed", {})
    previous = installed.get(entry["name"])
    if destination.exists():
        if not isinstance(previous, dict):
            if not force:
                raise TrackedSkillsError(
                    f"Refusing to replace unmanaged directory: {destination}"
                )
        elif directory_hash(destination) != previous.get("content_hash") and not force:
            raise TrackedSkillsError(
                f"{destination} has local changes; inspect it or rerun with --force"
            )

    with tempfile.TemporaryDirectory(prefix=".tracked-skill-", dir=SKILLS_DIR) as tmp:
        staged = Path(tmp) / entry["name"]
        if source_kind == "directory":
            shutil.copytree(source, staged)
        else:
            staged.mkdir()
            shutil.copy2(source, staged / "SKILL.md")
        if license_source is not None:
            shutil.copy2(license_source, staged / "UPSTREAM_LICENSE")
        provenance = {
            "project": entry["project"],
            "author": entry["author"],
            "source": entry["source_url"],
            "repository": entry["repo"],
            "commit": entry["commit"],
            "license": entry["license"],
        }
        (staged / ".tracked-source.json").write_text(
            json.dumps(provenance, indent=2) + "\n"
        )
        staged_hash = directory_hash(staged)

        if destination.exists() and directory_hash(destination) == staged_hash:
            print(f"{entry['name']}: already installed")
        else:
            backup = SKILLS_DIR / f".{entry['name']}.previous"
            if backup.exists():
                try:
                    shutil.rmtree(backup)
                except OSError as error:
                    raise TrackedSkillsError(
                        f"Could not remove stale backup {backup}: {error}"
                    ) from error
            moved_existing = False
            try:
                if destination.exists():
                    destination.rename(backup)
                    moved_existing = True
                staged.rename(destination)
            except OSError as error:
                if moved_existing:
                    try:
                        backup.rename(destination)
                    except OSError as restore_error:
                        raise TrackedSkillsError(
                            f"Could not restore {destination} after failed install"
                        ) from restore_error
                raise TrackedSkillsError(
                    f"Could not install {entry['name']}: {error}"
                ) from error
            if backup.exists():
                try:
                    shutil.rmtree(backup)
                except OSError as error:
                    raise TrackedSkillsError(
                        f"Installed {entry['name']}, but could not remove {backup}: "
                        f"{error}"
                    ) from error
            print(f"{entry['name']}: installed {entry['commit'][:12]}")

    installed[entry["name"]] = {
        "repo": entry["repo"],
        "source_path": entry["source_path"],
        "commit": entry["commit"],
        "content_hash": directory_hash(destination),
    }


def hydrate(entries: list[dict[str, str]], force: bool) -> None:
    state = load_json(STATE_PATH, {"version": 1, "installed": {}})
    if state.get("version") != 1 or not isinstance(state.get("installed"), dict):
        raise TrackedSkillsError(f"Unsupported local state in {STATE_PATH}")
    for entry in entries:
        materialize(entry, state, force)
        save_json(STATE_PATH, state)


def resolve_candidate(entry: dict[str, str]) -> tuple[Path, str]:
    cache = ensure_repo(entry, refresh=True)
    ref = entry["ref"]
    run("git", "fetch", "--quiet", "origin", ref, cwd=cache)
    candidate = run("git", "rev-parse", "FETCH_HEAD^{commit}", cwd=cache)
    return cache, candidate


def confirm(prompt: str) -> bool:
    try:
        return input(f"{prompt} [y/N] ").strip().lower() in {"y", "yes"}
    except EOFError:
        return False


def update_entries(
    manifest: dict[str, Any],
    selected: list[dict[str, str]],
    force: bool,
) -> None:
    approved: dict[str, str] = {}
    for entry in selected:
        key = "\0".join((entry["repo"], entry["ref"], entry["commit"]))
        if key in approved:
            continue
        cache, candidate = resolve_candidate(entry)
        current = entry["commit"]
        if candidate == current:
            print(f"{entry['project']}: already at {current[:12]}")
            approved[key] = current
            continue

        print(f"\n{entry['project']}: {current[:12]} -> {candidate[:12]}")
        print(run("git", "log", "--oneline", f"{current}..{candidate}", cwd=cache))
        print("\nDiff summary:")
        print(run("git", "diff", "--stat", current, candidate, cwd=cache))
        if confirm("Show the full diff?"):
            run("git", "diff", "--color=always", current, candidate, cwd=cache, capture=False)
        if confirm("Pin and install this update?"):
            approved[key] = candidate
        else:
            approved[key] = current

    selected_names = {entry["name"] for entry in selected}
    changed_names: list[str] = []
    today = date.today().isoformat()
    for raw in manifest["tracked_skills"]:
        if raw["name"] not in selected_names:
            continue
        key = "\0".join((raw["repo"], raw["ref"], raw["commit"]))
        candidate = approved.get(key, raw["commit"])
        if candidate != raw["commit"]:
            raw["commit"] = candidate
            raw["reviewed_at"] = today
            changed_names.append(raw["name"])

    if not changed_names:
        print("No registry pins changed.")
        return
    save_json(MANIFEST_PATH, manifest)
    _, updated_entries = load_manifest()
    hydrate(select_entries(updated_entries, changed_names), force)
    print(f"Updated registry pins: {', '.join(changed_names)}")


def verify(entries: list[dict[str, str]]) -> None:
    state = load_json(STATE_PATH, {"version": 1, "installed": {}})
    installed = state.get("installed", {})
    failures = 0
    for entry in entries:
        destination = SKILLS_DIR / entry["name"]
        record = installed.get(entry["name"]) if isinstance(installed, dict) else None
        if not destination.is_dir() or not isinstance(record, dict):
            print(f"{entry['name']}: not installed")
            failures += 1
            continue
        if record.get("commit") != entry["commit"]:
            print(f"{entry['name']}: installed commit does not match registry")
            failures += 1
            continue
        if directory_hash(destination) != record.get("content_hash"):
            print(f"{entry['name']}: local content differs from generated state")
            failures += 1
            continue
        print(f"{entry['name']}: verified {entry['commit'][:12]}")
    if failures:
        raise TrackedSkillsError(f"Verification failed for {failures} skill(s)")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Install and review external Agent Skills from pinned sources."
    )
    subparsers = result.add_subparsers(dest="command", required=True)

    for command in ("install", "verify"):
        child = subparsers.add_parser(command)
        child.add_argument("names", nargs="*", default=["all"])
        if command == "install":
            child.add_argument(
                "--force",
                action="store_true",
                help="replace unmanaged or locally modified destinations",
            )

    update = subparsers.add_parser("update")
    update.add_argument("names", nargs="*", default=["all"])
    update.add_argument(
        "--force",
        action="store_true",
        help="replace a locally modified generated destination after approval",
    )
    subparsers.add_parser("list")
    return result


def main() -> int:
    args = parser().parse_args()
    manifest, entries = load_manifest()
    if args.command == "list":
        for entry in entries:
            print(
                f"{entry['name']}\t{entry['commit'][:12]}\t"
                f"{entry['project']}\t{entry['source_url']}"
            )
        return 0

    selected = select_entries(entries, args.names)
    if args.command == "install":
        hydrate(selected, args.force)
    elif args.command == "verify":
        verify(selected)
    elif args.command == "update":
        update_entries(manifest, selected, args.force)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TrackedSkillsError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from error
