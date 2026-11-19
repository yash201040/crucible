---
type: "Reference"
title: "Sandbox credential protection and masking"
description: "sandbox.credentials files and envVars with deny or mask modes, mask fields (extract, decode jwt, maskClaims, injectHosts), AWS SigV4 pairing and sigv4 handling."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [sandbox, credentials, secrets, masking]
kind: "setting"
maturity: "unlabelled"
since: "2.1.221"
surfaces: [cli]
requires: "mask v2.1.221; extract/decode on env vars, jwt, awsPairs and sigv4 v2.1.224; mask needs sandbox.network.tlsTerminate"
identifiers:
  - "sandbox.credentials"
  - "sandbox.credentials.files"
  - "sandbox.credentials.envVars"
  - "sandbox.credentials.allowPlaintextInject"
  - "sandbox.credentials.awsPairs"
  - "sandbox.credentials.sigv4"
  - "sandbox.credentials.sigv4.streaming"
  - "sandbox.credentials.sigv4.presigned"
  - "sandbox.credentials.sigv4.sigv4a"
  - "mode"
  - "injectHosts"
  - "extract"
  - "onExtractNoMatch"
  - "decode"
  - "maskClaims"
  - "maskDuplicates"
  - "accessKeyIdVar"
  - "secretAccessKeyVar"
  - "sessionTokenVar"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Declares credential files and environment variables to protect from sandboxed commands. Each entry has a `path` (files) or `name` (variables) and a `mode`: `deny` hides it; `mask` shows a placeholder (sentinel) while the sandbox proxy substitutes the real value on outbound requests. There is no built-in credential deny list; only listed entries are protected. Scope `Any file`, but `mask` entries, `allowPlaintextInject`, `awsPairs` and `sigv4` are honored only from user settings, managed settings and `--settings`; `mask` entries are dropped from project and local settings.

# How to use it

| Key | Type | Default | What it does |
| :- | :- | :- | :- |
| `credentials.files` | array of `{path, mode, ...mask fields}` | unset | `deny` blocks reads (like `denyRead`). `mask` on Linux/WSL2 gives a sentinel copy; on macOS the file is unreadable instead. One file per entry |
| `credentials.envVars` | array of `{name, mode, ...}` | unset | `deny` removes the variable; `mask` gives a per-session sentinel. `name` starts with a letter or underscore, letters/digits/underscores. Same variable with both modes applies `deny` |
| `credentials.allowPlaintextInject` | Boolean | `false` | Allow mask substitution on plain HTTP, not just TLS-terminated HTTPS; cleartext, use only on trusted test networks |
| `credentials.awsPairs` | array of `{accessKeyIdVar, secretAccessKeyVar, sessionTokenVar?}` | unset (conventional `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN` trio paired automatically) | Link custom-named masked variables for SigV4 re-signing; each must be a whole-value `mask` entry without `extract`/`decode`, one slot only; proxy re-signs on the access-key entry's `injectHosts`; naming a conventional variable replaces automatic pairing |
| `credentials.sigv4` | object with `streaming`, `presigned`, `sigv4a` each `"deny"` or `"passthrough"` | all `"deny"` | What the proxy does with AWS forms it cannot re-sign (aws-chunked uploads, presigned URLs, SigV4A); `passthrough` forwards with the placeholder signature so AWS rejects it |

Mask fields:

| Field | Files | Env vars | What it does |
| :- | :- | :- | :- |
| `extract` | yes (v2.1.221) | yes (v2.1.224), not with `decode` | Regex with at least one capture group; masks group 1 only |
| `onExtractNoMatch` | `"warn"` (default), `"deny"`, `"error"` | same; only `"warn"` with `decode` | Outcome when nothing matched: warn leaves as-is, deny makes unreadable/unset, error stops sandbox setup. `deny` becomes `error` where the read block is not enforced |
| `decode` | `"jwt"` (v2.1.224) | `"jwt"` (v2.1.224) | Verify JWTs and replace with a structurally valid fake token |
| `maskClaims` | array, requires `decode` | same | Mask only named top-level payload claims |
| `maskDuplicates` | Boolean, default `false` | n/a | Also replace verbatim copies elsewhere in the file; only with `extract` or `decode`; raw substring match, use for long high-entropy secrets |
| `injectHosts` | array of hosts also in `allowedDomains` | same | Hosts where the proxy substitutes; unset means every `allowedDomains` host. IPv6 as bare compressed address, e.g. `"::1"` |

```json
{ "sandbox": { "credentials": { "envVars": [ { "name": "GITHUB_TOKEN", "mode": "mask", "injectHosts": ["api.github.com"] } ] } } }
```

# Limits and defaults

- `mask` substitution runs only through the proxy: set `sandbox.network.tlsTerminate`, or `allowPlaintextInject` for plain HTTP.
- With filesystem isolation disabled, `files` `deny` is not applied; env var protection still is. On macOS with isolation on, a `mask` file entry is applied as `deny` before `extract`/`decode`.
- Invalid managed entries: one with a valid `path`/`name` and a mode of `mask` or `deny` but a bad `extract` (e.g. no capture group) is degraded to `deny` with a warning (a degraded `files` entry pins `filesystem.disabled` like an explicit deny); entries with an unknown `mode` or invalid `path`/`name` are stripped; remaining valid entries still apply. Applies in v2.1.191 and later (before v2.1.221 every invalid entry was stripped).
- Mask fields on a `deny` entry are accepted but ignored.
