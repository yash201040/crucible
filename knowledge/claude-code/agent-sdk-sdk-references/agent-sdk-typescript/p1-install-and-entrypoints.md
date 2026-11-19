---
type: "Guide"
title: "TypeScript SDK install, bundling and entry points"
description: "How the TypeScript Agent SDK installs with a bundled native Claude Code binary, compiles to one executable, and offers a /core entry for bundlers."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [install, bundling, binary, entrypoint]
kind: "mixed"
maturity: "unlabelled"
since: "0.3.144"
surfaces: [sdk]
requires: "Node, Bun or Deno runtime; /core entry needs SDK v0.3.282+ and TypeScript 5.0+"
identifiers:
  - "@anthropic-ai/claude-agent-sdk"
  - "@anthropic-ai/claude-agent-sdk-darwin-arm64"
  - "@anthropic-ai/claude-agent-sdk/extract"
  - "@anthropic-ai/claude-agent-sdk/core"
  - "extractFromBunfs()"
  - "pathToClaudeCodeExecutable"
  - "bun build --compile"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The npm package `@anthropic-ai/claude-agent-sdk` ships a native Claude Code binary for the platform as an optional dependency (for example `@anthropic-ai/claude-agent-sdk-darwin-arm64`). Most installs need no separate Claude Code install. The SDK version tracks the bundled Claude Code version: SDK v0.3.191 bundles Claude Code v2.1.191, so a feature that needs a Claude Code version needs the SDK with the same patch number or later.

# How to use it

- Install: `npm install @anthropic-ai/claude-agent-sdk`.
- If a package manager skips optional dependencies, the SDK throws `Native CLI binary for <platform>-<arch> not found`. Set `pathToClaudeCodeExecutable` to a separately installed `claude` binary.
- Yarn 1.x ignores npm's `libc` field and installs both glibc and musl packages on Linux (about double size). On SDK v0.2.141+ the SDK still launches the right one. To shrink a container image delete the unused one, e.g. `rm -rf node_modules/@anthropic-ai/claude-agent-sdk-linux-x64-musl` for glibc x64.
- `bun build --compile`: `require.resolve` fails inside the `$bunfs` virtual filesystem, so embed the platform binary (`import binPath from "@anthropic-ai/claude-agent-sdk-darwin-arm64/claude" with { type: "file" }`), call `extractFromBunfs(binPath)` from `@anthropic-ai/claude-agent-sdk/extract`, and pass the result as `pathToClaudeCodeExecutable`. `extractFromBunfs()` needs SDK v0.3.144+; it copies the binary to a per-user temp dir and returns the input path unchanged outside a compiled executable.
- Each compiled executable embeds one platform binary; match the import to `--target`. To cross-compile install the other platform package, e.g. `npm install @anthropic-ai/claude-agent-sdk-linux-x64 --force`. On Windows the subpath is `claude.exe`.

# Limits and defaults

`/core` entry (`@anthropic-ai/claude-agent-sdk/core`) is for apps that bundle the SDK with their own dependencies. Requires SDK v0.3.282+ and TypeScript 5.0+. It exports `query()`, `startup()`, `prewarm()` (alpha, needs v0.3.314+ from /core), `tool()`, `createSdkMcpServer()`, `resolveSettings()`, the session rename/tag/delete functions, `AbortError`, runtime constants and every type. It leaves out `InMemorySessionStore` and the helpers that list, read, fork, import and summarize sessions. The root entry inlines `zod` and `@modelcontextprotocol/sdk`; `/core` imports them from your `node_modules` at the `peerDependencies` ranges. Import from root or `/core` in one process, never both (two copies of classes and state).
