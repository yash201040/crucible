---
type: "Reference"
title: "Glob, WebFetch and WebSearch tool variables"
description: "Variables that tune Glob and Grep behavior and timeouts, disable WebFetch, set its cache and deadline, and cap and refill WebSearch calls."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [glob, webfetch, websearch, limits]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_GLOB_HIDDEN"
  - "CLAUDE_CODE_GLOB_NO_IGNORE"
  - "CLAUDE_CODE_GLOB_TIMEOUT_SECONDS"
  - "USE_BUILTIN_RIPGREP"
  - "CLAUDE_CODE_DISABLE_WEB_FETCH"
  - "CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS"
  - "CLAUDE_CODE_WEBFETCH_DEADLINE_MS"
  - "CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION"
  - "CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Search and web tool limits.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_GLOB_HIDDEN` | `false` excludes dotfiles from Glob results (included by default). Does not affect `@` autocomplete, `ls`, Grep or Read. |
| `CLAUDE_CODE_GLOB_NO_IGNORE` | `false` makes Glob respect `.gitignore` (default returns gitignored files too). `@` autocomplete uses the `respectGitignore` setting. |
| `CLAUDE_CODE_GLOB_TIMEOUT_SECONDS` | Timeout for Glob and Grep searches; 20 s on most platforms, 60 s on WSL. |
| `USE_BUILTIN_RIPGREP` | `0` uses system `rg` instead of the bundled one. |
| `CLAUDE_CODE_DISABLE_WEB_FETCH` | `1` turns off WebFetch; WebSearch stays. Requires v2.1.285+. |
| `CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS` | How long WebFetch caches each URL (default `900000`, 15 min); plain digits only (`0` or others keep the default); read once per launch. Requires v2.1.233+. |
| `CLAUDE_CODE_WEBFETCH_DEADLINE_MS` | Upper bound on a WebFetch page download including redirects (default `300000`, five minutes); `0` removes it; plain digits only. Requires v2.1.268+. |
| `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` | Cap on WebSearch calls (default 200); at the cap further calls return a notice to continue with gathered information. Positive whole number, no upper bound; other values ignored, so it can be raised but not removed. Requires v2.1.212+. |
| `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR` | Refill rate of the WebSearch limit in calls per hour: default `100` in interactive terminal sessions, `0` (refill off) in non-interactive sessions. Plain digits only. Requires v2.1.290+. |
