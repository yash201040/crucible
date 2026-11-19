---
type: "Reference"
title: "Artifact tool settings"
description: "enableArtifact turns off the Artifact tool; disableArtifact is its deprecated predecessor."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, artifacts, tools, deprecated]
kind: "setting"
maturity: "deprecated"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "enableArtifact"
  - "disableArtifact"
  - "CLAUDE_CODE_DISABLE_ARTIFACT"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Artifact tool publishes session output as a private web page on claude.ai. Both keys are any-file scope.

# How to use it

| Name | Values | Default | What it does |
| :- | :- | :- | :- |
| `enableArtifact` | Boolean | unset (follows account availability) | `false` turns the tool off for every session the file applies to. Every file can turn it off, none can turn it on; `true` equals unset and never overrides a `false` from another file, `CLAUDE_CODE_DISABLE_ARTIFACT` or the org admin setting. `/config` Artifacts row writes it to user settings and is hidden while another source keeps it off |
| `disableArtifact` | Boolean | unset | Deprecated, replaced by `enableArtifact`. `true` equals `enableArtifact: false` and no other file turns it back on; `false` is ignored. `CLAUDE_CODE_DISABLE_ARTIFACT=1` turns it off per session |
