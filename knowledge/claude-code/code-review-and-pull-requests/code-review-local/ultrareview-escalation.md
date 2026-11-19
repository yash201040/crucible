---
type: "Feature"
title: "Escalate /code-review to ultrareview"
description: "/code-review ultra runs the deeper cloud ultrareview against the default branch; unavailable on third-party providers, ZDR, HIPAA and CMEK."
resource: "https://code.claude.com/docs/en/code-review-local"
tags: [ultrareview, cloud, code-review, limits]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.227"
surfaces: [cli, cloud]
requires: "claude.ai account sign-in"
identifiers:
  - "/code-review ultra"
  - "/code-review ultra --fix"
  - "claude ultrareview"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-local"
    resource: "https://code.claude.com/docs/en/code-review-local"
    title: "Review locally with /code-review"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/code-review ultra --fix` runs ultrareview in the cloud then applies its findings to the working tree when they return. It compares the current branch against the repository's default branch plus uncommitted and staged changes. Pass a branch (`/code-review ultra develop`) for another base. Uncommitted changes to credential-like files (`.env`, `*.tfvars`) follow the rules for uploading a local repository to a cloud session.

# How to use it

For a github.com PR target, Claude can post the finished findings as a comment from your GitHub account (v2.1.227+). From scripts or CI use the `claude ultrareview` subcommand, which waits and prints findings to stdout (documented on the ultrareview page).

# Limits and defaults

Not available on Amazon Bedrock, Google Cloud's Agent Platform or Microsoft Foundry, or for organizations with Zero Data Retention or the HIPAA configuration: there `/code-review ultra` runs a local review instead. Organizations using customer-managed encryption keys (CMEK) cannot run ultrareview. A session-scoped scheduled task never launches the cloud review. In non-interactive runs ultrareview does not wait for the cloud review.
