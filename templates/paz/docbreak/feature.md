# Feature Plan Breakdown Template

For documents containing feature descriptions, user stories, and requirements.

## Feature Artifacts to Generate

### 1. Feature Inventory (01-feature-inventory.md)

```markdown
# Feature Inventory

> Complete catalog of all features mentioned in planning document

## Feature Summary

| ID | Feature Name | Stage/Phase | Priority | Status | Complexity |
|----|--------------|-------------|----------|--------|------------|
| F-01 | {Name} | {Stage 1} | P0 | {📋 Planned} | {Medium} |
| F-02 | {Name} | {Stage 1} | P1 | {🔄 In Progress} | {Small} |
| F-03 | {Name} | {Stage 2} | P2 | {✅ Complete} | {Large} |
| ... | ... | ... | ... | ... | ... |

## Features by Stage/Phase

### Stage 1: {Name}
**Goal**: {What this stage achieves}

- **F-01**: {Feature name} - {one-line description}
- **F-02**: {Feature name} - {one-line description}
- **F-03**: {Feature name} - {one-line description}

### Stage 2: {Name}
[Same structure]

## Features by Priority

### P0: Must Have (MVP)
Critical features required for launch:
- **F-{id}**: {Name} - {why critical}

### P1: Should Have
Important but not launch-blocking:
- **F-{id}**: {Name} - {value proposition}

### P2: Nice to Have
Enhancements for future iterations:
- **F-{id}**: {Name} - {when to consider}

### P3: Ideas/Future
Concepts for long-term roadmap:
- **F-{id}**: {Name} - {vision}

## Feature Dependencies

### Independent Features
Can be built in parallel:
- F-{id}, F-{id}, F-{id}

### Dependent Features
Must be built in sequence:
```
F-01 (Foundation)
  ↓
F-02, F-03 (Build on F-01)
  ↓
F-04 (Requires F-02 & F-03)
```

## Feature Status Dashboard

- ✅ Complete: {count} features
- 🔄 In Progress: {count} features
- 📋 Planned: {count} features
- 💡 Ideas: {count} features

**Total**: {count} features
```

### 2. Feature Specifications (02-feature-{name}-spec.md)

