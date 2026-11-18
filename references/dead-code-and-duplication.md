# Dead Code, Duplication, and Reuse Review

## Dead code: proof before removal

Potential signals:
- No static references or imports.
- Unused exports or package dependencies.
- Unreachable branches or obsolete feature paths.
- Duplicate implementations superseded by a newer path.
- Stale files that are not registered or loaded.

Before marking code dead, check:
- Dynamic imports, lazy routes, reflection, string-based registries.
- Framework conventions (auto-discovered routes, commands, serializers, templates, migrations, plugins).
- Dependency injection containers and configuration-based wiring.
- Event listeners, callbacks, decorators, annotations, signals, scheduled jobs, CLI entry points.
- Public APIs, scripts, build hooks, package exports, external consumers.
- Tests, fixtures, generated code, and code generation inputs.
- Runtime configuration and feature flags.

Classify:
- **Confirmed dead**: no valid entry point or reference after relevant dynamic/framework paths were checked.
- **Likely unused**: static evidence suggests unused but dynamic/runtime paths remain possible.
- **Needs verification**: insufficient evidence or external consumer may exist.

Never delete migrations, public exports, plugin hooks, command handlers, or externally consumed APIs solely because local search finds no references.

## Duplication taxonomy

1. Exact duplication: same statements and behavior.
2. Structural duplication: same algorithm with different names/values.
3. Semantic duplication: independently implemented behavior with the same business meaning.
4. UI duplication: repeated visual/interaction patterns.
5. Accidental similarity: code looks alike but represents different domain rules.

Only the first four are candidates for further evaluation. Similar syntax is not proof of equivalent semantics.

## Reuse decision test

Extract shared code when most are true:
- The behavior has the same meaning and invariants.
- Changes should be coordinated.
- The shared abstraction has a clear owner.
- The API is simpler than maintaining the copies.
- Callers can use it without awkward flags or conditionals.
- Tests can cover shared behavior and caller-specific differences.

Keep code separate when:
- Similarity is superficial.
- Domain rules differ or are likely to evolve independently.
- A shared abstraction requires many boolean flags or mode parameters.
- It would create cross-layer coupling.
- The shared helper would have only one meaningful caller and no clear reuse value.
- The abstraction hides important behavior or makes debugging harder.

## Candidate destinations

| Repeated concern | Possible shared destination |
|---|---|
| Pure deterministic transformation | Utility / domain function |
| Business operation with dependencies | Domain service / application service |
| API transport and request policy | API client / service |
| Reusable stateful UI behavior | Custom hook / composable |
| Repeated UI with meaningful variants | Shared component |
| Form validation rules | Schema / validator |
| Cross-cutting constants | Domain constants/config |
| Repeated database access | Query/service layer, repository only if justified |

## Component extraction checklist

Before extracting a component, verify:
- Same visual and interaction responsibility.
- Accessibility semantics can be preserved.
- Variants are meaningful and limited.
- Props represent real customization, not every internal detail.
- State ownership is clear.
- Styling/theming conventions are consistent.
- Component does not become a dumping ground.

## Required evidence

For each candidate, list all known occurrences, behavior differences, callers, proposed shared API, and regression tests. Do not claim a duplication percentage unless a tool measured it and the measurement scope is stated.
