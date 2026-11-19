---
type: "Reference"
title: "Interface, account, install and integration commands"
description: "Commands for appearance, terminal setup, sign-in, IDE, desktop, cloud, Slack and GitHub integration, feedback, diagnostics, plus removed commands."
resource: "https://code.claude.com/docs/en/commands"
tags: [slash-commands, ui, account, integrations, removed]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/artifacts"
  - "/autofix-pr"
  - "/bug"
  - "/share"
  - "/feedback"
  - "/chrome"
  - "/color"
  - "/desktop"
  - "/app"
  - "/design-login"
  - "/focus"
  - "/heapdump"
  - "/help"
  - "/ide"
  - "/insights"
  - "/install-github-app"
  - "/install-slack-app"
  - "/keybindings"
  - "/login"
  - "/logout"
  - "/mobile"
  - "/ios"
  - "/android"
  - "/passes"
  - "/powerup"
  - "/pr-comments"
  - "/privacy-settings"
  - "/radio"
  - "/release-notes"
  - "/remote-control"
  - "/rc"
  - "/remote-env"
  - "/restart"
  - "/update"
  - "/scroll-speed"
  - "/setup-bedrock"
  - "/setup-vertex"
  - "/statusline"
  - "/stickers"
  - "/team-onboarding"
  - "/teleport"
  - "/tp"
  - "/terminal-setup"
  - "/theme"
  - "/tui"
  - "/ultraplan"
  - "/upgrade"
  - "/vim"
  - "/voice"
  - "/web-setup"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "commands"
    resource: "https://code.claude.com/docs/en/commands"
    title: "Commands"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The remaining commands: display and terminal setup, authentication, integrations and feedback, plus commands marked removed.

# How to use it

| Command | What it does |
| :- | :- |
| `/artifacts` | List artifacts you own or that are shared with you; attach, open or copy link |
| `/autofix-pr [prompt]` | Spawn a cloud session that watches the branch's PR and pushes fixes for CI failures and review comments; PR found with `gh pr view`; needs `gh` and cloud session access |
| `/bug [report]` | Report a bug or share the conversation after a consent screen; goes to Anthropic when signed in first-party, else written to a local archive under `~/.claude/feedback-bundles/`. In the VS Code extension it opens the extension's dialog (v2.1.229+). Opens at once mid-response (before v2.1.232 it queued). Alias `/share`; before v2.1.212 both were aliases of `/feedback` |
| `/feedback [report]` | Product feedback via the same dialog and consent as `/bug`; with Claude-drafted feedback and no argument it opens the drafts queue |
| `/chrome` | Configure Claude in Chrome settings |
| `/color [color\|default]` | Prompt bar color: `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan`; no argument picks randomly; syncs to claude.ai/code with Remote Control; works with `-p` |
| `/desktop` | Continue the session in the Desktop app; macOS or x64 Windows, Claude subscription. Alias `/app` |
| `/design-login` | Authorize design-system access for `/design-sync` with a claude.ai account (standalone Claude Design site closes by December 14, 2026) |
| `/focus` | Toggle the focus view (last prompt, one-line tool summary, final response); fullscreen rendering only; `/focus [on\|off]` from Remote Control needs v2.1.281+ |
| `/heapdump` | Write a heap snapshot and memory breakdown to `~/Desktop` (or home on Linux); share only the `-diagnostics.json`, the `.heapsnapshot` contains the conversation and credentials. Hidden from the menu |
| `/help` | Help and available commands |
| `/ide` | Manage IDE integrations and status |
| `/insights` | HTML report analyzing recent sessions on this machine; not in cloud sessions |
| `/install-github-app` | Install the Claude GitHub App for a github.com repository, optionally GitHub Actions workflows and secrets; on gitlab.com or bitbucket.org it prints a notice and exits |
| `/install-slack-app` | Install the Claude Slack app via browser OAuth |
| `/keybindings` | Open the keyboard shortcuts file |
| `/login`, `/logout` | Sign in or out of the Anthropic account |
| `/mobile` | QR code for the mobile app. Aliases `/ios`, `/android` |
| `/passes` | Share a free week of Claude Code; visible only if eligible |
| `/powerup` | Interactive lessons with animated demos |
| `/pr-comments [PR]` | Removed in v2.1.91; ask Claude directly |
| `/privacy-settings` | Privacy settings for Pro, Max and Ultra subscribers |
| `/radio` | Open Claude FM lo-fi radio in the browser |
| `/release-notes` | Changelog version picker; notes do not enter the conversation Claude sees |
| `/remote-control` | Make this session available to Remote Control from claude.ai; needs a claude.ai subscription. Alias `/rc` |
| `/remote-env` | Default cloud environment for cloud sessions started from the CLI |
| `/restart` | Restart and resume the session to apply an update; Pro, Max or Ultra, native install on macOS or Linux (not WSL); v2.1.288+. Alias `/update` |
| `/scroll-speed` | Mouse wheel scroll speed; fullscreen only, not in the JetBrains terminal |
| `/setup-bedrock` | Amazon Bedrock auth, region and model pins wizard; hidden until `CLAUDE_CODE_USE_BEDROCK=1` |
| `/setup-vertex` | Google Cloud Agent Platform wizard; hidden until `CLAUDE_CODE_USE_VERTEX=1` |
| `/statusline` | Configure the status line, or auto-configure from the shell prompt |
| `/stickers` | Check sticker availability |
| `/team-onboarding` | Onboarding guide from the past 30 days of usage; Team and Enterprise subscribers also get a share link |
| `/teleport` | Pull a cloud session into this terminal; needs a claude.ai subscription. Alias `/tp` |
| `/terminal-setup` | Shift+Enter keybinding for VS Code, Cursor, Devin Desktop, Alacritty, Zed; Option+Enter and bell in Apple Terminal; clipboard access in iTerm2 |
| `/theme` | Color theme: `auto`, light and dark, daltonized, ANSI, custom themes from `~/.claude/themes/` or plugins |
| `/tui [classic\|fullscreen]` | Set the renderer and relaunch; `classic` accepted on v2.1.327+ (`default` earlier); no argument prints the active renderer |
| `/ultraplan <prompt>` | Removed; use plan mode |
| `/upgrade` | Open the upgrade page; prints the URL when no browser (v2.1.323+); not shown on Enterprise |
| `/vim` | Removed in v2.1.92; use `/config` then Editor mode |
| `/voice [hold\|tap\|off]` | Toggle voice dictation; needs a Claude.ai account |
| `/web-setup` | Connect GitHub for cloud sessions using local `gh` credentials |
