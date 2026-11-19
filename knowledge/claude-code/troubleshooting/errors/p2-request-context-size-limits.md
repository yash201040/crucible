---
type: "Limit"
title: "Context, request size, image and PDF limits"
description: "Prompt is too long, request over 32MB, image dimension limits, resize failures and PDF limits, with compaction recovery behavior."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, context, compaction, limits, images]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "DISABLE_COMPACT"
  - "DISABLE_AUTO_COMPACT"
  - "autoCompactEnabled"
  - "/compact"
  - "/clear"
  - "/context"
  - "/rewind"
  - "/mcp disable <name>"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The request-size and context-window errors, and how Claude Code recovers from them.

# How to use it

| Error | Detail |
|---|---|
| `Prompt is too long` | Interactive text: `Context limit reached · /compact or /clear to continue` (only `/clear` if `DISABLE_COMPACT`); `-p` output stays `Prompt is too long`. Auto-compact is on by default; the `/config` toggle writes `autoCompactEnabled`. Bedrock wording `Input is too long for requested model.` handled since v2.1.217; gateway token `capability_rejected: prompt_too_long` since v2.1.228. Failed auto-compaction appends `· automatic compaction failed: <error>` (v2.1.229+). |
| Single-exchange conversation | Cannot be compacted; the message says whether content or system prompt/tools/attachments dominate (v2.1.162+). `/compact` answers `Not enough messages to compact.` |
| Last-resort compaction | Keeps newest prompt verbatim and summarizes the rest; skipped when carried content has no model reply and under about 1,000 tokens (v2.1.269+). |
| Custom `ANTHROPIC_BASE_URL` | Set the real context window or update to v2.1.299+ (before that the turn ended near an assumed 200K window). v2.1.304 fixed the error after stopping during compaction; v2.1.306 fixed hiding of 400/422 behind it on v2.1.305. |
| `Context exceeds the 200k-token limit by 94k tokens` | Shown by `/context`; a compaction-window variant reads `Context is 94k tokens past the 200k-token compaction window` (e.g. 200K boundary on 1M models). |
| `Request too large (max 32MB)` | Raw body limit before tokenization, separate from context. Measured forms: images/documents over limit (retried with them stripped), or messages alone over limit (`compacting cannot make it fit`, no retry; non-interactive says reduce input or start a new session). |
| `Image was too large` | API accepts up to 8000 px on the longest edge, or 3000 px when more than 20 images are in context. Related: `could not be processed and was removed`, `dimension limit for many-image requests (3000px)`. Fixes in v2.1.299 (image removal choice, SDK/VS Code/Desktop resizing) and v2.1.166. |
| `Unable to resize image` | Decode/resize failed (CMYK JPEG, animated WebP, damaged file); stated limit 2000x2000px (can read 2576x2576px). Use PNG, JPEG, GIF or WebP. |
| `Request rejected as unprocessable by the model` | 400; oldest images/documents are removed and resent (v2.1.290+). |
| PDF errors | `PDF too large (max 100 pages, 20MB)`, `PDF is password protected`, `The PDF file was not valid`; page-range reads need `pdftoppm` (poppler-utils). |

# Notes

Mitigations listed: `/context`, disabling unused MCP servers, trimming `CLAUDE.md`, path-scoped rules, referencing files by path.
