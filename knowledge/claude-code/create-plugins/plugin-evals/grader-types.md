---
type: "Reference"
title: "Grader types, options and targets"
description: "The six grader types (regex, tool_used, tool_order, file_exists, llm, baseline), common keys and what a grader can look at."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, graders, regex, judge]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [headless]
requires: ""
identifiers:
  - "type"
  - "weight"
  - "arm"
  - "with-only"
  - "both"
  - "regex"
  - "tool_used"
  - "tool_order"
  - "file_exists"
  - "llm"
  - "baseline"
  - "pattern"
  - "flags"
  - "match"
  - "target"
  - "focus"
  - "tool"
  - "input_match"
  - "min"
  - "max"
  - "before"
  - "after"
  - "path"
  - "exists"
  - "criteria"
  - "baseline_file"
  - "last_message"
  - "trace"
  - "files"
  - "mock_calls"
  - "{ source: file, path: <path> }"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each file under `graders/` is one check; its name is the filename without `.md`. `regex`, `tool_used`, `tool_order` and `file_exists` are computed from transcript and files and cost nothing; `llm` and `baseline` call a judge model and add cost.

# How to use it

Common keys: `type` (required), `weight` (default `1`, any positive number), `arm` (`with-only` excludes from scoring in a two-arm run; `both` forces scoring in both arms).

| Type | Options | Passes when |
| :- | :- | :- |
| `regex` | `pattern`, `flags`, `match`, `target` | JavaScript regex found in target. `match: not_contains` requires absence, `match: "count:N"` exactly N. Use `flags: i`; inline `(?i)` unsupported |
| `tool_used` | `tool`, `input_match`, `min`, `max` | Calls to `tool` whose JSON input matches `input_match` number between `min` (default 1) and `max` (default unlimited). Never called: `min: 0` and `max: 0` |
| `tool_order` | `before`, `after` | Both called and first `before` call precedes first `after` call; each a tool name or `{ tool, input_match }` |
| `file_exists` | `path`, `exists` | A file Claude created matches the glob, or none with `exists: false`. Only files created during the run count |
| `llm` | `criteria`, `focus` | Judge votes PASS in at least two of three votes; in `.md` layout the body is the criteria |
| `baseline` | `baseline_file`, `criteria` | Judge finds the run satisfies criteria at least as well as the reference `.jsonl` transcript in the case dir |

What a `regex` `target` or `llm` `focus` can see:

| Value | Sees |
| :- | :- |
| `last_message` (default) | Final response text |
| `trace` | Session as JSON, one message per line; regex sees all, `llm` judge sees first 12 and last 12; quotes JSON-escaped (`\"`) |
| `files` | Paths Claude created, one per line; not contents, not scaffolded or merely modified files |
| `{ source: file, path: <path> }` | Contents of one workspace file after the run; PNG, JPEG, GIF, WebP shown to the judge as images; other binaries (`.pptx`, PDF) refused by `llm` |
| `mock_calls` | Each call to a mocked MCP tool with input and the mock's answer |

# Notes

Judge model defaults to the background-task model; set `--judge-model`.
