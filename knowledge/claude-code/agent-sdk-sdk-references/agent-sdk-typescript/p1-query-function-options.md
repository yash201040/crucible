---
type: "Reference"
title: "query() and the Options object"
description: "The query() entry point and every Options property: permissions, budgets, sessions, system prompt, MCP, settings, subagents, spawning."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [query, options, configuration, budget, permissions, sessions]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "query()"
  - "abortController"
  - "additionalDirectories"
  - "agent"
  - "agents"
  - "agentProgressSummaries"
  - "allowDangerouslySkipPermissions"
  - "allowedTools"
  - "betas"
  - "canUseTool"
  - "continue"
  - "cwd"
  - "debug"
  - "debugFile"
  - "disallowedTools"
  - "effort"
  - "enableFileCheckpointing"
  - "env"
  - "executable"
  - "executableArgs"
  - "extraArgs"
  - "fallbackModel"
  - "forkSession"
  - "forwardSubagentText"
  - "hooks"
  - "includeHookEvents"
  - "includePartialMessages"
  - "loadTimeoutMs"
  - "managedSettings"
  - "maxBudgetUsd"
  - "maxThinkingTokens"
  - "maxTurns"
  - "mcpServers"
  - "model"
  - "onElicitation"
  - "outputFormat"
  - "outputStyle"
  - "pathToClaudeCodeExecutable"
  - "permissionMode"
  - "permissionPromptToolName"
  - "permissionPrompts"
  - "persistSession"
  - "planModeInstructions"
  - "plugins"
  - "projectConfigRoot"
  - "promptSuggestions"
  - "resume"
  - "resumeDropsTurn"
  - "resumeSessionAt"
  - "sandbox"
  - "sessionId"
  - "sessionStore"
  - "sessionStoreFlush"
  - "settings"
  - "settingSources"
  - "skills"
  - "spawnClaudeCodeProcess"
  - "stderr"
  - "strictMcpConfig"
  - "systemPrompt"
  - "SYSTEM_PROMPT_DYNAMIC_BOUNDARY"
  - "taskBudget"
  - "thinking"
  - "title"
  - "toolAliases"
  - "toolConfig"
  - "tools"
  - "verbatimPrompts"
  - "CLAUDE_AGENT_SDK_CLIENT_APP"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`query({ prompt, options? }): Query` is the main function. `prompt` is a `string` or an `AsyncIterable<SDKUserMessage>` (streaming input mode). It returns a [`Query`](./p1-query-object-methods.md), an `AsyncGenerator<SDKMessage, void>` with extra methods. `Options` configures it.

# How to use it

