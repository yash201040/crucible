---
type: "Reference"
title: "Path rules, containment and defaults"
description: "Component paths start with ./, resolve inside the plugin root and must exist; each key replaces, adds to or merges with its default location."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, paths, containment, defaults]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.283"
surfaces: [cli]
requires: ""
identifiers:
  - "./"
  - "<component> path escapes plugin directory: <path>"
  - "<component> path not found: <path>"
  - "Path contains \"..\" which could be a path traversal attempt"
  - "Path not found"
  - "Default <folder>/ folder is ignored because the manifest sets \"<key>\""
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every component path is relative to the plugin root and must start with `./` (a path like `commands/foo.md` fails validation). Exceptions: `skills` also accepts `"."` (and `"./"`) for the plugin root; `mcpServers` also accepts an `https://` bundle URL. `experimental.evals` is not a component path: it names a directory below the plugin root (e.g. `"quality/evals"`, with or without `./`), with an array only the first entry is used, and `claude plugin eval` checks it at run time.

# How to use it

**Containment and existence**: each path must resolve inside the plugin root and exist. Escaping paths do not load; the `/plugin` Errors tab shows `<component> path escapes plugin directory: <path>` (validate error `Path contains ".." which could be a path traversal attempt`). For an `mcpServers`/`lspServers` file, a `path not read` message means the path is absolute or contains `..`. Missing paths show `<component> path not found: <path>` (validate `Path not found`). For `outputStyles`, `lspServers`, `monitors` and `themes` the validate check requires v2.1.283 or later.

**Combination with defaults**:
- Replaces the default: `commands`, `agents`, `outputStyles`, `workflows`, `experimental.themes`, `experimental.monitors`. To keep the default list it too: `"commands": ["./commands/", "./extras/"]`.
- Adds to the default: `skills`.
- Merges: `hooks`, `mcpServers`, `lspServers` (default file first, manifest declarations merged in).

# Limits and defaults

If a default folder exists and the manifest sets the replacing key, only manifest paths load and `claude plugin list` and `/plugin` warn `Default <folder>/ folder is ignored because the manifest sets "<key>"`. Avoid it by setting the key to a path inside the folder, e.g. `"commands": ["./commands/deploy.md"]`.
