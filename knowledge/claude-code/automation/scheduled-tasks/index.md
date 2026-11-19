# automation/scheduled-tasks

* [Compare scheduling options](compare-scheduling-options.md) - Cloud, Desktop and /loop scheduling differ in where they run, persistence, file access, permissions and minimum interval. **[high]**
* [Cron expression syntax](cron-expression-reference.md) - Standard 5-field cron syntax accepted by CronCreate, with examples and unsupported extensions.
* [Session scope and resume](cron-tools-and-management-note.md) - Scheduled tasks belong to the session; --resume and --continue restore unexpired ones. **[high]**
* [Cron tools and task management](cron-tools-and-management.md) - CronCreate, CronList and CronDelete tools for session-scoped scheduled tasks, with ID format and the 50-task cap. **[high]**
* [Disable session-scoped scheduling](disable-session-scheduling.md) - CLAUDE_CODE_DISABLE_CRON=1 turns off the scheduler, CronCreate and /loop. **[high]**
* [Jitter and run timing](jitter-and-timing.md) - Claude Code offsets scheduled run times: recurring tasks run late by up to half the gap (max 30 min), one-shots on :00/:30 up to 90 s early. **[high]**
* [The /loop command](loop-command-forms.md) - The /loop bundled skill reruns a prompt on a fixed interval, a Claude-chosen interval, or a built-in maintenance prompt. **[high]**
* [loop.md default prompt file](loop-md-default-prompt.md) - A loop.md file replaces the built-in maintenance prompt used by a bare /loop.
* [One-time reminders](one-time-reminders.md) - Natural-language one-shot tasks that fire once at a pinned minute and delete themselves.
* [Session-scoped scheduling limitations](scheduling-limitations.md) - Tasks fire only while Claude Code runs and is idle, with no catch-up, specific resume behavior and worktree caveats. **[high]**
* [Seven-day expiry of recurring tasks](seven-day-expiry.md) - Recurring session-scoped tasks fire a final time and delete themselves 7 days after creation. **[high]**
* [Stopping and detaching loops](stop-a-loop.md) - How self-paced and fixed-interval loops are stopped, and how to detach from a background session without stopping one. **[high]**
