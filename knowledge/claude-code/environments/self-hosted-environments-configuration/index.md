# environments/self-hosted-environments-configuration

* [Send model requests to Bedrock or Agent Platform](bedrock-and-agent-platform-inference.md) - Configure a runner so sessions call models in your AWS or Google Cloud account, and what changes in those sessions. **[high]**
* [Runner lifecycle hooks](lifecycle-hooks.md) - checkout, post-session and command hooks in a hooks directory that replace stages of the runner's per-session pipeline. **[high]**
* [MCP servers in self-hosted sessions](mcp-servers-in-sessions.md) - How MCP servers reach runner sessions, startup waits, and denying the built-in Claude Code Remote server. **[high]**
* [On-demand runners and the orchestrator](on-demand-runners-orchestrator.md) - A stateless orchestrator runs a spawn-runner hook per queued session to boot one single-use runner each, with an exit-code contract. **[high]**
* [Permissions and per-session config assembly](permissions-and-session-config.md) - How the runner builds each session's config from a host snapshot, pins permission mode, and handles repository settings and managed settings. **[high]**
* [Stop hook that prompts sessions to push work](stop-hook-push-nudge.md) - Reference Stop hook for runners that nudges Claude to commit and push, since the runner installs none. **[high]**
* [Runner wrapper scripts](wrapper-scripts.md) - A script the runner starts in place of the Claude Code binary for each session, with a documented environment and fd rules. **[high]**
