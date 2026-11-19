---
type: "Reference"
title: "Plugin, skill and at-mention events"
description: "plugin_installed, plugin_loaded, skill_activated and at_mention events for inventory and usage of plugins and skills."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, plugins, skills, inventory]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude_code.plugin_installed"
  - "claude_code.plugin_loaded"
  - "claude_code.skill_activated"
  - "claude_code.at_mention"
  - "marketplace.is_official"
  - "install.trigger"
  - "plugin.version"
  - "plugin.scope"
  - "enabled_via"
  - "has_hooks"
  - "has_mcp"
  - "host_owned_mcp"
  - "skill_path_count"
  - "command_path_count"
  - "agent_path_count"
  - "safe_mode"
  - "--safe-mode"
  - "invocation_trigger"
  - "skill.source"
  - "skill.kind"
  - "mention_type"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Events for inventorying plugins and skills across a fleet.

# How to use it

- `claude_code.plugin_installed`: after install via `claude plugin install` or `/plugin` UI. Attributes `marketplace.is_official`, `install.trigger` (`cli`/`ui`), `plugin.name`, `plugin.version`, `marketplace.name` (third-party values only with DETAILS).
- `claude_code.plugin_loaded`: once per enabled plugin at session start. `plugin.name` (`third-party` unless DETAILS), `marketplace.name`, `plugin.version` (only if name not redacted and declared), `plugin.scope` (`official`,`community`,`org`,`user-local`,`default-bundle`), `enabled_via` (`default-enable`,`org-policy`,`admin-install`,`seed-mount`,`user-install`; before v2.1.246 `admin-install` plugins showed as `user-install` or `seed-mount`), `plugin_id_hash` (hash of name plus marketplace, only to your exporter; for plugins synced from claude.ai uses the reported marketplace name or `synced`; before v2.1.246 the reported name was not used), `has_hooks` (hook config or a mod), `has_mcp`, `host_owned_mcp` (SDK host manages the plugin's MCP and Claude Code skipped its server config), `skill_path_count`, `command_path_count`, `agent_path_count`, `safe_mode` (`--safe-mode`: inventory only, nothing loads; v2.1.169+).
- `claude_code.skill_activated`: when a skill is invoked by the Skill tool or a `/` command. `skill.name` (`custom_skill` for user-defined and third-party plugin skills unless DETAILS), `invocation_trigger` (`user-slash`, `claude-proactive`, `nested-skill`), `skill.source` (`bundled`, `userSettings`, `projectSettings`, `plugin`...), `skill.kind` (`workflow` for a workflow skill), `plugin.name` and `marketplace.name` (with DETAILS or official plugins).
- `claude_code.at_mention`: when an `@`-mention resolves; early exits (permission denial, oversized files, PDF reference attachments, directory listing failures) emit nothing. `mention_type` (`file`,`directory`,`agent`,`mcp_resource`,`peer`; `peer` = one of your other sessions, v2.1.232+), `success`. At most 100 events of type `agent` and 100 of `mcp_resource` per prompt read; extra mentions still resolve.
