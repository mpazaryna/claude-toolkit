# Context Architecture Patterns

Patterns for building interconnected context that agents (and humans) can navigate.

---

## The Navigation Graph

Every doc links to related docs, creating a **navigation graph**:

```
       PRD (PRODUCT INTENT)
            │
            ↓
         ADR (WHY)
            ↑
            │
            ↓
Design (HOW) ←→ Spec (WHAT)
     ↑              ↑
     │              │
     └──→ Plan ←────┘
         (STEPS)
            │
            ↓
     Devlog (NARRATIVE)
```

PRD sits at the top—product intent flows down into technical decisions.

Agents can traverse this graph based on what they need.

---

## Cross-Reference Pattern

Every doc includes a **Related Documents** header:

```markdown
**Related Documents**:
- **Product**: [PRD](../prd/feature.md) - Product intent
- **Why**: [ADR-NNN](../adr/NNN-feature.md) - Decision rationale
- **How**: [Design Doc](../design/feature.md) - Architecture
- **What**: [Spec](../spec/feature.md) - Requirements
- **Steps**: [Plan](../plan/feature-implementation.md) - Tasks
- **Tracking**: [GitHub Issue #N](url) - Current status
```

### PRD Cross-References

```markdown
**Related Documents**:
- **Decisions**: [ADR-NNN](../adr/NNN-feature.md) - Technical decisions
- **Architecture**: [Design Doc](../design/feature.md) - How it works
- **Requirements**: [Spec](../spec/feature.md) - Technical requirements
- **Implementation**: [Plan](../plan/feature-implementation.md) - Build steps
```

### ADR Cross-References

```markdown
**Related Documents**:
- **Product**: [PRD](../prd/feature.md) - Product intent
- Design: [docs/design/feature.md](../design/feature.md)
- Specification: [docs/spec/feature.md](../spec/feature.md)
- Implementation: [docs/plan/feature-implementation.md](../plan/feature-implementation.md)
```

### Design Cross-References

```markdown
**Related Documents**:
- **Decision Rationale**: [ADR-NNN](../adr/NNN-feature.md)
- **Requirements**: [Spec](../spec/feature.md)
- **Implementation Plan**: [Plan](../plan/feature-implementation.md)
- **Tracking**: [GitHub Issue #N](url)
```

### Spec Cross-References

```markdown
**Related Documents**:
- **Why**: [ADR-NNN](../adr/NNN-feature.md) - Decision rationale
- **How**: [Design Doc](../design/feature.md) - Architecture
- **Steps**: [Implementation Plan](../plan/feature-implementation.md) - Tasks
```

### Plan Cross-References

```markdown
**Related Documents**:
- **Why**: [ADR-NNN](../adr/NNN-feature.md)
- **How**: [Design Doc](../design/feature.md)
- **What**: [Spec](../spec/feature.md)
- **Tracking**: [GitHub Issue #N](url)
```

### Devlog Cross-References

```markdown
## Related Work

- [ADR-NNN: Title](../adr/NNN-feature.md) - Decision that led to this
- [Design: Title](../design/feature.md) - Architecture context
- [Plan: Title](../plan/feature-implementation.md) - Implementation details
- [GitHub Issue #N](url) - Tracking
```

---

## Naming Conventions

### Directory Structure

```
docs/
├── prd/                    # Product Requirements Documents
│   ├── feature-a.md
│   └── feature-b.md
├── adr/                    # Architecture Decision Records
│   ├── 001-feature-a.md
│   ├── 002-feature-b.md
│   └── 003-feature-c.md
├── design/                 # Living Design Documents
│   ├── feature-a.md
│   └── feature-b.md
├── spec/                   # Requirements Specifications
│   ├── feature-a.md
│   └── feature-b.md
├── plan/                   # Implementation Plans
│   ├── feature-a-implementation.md
│   └── feature-b-implementation.md
├── devlog/                 # Development Logs
│   ├── 2025-01-15-topic-a.md
│   └── 2025-01-16-topic-b.md
└── issues/                 # GitHub Issue Bodies (optional)
    └── github-issue-NN-body.md
```

### File Naming

| Doc Type | Pattern | Example |
|----------|---------|---------|
| PRD | `kebab-case-feature.md` | `user-authentication.md` |
| ADR | `NNN-kebab-case-title.md` | `001-composable-agent-architecture.md` |
| Design | `kebab-case-feature.md` | `composable-agent-architecture.md` |
| Spec | `kebab-case-feature.md` | `composable-agent-architecture.md` |
| Plan | `kebab-case-feature-implementation.md` | `composable-agent-implementation.md` |
| Devlog | `YYYY-MM-DD-kebab-case-topic.md` | `2025-12-03-information-architecture.md` |

### ADR Numbering

ADRs are numbered sequentially:
- `001-` - First decision
- `002-` - Second decision
- etc.

