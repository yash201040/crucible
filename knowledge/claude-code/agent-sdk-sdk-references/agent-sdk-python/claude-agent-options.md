---
type: "Reference"
title: "ClaudeAgentOptions fields"
description: "Every field of the Python ClaudeAgentOptions dataclass: tools, permissions, budgets, sessions, models, hooks, sandbox, session store and more."
resource: "https://code.claude.com/docs/en/agent-sdk/python"
tags: [python, options, configuration, budget, sessions]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "ClaudeAgentOptions"
  - "tools"
  - "allowed_tools"
  - "disallowed_tools"
  - "system_prompt"
  - "mcp_servers"
  - "strict_mcp_config"
  - "permission_mode"
  - "continue_conversation"
  - "resume"
  - "session_id"
  - "max_turns"
  - "max_budget_usd"
  - "model"
  - "fallback_model"
  - "betas"
  - "output_format"
  - "permission_prompt_tool_name"
  - "cwd"
  - "cli_path"
  - "settings"
  - "add_dirs"
  - "env"
  - "extra_args"
  - "max_buffer_size"
  - "stderr"
  - "debug_stderr"
  - "can_use_tool"
  - "hooks"
  - "user"
  - "include_partial_messages"
  - "include_hook_events"
  - "forward_subagent_text"
  - "verbatim_prompts"
  - "fork_session"
  - "resume_session_at"
  - "resume_drops_turn"
  - "agents"
  - "setting_sources"
  - "skills"
  - "sandbox"
  - "plugins"
  - "max_thinking_tokens"
  - "thinking"
  - "effort"
  - "enable_file_checkpointing"
  - "session_store"
  - "session_store_flush"
  - "load_timeout_ms"
  - "task_budget"
  - "CLAUDE_AGENT_SDK_CLIENT_APP"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-python"
    resource: "https://code.claude.com/docs/en/agent-sdk/python"
    title: "Agent SDK reference - Python"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`ClaudeAgentOptions` is the configuration dataclass passed to `query()` or `ClaudeSDKClient`. Defaults are in the table.

# How to use it