```markdown
# Feature: {Feature Name}

**ID**: F-{id}
**Source**: {doc reference}
**Stage/Phase**: {where it belongs}
**Priority**: {P0/P1/P2/P3}
**Status**: {current status}

## Overview

### Problem Statement
{What user problem does this solve}

### Solution Summary
{How this feature solves it}

### User Value
{Why users want this}

### Business Value
{Why business needs this}

## User Stories

### Primary Story
**As a** {user type}
**I want to** {action}
**So that** {benefit}

**Acceptance Criteria**:
- [ ] {Testable criterion 1}
- [ ] {Testable criterion 2}
- [ ] {Testable criterion 3}

### Secondary Stories
[Additional user stories for this feature]

## Functional Requirements

### FR-{id}: {Requirement Title}
**Priority**: {Must Have | Should Have | Nice to Have}

**Description**: {What the system must do}

**Acceptance Criteria**:
- [ ] {Specific, testable criterion}

**Dependencies**: {Other requirements this depends on}

---

[Repeat for each functional requirement]

## Non-Functional Requirements

### NFR-{id}: {Requirement Title}
**Category**: {Performance | Security | Usability | Reliability}
**Target**: {Measurable target: e.g., "< 200ms response time"}

**Rationale**: {Why this matters}

**Verification**: {How to test/measure}

---

[Repeat for each non-functional requirement]

## User Experience

### User Flows
1. **Happy Path**: {Step-by-step user journey}
2. **Error Path**: {What happens when things go wrong}
3. **Edge Cases**: {Unusual but valid scenarios}

### UI/UX Requirements
- {Screen/view needed}
- {Interaction pattern}
- {Visual design consideration}

### Accessibility
- {A11y requirement 1}
- {A11y requirement 2}

## Technical Approach

### Architecture
{High-level technical design}

### Components Involved
- **{Component A}**: {role in feature}
- **{Component B}**: {role in feature}

### Data Models
- **{Model A}**: {how it's used}
- **{Model B}**: {how it's used}

### APIs/Interfaces
- **{API endpoint/interface}**: {purpose}

### Third-Party Integrations
- **{Service/SDK}**: {why needed}

## Implementation Tasks

### Phase 1: Foundation
- [ ] T-{id}: {Task}
  - **Description**: {details}
  - **Effort**: {estimate}
  - **Owner**: {person/team}

### Phase 2: Core Functionality
- [ ] T-{id}: {Task}
  [Same structure]

### Phase 3: Polish & Testing
- [ ] T-{id}: {Task}
  [Same structure]

## Testing Strategy

### Unit Tests
- {What to unit test}
- {Coverage target}

### Integration Tests
- {Scenario 1}
- {Scenario 2}

### E2E Tests
- {User journey to automate}

### Manual Testing
- {Exploratory testing areas}
- {Edge cases to verify}

## Dependencies

### Depends On
- **{Feature/Component}**: {Why needed}
- **{External service}**: {How used}

### Blocks
- **{Feature}**: {How this enables it}

## Risks & Concerns

### Technical Risks
- **{Risk}**: {Mitigation}

### UX Risks
- **{Risk}**: {How to validate}

### Performance Concerns
- **{Concern}**: {Optimization strategy}

## Success Metrics

### Adoption Metrics
- {What indicates users find this valuable}

### Performance Metrics
- {Technical metrics to monitor}

### Business Metrics
- {ROI or business impact measures}

## Rollout Plan

### Release Strategy
- {Alpha/Beta/GA approach}
- {Feature flags}
- {Gradual rollout}

### Documentation Needed
- [ ] User documentation
- [ ] API documentation
- [ ] Developer guide

### Training Required
- {Who needs training}
- {What materials needed}

## Open Questions

### Q-{id}: {Question}
**Impact**: {What depends on this answer}
**Options**: {Possible solutions}
**Decision By**: {date}
**Owner**: {who decides}

---

[Repeat for open questions]

## Future Enhancements

Ideas for v2/v3 of this feature:
- {Enhancement idea 1}
- {Enhancement idea 2}
```

### 3. User Stories Collection (03-user-stories.md)

```markdown
# User Stories

> All user stories extracted from planning document

## Stories by User Type

### {User Type 1}: {Description of user type}

#### US-{id}: {Story Title}
**Feature**: F-{id} ({Feature name})
**Priority**: {P0/P1/P2/P3}
**Status**: {📋 Planned | 🔄 In Progress | ✅ Done}

**Story**:
As a **{user type}**
I want to **{action}**
So that **{benefit}**

**Acceptance Criteria**:
- [ ] Given {context}, when {action}, then {outcome}
- [ ] Given {context}, when {action}, then {outcome}

**Notes**: {Additional context}

**Tasks**:
- [ ] T-{id}: {Implementation task}

---

[Repeat for each story for this user type]

### {User Type 2}
[Same structure]

## Stories by Feature

### Feature F-{id}: {Feature Name}
- US-{id}: {Story title}
- US-{id}: {Story title}
- US-{id}: {Story title}

## Story Mapping

```
User Activity 1     User Activity 2     User Activity 3
     |                   |                   |
   US-01               US-04               US-07
   US-02               US-05               US-08
   US-03               US-06               US-09

   MVP ─────────────────────────────────────┘
   V2 ──────────────────────┘
```

## Epic Groupings

### Epic E-{id}: {Epic Name}
**Goal**: {What this epic achieves}

**Stories**:
- US-{id}: {Story}
- US-{id}: {Story}
- US-{id}: {Story}

**Total Effort**: {story points or time estimate}

## Story Status

| Status | Count | Stories |
|--------|-------|---------|
| ✅ Done | {#} | US-{id}, US-{id} |
| 🔄 In Progress | {#} | US-{id}, US-{id} |
| 📋 Planned | {#} | US-{id}, US-{id} |

## Story Dependencies

### US-{id} enables:
- US-{id}
- US-{id}

### US-{id} depends on:
- US-{id}
- US-{id}
```

