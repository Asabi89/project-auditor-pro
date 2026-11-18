# Architecture Review

## Review dimensions

### Boundaries and responsibilities
- Is each module/file cohesive and purpose-driven?
- Are UI, transport, domain rules, persistence, and infrastructure responsibilities appropriately separated?
- Are controllers/handlers thin enough to remain understandable?
- Are business rules hidden in templates, UI components, ORM hooks, or request handlers?

### Dependency direction
- Identify circular imports/dependencies.
- Identify lower-level modules depending on high-level presentation code.
- Identify shared modules that import application-specific modules.
- Check whether dependency injection is clear or unnecessarily magical.

### Data and API contracts
- Trace data from input to validation, authorization, business logic, persistence, and output.
- Check validation consistency at trust boundaries.
- Check response/error shapes, pagination, versioning, and backward compatibility.
- Check transaction boundaries and consistency guarantees.

### Frontend-specific
- State ownership and state duplication.
- Prop drilling versus justified composition/context/store.
- Component size and responsibility.
- Side-effect lifecycle and cleanup.
- API/data-fetching ownership and cache invalidation.
- Accessibility and semantic HTML.
- Route-level code splitting and loading/error boundaries.

### Backend-specific
- Controller/service/model responsibilities.
- Authorization at object and operation level.
- Transaction and concurrency handling.
- ORM query boundaries and N+1 risks.
- Background job idempotency and retry policy.
- Validation and serialization boundaries.

### Data and infrastructure
- Schema constraints and indexes.
- Migration safety and reversibility.
- Secrets/config separation.
- Container least privilege and immutable builds.
- Health checks, timeouts, resource limits, and observability.

## Anti-patterns to investigate, not assume

- God object/component/service.
- Anemic or over-engineered domain model.
- Service locator abuse.
- Circular dependencies.
- Excessive layers and pass-through wrappers.
- Premature microservices.
- Generic abstractions with many flags.
- Business logic duplicated across client and server.
- Shared mutable state without clear ownership.

## Recommendation standard

For each architecture issue, explain the concrete consequence (change amplification, coupling, test difficulty, security boundary confusion, latency, failure propagation, or developer friction). Recommend the smallest change that addresses that consequence. Include a migration sequence and compatibility considerations.
