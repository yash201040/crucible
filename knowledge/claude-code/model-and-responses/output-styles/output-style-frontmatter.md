---
type: "Reference"
title: "Output style frontmatter fields"
description: "Frontmatter fields name, description, keep-coding-instructions and force-for-plugin, with parse-error behavior."
resource: "https://code.claude.com/docs/en/output-styles#frontmatter-reference"
tags: [output-styles, frontmatter, plugins]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "name"
  - "description"
  - "keep-coding-instructions"
  - "force-for-plugin"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "output-styles"
    resource: "https://code.claude.com/docs/en/output-styles"
    title: "Output styles"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

YAML frontmatter between `---` markers at the top of a style file. All fields optional; names are lowercase words separated by hyphens.

# How to use it

| Field | Required | Description |
| :- | :- | :- |
| `name` | No | Name shown in the `/config` picker. Default: the file name |
| `description` | No | Description shown in the `/config` picker |
| `keep-coding-instructions` | No | `true` keeps Claude Code's built-in software engineering instruction section alongside your style. Default: `false` |
| `force-for-plugin` | No | Plugin styles only. `true` applies the style automatically when the plugin is enabled, overriding the user's `outputStyle`; if several enabled plugins set it, the first loaded is used. Default: `false` |

# Limits and defaults

- A misspelled field is ignored without error. If the YAML does not parse, the style still loads under its file name with no fields set; run `claude --debug` to see the error.
