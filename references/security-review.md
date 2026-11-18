# Application Security Review

## Method

1. Identify assets: accounts, personal data, credentials, payment data, business records, tokens, source artifacts.
2. Identify actors and trust boundaries: anonymous users, authenticated users, roles, administrators, services, third parties, queues, browser, database, filesystem, cloud.
3. Map entry points: routes, APIs, forms, uploads, webhooks, CLI, jobs, message consumers, admin interfaces.
4. Trace untrusted input to sensitive sinks.
5. Review authentication, authorization, data exposure, cryptography, configuration, dependencies, and operational controls.
6. Verify findings with safe static evidence or local tests. Do not exploit production systems.

## Common vulnerability classes

### Identity and access control
- Missing server-side authorization.
- IDOR/BOLA and tenant isolation failures.
- Role/permission confusion and privilege escalation.
- Weak password hashing or credential reset.
- Session fixation, insecure cookies, token leakage, poor revocation.
- Missing MFA where risk requires it.

### Injection and output handling
- SQL/NoSQL/ORM injection.
- OS command injection.
- XSS (stored, reflected, DOM).
- Template injection.
- LDAP, XPath, header, and log injection.
- Unsafe deserialization and expression evaluation.

### Request and network security
- CSRF on state-changing requests.
- SSRF, open redirects, path traversal.
- CORS misconfiguration (CORS is not authentication).
- Missing rate limits and abuse controls.
- Webhook signature/replay validation.
- DNS/IP validation and redirect handling for outbound requests.

### Data handling
- Excessive data exposure and mass assignment.
- Sensitive data in logs, analytics, URLs, or error messages.
- Weak encryption or incorrect key management.
- Insecure file upload/type validation/storage.
- Missing retention/deletion controls where applicable.

### Platform/configuration
- Hardcoded or committed secrets.
- Debug mode, verbose errors, permissive defaults.
- Missing/weak security headers and TLS assumptions.
- Insecure Docker, CI/CD, cloud IAM, storage ACLs.
- Unsafe dependency versions and abandoned packages.

## Verification rules

- Check whether the vulnerable path is reachable and under what conditions.
- Check whether input is attacker-controlled.
- Trace sanitization/parameterization and authorization to the actual sink.
- Distinguish a scanner alert from a verified vulnerability.
- Never print secret values. Report file, variable/key name, and a redacted sample only.
- Do not include weaponized payloads or instructions to attack third-party targets.
- Do not send proprietary code or secrets to external services without explicit permission.
- Do not run destructive or state-changing tests against production.

## Security finding format

Include:
- Asset and trust boundary.
- Entry point and affected sink.
- Required attacker capability.
- Missing/ineffective control.
- Impact: confidentiality, integrity, availability, or privilege.
- Reachability and confidence.
- Safe verification evidence.
- Remediation and regression test.

## Severity guidance

Critical: remotely reachable compromise of core system/data, authentication bypass with broad impact, or equivalent severe issue.
High: exploitable access-control flaw, injection with meaningful impact, secret exposure, or major data compromise.
Medium: meaningful exploit requiring constraints, limited exposure, or security control weakness with realistic impact.
Low: defense-in-depth weakness or limited-impact issue.
Info: hardening recommendation without demonstrated vulnerability.

Severity depends on reachability, exploit prerequisites, asset value, and blast radius. Do not assign severity based only on a scanner label.

## Useful references

Use current versions when browsing is permitted:
- OWASP Top 10
- OWASP Application Security Verification Standard (ASVS)
- OWASP API Security Top 10
- OWASP Cheat Sheet Series
- CWE and ecosystem security advisories
