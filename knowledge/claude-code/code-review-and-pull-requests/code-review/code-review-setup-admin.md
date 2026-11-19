---
type: "Guide"
title: "Code Review pointers to admin setup"
description: "Where Code Review is turned on, who can start reviews, and which pages hold setup, customization, costs and troubleshooting."
resource: "https://code.claude.com/docs/en/code-review"
tags: [code-review, admin, setup]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Owner role in the Claude organization"
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review"
    resource: "https://code.claude.com/docs/en/code-review"
    title: "Code Review"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An index of the Code Review doc set: set up (requirements, GitHub App, repositories, review level, when reviews run), customize (`REVIEW.md` and `CLAUDE.md`), read and request reviews (severities, comment commands), troubleshoot, and costs.

# How to use it

An Owner of the Claude organization turns it on. Who can start a review: where automatic, opening or pushing to a PR (except drafts and forks); a comment command only from a person with write access. Code Review may keep an earlier result after some pushes.

# Notes

Related: GitHub Enterprise Server connection, the shared GitHub App permission set, and Anthropic's blog on its AI-native secure development lifecycle.
