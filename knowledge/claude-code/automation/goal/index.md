# automation/goal

* [Background work and goal check-ins](goal-background-checkins.md) - Evaluation is deferred while subagents or background commands run; timed check-ins with backoff and an idle-check-in cap. **[high]**
* [/goal completion condition](goal-command.md) - Set a completion condition; Claude keeps taking turns until an evaluator model judges it met or impossible. **[high]**
* [Goal behavior on turn errors](goal-errors.md) - Which failures clear a goal, which retry or pause it, and the v2.1.269 interactive notices. **[high]**
* [How /goal evaluation and cost work](goal-evaluation.md) - Verdicts of the evaluator model, the no-progress stop, and which model evaluates and bills. **[high]**
