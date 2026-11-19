---
type: "Reference"
title: "Element tree: elements and where they draw"
description: "A ui.render hook returns an element tree built from $.ui.resolve(e); table of main elements, props and which apps draw them."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, elements, tree, jsx]
kind: "ui"
maturity: "unlabelled"
since: "2.1.326"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "$.ui.resolve"
  - "Box"
  - "Text"
  - "Button"
  - "Link"
  - "Code"
  - "Markdown"
  - "Input"
  - "Select"
  - "Svg"
  - "Client"
  - "Raster"
  - "Image"
  - "overflowX"
  - "maxLines"
  - "ui.message"
  - "ui.fault"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The hook returns an element tree. Get element functions with `const { Box, Text, Button } = $.ui.resolve(e)`; pass props, with children in `children`. A `.tsx` or `.jsx` module may use JSX after destructuring.

| Element | Draws | Where |
| :- | :- | :- |
| `Box` | flex container: `flexDirection`, `borderStyle`, `width`, `overflowX`; spacing props take a number or step `'xs'` to `'xl'`. `overflowX` needs v2.1.326+ | Everywhere |
| `Text` | styled text: `color`, `bold`, `dimColor`, `italic`, `wrap` (`'wrap'`, `'truncate'`, `'truncate-start'`, `'truncate-middle'`, `'truncate-end'`, `'clip'`), `maxLines`, `weight`. `maxLines` and `'clip'` need v2.1.326+ | Everywhere |
| `Button` | control calling `onPress` | Everywhere |
| `Link`, `Code`, `Markdown` | link (`href`, `label`), code block, Claude-reply formatted text; `Markdown` takes `text` and needs a `key` with `onLinkPress` | Everywhere |
| `Input`, `Select` | text field, dropdown | Terminal, Desktop, VS Code |
| `Svg` | SVG document | Desktop, VS Code |
| `Client` | region drawn by a second file; that file gets no mods API; posts data arriving as `ui.message`; failure fires `ui.fault` | Terminal, Desktop |
| `Raster`, `Image` | cell grid, picture | Terminal |

# Limits and defaults

A tree with a prop an element does not take, or a child where none goes, makes the hook fail with a `hook skipped` line, e.g. `my-mod: ui.render hook skipped: returned the wrong shape (a tree Pane refuses: Text prop "bogusProp" is not allowed)`. In Desktop and VS Code a `Link` draws as plain text unless `href` is `https:` or `http://localhost`, has no `@` (use `%40`), and equals `new URL(href).href` apart from a missing `/` after the host (no uppercase host, space, or `:443` on https). In the terminal, when a `Client`'s file fails, a dim line such as `my-mod: Client client/spinner.js: boom` takes its place; if the mod handles `ui.fault`, Claude Code redraws the site afterwards.
