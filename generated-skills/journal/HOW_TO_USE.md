# How to Use the Internal Communications Skill

## Quick Start

Ask Claude to write internal communications in your company's format:

```
"Write a 22A update about the authentication project"
"Create a devlog for this week"
"Draft a condensed 22B for leadership"
```

## What This Skill Does

The Internal Communications skill helps you write professional, well-formatted communications following your company's specific conventions. Claude will:

1. Identify the communication type from your request
2. Load the appropriate template from the `examples/` directory
3. Follow the specific formatting, tone, and structure guidelines
4. Generate a complete, ready-to-send communication

## Supported Formats

### 1. Form 22A - Full Team Updates

**When to use:** Weekly or bi-weekly team updates, detailed project status

**Format:** Progress → Plans → Problems (3P format)

**Example request:**
```
"Write a 22A update for the API modernization project"
```

**Claude will generate:**
```markdown
# API Modernization - Week of Nov 14

## Progress
- Completed authentication refactor
- Migrated 15 endpoints to new framework
- Added comprehensive error handling

## Plans
- Complete remaining 10 endpoints by Friday
- Begin load testing next week
- Documentation update sprint

## Problems
- Performance regression in user lookup (investigating)
- Need decision on rate limiting strategy
- Blocked on database migration approval
```

### 2. Form 22B - Condensed Updates

**When to use:** Quick updates, leadership summaries, standup notes

**Format:** Shorter 3P format with bullet points

**Example request:**
```
"Create a 22B for today's standup"
```

**Claude will generate:**
```markdown
## Progress
- Merged authentication PR
- Fixed 3 bugs in payment flow

## Plans
- Start user profile refactor
- Review team's PRs

## Problems
- None currently
```

### 3. Devlog - Developer Logs

**When to use:** Daily or weekly progress logs, learning documentation, technical notes

**Format:** Date-stamped entries with context, work completed, and learnings

**Example request:**
```
"Write a devlog entry for today's work on the database migration"
```

**Claude will generate:**
```markdown
## 2024-11-14 - Database Migration Sprint

### Context
Working on migrating PostgreSQL to v15 for performance improvements.

### Work Completed
- Upgraded dev environment successfully
- Tested migration scripts on staging
- Documented rollback procedure
- Identified 2 queries needing optimization

### Learnings
- New JSONB operators significantly faster
- Parallel index creation reduces downtime
- Need better monitoring for query performance

### Next Steps
- Production migration scheduled for weekend
- Monitor query performance post-migration
- Update team documentation
```

## Usage Examples

### Example 1: Project Status Update

```
User: "Write a 22A update for the mobile app redesign project. We completed the home screen, started the settings page, and are blocked on design approval for the profile page."

Claude: I'll create a Form 22A update following your company's format.

[Loads examples/form-22a.md template]
[Applies formatting and tone guidelines]

# Mobile App Redesign - Week of Nov 14

## Progress ✅
- ✅ Completed home screen implementation
  - New card-based layout
  - Smooth animations and transitions
  - Accessibility features added
- ✅ User testing completed with positive feedback
  - 4.5/5 average satisfaction score
  - No critical issues identified

## Plans 📋
- 🚀 Complete settings page by EOW
  - Profile preferences
  - Notification controls
  - Privacy settings
- 🎨 Begin profile page implementation (pending approval)
- 📊 Prepare demo for stakeholder review

## Problems ⚠️
- ⏸️ Blocked on design approval for profile page
  - Waiting on design team feedback
  - May impact timeline by 2-3 days
- 🤔 Need decision: Dark mode implementation timeline
  - Additional 1 week if included in this sprint
  - Can defer to next sprint if needed
```

### Example 2: Developer Log

```
User: "Create a devlog about debugging the memory leak I found today in the image processing module"

Claude: I'll create a devlog entry documenting your debugging work.

[Loads examples/devlog.md template]

## 2024-11-14 - Memory Leak Investigation

### Context
Users reported app crashes after processing multiple images. Memory profiler showed continuous growth in heap allocation.

### Investigation Process
1. **Profiling** (1 hour)
   - Used Instruments to identify leak
   - Found strong reference cycle in ImageProcessor

2. **Root Cause** (30 minutes)
   - Closure capturing self strongly
   - Background task not being deallocated

3. **Solution** (1 hour)
   - Added [weak self] to closure
   - Implemented proper cleanup in deinit
   - Added unit test to catch similar issues

### Code Changes
- Modified: ImageProcessor.swift
- Added: ImageProcessorTests.swift
- Memory usage: 200MB → 45MB (77% reduction)

### Learnings
- Always use weak self in async closures
- Memory profiling should be part of PR review
- Unit tests can catch memory leaks
- Consider adding automated memory regression tests

### Testing Done
- Processed 100 images sequentially: No leaks
- Background processing: Memory stable
- App lifecycle transitions: Proper cleanup

### Next Steps
- Deploy fix to TestFlight
- Monitor crash reports
- Add memory regression test to CI
- Document pattern in team guidelines
```

### Example 3: Incident Report

