---
type: "Feature"
title: "WebFetch domain rules"
description: "WebFetch rules use domain: with * wildcards; bare WebFetch and WebFetch(domain:*) differ for the sandbox and artifact reads."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, webfetch, domains, sandbox]
kind: "setting"
maturity: "unlabelled"
since: "2.1.172"
surfaces: [cli]
requires: ""
identifiers:
  - "WebFetch(domain:example.com)"
  - "WebFetch(domain:*.example.com)"
  - "WebFetch(domain:*)"
  - "WebFetch(domain:claude.ai)"
  - "Artifact"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`domain:` rules match the request hostname, case-insensitive, with `*` wildcards; a trailing `.` is stripped from rule and hostname. Wildcards need v2.1.172+ to match fetches.

# How to use it

- `WebFetch(domain:example.com)` matches that host only; add `WebFetch(domain:*.example.com)` for subdomains.
- `WebFetch(domain:*.example.com)` matches subdomains at any depth, not `example.com`.
- `WebFetch(domain:*)` matches every domain.
- In other positions a wildcard matches only text between two dots: `WebFetch(domain:example.*)` matches `example.org` but not `example.evil.com`.

| Rule | In `allow` | In `deny` |
| :- | :- | :- |
| `WebFetch` | Fetches without prompting; does not change hosts sandboxed commands can reach | Removes the `WebFetch` tool; no sandbox change |
| `WebFetch(domain:*)` | Fetches without prompting and sandboxed commands can reach any host | Tool kept, each fetch refused, sandboxed commands reach no host |

To fetch freely while keeping the sandbox allowlist, allow bare `WebFetch`; a sandboxed `curl` to an outside host still prompts. In auto mode Claude names the host in per-command allowed domains for the classifier.

# Notes

Artifact reads (pages the Artifact tool publishes on claude.ai): a bare `WebFetch` deny/ask does not apply (from v2.1.268; before it blocked or prompted each read). A `domain:` rule covering `claude.ai` or `*.claudeusercontent.com`, or an `Artifact` rule, does. The denial names the rule.
