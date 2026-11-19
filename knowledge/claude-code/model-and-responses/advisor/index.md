# model-and-responses/advisor

* [Advisor cost and prompt caching](advisor-cost-and-caching.md) - Advisor tokens bill at the advisor model's rates; toggling the advisor does not invalidate the main model's prompt cache. **[high]**
* [Advisor model pairings and Fable consent](advisor-model-pairings.md) - Which advisor models each main model accepts, aliases, version requirements, validation behavior and the Fable usage-credits consent. **[high]**
* [Advisor requirements and comparison](advisor-requirements.md) - Provider, gateway, model and feature-flag requirements for the advisor, and how it compares with opusplan, subagents and /model.
* [What an advisor consultation looks like](advisor-session-display.md) - The transcript lines shown while and after the advisor is consulted, and how Claude treats its guidance.
* [Advisor tool overview](advisor-tool-overview.md) - Claude consults a second, stronger server-side model at key moments; experimental and limited to some providers. **[high]**
* [Enable and disable the advisor](enable-the-advisor.md) - Set the advisor with /advisor, the advisorModel setting or the --advisor flag; turn it off with /advisor off or an env var. **[high]**
