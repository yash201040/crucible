---
type: "Concept"
title: "Artifacts overview"
description: "An artifact is a live, interactive page Claude Code publishes from a session to a private claude.ai URL that updates in place."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, publishing, claude-ai]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: "Pro, Max, Ultra, Team or Enterprise plan; session signed in with /login"
identifiers:
  - "/login"
  - "Artifact"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An artifact is a live web page that Claude Code publishes from your session to a private URL on claude.ai. It opens in a browser and updates in place as the session continues. It can be kept private, shared with an organization, or published to a public link.

It is a capture of work: one self-contained page with no backend, so it cannot serve several routes. For a hosted internal tool with a backend, deploy on your own infrastructure instead.

# How to use it

Use an artifact when terminal text is the wrong medium: annotated PR walkthroughs, dashboards from data the session pulled, side-by-side options, an investigation timeline that fills in during a long task, a link to send a teammate instead of pasting output, or a status board that pulls fresh data through MCP connectors.

Claude may publish one on its own, or you ask in plain language ("Make an artifact that walks through this PR with the diff annotated inline."). Prompt patterns the page lists: walk through a change, compare alternatives, tune with interactive controls, bring the result back to the session (an export control such as a "Copy as prompt" button), and track work in progress (a checklist republished as work proceeds).

# Notes

- Generating a page costs output tokens; styled pages cost more than the same text. To cut cost: prefer SVG or HTML/CSS over embedded raster images, omit unneeded interactivity, and have the page summarize large datasets instead of inlining them.
- See [Availability](./availability-requirements.md), [page constraints](./page-constraints.md) and [sharing](./share-and-edit.md).
