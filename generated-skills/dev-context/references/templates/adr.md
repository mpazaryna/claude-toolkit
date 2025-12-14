# ADR Template: Architecture Decision Record

Use this template when documenting WHY a decision was made. ADRs are **immutable**—if the decision changes, write a new ADR.

---

## Template

```markdown
# ADR-{NNN}: {Decision Title}

**Status**: {Proposed | Accepted | Deprecated | Superseded by ADR-XXX}
**Date**: {YYYY-MM-DD}
**Decision Makers**: {names}
**Related Documents**:
- Design: [docs/design/{feature}.md](../design/{feature}.md)
- Specification: [docs/spec/{feature}.md](../spec/{feature}.md)
- Implementation: [docs/plan/{feature}-implementation.md](../plan/{feature}-implementation.md)

---

## Context

### Problem Statement

{What problem are we solving? Why does this decision matter?}

{2-3 paragraphs explaining:}
- The specific challenge or need
- Why the status quo doesn't work
- What's at stake if we don't address this

### Strategic Importance

{Why this decision matters for the larger system/project:}
- {Benefit 1}
- {Benefit 2}
- {Benefit 3}

### Existing Foundation

{What we already have that this builds upon:}
- {Existing component/pattern 1}
- {Existing component/pattern 2}

---

## Decision

{Clear statement of the decision made.}

{1-2 sentences: "We will {do X} because {reason}."}

### Key Components

{Break down the decision into actionable parts:}

#### 1. {Component/Aspect 1}
- {Detail}
- {Detail}

#### 2. {Component/Aspect 2}
- {Detail}
- {Detail}

---

## Alternatives Considered

### Alternative 1: {Name}

**Description**: {What this alternative would look like}

**Rejected because**:
- {Reason 1}
- {Reason 2}

### Alternative 2: {Name}

**Description**: {What this alternative would look like}

**Rejected because**:
- {Reason 1}
- {Reason 2}

---

## Consequences

### Positive Consequences

{What we gain from this decision:}

**{Category 1}**:
- {Benefit}
- {Benefit}

**{Category 2}**:
- {Benefit}

### Negative Consequences

{What we accept as tradeoffs:}

**{Category 1}**:
- {Tradeoff}

### Mitigation Strategies

{How we address the negative consequences:}

**For {negative consequence}**:
- {Mitigation approach}

---

## Implementation Notes

{Brief notes on how this will be implemented—detailed steps go in the Plan doc.}

### Phased Approach

**Phase 1**: {Brief description}
**Phase 2**: {Brief description}

### Success Metrics

{How we know this decision was correct:}
- {Metric 1}
- {Metric 2}

---

## Related Decisions

**Built upon**:
- ADR-{NNN}: {Related previous decision}

**Future ADRs needed**:
- {Potential future decision topic}

---

## References

{Links to external resources, internal docs, prior art}

---

**Approved by**: {name}
**Date**: {YYYY-MM-DD}
```

---

## Key Principles

1. **Immutable**: Once accepted, don't edit—write a new ADR if decision changes
2. **Context-rich**: Future readers should understand WHY without asking
3. **Alternatives documented**: Show what was considered and rejected
4. **Consequences explicit**: Both positive and negative
5. **Cross-referenced**: Link to Design/Spec/Plan docs

## Naming Convention

```
docs/adr/NNN-kebab-case-decision-name.md
```

Examples:
- `001-composable-agent-architecture.md`
- `002-swiftdata-over-coredata.md`
- `003-jwt-authentication-strategy.md`

## Status Values

- **Proposed**: Under discussion
- **Accepted**: Decision finalized
- **Deprecated**: No longer applies
- **Superseded by ADR-XXX**: Replaced by newer decision
