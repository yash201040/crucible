---
type: "Feature"
title: "Offer a file download"
description: "A page offers generated files (CSV, PNG) through the downloads capability because the viewer blocks self-started downloads."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, downloads, capability]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [web]
requires: "downloads runtime capability enabled per account"
identifiers: []
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An artifact can give viewers a file it generates, such as a CSV of a table or a PNG of a chart, saved through a download control (a button). File downloads are a runtime capability claude.ai enables per account; Claude checks before building the control and declares the downloads capability when publishing (which triggers an approval prompt).

# How to use it

Ask for the control and format: "Add a button that downloads this table as a CSV file."

# Limits and defaults

The artifact viewer blocks any download the page starts itself, including links to `data:` or `blob:` URLs. Buttons built that way must be rebuilt with the downloads capability.
