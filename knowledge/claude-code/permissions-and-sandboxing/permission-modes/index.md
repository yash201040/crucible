# permissions-and-sandboxing/permission-modes

* [acceptEdits mode](acceptedits-mode.md) - Auto-approves file edits and common filesystem commands inside the working directory; lists what still prompts.
* [Actions no mode auto-approves](actions-no-mode-approves.md) - Calls that still prompt or are denied in every permission mode, including bypassPermissions. **[high]**
* [Boundaries and approvals in conversation](auto-conversation-boundaries.md) - How the classifier treats user-stated boundaries as blocks and stated approvals as clearing a block, and their limits. **[high]**
* [Auto mode fallback and block thresholds](auto-fallback-thresholds.md) - Behavior when the classifier blocks or fails: 3 in a row or 20 total pauses auto mode; non-interactive runs keep going. **[high]**
* [First read outside working directories](auto-first-read-outside.md) - Auto mode asks once before the first Read/Grep/Glob outside working directories; the four answers and the setting they write.
* [Auto mode and its requirements](auto-mode-availability.md) - What auto mode is, supported plans, providers and models, how to disable it, and why it may be unavailable. **[high]**
* [Auto mode with subagents; cost and latency](auto-subagents-cost.md) - Classifier checks at subagent spawn, run and finish, and which accounts pay for classifier calls. **[high]**
* [bypassPermissions mode](bypass-permissions-mode.md) - Disables prompts and safety checks; enabling rules, root refusal, warning dialog, background-session and cloud limits. **[high]**
* [What the classifier allows by default](classifier-allowed-by-default.md) - Actions auto mode lets through without a prompt, including branch pushes, and how to force a checkpoint with ask rules. **[high]**
* [What the classifier blocks by default](classifier-blocked-by-default.md) - Default block list for auto mode, version-gated additions, and the trust boundary it assumes. **[high]**
* [How the classifier evaluates actions](classifier-decision-order.md) - Fixed decision order for each action in auto mode, rule exceptions, dropped allow rules, and what the classifier sees. **[high]**
* [Choose the classifier model](classifier-model-choice.md) - Default classifier model rules and CLAUDE_CODE_AUTO_MODE_MODEL override, plus how to verify with the debug log. **[high]**
* [Common permission setups](common-setups.md) - Goal-to-command table pairing review, plan, auto, CI allowlist and unattended container runs with flags and isolation. **[high]**
* [Critical-path removals per mode and timeouts](critical-path-outcomes.md) - Outcome of a critical-path removal in each mode and surface, the two-minute countdown, and CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT. **[high]**
* [Turn off the rm prompt in bypass mode](critical-path-prompt-off.md) - CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS lets critical-path rm run unprompted in bypassPermissions, with startup notices and causes it fails. **[high]**
* [Critical-path rm protection](critical-paths.md) - Which rm and rmdir targets count as critical paths, what no allow rule or hook can approve, and the controls that still apply. **[high]**
* [Dangerous rm and mounted drive prompts](dangerous-rm-and-mounted-drive.md) - The Dangerous rm operation not ruled out reason, the mounted-drive prompt, path shapes, and the env var that disables it.
* [dontAsk mode](dontask-mode.md) - Auto-denies every call that would prompt; only pre-approved tools and no-approval actions run, for CI and scripts. **[high]**
* [Default mode in -p and SDK runs](headless-sdk-default-mode.md) - Non-interactive and Agent SDK runs start Manual (default) from v2.1.302 and deny calls needing approval unless allowed. **[high]**
* [Permission modes under HIPAA configuration](hipaa-permission-modes.md) - How the HIPAA configuration changes the starting mode by version and which managed settings disable auto and bypass.
* [Permission modes overview](modes-overview.md) - The six permission modes, what each runs without asking, the Manual/default naming, and how rules layer on top. **[high]**
* [Review and approve a plan](plan-approval.md) - The approval prompt options in plan mode and what mode each one switches the session to.
* [Plan mode](plan-mode.md) - Research-and-propose mode that blocks edits until a plan is approved; shell commands go to the classifier or prompt.
* [Protected paths](protected-paths.md) - Directories and files whose writes are gated per permission mode, with the per-mode outcome table and exceptions. **[high]**
* [Remove-Item and cmd removal checks](remove-item-powershell.md) - PowerShell Remove-Item and cmd rd/del checks: system paths and wildcards denied in every mode, and the opt-out variable.
* [Server-side classifier review](server-side-classifier-review.md) - Auto mode can have the server review actions inside the session's model requests, with version gates, fallbacks and the CLAUDE_CODE_AUTO_MODE_SERVER switch. **[high]**
* [Set the starting permission mode](start-in-different-mode.md) - Where to set permissions.defaultMode per scope (session, machine, project, organization) and what each honors.
* [Which mode a session starts in](starting-mode-resolution.md) - Order of precedence and built-in default for a new session's permission mode, with version gates. **[high]**
* [Switch modes in the CLI](switch-modes-cli.md) - Shift+Tab cycle order, status bar labels, which modes join the cycle, and the Bash-prompt switch to auto.
* [Switch modes in VS Code, Desktop, web](switch-modes-ide-desktop-web.md) - Mode selectors, labels and start-mode rules for VS Code, the desktop app, cloud sessions and Remote Control.
