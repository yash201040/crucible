---
type: "Reference"
title: "Plugin authoring errors and claude plugin validate messages"
description: "Developer-side failures: component paths, userConfig, skills not loading, strict-mode conflicts, and the validate message table and flags."
resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
tags: [plugins, authoring, validate, userconfig, skills]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, ide]
requires: "claude plugin configure and <server>.<key> user config need v2.1.285 or later"
identifiers:
  - "claude plugin validate"
  - "/plugin validate"
  - "--strict"
  - "claude plugin configure"
  - "/plugin configure"
  - "--config"
  - "userConfig"
  - "user_config"
  - "claude plugin eval"
  - "claude plugin eval init"
  - "--eval-dir"
  - "disable-model-invocation"
  - "strict"
  - "engines"
  - "commands path not found"
  - "path escapes plugin directory"
  - "SKILL.md"
  - "--plugin-dir"
  - "${CLAUDE_PLUGIN_ROOT}"
  - "exec form"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-troubleshooting"
    resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
    title: "Troubleshoot plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Failures while developing a plugin with `--plugin-dir` or a local marketplace.

# How to use it

- `commands path not found: <path>` (also `skills`, `agents`, `hooks`): path from `plugin.json` or the marketplace entry resolved against the plugin root; use `./` paths; outside-root paths report `<component> path escapes plugin directory` and are dropped. Before v2.1.299 it could appear on a `synced[0]` row after another session moved files.
- `--plugin-dir` must be the plugin root (with `.claude-plugin/plugin.json`); at a marketplace root nothing loads and there is no error (before v2.1.281 it loaded one empty plugin).
- Files referenced outside the plugin dir (`../shared-utils`) vanish after install because of the cache; move inside or symlink.
- Windows with Git Bash: shell-form hooks get `${CLAUDE_PLUGIN_ROOT}` with forward slashes; use an exec-form hook (spawns directly with `args`) or `"shell": "powershell"` for native paths.
- Skills missing: put `skills/` and `commands/` at plugin root, not in `.claude-plugin/`; each skill is a directory with `SKILL.md`; a `skills` manifest entry pointing at a file reports `path is a file; skills entries must be directories containing SKILL.md`.
- Skill never invoked by Claude: `disable-model-invocation: true`, weak description, or truncated descriptions; measure with an eval case using a `tool_used: Skill` grader and `claude plugin eval`. `claude plugin eval init` must run in the plugin root (`<directory> is not a plugin or skill folder`); `--eval-dir` overrides.
- `userConfig` dialog: shown by interactive `/plugin install` and Discover; VS Code asks after install (before v2.1.285 not); `claude plugin install` never prompts: pass `--config KEY=VALUE` (one per option), else it prints `N userConfig options not yet set — run /plugin configure <plugin>@<marketplace> in Claude Code, or pass --config KEY=VALUE.` (`(M required)` when needed). Undeclared key: `⚠ Installed, but --config not applied: ...`. MCPB bundles with their own `user_config` use `<server>.<key>` keys (v2.1.285+). `claude plugin configure` (v2.1.285+) lists unset options and saves values piped on stdin.
- `Plugin <name> has conflicting manifests: both plugin.json and marketplace entry specify components`: entry `strict: false` also declaring `commands`, `agents`, `skills`, `hooks`, `outputStyles` or `themes`; remove them or set `strict: true`.
- `Warning: No commands found in plugin <name> custom directory: <path>` appears only in the `--debug` log.

`claude plugin validate <path>` (or `/plugin validate`) prints `Found N errors` and `Validation failed`, exit code 1. It reads `.claude-plugin/plugin.json`, `marketplace.json`, or both (since v2.1.289 a dir with both is validated as both). `--strict` makes `No frontmatter block found` and `Unknown field '<key>'` warnings fatal.

| Message | Fix |
|---|---|
| `File not found: <path>` / `No manifest found in directory...` | run against the dir containing `.claude-plugin/` |
| `Invalid JSON syntax: <parse error>` | fix JSON; a broken `hooks/hooks.json` makes sessions load without those hooks |
| `Path not found: <path>...` | fix or create |
| `Path contains ".." which could be a path traversal attempt` | stay inside plugin root |
| `Path is a file; skills entries must be directories containing SKILL.md` | point at parent dir or `.` |
| `No frontmatter block found` / `YAML frontmatter failed to parse` | fix `---` frontmatter |
| `Plugin name "<name>" is reserved: it passes as one of Anthropic's own` | rename |
| `Must be a version range such as ">=2.1.0"; got "<value>"` | `engines.claude-code` must be a semver range |
| `Unknown field '<key>'` | remove; ignored at load |
