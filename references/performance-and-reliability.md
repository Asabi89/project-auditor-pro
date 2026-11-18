# Performance and Reliability Review

## Performance
- Database: N+1, full table scans, missing/unused indexes, unbounded result sets, inefficient joins, repeated serialization.
- Network: duplicate requests, chatty APIs, missing timeouts, oversized payloads, retry storms.
- Frontend: unnecessary renders, expensive derived state, memory leaks, large bundles, blocking main-thread work, unoptimized assets.
- Backend: synchronous work in request paths, unbounded concurrency, inefficient algorithms, resource leaks.
- Caching: stale data, missing invalidation, cache stampedes, sensitive data cached across users.

## Reliability
- Clear error boundaries and actionable errors.
- Timeouts, bounded retries, exponential backoff and jitter where appropriate.
- Idempotency for retried operations.
- Transaction boundaries and rollback behavior.
- Race conditions and concurrency limits.
- Queue visibility, dead-letter handling, and job idempotency.
- Resource cleanup and graceful shutdown.
- Logging without secrets or unnecessary personal data.
- Health checks, metrics, tracing, and alertability.

## Evidence
Prefer measurements, query plans, profiler output, bundle reports, load-test evidence, or a clearly reproducible code path. Label unmeasured risks as hypotheses and propose a measurement plan rather than claiming a measured regression.
