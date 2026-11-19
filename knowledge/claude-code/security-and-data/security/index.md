# security-and-data/security

* [MCP, IDE and cloud execution security](mcp-ide-cloud-security.md) - MCP server trust model, plus controls for Anthropic-hosted cloud sessions (isolated VMs, proxy-held GitHub credentials, push restrictions) and Remote Control.
* [Permission modes and built-in protections](permissions-and-builtin-protections.md) - Auto and manual permission modes, accept edits, working directory boundary, sandboxed Bash and fail-closed matching. **[high]**
* [Prompt injection safeguards and trust verification](prompt-injection-safeguards.md) - Safeguards including network approval, WebFetch summaries, trust dialog behavior (none in -p mode), credential storage and the Windows WebDAV warning. **[high]**
* [Team security practices and vulnerability reporting](team-security-practices.md) - Managed settings, shared permissions, OpenTelemetry monitoring, ConfigChange hooks, sandbox runtime or dev container isolation, and the HackerOne reporting path.
