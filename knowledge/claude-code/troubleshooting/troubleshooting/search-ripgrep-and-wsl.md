---
type: "Guide"
title: "Search and file discovery problems"
description: "Using system ripgrep via USE_BUILTIN_RIPGREP=0 and mitigating slow or incomplete search on WSL."
resource: "https://code.claude.com/docs/en/troubleshooting"
tags: [search, ripgrep, wsl, env-var]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "USE_BUILTIN_RIPGREP"
  - "claude doctor"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "troubleshooting"
    resource: "https://code.claude.com/docs/en/troubleshooting"
    title: "Troubleshooting"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

If the Search tool, `@file` mentions, custom agents or custom skills do not find files, the bundled `ripgrep` binary may not run on the system.

# How to use it

Install the platform ripgrep (`brew install ripgrep`, `sudo apt install ripgrep`, `apk add ripgrep`, `pacman -S ripgrep`, `winget install BurntSushi.ripgrep.MSVC`) and set `USE_BUILTIN_RIPGREP` to `0` in the shell or in the `env` block of `settings.json`:

```json
{ "env": { "USE_BUILTIN_RIPGREP": "0" } }
```

Confirm with `claude doctor`: the Search line should show the system ripgrep path instead of `OK (bundled)`.

# Limits and defaults

On WSL, cross-filesystem disk read penalties can yield fewer matches than expected while `claude doctor` still shows Search as OK. Mitigations: more specific searches, keep the project on the Linux filesystem (`/home/`) not `/mnt/c/`, or run natively on Windows.
