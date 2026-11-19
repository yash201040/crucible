---
type: "Reference"
title: "Context content, system prompt and minimal-mode variables"
description: "Variables that strip CLAUDE.md, memory, attachments, git instructions or the whole configuration, and choose the system prompt size."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [context, memory, system-prompt, bare-mode]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_SIMPLE"
  - "CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT"
  - "CLAUDE_CODE_SAFE_MODE"
  - "CLAUDE_CODE_DISABLE_CLAUDE_MDS"
  - "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD"
  - "CLAUDE_CODE_DISABLE_AUTO_MEMORY"
  - "CLAUDE_CODE_DISABLE_ATTACHMENTS"
  - "CLAUDE_CODE_DISABLE_FILE_MENTIONS"
  - "CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS"
  - "SLASH_COMMAND_TOOL_CHAR_BUDGET"
  - "CLAUDE_CODE_NEW_INIT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Switches that decide what enters or stays out of the model's context and which prompt variant is used.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_SIMPLE` | `1` runs with a minimal system prompt and only Bash, file read and file edit tools; MCP tools from `--mcp-config` stay. OAuth and keychain credentials are not read, so use `ANTHROPIC_API_KEY` or an `apiKeyHelper` in `--settings`. Same as `--bare`. |
| `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT` | Full versus shorter prompt with abbreviated tool descriptions. Unset: Haiku 4.5, Sonnet 5, Opus 4.7 and earlier in those families use full, newer models use shorter. `1` forces shorter on any model; `0`/`false`/`no`/`off` forces full even where an experiment would pick shorter. Both keep the full tool set, hooks, MCP servers and CLAUDE.md discovery. |
| `CLAUDE_CODE_SAFE_MODE` | `1` starts safe mode: CLAUDE.md, skills, plugins, hooks, MCP servers, custom commands and agents, output styles, workflows, themes, keybindings, status line and file-suggestion commands, LSP servers and auto memory do not load. Managed policy still applies (policy hooks, status line, file-suggestion commands) but managed plugins, skills, CLAUDE.md and policy MCP servers do not. Same as `--safe-mode`; child processes inherit it. |
| `CLAUDE_CODE_DISABLE_CLAUDE_MDS` | `1` loads no CLAUDE.md memory files (user, project, auto). |
| `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` | `1` loads memory files (`CLAUDE.md`, `.claude/CLAUDE.md`, `.claude/rules/*.md`, `CLAUDE.local.md`) from `--add-dir` directories; off by default. |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | `1` disables auto memory; `0` forces it on even under `--bare` or `autoMemoryEnabled: false`. |
| `CLAUDE_CODE_DISABLE_ATTACHMENTS` | `1` sends `@` file mentions as plain text. Ignored in project and local settings. |
| `CLAUDE_CODE_DISABLE_FILE_MENTIONS` | `1` stops expanding `@` mentions of files and directories; Claude gets the paths with a note to read them. Ignored in project and local settings. Requires v2.1.299+. |
| `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS` | `1` removes built-in commit/PR instructions and the git status snapshot; beats `includeGitInstructions`. |
| `SLASH_COMMAND_TOOL_CHAR_BUDGET` | Character budget for skill metadata shown to the Skill tool; scales at 1% of the context window, fallback 8,000. Legacy name. |
| `CLAUDE_CODE_NEW_INIT` | `1` makes `/init` run an interactive setup flow (asks which files to generate: CLAUDE.md, skills, hooks) before exploring. |
