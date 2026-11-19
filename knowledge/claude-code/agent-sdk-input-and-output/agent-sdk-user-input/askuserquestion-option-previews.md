---
type: "Feature"
title: "AskUserQuestion option previews (TypeScript)"
description: "toolConfig.askUserQuestion.previewFormat adds a markdown or html preview field to each option."
resource: "https://code.claude.com/docs/en/agent-sdk/user-input"
tags: [agent-sdk, askuserquestion, preview, typescript]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "toolConfig.askUserQuestion.previewFormat"
  - "preview"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-user-input"
    resource: "https://code.claude.com/docs/en/agent-sdk/user-input"
    title: "Handle approvals and user input"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A TypeScript option that makes Claude add a `preview` (visual mockup) to question options.

# How to use it

`options: { toolConfig: { askUserQuestion: { previewFormat: "html" } } }`

| `previewFormat` | `preview` contains |
| - | - |
| unset (default) | field absent; Claude does not generate previews |
| `"markdown"` | ASCII art and fenced code blocks |
| `"html"` | a styled `<div>` fragment; the SDK rejects `<script>`, `<style>` and `<!DOCTYPE>` before your callback runs |

# Notes

The format applies to all questions in the session. Claude includes `preview` only where a visual comparison helps (layouts, colors) and omits it for yes/no or text-only choices, so check for `undefined` before rendering.
