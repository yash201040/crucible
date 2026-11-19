---
type: "Reference"
title: "userConfig schema"
description: "userConfig declares values prompted when a plugin is enabled; strict option fields, fixed options lists, storage of sensitive values."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, userconfig, secrets, config]
kind: "file"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cli]
requires: ""
identifiers:
  - "userConfig"
  - "type"
  - "title"
  - "required"
  - "default"
  - "options"
  - "multiple"
  - "sensitive"
  - "min"
  - "max"
  - "pluginConfigs"
  - "/config"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`userConfig` declares values Claude Code prompts the user for when the plugin is enabled, so users do not edit `settings.json`. Keys are identifiers of letters, digits and underscores, not starting with a digit. Each value is a strict object (unknown key fails validation). Each option of each enabled plugin also appears as a row in the `/config` panel, except `sensitive` options and `multiple` lists (rows need v2.1.269 or later).

# How to use it

| Field | Required | Description |
| :- | :- | :- |
| `type` | Yes | `string`, `number`, `boolean`, `directory` or `file` |
| `title` | Yes | Label in the configuration dialog |
| `description` | Yes | Help text beneath the field |
| `required` | No | If `true`, the dialog does not accept an empty value |
| `default` | No | Value when none given: string, number, boolean or array of strings |
| `options` | No | For `string`: accepted values, shown as a picker in `/config`. Requires v2.1.271 or later |
| `multiple` | No | For `string`, allows an array of strings |
| `sensitive` | No | If `true`, masks input and stores in secure storage instead of `settings.json` |
| `min` / `max` | No | Bounds for `number` |

**Fixed options**: set `options` (e.g. `["neutral", "warm", "formal"]`) with `default` one of them, or `required: true`. Applies to a `string` field that is not `multiple` or `sensitive`. Each option is a plain label of 1 to 64 characters; breaking the rules fails the plugin load (validate reports it). Declaring `options` on any field makes the plugin unloadable on Claude Code before v2.1.271.

# Limits and defaults

Non-sensitive values are saved under `pluginConfigs` in the user's `settings.json`; sensitive values go to the platform's secure credential store. The settings reference lists which settings files `pluginConfigs` is read from.
