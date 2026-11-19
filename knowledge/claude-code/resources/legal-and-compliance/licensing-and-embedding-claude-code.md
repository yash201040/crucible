---
type: "Concept"
title: "Licensing and offering Claude Code in products"
description: "Which terms govern Claude Code and the conditions for preinstalling or running it in your own products or hosted sandboxes."
resource: "https://code.claude.com/docs/en/legal-and-compliance"
tags: [legal, license, embedding, terms, sandboxes]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: "Commercial Terms of Service for embedding"
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "legal-and-compliance"
    resource: "https://code.claude.com/docs/en/legal-and-compliance"
    title: "Legal and compliance"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Use is under the Commercial Terms of Service (Team, Enterprise, Claude API users) or Consumer Terms of Service (Free, Pro, Max, Ultra). Via Claude API (1P) or Amazon Bedrock / Google Cloud's Agent Platform (3P), the existing commercial agreement applies unless otherwise agreed.

# How to use it

Preinstalling or running Claude Code in your products or services (for example hosted sandboxes or other agent infrastructure) requires agreeing to the Commercial Terms of Service and these conditions:
- The Claude Code binary must not be modified; it must be installed and run as published, and no built-in authentication method (Claude account sign-in or the user's own API key) may be removed, disabled or restricted.
- Customers may not pay for, resell or intermediate Claude usage on end users' behalf. Each end user authenticates with their own Anthropic API key, Claude subscription credentials, or 3P provider credential (Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry), billed to the end user.

# Notes

Naming: you may say in plain text that your product has Claude Code preinstalled or runs it. You may not use Claude Code or Anthropic names or logos in your product, feature or company name, your logo, or in a way suggesting Anthropic built, endorses or partners with it; other use is under the Trademark Guidelines and needs written permission. Claude Code remains under Anthropic's standard terms regardless of platform.
