# Tooling by Ecosystem

Use only tools already installed or explicitly approved. First inspect package scripts and project conventions. Prefer lockfile-aware commands. Do not blindly update dependencies.

## General
- Git: status, diff, log, blame where useful.
- Format/lint/type-check commands already defined by the repository.
- Existing unit, integration, and end-to-end tests.
- Secret scanning and SAST where available.
- Dependency audit tools appropriate to the lockfile.
- `scripts/inventory.py` for a basic read-only file inventory.

## JavaScript / TypeScript
- Inspect `package.json`, lockfile, `tsconfig`, ESLint, test and build configuration.
- Possible checks if installed: `npm audit`, `pnpm audit`, `yarn npm audit`, ESLint, TypeScript compiler, Vitest/Jest, Playwright, Semgrep.
- Duplication tools such as jscpd may help; verify results manually.
- Review `eval`, unsafe DOM sinks, `dangerouslySetInnerHTML`, URL handling, auth/session storage, dependency scripts, and server/client boundaries.

## Python
- Inspect `pyproject.toml`, requirements files, lockfiles, Django/FastAPI/Flask settings.
- Possible checks if installed: `pip-audit`, `bandit`, `ruff`, `mypy`/`pyright`, pytest, Semgrep.
- Review ORM raw SQL, template escaping, deserialization, subprocess use, debug settings, CSRF, CORS, permissions, and upload handling.

## PHP
- Inspect Composer manifests/lockfiles, framework config, routes, middleware, migrations.
- Possible checks if installed: Composer audit, PHPStan/Psalm, PHP_CodeSniffer, PHPUnit, Semgrep.
- Review prepared statements, output escaping, CSRF, file uploads, serialization, and authorization.

## Java / Kotlin
- Inspect Maven/Gradle manifests and dependency locks.
- Possible checks if installed: OWASP Dependency-Check, SpotBugs, Semgrep, Checkstyle, tests.
- Review deserialization, expression language, authorization annotations, secrets, and dependency injection.

## Rust
- Inspect Cargo.toml/Cargo.lock, features, unsafe blocks, FFI, and error handling.
- Possible checks if installed: `cargo audit`, `cargo deny`, Clippy, tests.
- Review unsafe code, panic boundaries, input parsing, cryptography use, and dependency features.

## Go
- Inspect go.mod/go.sum, modules, handlers, middleware, goroutines.
- Possible checks if installed: `govulncheck`, `staticcheck`, `gosec`, `go test`, `go vet`.
- Review context cancellation, race conditions, SQL construction, HTTP timeouts, and auth middleware.

## Containers / IaC / CI
- Inspect Dockerfiles, compose files, Kubernetes manifests, Terraform, workflow files, and deployment scripts.
- Possible checks if installed: Trivy, Checkov, Hadolint, actionlint, kube-linter.
- Review least privilege, pinned images/actions, secret handling, exposed ports, writable filesystems, network policy, and CI token permissions.

Tool output is evidence to investigate, not an unquestionable verdict. Record exact command, scope, exit status, and limitations.
