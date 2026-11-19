---
type: "Feature"
title: "Mask credentials with proxy substitution"
description: "Show sandboxed commands a sentinel placeholder while the sandbox proxy swaps in the real credential for allowed hosts; covers env vars, files and AWS SigV4."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, credentials, masking, proxy, tls]
kind: "setting"
maturity: "experimental"
since: "2.1.221"
surfaces: [cli]
requires: "network.tlsTerminate (experimental); user, managed or --settings scope"
identifiers:
  - "\"mode\": \"mask\""
  - "sandbox.network.tlsTerminate"
  - "injectHosts"
  - "sandbox.credentials.allowPlaintextInject"
  - "sandbox.credentials.awsPairs"
  - "sandbox.credentials.sigv4"
  - "extract"
  - "decode"
  - "maskClaims"
  - "onExtractNoMatch"
  - "maskDuplicates"
  - "claude doctor"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With `"mode": "mask"`, sandboxed commands see a per-session placeholder (the sentinel) and the sandbox proxy substitutes the real value on outbound requests to allowed hosts, so the command and its logs never hold the real credential. The page labels `network.tlsTerminate` experimental.

# How to use it

Requirements:
- **TLS termination**: set `network.tlsTerminate` (e.g. `{}`) so the proxy sees request contents. Without it the sentinel reaches the server unchanged and auth fails. `claude doctor` warns `TLS termination is unavailable`.
- **Allowed destination**: each `injectHosts` host must also be reachable via `network.allowedDomains`. A `mask` entry with no `injectHosts` substitutes on every host in `allowedDomains`.
- **Trusted scope**: `mask` entries, `network.tlsTerminate`, `credentials.allowPlaintextInject`, `awsPairs` and `sigv4` are honored only from user settings, managed settings and `--settings`; ignored in a repository's `.claude/settings.json` and `.claude/settings.local.json`. When delivered via server-managed settings they count as settings needing approval.

Example env var masking:
```
"network": {"tlsTerminate": {}, "allowedDomains": ["*.github.com","registry.npmjs.org"]},
"credentials": {"envVars": [ {"name":"GH_TOKEN","mode":"mask","injectHosts":["api.github.com"]}, {"name":"NPM_TOKEN","mode":"mask"} ]}
```

- If a variable is listed with `deny` in any scope, `deny` wins.
- Whole-value replacement by default; for structured values (`DATABASE_URL`, JWT) use `extract`, `decode`, `maskClaims`, `onExtractNoMatch`.
- IPv6: `allowedDomains` uses bracketed form `"[::1]"`; `injectHosts` uses bare compressed form `"::1"` (ports ignored). `claude doctor` warns `Sandbox credential injectHosts entries can never match their destination` (v2.1.229+).
- AWS: mask `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` together so the proxy re-signs SigV4 (v2.1.221+). `AWS_SESSION_TOKEN` is auto-linked; other variable names are grouped with `credentials.awsPairs` (v2.1.224+). Streaming uploads, presigned URLs and SigV4A requests cannot be recomputed and fail if signed with a masked placeholder; `credentials.sigv4` (v2.1.224+) forwards them and AWS rejects them.
- Files (v2.1.221+): `"mode": "mask"` on a `credentials.files` entry. Linux/WSL2: command reads a sentinel copy. macOS: command cannot read the file at all (same as `deny`), even with filesystem isolation disabled. Example: `~/.config/gh/hosts.yml` with `extract` `oauth_token:\\s*(\\S+)`.

# Limits and defaults

- Default `onExtractNoMatch` is `warn`, which skips the entry so the real file is readable unmasked; use `deny` when the secret might be present but the pattern might miss.
- `mask` applies to a single file. Claude Code falls back to `deny` for a directory path, glob, file over 8 MiB, or non-UTF-8 file.
- On macOS, `mask` is applied as `deny` while filesystem isolation is on.
