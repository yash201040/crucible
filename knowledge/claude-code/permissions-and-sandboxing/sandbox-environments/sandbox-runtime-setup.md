---
type: "Guide"
title: "Set up and launch the sandbox runtime"
description: "Install @anthropic-ai/sandbox-runtime, write ~/.srt-settings.json with write and network allowances, and launch with srt claude."
resource: "https://code.claude.com/docs/en/sandbox-environments"
tags: [sandboxing, sandbox-runtime, srt, unattended]
kind: "mixed"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: "bubblewrap, socat and ripgrep on Linux and WSL2; none extra on macOS"
identifiers:
  - "@anthropic-ai/sandbox-runtime"
  - "srt"
  - "srt claude"
  - "~/.srt-settings.json"
  - "--settings"
  - "CLAUDE_CODE_TMPDIR"
  - "skipWebFetchPreflight"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandbox-environments"
    resource: "https://code.claude.com/docs/en/sandbox-environments"
    title: "Choose a sandbox environment"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `@anthropic-ai/sandbox-runtime` package wraps an entire process in the same Seatbelt (macOS) or bubblewrap (Linux) isolation as the built-in Bash sandbox, so tools, hooks and MCP servers are constrained too. The docs call it a beta research preview whose configuration format may change. The same `srt` command can sandbox standalone MCP servers or helper processes.

# How to use it

1. Linux and WSL2: install `bubblewrap` and `socat` as for the built-in sandbox, and `ripgrep` from the distribution (Claude Code bundles it but the standalone runtime resolves it from PATH). macOS needs nothing extra.
2. Write config to `~/.srt-settings.json` or a file passed with `--settings` (schema in the package README). Default is no network and writes confined to built-in runtime paths.
3. Allow writes to the project directory, `~/.claude` and `~/.claude.json`, and the runtime-files directory: `/tmp` on Linux and WSL2, `/private/tmp` on macOS (`/tmp` is a symlink and Seatbelt checks the resolved path), unless `CLAUDE_CODE_TMPDIR` is set.
4. Allow network domains: `api.anthropic.com` or your provider endpoint (keep `api.anthropic.com` on a third-party provider because the WebFetch domain safety check still calls it unless `skipWebFetchPreflight: true`); `claude.ai` and `platform.claude.com` for OAuth sign-in and token refresh (API-key runs can drop these two).
5. On Linux and WSL2, write grants apply only to paths that already exist; create them first: `mkdir -p ~/.claude && { [ -f ~/.claude.json ] || echo '{}' > ~/.claude.json; }`
6. Install globally outside every writable path: `npm install -g @anthropic-ai/sandbox-runtime`
7. From the project directory run `srt claude`.

# Notes

See also the secure deployment guide for Agent SDK applications.
