# model-and-responses/code-mode

* [Code Mode overview and limitations](code-mode-overview.md) - Experimental mode where Claude writes JavaScript that makes several tool calls in one step, with a list of its limitations. **[high]**
* [Code Mode permission checks and hooks](code-mode-permissions-and-hooks.md) - How permission rules, PreToolUse and PostToolUse hooks and the auto mode classifier apply to code that Code Mode runs. **[high]**
* [Code Mode requirements](code-mode-requirements.md) - Version, account, organization, model, surface, installation and agent-teams requirements for Code Mode. **[high]**
* [Code Mode troubleshooting](code-mode-troubleshooting.md) - Reasons Code Mode does not start with fixes, and the hook-failure errors that refuse tool calls.
* [Turn Code Mode on, off, or block it](enable-and-disable-code-mode.md) - Enable with CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1, resume only with it on, and block it organization-wide with managed settings. **[high]**
* [Code Mode long-running and background code](long-running-code.md) - Code waits up to ten minutes by default; in auto or bypassPermissions mode it can run in the background for up to two hours. **[high]**
