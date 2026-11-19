---
type: "Feature"
title: "Invoke plugin skills by namespace"
description: "Plugin skills are namespaced with the plugin name and can be dispatched by sending /plugin-name:skill-name as the prompt."
resource: "https://code.claude.com/docs/en/agent-sdk/plugins"
tags: [plugins, skills, namespace, dispatch]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "/plugin-name:skill-name"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-plugins"
    resource: "https://code.claude.com/docs/en/agent-sdk/plugins"
    title: "Plugins in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Skills from plugins are automatically namespaced with the plugin name to avoid conflicts. Claude can invoke them on its own when relevant, or you can send `/plugin-name:skill-name` as the prompt (for example `/my-plugin:greet`).

# How to use it

Load the plugin with the [plugins option](./load-local-plugins.md), then set `prompt: "/my-plugin:greet"`. In an allow-list of skills, plugin skills are listed as `plugin:skill` (see [skills option](../agent-sdk-skills/skills-option-and-allowlist.md)).
