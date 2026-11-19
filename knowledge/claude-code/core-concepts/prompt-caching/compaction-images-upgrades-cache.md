---
type: "Feature"
title: "Compaction, images and upgrades vs cache"
description: "Compaction rebuilds the conversation cache, many images get oldest removed in batches, and upgrades rebuild from the top."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, compaction, images, upgrade, idle-compaction]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.290"
surfaces: [cli]
requires: "idleCompaction needs v2.1.290 or later"
identifiers:
  - "/compact"
  - "/rewind"
  - "idleCompaction"
  - "DISABLE_AUTOUPDATER"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three more actions that cost an uncached turn.

# How to use it

**Compaction.** Replaces message history with a summary, invalidating the conversation layer. System prompt layer reads from cache if current; if out of date (e.g. after resume) it rebuilds once. Project context is reloaded from disk and rebuilt even if files are unchanged. The summarization is a separate request repeating system prompt, tools and history plus a summarization instruction; while the cache is warm it reads the prefix from cache (cheap), after a break longer than the cache lifetime it reprocesses all history uncached, so `/compact` costs most when resuming an old session. Run it at natural breaks; to abandon a path use `/rewind` instead (truncates to an already-cached prefix).

**Idle compaction.** A long conversation left idle on the one-hour TTL can be compacted. Set `idleCompaction` to `false` to turn it off (v2.1.290+).

**Images.** The API limits images and PDFs per request, and Claude Code also caps their total size. When the next request would pass either limit, it removes a batch of the oldest images and PDFs; Claude can no longer see them (share again if needed). The conversation is reprocessed from the earliest changed message, giving one slower turn per batch.

**Upgrading.** A new version typically changes the system prompt or tool definitions, so the first conversation after an upgrade builds its cache from the top. Auto-update applies on next launch, never mid-session. Set `DISABLE_AUTOUPDATER=1` to control when upgrades apply.
