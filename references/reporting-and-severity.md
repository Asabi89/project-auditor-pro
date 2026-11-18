# Reporting, Evidence, and Severity

## Evidence quality
- **Confirmed**: directly demonstrated by code/configuration or safe reproducible test.
- **Likely**: strong evidence, but runtime/configuration context is incomplete.
- **Needs verification**: plausible concern requiring missing context or a safe test.

## Severity
- **CRITICAL**: severe compromise with realistic reachability and broad impact.
- **HIGH**: significant exploitable risk or major integrity/availability/maintainability concern.
- **MEDIUM**: meaningful risk with limited scope or prerequisites.
- **LOW**: localized issue with low impact.
- **INFO**: optional improvement or observation.

Do not inflate severity. State the reasoning and assumptions.

## Finding IDs
Use stable prefixes:
- SEC — security
- DEAD — dead code
- DUP — duplication/reuse
- ARCH — architecture
- PERF — performance
- REL — reliability
- DEP — dependencies
- TEST — testing
- DOC — documentation

Do not renumber IDs during follow-up reports; mark resolved status instead.

## Good finding
A useful finding is specific, reproducible, actionable, and proportionate. Avoid generic statements such as "improve security" or "clean up architecture."

## Coverage
Every audit report must disclose:
- Total discovered files (if measurable).
- Reviewed source/config files.
- Excluded files and why.
- Files not reviewed and why.
- Commands run and not run.
- Limitations (no runtime credentials, no production access, no external scan permission, etc.).
