---
type: "Feature"
title: "MCP elicitation requests"
description: "Servers ask for structured input mid-task via form or URL mode dialogs; hook auto-response, cloud cards and declared capabilities."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, elicitation, hooks, interactive]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli, cloud, desktop]
requires: ""
identifiers:
  - "Elicitation"
  - "elicitation: {form: {}, url: {}}"
  - "elicitation: {}"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

No configuration needed: when a server asks for input, a dialog appears in the terminal and the answer goes back to the server. Form mode shows server-defined fields; URL mode asks whether to open a link in your browser (for sign-in and similar).

# How to use it

- Auto-respond without a dialog with the `Elicitation` hook.
- Cloud sessions: answer on the card at claude.ai/code or in the Desktop app's Code tab (Form: fill and Submit; URL: Open link, finish, click "I'm done, continue"; or Decline). With no card, you cannot answer there; stop the turn in your own session.

# Limits and defaults

- URL mode passes the URL as a command-line argument to the system URL handler; over the cap you can only decline. Each character needing escaping (such as `%` or `&`) counts four times: a plain URL reaches the cap near 8,000 characters, one with every third char a `%` near 4,000.
- Declared client capability: `elicitation: {form: {}, url: {}}` on protocol revision 2026-07-28 connections and on earlier-revision (2025-11-25 and older) connections to stdio, `sse`, `http`, `ws` servers in the user's MCP configuration (v2.1.287 or later); the bare `elicitation: {}` (form only) on other earlier-revision connections such as claude.ai connectors. A server on Java MCP SDK 0.17.0 or earlier may reject the form-and-url declaration.
