---
type: "Feature"
title: "Mocking MCP servers in evals"
description: "Per-tool mock files answer MCP calls so skills can be evaluated without the real service; fixed or agent-answered."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, mcp, mocks, replay]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [headless]
requires: ""
identifiers:
  - "evals/mocks/<server>/<tool>.md"
  - "evals/mocks/<server>/_server.md"
  - "evals/mocks/<server>/_tools.json"
  - "evals/mocks/.replay/<server>/"
  - "mock-recordings/"
  - "ADOPT.txt"
  - "expect"
  - "error"
  - "type: agent"
  - "type"
  - "abort_when"
  - "tools"
  - "{{input.<field>}}"
  - "{{file:fixtures/<name>}}"
  - "--mocks record"
  - "--mocks off"
  - "--allow-real-servers"
  - "mcp__plugin_<plugin>_<server>__<tool>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Put one Markdown file per tool at `evals/mocks/<server>/<tool>.md` (suite-wide) or under a case's own `mocks/` (overrides the suite file by file); `<server>` is the server's name in the plugin's MCP configuration. A run never starts the plugin's real MCP servers unless asked. Claude Code registers a substitute server under each server's name: tools with a mock file answer from it and need no `--allow-tools` grant; a tool without a mock is unavailable. A server with no mocks appears in the `mocked:` progress line as `plugin_<plugin>_<server>[not started: no mock]`. To grade the calls use `target: mock_calls`.

# How to use it

The file body is the tool result. Example `evals/mocks/tracker/create_issue.md`: frontmatter `expect: {title: string, priority: [low, medium, high]}`, body `Created issue #4821: {{input.title}}`.

| Key | Default | Purpose |
| :- | :- | :- |
| `type` | `fixed` | `fixed` returns the body; `agent` has the judge model answer as the server from instructions in the body, seeing earlier calls as history |
| `expect` | unset | Map of dotted input paths to a type (`string`, `number`, `boolean`, `array`, `object`), a `/regex/`, a literal, or a list of literals. A violating call aborts the run with score 0, reported as `aborted` with server, tool and reason |
| `error` | `false` | `fixed` only: return body as a tool error |
| `abort_when` | unset | `agent` only: prose of the only conditions under which the agent may abort |

Substitutions: `{{input.<field>}}` and `{{file:fixtures/{input.<field>}.json}}` (fixtures beside the mock). Optional files per server: `_server.md` (one `type: agent` mock answering several tools listed in `tools:`; a `<tool>.md` takes precedence; an `expect:` guard there is a load error unless `tools:` lists one tool) and `_tools.json` (saved `tools/list` response for real descriptions and schemas).

Real servers: `--allow-real-servers` starts the real process for each unmocked server; `--mocks off` ignores mocks and starts every declared server. Those processes run as you, outside the sandbox, and their tools need `--allow-tools` (e.g. `"mcp__plugin_my-plugin_github__*"`).

# Limits and defaults

- Agent mocks share one budget per run of 4 times the case's `max_turns` (40 at default 10); `.replay/` answers count; a call past it aborts the run with score 0 (`mock call budget exceeded`).
- Agent-mock answers vary with the `--judge-model`. When a run completes without error or abort, answers are saved under the results directory's `mock-recordings/`; `ADOPT.txt` says which `.replay/<server>/` directory to copy each into. Later runs then answer the identical call from it with no model call; commit `mocks/.replay/` for repeatable CI.
- `expect` regex dialect (checked at load): literals, `.`, escapes like `\d`, classes like `[a-z]`, quantifiers `*`, `+`, `?`, `{m,n}` on a single char/escape/class, optional leading `^` and trailing `$`, flags `i` and `s` only. Groups, alternation, backreferences, lookaround or other flags stop the case from loading (score 0, error names the pattern); use a list of literals instead. Values over a maximum length are violations; anchor with `^` and keep quantifiers few.
