---
type: "Reference"
title: "Launcher contract and value format"
description: "Rules a corporate launcher script must follow and how the CLAUDE_CODE_PROCESS_WRAPPER value is parsed."
resource: "https://code.claude.com/docs/en/corporate-launcher"
tags: [launcher, contract, process-wrapper, argv]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.208"
surfaces: [cli]
requires: "Not supported on Windows"
identifiers:
  - "CLAUDE_CODE_PROCESS_WRAPPER"
  - "processWrapper"
  - "exec \"$@\""
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "corporate-launcher"
    resource: "https://code.claude.com/docs/en/corporate-launcher"
    title: "Run Claude Code behind a corporate launcher"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

If the launcher cannot run, Claude Code refuses to start the process rather than starting it unwrapped (except on Windows). The script must obey these rules.

# How to use it

| Rule | Detail |
|---|---|
| End with `exec "$@"` | A forking launcher leaves an orphan; agent view marks the session failed naming the launcher |
| Keep arguments intact | Strip only the launcher's own arguments (they come first); do not reorder or add |
| Pass all inherited environment | Adding is fine; dropping breaks per-session tokens, model/provider selection and the wrapper variable itself; `/status` reports mismatch |
| Reach `exec` in about 3 seconds | A background session may run the launcher three times in series before first output |
| Tolerate nested invocation | Applied to every nested self-spawn |
| No terminal or stdout output before `exec` | Reported as crash cause; stdout reaches programs parsing `claude -p` output |
| Do not depend on argument spelling | `--flag value` vs `--flag=value` can change between versions |
| `exec` from the starting directory | Do not change working directory |
| Do not read stdin | Redirect from `/dev/null` |
| Absolute paths for other programs | `PATH` may lack shell-profile entries |

Value format: absolute path, optionally followed by launcher arguments. Whitespace separates tokens; double quotes group; single quote is an ordinary character; a value starting with `[` is a JSON string array (in a settings file write it as an escaped JSON string); shell syntax (variables, globbing, `;`, `|`, `&`, `$(`) is not supported, and unquoted operators are a configuration error. Unusable values cause refusal to start the process (see the launcher error reference in the errors page).

Launcher arguments example: value `/opt/corp/launcher --profile cc`; script reads `$1`/`$2` then `shift 2` before `exec "$@"`.

# Notes

Restoring an original `~/.local/bin/claude` symlink is advised if it was replaced by a launcher; a replaced symlink double-wraps the first session and `/doctor` reports an externally managed install.
