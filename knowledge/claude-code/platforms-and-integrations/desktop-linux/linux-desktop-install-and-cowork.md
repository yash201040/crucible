---
type: "Guide"
title: "Claude Desktop on Linux (beta)"
description: "Installing and updating the desktop app on Ubuntu and Debian via apt or .deb, Cowork virtualization requirements, and what the beta lacks."
resource: "https://code.claude.com/docs/en/desktop-linux"
tags: [desktop, linux, beta, apt, cowork]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [desktop]
requires: "Ubuntu 22.04+ or Debian 12+, x86_64 or arm64; Cowork needs KVM"
identifiers:
  - "claude-desktop"
  - "CLAUDE_DESKTOP_ADD_REPO"
  - "/etc/default/claude-desktop"
  - "/etc/apt/sources.list.d/claude-desktop.list"
  - "/usr/share/keyrings/claude-desktop-archive-keyring.asc"
  - "/dev/kvm"
  - "/dev/vhost-vsock"
  - "vhost_vsock"
  - "/etc/claude-desktop/managed-settings.json"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop-linux"
    resource: "https://code.claude.com/docs/en/desktop-linux"
    title: "Claude Desktop on Linux (beta)"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Linux desktop app gives the same Chat, Cowork and Claude Code experience as macOS and Windows. Linux support is in beta. Only Debian-based distributions are supported (Fedora, Arch and others: use the CLI; Fedora and RHEL support is planned).

# How to use it

1. Download key: `sudo curl -fsSLo /usr/share/keyrings/claude-desktop-archive-keyring.asc https://downloads.claude.ai/claude-desktop/key.asc`; verify with `gpg --show-keys`; fingerprint must be `31DDDE24DDFAB679F42D7BD2BAA929FF1A7ECACE`.
2. Register the apt repo `https://downloads.claude.ai/claude-desktop/apt/stable stable main` in `/etc/apt/sources.list.d/claude-desktop.list` (arch amd64, arm64).
3. `sudo apt update && sudo apt install claude-desktop`; launch Claude or run `claude-desktop`; sign in.

Alternatives: download the `.deb` from the pool and `sudo apt install ./claude-desktop_*.deb`; to skip registering the repo, create `/etc/default/claude-desktop` with `CLAUDE_DESKTOP_ADD_REPO="false"` (then no automatic updates). Update: the app does not self-update; use `sudo apt update && sudo apt upgrade`. Uninstall: `sudo apt remove claude-desktop`.

Policy file for admins: `/etc/claude-desktop/managed-settings.json`.

# Limits and defaults

- Cowork runs in a QEMU/KVM VM: needs hardware virtualization, QEMU and UEFI packages (`qemu-system-x86`, `ovmf`, `virtiofsd` on x86_64; `qemu-system-arm`, `qemu-efi-aarch64`, `virtiofsd` on arm64), access to `/dev/kvm` and `/dev/vhost-vsock` (join the `kvm` group; `sudo modprobe vhost_vsock`). Checked once at launch.
- Not in the beta: Computer Use, Dictation (use CLI voice dictation), Quick Entry hotkey on native Wayland needs the GlobalShortcuts portal (works on X11).
- Must not run as root. Sign-in is stored in the desktop keyring (GNOME Keyring or KDE Wallet); without an unlocked keyring you sign in every launch. libc6 >= 2.34 required.
