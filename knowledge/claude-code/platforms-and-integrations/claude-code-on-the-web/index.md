# platforms-and-integrations/claude-code-on-the-web

* [Auto-fix pull requests](auto-fix-pull-requests.md) - Claude watches a PR in a cloud session and responds to CI failures and review comments, pushing fixes when clear. **[high]**
* [Cloud session context, commands, sharing and expiry](cloud-session-management-and-limits.md) - Permission modes, supported commands, auto-compaction variables, subagents, sharing, archiving, environment expiry and what is not restored. **[high]**
* [Cloud sessions, environments and GitHub access](cloud-sessions-overview.md) - Cloud sessions run Claude Code on Anthropic or self-hosted infrastructure, started from web, mobile, desktop, terminal or schedules, with GitHub connection options. **[high]**
* [Send follow-ups to a cloud session from the CLI](send-followups-to-cloud-session.md) - claude -p with --cloud <session-id> queues a message into an existing cloud session and exits, usable from scripts and CI. **[high]**
* [Start cloud sessions with --cloud and teleport back](start-and-teleport-sessions.md) - claude --cloud creates cloud sessions from the terminal, local repos can be bundled and uploaded, and --teleport pulls a session into the terminal. **[high]**
