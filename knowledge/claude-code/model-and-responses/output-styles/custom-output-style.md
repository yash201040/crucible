---
type: "Feature"
title: "Create a custom output style"
description: "A custom style is a Markdown file with frontmatter and instructions, stored at user, project, managed or plugin level."
resource: "https://code.claude.com/docs/en/output-styles#create-a-custom-output-style"
tags: [output-styles, custom, plugins, managed-settings]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: "VS Code menu file creation needs v2.1.261+"
identifiers:
  - "~/.claude/output-styles"
  - ".claude/output-styles"
  - "output-styles/"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "output-styles"
    resource: "https://code.claude.com/docs/en/output-styles"
    title: "Output styles"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A custom output style is a Markdown file: frontmatter for metadata, then instructions for Claude. The file name becomes the style name unless `name` is set.

# How to use it

Save at one of three levels:
- User: `~/.claude/output-styles`
- Project: `.claude/output-styles`
- Managed policy: `.claude/output-styles` inside the managed settings directory

Plugins can also ship styles in an `output-styles/` directory. Then switch with `/output-style <style>` or `/config` > **Output style**. Example:

```markdown
---
name: Diagrams first
description: Lead every explanation with a diagram
keep-coding-instructions: true
---

When explaining code, architecture, or data flow, start with a Mermaid diagram ...
```

# Limits and defaults

- Project styles load from every `.claude/output-styles/` between the working directory and the repository root; for the same name the one closest to the working directory wins.
- In the terminal, style files are read at startup: restart Claude Code after creating or editing one in a running session.
- In VS Code you can create the file from the Output styles menu (v2.1.261+).
