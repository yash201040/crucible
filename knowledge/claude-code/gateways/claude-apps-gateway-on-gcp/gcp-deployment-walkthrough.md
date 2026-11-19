---
type: "Guide"
title: "Gateway on Google Cloud: Cloud Run or GKE walkthrough"
description: "Worked example deploying the gateway with Agent Platform, Cloud SQL private IP, Secret Manager and Cloud Run or GKE; not a supported production deployment."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-on-gcp"
tags: [gateway, gcp, cloud-run, gke, vertex]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "GCP project with billing, Claude models enabled in Model Garden"
identifiers:
  - "roles/aiplatform.user"
  - "roles/secretmanager.secretAccessor"
  - "roles/iam.workloadIdentityUser"
  - "--no-invoker-iam-check"
  - "--allow-unauthenticated"
  - "--min-instances=1"
  - "--ingress=internal"
  - "--timeout=3600"
  - "--vpc-egress=private-ranges-only"
  - "--platform=linux/amd64"
  - "--provenance=false"
  - "gce-internal"
  - "BackendConfig"
  - "timeoutSec"
  - "gateway-config"
  - "setup.sh"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-on-gcp"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-on-gcp"
    title: "Deploy Claude apps gateway on Google Cloud"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A worked example ("a working example for customer-managed infrastructure rather than a supported production deployment") using Cloud Run or GKE, Artifact Registry, Cloud SQL for PostgreSQL 16 (private IP only via Private Services Access, tier `db-g1-small`), Secret Manager (`gateway-jwt-secret`, `gateway-oidc-client-secret`, `gateway-postgres-url`, `gateway-config`), a `claude-gateway` service account with `roles/aiplatform.user`, and a front end you provide (internal Application Load Balancer for Cloud Run, internal GKE Ingress class `gce-internal`). Google Workspace is the example IdP.

# How to use it

Steps: enable APIs; create service account and bind the role; build `linux/amd64` image with `--provenance=false` and push; create the VPC, subnet, peering and Cloud SQL (`--no-assign-ip`, URL with `sslmode=require`); write `gateway.yaml` with `provider: vertex`, `auth: {}` (Application Default Credentials), `scopes: [openid, profile, email]` and `extra_auth_params: { access_type: offline, prompt: consent }`; store secrets; deploy; push client settings.

`trusted_proxies` by front end: Cloud Run direct `[169.254.0.0/16]`; internal ALB in front of Cloud Run `169.254.0.0/16` plus the proxy-only subnet CIDR; GKE internal Ingress the proxy-only subnet CIDR. An external `gce` Ingress is not supported because its public address fails the private-network check.

Cloud Run deploy flags: `--min-instances=1 --max-instances=8 --timeout=3600 --ingress=internal`, Direct VPC egress (`--network --subnet --vpc-egress=private-ranges-only`), `--set-secrets` mounting `gateway-config` at `/etc/claude/gateway.yaml` and the other three as env vars, and `--no-invoker-iam-check` (or `--allow-unauthenticated`) because the gateway does its own OIDC. The `*.run.app` URL resolves publicly, so use an internal load balancer hostname or a Private Service Connect plus private DNS zone setup.

GKE: cluster on the same VPC, Workload Identity (`--workload-pool`, node pools `GKE_METADATA`), Secret Manager CSI driver at `/secrets`, `${file:/secrets/...}` references, probe `/readyz`, and a BackendConfig with raised `timeoutSec` (default 30 s cuts streams). Do not block `169.254.169.254` with NetworkPolicy; the boot warning about it is expected.

# Limits and defaults

Cloud Run request timeout default 300 s (use 3600); each instance holds up to `store.max_connections` (5) DB connections, so check `--max-instances=8` against database limits. Google id_tokens carry no groups, so use `oidc.google_groups` or `email_domain` matching. Cloud Run errors: 403 before the container (invoker check on), `invoker_iam_disabled is not currently available` when `constraints/run.managed.requireInvokerIam` blocks it, amd64 manifest errors, 403 `PERMISSION_DENIED` from Agent Platform (wrong service account or model not enabled). The `examples/gateway/gcp` bundle has `setup.sh`, `terraform/`, `gateway.yaml.example` and a distroless `Dockerfile`; its default invoker layer is an `allUsers` `run.invoker` grant.
