# Devlog Template: Development Log

Use this template when documenting NARRATIVE of work. Devlogs are **historical**—they capture lessons learned and context for future reference.

---

## Template

```markdown
# {Title: What This Devlog Is About}

**Date**: {YYYY-MM-DD}
**Author**: {name}
**Topic**: {Brief description of the subject matter}

---

## TL;DR

{2-3 sentences summarizing the key insight or outcome. Someone should understand the main point without reading further.}

---

## The Problem

### What Happened

{Describe the situation that led to this work:}
- What were you trying to do?
- What challenge did you face?
- Why did it matter?

### Why This Is Important

{Explain why this problem matters:}
- Impact on the project
- Impact on future work
- What was at stake

---

## The Solution

### What We Did

{Describe the approach taken:}

**Before**:
```
{How things were before}
```

**After**:
```
{How things are now}
```

### How We Did It

{Walk through the key steps:}

1. **{Step 1}**: {Description}
2. **{Step 2}**: {Description}
3. **{Step 3}**: {Description}

### Why This Works

{Explain the reasoning:}
- Why this approach over alternatives
- Key insights that made it work
- What makes it sustainable

---

## Key Insights

### Insight 1: {Title}

{Explanation of something learned that others can apply}

### Insight 2: {Title}

{Another transferable insight}

### Insight 3: {Title}

{Another insight}

---

## Lessons Learned

### What Worked

- {Thing that went well}
- {Another success}

### What Didn't Work

- {Thing that failed or was harder than expected}
- {Why it didn't work}

### What We'd Do Differently

- {Hindsight improvement}
- {Another improvement}

---

## Patterns Established

### Pattern 1: {Pattern Name}

**When to use**: {Situation}

**How it works**:
```
{Description or example}
```

**Benefits**:
- {Benefit 1}
- {Benefit 2}

### Pattern 2: {Pattern Name}

{Same structure}

---

## Impact

### Immediate Effects

- {What changed right away}
- {What's now possible}

### Future Implications

- {How this affects future work}
- {New capabilities unlocked}

---

## Open Questions

{Questions that remain unanswered:}

1. {Question}
2. {Question}

---

## Related Work

- [ADR-{NNN}: {Title}](../adr/{NNN}-{feature}.md) - Decision that led to this
- [Design: {Title}](../design/{feature}.md) - Architecture context
- [Plan: {Title}](../plan/{feature}-implementation.md) - Implementation details
- [GitHub Issue #{N}]({url}) - Tracking

---

## Meta-Reflection

{Optional: What this devlog itself represents or teaches}

---

**Last Updated**: {YYYY-MM-DD} by {name}
```

---

## Key Principles

1. **Narrative**: Tell the story, not just facts
2. **Transferable insights**: Lessons others can apply
3. **Honest about failures**: What didn't work is valuable
4. **Pattern documentation**: Capture reusable patterns
5. **Cross-referenced**: Link to related context docs

## Naming Convention

```
docs/devlog/YYYY-MM-DD-kebab-case-topic.md
```

Examples:
- `2025-12-03-information-architecture-for-agentic-workflows.md`
- `2025-12-05-agent-registry-and-naming-conventions.md`
- `2025-11-15-auth-migration-lessons.md`

## When to Write a Devlog

- **Completed significant work**: Capture lessons while fresh
- **Solved a hard problem**: Document for future reference
- **Established new pattern**: Share with team/future self
- **Failed and learned**: Failures are valuable knowledge
- **Made architectural change**: Explain the journey

## Devlog vs Other Doc Types

| Doc Type | Purpose | Updates |
|----------|---------|---------|
| **ADR** | WHY decision made | Never (immutable) |
| **Design** | HOW system works | When system changes |
| **Spec** | WHAT requirements are | When requirements change |
| **Plan** | STEPS to build | As work progresses |
| **Devlog** | NARRATIVE of work | Written once, never updated |

Devlogs are **write-once**. If you have new insights, write a new devlog that references the old one.

## Writing Good TL;DRs

**Bad**: "This devlog is about documentation."

**Good**: "We split a 1000+ line doc into four semantic types (ADR/Design/Spec/Plan) to enable AI agents to automatically read only the context they need, reducing token usage by 50-80%."

The TL;DR should make someone want to read more OR give them enough to not need to.
