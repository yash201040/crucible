---
type: "Reference"
title: "Organization admin and Compliance API"
description: "Owner toggles, retention, audit and the Compliance API endpoints for listing and deleting an organization's artifacts."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, admin, compliance-api, retention]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [web]
requires: "Team or Enterprise; Owner role; audit feed on Enterprise"
identifiers:
  - "GET /v1/compliance/apps/code/artifacts"
  - "GET /v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}"
  - "DELETE /v1/compliance/apps/code/artifacts/{artifact_id}"
  - "Enable artifact connectors"
  - "External sharing"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Owners on Team and Enterprise control artifacts from claude.ai admin settings. Content is stored on Anthropic-operated infrastructure and visible only to authenticated members of the publishing organization and the people they share it with, unless shared publicly.

# How to use it

| Control | Where |
| --- | --- |
| Enable or disable artifacts | Organization settings > Artifacts, **Artifacts** toggle; Enterprise with RBAC can scope by role (Organization settings > Roles, **Artifacts** permission) |
| Connector calls | Organization settings > Capabilities, **Enable artifact connectors** toggle (separate; also governs artifacts made in claude.ai conversations) |
| Public sharing | Off by default; turn on **External sharing** under the **Artifacts** toggle. Turning off blocks existing public links without changing audiences; access resumes if re-enabled |
| Retention | Organization settings > Data and privacy; separate periods for private and shared artifacts |
| Audit | Enterprise: Compliance API Activity Feed, filter `activity_types` containing `artifact` |

Compliance API endpoints: `GET /v1/compliance/apps/code/artifacts` (list), `GET /v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}` (version content), `DELETE /v1/compliance/apps/code/artifacts/{artifact_id}`.
