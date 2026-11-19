---
type: "Reference"
title: "Code Mode requirements"
description: "Version, account, organization, model, surface, installation and agent-teams requirements for Code Mode."
resource: "https://code.claude.com/docs/en/code-mode"
tags: [code-mode, requirements, models, agent-teams]
kind: "mixed"
maturity: "experimental"
since: "2.1.323"
surfaces: [cli]
requires: "v2.1.323+, Opus 5.5 / Sonnet 5.5 / Haiku 5.5 / Fable 5.2, native build"
identifiers:
  - "-p"
  - "--restricted"
  - "--tools"
  - "--disallowedTools"
  - "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-mode"
    resource: "https://code.claude.com/docs/en/code-mode"
    title: "Run tool calls from code with Code Mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

What must hold for Code Mode to start. Otherwise Claude Code starts without it and says why.

# Limits and defaults

| Requirement | Detail |
| - | - |
| Version | v2.1.323 or later, on either release channel (stable may need to catch up, or switch to latest) |
| Account | Claude subscription or Console account. Not through a gateway, Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, Microsoft Foundry or Claude Models on Google Cloud (Anthropic managed) |
| Organization | Not the HIPAA configuration, not zero data retention |
| Model | Claude Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable 5.2 |
| Surface | Interactive `claude` in a terminal. Not `-p`, not the Agent SDK, VS Code panel, Desktop app or cloud sessions |
| Agent teams | With agent teams on, v2.1.326 or later. Teammates run in Code Mode in the default in-process display mode; they start without it in split panes |
| Installation | The native build |
| Windows | Git for Windows installed |

Also blocked by settings such as an API key helper, OpenTelemetry export or `DISABLE_TELEMETRY` (see [troubleshooting](./code-mode-troubleshooting.md)). Launch options: do not use `--restricted`; `REPL` must be in `--tools` if given and not in `--disallowedTools` or `deny` rules.