| Property | Type / default | What it does |
| :- | :- | :- |
| `abortController` | `AbortController` | Cancel operations |
| `additionalDirectories` | `string[]`, `[]` | Extra dirs; passed as `--add-dir` (with `project` source also loads that dir's skills, commands, subagents) |
| `agent` | `string` | Main-thread agent name; must be in `agents` or settings |
| `agents` | `Record<string, AgentDefinition>` | Programmatic subagents |
| `agentProgressSummaries` | `false` | One-line progress summaries on `task_progress` `summary` for fore/background subagents |
| `allowDangerouslySkipPermissions` | `false` | Required for `permissionMode: 'bypassPermissions'` |
| `allowedTools` | `[]` | Auto-approve list; does not restrict to them. Naming a task-tracking tool opts the session in |
| `betas` | `SdkBeta[]` | Beta features |
| `canUseTool` | callback | Called only when permission flow falls to a prompt |
| `continue`, `resume`, `resumeSessionAt`, `forkSession`, `sessionId` | bool / string | Continue latest, resume ID, resume at message UUID, fork on resume, force a UUID |
| `cwd` | `process.cwd()` | Working directory |
| `debug`, `debugFile` | `false` | Debug logs; `debugFile` implies debug |
| `disallowedTools` | `[]` | Bare name removes the tool from context; scoped `"Bash(rm *)"` denies matching calls in every mode incl. `bypassPermissions` |
| `effort` | `low|medium|high|xhigh|max` | Effort level |
| `enableFileCheckpointing` | `false` | Needed for `rewindFiles()` |
| `env` | `process.env` | Replaces (not merges) subprocess env; spread `process.env` |
| `executable`, `executableArgs` | `bun|deno|node`, `[]` | JS runtime and args |
| `extraArgs` | `{}` | Extra CLI args |
| `fallbackModel` | string | Comma-separated list allowed |
| `forwardSubagentText` | `false` | Forward subagent text/thinking with `parent_tool_use_id` |
| `hooks` | `{}` | Hook callbacks per `HookEvent` |
| `includeHookEvents` | `false` | Emit hook_started/progress/response messages (SessionStart/Setup always) |
| `includePartialMessages` | `false` | Stream events |
| `loadTimeoutMs` | `60000`, alpha | Timeout per `sessionStore.load()`/`listSubkeys()` on resume |
| `managedSettings` | `Settings` | Policy-tier settings from host; ignored on admin-managed machines unless `parentSettingsBehavior: 'merge'` |
| `maxBudgetUsd` | number | Stop at client-side cost estimate; leave headroom; excludes resumed totals |
| `maxThinkingTokens` | deprecated | Use `thinking` |
| `maxTurns` | number | Max agentic turns |
| `mcpServers` | `{}` | MCP server configs |
| `model` | CLI default | Alias or full ID |
| `onElicitation` | callback | MCP elicitation; unhandled requests are declined |
| `outputFormat` | `{ type: 'json_schema', schema }` | Structured output |
| `outputStyle` | not an Options field | Set via `settings` instead |
| `pathToClaudeCodeExecutable` | bundled binary | Custom binary |
| `permissionMode` | `default` | See [permission types](./p1-agent-definition-and-permissions.md) |
| `permissionPromptToolName` | string | MCP tool that answers permission prompts |
| `permissionPrompts` | `'host'|'none'`, `'host'` | `'none'` denies calls that would prompt; needs Claude Code v2.1.259+ |
| `persistSession` | `true` | `false` disables disk persistence (no resume) |
| `planModeInstructions` | string | Replaces plan-mode workflow body |
| `plugins` | `SdkPluginConfig[]` | Local plugins |
| `projectConfigRoot` | string | Trusted checkout that `cwd` is a worktree of; reads settings, `.mcp.json`, `.claude/` from it; sets `CLAUDE_PROJECT_DIR`. v2.1.275+ |
| `promptSuggestions` | `false` | Emit `prompt_suggestion` |
| `resumeDropsTurn` | string | Pairs with `resumeSessionAt`; refuses resume if discarded range has unattributable content; v2.1.223+ (`--resume-drops-turn`) |
| `sandbox` | `SandboxSettings` | See [sandbox](./p2-sandbox-settings.md) |
| `sessionStore`, `sessionStoreFlush` | alpha flush `'batched'|'eager'` (default `'batched'`) | Mirror transcripts to external store |
| `settings` | `string | Settings` | Inline object, file path or JSON string; flag-settings layer |
| `settingSources` | all sources | `[]` disables user/project/local; managed policy always loads |
| `skills` | `string[] | 'all'` | Enabled skills; exact names only (v0.3.221+ rejects wildcards); adds Skill tool to `allowedTools` |
| `spawnClaudeCodeProcess` | function | Run Claude Code in VM/container/remote |
| `stderr` | callback | stderr output |
| `strictMcpConfig` | `false` | Ignore `.mcp.json`, user settings, plugin and claude.ai connector MCP servers |
| `systemPrompt` | undefined (minimal) | String, string[] with `SYSTEM_PROMPT_DYNAMIC_BOUNDARY`, `{type:'custom',prompt,snapshot?}`, or `{type:'preset',preset:'claude_code',append?,excludeDynamicSections?,snapshot?}`; custom form and `snapshot` need v0.3.257+ |
| `taskBudget` | `{ total }`, alpha | API-side token budget told to the model |
| `thinking` | adaptive default | See thinking config |
| `title` | string | Session display title; persisted title wins on resume |
| `toolAliases` | map | e.g. `{ Bash: 'mcp__workspace__bash' }` |
| `toolConfig` | `ToolConfig` | `askUserQuestion.previewFormat` |
| `tools` | array or `{type:'preset',preset:'claude_code'}` | Tool set |
| `verbatimPrompts` | `false` | Sends `client_composed: true` on each message; SDK v0.3.280+ and Claude Code v2.1.248+ |

# Limits and defaults

Timeout env vars passed through `env` (spread `process.env`): `API_TIMEOUT_MS` (default `600000`, per request attempt until headers; main loop and subagents), `CLAUDE_CODE_MAX_RETRIES` (default `10`, cap `15`), `CLAUDE_CODE_RETRY_WATCHDOG=1` (retry transient capacity errors forever; on v2.1.199+ other transient default `300`, cap removed), `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` (subagent stall watchdog; default `CLAUDE_STREAM_IDLE_TIMEOUT_MS` plus 5 min = `600000`, with watchdog off `600000`; before v2.1.257 always `600000`; on stall aborts subagent, marks background task failed with partial result), `CLAUDE_ENABLE_STREAM_WATCHDOG` (on by default, `0` disables), `CLAUDE_STREAM_IDLE_TIMEOUT_MS` (default and minimum `300000`). With `includePartialMessages`, `ping` stream events are liveness frames while a gateway behind `ANTHROPIC_BASE_URL` holds a response open (before v2.1.257 they stopped after 5 min). Set `CLAUDE_AGENT_SDK_CLIENT_APP` in `env` to identify your app in the User-Agent.
