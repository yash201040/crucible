---
type: "Reference"
title: "Plugin relevance block and signals"
description: "The relevance object in a marketplace entry, its signal fields with limits and matching rules, and validation."
resource: "https://code.claude.com/docs/en/plugins/relevance"
tags: [plugins, relevance, suggestions, marketplace, signals]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "relevance"
  - "relevance.topic"
  - "relevance.signals"
  - "cwd"
  - "cli"
  - "hosts"
  - "filesRead"
  - "manifestDeps"
  - "claude plugin validate"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-relevance"
    resource: "https://code.claude.com/docs/en/plugins/relevance"
    title: "Recommend plugins for your org"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A marketplace operator adds a `relevance` object to a plugin entry in `marketplace.json`; Claude Code suggests the plugin when the session matches a signal. Matching is local, adds no network traffic, and matched signals are not reported to Anthropic or the operator. Claude Code never installs automatically.

# How to use it

`relevance.topic`: optional string, at most 64 chars, fills "Working with *topic*?"; defaults to the plugin name capitalized per hyphen segment. `relevance.signals`: at least one must be set.

| Signal | Type | Matches | Limit |
|---|---|---|---|
| `cwd` | string[] globs | session working directory (absolute, and relative to git root); directory and everything under it; only signal that can match at session start | 10 patterns x 256 chars |
| `cli` | string[] | command name of shell commands Claude ran (first token after env assignments and `sudo`; compound commands record only the leading command), exact | 10 x 64 |
| `hosts` | string[] | hostnames in `http(s)://` URLs in Bash commands; bare lowercase hostname, case-insensitive exact | 20 x 128 |
| `filesRead` | string[] globs | paths of files Claude read (also written/edited files and auto-loaded `CLAUDE.md`); forward-slash normalized, case-insensitive | 10 x 256 |
| `manifestDeps` | objects `{file, pattern}` | JS regex `file` (case-insensitive on path) and `pattern` (case-sensitive on contents) in manifests Claude read | 10 entries, each value 256 chars; manifests over 512 KB skipped |

Example: `"relevance": {"topic": "Terraform", "signals": {"cli": ["terraform"], "filesRead": ["**/*.tf"]}}`.

# Limits and defaults

Unknown fields under `relevance` and `relevance.signals` are ignored at load time (older clients still load). A recognized field exceeding its limit invalidates the whole plugin entry so it cannot be installed. `claude plugin validate ./my-marketplace` warns on unknown keys, flags non-object `relevance`, rejects `signals.hosts` entries with scheme, port or path; output ends `Validation passed`, `Validation passed with warnings` or `Validation failed`.
