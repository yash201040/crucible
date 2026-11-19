# mods/plugins-mods-test

* [Check results with expect](check-result-with-expect.md) - The kit's expect has its own matcher set; .not, .resolves and .rejects work; a failing expect inside a plain stub makes the test fail.
* [What each stub returns](look-up-stub-returns.md) - Table of the stub shape to register for each common mods API call or event, and which calls the kit answers itself.
* [Mod test: where to go next](next-steps.md) - Pointers from the mod test page to troubleshooting and the mods reference.
* [Stubs: the test's $ and on](stub-claude-code-answers.md) - A test function receives $ (acts as Claude Code, fires events) and on (registers stubs that answer mods API calls); mock helpers cover clock, store, env, session.
* [Test a drawing with ui.mount](test-a-drawing.md) - $.ui.mount draws a render site through the mod's ui.render hook and returns a handle with press, input, select, find, keepsBeneath and unmount.
* [Test a policy mod](test-a-policy-mod.md) - tier() sets the load tier of the mod under test and test options plugins adds inline mods, to check a prependPlugins policy admits or refuses another mod.
* [Test a timer with a mock clock](test-a-timer.md) - mock.clock(on) gives a clock the test controls (advance, set, now, settle, sleep) so timer behavior is checked without waiting.
* [Test a drawing after /clear](test-drawing-after-clear.md) - Each test starts with $.state at defaults as /clear leaves them; fire classic.SessionStart with source clear to test reload of saved values.
* [Test kit rules](test-kit-rules.md) - Rules for stubs and events in the mod test kit: register before first $ call, session.start does not run itself, ui.render and turn.step stubs.
* [Write and run a mod test](write-a-mod-test.md) - claude plugin test runs *.test.ts files that fire events through a mod's hooks with no session, sign-in or network.
