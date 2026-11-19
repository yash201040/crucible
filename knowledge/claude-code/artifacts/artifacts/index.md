# artifacts/artifacts

* [Artifacts overview](artifacts-overview.md) - An artifact is a live, interactive page Claude Code publishes from a session to a private claude.ai URL that updates in place.
* [Artifact availability requirements](availability-requirements.md) - Plan, authentication, provider, policy and surface conditions that must all hold for artifacts, including SDK and -p exclusions. **[high]**
* [Comments and automatic replies](comments-and-auto-reply.md) - Claude reads and replies to comment threads on a shared artifact and, from v2.1.228, is notified and replies on its own within caps. **[high]**
* [Create and publish an artifact](create-and-publish.md) - How Claude writes and publishes an artifact file, what opens, and the keys and variables that control reopening and auto-open.
* [Disable artifacts](disable-artifacts.md) - Ways to turn artifacts off: /config, enableArtifact, CLAUDE_CODE_DISABLE_ARTIFACT, a deny rule, and precedence rules.
* [Offer a file download](file-download-capability.md) - A page offers generated files (CSV, PNG) through the downloads capability because the viewer blocks self-started downloads.
* [Live data from MCP connectors](mcp-connector-pages.md) - A published page can call claude.ai MCP connectors on each view, using the viewer's own connections.
* [Organization admin and Compliance API](organization-admin-controls.md) - Owner toggles, retention, audit and the Compliance API endpoints for listing and deleting an organization's artifacts.
* [Artifact page constraints](page-constraints.md) - CSP and format rules for an artifact page: allowed CDNs, no backend, source types, 16 MiB size, no self-started downloads.
* [When publishing asks for approval](publish-approval-prompts.md) - The cases in which Claude Code asks you, or the auto-mode classifier, before publishing or changing an artifact. **[high]**
* [Read an artifact shared with you](read-shared-artifact.md) - Claude reads another person's artifact like a WebFetch summary and Claude Code asks approval in several cases.
* [Share an artifact and co-edit](share-and-edit.md) - Audiences for sharing (organization, folder, public), view links, editor role and handling of stale copies.
* [Update and find artifacts](update-and-find.md) - Republishing to the same URL, versions, updating from another session, one-step edits, and the /artifacts list and keys.
* [Design guidance, templates and /design](visual-design-and-templates.md) - Built-in design skill, design-system precedence, Google Fonts rule, account templates, the /design command and Claude Docs.
