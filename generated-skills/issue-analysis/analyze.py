#!/usr/bin/env python3
"""
GitHub Issue Analysis Script
Reads dat/github-issues-export.json and generates insights.
"""

import json
import sys
from pathlib import Path

def load_data(filepath='docs/issues/github-issues-export.json'):
    """Load exported issue data."""
    with open(filepath) as f:
        return json.load(f)

def milestone_progress(issues):
    """Calculate progress by milestone."""
    milestones = {}
    for i in issues:
        m = i['milestone'] or 'No Milestone'
        if m not in milestones:
            milestones[m] = {'open': 0, 'closed': 0}
        if i['state'] == 'OPEN':
            milestones[m]['open'] += 1
        else:
            milestones[m]['closed'] += 1
    return milestones

def board_status(issues):
    """Count issues by board status."""
    statuses = {}
    for i in issues:
        s = i['project_status'] or 'Not on board'
        statuses[s] = statuses.get(s, 0) + 1
    return statuses

def get_by_status(issues, status):
    """Get issues with specific board status."""
    return [i for i in issues if i['project_status'] == status]

def print_report(data):
    """Print full analysis report."""
    issues = data['issues']

    # Milestone Progress
    print("=" * 60)
    print("MILESTONE PROGRESS")
    print("=" * 60)
    for m, counts in sorted(milestone_progress(issues).items()):
        total = counts['open'] + counts['closed']
        pct = (counts['closed'] / total * 100) if total > 0 else 0
        bar = '█' * int(pct / 5) + '░' * (20 - int(pct / 5))
        print(f"{m[:40]:<40} {counts['closed']:>2}/{total:<2} {bar} {pct:.0f}%")

    # Board Status
    print("\n" + "=" * 60)
    print("BOARD STATUS")
    print("=" * 60)
    for s, count in sorted(board_status(issues).items(), key=lambda x: -x[1]):
        bar = '█' * min(count, 40)
        print(f"{s:<15} {count:>3} {bar}")

    # Blocked
    print("\n" + "=" * 60)
    print("BLOCKED (Need Attention)")
    print("=" * 60)
    blocked = get_by_status(issues, 'Blocked')
    if blocked:
        for i in blocked:
            print(f"  #{i['number']:<3} {i['title'][:50]}")
    else:
        print("  None")

    # In Progress
    print("\n" + "=" * 60)
    print("IN PROGRESS (Active Work)")
    print("=" * 60)
    for i in get_by_status(issues, 'In Progress'):
        print(f"  #{i['number']:<3} {i['title'][:50]}")

    # Ready
    print("\n" + "=" * 60)
    print("READY (Next Up)")
    print("=" * 60)
    ready = get_by_status(issues, 'Ready')
    if ready:
        for i in ready:
            print(f"  #{i['number']:<3} {i['title'][:50]}")
    else:
        print("  None")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total Issues: {data['summary']['total']}")
    print(f"Open: {data['summary']['open']} | Closed: {data['summary']['closed']}")
    print(f"Completion: {data['summary']['closed'] / data['summary']['total'] * 100:.0f}%")

if __name__ == '__main__':
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'dat/github-issues-export.json'
    data = load_data(filepath)
    print_report(data)
