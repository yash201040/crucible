---
type: "Guide"
title: "Examples: GitHub and PostgreSQL servers"
description: "Worked commands for GitHub's remote MCP server with a PAT header and a DBHub stdio server for PostgreSQL."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, examples, github, database]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "https://api.githubcopilot.com/mcp/"
  - "@bytebase/dbhub"
  - "--dsn"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

GitHub (fine-grained personal access token as header; `claude mcp add` does not validate credentials, so a bad token only fails at connect, with the HTTP status such as 401 in the failure detail):

```
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

PostgreSQL via DBHub (use a read-only database user in the DSN):

```
claude mcp add --transport stdio db -- npx -y @bytebase/dbhub --dsn "postgresql://readonly:pass@prod.db.com:5432/analytics"
```

Verify with `/mcp` (checkmark on the row).
