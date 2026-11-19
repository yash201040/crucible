---
type: "Feature"
title: "Design guidance, templates and /design"
description: "Built-in design skill, design-system precedence, Google Fonts rule, account templates, the /design command and Claude Docs."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, templates, design, claude-docs]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.265"
surfaces: [cli, web]
requires: "Template turned on for the org on Team/Enterprise; Docs and Sheets need the Claude Docs connector; /design needs Claude Code v2.1.265+"
identifiers:
  - "/design"
  - "claude.ai Claude Docs"
  - "/mcp"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude applies a built-in design skill and first looks for an existing design system in the project. Record tokens (colors, typography, spacing) in CLAUDE.md or a theme file. Precedence: your prompt, then your design system, then Claude's own choices. Claude can load a typeface from Google Fonts (the one external font source); other typefaces are inlined as `@font-face` data URIs with fallback stacks.

Artifact templates on your claude.ai account also work from Claude Code (Claude Design, Claude Docs, possibly Sheets, Whiteboards, Data). Ask Claude to list the templates available. To get a file instead, name the format such as `.csv`.

# How to use it

- `/design <brief>` (for example `/design a settings screen for a mobile banking app`) drafts artboards on one canvas published as a Claude Design artifact. Review in a desktop browser; edits save automatically; export each artboard as PNG or PDF.
- Claude Docs arrives as a claude.ai connector listed in `/mcp` as `claude.ai Claude Docs`. Requests for a document meant for others go there instead of an artifact page. A document that belongs in the codebase (a README) stays a file; name `.docx` or Markdown to get a file.

# Limits and defaults

Requirements: artifacts available; on Team and Enterprise the template enabled by an Owner (Organization settings > Artifacts); on Enterprise with custom roles, a role including the template; Docs and Sheets need the Claude Docs connector (turn it back on if disabled).
