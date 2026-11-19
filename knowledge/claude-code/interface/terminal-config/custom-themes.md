---
type: "Feature"
title: "Themes and custom color themes"
description: "Pick a theme with /theme and define custom themes as JSON files in ~/.claude/themes with a base preset and color token overrides."
resource: "https://code.claude.com/docs/en/terminal-config"
tags: [themes, colors, interface, customization]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/theme"
  - "~/.claude/themes/"
  - "custom:<slug>"
  - "name"
  - "base"
  - "overrides"
  - "claude"
  - "text"
  - "inverseText"
  - "inactive"
  - "subtle"
  - "suggestion"
  - "permission"
  - "remember"
  - "success"
  - "error"
  - "warning"
  - "merged"
  - "promptBorder"
  - "planMode"
  - "autoAccept"
  - "bashBorder"
  - "ide"
  - "fastMode"
  - "effortUltra"
  - "diffAdded"
  - "diffRemoved"
  - "diffAddedDimmed"
  - "diffRemovedDimmed"
  - "diffAddedWord"
  - "diffRemovedWord"
  - "userMessageBackground"
  - "userMessageBackgroundHover"
  - "bashMessageBackgroundColor"
  - "memoryBackgroundColor"
  - "selectionBg"
  - "composerSidebarBackground"
  - "rate_limit_fill"
  - "rate_limit_empty"
  - "briefLabelYou"
  - "briefLabelClaude"
  - "<color>_FOR_SUBAGENTS_ONLY"
  - "rainbow_<color>"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "terminal-config"
    resource: "https://code.claude.com/docs/en/terminal-config"
    title: "Configure your terminal for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/theme` (or the picker in `/config`) chooses a Claude Code theme; the auto option follows the terminal's light or dark background. Custom themes appear in the list, as do themes contributed by plugins. Select **New custom theme...** to create one; `Ctrl+E` edits the highlighted one.

# How to use it

A custom theme is a JSON file in `~/.claude/themes/`; the filename without `.json` is the slug and selecting it stores `custom:<slug>`.

| Field | Meaning |
| :- | :- |
| `name` | Display label; defaults to the slug |
| `base` | `dark`, `light`, `dark-daltonized`, `light-daltonized`, `dark-ansi`, `light-ansi`; default `dark` |
| `overrides` | Map of token to color; other tokens fall through to base |

Color values: `#rrggbb`, `#rgb`, `rgb(r,g,b)`, `ansi256(n)`, `ansi:<name>`. Unknown tokens and invalid values are ignored. Files are watched and reload live; restart once if the folder did not exist at startup.

Token groups: text/accent (`claude`, `text`, `inverseText`, `inactive`, `subtle`, `suggestion`, `permission`, `remember`); status (`success`, `error`, `warning`, `merged`); input and modes (`promptBorder`, `planMode`, `autoAccept`, `bashBorder`, `ide`, `fastMode`, `effortUltra` - the `ultracode` tag, override works on v2.1.239+); diffs (`diffAdded`, `diffRemoved`, `diffAddedDimmed`, `diffRemovedDimmed`, `diffAddedWord`, `diffRemovedWord`); fullscreen backgrounds (`userMessageBackground`, `userMessageBackgroundHover`, `bashMessageBackgroundColor`, `memoryBackgroundColor`, `selectionBg`, `composerSidebarBackground`; the first three of that group besides hover/selection/sidebar paint in both renderers, the last three only in fullscreen); usage meter and labels (`rate_limit_fill`, `rate_limit_empty`, `briefLabelYou`, `briefLabelClaude`).

# Notes

- Shimmer pairs: `claude`/`claudeShimmer`, `warning`/`warningShimmer`, `permission`/`permissionShimmer`, `promptBorder`/`promptBorderShimmer`, `inactive`/`inactiveShimmer`, `fastMode`/`fastModeShimmer`.
- Subagents and parallel tasks use eight named colors via `<color>_FOR_SUBAGENTS_ONLY` where color is `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan`; a subagent with `color: blue` uses `blue_FOR_SUBAGENTS_ONLY`.
- `ultrathink` renders as a rainbow using `rainbow_<color>` and `rainbow_<color>_shimmer` (`red`, `orange`, `yellow`, `green`, `blue`, `indigo`, `violet`).
