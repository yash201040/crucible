---
type: "Reference"
title: "Environment, model, telemetry and sandbox warnings"
description: "Warnings for otelHeadersHelper, headersHelper trust, crossSessionInbound, Foundry resource, 200K limit, unrecognized model ID line, sandbox locks and mask files."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, warnings, models, sandbox, telemetry]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.233"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "otelHeadersHelper"
  - "headersHelper"
  - "crossSessionInbound"
  - "ANTHROPIC_FOUNDRY_RESOURCE"
  - "ANTHROPIC_FOUNDRY_BASE_URL"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "autoCompactWindow"
  - "CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT"
  - "CLAUDE_CODE_MAX_CONTEXT_TOKENS"
  - "ANTHROPIC_BETAS"
  - "--betas"
  - "modelOverrides"
  - "[claude-code:unrecognized_model]"
  - "allowManagedReadPathsOnly"
  - "allowManagedDomainsOnly"
  - "sandbox.filesystem.allowRead"
  - "sandbox.network.allowedDomains"
  - "claude doctor"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Warnings tied to specific settings and environment variables, relevant to scripted and fleet runs because several only appear on stderr in `-p` mode or in the debug log.

# How to use it

| Warning | Meaning | Fix |
|---|---|---|
| `otelHeadersHelper failed; telemetry is not being exported. See /status: ...` | Script failed or printed invalid output; exports fail and the backend gets nothing from the session. Once per interactive session; in `-p` stderr: `otelHeadersHelper failed (OpenTelemetry export headers unavailable): <error>` | Exit 0 within 30 seconds and print a JSON object of string header values |
| `MCP server '<name>': headersHelper not run - this workspace has no persisted trust` | `headersHelper` is a shell command so it needs saved folder trust; the server connects with static `headers` only. Written to stderr in non-interactive mode once per server; debug log when interactive. Parent-folder trust and `-p`/SDK sessions do not satisfy it | Accept the dialog interactively, or set `projects["<path>"].hasTrustDialogAccepted` in `~/.claude.json` |
| `"crossSessionInbound" must be one of "accept", "hold", "refuse"` | Unrecognized value is ignored while cross-session messages are held for approval; in managed settings it is treated as `refuse` (before v2.1.248 ignored silently) | Set one of the three values or remove |
| `ANTHROPIC_FOUNDRY_RESOURCE must be a Foundry resource name` | Value is a URL or host name rather than 2 to 64 letters, digits and hyphens (not starting/ending with a hyphen); appears as `API Error:` in place of the reply | Use only the resource name, or set `ANTHROPIC_FOUNDRY_BASE_URL` and remove the other; only one is accepted |
| `CLAUDE_CODE_DISABLE_1M_CONTEXT is set, but the 200K limit isn't enforced for <model>` | No compaction threshold caps the session at 200K: unrecognized model ID (gateway alias) with `CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT=1` or `CLAUDE_CODE_MAX_CONTEXT_TOKENS` above 200K, or a `context-1m` beta via `ANTHROPIC_BETAS` or `--betas` | `CLAUDE_CODE_AUTO_COMPACT_WINDOW=200000` or `autoCompactWindow` set to `200000`; `claude update`. Stderr only for `-p` text output; otherwise debug log |
| `[claude-code:unrecognized_model] {"model":"...","query_source":"sdk"}` | Request sent with a model ID the version does not recognize and no `modelOverrides` match; request is still sent. In `-p` it goes to stderr under every `--output-format` (parse by the prefix; one-line JSON, more fields may be added); interactive and background sessions write it to the debug log. Once per model ID per process. `query_source` is `sdk` for a `-p` main conversation and starts with `agent:` for a subagent. Not written for Bedrock `us.anthropic.claude-...` IDs, Google Cloud Agent Platform `@`-suffixed IDs, Foundry deployment names containing a Claude model ID, or resolvable Bedrock inference-profile ARNs. Before v2.1.233 nothing was written | Add `modelOverrides` keyed by an Anthropic model ID (not an alias such as `opus`), e.g. `{"modelOverrides": {"claude-opus-4-6": "my-proxy-model"}}`; `claude update`; fix typos |
| `sandbox.filesystem.allowRead is ignored - managed settings set allowManagedReadPathsOnly` | Shown in `/status` and `claude doctor`; also for `sandbox.network.allowedDomains` under `allowManagedDomainsOnly` | Admin adds entries to managed settings; remove entries to clear the warning |
| `Sandbox mask files left behind at write-deny paths` | Linux and WSL2 with sandbox filesystem isolation: 0-byte read-only placeholders remain after a kill (e.g. SIGKILL) or exit during a running sandboxed command; can make "Yes, and don't ask again" fail to save. Before v2.1.309: `Stale sandbox mask files left by a killed session`; before v2.1.257 not flagged | Quit all sessions in the project, `rm` each listed file, rerun `claude doctor` |

# Limits and defaults

- `otelHeadersHelper` must exit 0 within 30 seconds.
- Foundry resource name: 2 to 64 characters.

# Notes

Warnings that only reach stderr in `-p` mode can be parsed by a harness; the `[claude-code:unrecognized_model]` prefix is documented as the match key.
