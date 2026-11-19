# platforms-and-integrations/routines

* [Cloud scheduled tasks (routines)](cloud-scheduled-tasks-overview.md) - Saved prompt, repositories and connectors that run as cloud Claude Code sessions on a schedule, API call or GitHub event. **[high]**
* [API trigger and /fire endpoint](routine-api-trigger-fire.md) - Start a scheduled task by POSTing to its own /fire endpoint with a per-task bearer token and optional text context. **[high]**
* [GitHub trigger and PR filters](routine-github-trigger.md) - Start a fresh cloud session on pull request, release or issue events, with filters on PR fields. **[high]**
* [Permissions and artifacts during scheduled runs](routine-permissions-and-artifacts.md) - Cloud scheduled runs start in auto mode, may still pause for prompts, and may publish artifacts without asking under stated conditions. **[high]**
* [Scheduled task usage and hourly limits](routine-usage-limits.md) - Hourly run caps per account and per task for scheduled, Run now and API-fired runs, and behavior at subscription limits. **[high]**
* [/schedule command and schedule triggers](schedule-command-and-schedule-trigger.md) - Create, list, update and run cloud scheduled tasks from the CLI, with recurring cadence, custom cron and one-off runs. **[high]**
