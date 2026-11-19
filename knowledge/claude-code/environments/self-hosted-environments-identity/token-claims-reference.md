---
type: "Reference"
title: "Session token claims and act chain"
description: "Claims in the self-hosted session JWT, including ccr:* claims, flat duplicates and the RFC 8693 act delegation chain."
resource: "https://code.claude.com/docs/en/self-hosted-environments-identity"
tags: [self-hosted, jwt, claims, identity, act-chain]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "iss"
  - "sub"
  - "aud"
  - "exp"
  - "iat"
  - "jti"
  - "ccr:role"
  - "ccr:session_id"
  - "ccr:pool_id"
  - "ccr:org_id"
  - "ccr:account_id"
  - "account_email"
  - "organization_uuid"
  - "account_uuid"
  - "act"
  - "act.sub"
  - "act.email"
  - "act.attested_by"
  - "--lock-to-account"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-identity"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-identity"
    title: "Verify session identity in self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claims of the session token. Key identity on `act.sub` or `ccr:account_id`, not email: email claims are optional, even for user sessions (a session dispatched from the CLI can lack both). Service-identity sessions carry an `agent:` subject and omit `act.email`, `ccr:account_id`, `account_email`, `account_uuid`. Ignore unrecognized claims. The flat `account_email`, `organization_uuid`, `account_uuid` claims are compatibility duplicates that may be removed.

# How to use it

| Claim | Meaning |
| :- | :- |
| `iss` | Always `ccr` |
| `sub` | `ccr:session:<session_id>` |
| `aud` | Array: always `anthropic-api`, plus your `ccpool_...` environment ID; verify the environment ID |
| `exp`, `iat`, `jti` | Expiry (4 h default, 8 h max), issued-at, unique id |
| `ccr:role` | `session_worker` for session tokens (other roles: environment secrets, runner tokens, work orders, same key set) |
| `ccr:session_id` | `cse_...` form, equals `CLAUDE_CODE_REMOTE_SESSION_ID`; replace `cse_` with `session_` to match `CLAUDE_RUNNER_SESSION_ID` in lifecycle hooks |
| `ccr:pool_id` | Environment ID (same as in `aud`) |
| `ccr:org_id` | Anthropic organization ID |
| `ccr:account_id` | Creator's `user_...` ID; equals `act.sub` without `user:`, `CLAUDE_RUNNER_ACCOUNT_ID` and the `--lock-to-account` value |
| `act` | RFC 8693 delegation chain |

`act` chain: `act.sub` is `user:<id>` or `agent:<id>`; `act.email` optional; `act.attested_by` reserved, expect absent; `act.act.sub` is `ccr:runner:<runner_id>`; `act.act.act.sub` is `ccr:pool:<pool_id>`; `act.act.act.act` is the identity that created the environment secret.
