---
type: "Reference"
title: "What the classifier allows by default"
description: "Actions auto mode lets through without a prompt, including branch pushes, and how to force a checkpoint with ask rules."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [auto-mode, classifier, allowlist, git, sandbox]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "autoMode.environment"
  - "permissions.ask"
  - "claude auto-mode defaults"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Allowed by default in auto mode: local file operations in the working directory; installing dependencies declared in lock files or manifests; reading `.env` and sending credentials to their matching API; read-only HTTP requests; pushing to any branch of the repository you work in, including the default branch (a branch named like a deploy target such as `production` or `gh-pages` is judged on its own terms); deleting the exact jobs Claude created earlier this session; reading/writing security code and threat models for the task; messages between agents in the same multi-agent session; sending data to trusted domains, buckets and services listed in `environment` (data flow only, not destructive or credential operations); Claude in Chrome navigation to a trusted internal domain, localhost or a named URL.

# How to use it

A push's content is still checked against the other rules; `permissions.deny` rules can still block push commands as written in every mode; the remote's branch protection still applies. Creating a PR that matches the request runs without a prompt unless blocked (secrets leaving the repo, or PR to a different repository/organization). To require a human checkpoint while staying in auto, add `permissions.ask` rules (they match the command as written).

# Limits and defaults

Sandboxed commands get no network by default. Claude names the hosts a command needs on the command; the classifier reviews them with the command; an approved list opens those hosts for that command only. Run `claude auto-mode defaults` to print built-in rules; administrators add trusted repos, buckets and services via `autoMode.environment`.
