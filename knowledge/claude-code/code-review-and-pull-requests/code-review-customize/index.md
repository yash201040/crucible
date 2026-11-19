# code-review-and-pull-requests/code-review-customize

* [REVIEW.md and CLAUDE.md for Code Review](review-md-and-claude-md.md) - Commit REVIEW.md and CLAUDE.md files to tune what Code Review flags: severity calibration, nit caps, skipped paths, extra checks, subdirectory files.
* [Which branch REVIEW.md is read from](review-md-branch-protection.md) - Code Review reads REVIEW.md from the base or default branch, never the PR's changes, and honors severity cuts and exclusions only from a protected branch.
* [Include files and skills in REVIEW.md](review-md-includes-and-skills.md) - A line of just @filename in the root REVIEW.md pulls in files beside it or a .claude/skills SKILL.md, subject to limits of eight files and 150,000 bytes.
