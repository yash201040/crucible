# platforms-and-integrations/desktop

* [Cloud sessions, Remote Control and Dispatch in Desktop](cloud-remote-control-and-dispatch.md) - Send work to the cloud, continue sessions elsewhere, expose local sessions to other devices, and receive Dispatch-started sessions. **[high]**
* [Code tab sessions, prompt box and workspace](code-tab-workspace-and-prompting.md) - How a Desktop session starts, the prompt box, panes, terminal, file editing, view modes, keyboard shortcuts and usage display.
* [Computer use in Desktop](computer-use-in-desktop.md) - Research-preview screen and app control on macOS and Windows with per-app tiers, off by default.
* [Connectors, skills and plugins in Desktop](connectors-skills-and-plugins.md) - Connector directory, skill invocation and plugin management in the Code tab, with SSH, WSL and cloud differences.
* [Desktop troubleshooting and SSH error codes](desktop-troubleshooting.md) - Fixes for 403 errors, blank screens, layout and version checks, host key failures and SSH connection error codes.
* [Desktop versus CLI comparison](desktop-vs-cli.md) - What carries over from the CLI, flag equivalents, moving sessions with /desktop and claude --desktop, and what Desktop lacks. **[high]**
* [Diff view, code review and PR monitoring](diff-review-and-pr-monitoring.md) - Line comments on diffs, the /code-review card, and Auto-fix or Merge when ready for pull requests in Desktop.
* [Desktop device policies, sign-in control and network access](enterprise-policies-and-network.md) - Admin console toggles, MDM and policy file locations, forceLoginOrgUUID, firewall hosts and deployment methods for Desktop.
* [Environments and environment variables](environments-and-env-vars.md) - Saved local, SSH and cloud environments, how to set variables for sessions and dev servers, and variables Desktop sets itself. **[high]**
* [Managed settings keys for Desktop](managed-settings-keys-for-desktop.md) - Managed keys that govern Desktop behavior and the Claude Code settings that act differently in the Code tab.
* [Parallel sessions, worktrees and cross-session control](parallel-sessions-and-worktrees.md) - Run many sessions side by side, isolate them in Git worktrees, use side chats, watch background tasks, and let Claude message other sessions. **[high]**
* [Desktop permission modes and auto mode](permission-modes-in-desktop.md) - The five Desktop permission modes with their settings keys, defaults, cloud limits and auto mode availability. **[high]**
* [App preview, Browser pane and launch.json](preview-browser-and-launch-json.md) - Claude starts dev servers in the Browser pane, auto-verifies edits, browses external sites with approvals, and is configured via .claude/launch.json.
* [SSH tasks while Desktop is disconnected](ssh-disconnected-tasks-and-helper.md) - How SSH tasks keep running when Desktop sleeps or quits, the limits that end them, and what the remote helper installs. **[high]**
* [SSH host commands, sshConfigs and allowlist](ssh-managed-connections-and-host-commands.md) - Settings that create or distribute SSH connections: sshHostCommands, sshConfigs, sshHostAllowlist and related controls. **[high]**
* [SSH sessions: setup and requirements](ssh-sessions-setup.md) - Connecting Desktop to remote machines over SSH: fields, requirements, ssh config use, jump hosts, containers, port forwarding and Windows remotes. **[high]**
