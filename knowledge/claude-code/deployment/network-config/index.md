# deployment/network-config

* [Network settings for background agents](background-agents-network.md) - Background sessions are hosted by a shared supervisor, so network variables must live in settings, not the shell; processWrapper applies there too. **[high]**
* [Network access requirements and allowlists](network-access-requirements.md) - Hosts Claude Code reaches, what each is for and how to disable optional ones, plus provider routing, IP allowlist and GitHub firewall notes.
* [Proxy, CA certificate and mTLS configuration](proxy-ca-and-mtls.md) - Proxy variables, CA store sources, custom CA files and mTLS client certificates with rotation behavior, plus where each is honored.
* [Streaming idle watchdogs and timeouts](streaming-idle-watchdogs.md) - Four timers that abort quiet streaming responses, their defaults, which providers each runs on, and the variables that tune them. **[high]**
