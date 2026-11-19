---
type: "Feature"
title: "Gateway on AWS: telemetry and cost attribution"
description: "Per-developer AWS billing split with assume_role session names, per-team application inference profiles, and logging and metrics sinks."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-on-aws"
tags: [gateway, aws, cost-attribution, telemetry, bedrock]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.281"
surfaces: [cli]
requires: "gateway on Claude Code v2.1.281 or later for assume_role session_name"
identifiers:
  - "assume_role"
  - "session_name: email"
  - "telemetry.forward_to"
  - "enforceAvailableModels"
  - "availableModels"
  - "--model"
  - "is not in your role's availableModels allowlist"
  - "application-inference-profile"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-on-aws"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-on-aws"
    title: "Deploy Claude apps gateway on AWS"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default the gateway signs every Bedrock request with one principal (ECS task role or IRSA role), so AWS sees one IAM principal. Two combinable routes split spend in AWS billing data. Telemetry on AWS: point `telemetry.forward_to` at an OpenTelemetry collector such as the AWS Distro for OpenTelemetry (ADOT) collector, exported to CloudWatch, Amazon Managed Service for Prometheus or any OTLP backend; the collector must be an `https://` internal service.

# How to use it

Per developer: create a second IAM role with the Bedrock permissions that trusts the gateway principal, give that principal `sts:AssumeRole` on it, and set `assume_role` with `session_name: email` on the Bedrock upstream. The gateway assumes the role once per developer per hour (one STS call per active developer per hour per replica), so requests appear as `arn:aws:sts::<account>:assumed-role/<role>/<email>`. The private subnets need a path to `sts.<region>.amazonaws.com`. Use a billing export with IAM principal data (IAM principal cost allocation).

Per team: create one Bedrock application inference profile per team and model, tag and activate the tag as a cost allocation tag, add a `models:` entry per team (include the served model id such as `claude-opus-4-8` in the custom id so the spend meter can price it), and pin IdP groups to ids with `managed.policies` using `availableModels` and `enforceAvailableModels: true`. Developers in a pinned team start with `--model <team-id>`. The signing role must be allowed to invoke `application-inference-profile/*` ARNs. A developer on two teams needs a pair group whose policy is listed first and allows both ids; the default is first-match, so otherwise a session on the other team's id fails with `is not in your role's availableModels allowlist`.

# Limits and defaults

Without a `match: {}` catch-all, an unmatched developer gets every catalog model and can bill either team's profile. A developer has one spend total and one cap per period regardless of id; set a per-user cap so a lower team cap does not block the other team. Config grows as teams times models. Logs: on ECS Fargate stderr goes to `/ecs/claude-gateway` via `awslogs`; on EKS install the CloudWatch Observability add-on or Fluent Bit or the audit trail is lost. Container metrics: `aws ecs update-cluster-settings ... name=containerInsights,value=enabled`.
