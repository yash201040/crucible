---
type: "Feature"
title: "Verify the session access token"
description: "Every self-hosted session gets an ES256 JWT in CLAUDE_CODE_SESSION_ACCESS_TOKEN; services verify it against Anthropic's JWKS."
resource: "https://code.claude.com/docs/en/self-hosted-environments-identity"
tags: [self-hosted, jwt, identity, verification, security]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: "Team or Enterprise plan"
identifiers:
  - "CLAUDE_CODE_SESSION_ACCESS_TOKEN"
  - "https://api.anthropic.com/v1/code/.well-known/jwks.json"
  - "self-hosted-runner decode-token"
  - "--no-verify"
  - "CLAUDE_RUNNER_CLAUDE_BIN"
  - "CCR_SESSION_ACCOUNT_EMAIL"
  - "CLAUDE_RUNNER_ACCOUNT_EMAIL"
  - "CLAUDE_RUNNER_ACCOUNT_ID"
  - "CLAUDE_CODE_REMOTE_SESSION_ID"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-identity"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-identity"
    title: "Verify session identity in self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The token lets internal services confirm a request came from a session in your environment and identify who or what created it. It proves Anthropic issued it for a specific session and environment, and whether a user or the organization's service identity (as for Claude Tag channel sessions) created it. It does not prove which process presents it: any code or MCP server in the session can read the variable.

# How to use it

Format: `sk-ant-cc-<header>.<payload>.<signature>`; strip the prefix before a JWT library. `sk-ant-si-` tokens are Anthropic-hosted sessions with a different key set; reject them. Algorithm `ES256` (P-256, SHA-256), `kid` in header.

Service-side checks in order:

1. Prefix is `sk-ant-cc-`.
2. Verify signature with the JWKS at the URL above (public, `Cache-Control: public, max-age=300`; do not pin one key; refetch once on an unknown `kid`; reject `alg` other than `ES256`).
3. `iss` is exactly `ccr`.
4. `aud` array contains your environment ID (`ccpool_...`).
5. `ccr:role` is exactly `session_worker`.
6. `exp` not in the past.
7. Read identity from `act`.

Examples given in Node.js (`jose`) and Python (`PyJWT`). Inside a wrapper script: `"$CLAUDE_RUNNER_CLAUDE_BIN" self-hosted-runner decode-token | jq -re '.act.email // .act.sub'`. `decode-token` reads the token from an argument, `CLAUDE_CODE_SESSION_ACCESS_TOKEN`, or stdin (in that order), checks signature and expiry only (not `iss`, `aud`, role), exits 1 on failure; `--no-verify` is for offline inspection only. Use `jq -re` so a missing claim fails.

# Limits and defaults

- Lifetime: four hours default, eight hours maximum; the runner refreshes and pushes new tokens, so one session presents several valid tokens.
- Verification is offline and there is no revocation feed: a verified token stays valid until `exp`. Scope derived credentials to one coding session, bound them to `exp` or shorter, and audit by `ccr:session_id` and `jti`.
- Plain env vars: spawn-runner hook gets `CLAUDE_RUNNER_ACCOUNT_EMAIL`/`CLAUDE_RUNNER_ACCOUNT_ID` from the unverified work order; wrappers get `CCR_SESSION_ACCOUNT_EMAIL` (unverified, labelling only, not for auth).
