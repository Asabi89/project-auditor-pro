#!/usr/bin/env python3
"""Read-only repository inventory helper. Does not open file contents or modify files."""
import argparse
import json
import os
from pathlib import Path
import stat

VCS_EXCLUDES = {".git", ".hg", ".svn"}
GENERATED_EXCLUDES = {
    "node_modules", "vendor", ".venv", "venv",
    "__pycache__", ".mypy_cache", ".pytest_cache", ".next", "dist", "build",
    "coverage", ".turbo", ".cache", "target"
}

def is_link(metadata):
    return stat.S_ISLNK(metadata.st_mode) or bool(
        getattr(metadata, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT
    )


def raise_walk_error(error):
    raise error


def inventory(root, excludes):
    records = []
    for directory, directories, filenames in os.walk(root, onerror=raise_walk_error):
        directory = Path(directory)
        directories[:] = [
            name for name in directories
            if name not in excludes and not is_link((directory / name).lstat())
        ]
        for name in filenames:
            if name in excludes:
                continue
            path = directory / name
            metadata = path.lstat()
            if is_link(metadata) or not stat.S_ISREG(metadata.st_mode):
                continue
            records.append({
                "path": path.relative_to(root).as_posix(),
                "suffix": path.suffix.lower(),
                "bytes": metadata.st_size,
            })
    return sorted(records, key=lambda item: item["path"])


def main():
    parser = argparse.ArgumentParser(description="Create a read-only project file inventory.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root")
    parser.add_argument("--include-generated", action="store_true",
                        help="Include common generated/build directories (VCS metadata stays excluded)")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    excludes = VCS_EXCLUDES if args.include_generated else VCS_EXCLUDES | GENERATED_EXCLUDES
    try:
        root = Path(args.root).resolve()
        if not root.is_dir():
            parser.error(f"Not a directory: {root}")
        records = inventory(root, excludes)
    except (OSError, RuntimeError) as error:
        parser.exit(1, f"Inventory failed: {error}\n")

    if args.json:
        print(json.dumps({"root": str(root), "count": len(records), "files": records}, indent=2))
    else:
        print(f"Root: {root}\nFiles: {len(records)}")
        for item in records:
            print(f'{item["path"]}\t{item["bytes"]} bytes')

if __name__ == "__main__":
    main()
