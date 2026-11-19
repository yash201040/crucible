---
type: "Feature"
title: "Live data from MCP connectors"
description: "A published page can call claude.ai MCP connectors on each view, using the viewer's own connections."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, mcp, connectors, live-data]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.209"
surfaces: [cli, web]
requires: "Pro, Max, Ultra, Team or Enterprise; Claude Code v2.1.209+; connectors from the claude.ai account"
identifiers:
  - "claude.ai/customize/connectors"
  - "Enable artifact connectors"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An artifact can call MCP connectors each time someone views it, so it shows current data. On earlier versions than v2.1.209 the page holds only data gathered while building. Claude declares at publish which connectors the page may call, and the page cannot call others. Only claude.ai account connectors qualify; local MCP servers (such as from `.mcp.json`) can supply data while building but the published page cannot call them.

# How to use it

Name the connector and data in the prompt, for example a dashboard of open PRs "through my GitHub connector when the page loads". The page fetches on load and can refresh on an interval or via a refresh control; responses are cached in the viewer's browser, so a reopened page renders cached data first, then updates.

Viewer rules:
- Each viewer's own connectors are used, so two viewers may see different data; the page never sees credentials (claude.ai makes the calls).
- claude.ai asks each viewer permission before the first call. A viewer who declines or lacks the connector sees the page without live sections. A denial lasts for that page load.
- Actions with side effects (post a message, update an issue) run on the account of whoever selects the control.
- Connector calls do not run for a public-link viewer who is not signed in or is outside the organization.

Ask Claude to add a fallback message per live section naming the connector.

# Limits and defaults

Empty live sections for an org viewer: connector not connected (add at claude.ai/customize/connectors, reload), permission declined, org toggle **Enable artifact connectors** off, or the page calls tool names the connector does not expose. From v2.1.265, Claude Code checks declared tool names against the session's available connector tools, warns about mismatches and refuses the publish when none match; before v2.1.265 it published unchecked.
