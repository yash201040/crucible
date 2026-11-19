---
type: "Feature"
title: "Remote Control overview and requirements"
description: "Remote Control lets claude.ai/code or the Claude mobile app drive a Claude Code session that keeps running on your own machine."
resource: "https://code.claude.com/docs/en/remote-control"
tags: [remote-control, sessions, requirements, mobile]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide, web, mobile]
requires: "Pro, Max, Ultra, Team or Enterprise plan with claude.ai login; not API keys"
identifiers:
  - "claude remote-control"
  - "claude --remote-control"
  - "/remote-control"
  - "/rc"
  - "ANTHROPIC_BASE_URL"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "CLAUDE_CODE_DISABLE_FEATURE_FLAGS"
  - "DISABLE_TELEMETRY"
  - "DO_NOT_TRACK"
  - "disableRemoteControl"
  - "remoteControlAtStartup"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "remote-control"
    resource: "https://code.claude.com/docs/en/remote-control"
    title: "Continue local sessions from any device with Remote Control"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Remote Control connects claude.ai/code or the Claude iOS/Android app to a Claude Code session running on your machine. Claude keeps running locally (filesystem, MCP servers, tools, project config stay local); the web/mobile UI is a window into it, so the machine must stay on and the `claude` process must keep running. Conversation plus subagent and dynamic-workflow progress stay in sync across all connected devices. Files and photos can be sent from phone or browser (non-image files are downloaded to the machine and passed as `@` references). It reconnects automatically after sleep or network loss. Unlike cloud sessions, nothing runs in the cloud.

# Requirements

| Requirement | Detail |
|---|---|
| Plan | Pro, Max, Ultra, Team, Enterprise. API keys not supported. Team/Enterprise: an Owner must enable the Remote Control toggle in Claude Code admin settings |
| Custom roles | Enterprise custom roles need both the cloud sessions permission and the "Claude Code remote control" permission |
| Auth | claude.ai `/login`. Without it `claude remote-control` exits with an error, while `claude --remote-control` starts an interactive session with Remote Control off |
| Endpoint | Not available on Amazon Bedrock, Google Cloud Agent Platform, Microsoft Foundry, with `ANTHROPIC_BASE_URL` pointing away from api.anthropic.com (LLM gateway/proxy), or via a Claude apps gateway |
| Feature flags | `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` or `CLAUDE_CODE_DISABLE_FEATURE_FLAGS` make it unavailable. `DISABLE_TELEMETRY` or `DO_NOT_TRACK` alone keep it available (needs v2.1.283+, or v2.1.304+ in Claude Desktop) unless the org requires Trusted Devices |
| Workspace trust | In an untrusted directory `claude remote-control` asks `Trust <directory>? [y/N]`; with non-terminal stdin/stdout it exits with a `Workspace not trusted` error. Trust is never saved for the home directory |

# Limits and defaults

- Not available to organizations with Zero Data Retention or the HIPAA configuration.
- Session transcript (messages, responses, tool activity) is stored on Anthropic servers while connected; execution stays local.
- Turn off entirely with the `disableRemoteControl` setting.
- Auto-connect for every interactive session: `/config` toggle "Enable Remote Control for all sessions" (values `true`, `false`, `default`) or setting `remoteControlAtStartup`. A `true` in project/local settings is ignored (cannot be forced via a checked-in file); a `false` there is honored. Each interactive process registers one remote session.
- Comparison of ways to work away from the terminal (Dispatch, Remote Control, Channels, Slack, self-hosted environments, scheduled tasks) is given as a table on the page.
