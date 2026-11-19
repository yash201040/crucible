# mods/plugins-mods-interface

* [Backdrop and theme ($.theme.set, $.theme.clear)](backdrop-theme-set-clear.md) - $.theme.set sets a backdrop and colors for the Desktop or mobile app; $.theme.clear removes them; replaces the removed $.ui.backdrop.
* [Worked example: a pane with tabs and a counter](build-a-pane-with-tabs.md) - Builds a /hello-tabs mod whose pane has two tabs and a persisted counter, showing the render cycle of callback, state change and invalidate.
* [Element tree: elements and where they draw](build-a-tree-from-elements.md) - A ui.render hook returns an element tree built from $.ui.resolve(e); table of main elements, props and which apps draw them.
* [Change what Claude Code already draws (render sites)](change-what-claude-code-draws.md) - Claude Code's own messages, tool rows, spinner and notices are render sites a mod can restyle, replace or leave alone.
* [User collapse of the band above the prompt](collapse-the-band.md) - The user can collapse the band to one dim row; the mod cannot expand it and nothing in it can be pressed while collapsed.
* [Change the Desktop app colors with a mod](desktop-colors-mod.md) - Ask Claude or write a colors mod using makeColors and $.theme.set to recolor the Desktop Code tab; fix and remove steps.
* [Draw a grid of colored cells (Raster and $.ui.blit)](draw-grid-of-colored-cells.md) - Raster packs cells as base64 (code point, color, background) for terminal heat maps; $.ui.blit repaints one Raster without re-rendering.
* [Drawing in the VS Code extension](draw-in-vscode-extension.md) - How mod drawing behaves in the VS Code chat panel: versions, pane docking, focus rules, labels and text limits.
* [Keep state: variable, $.state and $.store](keep-state-store-and-state.md) - Three places a mod keeps values with different lifetimes, and the atom/read/update helpers with their validation rules.
* [Keyboard focus, keys and hotkeys in panes and band](keyboard-focus-and-hotkeys.md) - How a pane gets focus, what each key does while focused, hotkey and autoFocus props, and the Ctrl+X chords.
* [Open and close a pane ($.ui.open fields)](open-pane-ui-open.md) - $.ui.open fields, the true-only flags, immediate commands and when a mod-initiated pane waits for a wider terminal.
* [Pick where to draw: pane and band above the prompt](pick-where-to-draw-pane-band.md) - A ui.render hook picks a render site by component matcher; Pane and AbovePrompt are empty until a mod fills them.
* [Place a row in the transcript ($.ui.place)](place-a-row-in-transcript.md) - $.ui.place adds a mod-drawn row at the end of the transcript, drawn at the Placed render site, that Claude does not see.
* [Redrawing a site: invalidate, timer and throttling](redraw-a-site.md) - ui.render reruns on prop or width changes; mods call $.ui.invalidate or $.clock.every for data changes, with throttled coalesced redraws.
* [Callbacks and keys for Button, Input, Select](respond-to-presses-and-typing.md) - Control callbacks, which controls need a key, and how ui.press, ui.input and ui.select let other mods observe them.
* [Reload saved state after /clear and share the store across sessions](state-after-clear-and-multi-session.md) - $.state resets on /clear, /resume and /branch, so reload from $.store via classic.SessionStart; sessions share one non-atomic $.store.
* [Typed input with a list of rows (notes pane)](typed-input-and-lists.md) - Pattern for an Input plus a per-item row list with delete buttons, saved to $.store, with a key per row button.
