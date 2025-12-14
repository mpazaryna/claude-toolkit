# Design Template: Living Architecture Document

Use this template when documenting HOW a system works. Design docs are **living**—update as the system evolves.

---

## Template

```markdown
# {Feature/System Name}

**Type**: System Architecture Design
**Version**: {X.Y}
**Last Updated**: {YYYY-MM-DD}
**Status**: {Draft | Active | Deprecated}

**Related Documents**:
- **Decision Rationale**: [ADR-{NNN}](../adr/{NNN}-{feature}.md)
- **Requirements**: [Spec](../spec/{feature}.md)
- **Implementation Plan**: [Plan](../plan/{feature}-implementation.md)
- **Tracking**: [GitHub Issue #{N}]({url})

---

## Overview

{2-3 paragraphs explaining:}
- What this system/feature does
- Why it exists (brief—detail in ADR)
- Key principle or philosophy

**Key Principle**: `{One-line summary of the core idea}`

---

## Architecture

### High-Level Structure

{ASCII diagram or description of components:}

```
┌─────────────────────────────────────────────────────────┐
│ Layer N: {Name}                                         │
│   {Components}                                          │
└─────────────────────────────────────────────────────────┘
                           │
┌─────────────────────────────────────────────────────────┐
│ Layer N-1: {Name}                                       │
│   {Components}                                          │
└─────────────────────────────────────────────────────────┘
```

### Component Responsibilities

#### {Component 1}

**Purpose**: {What it does}

**Inputs**: {What it receives}
**Outputs**: {What it produces}

**Key behaviors**:
- {Behavior 1}
- {Behavior 2}

#### {Component 2}

**Purpose**: {What it does}

{Same structure as above}

---

## Patterns

### Pattern 1: {Pattern Name}

**When to use**: {Situation where this pattern applies}

**How it works**:
```
{Flow or pseudocode showing the pattern}
```

**Example**:
```
{Concrete example of pattern in use}
```

### Pattern 2: {Pattern Name}

{Same structure as above}

---

## Data Flow

{How data moves through the system:}

```
{Input} → {Component A} → {Component B} → {Output}
           ↓
         {Side effect}
```

### Key Data Structures

{Important data shapes:}

```json
{
  "field": "type",
  "nested": {
    "field": "type"
  }
}
```

---

## Integration Points

### External Dependencies

{What this system connects to:}

| Dependency | Purpose | Interface |
|------------|---------|-----------|
| {System A} | {Why} | {API/Protocol} |
| {System B} | {Why} | {API/Protocol} |

### Internal Dependencies

{What internal components this relies on:}

- {Component}: {Why}
- {Component}: {Why}

---

## Configuration

{Key configuration options:}

| Setting | Purpose | Default |
|---------|---------|---------|
| {setting} | {what it controls} | {value} |

---

## Error Handling

{How the system handles failures:}

### Failure Modes

| Failure | Impact | Handling |
|---------|--------|----------|
| {Failure type} | {What breaks} | {How we handle it} |

### Recovery Patterns

{How the system recovers:}

- {Pattern 1}
- {Pattern 2}

---

## Performance Considerations

{Key performance characteristics:}

- **Expected throughput**: {metric}
- **Latency targets**: {metric}
- **Resource usage**: {metric}

### Optimization Strategies

{Current and future optimizations:}

- {Strategy 1}
- {Strategy 2}

---

## Security Considerations

{Security-relevant aspects:}

- {Consideration 1}
- {Consideration 2}

---

## Open Questions

{Unresolved design questions:}

1. {Question}
2. {Question}

---

## Change Log

| Date | Version | Changes |
|------|---------|---------|
| {YYYY-MM-DD} | {X.Y} | {What changed} |

---

**Last Updated**: {YYYY-MM-DD}
```

---

## Key Principles

1. **Living document**: Update as system evolves
2. **Visual where possible**: Diagrams > prose for architecture
3. **Pattern-focused**: Document reusable patterns
4. **Cross-referenced**: Link to ADR (why), Spec (what), Plan (how to build)
5. **Version tracked**: Change log shows evolution

## Naming Convention

```
docs/design/kebab-case-feature-name.md
```

Examples:
- `composable-agent-architecture.md`
- `authentication-system.md`
- `sync-engine.md`

## When to Update

- New component added
- Pattern changed
- Integration point modified
- Performance characteristics changed
- After completing implementation plan phase
