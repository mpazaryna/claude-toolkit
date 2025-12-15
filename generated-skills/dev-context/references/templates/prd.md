# PRD Template: Product Requirements Document

Use this template when capturing WHAT to build and WHY it matters from a product perspective. PRDs are **stable**—they define product intent before engineering begins.

---

## Template

```markdown
# PRD: {Feature Name}

**Status**: {Draft | Review | Approved | Implemented}
**Version**: {X.Y}
**Date**: {YYYY-MM-DD}
**Owner**: {Product owner name}

**Related Documents**:
- **Decisions**: [ADR-NNN](../adr/NNN-feature.md) - Technical decisions
- **Architecture**: [Design Doc](../design/feature.md) - How it works
- **Requirements**: [Spec](../spec/feature.md) - Technical requirements
- **Implementation**: [Plan](../plan/feature-implementation.md) - Build steps

---

## Executive Summary

{2-3 sentences: What are we building and why does it matter?}

**Value Proposition**: {One-line statement of the core value delivered}

---

## Problem Statement

### The Problem

{What problem are we solving? Be specific about the pain point.}

{2-3 paragraphs explaining:}
- Who experiences this problem
- How they experience it today
- What's the cost of not solving it

### Why Now?

{Why is this the right time to solve this problem?}

- {Reason 1: market pressure, user feedback, strategic priority}
- {Reason 2}
- {Reason 3}

---

## Users & Personas

### Primary Persona: {Name}

**Who**: {Brief description of this user type}
**Goal**: {What they're trying to accomplish}
**Pain Point**: {Their specific frustration today}

### Secondary Persona: {Name}

**Who**: {Brief description}
**Goal**: {What they're trying to accomplish}
**Pain Point**: {Their specific frustration}

---

## User Stories

### US-1: {Story Title}

**As a** {persona},
**I want** {capability},
**So that** {benefit}.

**Acceptance Criteria**:
- AC-1.1: {Criterion}
- AC-1.2: {Criterion}
- AC-1.3: {Criterion}

---

### US-2: {Story Title}

**As a** {persona},
**I want** {capability},
**So that** {benefit}.

**Acceptance Criteria**:
- AC-2.1: {Criterion}
- AC-2.2: {Criterion}

---

### US-3: {Story Title}

**As a** {persona},
**I want** {capability},
**So that** {benefit}.

**Acceptance Criteria**:
- AC-3.1: {Criterion}
- AC-3.2: {Criterion}

---

## Requirements

### Functional Requirements

| ID | Requirement | Priority | User Story |
|----|-------------|----------|------------|
| FR-1 | {The system shall...} | Must Have | US-1 |
| FR-2 | {The system shall...} | Must Have | US-2 |
| FR-3 | {The system shall...} | Should Have | US-3 |
| FR-4 | {The system shall...} | Nice to Have | US-1 |

### Non-Functional Requirements

| ID | Requirement | Target |
|----|-------------|--------|
| NFR-1 | Performance: {aspect} | {measurable target} |
| NFR-2 | Reliability: {aspect} | {measurable target} |
| NFR-3 | Usability: {aspect} | {measurable target} |

---

## Success Criteria

### Launch Criteria

The feature is ready to launch when:

- [ ] {Criterion 1}
- [ ] {Criterion 2}
- [ ] {Criterion 3}

### Success Metrics

| Metric | Baseline | Target | Timeframe |
|--------|----------|--------|-----------|
| {Metric 1} | {current} | {goal} | {when to measure} |
| {Metric 2} | {current} | {goal} | {when to measure} |
| {Metric 3} | N/A | {goal} | {when to measure} |

### Definition of Success

{1-2 sentences: How do we know this was successful 30/60/90 days after launch?}

---

## Constraints & Assumptions

### Constraints

{What limitations exist that bound the solution?}

- {Technical constraint}
- {Business constraint}
- {Resource constraint}

### Assumptions

{What are we assuming to be true?}

- {Assumption 1} — *Risk if wrong: {impact}*
- {Assumption 2} — *Risk if wrong: {impact}*
- {Assumption 3} — *Risk if wrong: {impact}*

---

## Out of Scope

The following are explicitly **NOT** included in this version:

| Item | Reason | Future Consideration |
|------|--------|---------------------|
| {Feature/capability 1} | {Why not now} | {When/if to revisit} |
| {Feature/capability 2} | {Why not now} | {When/if to revisit} |
| {Feature/capability 3} | {Why not now} | {When/if to revisit} |

---

## Dependencies

### Internal Dependencies

| Dependency | Team/System | Status | Risk |
|------------|-------------|--------|------|
| {Dependency 1} | {owner} | {status} | {risk level} |
| {Dependency 2} | {owner} | {status} | {risk level} |

### External Dependencies

| Dependency | Provider | Status | Mitigation |
|------------|----------|--------|------------|
| {Dependency 1} | {provider} | {status} | {mitigation} |

---

## Open Questions

| # | Question | Owner | Due | Resolution |
|---|----------|-------|-----|------------|
| 1 | {Question} | {who} | {date} | {answer when resolved} |
| 2 | {Question} | {who} | {date} | |

---

## Change Log

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| {YYYY-MM-DD} | {X.Y} | Initial draft | {name} |

---

**Approval**: {Pending | Approved by [name] on [date]}
**Next Steps**: Create technical context → ADR for key decisions, then Design/Spec/Plan
```

---

## Key Principles

1. **Product perspective**: Focus on user value, not implementation details
2. **Problem-first**: Clearly articulate the problem before jumping to solutions
3. **User stories**: Capture needs in "As a... I want... So that..." format
4. **Measurable success**: Define metrics that prove the feature worked
5. **Explicit scope**: Out of Scope is as important as In Scope
6. **Living handoff**: This doc feeds into ADR/Design/Spec/Plan

## Naming Convention

```
docs/prd/kebab-case-feature-name.md
```

Examples:
- `user-authentication.md`
- `sync-engine-v2.md`
- `notification-system.md`

## Status Values

- **Draft**: Being written, not ready for review
- **Review**: Ready for stakeholder feedback
- **Approved**: Signed off, ready for engineering
- **Implemented**: Feature shipped (doc becomes historical reference)

## PRD vs Spec

| PRD | Spec |
|-----|------|
| Product perspective | Engineering perspective |
| User stories | Technical requirements |
| Business value | Acceptance criteria |
| Success metrics | Performance targets |
| "What to build" | "What it must do technically" |

The PRD informs the Spec. They are complementary, not redundant.

## Priority Levels

- **Must Have**: Feature doesn't ship without this
- **Should Have**: Important but can work around
- **Nice to Have**: Enhances value but not critical

## Writing Good User Stories

**Bad**: "User can log in"
**Good**: "As a returning user, I want to log in with my email and password, so that I can access my saved preferences"

**Bad**: "Fast performance"
**Good**: "NFR-1: Page load time < 2 seconds on 3G connection"
