---
name: dev-context
description: Context architecture skill for aligning work. Use when starting new features, making architectural decisions, or setting up implementation work. Generates interconnected ADR/Design/Spec/Plan scaffolding that agents can navigate and humans can enrich.
---

# Dev Context

Build context architecture for work. Not documentation—**context alignment**.

> When you start new work, align the WHY → HOW → WHAT → STEPS before coding.

## The Context Architecture

| Doc Type | Purpose | Lifecycle | Agent Reads For |
|----------|---------|-----------|-----------------|
| **ADR** | WHY decisions | Immutable | Understanding past choices |
| **Design** | HOW it works | Living | Building components |
| **Spec** | WHAT is required | Stable | Validation criteria |
| **Plan** | STEPS to build | Evolving | Task execution |
| **Devlog** | NARRATIVE | Historical | Learning patterns |

Each doc type is an **interface contract**:
- ADR: "I tell you WHY and never change"
- Design: "I tell you HOW it works today"
- Spec: "I tell you WHAT must be done"
- Plan: "I tell you STEPS to take"

## When to Use This Skill

**Starting new work**:
- "Set up context for the auth refactor"
- "Create context for the new sync feature"

**Making architectural decisions**:
- "Create ADR for choosing SwiftData over CoreData"
- "Document the caching strategy decision"

**Planning implementation**:
- "Set up the implementation plan for Phase 2"
- "Create spec for the API redesign"

**Capturing lessons**:
- "Write devlog for the completed migration"
- "Document what we learned from the spike"

## How to Use This Skill

1. **Identify context needs** from the request
2. **Load appropriate templates** from `references/templates/`
3. **Generate scaffolding** with intelligent placeholders
4. **Create cross-references** between all docs
5. **Return file paths** and next steps

## Context Generation Modes

### Mode 1: Full Context (New Feature)

**Trigger**: "Set up context for [feature]", "Create context for [work]"

**Generates**:
```
docs/
├── adr/NNN-feature-name.md
├── design/feature-name.md
├── spec/feature-name.md
└── plan/feature-name-implementation.md
```

**Process**:
1. Read `references/templates/adr.md` → Generate ADR
2. Read `references/templates/design.md` → Generate Design
3. Read `references/templates/spec.md` → Generate Spec
4. Read `references/templates/plan.md` → Generate Plan
5. Read `references/patterns.md` → Add cross-references
6. Return summary with file paths

### Mode 2: Decision Only (ADR)

**Trigger**: "Create ADR for [decision]", "Document decision about [choice]"

**Generates**:
```
docs/adr/NNN-decision-name.md
```

**Process**:
1. Find next ADR number (glob `docs/adr/*.md`)
2. Read `references/templates/adr.md`
3. Generate ADR with context from request
4. Link to related existing docs if applicable

### Mode 3: Implementation Setup (Plan + Spec)

**Trigger**: "Set up implementation for [work]", "Create plan for [feature]"

**Generates**:
```
docs/
├── spec/feature-name.md
└── plan/feature-name-implementation.md
```

**Process**:
1. Read `references/templates/spec.md` → Generate Spec
2. Read `references/templates/plan.md` → Generate Plan
3. Cross-reference between them
4. Link to existing ADR/Design if found

### Mode 4: Devlog (Capture Learning)

**Trigger**: "Write devlog for [work]", "Document lessons from [experience]"

**Generates**:
```
docs/devlog/YYYY-MM-DD-topic-slug.md
```

**Process**:
1. Read `references/templates/devlog.md`
2. Generate devlog with narrative structure
3. Link to related ADR/Design/Plan/Spec

## Quick Reference

| Request | Mode | Templates |
|---------|------|-----------|
| "Set up context for X" | Full | All 4 templates |
| "Create ADR for X" | Decision | `adr.md` |
| "Create plan for X" | Implementation | `spec.md`, `plan.md` |
| "Write devlog for X" | Capture | `devlog.md` |
| "Update design for X" | Update | `design.md` (edit existing) |

## Cross-Reference Pattern

Every generated doc includes a **Related Documents** section:

```markdown
**Related Documents**:
- **Why**: [ADR-NNN](../adr/NNN-feature.md)
- **How**: [Design](../design/feature.md)
- **What**: [Spec](../spec/feature.md)
- **Steps**: [Plan](../plan/feature-implementation.md)
```

This creates a **navigation graph** for agents.

## Token Optimization

Instead of one 1000+ line doc, generate focused docs:
- ADR: ~200-300 lines (decision context)
- Design: ~300-600 lines (architecture)
- Spec: ~300-500 lines (requirements)
- Plan: ~200-400 lines (tasks)

Agent reads only what it needs → 50-80% token reduction.

## Part of the dev-* Family

| Skill | Purpose |
|-------|---------|
| `dev-inquiry` | Thinking through technical choices |
| `dev-context` | Aligning context for work |
| `dev-reports` | Communicating work progress |

## Templates

See `references/templates/` for each doc type:
- `adr.md` - Architecture Decision Record
- `design.md` - Living Design Document
- `spec.md` - Requirements Specification
- `plan.md` - Implementation Plan
- `devlog.md` - Development Log

See `references/patterns.md` for cross-referencing and naming conventions.
