---
type: "Reference"
title: "Mods API methods by namespace"
description: "Every $ namespace and method a mod hook can call, with version notes for agent, session, ui, theme and fs methods."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, api, namespaces, agent]
kind: "api"
maturity: "unlabelled"
since: "2.1.326"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "$.plugin"
  - "$.ui"
  - "$.theme"
  - "$.command"
  - "$.tool"
  - "$.agent"
  - "$.model"
  - "$.prompt"
  - "$.turn"
  - "$.session"
  - "$.config"
  - "$.settings"
  - "$.env"
  - "$.fs"
  - "$.store"
  - "$.state"
  - "$.clock"
  - "$.http"
  - "$.process"
  - "$.mcp"
  - "$.audio"
  - "$.telemetry"
  - "$.agent.spawn"
  - "$.agent.list"
  - "$.agent.limits"
  - "$.session.usage"
  - "$.prompt.submit"
  - "$.turn.abort"
  - "$.mcp.connect"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The mods API is the `$` argument every hook receives. `open` in the `$.ui` row is the call `$.ui.open(...)`.

| Namespace | Methods |
| :- | :- |
| `$.plugin` | `name`, `root` |
| `$.ui` | `resolve`, `invalidate`, `open`, `close`, `panes`, `place` (v2.1.314+), `focus`, `scroll`, `toast`, `notify`, `status`, `log`, `notice`, `ask`, `copy`, `selection`, `blit`, `view` (v2.1.300+) |
| `$.theme` | `set`, `clear` (backdrop for Desktop/mobile; v2.1.319+) |
| `$.command` | `register`, `run`, `list` |
| `$.tool` | `register`, `call`, `check`, `list` |
| `$.agent` | `register`, `spawn`, `call`, `list`, `limits`; `call` and `limits` need v2.1.326+; `list()` returns this session's subagents and teammates each with `status` of `pending`, `running`, `waiting`, `idle`, `completed`, `failed`, `killed` (`idle` and `waiting` need v2.1.289+) |
| `$.model` | `complete`, `fork`, `classify` |
| `$.prompt` | `submit`, `read`, `fill`, `suggest`, `compose` |
| `$.turn` | `abort` |
| `$.session` | `messages`, `cwd`, `root`, `model`, `turns`, `id`, `repo`, `surfaces`, `usage`, `version`, `compact`, `send`, `append`, `authorize` |
| `$.config` | `list`, `set` |
| `$.settings` | `read` |
| `$.env` | `get`, `set` |
| `$.fs` | `read`, `write`, `list`, `exists`, `stat`, `ancestors` |
| `$.store` | `get`, `set`, `delete`, `keys` |
| `$.state` | `get`, `set`; helpers `atom`, `read`, `update`, `derive`, `memberOf` from `claude-code` |
| `$.clock` | `now`, `sleep`, `after`, `every` |
| `$.http` | `fetch` |
| `$.process` | `run`, `spawn` |
| `$.mcp` | `call`, `connect` |
| `$.audio` | `play`, `speak` |
| `$.telemetry` | `log`, `mark` |

# Notes

- `$.prompt.submit({ text })`: Claude reads the text after a sentence naming your mod as sender; `submit({ text, asUser: true })` sends it as the user's own words without that sentence.
- `$.session.usage()` returns `{ startedAt, context, rateLimits, cost }`; `context` has `tokens`, `window`, `percent`; `rateLimits` is a list of `{ kind, percentUsed, resetsAt }`.
- `$.fs.write` is not atomic (replaces content in place, so another process can read a partial file); keep multi-session data in `$.store` (shared by every session on the machine).
- `$.mcp.connect(server)` connects an MCP server listed in your own plugin's manifest.
- `$.telemetry` records are sent only when Claude Code or a built-in mod makes the call.
