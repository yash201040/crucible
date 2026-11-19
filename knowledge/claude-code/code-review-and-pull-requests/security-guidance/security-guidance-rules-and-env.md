---
type: "Reference"
title: "Security guidance custom rules and switches"
description: "Add reviewer guidance and per-edit patterns via .claude files and toggle layers or models with ENABLE_* and SECURITY_REVIEW_MODEL variables."
resource: "https://code.claude.com/docs/en/security-guidance"
tags: [security, plugin, env-vars, custom-rules]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "security-guidance plugin"
identifiers:
  - "ENABLE_PATTERN_RULES"
  - "ENABLE_STOP_REVIEW"
  - "ENABLE_COMMIT_REVIEW"
  - "ENABLE_CODE_SECURITY_REVIEW"
  - "SECURITY_GUIDANCE_DISABLE"
  - "SECURITY_REVIEW_MODEL"
  - "SG_AGENTIC_MODEL"
  - ".claude/claude-security-guidance.md"
  - ".claude/claude-security-guidance.local.md"
  - "~/.claude/claude-security-guidance.md"
  - ".claude/security-patterns.yaml"
  - ".claude/security-patterns.yml"
  - ".claude/security-patterns.json"
  - "rule_name"
  - "reminder"
  - "regex"
  - "substrings"
  - "paths"
  - "exclude_paths"
  - "/plugin disable security-guidance@claude-plugins-official"
  - "/plugin uninstall security-guidance@claude-plugins-official"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "security-guidance"
    resource: "https://code.claude.com/docs/en/security-guidance"
    title: "Catch security issues as Claude writes code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two additive extension points (you cannot disable built-in checks via them): a Markdown guidance file for model-backed reviews (threat model and checklist in plain language; guidance only, not guardrails; a rule to ignore a class does not suppress findings; for hard enforcement pair with a blocking hook or CI), and a patterns file for the per-edit match.

# How to use it

| Variable | Effect |
| :- | :- |
| `ENABLE_PATTERN_RULES=0` | Disable per-edit pattern check |
| `ENABLE_STOP_REVIEW=0` | Disable end-of-turn review |
| `ENABLE_COMMIT_REVIEW=0` | Disable commit and push review |
| `ENABLE_CODE_SECURITY_REVIEW=0` | Disable all model-backed reviews |
| `SECURITY_GUIDANCE_DISABLE=1` | Disable plugin without uninstalling |
| `SECURITY_REVIEW_MODEL` | Model for end-of-turn review (default Claude Opus) |
| `SG_AGENTIC_MODEL` | Model for commit review (default Claude Opus) |

`security-patterns.yaml` schema: `patterns:` list of `rule_name` (identifier shown), `reminder` (warning text, capped at 1 KB), `regex` (Python regex) or `substrings` (list), optional `paths` and `exclude_paths` (globs on the full file path, prefix project-relative with `**/`). Also read as `.yml` and `.json` (same schema; YAML needs PyYAML importable, JSON works anywhere).

# Limits and defaults

Lookup locations for both file types, all loaded and concatenated: user `~/.claude/claude-security-guidance.md`, project `.claude/claude-security-guidance.md`, project local `.claude/claude-security-guidance.local.md` (gitignore it). Combined cap 8 KB for the guidance file. Up to 50 custom rules; regexes prone to catastrophic backtracking are skipped. Admins can push the user-scope file through device management.

# Notes

Pause or remove: `/plugin disable security-guidance@claude-plugins-official`, `/plugin uninstall ...`. If enabled via project `.claude/settings.json`, uninstalling writes an override to `.claude/settings.local.json` (or offers removing it for everyone); if enabled via managed settings, disable and uninstall are refused.
