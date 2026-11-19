---
type: "Reference"
title: "Generated mod type definitions"
description: "Claude Code writes TypeScript declaration files into .claude-plugin/types/ matching the running version for editor autocomplete and type-checking."
resource: "https://code.claude.com/docs/en/plugins/mods/create"
tags: [mods, typescript, types, tsconfig]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Interactive session with a mod loaded from --plugin-dir or written by Claude"
identifiers:
  - ".claude-plugin/types/claude-code/index.d.ts"
  - ".claude-plugin/types/claude-code-tools/index.d.ts"
  - ".claude-plugin/types/claude-code-mcp/index.d.ts"
  - "tsconfig.json"
  - "tsc -p ./first-mod"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-create"
    resource: "https://code.claude.com/docs/en/plugins/mods/create"
    title: "Create a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When Claude Code loads a mod from `--plugin-dir` in an interactive session, or one it wrote for you, it writes declaration files into the mod's `.claude-plugin/types/` describing the events, mods API methods and elements of the running version.

| Path | Declares |
| :- | :- |
| `claude-code/index.d.ts` | Every event with input and result, every API namespace and method, elements each surface can draw (fullest reference, with a comment and example per method) |
| `claude-code-tools/index.d.ts` | Built-in tools' inputs and results, so `e.tool === 'Bash'` narrows `e` |
| `claude-code-mcp/index.d.ts` | Inputs of MCP tools connected when you last saved a file in the mod |
| `index.d.ts` in a directory named for a plugin | What that plugin adds to the mods API; one per plugin in `dependencies` |
| `tsconfig.json` | Compiler options fitting a hooks module |

# Notes

If the mod has no `tsconfig.json`, one at the mod's root extending the generated one is added so editors and `tsc -p ./first-mod` type-check without more setup. Events and methods can change between releases; trust these files over any page.
