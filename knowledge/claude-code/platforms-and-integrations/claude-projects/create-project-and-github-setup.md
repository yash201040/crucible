---
type: "Guide"
title: "Creating a project and GitHub access"
description: "Prerequisites, the New project dialog, continuing an existing session in a project, and installing the Claude GitHub App."
resource: "https://code.claude.com/docs/en/claude-projects"
tags: [projects, setup, github, prerequisites]
kind: "ui"
maturity: "beta"
since: ""
surfaces: [web, desktop, mobile]
requires: "Pro, Max or Ultra plan; github.com repos with push access and Claude GitHub App installed"
identifiers:
  - "claude.ai/code/projects/browse"
  - "Continue in project"
  - "/remote-control"
  - "/web-setup"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-projects"
    resource: "https://code.claude.com/docs/en/claude-projects"
    title: "Let Claude coordinate ongoing work with Projects"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How a project is created and what it needs.

# How to use it

- Prerequisites: Projects shows in the sidebar (directly or under More). Code must be on github.com (not GitHub Enterprise Server, GitLab or Bitbucket) with push access, and the Claude GitHub App installed. A `/web-setup` token is not enough for a project's cloud threads. MCP servers must show as connected in claude.ai connectors.
- New project dialog: Name (required), "What do you want to work on?" (optional one-line goal), Context (optional repos, files, folders, Google Drive folders). If the button says **Get started**, upgrade or archive existing claude.ai projects first.
- On a first project, Claude takes its own turn unless you send a message first (uses plan): it may start a read-only exploration thread and post **Setup recommendations** (repos, scheduled tasks, threads), each starting switched on; **Update setup** applies them.
- From a cloud session: sidebar menu **Continue in project**, then **Continue as new project** or an existing project (the original session stays; a running turn keeps going, but the **Set up project** banner stops it). A local session connected via Remote Control gets the same menu, but Claude cannot read its transcript if **Require trusted devices** was on.
- GitHub: connect once; install the Claude GitHub App per repo or per org (org repos need an org owner to approve); authorize SSO if the org enforces SAML SSO, or its private repos do not appear.
- Repositories: add the one or two repos most tasks touch; a thread can add a repo to itself (this thread only, cloned partway through so its `CLAUDE.md` was not loaded). Once a project has repos, Claude can only add repos from an owner the project already uses; others you add yourself in Project settings > Environment. A project may have no repo.
- Files: up to 1,000 files and 2 GB per upload, single file up to 480 MB; folders skip hidden files and `node_modules`; at most 10 folders and Drive folders combined; uploads are copies (Replace to update); files read under `/mnt/project-files`.

# Limits and defaults

- Repository access errors: "Couldn't start the session — Claude doesn't have GitHub access to this project's repository", "Unable to access your repository", "Claude can't access" a repository. Fix with Install on GitHub / Select repositories, then ask Claude to start a new thread.
