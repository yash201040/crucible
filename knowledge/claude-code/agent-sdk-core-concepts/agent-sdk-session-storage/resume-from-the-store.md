---
type: "Concept"
title: "Resume from the store"
description: "How resume and continue load a transcript from the store into a temporary config dir and what happens when the store has nothing."
resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
tags: [resume, continue, session-store, config-dir]
kind: "behavior"
maturity: "unlabelled"
since: "0.3.222"
surfaces: [sdk]
requires: ""
identifiers:
  - "resume"
  - "continue"
  - "continue_conversation"
  - "CLAUDE_CONFIG_DIR"
  - "enabledPlugins"
  - "extraKnownMarketplaces"
  - "additionalMarketplaces"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-session-storage"
    resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
    title: "Persist sessions to external storage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With a store and `resume`, or `continue: true` (TypeScript) / `continue_conversation=True` (Python), the SDK asks the store before spawning the subprocess: `resume` asks for the given ID; continue asks for the store's newest session. A returned transcript is written to a temporary config directory, the subprocess runs with `CLAUDE_CONFIG_DIR` pointing there, and the directory (with that run's local transcript) is deleted at run end.

# How to use it

Seeding the temp directory from your real config:
- TypeScript: credentials, `.claude.json`, user `settings.json`, minus `enabledPlugins`, `extraKnownMarketplaces`, its `additionalMarketplaces` alias and any `CLAUDE_CONFIG_DIR` in the file's `env` block. `apiKeyHelper` in settings works. Before v0.3.232 the alias was not stripped; before v0.3.222 only credentials and `.claude.json` were copied.
- Python: credentials and `.claude.json` only, so `apiKeyHelper` in user `settings.json` fails with `Not logged in`. An `apiKeyHelper` in managed or project settings still works.

# Limits and defaults

When the store has nothing: `resume` passes the ID through to the subprocess (local transcript resumed as without a store); TypeScript `continue: true` starts a fresh session; Python `continue_conversation=True` continues the newest local session.
