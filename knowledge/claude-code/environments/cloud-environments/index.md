# environments/cloud-environments

* [Configure, select from the CLI, and archive environments](configure-select-archive-environments.md) - How to add or edit environments in the selector, set the CLI default with /remote-env, and archive an environment. **[high]**
* [Default allowed domains](default-allowed-domains.md) - Domains reachable under Limited network access with Allow package managers checked, grouped by category.
* [Default environment and how sessions pick one](default-environment-and-selection.md) - Cloud sessions run in an environment; Default has Limited network and no config, and each surface picks an environment differently. **[high]**
* [Environment caching](environment-caching.md) - Anthropic snapshots the filesystem after a setup script completes within about five minutes and reuses it for later sessions. **[high]**
* [Environment variables in cloud environments](environment-variables.md) - How .env-format variables on an environment reach sessions, when they refresh, and which ones are treated specially. **[high]**
* [GitHub proxy and security proxy](github-and-security-proxies.md) - In Anthropic-hosted environments GitHub traffic goes through a credential-swapping proxy with push and GraphQL restrictions, and all traffic through a security proxy. **[high]**
* [Network access levels and allowed domains](network-access-levels.md) - Each environment has one of three network access levels (None, Limited, Full) plus an allowed-domains list; some paths bypass it. **[high]**
* [Network secrets (agent proxy credentials)](network-secrets.md) - Store an API key on a cloud environment so Anthropic's agent proxy attaches it to requests for listed hosts without the session seeing it. **[high]**
* [Organization-shared environments and Claude Tag](organization-shared-environments.md) - Owners on Team and Enterprise can share environments org-wide, set an org default, and pick the environment Claude Tag channels use.
* [Cloud VM resource and time limits](resource-and-time-limits.md) - Approximate VM ceilings (4 vCPU, 16 GB, 30 GB) and the time limits for commands, hooks, setup scripts and idle sessions. **[high]**
* [Setup scripts vs SessionStart hooks in the cloud](setup-script-vs-sessionstart-hook.md) - When to use each, the order they run, an example dependency-install hook keyed on CLAUDE_CODE_REMOTE, and cloud limitations of hooks. **[high]**
* [Setup scripts](setup-scripts.md) - A Bash script run as root when a new cloud session starts, before Claude Code launches, to install tools not pre-installed. **[high]**
* [Cloud VM image and pre-installed tools](vm-installed-tools.md) - Ubuntu 24.04 x86_64 VM with listed language runtimes, databases, Docker and Chrome; what is not pre-installed.
* [What carries over into cloud sessions](what-carries-over-from-your-setup.md) - Table of which repo, user and organization configuration reaches a cloud session, and how to add personal preferences. **[high]**
