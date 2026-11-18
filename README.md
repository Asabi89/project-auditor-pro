# PROJECT AUDITOR PRO

Universal Agent Skills-compatible skill for exhaustive codebase review and approval-gated remediation.

## Install

Copy the `project-auditor-pro` directory into the agent's skills directory, for example:

- Repository-local: `.agents/skills/project-auditor-pro/`
- User-level: `~/.agents/skills/project-auditor-pro/`

The exact discovery path can vary by agent. Keep the directory name aligned with the `name` in `SKILL.md`.

## Use

Ask your coding agent:

> Use project-auditor-pro to audit this repository exhaustively, file by file. Do not modify anything yet. Produce the coverage ledger, findings, and prioritized remediation batches.

After reviewing the report, approve a specific batch:

> I approve remediation batch 1 only. Implement it incrementally, preserve unrelated changes, and run the stated validation.

## Contents

- `SKILL.md`: core instructions and mandatory workflow.
- `references/`: specialist review playbooks.
- `templates/`: consistent report and finding formats.
- `scripts/inventory.py`: read-only file inventory helper.

## Inventory helper

Run with Python 3 (standard library only), passing the root of the project to audit:

    python scripts/inventory.py /path/to/project --json

Omit the root to inspect the current directory. Omit `--json` for a text listing.
Use `--include-generated` to include common generated and dependency directories.
Version-control metadata and symbolic links or Windows reparse points inside the
project are always skipped. Record relevant exclusions separately in the audit ledger.

## Safety model

Audit first; no edits before explicit approval. The helper script only lists files and sizes. Security scanners and external services are optional and must respect repository privacy and user authorization.

## Limitations

Static review cannot prove the absence of vulnerabilities or runtime defects. Dynamic behavior, deployment configuration, permissions, production infrastructure, and external consumers may require separate authorized verification.
