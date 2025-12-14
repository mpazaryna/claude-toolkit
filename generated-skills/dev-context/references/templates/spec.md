# Spec Template: Requirements Specification

Use this template when documenting WHAT must be done. Specs are **stable**—they define acceptance criteria.

---

## Template

```markdown
# {Feature Name} - Requirements Specification

**Status**: {Draft | Active | Complete}
**Version**: {X.Y}
**Date**: {YYYY-MM-DD}
**Owner**: {name}

**Related Documents**:
- **Why**: [ADR-{NNN}](../adr/{NNN}-{feature}.md) - Decision rationale
- **How**: [Design Doc](../design/{feature}.md) - Architecture
- **Steps**: [Implementation Plan](../plan/{feature}-implementation.md) - Tasks

---

## Purpose

This document specifies the **functional and non-functional requirements** for {feature}. It defines **WHAT** the system must accomplish, not HOW it will be implemented.

**Use this document to**:
- Validate that the system meets requirements
- Write acceptance tests
- Determine if a feature is complete
- Guide design decisions

---

## Functional Requirements

### FR-1: {Requirement Name}

**Requirement**: The system SHALL {do something specific}.

**Rationale**: {Why this requirement exists}

**Acceptance Criteria**:
- AC-1.1: {Specific, testable criterion}
- AC-1.2: {Specific, testable criterion}
- AC-1.3: {Specific, testable criterion}

**Test**:
```
Given: {precondition}
When: {action}
Then: {expected result}
```

---

### FR-2: {Requirement Name}

**Requirement**: The system SHALL {do something specific}.

**Rationale**: {Why this requirement exists}

**Acceptance Criteria**:
- AC-2.1: {Specific, testable criterion}
- AC-2.2: {Specific, testable criterion}

**Test**:
```
Given: {precondition}
When: {action}
Then: {expected result}
```

---

### FR-3: {Requirement Name}

{Same structure}

---

## Non-Functional Requirements

### NFR-1: Performance - {Aspect}

**Requirement**: {Performance characteristic} SHALL be {measurable target}.

**Current Baseline**: {Current state if known}
**Target**: {Goal}

**Measurement**:
```
{How to measure this requirement}
```

---

### NFR-2: Performance - {Aspect}

{Same structure}

---

### NFR-3: Quality - {Aspect}

**Requirement**: {Quality characteristic} SHALL {meet standard}.

**Quality Criteria**:
- {Criterion 1}
- {Criterion 2}

**Validation**: {How to validate}

---

### NFR-4: Maintainability - {Aspect}

**Requirement**: {Maintainability characteristic}.

**Targets**:
- {Target 1}
- {Target 2}

**Measurement**: {How to measure}

---

## Acceptance Criteria (System-Level)

### AC-S1: {Scenario Name}

**Scenario**: {Description of end-to-end scenario}

```
Given: {Starting state}
When: {User/System action}
Then:
  - {Expected outcome 1}
  - {Expected outcome 2}
  - {Expected outcome 3}
```

---

### AC-S2: {Scenario Name}

{Same structure}

---

### AC-S3: {Scenario Name}

{Same structure}

---

## Out of Scope (Future Versions)

The following are explicitly OUT OF SCOPE for this version:

- {Feature/capability 1} - (future: {when/why})
- {Feature/capability 2} - (future: {when/why})
- {Feature/capability 3} - (future: {when/why})

These are important but not blocking current scope.

---

## Success Metrics

### Quantitative Metrics

| Metric | Baseline | Target | Measurement |
|--------|----------|--------|-------------|
| {Metric 1} | {current} | {goal} | {how to measure} |
| {Metric 2} | {current} | {goal} | {how to measure} |

### Qualitative Metrics

| Metric | Validation Method |
|--------|-------------------|
| {Metric 1} | {How to validate} |
| {Metric 2} | {How to validate} |

---

## Validation Plan

### Phase {N} Validation

- [ ] {Validation checkpoint 1}
- [ ] {Validation checkpoint 2}
- [ ] {Validation checkpoint 3}

### Phase {N+1} Validation

- [ ] {Validation checkpoint}

---

## Requirements Traceability

| Requirement | Design Reference | Implementation Phase |
|-------------|------------------|---------------------|
| FR-1 | Design Doc: {section} | Phase {N} |
| FR-2 | Design Doc: {section} | Phase {N} |
| NFR-1 | Design Doc: {section} | Phase {N} |

---

## Change Log

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| {YYYY-MM-DD} | {X.Y} | {Description} | {name} |

---

**Approval**: This specification is approved for implementation.
**Next Steps**: Reference [Implementation Plan](../plan/{feature}-implementation.md) for build phases.
```

---

## Key Principles

1. **WHAT not HOW**: Define requirements, not implementation
2. **Testable criteria**: Every requirement has acceptance criteria
3. **Measurable NFRs**: Performance/quality targets are specific numbers
4. **Traceable**: Requirements map to design and implementation
5. **Stable**: Changes are versioned and logged

## Naming Convention

```
docs/spec/kebab-case-feature-name.md
```

Examples:
- `composable-agent-architecture.md`
- `user-authentication.md`
- `sync-engine.md`

## Requirement Types

- **FR** (Functional Requirement): What the system does
- **NFR** (Non-Functional Requirement): How well it does it
- **AC** (Acceptance Criteria): How we know it's done
- **AC-S** (System-level AC): End-to-end scenarios

## Writing Good Acceptance Criteria

**Bad**: "The system should be fast"
**Good**: "Response time SHALL be < 200ms for 95th percentile"

**Bad**: "Users can log in"
**Good**: "AC-1.1: Valid credentials return JWT token within 500ms"
