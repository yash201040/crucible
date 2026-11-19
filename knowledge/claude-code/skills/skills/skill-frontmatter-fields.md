---
type: "Reference"
title: "Skill frontmatter fields"
description: "Every SKILL.md frontmatter field (name, description, allowed-tools, model, effort, context, hooks, paths, shell and more) with semantics."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, frontmatter, reference, fields]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "name"
  - "description"
  - "when_to_use"
  - "argument-hint"
  - "arguments"
  - "disable-model-invocation"
  - "user-invocable"
  - "allowed-tools"
  - "disallowed-tools"
  - "model"
  - "effort"
  - "context"
  - "agent"
  - "background"
  - "hooks"
  - "paths"
  - "shell"
  - "metadata"
  - "license"
  - "compatibility"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

YAML frontmatter at the top of `SKILL.md`. All fields optional; only `description` is recommended. Field names are lowercase hyphenated except `when_to_use`. A `.claude/commands/` file accepts the same fields except `name` and `paths`.

# How to use it

Names must match exactly; unknown fields are silently ignored. Booleans accept `yes`, `no`, `on`, `off`, `1`, `0` in any case besides `true`/`false`. Frontmatter is read only when the opening `---` is the file's first line; if the YAML does not parse the skill still loads with no fields set.

| Field | Default | What it does |
| :- | :- | :- |
| `name` | directory name | Command name in the `/` menu |
| `description` | first non-empty body line | What it does and when to use; combined with `when_to_use` truncated at 1,536 characters in the listing; `<` `>` display as `&lt;` `&gt;` |
| `when_to_use` | none | Extra trigger context appended to `description`, counts toward the 1,536 cap |
| `argument-hint` | none | Autocomplete hint, e.g. `[issue-number]` |
| `arguments` | none | Named positional args for `$name` substitution; space-separated string or YAML list |
| `disable-model-invocation` | `false` | Claude cannot auto-load; also blocks preloading into subagents and running when a session-scoped scheduled task fires with the skill as prompt |
| `user-invocable` | `true` | `false` hides it from `/` menu and typing `/name` does not run it |
| `allowed-tools` | none | Tools allowed without prompting during the invoking turn; cleared on next message; space/comma string or YAML list |
| `disallowed-tools` | none | Tools removed from the pool while active; cleared on next message; cannot remove `EndConversation` while any other tool remains |
| `model` | inherit | Model for the rest of the turn, same values as `/model`, or `inherit`; not saved; excluded by `availableModels` or unsupported in auto mode/plan mode classifier means session model kept; with `context: fork` sets the forked subagent's model |
| `effort` | per resolution order | `low`, `medium`, `high`, `xhigh`, `max` (availability depends on model) for the turn; does not override `CLAUDE_CODE_EFFORT_LEVEL`; with fork sets subagent effort |
| `context` | none | `fork` runs in a forked subagent |
| `agent` | `general-purpose` | Subagent type when `context: fork` |
| `background` | `true` | With fork only; `false` waits for the result in the same turn |
| `hooks` | none | Hooks registered on invocation and kept for the session (see hooks docs for `once` and limits) |
| `paths` | none | Globs (comma string or YAML list) so the skill auto-loads only for matching files; relative to the current working directory; files outside do not match |
| `shell` | `bash` | `bash` or `powershell` for `` !`command` `` and ` ```! ` blocks; PowerShell tool is on by default on Windows without Git Bash and (with Git Bash) for claude.ai and Console accounts; needs `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` on Bedrock, Google Cloud's Agent Platform, Foundry, macOS, Linux, WSL; `0` turns it off |
| `metadata` | none | Free-form YAML map for your own tooling; Claude Code ignores it, drops non-map values; do not reuse field names like `paths` as keys |
| `license` | none | Agent Skills spec field; accepted, not acted on |
| `compatibility` | none | Spec field, string up to 500 characters; accepted, not acted on |
