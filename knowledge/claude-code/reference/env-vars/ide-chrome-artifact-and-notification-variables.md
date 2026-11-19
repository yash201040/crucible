---
type: "Reference"
title: "IDE, Chrome, artifact, notification and Code Mode variables"
description: "Variables for IDE auto-connect, Claude in Chrome, artifact publishing, push notifications, prompt suggestions, recaps and the experimental Code Mode."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [ide, artifacts, notifications, code-mode]
kind: "env_var"
maturity: "experimental"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "CLAUDE_CODE_AUTO_CONNECT_IDE"
  - "CLAUDE_CODE_IDE_HOST_OVERRIDE"
  - "CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL"
  - "CLAUDE_CODE_IDE_SKIP_VALID_CHECK"
  - "CLAUDE_CODE_ENABLE_CFC"
  - "CLAUDE_CODE_DISABLE_CFC_PROMPT"
  - "CLAUDE_CODE_ARTIFACT_AUTO_OPEN"
  - "CLAUDE_CODE_ARTIFACT_COMMENTS"
  - "CLAUDE_CODE_ARTIFACT_COMMENTS_AUTOREACT"
  - "CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS"
  - "CLAUDE_CODE_DISABLE_ARTIFACT"
  - "CLAUDE_CLIENT_PRESENCE_FILE"
  - "CLAUDE_CODE_DISABLE_NOTIFICATION_PRESENCE_CHECK"
  - "CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION"
  - "CLAUDE_CODE_ENABLE_AWAY_SUMMARY"
  - "CLAUDE_REMOTE_CONTROL_SESSION_NAME_PREFIX"
  - "CLAUDE_CODE_EXPERIMENTAL_CODE_MODE"
  - "DISABLE_COST_WARNINGS"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Integration switches. Only `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE` carries the docs' "experimental" label.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_AUTO_CONNECT_IDE` | `false` prevents automatic IDE connection from a supported IDE's terminal; `true` forces an attempt when detection fails (for example tmux hides the parent terminal). Beats the `autoConnectIde` setting. |
| `CLAUDE_CODE_IDE_HOST_OVERRIDE` | Host address for the IDE extension connection (auto-detected, including WSL-to-Windows routing). |
| `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL` | `1` stops `/ide` installing the extension; same as `autoInstallIdeExtension: false`. Before v2.1.318 Claude Code also installed or updated the extension on start in VS Code, Cursor or Devin Desktop terminals; this variable stops that too. |
| `CLAUDE_CODE_IDE_SKIP_VALID_CHECK` | `1` skips validation of IDE lockfile entries (use when auto-connect cannot find a running IDE). |
| `CLAUDE_CODE_ENABLE_CFC` | `1` starts a CLI session with Chrome integration on, `0` off. Beats `claudeInChromeDefaultEnabled`; `--chrome` and `--no-chrome` beat both. `1` is ignored in project and local settings. |
| `CLAUDE_CODE_DISABLE_CFC_PROMPT` | For hosts supplying their own browser guidance: `1` keeps Claude in Chrome tools but omits the Chrome system prompt section and the `/claude-in-chrome` bundled skill (VS Code extension v2.1.314+ also omits it from messages). Requires v2.1.257+. |
| `CLAUDE_CODE_ARTIFACT_AUTO_OPEN` | `0` stops opening the browser when an artifact is published. |
| `CLAUDE_CODE_ARTIFACT_COMMENTS` | `0` stops Claude reading and replying to artifact comments; no effect when `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` turned artifacts off. Requires v2.1.221+. |
| `CLAUDE_CODE_ARTIFACT_COMMENTS_AUTOREACT` | `0` stops Claude replying on its own to comments sent to it. Requires v2.1.228+. |
| `CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS` | `0` stops applying small changes to an artifact file as part of publishing; Claude edits with file tools and publishes separately. Requires v2.1.300+. |
| `CLAUDE_CODE_DISABLE_ARTIFACT` | `1` turns off the Artifact tool (private web page on claude.ai); no settings file turns it back on. From a settings file use `enableArtifact: false`; deprecated `disableArtifact` also works. |
| `CLAUDE_CLIENT_PRESENCE_FILE` | Path of a file an external tool (such as a screen-lock listener) creates on unlock and deletes on lock; while it exists Claude Code skips Remote Control mobile push notifications. Absent or unreadable: notifications sent. Checked once per push-triggering event. Requires v2.1.181+. |
| `CLAUDE_CODE_DISABLE_NOTIFICATION_PRESENCE_CHECK` | `1` sends the `PushNotification` desktop notification even while you type or the terminal is focused; the server may still suppress mobile push. Requires v2.1.193+. |
| `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` | `false` turns off prompt suggestions (beats `promptSuggestionEnabled`). Suggestions pause near or at the usage limit; `true` keeps that pause from applying until the limit is reached. Requires v2.1.238+. |
| `CLAUDE_CODE_ENABLE_AWAY_SUMMARY` | `0` forces session recaps off; `1` forces on when `awaySummaryEnabled` is `false`. Beats the setting and the `/config` toggle. |
| `CLAUDE_REMOTE_CONTROL_SESSION_NAME_PREFIX` | Prefix for auto-generated Remote Control session names (default the hostname, giving names like `myhost-graceful-unicorn`). The `--remote-control-session-name-prefix` flag sets it for one invocation. |
| `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE` | `1` starts sessions in Code Mode (experimental); `0` keeps it off; set in managed settings to block it for an organization. Does not count in every settings file. Needs feature flags and version and account requirements. |
| `DISABLE_COST_WARNINGS` | `1` disables cost warning messages. |
