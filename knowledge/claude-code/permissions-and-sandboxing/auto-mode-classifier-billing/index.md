# permissions-and-sandboxing/auto-mode-classifier-billing

* [Auto mode classifier charge notice](ineligible-session-notice.md) - Notice shown when server-side no-charge classifier checks do not reach the session, so Claude Code's own billed classifier requests are used. **[high]**
* [Make the session eligible (CLAUDE_CODE_AUTO_MODE_SERVER)](make-session-eligible.md) - Gateway pass-through requirements for server-side classifier checks and the temporary CLAUDE_CODE_AUTO_MODE_SERVER=0 opt-out. **[high]**
* [Why the classifier billing notice appears](why-notice-appears.md) - Plans that never see the notice and the usual causes: a gateway or proxy in the path, or server-side checks not yet reaching a platform, region or credential.
