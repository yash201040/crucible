---
type: "Guide"
title: "System prompt starting points"
description: "Minimal default, the claude_code preset, or a custom string, and how to decide between them."
resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
tags: [system-prompt, preset, claude-code-preset, defaults]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "systemPrompt"
  - "system_prompt"
  - "claude_code"
  - "preset"
  - "append"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-modifying-system-prompts"
    resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
    title: "Modifying system prompts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three starting points:
- Minimal default (no `systemPrompt`/`system_prompt`): covers tool calling only and omits the `claude_code` preset's security and safety instructions. This differs from `claude -p`, which uses the Claude Code system prompt by default.
- `claude_code` preset: `systemPrompt: { type: "preset", preset: "claude_code" }` (Python `system_prompt={"type": "preset", "preset": "claude_code"}`), optionally with `append`.
- Custom string: the SDK sends only what you provide.

# How to use it

| Building | Use |
| :- | :- |
| CLI or IDE-like coding tool, human steering | `claude_code` preset |
| Same plus product rules | preset with `append` (lowest-risk) |
| Different surface, identity or permission model, or non-coding agent | Custom string; you replace tool guidance and safety instructions |
| Thin tool-calling loop | No `systemPrompt` |

"Different" means: different surface (output not read in a terminal by the person who triggered it), different identity, different permission model (autonomous or narrow resources), or non-coding tasks. Unattended coding automation such as a CI lint-fix or diff-review job still fits the preset.
