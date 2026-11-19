---
type: "Reference"
title: "Gallery: Text, Markdown, Link, Code and Box"
description: "Sample usage and rendering notes for the display elements Text, Markdown, Link, Code (including diff) and Box."
resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
tags: [mods, elements, text, code, layout]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "Text"
  - "Markdown"
  - "Link"
  - "Code"
  - "Box"
  - "format: 'diff'"
  - "startLine"
  - "borderStyle"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-gallery"
    resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
    title: "Interface gallery for mods"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Element | Usage | Notes |
| :- | :- | :- |
| `Text` | `Text({ children: ['...'] })` with props `bold`, `italic`, `underline`, `strikethrough`, `dimColor`, `inverse`, `color`, `backgroundColor` | `dimColor` draws gray; `backgroundColor` fills only as wide as the text |
| `Markdown` | `Markdown({ text: '## Title\n...' })` | content goes in `text`, not `children`; headings bold without `#`, inline code colored, quotes italic with a bar |
| `Link` | `Link({ href, label })` | terminal draws label then URL as text; whether a click opens it depends on the terminal |
| `Code` | `Code({ language, startLine, source })` or `path` to infer language | colors come from the user's theme; `startLine` numbers lines from that number |
| `Code` diff | `Code({ format: 'diff', source: '@@ -1,3 +1,3 @@ ...' })` | `source` is one or more unified diff hunks; line numbers replace the `@@` line; changed words get a stronger shade |
| `Box` | `Box({ flexDirection, gap, columnGap, paddingX, borderStyle: 'round', children })` | lays out in row or column; border stretches to pane width |

# Limits and defaults

In the VS Code extension, `Code` shows `source` as plain text: no colors, line numbers or diff shading.
