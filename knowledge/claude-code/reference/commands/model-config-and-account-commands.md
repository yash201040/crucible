---
type: "Reference"
title: "Model, permission, configuration and usage commands"
description: "Slash commands for model, effort, fast mode, permissions, sandbox, settings, memory, hooks, MCP, plugins, skills, output style and usage."
resource: "https://code.claude.com/docs/en/commands"
tags: [slash-commands, model, permissions, config, usage]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/advisor"
  - "/agents"
  - "/auto-mode-setup"
  - "/config"
  - "/settings"
  - "/cost"
  - "/effort"
  - "/fast"
  - "/hooks"
  - "/import"
  - "/init"
  - "/mcp"
  - "/memory"
  - "/model"
  - "/output-style"
  - "/permissions"
  - "/allowed-tools"
  - "/plan"
  - "/plugin"
  - "/rate-limit-options"
  - "/reload-plugins"
  - "/reload-skills"
  - "/sandbox"
  - "/skill-doctor"
  - "/skills"
  - "/stats"
  - "/usage"
  - "/usage-credits"
  - "CLAUDE_CODE_NEW_INIT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "commands"
    resource: "https://code.claude.com/docs/en/commands"
    title: "Commands"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Commands that change the model, effort, permissions and extensions in a session, and show cost and usage.

# How to use it

| Command | What it does |
| :- | :- |
| `/advisor [model\|off]` | Enable or disable the advisor tool (second model consulted at key moments); `fable`, `opus`, `sonnet` or full ID; `fable` needs Fable access. Without an interactive terminal or over Remote Control pass the argument; with none it prints the current advisor. v2.1.260+ |
| `/agents` | Prints a reminder to ask Claude to create or manage subagents or edit `.claude/agents/` or `~/.claude/agents/`; on v2.1.197 and earlier it opened an interactive interface |
| `/auto-mode-setup` | Draft `autoMode.environment` entries from project and recent sessions, review, save to user settings. Pro/Max/Ultra/Team: v2.1.228+ (native Windows v2.1.233+); Enterprise or Console API key: v2.1.283+ |
| `/config [key=value ...]` | Open Settings, or set keys directly (`/config verbose=true`, `/config model=sonnet`), also with `-p` and from the mobile app via Remote Control; cannot enable settings needing panel confirmation such as `autoContinueAtUsageLimit`; `/config --help` lists keys. Alias `/settings` |
| `/effort [level\|auto\|status\|ultracode [on\|off]]` | Set effort `low` to `xhigh`, `max` (session-only) or `auto`; `status` prints it; `ultracode`/`ultracode on`/`ultracode off` toggle ultracode (`on`/`off` need v2.1.284+); the `ultracode` key persists. Works with `-p` on v2.1.205+ |
| `/fast [on\|off]` | Toggle fast mode; mid-response it toggles without waiting (running turn keeps its speed); with `-p` availability is limited |
| `/hooks` | View hook configurations |
| `/import [codex\|gemini\|cursor] [--dry-run] [--yes]` | Bring instruction files, MCP servers, commands, subagents and skills from Codex, Gemini CLI or Cursor (Cursor needs v2.1.265+). With `-p` it lists findings and the confirming command. Unavailable on Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, Claude Platform on AWS, through a Claude apps gateway, or with feature-flag fetching off |
| `/init` | Create a starter `CLAUDE.md`; `CLAUDE_CODE_NEW_INIT=1` gives an interactive flow covering skills, hooks and personal memory files; offers `/import` if Codex or Gemini config is found |
| `/mcp [reconnect (<server>\|all)\|enable\|disable [<server>\|all]]` | Manage MCP connections and OAuth; `reconnect all` retries failed or unauthenticated servers; with `-p` and no argument prints a text status |
| `/memory` | Edit `CLAUDE.md`, toggle auto memory, view entries |
| `/model [model]` | Switch model and save as default for new sessions; `s` on a picker row switches for this session only; with `-p` a model argument is not saved as default (v2.1.205+) |
| `/output-style [style]` | List or switch output styles. v2.1.269+ |
| `/permissions` | Manage allow, ask and deny rules, working directories and recent auto mode denials; Auto mode tab edits classifier rules; in the desktop app edit settings files. Alias `/allowed-tools` |
| `/plan [description]` | Enter plan mode, optionally starting on a task |
| `/plugin [subcommand]` | Plugin menu, or `list`, `install`, `enable`, `disable`; the install summary says whether `/reload-plugins` is needed |
| `/rate-limit-options` | Options when a claude.ai usage limit blocks a request: wait and continue automatically, usage credits, upgrade. Needs a claude.ai subscription; wait rows need v2.1.234+ |
| `/reload-plugins [--force]` | Reload active plugins without restarting; warns and skips when it would change loaded MCP tools and invalidate the prompt cache unless `--force`. Also works with `-p`, the Agent SDK and desktop (typed input only, no plugin MCP server changes); v2.1.260+ |
| `/reload-skills` | Re-scan skill and command directories without restarting |
| `/sandbox` | Toggle sandbox mode on supported platforms |
| `/skill-doctor` | Show each skill's context cost and usage frequency. Needs v2.1.252+ and feature-flag fetching |
| `/skills` | List skills; type to filter, `t` sorts by tokens, `Space`/`Enter` cycles visibility, `Esc` saves. Cannot cycle plugin skills, skills with `disable-model-invocation: true`, or skills with a `skillOverrides` entry in managed settings or `--settings` |
| `/usage` | Session cost, plan usage limits and activity stats, plan-limit breakdown on Pro/Max/Ultra/Team/Enterprise, and gateway spend where tracked. Aliases `/cost`, `/stats` (opens Stats tab) |
| `/usage-credits` | Configure usage credits or request them from an admin; prints the URL over SSH (v2.1.205+). Previously `/extra-usage` |
