---
type: "Feature"
title: "Define a custom tool"
description: "Build a tool from name, description, input schema and handler with tool() or @tool, wrapped in an in-process MCP server."
resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
tags: [custom-tools, mcp, in-process, schema]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "tool()"
  - "@tool"
  - "createSdkMcpServer"
  - "create_sdk_mcp_server"
  - "content"
  - "structuredContent"
  - "isError"
  - "is_error"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-custom-tools"
    resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
    title: "Give Claude custom tools"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Custom tools are your own functions Claude can call, served by the SDK's in-process MCP server (runs inside your application, not as a separate process).

# How to use it

A tool has four parts, passed to `tool()` (TypeScript) or the `@tool` decorator (Python):

| Part | Meaning |
| --- | --- |
| Name | Unique identifier Claude calls |
| Description | Claude reads it to decide when to call |
| Input schema | TypeScript: Zod schema (`.describe()` adds field descriptions). Python: dict like `{"latitude": float}`, `Annotated[float, "desc"]` for descriptions, or a full JSON Schema dict (needed for enums, ranges, optional fields, nested objects) |
| Handler | Async function receiving validated args; returns `content` (required array of blocks with type `text`, `image`, `audio`, `resource` or `resource_link`), optional `structuredContent`, optional `isError` |

Wrap tools in `createSdkMcpServer({ name, version, tools })` / `create_sdk_mcp_server(name=, version=, tools=[...])`. One server holds many tools.

Optional parameter: TypeScript `.optional()` on the Zod field; Python dict schema requires every key, so use the JSON Schema form, leave the key out of `required`, and read with `args.get()`. Apply defaults in the handler.

# Notes

Python examples that make HTTP requests use httpx. See [calling and permissions](./call-custom-tool-and-access.md), [errors](./handle-tool-errors.md) and [result content](./tool-result-content.md).
