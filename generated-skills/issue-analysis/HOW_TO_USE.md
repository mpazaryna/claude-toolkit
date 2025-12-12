# How to Use This Skill

Hey Claude—I just added the "issue-analysis" skill. Can you analyze my GitHub issues and show me the project status?

## Example Invocations

**Quick status check:**
"How's the project going?"

**Milestone progress:**
"What's our milestone progress? Are we on track for v1.0?"

**Find blockers:**
"Show me all blocked issues that need attention"

**Full analysis:**
"Analyze our GitHub backlog and give me insights on project health"

**Export data:**
"Export all issues to JSON for offline analysis"

## What to Provide

- A GitHub repository with issues (uses `gh` CLI)
- A GitHub project board (optional, for board status tracking)
- The repo/owner configured in the export script

## What You'll Get

- **Milestone Progress**: Visual progress bars showing % complete per milestone
- **Board Status**: Counts by column (Todo, In Progress, Done, Blocked)
- **Blocked Items**: List of issues that need unblocking
- **In Progress**: Currently active work items
- **Ready Queue**: Next items ready to be picked up
- **Summary Stats**: Total issues, open/closed ratio, completion %

## Prerequisites

Ensure the `gh` CLI is installed and authenticated:
```bash
gh auth status
```

## Output Files

- `docs/issues/github-issues-export.json` - Raw exported data
- Console output with formatted analysis report
