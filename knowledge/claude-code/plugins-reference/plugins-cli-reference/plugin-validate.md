---
type: "Feature"
title: "claude plugin validate"
description: "Validates a plugin or marketplace manifest or component files with exit codes 0, 1 and 2, optional --strict and a --json report for CI."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, validate, ci, json]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.259"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude plugin validate"
  - "--strict"
  - "--json"
  - "Validation passed"
  - "Validation passed with warnings"
  - "Validation failed"
  - "Validation failed (--strict treats warnings as errors)"
  - "Unexpected error during validation: <reason>"
  - "success"
  - "strict"
  - "target"
  - "manifest"
  - "contents"
  - "gatingHooks"
  - "hasCatch"
  - "advice"
  - "installLine"
  - ".claude-plugin/marketplace.json"
  - ".claude-plugin/plugin.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin validate <path> [options]` checks a plugin manifest, a marketplace manifest, or the skills, agents and commands in a directory, with exit codes a CI job can act on.

# How to use it

| Flag | Description |
| :- | :- |
| `--strict` | Treat warnings as errors (unrecognized fields and missing metadata the runtime tolerates then fail) |
| `--json` | Report as one JSON object, same exit codes. v2.1.259 or later |

**Directory targeting**: given a directory it validates `.claude-plugin/marketplace.json` if present, else `.claude-plugin/plugin.json`, else component files by directory name (`skills`, `agents`, `commands`: files inside; `.claude`: the three directories inside; any other: those three under its `.claude`). With both marketplace and plugin manifests it validates the marketplace and also the plugin manifest and component files (v2.1.289 or later).

**Manifest file targeting**: a file not named `plugin.json`/`marketplace.json` and not in `.claude-plugin` is validated as a marketplace if `plugins` is an array, `plugins` and `owner` are both present, or it has a marketplace-only field (e.g. `owner`) and no plugin-only field (e.g. `author`); otherwise as a plugin manifest. Any other file in a `.claude-plugin` directory is a plugin manifest.

| Exit code | Verdict line | Meaning |
| :- | :- | :- |
| `0` | `Validation passed` or `Validation passed with warnings` | Manifest loads; with `--strict` no warnings either |
| `1` | `Validation failed` or `Validation failed (--strict treats warnings as errors)` | Error, or a warning under `--strict`; advice never counts |
| `2` | `Unexpected error during validation: <reason>` | Validator failure (e.g. unreadable path); nothing on stdout, message on stderr |

`--json` top-level fields: `success`, `strict`, `target`, `manifest` (or `null` without a manifest), `contents` (per-file `file`, `errors`, `warnings`, `notes`; files without issues get no entry; for marketplace plus plugin the `manifest` is the marketplace result), `gatingHooks` (inside `contents`: per mod hook that can refuse an action such as `tool.call`, `module`, `pattern`, `hook`, `hasCatch`; v2.1.290 or later), `advice` (v2.1.295 or later).

# Limits and defaults

- Symlinks are not followed: a linked `skills`/`agents`/`commands` directory under the root warns nothing was read; linked entries inside are skipped with a warning; naming a symlinked directory (or symlinked `.claude` parent) is an error and checks nothing.
- Not read: a plugin-root `SKILL.md`; a plugin-root `CLAUDE.md` is warned about; in a marketplace run, files of plugins listed from other directories (validate each plugin directory).

# Notes

Advice is covered in [README install advice](./validate-readme-advice.md).
