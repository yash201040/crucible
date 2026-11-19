---
type: "Guide"
title: "Write a policy mod with plugin.register"
description: "A policy mod can refuse or trim other mods through the plugin.register event, audit tool calls and fs.write, and fail closed with a catch handler."
resource: "https://code.claude.com/docs/en/plugins/mods/admin"
tags: [mods, policy-mod, plugin-register, audit, hooks]
kind: "hook"
maturity: "unlabelled"
since: "2.1.326"
surfaces: [cli]
requires: "mod in prependPlugins; v2.1.326 or later to leave out only the hooks module"
identifiers:
  - "plugin.register"
  - "tool.call"
  - "fs.write"
  - "ui.focus"
  - "e.tier"
  - "e.uses.calls"
  - "e.provides"
  - "provides.modules"
  - "refuse"
  - "deny"
  - "next.called"
  - "next.origin.plugin"
  - "$.ui.log"
  - "/reload-plugins"
  - "acme-guard/hooks/register.js"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-admin"
    resource: "https://code.claude.com/docs/en/plugins/mods/admin"
    title: "Manage mods for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

To keep all user mods out, use `allowManagedModsOnly`; write a policy mod to allow some user mods and refuse others, or to record what mods do. Each time another mod is about to load, a mod in `prependPlugins` receives the `plugin.register` event with the `claude plugin validate` list. It can also handle any mods API call by name (method without `$.`, so a hook on `fs.write` sees every `$.fs.write` call) to record or refuse it for every other mod. On v2.1.323+, a `ui.focus` hook needs a wider matcher to receive other mods' `$.ui.focus` calls.

# How to use it

Event fields: `e.tier` (`prepend`, `user`, `append`, `builtin`; any installed mod is `user`), `e.uses.calls` (e.g. `process.run`), `e.provides` (plugin parts by kind such as `modules`).

```javascript
export function register(on) {
  on('plugin.register', async ($, e, next) => {
    const blocked = e.uses.calls.filter((c) => ['process.run','process.spawn'].includes(c))
    if (e.tier === 'user' && blocked.length > 0) {
      if (e.provides) return next({ ...e, provides: { ...e.provides, modules: [] } })
      return { refuse: 'Acme policy: mods may not call ' + blocked.join(', ') }
    }
    return next(e)
  })
  on('tool.call', async ($, e, next) => { $.ui.log('audit tool.call ' + e.tool, { to: 'debug' }); return next(e) })
  on('fs.write', async ($, e, next) => { $.ui.log('audit fs.write by ' + next.origin.plugin + ' ' + JSON.stringify(e.path), { to: 'debug' }); return next(e) })
}
```

To block one call without refusing the mod, return `{ deny: 'reason' }` from a hook on that call's name after checking who made it. Send audit lines elsewhere with `$.http.fetch`.

# Limits and defaults

- On v2.1.326+, emptying `provides.modules` loads the rest of the plugin; `{ refuse }` keeps the whole plugin out, including MCP servers and `hooks/hooks.json`. Before v2.1.326 refuse leaves out only the hooks module and the debug line reads `refused by acme-guard:`; newer line: `hooks module left out by acme-guard`.
- A hook that throws or exceeds its time limit is skipped, so the check fails open. Fail closed with `.catch`: `on('plugin.register', checkMod).catch(...)` passing non-`user` tiers to `next(e)`, trimming modules if `!next.called`, else refusing. The handler does not help for a time-limit overrun.
- A session can run without the policy mod: after the hooks worker crashes three times, Claude Code unloads every non-built-in mod until `/reload-plugins` or a new session; `--safe-mode` also runs without installed mods.