### 4. Acceptance Criteria (04-acceptance-criteria.md)

```markdown
# Acceptance Criteria & Test Scenarios

## Feature-Level Acceptance

### Feature F-{id}: {Feature Name}

#### Release Criteria
Feature is considered complete when:
- [ ] All P0 user stories done
- [ ] All automated tests passing
- [ ] Manual QA sign-off
- [ ] Performance targets met
- [ ] Documentation complete
- [ ] Accessibility verified
- [ ] Security review passed

#### Verification Plan

**Test Environment**: {where to test}
**Test Data**: {what data to use}
**Test Users**: {who tests}

---

## Story-Level Acceptance

### US-{id}: {Story Title}

#### Acceptance Criteria

**AC-{id}**: {Criterion}
**Given** {precondition}
**When** {user action}
**Then** {expected outcome}

**Test Steps**:
1. {Step 1}
2. {Step 2}
3. {Step 3}

**Expected Result**: {What should happen}
**Actual Result**: {To be filled during testing}
**Status**: {✅ Pass | ❌ Fail | 🔄 Blocked}

---

[Repeat for each acceptance criterion]

#### Edge Cases

**EC-{id}**: {Edge case description}
**Scenario**: {Unusual but valid situation}
**Expected Behavior**: {How system should respond}

---

## Test Coverage Matrix

| Feature | Unit Tests | Integration Tests | E2E Tests | Manual Tests |
|---------|-----------|-------------------|-----------|--------------|
| F-01 | ✅ 95% | ✅ Complete | ✅ Complete | ✅ Passed |
| F-02 | 🔄 80% | 📋 Planned | 📋 Planned | 📋 Pending |
| ... | ... | ... | ... | ... |

## Regression Testing

### Critical Paths (always test)
1. {User journey 1}
2. {User journey 2}
3. {User journey 3}

### Smoke Tests (quick validation)
- [ ] {Basic function 1 works}
- [ ] {Basic function 2 works}

## Definition of Done

A story/feature is "done" when:
- [ ] Code complete and reviewed
- [ ] Unit tests written and passing
- [ ] Integration tests passing
- [ ] Acceptance criteria verified
- [ ] No critical bugs
- [ ] Documentation updated
- [ ] Demo-able to stakeholders
- [ ] Deployed to staging
- [ ] QA sign-off received
```

## Feature Analysis Patterns

### Extracting User Stories

Look for these patterns:
- "As a {role}, I want {action}, so that {benefit}"
- "Users need to {action}"
- "The system should {behavior}"
- Feature descriptions with actors

### Identifying Requirements

**Explicit requirements**:
- "Must", "Shall", "Required"
- Numbered requirement lists
- "The system will..."

**Implicit requirements**:
- Described behaviors
- Mentioned constraints
- User expectations

### Categorizing Features

**By complexity**:
- Simple: CRUD, basic UI, configuration
- Moderate: Business logic, calculations, workflows
- Complex: AI/ML, real-time, distributed systems

**By type**:
- Core functionality
- User experience enhancements
- Performance optimizations
- Security/privacy features
- Integration features
- Administrative/operational

### Priority Inference

Indicators of priority:
- Mentioned in MVP/Phase 1
- Marked as "critical" or "must-have"
- Dependency for many features
- User pain point severity
- Business impact magnitude

### Completeness Check

A feature spec should answer:
- [ ] Who is this for? (user type)
- [ ] What problem does it solve?
- [ ] How does it work? (functionality)
- [ ] How do we know it's done? (acceptance)
- [ ] What could go wrong? (risks)
- [ ] How do we measure success? (metrics)
