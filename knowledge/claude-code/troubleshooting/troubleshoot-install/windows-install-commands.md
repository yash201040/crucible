---
type: "Reference"
title: "Install commands and error lookup by shell"
description: "Which installer command belongs to which shell, plus the page's error-to-fix lookup for common install messages."
resource: "https://code.claude.com/docs/en/troubleshoot-install"
tags: [install, windows, powershell, cmd, reference]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "curl -fsSL https://claude.ai/install.sh | bash"
  - "irm https://claude.ai/install.ps1 | iex"
  - "curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd"
  - "claude doctor"
  - "/doctor"
  - "/feedback"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "troubleshoot-install"
    resource: "https://code.claude.com/docs/en/troubleshoot-install"
    title: "Troubleshoot installation and login"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A lookup of the correct installer command per shell and the wrong-shell errors that appear when the wrong one is used.

# How to use it

| Shell | Installer command |
| :- | :- |
| macOS/Linux/WSL | `curl -fsSL https://claude.ai/install.sh \| bash` |
| Windows PowerShell | `irm https://claude.ai/install.ps1 \| iex` |
| Windows CMD | `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` |

| Error text | Meaning |
| :- | :- |
| `'irm' is not recognized` | In CMD, not PowerShell |
| `The token '&&' is not a valid statement separator` | CMD command run in PowerShell |
| `A parameter cannot be found that matches parameter name 'fsSL'` | macOS/Linux curl command in PowerShell (curl is an alias) |
| `'bash' is not recognized as the name of a cmdlet` | macOS/Linux installer on Windows |
| Command prints script text | Ran only the download half (missing `\| iex`, or missing `-o`) |
| `The process cannot access the file ... being used by another process` | Delete `%USERPROFILE%\.claude\downloads` and retry |

# Notes

After any install, open a new terminal and run `claude --version` (prints a version such as `2.1.211 (Claude Code)`). Further help: `claude doctor`, `/feedback`, GitHub issues, or Anthropic support via the Get help entry.
