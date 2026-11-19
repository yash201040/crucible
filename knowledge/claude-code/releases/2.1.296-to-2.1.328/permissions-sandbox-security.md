---
type: "Release Digest"
title: "Permissions, sandbox and security, 2.1.296 to 2.1.328"
description: "Release-note changes to permission modes, auto mode, sandbox, deny and ask rules and unattended-run permission behaviour between 2.1.296 and 2.1.328."
resource: "https://code.claude.com/docs/en/changelog"
tags: [permissions, auto-mode, sandbox, security, unattended, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "disableAutoMode"
  - "permissions.denyInsteadOfPrompting"
  - "permissions.blockReadsOutsideWorkingDirectories"
  - "permissions.blockWritesOutsideWorkingDirectories"
  - "permissions.allow"
  - "sandbox.failIfUnavailable"
  - "sandbox.autoAllowBashIfSandboxed"
  - "sandbox.filesystem.allowWrite"
  - "sandbox.allowNestedUserNamespaces"
  - "sandbox.enabled"
  - "sandbox.excludedCommands"
  - "dangerouslyDisableSandbox"
  - "allowUnsandboxedCommands"
  - "allowManagedDomainsOnly"
  - "CLAUDE_CODE_AUTO_MODE_MODEL"
  - "CLAUDE_CODE_AUTO_MODE_SERVER"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "autoMode.environment"
  - "autoMode.allow"
  - "$defaults"
  - "defaultMode"
  - "dontAsk"
  - "--permission-mode"
  - "--allowedTools"
  - "--disallowedTools"
  - "--tools"
  - "--add-dir"
  - "/add-dir"
  - "/sandbox"
  - "/permissions"
  - "/auto-mode-setup"
  - "/rewind"
  - "/security-review"
  - "attributionProject"
  - "claude_code.safety_event"
  - "forceLoginOrgUUID"
  - "allowedProviders"
  - "allowedHttpHookUrls"
  - "allowManagedPermissionRulesOnly"
  - "PowerShell"
  - "--trust-workspace"
  - "--bare"
  - "managed-settings"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.296 to 2.1.328"
stale_after: "2027-01-19T00:00:00Z"
---

# What changed

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.328 | 2026-11-19 | Auto mode added for Opus 4.6 and Sonnet 4.6 on Bedrock, Google Cloud's Agent Platform, Foundry and Claude apps gateway; interactive sessions with no permission mode start in it. | `disableAutoMode` |
| 2.1.328 | 2026-11-19 | Plan mode and Bash prompts for those models on third-party providers use and offer auto mode; disableAutoMode turns both off. | `disableAutoMode` |
| 2.1.328 | 2026-11-19 | A sandbox that cannot start is reported differently unless sandbox.failIfUnavailable is set: the next sandboxed Bash command is refused and says the sandbox is off for the session. | `sandbox.failIfUnavailable` |
| 2.1.328 | 2026-11-19 | Startup warning when the self-hosted runner host's settings.json sets a default permission mode that sessions ignore. | |
| 2.1.327 | 2026-11-17 | Path checks refuse some symbolic links; what counts as inside a working directory changed so some paths now ask. | |
| 2.1.327 | 2026-11-17 | permissions.blockReadsOutsideWorkingDirectories asks about more Bash commands in bypass and auto modes, denies some in auto, and refuses more commands naming a path under a Read or Edit deny rule. | `permissions.blockReadsOutsideWorkingDirectories` |
| 2.1.327 | 2026-11-17 | Auto mode's notice about falling back to billed classifier requests says an upcoming release removes the fallback; each action it would have checked will be asked about or denied. | |
| 2.1.327 | 2026-11-17 | Auto mode ignores more allow rules that run any package, like Bash(pnpm dlx *), and path or version forms of them. | |
| 2.1.327 | 2026-11-17 | Bash commands whose variables expand to very long text are denied; the PowerShell tool asks before one more command, refused with nobody to answer unless a whole-tool rule, auto or bypass mode allows. | `PowerShell` |
| 2.1.327 | 2026-11-17 | Arrow keys on most permission prompts stop at No instead of wrapping; ExitWorktree asks before removing a worktree that may hold unsaved work. | |
| 2.1.326 | 2026-11-16 | Terminal and VS Code sessions under the Claude Code + Cowork HIPAA configuration start in auto mode by default; sessions with no mode start in auto when the policy has not loaded; server-managed defaultMode applies once settings load, or Manual if settings fail with no stored copy. | `defaultMode`, `disableAutoMode` |
| 2.1.326 | 2026-11-16 | Sandbox: commands on macOS, Linux and WSL no longer write to some sensitive home folders by default (allow with sandbox.filesystem.allowWrite in user or managed settings); unexpected entries in a repository's .git folder are set aside after a command; missing --add-dir folders created before each sandboxed command on Linux and WSL. | `sandbox.filesystem.allowWrite` |
| 2.1.326 | 2026-11-16 | The Bash sandbox asks before some lines that set environment variables when auto-allow is off; unattended runs can refuse them. | |
| 2.1.326 | 2026-11-16 | Claude's file tools refuse writes to sign-in files such as .credentials.json and some device and process files; some cp and mv commands ask first. | |
| 2.1.326 | 2026-11-16 | Some tool calls in bypass permissions mode ask for approval, or are denied where no one can be asked; PowerShell asks about more commands even in bypass mode and refuses some. | |
| 2.1.326 | 2026-11-16 | Auto mode ignores wildcard shell allow rules that name no program or start with $HOME, and judges wildcard rules whose program is a Windows backslash path; a managed autoMode.environment list without $defaults replaces every built-in entry in Desktop and SDK apps too. | `autoMode.environment`, `$defaults` |
| 2.1.326 | 2026-11-16 | --add-dir and /add-dir in local terminal sessions show the trust prompt for an untrusted folder; claude --bg refuses such a folder. | `--add-dir`, `/add-dir`, `--bg` |
| 2.1.326 | 2026-11-16 | Startup warning when --allowedTools, --disallowedTools or --tools has an entry that is not a complete rule. | `--allowedTools`, `--disallowedTools`, `--tools` |
| 2.1.326 | 2026-11-16 | /rewind on macOS, Linux and WSL skips some files and reports them when the sandbox is on. | `/rewind` |
| 2.1.326 | 2026-11-16 | Permission answers over Remote Control and on self-hosted runners save always-allow choices differently. | |
| 2.1.325 | 2026-11-13 | Sandboxed Bash commands follow the normal permission flow by default; set sandbox.autoAllowBashIfSandboxed true to keep running them without prompts (set it in the highest-ranking managed source where managed settings turn the sandbox on). | `sandbox.autoAllowBashIfSandboxed` |
| 2.1.325 | 2026-11-13 | Read-only git commands ask first in a repository that is not the project's or a trusted one; name it with --add-dir, not additionalDirectories. | `--add-dir`, `additionalDirectories` |
| 2.1.325 | 2026-11-13 | Always allow in Desktop, IDE and SDK hosts offers a rule alone only when saving it would allow that command again, so a scheduled task relying on one may wait for you. | |
| 2.1.325 | 2026-11-13 | The sandbox refuses writes to .claude settings, skills, agents, commands and hooks in added directories as in the launch folder. | |
| 2.1.325 | 2026-11-13 | Sandbox helper programs, ripgrep, local git commands and the sandbox runtime run without sign-in tokens, API keys or the mTLS key passphrase in their environment. | |
| 2.1.325 | 2026-11-13 | Account email check also refuses your email as a client identity in scripts, file writes, web fetches and MCP calls. | |
| 2.1.323 | 2026-11-12 | Sandbox on macOS, Linux and WSL ignores write access granted through a symlink that leads elsewhere; git worktree add, move and remove and commits in a worktree the session did not start in fail read-only; start-up stops when a --settings file is invalid JSON and has a sandbox key. | |
| 2.1.323 | 2026-11-12 | Dont-ask-again allow rules that look like they hold a secret, or would be saved to a git-tracked settings.local.json, last for the session only. | |
| 2.1.323 | 2026-11-12 | /security-review asks before Claude runs it; skills' inline git commands stop in bare-repository worktrees until allowed outside auto and bypass mode. | `/security-review` |
| 2.1.323 | 2026-11-12 | A start-up warning for Bash allow rules with a star in a variable's value, such as Bash(PORT=* npm run dev). | |
| 2.1.323 | 2026-11-12 | glab config set without --global or --host fails read-only inside the Bash sandbox; worktree creation refuses checkouts whose .git folders are links or hold hard links. | |
| 2.1.321 | 2026-11-09 | cp and mv spelled by a path such as /bin/cp get the same path checks; account email check refuses only a shell command holding your email and naming a User-Agent. | |
| 2.1.319 | 2026-11-06 | Added permissions.denyInsteadOfPrompting: a tool call that would wait on a permission prompt is denied and the turn continues, in terminal sessions, subagents and teammates. | `permissions.denyInsteadOfPrompting` |
| 2.1.319 | 2026-11-06 | Auto mode with telemetry or feature flags off, including behind LLM gateways: unverifiable calls are asked or denied with no built-in classifier fallback; CLAUDE_CODE_AUTO_MODE_SERVER=0 keeps the classifier, =1 turns on the server check even with CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS set. | `CLAUDE_CODE_AUTO_MODE_SERVER`, `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` |
| 2.1.319 | 2026-11-06 | A project's settings files or a plugin can no longer switch auto mode's server-side check back on once switched off outside the project. | |
| 2.1.319 | 2026-11-06 | An exact Bash or PowerShell ask rule is refused when a broader deny rule covers the command; Bash asks before which with flags outside a lookup set; --add-dir directories register marketplaces only after their trust dialog is accepted. | |
| 2.1.316 | 2026-10-31 | autoMode.allow list without $defaults no longer removes the built-in rule on scheduled-task prompts; server-managed settings for Team and Enterprise apply without an approval prompt and an unverified stored copy is refused. | `autoMode.allow`, `$defaults` |
| 2.1.314 | 2026-10-30 | Added permissions.blockWritesOutsideWorkingDirectories: Write, Edit and NotebookEdit refuse paths outside the working directories in every permission mode. | `permissions.blockWritesOutsideWorkingDirectories` |
| 2.1.314 | 2026-10-30 | Auto mode in Cowork cloud sessions: a hook's allow of an MCP tool call counts as no answer; /permissions Recently blocked refuses approving a call you cannot read in full. | `/permissions` |
| 2.1.309 | 2026-10-22 | sed -i gets the standard Bash prompt and runs as written, no longer restored by /rewind; commands excluded from the sandbox ask before writing to its write-list paths while the sandbox is enabled but cannot run. | `/rewind` |
| 2.1.307 | 2026-10-21 | Added the claude_code.safety_event OpenTelemetry event for each tool call a rule, auto mode, safety check, hook or sandbox stopped, prompted or sent back (stopped being sent in 2.1.312). | `claude_code.safety_event` |
| 2.1.305 | 2026-10-20 | Added sandbox.allowNestedUserNamespaces so sandboxed Linux commands can create user namespaces (lets them get around the sandbox's file protections). | `sandbox.allowNestedUserNamespaces` |
| 2.1.304 | 2026-10-19 | Added /auto-mode-setup, also on Bedrock, Vertex, Foundry, Claude apps gateway and telemetry-disabled sessions. | `/auto-mode-setup` |
| 2.1.302 | 2026-10-16 | Added CLAUDE_CODE_AUTO_MODE_MODEL to choose the client-side auto mode classifier's model; auto mode with the server classifier compacts a too-long conversation instead of denying every checked call. | `CLAUDE_CODE_AUTO_MODE_MODEL` |
| 2.1.301 | 2026-10-15 | OTel tool_decision events gain classifier_verdict, permission_mode and (with OTEL_LOG_TOOL_DETAILS=1) classifier_category. | `classifier_verdict`, `permission_mode`, `classifier_category`, `OTEL_LOG_TOOL_DETAILS` |
| 2.1.300 | 2026-10-14 | CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST sessions ignore CA-bundle, tool-proxy, git TLS and git config variables in settings. | `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` |
| 2.1.299 | 2026-10-14 | Plan mode note when bypass permissions is available; Cowork cloud auto mode: PermissionRequest hook cannot approve shell commands or subagents. | |

# Not found in the documentation pages

- `attributionProject`
