# permissions-and-sandboxing/sandbox-environments

* [Sandbox approaches compared](compare-sandbox-approaches.md) - Six isolation options from the per-command Bash sandbox to cloud sessions, with what each isolates and requires. **[high]**
* [Dev containers, custom containers, VMs and cloud sessions](containers-vms-and-cloud-sessions.md) - Container, VM and cloud isolation options for running Claude Code, including the example dev container with a default-deny firewall. **[high]**
* [Enforcing isolation across an organization](enforce-isolation-organization.md) - Only the built-in Bash sandbox is enforced by Claude Code via managed settings; containers and VMs rely on device management.
* [Isolation for unattended runs](isolation-and-permission-modes.md) - Run --dangerously-skip-permissions only inside a container, VM or sandbox runtime; auto mode's classifier is not an isolation boundary. **[high]**
* [Sandbox runtime built-in denies and start-up behavior](sandbox-runtime-built-in-denies.md) - The runtime denies risky writes by default, differs between macOS and Linux on nested paths, and refuses to start on a bad settings file. **[high]**
* [Set up and launch the sandbox runtime](sandbox-runtime-setup.md) - Install @anthropic-ai/sandbox-runtime, write ~/.srt-settings.json with write and network allowances, and launch with srt claude. **[high]**
* [Sandboxed Bash tool scope](sandboxed-bash-tool.md) - The built-in per-command sandbox restricts Bash, PowerShell and Monitor commands only; MCP servers, hooks and monitors run unconstrained. **[high]**
