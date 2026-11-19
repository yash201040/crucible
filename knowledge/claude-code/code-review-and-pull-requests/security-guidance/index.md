# code-review-and-pull-requests/security-guidance

* [Security guidance plugin](security-guidance-plugin.md) - A hook-based plugin that reviews Claude's own edits for vulnerabilities per edit, per turn and per commit, and has Claude fix findings in the same session. **[high]**
* [Security guidance custom rules and switches](security-guidance-rules-and-env.md) - Add reviewer guidance and per-edit patterns via .claude files and toggle layers or models with ENABLE_* and SECURITY_REVIEW_MODEL variables.
* [Security guidance in the security tool stack](security-guidance-tool-layers.md) - Where the in-session security guidance plugin sits relative to /security-review, the Claude Security plugin, Code Review and CI scanners.
