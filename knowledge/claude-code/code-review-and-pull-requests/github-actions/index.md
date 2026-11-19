# code-review-and-pull-requests/github-actions

* [Action inputs, CLI args, costs and troubleshooting](action-parameters-and-costs.md) - Common claude-code-action inputs, passing CLI args such as --max-turns, cost controls, beta-to-v1 migration, and fixes for non-responding or CI-less runs. **[high]**
* [GitHub Action setup, secrets and app permissions](github-action-setup.md) - Install claude-code-action via /install-github-app or manually, with ANTHROPIC_API_KEY or CLAUDE_CODE_OAUTH_TOKEN, org rollout, OIDC federation and App permissions. **[high]**
* [Action interactive and automation modes](interactive-and-automation-modes.md) - The action detects mode from the prompt input: no prompt waits for @claude, a prompt runs automatically; checks on who can trigger runs. **[high]**
