---
type: "Guide"
title: "Platform, npm and binary install failures"
description: "Windows, Linux, macOS, WSL, Docker and npm-specific install failures with their versions and fixes."
resource: "https://code.claude.com/docs/en/troubleshoot-install"
tags: [install, windows, linux, npm, wsl]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_GIT_BASH_PATH"
  - "npm config set \"allow-scripts=@anthropic-ai/claude-code\" --location=user"
  - "EALLOWSCRIPTS"
  - "node node_modules/@anthropic-ai/claude-code/install.cjs"
  - "node node_modules/@anthropic-ai/claude-code/cli-wrapper.cjs"
  - "npm install -g @anthropic-ai/claude-code@latest"
  - "claude.exe.old.*"
  - "wsl --set-version <DistroName> 2"
  - "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"
  - "ZDOTDIR"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "troubleshoot-install"
    resource: "https://code.claude.com/docs/en/troubleshoot-install"
    title: "Troubleshoot installation and login"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A set of fixes for install and startup failures that depend on platform or package manager.

# How to use it

| Symptom | Cause and fix |
| :- | :- |
| `Killed` / `Installation was killed before it could finish (exit code 137)` on Linux | OOM kill. Install needs about 512 MB free; Claude Code needs at least 4 GB RAM. Add swap (2 GB swapfile example) or use a bigger instance. Before v2.1.200 only a bare `Killed` was shown. Message comes from the macOS/Linux/WSL script, never the Windows scripts. |
| Install hangs in Docker as root in `/` | Installer scans the filesystem; set `WORKDIR /tmp` before the install, or give Docker Desktop more memory. |
| `Raw mode is not supported` during install | Before v2.1.246, server-managed settings needing security approval tried to show a dialog during piped `claude install`. From v2.1.246 `claude install` and `claude update` skip the dialog. Still fails if startup waits for the settings fetch (for example `forceRemoteSettingsRefresh`). Rerun the installer. |
| `claude update` / `claude doctor` hang | Before v2.1.214, a directory at a shell config path (`~/.zshrc`, `~/.bashrc`, `~/.config/fish/config.fish`, `$ZDOTDIR/.zshrc`, first of `~/.bash_profile`/`~/.bash_login`/`~/.profile` on macOS) caused a hang. |
| `Claude Code on Windows requires either Git for Windows (for bash) or PowerShell` | Git for Windows is optional (PowerShell tool is used without Git Bash). Set `CLAUDE_CODE_GIT_BASH_PATH` to a `bash.exe`, `sh.exe`, `bash` or `sh` file; other names (for example `git-bash.exe`) are ignored with a `--debug` warning. Before v2.1.219 any existing file was accepted and a missing path exited at startup. |
| `Claude Code does not support 32-bit Windows` | Used the `Windows PowerShell (x86)` entry; open the non-x86 one. |
| `claude.exe` missing after update on Windows | Rename the newest `claude.exe.old.<timestamp>` backup back, or reinstall. Before v2.1.281 the backup could be deleted while `claude.exe` was missing. |
| `Error loading shared library` | musl/glibc binary mismatch; reinstall, on Alpine install the setup-page packages first. |
| `Illegal instruction` | Wrong architecture, or CPU/VM lacking AVX; no native-binary workaround (issue #50384). |
| `dyld: ... cannot load` on macOS | macOS 13.0 or later required. |
| `Bus error` / `oh no: Bun has crashed` mid-session | Executable became unreadable (truncated or deleted on network storage); start a new session. |
| `Exec format error` on WSL1 | Known regression (issue #38788); use `wsl --set-version <DistroName> 2` or a `claude()` shell function calling `/lib64/ld-linux-x86-64.so.2`. |
| `running scripts is disabled on this system` | PowerShell execution policy blocks npm `.ps1` shims; use `Set-ExecutionPolicy ... RemoteSigned -Scope CurrentUser`, the `.cmd` launcher, or the PowerShell installer. |

# Limits and defaults

- npm package downloads the native binary as a per-platform optional dependency; prebuilt binaries: `darwin-arm64`, `darwin-x64`, `linux-x64`, `linux-arm64`, `linux-x64-musl`, `linux-arm64-musl`, `win32-x64`, `win32-arm64`. FreeBSD is unsupported (before v2.1.205 it was treated as Linux).
- `Error: claude native binary not installed.` means postinstall did not run (`--ignore-scripts`, some pnpm configs) or optional dependencies were omitted (`--omit=optional`, `--no-optional`, `--ignore-optional`, `optional=false`). Corporate mirrors must carry all eight `@anthropic-ai/claude-code-*` platform packages.
- npm 12 skips postinstall by default: switch to the native installer, or add the package to `allow-scripts` in user npm config. On npm 12.0.x update to 12.1+ first; with the setting saved, some installs can fail with `EALLOWSCRIPTS`. Do not use `sudo` on `EACCES`.
- `npm error code ENOTEMPTY`: delete `$(npm root -g)/@anthropic-ai/claude-code` and leftover `.claude-code-*` directories, then reinstall.

# Notes

On Windows, `bin/claude.exe` from an npm install is a shell-script placeholder, so PowerShell and CMD report they cannot run the file rather than printing the message.