```
User: "Write an incident report about the API outage this morning. It lasted 15 minutes, affected 30% of users, caused by a database connection pool exhaustion."

Claude: I'll create an incident report using the internal comms format.

## Incident Report - API Outage (2024-11-14)

### Summary
API experienced partial outage from 9:15 AM - 9:30 AM EST, affecting approximately 30% of users due to database connection pool exhaustion.

### Timeline
- **9:15 AM** - Alerts triggered for elevated error rates
- **9:17 AM** - On-call engineer investigates
- **9:20 AM** - Root cause identified: Connection pool exhausted
- **9:25 AM** - Emergency fix deployed (increased pool size)
- **9:30 AM** - Service fully recovered
- **9:45 AM** - Monitoring confirms stability

### Impact
- **Users Affected:** ~30% (estimated 5,000 users)
- **Duration:** 15 minutes
- **Services Impacted:** User authentication, API calls
- **Data Loss:** None
- **Revenue Impact:** Minimal (off-peak hours)

### Root Cause
Database connection pool configuration was too small for current traffic patterns. Recent growth in API usage (40% increase over 2 weeks) exceeded pool capacity during peak hours.

### Resolution
- **Immediate:** Increased connection pool from 50 to 100 connections
- **Short-term:** Added monitoring for pool utilization
- **Long-term:** Implement auto-scaling connection pools

### Action Items
- [ ] Review all connection pool configurations (Owner: DevOps, Due: Nov 16)
- [ ] Add proactive alerts for pool utilization >70% (Owner: SRE, Due: Nov 17)
- [ ] Implement connection pool auto-scaling (Owner: Platform, Due: Nov 30)
- [ ] Update runbook with connection pool troubleshooting (Owner: On-call, Due: Nov 15)
- [ ] Post-mortem meeting scheduled for Nov 15, 2:00 PM

### Lessons Learned
- Need better monitoring for resource utilization
- Traffic growth patterns should trigger infra reviews
- Emergency response was effective (15 min resolution)
- Documentation helped quick diagnosis
```

## How It Works

### 1. Format Detection

Claude automatically detects the communication type from your request:

| You say... | Claude loads... |
|------------|----------------|
| "22A update" | examples/form-22a.md |
| "devlog" | examples/devlog.md |
| "22B" or "condensed update" | examples/form-22b.md |
| "status report" | Best matching format |

### 2. Template Loading

Claude reads the appropriate template file which contains:
- Structure guidelines
- Tone and voice requirements
- Formatting conventions
- Example content

### 3. Content Generation

Claude applies the template rules to your specific context:
- Uses proper headings and formatting
- Follows tone guidelines (professional, concise, clear)
- Includes required sections
- Adapts examples to your situation

## Best Practices

### Provide Clear Context

**Good:**
```
"Write a 22A for the payment system upgrade. We finished stripe integration, starting PayPal next week, and need legal approval for crypto payments."
```

**Better:**
```
"Write a 22A for the payment system upgrade project.

Progress: Completed Stripe integration, tested with 100 transactions
Plans: Start PayPal integration next sprint, estimated 2 weeks
Problems: Blocked on legal review for cryptocurrency payment option
```

### Specify Your Audience

```
"Write a devlog about the database optimization (technical audience)"
"Create a 22B for leadership (executive summary style)"
"Draft a project update for stakeholders (non-technical)"
```

### Include Relevant Details

- Dates and timelines
- Metrics and numbers
- Blockers and dependencies
- Team members involved
- Links to related docs/tickets

## Customization

### Add Your Own Formats

Create new format files in the `examples/` directory:

1. Create `examples/weekly-report.md`
2. Define structure and guidelines
3. Update `SKILL.md` to reference it

### Update Existing Formats

Edit the template files to match your company's evolving conventions:

```bash
# Edit the 22A format
vim generated-skills/internal-comms/examples/form-22a.md
```

## Common Questions

**Q: Can Claude post these for me?**
A: No, Claude generates the content. You copy and post to Slack, email, etc.

**Q: What if my company uses different formats?**
A: Edit the example files or add new ones to match your conventions.

**Q: Can it generate from code changes?**
A: Yes! "Write a 22A based on my git commits this week"

**Q: Does it work for other languages?**
A: Yes, ask for specific language: "Write a 22A in Spanish"

## Tips for Great Internal Comms

1. **Be specific with numbers**
   - ✅ "Completed 15 of 20 endpoints"
   - ❌ "Made good progress"

2. **Highlight blockers clearly**
   - ✅ "Blocked on design approval, impacts timeline by 2 days"
   - ❌ "Waiting on design"

3. **Make plans actionable**
   - ✅ "Complete user auth by Friday, Nov 17"
   - ❌ "Work on auth"

4. **Use consistent formatting**
   - Follow the template structure
   - Use emojis if your company culture supports it
   - Keep tone professional but friendly

## Related Skills

- **commit-helper** - Generate commit messages for work tracking
- **code-reviewer** - Review code before reporting completion

---

Generated by Claude Code Skills Factory
