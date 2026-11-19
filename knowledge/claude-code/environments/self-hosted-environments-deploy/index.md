# environments/self-hosted-environments-deploy

* [Git configuration and Anthropic git proxy](git-configuration-and-proxy.md) - How runners get git identity, credentials and signing: --configure-git, shipped config, Anthropic-managed git (github.com only), URL rewrites. **[high]**
* [Harden a self-hosted runner deployment](harden-deployment.md) - Checklist of isolation, credential, egress, IAM and repo-settings controls to apply before connecting self-hosted runners to production systems. **[high]**
* [Known issues and troubleshooting](known-issues-and-troubleshooting.md) - Connector traffic leaving the network, common runner and session failures with their log lines, and proxy problems with the SSE stream.
* [Network requirements and egress proxy authentication](network-requirements-egress-proxy.md) - Hosts a runner and its sessions must reach, hosts that need no allowlisting, and how to authenticate to a corporate egress proxy.
* [Build the runner image and size resources](runner-image-and-sizing.md) - Dockerfile starting point, version pinning, CPU and memory starting values, per-session memory limits, and pid limits for runner containers. **[high]**
* [Kubernetes, Compose, shutdown timing and runner exits](runner-supervision-and-shutdown.md) - Deployment recipes, health probes, how SIGTERM drains a runner, defer-shutdown, stop-timeout sizing, and restart-with-backoff rules. **[high]**
* [Scale the fleet and release idle sessions](scaling-and-idle-sessions.md) - Fixed fleet versus on-demand runners, owner-locking, releasing idle sessions, holding idle sessions, and kill-after limits. **[high]**
