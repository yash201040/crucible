---
type: "Guide"
title: "Connect the tools Claude needs"
description: "Prefer an existing CLI (e.g. gh) for external systems, use MCP when none exists, and trim idle MCP servers."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [mcp, cli, tools, gh, code-intelligence]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude mcp add --transport http"
  - "/mcp"
  - "--help"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

If an external system has a CLI, that is usually the easiest route (with `gh` installed and signed in, Claude opens pull requests and reads review comments unprompted; for an unfamiliar CLI, pointing Claude at `--help` is enough). For systems without a CLI, use MCP.

# How to use it

```bash
claude mcp add --transport http notion https://mcp.notion.com/mcp
```

The server then appears under `/mcp` in a session. Connected servers add tool names and instructions to context even when unused, so disable ones you do not need. In typed languages a code intelligence plugin lets Claude jump to definitions.
