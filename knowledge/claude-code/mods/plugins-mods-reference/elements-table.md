---
type: "Reference"
title: "Elements: props and which apps draw them"
description: "Table of Box, Text, Button, Link, Code, Markdown, Input, Select, Svg, Client, Raster and Image with main props and per-app support."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, elements, props, surfaces]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
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
  - "isInteractive"
  - "onLinkPress"
  - "pressableLinks"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Element | Main props | Terminal | Desktop | VS Code |
| :- | :- | :-: | :-: | :-: |
| `Box` | `key`, flex layout, `gap`/`padding`/`margin`, `width`, `height`, `minWidth`, `minHeight`, `borderStyle`, `borderColor`, `borderDimColor`, `backgroundColor`, `position`, `top`, `left`, `right`, `bottom`, `overflow`, `display`, `hover` | yes | yes | yes |
| `Text` | `color`, `backgroundColor`, `bold`, `italic`, `underline`, `strikethrough`, `dimColor`, `inverse`, `wrap`, `size`, `weight`, `mono`, `tabular`, `hover` | yes | yes | yes |
| `Button` | `key`, `label`, `children`, `onPress`, `hotkey`, `plain`, `dimColor`, `autoFocus`, `action`, `variant`, `role`, `hover` | yes | yes | yes |
| `Link` | `href`, `label` | yes | yes | yes |
| `Code` | `source`, `language`, `path`, `startLine`, `format`, `wrap` | yes | yes | yes |
| `Markdown` | `text`, `key`, `dimColor`, `onLinkPress`, `pressableLinks` | yes | yes | yes |
| `Input` | `key`, `label`, `placeholder`, `value`, `submitLabel`, `rows`, `onSubmit`, `onInput`, `autoFocus` | yes | yes | yes |
| `Select` | `key`, `label`, `options`, `value`, `onSelect`, `autoFocus` | yes | yes | yes |
| `Svg` | `source` SVG markup up to 131,072 characters, `alt`, `width`, `height`, `isInteractive` | no | yes | yes |
| `Client` | `module`, `key`, `props`, `width`, `height`, `flexGrow` | yes | yes | no |
| `Raster` | `key`, `columns` up to 512, `rows` up to 256, `cells` | yes | no | no |
| `Image` | `key`, `source` (PNG or RGBA bytes up to 2 MiB, or a file path), `columns` and `rows` up to 255, `alt` | yes | no | no |

# Limits and defaults

VS Code ignores some props (drawing the element as if omitted): `Box` `position`/`top`/`left`/`right`/`bottom`, `alignSelf`, `borderDimColor`, `hover`; `Text` `size`, `mono`, `tabular`, `hover`; `Button` `hotkey`, `plain`, `autoFocus`, `action`, `hover`, `variant`, `role` (user clicks or presses Enter); `Code` `language`, `path`, `startLine`, `format`, `wrap` (no colors/line numbers; diff shows raw text); `Input`/`Select` `autoFocus`, and `rows` on `Input`; `Svg` `isInteractive`.
