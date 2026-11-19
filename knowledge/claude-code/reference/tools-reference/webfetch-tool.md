---
type: "Feature"
title: "WebFetch tool behavior"
description: "URL fetch with a prompt-driven extraction step, caching, deadlines, domain permission prompts and availability controls."
resource: "https://code.claude.com/docs/en/tools-reference#webfetch-tool-behavior"
tags: [webfetch, web, caching, permissions, deadline]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "WebFetch"
  - "CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS"
  - "CLAUDE_CODE_WEBFETCH_DEADLINE_MS"
  - "CLAUDE_CODE_DISABLE_WEB_FETCH"
  - "WebFetch(domain:*)"
  - "allowManagedPermissionRulesOnly"
  - "allowedDomains"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Takes a URL and a prompt, converts HTML to Markdown, then (usually) runs the prompt over the content in a separate model call; Claude receives that result, so the tool is lossy by design. Use `curl` via Bash for the unprocessed page.

# How to use it

| Behavior | Value |
| :- | :- |
| Refused hosts | `localhost` and any hostname without a dot |
| HTTP URLs | upgraded to HTTPS |
| Content read | up to 100,000 characters per call (v2.1.290+ reports how much went unread) |
| Cache | 15 minutes by default; `CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS` (v2.1.233+) |
| Download deadline | 5 minutes including redirects; `CLAUDE_CODE_WEBFETCH_DEADLINE_MS` (v2.1.268+), `0` removes it |
| Cross-host redirect | returned as text naming both URLs; Claude fetches again |
| Overload | retried with backoff, then error result |
| Headers | `User-Agent` begins `Claude-User`; `Accept` prefers Markdown |

Permissions: in Manual and `acceptEdits` modes it prompts except for allowed or denied domains and a built-in preapproved documentation-domain set. Options: Yes (this fetch only), Yes and don't ask again for the domain (saves `WebFetch(domain:...)` in `.claude/settings.local.json`; hidden when `allowManagedPermissionRulesOnly` is set), No. Allow in advance with `WebFetch(domain:example.com)`; `WebFetch(domain:*)` allows all. `auto` and `bypassPermissions` skip the prompt except for a domain an explicit `ask` rule matches. An explicit rule overrides the preapproved set. Every fetch also passes the WebFetch domain safety check.

# Limits and defaults

- Set `CLAUDE_CODE_DISABLE_WEB_FETCH=1` (v2.1.285+) to turn WebFetch off.
- Team or Enterprise accounts not behind an LLM gateway depend on organization policy requested from `api.anthropic.com` at start; if it did not load, WebFetch is withheld (check `/status` or `claude doctor`) and returns once a policy allowing it loads.
- Sandboxed commands do not inherit the preapproved domains; add to `allowedDomains` or a `WebFetch(domain:...)` rule. WebFetch never reads the sandbox allowlist.
