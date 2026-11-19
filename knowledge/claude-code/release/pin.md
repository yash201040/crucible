---
type: "Release Pin"
title: "Which Claude Code release this bundle describes"
description: "The bundle was built from the documentation as of release 2.1.328 (fetched 2026-11-19); experiments ran on 2.1.325 and 2.1.329."
resource: "https://code.claude.com/docs/en/changelog"
tags: [release, pin, refresh]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "2.1.328"
  - "manifest.json"
  - "crucible_okf.py refresh"
orchestration: "high"
status: "stable"
generated: { by: "claude-code/fable-5.2", at: "2026-11-20T00:00:00Z" }
sources:
  - id: "llms-full"
    resource: "https://code.claude.com/docs/llms-full.txt"
    title: "Claude Code documentation, full text"
    last_modified: "2026-11-19T19:48:42Z"
  - id: "llms-index"
    resource: "https://code.claude.com/docs/llms.txt"
    title: "Claude Code documentation index"
stale_after: "2027-01-19T00:00:00Z"
---

# What is pinned

| What | Value |
| --- | --- |
| Release the documentation described | 2.1.328 (November 19, 2026) |
| Documentation fetched | 2026-11-19T19:48:42Z, from the full-text file the documentation site publishes for agents |
| Pages | 205 English pages, each with its URL, its place in the documentation's own index, size and SHA-256 in [manifest.json](/manifest.json) |
| Release notes read | 2.1.101 to 2.1.328, without the bug-fix sections; see [releases](/releases/) |
| Release channels that day | stable 2.1.311, latest 2.1.328, next 2.1.329 |
| Installed where the experiments ran | 2.1.325 at first; it updated itself to 2.1.329 during the work |

The documentation site is not versioned: it always describes the latest release. The pin is therefore the fetch time, the newest release in the release notes at that time, and a hash per page.[^llms-full]

# How to see what changed since

    python3 scripts/crucible_okf.py refresh

It downloads the documentation again into a cache outside the repository and prints: the releases newer than the pin (their notes are written to one file), the pages whose text changed, new pages and removed pages, and how many concepts belong to the changed pages. It changes nothing in the bundle.

# How to bring the bundle up to date

1. Read the release notes since the pin first. Most of what matters to crucible is announced there.
2. Re-read only the changed and new pages and rewrite their concepts (one reader per group of pages; the reader instructions are in [the bundle's log](/log.md)).
3. Re-run the experiments in [experiments](/experiments/) whose subject changed: a result there holds only for the release it ran on.
4. Rebuild the indexes, write the new manifest, and add an entry to the log.

[^llms-full]: Claude Code documentation, full text
