# automation/channels

* [Channel enterprise controls](channel-enterprise-controls.md) - Managed settings channelsEnabled and allowedChannelPlugins, defaults by authentication type, and what happens when blocked.
* [Channel sender allowlists and pairing](channel-security.md) - Each approved channel keeps a sender allowlist; Telegram and Discord pair by code, iMessage self-chat bypasses the gate.
* [Channels](channels-overview.md) - A channel is an MCP server that pushes events (chat, webhooks, CI) into a running session; two-way, research preview. **[high]**
* [Channels research-preview limits](channels-research-preview.md) - Preview status: flag syntax may change, flags hidden from --help, allowlist-only plugins, and the development flag.
* [Fakechat quickstart](fakechat-quickstart.md) - Try channels with the officially supported localhost demo channel before connecting a real platform.
* [Telegram, Discord and iMessage plugins](supported-channel-plugins.md) - Setup steps, config files, env vars and access commands for the three supported channel plugins (all need Bun).