To find the next number:
```bash
ls docs/adr/*.md | tail -1  # Find highest number, add 1
```

---

## Semantic Routing

Agents can route to the right doc based on the question:

| Question Type | Route To | Why |
|---------------|----------|-----|
| "What are we building?" | PRD | Product intent |
| "What's the user value?" | PRD | Business justification |
| "Why did we...?" | ADR | Immutable decision record |
| "How does X work?" | Design | Current architecture |
| "What are the requirements?" | Spec | Acceptance criteria |
| "What should I build next?" | Plan | Task breakdown |
| "What happened with X?" | Devlog | Historical narrative |
| "What's the current status?" | Issue/Plan | Ephemeral tracking |

### Agent Routing Logic

```
IF question contains "building" OR "user value" OR "product" OR "feature":
    → Read PRD

IF question contains "why" OR "decision" OR "chose":
    → Read ADR

IF question contains "how" OR "architecture" OR "works":
    → Read Design Doc

IF question contains "requirements" OR "acceptance" OR "criteria":
    → Read Spec

IF question contains "tasks" OR "build" OR "implement" OR "next":
    → Read Plan

IF question contains "learned" OR "happened" OR "lessons":
    → Read Devlog
```

---

## Document Lifecycle

| Doc Type | Created | Updated | Lifecycle |
|----------|---------|---------|-----------|
| **PRD** | Before engineering | When product scope changes | Stable |
| **ADR** | When decision made | Never | Immutable |
| **Design** | Start of work | As system evolves | Living |
| **Spec** | Start of work | When requirements change | Stable |
| **Plan** | Start of work | As work progresses | Evolving |
| **Devlog** | After significant work | Never | Historical |

### Immutable vs Living

**Immutable (ADR, Devlog)**:
- Never edit after creation
- If decision changes → Write new ADR
- If new insights → Write new Devlog

**Living (Design, Plan)**:
- Update as work progresses
- Track changes in changelog
- Current state always accurate

**Stable (PRD, Spec)**:
- Update only when scope/requirements change
- Version changes explicitly
- PRD: product scope doesn't move casually
- Spec: acceptance criteria don't move casually

---

## Token Optimization

### Size Guidelines

| Doc Type | Target Lines | Purpose |
|----------|--------------|---------|
| PRD | 200-400 | Product intent |
| ADR | 200-300 | Decision context |
| Design | 300-600 | Architecture details |
| Spec | 300-500 | Requirements |
| Plan | 200-400 | Task breakdown |
| Devlog | 200-500 | Narrative |

### Why Multiple Small Docs > One Large Doc

**One 1000+ line doc**:
- Agent reads everything
- High token cost
- Context pollution
- Hard to navigate

**Four 250-line docs**:
- Agent reads only what needed
- 50-80% token reduction
- Focused context
- Clear navigation

---

## Generation Workflow

### Full Context Generation

When starting new work:

```
1. Parse feature name and description from request
2. Generate PRD with product intent (FIRST)
3. Determine next ADR number (glob docs/adr/*.md)
4. Generate ADR with decision context
5. Generate Design with architecture scaffolding
6. Generate Spec with requirements structure
7. Generate Plan with phase breakdown
8. Add cross-references to all docs
9. Return summary with file paths
```

### Partial Generation

When updating existing context:

```
1. Check what docs already exist (glob)
2. Read existing docs for context
3. Generate only missing docs
4. Update cross-references in existing docs
5. Return summary of changes
```

---

## Quality Checklist

### After Generation, Validate:

**PRD**:
- [ ] Has Status, Version, Date, Owner
- [ ] Problem statement is clear and compelling
- [ ] User stories have acceptance criteria
- [ ] Success metrics are measurable
- [ ] Out of scope is explicit
- [ ] Links to related docs

**ADR**:
- [ ] Has Status, Date, Decision Makers
- [ ] Context explains problem clearly
- [ ] Decision is stated explicitly
- [ ] Alternatives are documented
- [ ] Consequences (positive/negative) listed
- [ ] Links to related docs

**Design**:
- [ ] Has Status, Version, Last Updated
- [ ] Overview explains purpose
- [ ] Architecture is visualized (diagram/ASCII)
- [ ] Patterns are documented with examples
- [ ] Links to related docs

**Spec**:
- [ ] FRs have acceptance criteria
- [ ] NFRs are measurable
- [ ] System-level acceptance criteria exist
- [ ] Success metrics defined
- [ ] Links to related docs

**Plan**:
- [ ] Has Status, Owner, Timeline
- [ ] Phases have tasks and success criteria
- [ ] Deliverables identified
- [ ] Dependencies explicit
- [ ] Links to related docs

**Devlog**:
- [ ] TL;DR captures main insight
- [ ] Problem is clearly stated
- [ ] Solution is explained
- [ ] Lessons learned documented
- [ ] Links to related docs
