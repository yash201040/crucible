---
type: "Reference"
title: "Deployment options compared"
description: "Compares Teams/Enterprise, Anthropic Console, Bedrock, Claude Platform on AWS, Google Cloud Agent Platform and Foundry on billing, auth and cost tracking."
resource: "https://code.claude.com/docs/en/third-party-integrations"
tags: [deployment, providers, billing, enterprise]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "third-party-integrations"
    resource: "https://code.claude.com/docs/en/third-party-integrations"
    title: "Enterprise deployment overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Where model inference runs and how it is billed. Teams or Enterprise is recommended for most organizations (one subscription for Claude Code and Claude on the web, SSO, server-managed settings on Teams; Enterprise adds domain capture, role-based permissions, compliance API). Self-hosted compute for cloud sessions is separate (self-hosted environments).

# How to use it

| Option | Billing | Authentication | Cost tracking | Enterprise features |
|---|---|---|---|---|
| Teams/Enterprise | per-seat (Teams, PAYG available) / contact sales | claude.ai SSO or email | usage dashboard | team management, SSO, usage monitoring |
| Anthropic Console | PAYG | API key or Console sign-in without one | usage dashboard | none |
| Amazon Bedrock | PAYG through AWS | API key or AWS credentials | AWS Cost Explorer | IAM policies, CloudTrail |
| Claude Platform on AWS | PAYG through AWS Marketplace | API key or AWS credentials | AWS Cost Explorer | IAM policies, CloudTrail |
| Google Cloud Agent Platform (formerly Vertex AI) | PAYG through GCP | GCP credentials | GCP Billing | IAM roles, Cloud Audit Logs |
| Microsoft Foundry | PAYG through Azure | API key or Microsoft Entra ID | Azure Cost Management | RBAC policies, Azure Monitor |

Prompt caching is enabled by default on all. Only Teams/Enterprise includes Claude on web. Setup pages exist for each, plus the Claude apps gateway (self-hosted gateway adding IdP sign-in in front of Bedrock, Claude Platform on AWS, Google Cloud, Foundry or the Anthropic API) and Claude Models on Google Cloud (Anthropic managed). For Bedrock and Google Vertex AI, `claude` > **3rd-party platform** at the login prompt launches a setup wizard.
