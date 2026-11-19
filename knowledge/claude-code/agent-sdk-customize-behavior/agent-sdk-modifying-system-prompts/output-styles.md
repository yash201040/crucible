---
type: "Feature"
title: "Output styles in the SDK"
description: "Saved markdown instruction sets; frontmatter, locations, keep-coding-instructions and how to activate in the SDK."
resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
tags: [output-styles, frontmatter, settings, persona]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [sdk, cli]
requires: ""
identifiers:
  - "keep-coding-instructions"
  - "outputStyle"
  - "/output-style"
  - "/config"
  - "~/.claude/output-styles/"
  - ".claude/output-styles/"
  - "CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT"
  - "settings"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-modifying-system-prompts"
    resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
    title: "Modifying system prompts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Output styles are markdown files (frontmatter plus prompt) that change Claude's role, tone and format. Save to `~/.claude/output-styles/` (user) or `.claude/output-styles/` (project, shareable). A custom style drops the preset's software-engineering instructions unless the frontmatter sets `keep-coding-instructions: true`. Those instructions exist only in the full system prompt, so the setting has no effect on the shorter one; set `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT` to `0` to select the full prompt on any model.

# How to use it

Activate:
- CLI: `/output-style <style>` (needs Claude Code v2.1.269 or later) or `/config`.
- Settings: `outputStyle` in `.claude/settings.local.json`.
- TypeScript SDK: `options = { settings: { outputStyle: "Explanatory" } }`; `outputStyle` is not a top-level `Options` field.
- Python SDK: `settings='{"outputStyle": "Explanatory"}'` or a settings file path.

# Limits and defaults

Output styles load only when `settingSources` includes `'user'` or `'project'`.
