---
type: "Guide"
title: "Gateway on AWS: ECS Fargate or EKS walkthrough"
description: "Worked example deploying the gateway with Bedrock, RDS Postgres, Secrets Manager, an internal ALB and IAM roles; not a supported production deployment."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-on-aws"
tags: [gateway, aws, ecs, eks, bedrock]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "AWS account, VPC with two private subnets and NAT, ACM certificate"
identifiers:
  - "bedrock:InvokeModel"
  - "bedrock:InvokeModelWithResponseStream"
  - "bedrock:CountTokens"
  - "rds.force_ssl"
  - "sslmode=verify-full"
  - "NODE_EXTRA_CA_CERTS"
  - "idle_timeout.timeout_seconds"
  - "alb.ingress.kubernetes.io/ip-address-type"
  - "--ip-address-type ipv4"
  - "setup.sh"
  - "gateway.yaml.example"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-on-aws"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-on-aws"
    title: "Deploy Claude apps gateway on AWS"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A worked example, explicitly "a working example for customer-managed infrastructure rather than a supported production deployment". Components: ECS on Fargate service or EKS Deployment, ECR repo, RDS for PostgreSQL 16 in private subnets (not public, storage encrypted, parameter group `rds.force_ssl=1`), Secrets Manager secrets (JWT key, OIDC client secret, Postgres URL), an IAM role granting `bedrock:InvokeModel`, `bedrock:InvokeModelWithResponseStream`, `bedrock:CountTokens`, and an internal ALB. Okta is the sample IdP. Claude Platform on AWS can replace or accompany Bedrock.

# How to use it

Eight steps: (1) three security groups chaining ALB 443 to gateway 8080 to Postgres 5432; (2) task role (Bedrock only; resources `inference-profile/us.anthropic.*` and `foundation-model/anthropic.*`) plus an ECS execution role for ECR and secrets; submit Anthropic's one-time Bedrock use case form; (3) RDS instance with `sslmode=verify-full` and the AWS RDS CA bundle copied to `/etc/claude/rds-global-bundle.pem` with `NODE_EXTRA_CA_CERTS`; (4) `gateway.yaml` with `upstreams: [{provider: bedrock, region, auth: {}}]`, `session.ttl_hours: 8`, `trusted_proxies` set to the ALB subnet CIDRs; (5) secrets; (6) build `linux/amd64` image (or arm64 with `cpuArchitecture: ARM64`) to an IMMUTABLE-tag ECR repo; (7) deploy: ECS task def (1024 CPU, 2048 memory), ALB with `--ip-address-type ipv4`, HTTPS listener policy `ELBSecurityPolicy-TLS13-1-2-2021-06`, `idle_timeout.timeout_seconds` 3600, health check `/readyz`, service with deployment circuit breaker and 60 s grace period; EKS uses IRSA via `eksctl create iamserviceaccount` and ALB controller annotations (`scheme: internal`, `target-type: ip`, `ip-address-type: ipv4`, `inbound-cidrs`, `certificate-arn`, `ssl-policy`, `load-balancer-attributes`); (8) push client managed settings. A companion bundle at `examples/gateway/aws` has `setup.sh` (idempotent, ECS track), `gateway.yaml.example`, a `Dockerfile` and `terraform/`.

# Limits and defaults

Non-US regions need a `models:` block and different IAM ARN prefixes. Config edits on ECS need an image rebuild under a new tag. Streams dropping after quiet periods: gateways older than v2.1.229 on Bedrock or Claude Platform on AWS send no keepalive; the ALB closes after 60 s idle by default. Other AWS-specific errors: `403 AccessDeniedException` (use case form, Marketplace subscription lag, missing ARNs), `ValidationException` on-demand throughput (map to `us.anthropic.*` profile), `ResourceInitializationError` (execution role or egress path).
