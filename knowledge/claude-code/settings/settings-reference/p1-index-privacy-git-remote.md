---
type: "Reference"
title: "Index: privacy, git and remote keys"
description: "Settings keys for transcript retention, surveys, attribution, PR links, Remote Control, desktop sessions, SSH and notifications (index rows only)."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [privacy, git, remote-control, notifications]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "cleanupPeriodDays"
  - "desktopSessionCleanupPeriodDays"
  - "feedbackDrafts"
  - "feedbackSurveyRate"
  - "skipWebFetchPreflight"
  - "attribution"
  - "attribution.commit"
  - "attribution.pr"
  - "attribution.sessionUrl"
  - "includeCoAuthoredBy"
  - "includeGitInstructions"
  - "prUrlTemplate"
  - "agentPushNotifEnabled"
  - "awaySummaryEnabled"
  - "disableArtifact"
  - "enableArtifact"
  - "disableDeepLinkRegistration"
  - "disableDesktopLocalSessions"
  - "disableRemoteControl"
  - "disableRemotePreviewScripts"
  - "inputNeededNotifEnabled"
  - "preferredNotifChannel"
  - "remote.defaultEnvironmentId"
  - "remoteControlAtStartup"
  - "sshConfigs"
  - "sshHostAllowlist"
  - "sshHostCommands"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Index entries from "Privacy and telemetry", "Git and attribution" and "Remote, desktop, and notifications". Detailed sections are in other parts of the page.

# How to use it

| Key | Scope | What it does |
| :- | :- | :- |
| `cleanupPeriodDays` | Any file | Days Claude Code keeps transcripts before deleting them |
| `desktopSessionCleanupPeriodDays` | User or managed | Age limit in days for Claude Desktop and Cowork transcripts |
| `feedbackDrafts` | User or managed | Whether Claude queues feedback drafts for review |
| `feedbackSurveyRate` | Any file | How often the session quality survey appears |
| `skipWebFetchPreflight` | Any file | Skip the WebFetch hostname check when Anthropic is unreachable |
| `attribution` | Any file | Customize attribution on commits and pull requests |
| `attribution.commit` | Any file | Change or hide the commit trailer |
| `attribution.pr` | Any file | Change or hide the PR description attribution line |
| `attribution.sessionUrl` | Any file | Omit the claude.ai session link from cloud and Remote Control commits |
| `includeCoAuthoredBy` | Any file | Deprecated; use `attribution` |
| `includeGitInstructions` | Any file | Remove the built-in commit and PR instructions from context |
| `prUrlTemplate` | Any file | Point PR links at an internal code-review tool |
| `agentPushNotifEnabled` | Any file | Let Claude push-notify your phone when it decides to |
| `inputNeededNotifEnabled` | Any file | Push notification when Claude waits on you |
| `preferredNotifChannel` | Any file | Terminal bell or desktop notification on task completion |
| `awaySummaryEnabled` | Any file | Turn off the session recap shown on return |
| `remoteControlAtStartup` | Any file | Connect Remote Control automatically at session start |
| `disableRemoteControl` | Any file | Turn off Remote Control everywhere it can start |
| `remote.defaultEnvironmentId` | Any file | Default cloud environment for `claude --cloud`; a self-hosted `ccpool_` ID is read only from user and managed settings and `--settings` |
| `disableDesktopLocalSessions` | Managed | Turn off Desktop Code sessions that run on the device |
| `disableRemotePreviewScripts` | Managed | Turn off scripts in Desktop HTML previews in SSH and WSL sessions |
| `disableDeepLinkRegistration` | Any file | Stop registering the `claude-cli://` handler |
| `enableArtifact` | Any file | A `false` in any file turns the Artifact tool off; no file can turn it back on |
| `disableArtifact` | Any file | Deprecated; use `enableArtifact` |
| `sshConfigs` | User or managed | Add SSH connections to the Desktop environment selector |
| `sshHostCommands` | User or managed | SSH connections whose host comes from a command |
| `sshHostAllowlist` | Managed | Limit which hosts Desktop SSH sessions can reach |
