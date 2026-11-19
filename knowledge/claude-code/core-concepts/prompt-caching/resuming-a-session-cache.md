---
type: "Concept"
title: "Resuming a session and the cache"
description: "A resumed session resends the whole conversation and reads whatever prefix is unchanged and within cache lifetime."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, resume, system-prompt, append-system-prompt]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--append-system-prompt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On resume Claude Code sends the whole conversation again; the request reads from cache whatever prefix is unchanged and within the cache lifetime.

# Limits and defaults

The system prompt would change after a Claude Code upgrade or with different `--append-system-prompt` text on the resume. By default the resumed conversation keeps the system prompt it started with, so history stays behind the same prompt; the change takes effect after compaction or in a new conversation. The CLI reference section "System prompt flags in resumed conversations" covers cases where Claude Code rebuilds the prompt on every request. A resume costs most after the cache has expired.
