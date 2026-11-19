# environments/self-hosted-environments-reference

* [Runner environment-variable-only settings and telemetry](environment-variable-only-settings.md) - Env vars with no flag form: background grace, host config dir, fetch depth, git verify skip, plus telemetry controls for session children.
* [Health endpoint and runner Prometheus metrics](health-and-runner-metrics.md) - GET /healthz body, runner /metrics series, session lifecycle counter semantics, and how to join session cost to idle time. **[high]**
* [Orchestrator CLI flags and SCM connector](orchestrator-flags.md) - Flags of self-hosted-runner orchestrator for on-demand runners: hook concurrency and timeouts, pre-warming, shutdown drain, SCM connector. **[high]**
* [Orchestrator metrics, autoscaling and alert rules](orchestrator-metrics-and-alerts.md) - Orchestrator /healthz and /metrics series, autoscaling guidance for HPA and KEDA, PodMonitor, and sample Prometheus alert rules. **[high]**
* [Runner CLI flags: secrets, git, security and logs](runner-flags-config-git-security.md) - Runner flags for the environment secret, git handling, repo-settings guard, host config snapshot, proxy auth, auto mode lists and logging. **[high]**
* [Runner CLI flags: capacity, lifecycle and drain](runner-flags-lifecycle.md) - Runner flags for base dir, capacity, idle release, kill limits, drain, retire, hold and health, with env var pairs and defaults. **[high]**
