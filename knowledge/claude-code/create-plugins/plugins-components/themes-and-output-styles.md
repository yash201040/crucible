---
type: "Reference"
title: "Plugin themes and output styles"
description: "Plugins can ship color themes and output styles that appear in /theme and /output-style, with the manifest keys that replace the folder scan."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, themes, output-styles]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "themes/<slug>.json"
  - "output-styles/<name>.md"
  - "experimental.themes"
  - "outputStyles"
  - "/theme"
  - "/output-style"
  - "keep-coding-instructions"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin can include color themes and output styles; both appear in the same pickers as the user's own. Setting the manifest key replaces the folder scan.

# How to use it

| Component | Save as | Format | Appears in | Manifest key |
| :- | :- | :- | :- | :- |
| Theme | `themes/<slug>.json` | custom theme file format (`name`, `base`, `overrides`) | `/theme` under the file's `name` | `experimental.themes` |
| Output style | `output-styles/<name>.md` | custom output style, `name` and `description` frontmatter (example also uses `keep-coding-instructions`) | `/output-style` as `<plugin>:<name>` | `outputStyles` |

# Limits and defaults

Plugin themes are read-only; editing one in `/theme` saves a copy in the user's own themes directory.
