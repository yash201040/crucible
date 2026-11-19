# environments/self-hosted-environments-testing

* [Authenticating dispatch commands from CI](ci-authentication.md) - claude -p --environment and --cloud need a claude.ai OAuth token with a 30-day cap; API keys, setup-token and environment secrets do not work. **[high]**
* [Create and delete test environments via API](create-delete-test-environment-api.md) - Programmatic create and delete of self-hosted environments with the ccr-byoc beta header, so each CI run gets a clean environment. **[high]**
* [End-to-end test loop with Stop-hook read-back](e2e-test-loop-stop-hook.md) - Dispatch a session with claude -p --environment, capture each reply via a Stop hook, send follow-ups with --cloud, assert in CI. **[high]**
