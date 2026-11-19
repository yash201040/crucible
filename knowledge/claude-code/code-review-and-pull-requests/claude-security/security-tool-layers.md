---
type: "Concept"
title: "How Claude Security fits with other security tools"
description: "Defense-in-depth stack: security-guidance plugin, /security-review, Claude Security plugin, Code Review, managed Claude Security and CI scanners."
resource: "https://code.claude.com/docs/en/claude-security"
tags: [security, code-review, layers, comparison]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "/security-review"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-security"
    resource: "https://code.claude.com/docs/en/claude-security"
    title: "Scan your codebase for vulnerabilities"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Stage | Tool | Covers |
| :- | :- | :- |
| In session | Security guidance plugin | Common vulnerabilities in code Claude writes |
| On demand, single pass | `/security-review` | One pass on the current branch |
| On demand, deep scan | Claude Security plugin | Multi-agent scan of a repo or diff with verified findings and patches |
| On pull request | Code Review (Team and Enterprise) | Multi-agent correctness and security review |
| Managed | Claude Security product (Enterprise plan) | Hosted scanning that monitors connected repositories |
| In CI | Your static analysis and dependency scanners | Language rules, supply chain, policy |

# Notes

The plugin does not replace existing source-code security tools; it complements deterministic checks. Findings appear only after independent verifier agents analyze them, to keep reports short.
