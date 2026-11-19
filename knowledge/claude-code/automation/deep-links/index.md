# automation/deep-links

* [Choosing cwd or repo](cwd-versus-repo.md) - cwd suits identical paths; repo resolves a slug to the clone or worktree where claude last ran, without changing branch.
* [claude-cli:// deep links](deep-link-format.md) - A claude-cli:// URL opens Claude Code in a new local terminal with a working directory and a pre-filled, unsent prompt.
* [Deep link handler registration and platforms](handler-registration.md) - When and where Claude Code registers the claude-cli:// handler, terminal selection per OS, disableDeepLinkRegistration, VS Code and Desktop links.
* [Open a deep link from a shell or runbook](open-link-from-shell.md) - Per-OS commands to open a claude-cli:// link from scripts, and notes on embedding links in runbooks and GitHub Markdown.
