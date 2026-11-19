# agents-and-parallel-work/worktrees

* [Worktree cleanup on exit](clean-up-worktrees.md) - What happens to a worktree when an interactive session exits, and why -p runs leave worktrees behind. **[high]**
* [Isolating subagents with worktrees](isolate-subagents-worktrees.md) - isolation: worktree gives a subagent its own temporary worktree; cleanup sweep by cleanupPeriodDays, locks and manual removal. **[high]**
* [Managing worktrees manually with git](manage-worktrees-manually.md) - Create, list and remove worktrees with git worktree commands when you need a specific branch or an outside location.
* [Non-git version control via WorktreeCreate hooks](non-git-vcs-hooks.md) - WorktreeCreate and WorktreeRemove hooks replace git worktree logic for SVN, Perforce, Mercurial and enable /batch outside git. **[high]**
* [Refusing to use a worktree and resume messages](refusing-to-use-worktree.md) - The Refusing to use <path> as an isolation worktree error, its recoveries, and resume messages in interactive, -p and SDK runs including startup_failure_reason. **[high]**
* [Resuming a worktree session](resume-worktree-session.md) - Resumed sessions return to their worktree (interactive, -p --continue/--resume, SDK) after verification; launch-directory and fork rules. **[high]**
* [Starting Claude in a worktree](start-claude-in-worktree.md) - claude --worktree <name> creates an isolated git worktree and branch; also EnterWorktree, trust rules and the blockWritesOutsideWorkingDirectories interaction. **[high]**
* [What worktrees share with the main checkout](what-worktrees-share.md) - Shared .git, plugins, permission approvals and untracked skills/agents/commands; desktop-app configuration source.
* [Worktree base branch and PR checkout](worktree-base-branch-and-pr.md) - worktree.baseRef chooses fresh (default branch) or head; --worktree with a PR/MR number or URL branches from that change. **[high]**
* [Worktree creation errors and recoveries](worktree-creation-errors.md) - Error messages for symlinks, replaced objects, Git LFS filter drivers, partial clones, non-git directories and wrong-repository worktrees.
* [How Claude Code enforces worktree isolation](worktree-isolation-enforcement.md) - Four checks blocking edits, command directories, git redirects and unverifiable command shapes aimed at the main checkout. **[high]**
* [.worktreeinclude and reusing worktree names](worktreeinclude-and-reuse.md) - Copy gitignored files into new worktrees with .worktreeinclude; reopen vs reset rules when a name is reused; WorktreeCreate hook replaces it.
