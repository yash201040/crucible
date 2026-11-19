---
type: "Feature"
title: "Disable filesystem isolation"
description: "sandbox.filesystem.disabled turns off the filesystem layer while keeping network isolation, with which settings sources may set it and what stops being enforced."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, filesystem, network, risk]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "sandbox.filesystem.disabled"
  - "sandbox.network.allowedDomains"
  - "CLAUDE_CODE_SUBPROCESS_ENV_SCRUB"
  - "sandbox.credentials"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The sandbox has two independent layers: filesystem isolation and network isolation. Setting `sandbox.filesystem.disabled` to `true` (default `false`) skips filesystem isolation: sandboxed commands get unrestricted read/write of the host filesystem while network egress stays limited to allowed domains.

# How to use it

```
{ "sandbox": { "enabled": true,
  "filesystem": { "disabled": true },
  "network": { "allowedDomains": ["github.com", "*.npmjs.org"] } } }
```

Which sources can set it:
- User settings, managed settings and `--settings` can. Project `.claude/settings.json` and `.claude/settings.local.json` cannot.
- When managed settings configure `sandbox.filesystem` at all, or list any `sandbox.credentials.files` entry with `"mode": "deny"`, only managed settings can set the key.
- When `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set, the key is ignored from every source, managed included.
- A valid `mask` entry does not lock the key, even if it falls back to `deny` at startup; list an unmaskable path (such as a credential directory) as explicit `deny` in managed settings to lock it.

What changes when off:

| Protection | With filesystem isolation off |
| - | - |
| `filesystem.denyRead` and `credentials.files` deny blocks | Not enforced |
| `credentials.envVars` deny and mask | Enforced |
| `credentials.files` mask entries applied as masks | Enforced; an entry that fell back to `deny` is not |

Protected paths protection is also lifted. Sandboxed commands inherit your shell's `$TMPDIR`.

# Notes

Warning from the docs: with filesystem isolation off and commands auto-allowed, a command can write files later run or read (shell startup files, executables on `$PATH`, `~/.claude/settings.json`) to widen its access. `allowManagedDomainsOnly` narrows but does not remove the risk.
