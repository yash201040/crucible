---
type: "Guide"
title: "Claude Code in Slack setup and routing"
description: "Install the Claude Slack app, link your account and choose Code only or Code + Chat routing so @Claude mentions start cloud sessions."
resource: "https://code.claude.com/docs/en/slack"
tags: [slack, setup, routing, cloud-sessions]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cloud, web]
requires: "Pro, Max or Ultra plan; workspace not connected to Claude Tag; cloud sessions; GitHub repo"
identifiers:
  - "/invite @Claude"
  - "Routing Mode"
  - "Code only"
  - "Code + Chat"
  - "Connect Claude account"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "slack"
    resource: "https://code.claude.com/docs/en/slack"
    title: "Claude Code in Slack"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

This earlier Claude Code in Slack answers channel @mentions only from Pro, Max and Ultra accounts, and only in a workspace no organization has connected to Claude Tag. Each session runs under the individual user's Claude account, repositories and plan limits. Team/Enterprise should use Claude Tag (organization shared identity with admin-configured access). The legacy bot is retired effective October 5, 2026 for workspaces connected to a Claude organization; it replies with a retirement notice instead.

When mentioned with a coding task, Claude creates a Claude Code cloud session and posts progress to the thread.

# How to use it

1. A workspace admin installs the Claude app from the Slack App Marketplace.
2. Each user: App Home > **Connect Claude account**, finish auth in browser.
3. Sign in at claude.ai/code with the same account, connect GitHub, authenticate at least one repo.
4. Set **Routing Mode** in App Home: `Code only` (all @mentions go to Claude Code) or `Code + Chat` (Claude routes between Claude Code and chat). In Code + Chat, click **Switch to code repo...** on a chat reply to start a coding session.
5. Invite Claude to each channel with `/invite @Claude`; it is not added automatically and answers only in channels where added.

# Limits and defaults

- Channels only (public or private); does not work in direct messages.
- GitHub repositories only; each session can create one pull request; cloud session access required.
- Context: from a thread, its messages; from a channel, recent messages plus channel name, topic and description. Claude may follow directions in that context, so use only in trusted conversations. Paste teammate text such as error reports into the mention.
- Sessions count against the user's plan limits and appear in claude.ai/code history; on Team/Enterprise they are visible to the org.
