---
name: issue-analysis
description: Analyze GitHub issues for project health, milestone progress, and backlog insights. Use when asked about project status, issue analytics, or backlog health.
---

# GitHub Issue Analysis

Analyze GitHub issues to understand project health, milestone progress, and identify blockers.

## When to Use

- "How's the project going?"
- "What's our milestone progress?"
- "Show me blocked issues"
- "Analyze our backlog"
- "Export issues to JSON"

## Step 1: Export Data

Export all issues with milestone and project board status:

```bash
cat <<'SCRIPT' | python3 > docs/issues/github-issues-export.json
import json
import subprocess
from datetime import datetime

# Get issues
issues_json = subprocess.run(
    ['gh', 'issue', 'list', '--repo', 'j-bouchard/resin-platform', '--state', 'all', '--limit', '200',
     '--json', 'number,title,state,milestone,labels,createdAt,closedAt'],
    capture_output=True, text=True
).stdout
issues = json.loads(issues_json)

# Get project items (board status)
project_json = subprocess.run(
    ['gh', 'project', 'item-list', '1', '--owner', 'j-bouchard', '--limit', '200', '--format', 'json'],
    capture_output=True, text=True
).stdout
project_items = json.loads(project_json)

# Build project status lookup
project_status = {item['content']['number']: item['status'] for item in project_items['items'] if item.get('content')}

# Combine
result = {
    "exported_at": datetime.now().isoformat(),
    "repo": "j-bouchard/resin-platform",
    "project": "V4 Development",
    "summary": {
        "total": len(issues),
        "open": len([i for i in issues if i['state'] == 'OPEN']),
        "closed": len([i for i in issues if i['state'] == 'CLOSED'])
    },
    "issues": []
}

for issue in sorted(issues, key=lambda x: x['number']):
    result["issues"].append({
        'number': issue['number'],
        'title': issue['title'],
        'state': issue['state'],
        'milestone': issue['milestone']['title'] if issue.get('milestone') else None,
        'project_status': project_status.get(issue['number']),
        'labels': [l['name'] for l in issue.get('labels', [])],
        'created_at': issue.get('createdAt'),
        'closed_at': issue.get('closedAt')
    })

print(json.dumps(result, indent=2))
SCRIPT
```

## Step 2: Run Analysis

Read the exported data and generate insights:

```bash
cat <<'SCRIPT' | python3
import json

with open('docs/issues/github-issues-export.json') as f:
    data = json.load(f)

issues = data['issues']

# === MILESTONE PROGRESS ===
print("=" * 60)
print("MILESTONE PROGRESS")
print("=" * 60)
milestones = {}
for i in issues:
    m = i['milestone'] or 'No Milestone'
    if m not in milestones:
        milestones[m] = {'open': 0, 'closed': 0}
    if i['state'] == 'OPEN':
        milestones[m]['open'] += 1
    else:
        milestones[m]['closed'] += 1

for m, counts in sorted(milestones.items()):
    total = counts['open'] + counts['closed']
    pct = (counts['closed'] / total * 100) if total > 0 else 0
    bar = '█' * int(pct / 5) + '░' * (20 - int(pct / 5))
    print(f"{m[:40]:<40} {counts['closed']:>2}/{total:<2} {bar} {pct:.0f}%")

# === BOARD STATUS ===
print("\n" + "=" * 60)
print("BOARD STATUS")
print("=" * 60)
statuses = {}
for i in issues:
    s = i['project_status'] or 'Not on board'
    statuses[s] = statuses.get(s, 0) + 1

for s, count in sorted(statuses.items(), key=lambda x: -x[1]):
    bar = '█' * min(count, 40)
    print(f"{s:<15} {count:>3} {bar}")

# === BLOCKED ===
print("\n" + "=" * 60)
print("BLOCKED (Need Attention)")
print("=" * 60)
blocked = [i for i in issues if i['project_status'] == 'Blocked']
if blocked:
    for i in blocked:
        print(f"  #{i['number']:<3} {i['title'][:50]}")
else:
    print("  None")

# === IN PROGRESS ===
print("\n" + "=" * 60)
print("IN PROGRESS (Active Work)")
print("=" * 60)
in_progress = [i for i in issues if i['project_status'] == 'In Progress']
for i in in_progress:
    print(f"  #{i['number']:<3} {i['title'][:50]}")

# === READY ===
print("\n" + "=" * 60)
print("READY (Next Up)")
print("=" * 60)
ready = [i for i in issues if i['project_status'] == 'Ready']
if ready:
    for i in ready:
        print(f"  #{i['number']:<3} {i['title'][:50]}")
else:
    print("  None")

# === SUMMARY ===
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Total Issues: {data['summary']['total']}")
print(f"Open: {data['summary']['open']} | Closed: {data['summary']['closed']}")
print(f"Completion: {data['summary']['closed'] / data['summary']['total'] * 100:.0f}%")

SCRIPT
```

## Output Location

- **Export file**: `docs/issues/github-issues-export.json`
- **Report**: Printed to console (can be saved to `docs/issues/issue-analysis-report.md`)

## Available Analyses

| Analysis | Description |
|----------|-------------|
| Milestone progress | % complete per milestone |
| Board status | Todo/In Progress/Done/Blocked counts |
| Blocked items | Issues that need unblocking |
| In Progress | Active work items |
| Ready | Next items to pick up |

## Future Enhancements

- [ ] Velocity tracking (issues closed per week)
- [ ] Aging analysis (old open issues)
- [ ] Label breakdown
- [ ] Burndown chart data
- [ ] Compare snapshots over time
