---
type: "Reference"
title: "Isolation technologies and hardened Docker flags"
description: "Comparison of sandbox runtime, Docker, gVisor and VMs, with the hardened docker run options and the Unix socket proxy architecture."
resource: "https://code.claude.com/docs/en/agent-sdk/secure-deployment"
tags: [isolation, docker, gvisor, firecracker, sandbox-runtime]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk, cli]
requires: ""
identifiers:
  - "--cap-drop ALL"
  - "--security-opt no-new-privileges"
  - "--security-opt seccomp="
  - "--read-only"
  - "--tmpfs"
  - "--network none"
  - "--memory"
  - "--cpus"
  - "--pids-limit"
  - "--user"
  - "--userns-remap"
  - "--ipc private"
  - "--runtime=runsc"
  - "/etc/docker/daemon.json"
  - "bubblewrap"
  - "sandbox-exec"
  - "vsock"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-secure-deployment"
    resource: "https://code.claude.com/docs/en/agent-sdk/secure-deployment"
    title: "Securely deploying AI agents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Technology | Isolation strength | Overhead | Complexity |
| - | - | - | - |
| Sandbox runtime | Good (secure defaults) | Very low | Low |
| Containers (Docker) | Setup dependent | Low | Medium |
| gVisor | Excellent (with correct setup) | Medium/High | Medium |
| VMs (Firecracker, QEMU) | Excellent (with correct setup) | High | Medium/High |

# How to use it

- Sandbox runtime (`sandbox-runtime`): OS-level filesystem and network limits with no containers. `bubblewrap` on Linux, `sandbox-exec` on macOS; commands run in their own network namespace or under a Seatbelt profile, routed through a built-in proxy with a domain allowlist; JSON allowlists. Caveats: shares the host kernel; no TLS inspection by default so allowlist is by client-supplied hostname (domain fronting possible); permissive credentials on an allowed domain can be abused for exfiltration.
- Hardened container: `docker run --cap-drop ALL --security-opt no-new-privileges --security-opt seccomp=/path/to/seccomp-profile.json --read-only --tmpfs /tmp:rw,noexec,nosuid,size=100m --tmpfs /home/agent:rw,noexec,nosuid,size=500m --network none --memory 2g --cpus 2 --pids-limit 600 --user 1000:1000 -v /path/to/code:/workspace:ro -v /var/run/proxy.sock:/var/run/proxy.sock:ro agent-image`. Docker's default seccomp blocks about 44 syscalls. Avoid mounting `~/.ssh`, `~/.aws`, `~/.config`. Extra hardening: `--userns-remap` (needs daemon config), `--ipc private`.
- Unix socket architecture: with `--network none` run a proxy on the host and mount its socket; if `ANTHROPIC_BASE_URL` or `HTTP_PROXY` point at a localhost port, relay that port inside the container to the socket. Within the allowlist the agent can still send data to any allowed domain.
- gVisor: install `runsc`, register under `runtimes` in `/etc/docker/daemon.json`, run `docker run --runtime=runsc agent-image`. Overhead: about 0% CPU-bound, about 2x simple syscalls, up to 10-200x for heavy open/close file I/O.
- Firecracker microVM: boots in under 125 ms with under 5 MiB memory overhead; the VM has no network interface and talks over `vsock` to a host proxy that enforces allowlists and injects credentials. VMs depend on hypervisor and device emulation quality.
- Cloud: private subnet with no internet gateway; firewall rules (AWS Security Groups, GCP VPC) blocking all egress except the proxy; a proxy such as Envoy with `credential_injector`; minimal IAM; log all traffic at the proxy.