| Field | Default | What it does |
| :- | :- | :- |
| `tools` | `None` | tool list or `{"type":"preset","preset":"claude_code"}` |
| `allowed_tools` | `[]` | auto-approve these tools (does not restrict others; unlisted fall to `permission_mode` and `can_use_tool`). Naming a task-tracking tool also opts the session in |
| `disallowed_tools` | `[]` | bare name removes the tool from context; scoped rule like `"Bash(rm *)"` denies matching calls in every mode, incl. `bypassPermissions` |
| `system_prompt` | `None` | string, preset (with `append`), `{"type":"custom",...}` or `{"type":"file","path":...}` |
| `mcp_servers` | `{}` | dict of configs, or path to config file |
| `strict_mcp_config` | `False` | use only `mcp_servers`; ignore `.mcp.json`, user settings, plugin servers and claude.ai connectors (CLI `--strict-mcp-config`) |
| `permission_mode` | `None` | see [permissions](./permissions-and-callbacks.md) |
| `continue_conversation` / `resume` | `False` / `None` | continue latest / resume a session id |
| `session_id` | `None` | explicit UUID; cannot combine with `continue_conversation` or `resume` unless `fork_session` is set |
| `fork_session` | `False` | when resuming, fork to a new session id |
| `resume_session_at` | `None` | load only up to this message UUID (Python SDK 0.2.137+) |
| `resume_drops_turn` | `None` | user-prompt UUID whose turn a truncation discards; CLI refuses resume if the dropped range has foreign entries (SDK 0.2.137+, Claude Code 2.1.223+) |
| `max_turns` | `None` | cap on agentic turns |
| `max_budget_usd` | `None` | stop when the client-side cost estimate reaches this value; estimate can overshoot; counts only this call's spend, not totals restored from a resumed session |
| `model`, `fallback_model` | `None` | alias or full id; fallback accepts a comma-separated list |
| `betas` | `[]` | see `SdkBeta` below |
| `output_format` | `None` | `{"type":"json_schema","schema":{...}}` |
| `permission_prompt_tool_name` | `None` | MCP tool for permission prompts |
| `cwd`, `cli_path`, `add_dirs` | `None`, `None`, `[]` | working dir, CLI binary, extra dirs (each passed as `--add-dir`; with `project` source also loads that dir's skills, commands, subagents) |
| `settings` | `None` | settings file path or inline JSON |
| `env` | `{}` | env vars merged over the inherited environment; `CLAUDE_AGENT_SDK_CLIENT_APP` identifies your app in the User-Agent |
| `extra_args` | `{}` | extra CLI args passed through |
| `max_buffer_size` | `None` (1,048,576) | longest single CLI message in characters; longer raises `CLIJSONDecodeError` |
| `stderr` / `debug_stderr` | `None` / `sys.stderr` | stderr callback; `debug_stderr` is deprecated and ignored |
| `can_use_tool`, `hooks` | `None` | callbacks, see [permissions](./permissions-and-callbacks.md) |
| `user` | `None` | POSIX: OS account the CLI subprocess runs as; keeps parent `HOME`, runs in `cwd` |
| `include_partial_messages` | `False` | yield `StreamEvent` messages |
| `include_hook_events` | `False` | hook lifecycle events as `HookEventMessage` |
| `forward_subagent_text` | `False` | forward text and thinking blocks of foreground subagents (SDK 0.2.140+) |
| `verbatim_prompts` | `False` | send each user message with `client_composed=True`; needs SDK 0.2.158+ and Claude Code 2.1.248+ |
| `agents` | `None` | `dict[str, AgentDefinition]`, see [subagents](./agent-definition-and-agent-tool.md) |
| `setting_sources` | `None` | which of `"user"`, `"project"`, `"local"` to load; see below |
| `skills` | `None` | `"all"` or exact skill names; wildcard or malformed names raise `ValueError` (SDK 0.2.129+); adds the Skill tool to `allowed_tools` automatically; if `tools` is also passed include `"Skill"` |
| `sandbox`, `plugins` | `None`, `[]` | see [sandbox](./sandbox-settings.md); plugins are `{"type":"local","path":...}` only |
| `thinking`, `max_thinking_tokens` | `None` | `thinking` wins; `max_thinking_tokens` deprecated |
| `effort` | `None` | `"low"`, `"medium"`, `"high"`, `"xhigh"` (falls back to `high` where unsupported), `"max"` |
| `enable_file_checkpointing` | `False` | enable rewind |
| `session_store` | `None` | mirror transcripts to an external backend so another host can resume |
| `session_store_flush` | `"batched"` | `"batched"` (once per turn or full buffer) or `"eager"` (background flush after every frame) |
| `load_timeout_ms` | `60000` | per-call timeout for `session_store.load()` and `list_subkeys()` on resume |
| `task_budget` | `None` | `{"total": <int>}` API-side token budget, sent as `output_config.task_budget` with beta header `task-budgets-2026-03-13` |

Sub-types:
- `SystemPromptPreset` fields `type`, `preset`, `append`, `exclude_dynamic_sections` (moves per-user context such as the auto memory location into the first user message to improve prompt-cache reuse across users and machines), `snapshot` (set `False` to rebuild the prompt every request instead of reusing the recorded first-request prompt; SDK 0.2.153+). `SystemPromptCustom` (`type`, `prompt`, `snapshot`; 0.2.153+). `SystemPromptFile` (`type`, `path`; maps to `--system-prompt-file`).
- `ThinkingConfig`: `{"type":"adaptive"}`, `{"type":"enabled","budget_tokens":N}`, `{"type":"disabled"}`; optional `display` of `"summarized"` or `"omitted"` (API default on Claude Opus 4.7 and later is `"omitted"`). `TaskBudget` is `{"total": int}`.
- `SdkBeta = Literal["context-1m-2025-08-07"]`: retired on the Claude API for Sonnet 4.5 and Sonnet 4 (over-200K requests error). For 1M use a model with 1M by default such as `claude-sonnet-5-5` or `claude-opus-5-5`, or append `[1m]` as in `claude-opus-4-6[1m]`.
- `ToolsPreset`: `{"type":"preset","preset":"claude_code"}`.

# Limits and defaults

`setting_sources` values: `"user"` (`~/.claude/settings.json`), `"project"` (`.claude/settings.json`), `"local"` (`.claude/settings.local.json`). Default `None` loads all three like the CLI, but with `skills` set and this unset only user and project load. `[]` disables all filesystem settings (before Python SDK 0.1.59 an empty list was treated like omitted). Include `"project"` to load CLAUDE.md. Precedence high to low: local, project, user; programmatic options override filesystem settings; managed policy overrides programmatic options; endpoint-managed policy always loads.

A string `system_prompt` goes on the CLI argv: on Linux a single argument above about 128 KB fails with `Argument list too long`; on Windows the whole command line is about 32 KB. Use the file form for large prompts.

# Notes

Timeout environment variables passed through `env` are in [stalls and timeouts](./api-timeouts-and-stalls.md).
