---
type: "Guide"
title: "Configure, select from the CLI, and archive environments"
description: "How to add or edit environments in the selector, set the CLI default with /remote-env, and archive an environment."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, environments, remote-env, archive]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, web, mobile]
requires: ""
identifiers:
  - "/remote-env"
  - "remote.defaultEnvironmentId"
  - "claude --cloud"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Environments are managed from the environment selector under the message box on the new-session screen at claude.ai/code (and the Desktop app's cloud sessions). Environments you create are personal; Owner-created shared ones appear alongside.

# How to use it

- **Add**: selector, **New environment**, fill the form, **Add environment**. **Edit**: hover the row under **Cloud**, click the settings icon; rows are **Network access**, **Setup script**, **Environment variables**; save with **Add environment** or **Save changes**. Network secrets save separately.
- The selector shows only until you send a new session's first message. For a running session of your own, use the caret after the title, then **Edit cloud environment**.
- **CLI default**: `/remote-env` opens a picker and saves the choice to `remote.defaultEnvironmentId` in user settings, applying in every project until changed (unless a higher-precedence settings layer, such as repo project settings, sets the key). It does not start a session and cannot add or edit environments. A self-hosted `ccpool_...` ID follows a stricter source rule (see the `remote.defaultEnvironmentId` entry of the settings reference).
- **Archive**: open for editing, **Archive environment**, confirm. Shared environments are archived by an Owner from the Cloud environments page in admin settings.

# Limits and defaults

Archiving affects new sessions only:
- Running sessions continue; network secrets stay attached in them (delete secrets first if unwanted).
- The environment disappears from the selector and `/remote-env`.
- If it was your saved CLI default, CLI cloud sessions start in the Anthropic-hosted environment when listed, else the first non-bridge environment.
- Anything configured with it explicitly (such as a cloud scheduled task) cannot start new sessions; point it elsewhere.
- Anthropic-hosted environments cannot be deleted, only archived. An Owner can delete a self-hosted environment from the admin page.
