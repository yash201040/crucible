---
type: "Limit"
title: "What a Bash rule does not match"
description: "Deny and ask Bash rules cover the usual invocation form only; other paths, sh -c and option variants slip past."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, bash, security, limits, sandboxing]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Bash(curl *)"
  - "Bash(rm *)"
  - "Bash(git push *)"
  - "Bash(curl http://github.com/ *)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A Bash rule matches the command text Claude writes after compound splitting and wrapper stripping. It is not a security boundary around a program.

| Rule | Stops | Does not stop |
| :- | :- | :- |
| `Bash(curl *)` | `curl https://example.com` | `/usr/bin/curl https://example.com`, `sh -c 'curl https://example.com'` |
| `Bash(rm *)` | `rm -rf build/` | `/bin/rm -rf build/`, `bash -c 'rm -rf build/'` |
| `Bash(git push *)` | `git push origin main` | `git -C . push origin main`, `git -c push.default=current push origin main` |

# How to use it

- For filesystem and network enforcement independent of command text use sandboxing; to inspect full command text use a PreToolUse hook.
- Argument-constraining patterns are fragile: `Bash(curl http://github.com/ *)` misses `curl -X GET http://github.com/...`, https, redirects (`curl -L`), and `URL=... && curl $URL`.
- More reliable URL filtering: deny `curl`/`wget` and allow `WebFetch(domain:github.com)` (pair with the sandbox network allowlist since deny does not match by path or inside `sh -c`); use a PreToolUse hook that validates URLs; add `CLAUDE.md` guidance (shapes behavior, enforces nothing).

# Notes

WebFetch rules alone do not prevent network access: if Bash is allowed Claude can still use `curl` or `wget`.
