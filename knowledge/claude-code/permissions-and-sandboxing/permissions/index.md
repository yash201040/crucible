# permissions-and-sandboxing/permissions

* [What --add-dir directories load](add-dir-configuration-loading.md) - Additional directories grant file access only; flag-added ones also load skills, commands, subagents and a few settings keys. **[high]**
* [Agent and Cd permission rules](agent-and-cd-rules.md) - Agent(Name) rules gate subagents; Cd rules restrict the user-run /cd command and are not model-callable. **[high]**
* [Compound commands and stripped wrappers](bash-compound-commands-and-wrappers.md) - Every subcommand of a compound Bash command must be allowed; a fixed wrapper list is stripped before matching.
* [What a Bash rule does not match](bash-rule-limits.md) - Deny and ask Bash rules cover the usual invocation form only; other paths, sh -c and option variants slip past. **[high]**
* [Bash wildcard patterns](bash-wildcard-patterns.md) - How * works in Bash rules: position matters, trailing ' *' also matches the bare command, and :* is an equivalent suffix.
* [Exec wrappers and find actions](exec-wrappers-and-find-actions.md) - Prefix rules cannot auto-approve exec wrappers such as watch or find with -exec/-delete; use exact rules or a PreToolUse hook.
* [Precedence of hooks, rules and mods](hooks-rules-mods-precedence.md) - PreToolUse hooks cannot override deny or ask rules, a blocking hook beats allow rules, and mods can approve more in unmanaged setups. **[high]**
* [Managed settings and permission precedence](managed-settings-and-precedence.md) - Managed settings override everything; a deny at any level cannot be allowed elsewhere, and --allowedTools cannot override managed deny. **[high]**
* [Match rules by input parameter](match-by-input-parameter.md) - Deny and ask rules can match one scalar input parameter of a built-in tool, such as Agent(model:opus). **[high]**
* [Move the session with /cd](move-session-with-cd.md) - /cd changes the primary working directory, keeps the conversation and applies the new directory's project configuration at once.
* [Network path reads always prompt](network-path-reads.md) - From v2.1.292, reads of UNC or /net paths prompt regardless of allow rules, hooks or auto mode; dontAsk denies them.
* [Path escaping and ! negation](path-escaping-and-negation.md) - Approved paths are escaped; a deny or ask pattern starting with ! carves exceptions out of earlier rules from the same source.
* [Path pattern anchors and depth](path-pattern-anchors.md) - Read and Edit rules use gitignore syntax with //, ~/, / and relative anchors, and depth differs between allow and deny/ask.
* [Permission modes and mode-lock settings](permission-modes-reference.md) - The six permission modes, their aliases, and the settings that disable bypass or auto mode or deny instead of prompting. **[high]**
* [Comment on a permission prompt](permission-prompt-comments.md) - Attach a note to Claude when approving or denying a single action with Tab in the prompt.
* [Permission tiers and approval prompts](permission-tiers-and-prompts.md) - Which tool types ask for approval in Manual mode and where a 'Yes, and don't ask again' answer is saved.
* [How permissions interact with sandboxing](permissions-and-sandboxing-interplay.md) - Permissions gate tools and paths, sandboxing enforces OS limits on shell commands; autoAllowBashIfSandboxed skips the Bash prompt. **[high]**
* [PowerShell permission rules](powershell-rules.md) - PowerShell rules mirror Bash rules, with alias canonicalization, case-insensitive matching and AST-based compound splitting.
* [What runs before you trust a folder](pre-trust-repository-content.md) - Which repository-supplied content is used when only a parent is trusted or in claude -p and SDK runs, and how to harden an untrusted run. **[high]**
* [Workspace trust and project allow rules](project-allow-rules-and-trust.md) - Project allow rules and additionalDirectories apply only after the workspace trust dialog, which is not shown in -p or SDK runs. **[high]**
* [Read and Edit rules: coverage and gaps](read-edit-rules.md) - Edit rules cover all file-editing tools, Read deny is best-effort for readers and attachments; Write/Glob/Grep path rules never match. **[high]**
* [Built-in read-only Bash commands](read-only-commands.md) - A fixed, non-configurable set of Bash commands runs without prompts, with listed cases that still prompt in Manual mode.
* [Redirection and tee target checks](redirections-and-tee-checks.md) - Redirect and tee targets are checked against Edit/Read rules, protected paths and working directories.
* [Allow, ask and deny rules and their order](rule-order-and-manage-rules.md) - Rules are evaluated deny, then ask, then allow; /permissions edits them live and a bare tool-name deny removes the tool. **[high]**
* [Permission rule syntax](rule-syntax-and-match-all.md) - Rules are Tool or Tool(specifier); a bare name matches all uses, and tool labels differ from canonical names.
* [Symlink handling in permission checks](symlink-permission-checks.md) - Permission checks cover both the requested path and its resolved target; allow needs both to match, deny needs either.
* [Tool-name wildcards and MCP rules](tool-name-wildcards.md) - Glob patterns in the tool-name position for deny/ask rules, anchored globs for allow, and how MCP server names map to rules. **[high]**
* [WebFetch domain rules](webfetch-domain-rules.md) - WebFetch rules use domain: with * wildcards; bare WebFetch and WebFetch(domain:*) differ for the sandbox and artifact reads.
* [Working directories and additional directories](working-directories.md) - The launch directory is the primary working directory; extend access with --add-dir, /add-dir or additionalDirectories. **[high]**
