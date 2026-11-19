---
type: "Feature"
title: "iOS Simulator pane"
description: "Public-beta pane where Claude builds, launches and drives apps in the iOS Simulator, with device consent, session device handling and iPhone Duo support."
resource: "https://code.claude.com/docs/en/desktop-ios-simulator"
tags: [desktop, ios-simulator, beta, xcode, macos]
kind: "ui"
maturity: "beta"
since: ""
surfaces: [desktop]
requires: "macOS, Claude Desktop v1.24012.0+, Xcode with iOS platform; Pro, Max, Ultra, Team or Enterprise (not HIPAA Enterprise, not third-party providers); iPhone Duo needs Desktop v4.29.0+ and Xcode 27.1+"
identifiers:
  - "disableMobileSimulatorTools"
  - "requireCoworkFullVmSandbox"
  - "xcode-select"
  - "xcodebuild -downloadPlatform iOS"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop-ios-simulator"
    resource: "https://code.claude.com/docs/en/desktop-ios-simulator"
    title: "Test iOS apps in the simulator"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The pane streams the iOS Simulator next to the conversation. When Claude builds, installs, launches or checks an app in a simulator the pane opens by itself; no command or setting is needed. It drives the simulator directly, so it does not need computer use or the macOS Accessibility and Screen Recording permissions. From the CLI, Claude reaches the simulator through computer use instead.

# How to use it

- Ask Claude to build/run/verify the app; name a device ("run it on the iPhone SE simulator") to target it. Open manually from the title bar or side panel; **Attach simulator**, **Detach simulator**, device menu (booting a shut-down device).
- You can tap, swipe, press hardware buttons (Cmd+Shift+H home, Cmd+L lock, Cmd+Up/Down volume), rotate (Cmd+Right Arrow), screenshot (Cmd+S) or record (Cmd+R) to your Desktop. A **Claude is using this device** badge shows while Claude drives.
- Xcode: pane uses the install `xcode-select` points at (change with `sudo xcode-select -s <path>` and restart Desktop; 26.x or 27 recommended). Missing runtime: `xcodebuild -downloadPlatform iOS`.
- Device handling: with no named device Claude reuses a running one, even from another parallel session; name different devices to isolate. Desktop shuts down simulators it booted on quit, on archiving the session, or 10 minutes after detaching; devices you booted yourself are never shut down automatically.
- iPhone Duo: fold Closed, Half open, Open, or ask for a hinge angle 1 to 179 degrees; Claude may offer to export Xcode agent skills to your personal skills folder.

# Limits and defaults

- Local sessions only (not cloud or SSH); simulated devices only, no physical iPhone or iPad.
- First use per device requires consent (once per device); screenshots go to Anthropic under normal retention, so avoid real accounts. Opening a URL, building (`xcodebuild`), and installing/launching follow the session permission mode even after consent.
- Turn off: desktop settings, or org keys `disableMobileSimulatorTools` (pane remains for your own taps) or `requireCoworkFullVmSandbox` (disables pane and tools entirely).
