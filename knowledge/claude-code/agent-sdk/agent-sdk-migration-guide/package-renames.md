---
type: "Guide"
title: "Claude Code SDK to Agent SDK package migration"
description: "The Claude Code SDK became the Claude Agent SDK; package names, install steps and import changes for TypeScript and Python."
resource: "https://code.claude.com/docs/en/agent-sdk/migration-guide"
tags: [sdk, migration, packages, rename]
kind: "mixed"
maturity: "unlabelled"
since: "0.1.0"
surfaces: [sdk]
requires: ""
identifiers:
  - "@anthropic-ai/claude-code"
  - "@anthropic-ai/claude-agent-sdk"
  - "claude-code-sdk"
  - "claude-agent-sdk"
  - "claude_code_sdk"
  - "claude_agent_sdk"
  - "npm uninstall @anthropic-ai/claude-code"
  - "npm install @anthropic-ai/claude-agent-sdk"
  - "pip uninstall -y claude-code-sdk"
  - "pip install claude-agent-sdk"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-migration-guide"
    resource: "https://code.claude.com/docs/en/agent-sdk/migration-guide"
    title: "Migrate to Claude Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Claude Code SDK was renamed the Claude Agent SDK and its documentation moved to a dedicated Agent SDK section. A separate cookbook recipe covers migrating from the OpenAI Agents SDK.

# How to use it

| Aspect | Old | New |
| - | - | - |
| TS/JS package | `@anthropic-ai/claude-code` | `@anthropic-ai/claude-agent-sdk` |
| Python package | `claude-code-sdk` | `claude-agent-sdk` |

TypeScript: `npm uninstall @anthropic-ai/claude-code`, `npm install @anthropic-ai/claude-agent-sdk`, change imports (`query`, `tool`, `createSdkMcpServer` now come from `@anthropic-ai/claude-agent-sdk`), and update `package.json` including the version range (example: `"^0.0.42"` to `"^0.3.0"`).

Python: `pip uninstall -y claude-code-sdk` (the warning `Skipping claude-code-sdk as it is not installed.` is expected), `pip install claude-agent-sdk`, replace it in `requirements.txt` or `pyproject.toml`, and change imports from `claude_code_sdk` to `claude_agent_sdk`.

# Notes

Then review the [breaking changes](./breaking-changes.md).
