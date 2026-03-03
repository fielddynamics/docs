"""
cut_version.py
Snapshot the current framework/ directory into a frozen archive.

Creates  docs/framework-v{X.Y}/  by copying the entire framework/ tree,
then updates the manifest with the new archived version entry.

Usage:
    python scripts/cut_version.py              # reads version from manifest
    python scripts/cut_version.py --version 1.0  # explicit override
    python scripts/cut_version.py --dry-run    # preview without copying

After running, bump the version in framework/manifest.yaml for the next
development cycle (e.g., "1.0" -> "1.1").
"""

import argparse
import os
import re
import shutil
import sys

DOCS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAMEWORK_DIR = os.path.join(DOCS_ROOT, "framework")
MANIFEST_PATH = os.path.join(FRAMEWORK_DIR, "manifest.yaml")


def read_manifest_version():
    """Read the current version from framework/manifest.yaml."""
    if not os.path.isfile(MANIFEST_PATH):
        print("ERROR: manifest.yaml not found at", MANIFEST_PATH)
        sys.exit(1)
    with open(MANIFEST_PATH, "r", encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r'^version:\s*"?(\d+\.\d+)"?\s*$', line.strip())
            if m:
                return m.group(1)
    print("ERROR: could not parse version from manifest.yaml")
    sys.exit(1)


def update_manifest_archived(version_tag):
    """Add the given version to the archived_versions list in the manifest."""
    with open(MANIFEST_PATH, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    new_lines = []
    found_archived = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("archived_versions:"):
            found_archived = True
            existing = re.findall(r'"(\d+\.\d+)"', stripped)
            if version_tag not in existing:
                existing.append(version_tag)
            existing.sort(key=lambda v: list(map(int, v.split("."))))
            items = ", ".join('"' + v + '"' for v in existing)
            new_lines.append("archived_versions: [{}]\n".format(items))
        else:
            new_lines.append(line)

    if not found_archived:
        new_lines.insert(1, 'archived_versions: ["{}"]\n'.format(version_tag))

    with open(MANIFEST_PATH, "w", encoding="utf-8") as fh:
        fh.writelines(new_lines)
    print("Updated manifest archived_versions.")


def main():
    parser = argparse.ArgumentParser(
        description="Snapshot the framework into a versioned archive directory."
    )
    parser.add_argument(
        "--version",
        default=None,
        help="Version tag to archive (reads manifest if omitted).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without copying.",
    )
    args = parser.parse_args()

    version_tag = args.version or read_manifest_version()
    if not re.match(r"^\d+\.\d+$", version_tag):
        print("ERROR: version must be in major.minor format, got:", version_tag)
        sys.exit(1)

    archive_name = "framework-v" + version_tag
    archive_path = os.path.join(DOCS_ROOT, archive_name)

    print("Framework source:", FRAMEWORK_DIR)
    print("Archive target: ", archive_path)
    print("Version tag:    ", version_tag)

    if os.path.exists(archive_path):
        print("ERROR: archive directory already exists:", archive_path)
        print("Remove it first if you want to re-cut this version.")
        sys.exit(1)

    if args.dry_run:
        print("[DRY RUN] Would copy framework/ -> " + archive_name + "/")
        print("[DRY RUN] Would update manifest archived_versions.")
        return

    print("Copying framework tree...")
    shutil.copytree(FRAMEWORK_DIR, archive_path)
    print("Created", archive_path)

    update_manifest_archived(version_tag)

    print()
    print("Done. Next steps:")
    print("  1. Bump the version in framework/manifest.yaml for the next cycle.")
    print("  2. Restart the Flask server to pick up the new archive.")
    print("  3. Test by visiting /v{}/framework/".format(version_tag))


if __name__ == "__main__":
    main()
