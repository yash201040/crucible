---
type: "Feature"
title: "REVIEW.md and CLAUDE.md for Code Review"
description: "Commit REVIEW.md and CLAUDE.md files to tune what Code Review flags: severity calibration, nit caps, skipped paths, extra checks, subdirectory files."
resource: "https://code.claude.com/docs/en/code-review-customize"
tags: [code-review, review-md, claude-md, customization]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Code Review service (Team or Enterprise)"
identifiers:
  - "REVIEW.md"
  - "CLAUDE.md"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-customize"
    resource: "https://code.claude.com/docs/en/code-review-customize"
    title: "Customize Code Review"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`CLAUDE.md` is read by the service as project context: a change violating its rules becomes a finding at a fitting severity. The service reads the root `CLAUDE.md` and `CLAUDE.md` files in parent directories of each changed file (a subdirectory's when the PR changes a file under it). `REVIEW.md` at the repo root is freeform Markdown for review-only rules; its content goes to both the finding and verifying agents and is consulted when setting severity and writing the summary. It changes what is found and reported, not the review format.

The local `/code-review` command reads `CLAUDE.md` but not `REVIEW.md`; put guidance for both in `CLAUDE.md`.

# How to use it

Typical instructions: redefine what 🔴 Important means, cap nits ("report at most five Nits per review"), list paths and categories to skip (generated code, lockfiles, vendored dependencies, what CI enforces), add always-check rules ("new API routes have an integration test"), require evidence (a `file:line` citation) before a class of finding. Keep general project context in `CLAUDE.md`.

# Limits and defaults

Subdirectory `REVIEW.md` files (protected branch only) add checks for that subtree on top of the root file, but are ignored in or below directories named (whole-name, any case, any depth): tests (`test`, `tests`, `__tests__`, `testdata`, `fixtures`, `__fixtures__`, `golden`, `corpus`, `snapshots`, `__snapshots__`), examples (`example`, `examples`, `sample`, `samples`, `demo`, `demos`), `generated`, and third-party (`vendor`, `third_party`, `third-party`, `thirdparty`, `node_modules`, `bower_components`, `external`, `extern`, `deps`, `godeps`, `pods`, `carthage`, `site-packages`, `contrib`). Applied subdirectory files share a 150,000-byte limit (root file not counted); the check run reports files that did not fit.

# Notes

Changes to review behavior need the `REVIEW.md` change merged first, since it is read from the base or default branch. See [branch protection](./review-md-branch-protection.md) and [includes](./review-md-includes-and-skills.md).
