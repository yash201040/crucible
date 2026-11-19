---
type: "Limit"
title: "Trusting a mod: what it can reach and validate before install"
description: "A mod is unsandboxed code with the user's permissions; claude plugin validate lists its hooks and calls without running it."
resource: "https://code.claude.com/docs/en/plugins/mods/overview"
tags: [mods, security, trust, validate]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "claude plugin validate ./some-mod"
  - "cc-plugin-sec-default"
  - "hooks:"
  - "calls:"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-overview"
    resource: "https://code.claude.com/docs/en/plugins/mods/overview"
    title: "Mods overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod runs with your permissions inside Claude Code. Once loaded it can: read and write files anywhere your account can, start programs, make network requests; read secrets in environment variables and settings files; see every prompt and tool call; rewrite prompts or tool calls, submit a prompt as if typed, or message another of your sessions; approve a tool call before you are asked; call a model on your plan or API key.

# Limits and defaults

- Mods are not sandboxed. With sandboxing on, only Bash commands Claude runs are isolated; a process a mod starts runs outside it.
- A mod can approve many tool calls that `deny` or `ask` rules or `PreToolUse` hooks would stop, unless the built-in guard prevents it. With the guard loaded, by default a user's mod cannot. `cc-plugin-sec-default` on the **Installed** tab of `/plugin` (local terminal session) means the guard is loaded.
- A mod cannot change what the permission prompt shows.

# How to use it

Before installing, get the plugin's files and run `claude plugin validate ./some-mod`; the `hooks:` and `calls:` lines list events handled and what it asks Claude Code to do, without running it.
