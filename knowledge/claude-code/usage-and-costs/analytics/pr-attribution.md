---
type: "Concept"
title: "PR attribution algorithm"
description: "How merged PRs are matched against Claude Code sessions: time window, normalization, exclusions, and the claude-code-assisted label."
resource: "https://code.claude.com/docs/en/analytics"
tags: [analytics, attribution, pull-requests, github, label]
kind: "behavior"
maturity: "beta"
since: ""
surfaces: [web]
requires: "Claude for Teams or Enterprise with contribution metrics enabled"
identifiers:
  - "claude-code-assisted"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "analytics"
    resource: "https://code.claude.com/docs/en/analytics"
    title: "Track team usage with analytics"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When contribution metrics are enabled, Claude Code analyzes each merged PR by matching Claude Code session activity against the code in the PR.

# How to use it

On merge: (1) added lines are extracted from the PR diff; (2) Claude Code sessions that edited matching files within a time window are identified; (3) PR lines are matched against Claude Code output with multiple strategies; (4) metrics are computed for AI-assisted and total lines.

Before comparison lines are normalized: whitespace trimmed, multiple spaces collapsed, quotes standardized, lowercased.

Merged PRs with Claude Code-assisted lines get the GitHub label `claude-code-assisted`. To query contribution data through GitHub, search for PRs with that label.

# Limits and defaults

- Time window: sessions from 21 days before to 2 days after the PR merge date. Sessions outside it are ignored.
- Excluded as auto-generated: lock files (package-lock.json, yarn.lock, Cargo.lock and similar), generated code (Protobuf outputs, build artifacts, minified files), build dirs (dist/, build/, node_modules/, target/), test fixtures (snapshots, cassettes, mock data), and lines over 1,000 characters.
- Code rewritten by developers by more than 20% difference is not attributed.
- Source and destination branch of the PR are not considered.
