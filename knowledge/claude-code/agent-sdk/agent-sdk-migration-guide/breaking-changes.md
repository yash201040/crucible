---
type: "Guide"
title: "Agent SDK v0.1.0 breaking changes"
description: "ClaudeCodeOptions renamed, minimal system prompt by default, and the settingSources default for isolation."
resource: "https://code.claude.com/docs/en/agent-sdk/migration-guide"
tags: [sdk, breaking-changes, system-prompt, isolation]
kind: "mixed"
maturity: "unlabelled"
since: "0.1.0"
surfaces: [sdk]
requires: ""
identifiers:
  - "ClaudeCodeOptions"
  - "ClaudeAgentOptions"
  - "systemPrompt"
  - "system_prompt"
  - "{ type: \"preset\", preset: \"claude_code\" }"
  - "settingSources"
  - "setting_sources"
  - "~/.claude/settings.json"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-migration-guide"
    resource: "https://code.claude.com/docs/en/agent-sdk/migration-guide"
    title: "Migrate to Claude Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Agent SDK v0.1.0 introduced breaking changes for better isolation and explicit configuration.

# How to use it

- Python type rename: `ClaudeCodeOptions` is now `ClaudeAgentOptions` (e.g. `ClaudeAgentOptions(model="claude-opus-4-7", permission_mode="acceptEdits")`).
- System prompt: before v0.1.0 (v0.0.x) the SDK used Claude Code's system prompt by default; from v0.1.0 it uses a minimal system prompt. To restore the old behaviour pass `systemPrompt: { type: "preset", preset: "claude_code" }` in TypeScript options or `system_prompt={"type": "preset", "preset": "claude_code"}` in Python. A custom string is also accepted (`systemPrompt: "You are a helpful coding assistant"`).
- Settings sources: the default was briefly changed in v0.1.0 to load no filesystem settings and then reverted, so no migration action is needed. Current behaviour: omitting `settingSources` on `query()` loads user, project and local filesystem settings like the CLI (`~/.claude/settings.json`, `.claude/settings.json`, `.claude/settings.local.json`, CLAUDE.md files, custom commands). To run isolated pass `settingSources: []` (Python `setting_sources=[]`).

# Limits and defaults

Isolation matters especially for CI/CD pipelines, deployed applications, test environments and multi-tenant systems, so local customizations do not leak in. Python SDK 0.1.59 and earlier treated an empty list the same as omitting the option, so upgrade before relying on `setting_sources=[]`. Some inputs are read even when `settingSources` is `[]` (see the claude-code-features page section "What settingSources does not control").
