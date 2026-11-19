---
type: "Reference"
title: "Environment slots for trusted infrastructure"
description: "The context, trust and sensitivity slots in autoMode.environment and their defaults."
resource: "https://code.claude.com/docs/en/auto-mode-config#define-trusted-infrastructure"
tags: [auto-mode, environment, trust, classifier]
kind: "setting"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli]
requires: "Host containment entry needs v2.1.257 or later"
identifiers:
  - "autoMode.environment"
  - "claude auto-mode defaults"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "auto-mode-config"
    resource: "https://code.claude.com/docs/en/auto-mode-config"
    title: "Configure auto mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude auto-mode defaults` prints three kinds of environment entry. Entries are natural-language prose, not regex or tool patterns.

# How to use it

| Kind | Slots | Defaults |
| :- | :- | :- |
| Context | Organization; Primary use of Claude Code; Cloud provider(s); Repository visibility; Internal sharing / snippet hosting; Org-specific CLIs; Secrets management; CI/CD deploy targets; Network posture; Host containment; Protected deployment namespaces / environments; Data retention / declassification | `None configured` or conservative: primary use software development; repo assumed private unless host/name or an earlier readable message shows public; public paste/gist services outside trust; host containment = ordinary dev machine with open internet |
| Trust | Trusted repo, Source control, Trusted internal domains, Trusted cloud buckets, Key internal services, Internal package registry | repo and source control default to the working repo and its remotes; others `None configured` |
| Sensitivity | Sensitive data locations & audiences, Sensitive remote targets, Protected IaC scopes | host/namespace is a sensitive remote target when `prod` or `production` is a whole word (`prod-db` yes, `webprod01` no) |

Example: `"environment": ["$defaults", "Source control: github.example.com/acme-corp and all repos under it", "Trusted cloud buckets: s3://acme-build-artifacts"]`. Verify with `claude auto-mode config`.

# Limits and defaults

- The classifier reads your messages and the commands Claude runs, not their output, so visibility evidence must be in your own message.
- Without a Host containment entry naming an identity, requests for the host's own credentials are blocked.
- Rollout suggestion: add source-control org and key internal services first, then domains and buckets.
