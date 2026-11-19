---
type: "Feature"
title: "Cross-session messaging overview"
description: "Claude can list and message your other Claude Code sessions via ListAgents and SendMessage; version and provider requirements."
resource: "https://code.claude.com/docs/en/cross-session-messaging"
tags: [messaging, sessions, sendmessage, listagents]
kind: "tool"
maturity: "unlabelled"
since: "2.1.224"
surfaces: [cli, ide, desktop, cloud]
requires: "v2.1.224+ on macOS, Linux, WSL 2; v2.1.234+ on native Windows"
identifiers:
  - "SendMessage"
  - "ListAgents"
  - "/list-agents"
  - "/peers"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cross-session-messaging"
    resource: "https://code.claude.com/docs/en/cross-session-messaging"
    title: "Message your other Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A message is a piece of plain text one Claude writes to another, never the sender's history or files. Claude finds targets with `ListAgents` and sends with `SendMessage`; you never call them yourself. Claude can send unprompted (for example after a change affecting another session) or on request. Use cases: hand over a finding, coordinate parallel worktrees, get status from long-running work, reach sessions on other machines or in the cloud. To move a whole conversation, resume the session instead. When requirements are met it is on with nothing to enable.

# How to use it

Prompt examples (Claude writes the message): `Ask the session running in my other terminal whether the migration finished`. To name a target type `@` plus the first letters of a session name and pick it (v2.1.232+), e.g. `Let @api-worker know the schema migration finished`; names with spaces or other characters need quotes: `@"release notes"`. Typeahead lists live sessions on this machine; cloud and Remote Control sessions appear only after Claude has listed or messaged them. With several live sessions of the same name Claude asks which.

`/list-agents` (also `/peers`) shows what Claude can reach; `/status` has a `Peer address` row (prefixed `uds:`) or `unavailable` plus reason.

# Limits and defaults

Availability: on every provider for same-machine messaging, including Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, Microsoft Foundry and with feature-flag fetching off, but then it needs v2.1.248+. Sessions beyond this machine need Remote Control and a claude.ai sign-in as active auth; not available with API key or those providers. `/list-agents` not recognised means the session lacks the feature (check `claude --version`); if it works but a send did not arrive: deny rules, receiving session's inbound controls, cloud/other-machine session missing (needs Remote Control on both), `offline`, `can't receive cross-session messages`, a paused long exchange, or older sessions beyond a bounded number of paged results.
