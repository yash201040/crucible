---
type: "Guide"
title: "Install the Agent SDK and its bundled binary"
description: "Prerequisites and install commands for the TypeScript and Python Agent SDKs, and when no native Claude Code binary is bundled."
resource: "https://code.claude.com/docs/en/agent-sdk/quickstart"
tags: [agent-sdk, install, binary, python, typescript]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "Node.js 18.14+ or Python 3.10+; an Anthropic account"
identifiers:
  - "@anthropic-ai/claude-agent-sdk"
  - "claude-agent-sdk"
  - "pathToClaudeCodeExecutable"
  - "npm ci --omit=optional"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-quickstart"
    resource: "https://code.claude.com/docs/en/agent-sdk/quickstart"
    title: "Quickstart"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Agent SDK is installed as an npm package (TypeScript) or a pip/uv package (Python). Both bundle a native Claude Code binary, so most installs need no separate Claude Code install.

# How to use it

| Setup | Commands |
| - | - |
| TypeScript, new project | `npm init -y`, `npm pkg set type=module`, `npm install @anthropic-ai/claude-agent-sdk`, `npm install --save-dev tsx` |
| TypeScript, existing project | `npm install @anthropic-ai/claude-agent-sdk` and `npm install --save-dev tsx`; for a CommonJS project name the script `agent.mts` so top-level `await` works |
| Python with uv | `uv init`, `uv add claude-agent-sdk` |
| Python with pip | create a venv, then `pip install claude-agent-sdk` |

Run scripts with `npx tsx agent.ts`, `uv run agent.py` or `python agent.py`. The SDK can run from any folder and has access to files in that directory and its subdirectories by default.

# Limits and defaults

Prerequisites: Node.js 18.14+ or Python 3.10+, and an Anthropic account. Cases with no bundled binary:
- pip installs the Python source distribution instead of a platform wheel (for example on ARM64 Windows): install Claude Code natively; the Python SDK finds it on `PATH`.
- The TypeScript SDK gets its binary through npm optional dependencies, so an install that skips them (for example `npm ci --omit=optional`) has none: reinstall without skipping, or install natively and set `pathToClaudeCodeExecutable`.
