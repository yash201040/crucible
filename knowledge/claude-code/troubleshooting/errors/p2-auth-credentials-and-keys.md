---
type: "Reference"
title: "Credential and API key errors"
description: "Errors for missing, invalid, blocked or policy-disabled credentials: Not logged in, apiKeyHelper failures, bad header values, disabled organizations."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, authentication, api-key, apikeyhelper, unattended]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop]
requires: ""
identifiers:
  - "ANTHROPIC_API_KEY"
  - "apiKeyHelper"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "ANTHROPIC_AUTH_TOKEN"
  - "ANTHROPIC_CUSTOM_HEADERS"
  - "CLAUDE_AGENT_SDK_CLIENT_APP"
  - "/status"
  - "/login"
  - "oauth_org_not_allowed"
  - "claude -p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The authentication section of the error reference (part 2). These errors mean Claude Code cannot prove identity to the API. `/status` shows which credential is active.

# How to use it

| Message | Cause | Fix |
|---|---|---|
| `Not logged in · Please run /login` | No valid credential. In the Desktop app it reads `Authentication required · Sign in again to continue`. | `/login`; for CI set `ANTHROPIC_API_KEY` or an `apiKeyHelper` script. An interactive session picks up a claude.ai login made in another window sharing the same config directory (before v2.1.286 on macOS it needed a restart). |
| `Could not resolve authentication method...` | Background and cloud sessions started a worker with no credential. Interactive, `-p` and SDK runs report it as Not logged in and log this string only in debug. | Upgrade to v2.1.176+ (v2.1.174 for idle pre-initialized background workers); set `ANTHROPIC_API_KEY`, `CLAUDE_CODE_OAUTH_TOKEN` or provider credentials in the worker's environment. |
| `Invalid API key · Fix external API key` | Key rejected by the API, or blocked locally because it holds a character headers can't carry. | Check for stale `.env`/direnv keys, unset it and `/login`, run the helper directly. |
| `Your apiKeyHelper script is failing` | Command errored, timed out, printed nothing, or printed more than the key. | Key must be one printable-ASCII token, up to 16,384 characters, exit code 0. Claude Code re-runs the script and retries up to two more times (three attempts). `/login` does not help because the helper takes precedence. In `-p` mode stderr is prefixed `apiKeyHelper failed:`. |
| `Claude Code didn't send your claude.ai login` forms | Managed settings problem: `Your organization's settings need an update...`, `Couldn't load your organization's settings...`, `Restart Claude Code to finish signing in.` | Admin fixes the API key helper configuration; `/status` shows the `Setting sources` line. |
| `Invalid auth token`, `Invalid ANTHROPIC_CUSTOM_HEADERS`, `Invalid request header from the environment` | A header value contains a line break, NUL byte or character above U+00FF. | Retype the variable; keep one `Name: Value` pair per line. The check runs for the direct API and LLM gateways, not for third-party cloud providers like Bedrock. |
| `Your ANTHROPIC_API_KEY belongs to a disabled organization` | Stale key from a disabled Console org overrides a saved login. In `-p` mode the key is always used when present. | Unset the key, `/login`. |
| `Your organization has disabled API key authentication` | Console admin disabled API keys (v2.1.169+). | Unset `ANTHROPIC_API_KEY` or `apiKeyHelper`, `/login`. |
| `Your organization has disabled Claude subscription access for Claude Code` | Server-side org setting; cannot be overridden locally. SDK and `-p` surface it as `oauth_org_not_allowed`. | Use a Console API key or ask the admin. |

# Notes

Environment variables and `apiKeyHelper` take precedence over `/login`. See [OAuth and login expiry errors](./p2-auth-oauth-login-expiry.md) for expiry cases.
