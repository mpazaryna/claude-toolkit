# Roadmap Breakdown Template

For documents containing phases, milestones, timelines, and dependencies.

## Roadmap Artifacts to Generate

### 1. Phase Overview (01-phase-overview.md)

```markdown
# Roadmap Phase Overview

> High-level view of all project phases

## Timeline Summary

| Phase | Timeline | Status | Dependencies | Key Deliverables |
|-------|----------|--------|--------------|------------------|
| Phase 1: {Name} | {Q1 2025} | {✅ Complete / 🔄 In Progress / 📋 Planned} | {None} | {count} items |
| Phase 2: {Name} | {Q2 2025} | {📋 Planned} | {Phase 1} | {count} items |
| ... | ... | ... | ... | ... |

## Phase Dependency Graph

```
Phase 1 (Foundation)
    ↓
Phase 2 (Core Features) ← Phase 3 (Enhancement) [partial dependency]
    ↓                         ↓
Phase 4 (Integration) ←──────┘
    ↓
Phase 5 (Launch Prep)
```

## Critical Path

The longest sequence of dependent phases:
1. {Phase A} → {Phase B} → {Phase C}

**Total duration**: {X weeks/months}
**Key risks**: {What could delay this path}

## Parallel Work Opportunities

Phases that can run concurrently:
- {Phase X} + {Phase Y} (no dependencies)
- {Phase M} + {Phase N} (after Phase Z completes)

## Phase Status Dashboard

### ✅ Completed Phases
- {Phase 1}: {completion date}
- {Phase 2}: {completion date}

### 🔄 In Progress
- {Phase X}: {% complete} - {blockers}

### 📋 Upcoming
- {Phase Y}: {start date} - {prerequisites}

### ❓ Under Review
- {Phase Z}: {needs decision on scope/timing}
```

### 2. Individual Phase Plans (02-phase-{N}-plan.md)

```markdown
# Phase {N}: {Phase Name}

**Source**: {doc reference}
**Timeline**: {start} - {end}
**Status**: {current status}
**Owner**: {team/person}

## Phase Objectives

### Primary Goals
1. {Goal 1}: {measurable outcome}
2. {Goal 2}: {measurable outcome}
3. {Goal 3}: {measurable outcome}

### Success Criteria
- [ ] {Criteria 1}
- [ ] {Criteria 2}
- [ ] {Criteria 3}

## Scope

### In Scope
- {Feature/capability A}
- {Feature/capability B}
- {Feature/capability C}

### Out of Scope (Deferred to Later)
- {Item X} → Phase {M}
- {Item Y} → Phase {N}

### Scope Questions
- [ ] Q-{id}: {Open question about scope}

## Work Breakdown

### Workstream 1: {Name}
**Purpose**: {What this workstream achieves}
**Effort**: {person-weeks}
**Dependencies**: {what must exist first}

#### Tasks
- [ ] T-{id}: {Task title}
  - **Description**: {details}
  - **Effort**: {small/medium/large}
  - **Owner**: {TBD or assigned}
  - **Acceptance**: {done criteria}
  - **Blocks**: {what depends on this}

- [ ] T-{id}: {Next task}
  [Same structure]

### Workstream 2: {Name}
[Same structure]

## Dependencies

### Depends On (Prerequisites)
- **{Phase/Task}**: {Why needed}
- **{External dependency}**: {What we're waiting for}

### Enables (Downstream)
- **{Phase/Feature}**: {How this phase unblocks it}

### Concurrent Work
- **{Phase/Workstream}**: {Can run in parallel}

## Milestones

### Milestone 1: {Name}
**Target Date**: {date}
**Definition of Done**:
- [ ] {Criteria 1}
- [ ] {Criteria 2}

**Verification**:
- {How to prove milestone is achieved}

**Celebration**:
- {How to mark this achievement}

---

[Repeat for each milestone in phase]

## Risks & Mitigation

### Risk 1: {Description}
**Likelihood**: {High/Medium/Low}
**Impact**: {High/Medium/Low}
**Mitigation**:
- {Action to reduce risk}
- {Contingency plan if risk occurs}

---

[Repeat for each risk]

## Resources Required

### Team
- {Role 1}: {X hours/week}
- {Role 2}: {Y hours/week}

### Tools/Services
- {Tool/Service}: {Purpose}
- {Cost if applicable}

### External Dependencies
- {Vendor/Partner}: {What they provide}

## Communication Plan

### Status Updates
- **Frequency**: {daily/weekly/bi-weekly}
- **Format**: {standup/report/dashboard}
- **Audience**: {stakeholders}

### Key Checkpoints
- {Date}: {Checkpoint purpose}
- {Date}: {Checkpoint purpose}

## Phase Exit Criteria

Before moving to next phase:
- [ ] All P0 tasks complete
- [ ] Success criteria met
- [ ] Documentation updated
- [ ] Tests passing
- [ ] Stakeholder approval
- [ ] Known issues documented
- [ ] Lessons learned captured
```

### 3. Milestone Tracker (03-milestones.md)

```markdown
# Project Milestones

## All Milestones (Chronological)

### M-{id}: {Milestone Name}
**Date**: {target date}
**Phase**: {which phase}
**Status**: {🎯 Upcoming | 🔄 In Progress | ✅ Complete | ⚠️ At Risk | 🚫 Missed}

**Significance**: {Why this milestone matters}

**Deliverables**:
- {Deliverable 1}
- {Deliverable 2}

**Dependencies**:
- {What must complete before this}

**Tasks**:
- [ ] T-{id}: {Task contributing to milestone}
- [ ] T-{id}: {Another task}

**Verification**:
- {How to confirm milestone achieved}

**Current Status**: {narrative update}

---

[Repeat for each milestone]

## Milestone Timeline

```
Jan 2025        Feb 2025        Mar 2025        Apr 2025
   |               |               |               |
   M-1 --------→ M-2 ----------→ M-3 ----------→ M-4
  (✅)           (🔄)            (🎯)            (🎯)
```

## Critical Milestones

These milestones have significant dependencies or external constraints:

1. **M-{id}**: {Name}
   - {Why critical}
   - {Impact if missed}

## At-Risk Milestones

### ⚠️ M-{id}: {Name}
**Risk**: {What's threatening this}
**Impact if Missed**: {consequences}
**Recovery Plan**:
1. {Action 1}
2. {Action 2}

## Completed Milestones

### ✅ M-{id}: {Name}
**Completed**: {date}
**Learnings**:
- {What went well}
- {What could improve}
```

### 4. Dependency Map (04-dependencies.md)

```markdown
# Project Dependencies

## Dependency Types

### Technical Dependencies
Dependencies between components, systems, or technologies.

### Team Dependencies
Work that requires coordination between teams/people.

### External Dependencies
Third-party services, vendors, or outside factors.

### Sequential Dependencies
Work that must happen in specific order.

## Dependency Catalog

### D-{id}: {Dependency Name}
**Type**: {Technical | Team | External | Sequential}
**Status**: {✅ Resolved | 🔄 In Progress | ⚠️ Blocked | 📋 Pending}

**What Depends**:
- {Task/Phase A} needs this

**Depends On**:
- {Task/Phase B} must complete first

**Description**:
{Why this dependency exists}

**Resolution Plan**:
- [ ] {Action to resolve}
- **Target**: {date}
- **Owner**: {responsible party}

**Impact if Unresolved**:
- {What gets blocked}
- {Timeline impact}

**Workaround**:
{Alternative approach if dependency can't be resolved}

---

[Repeat for each dependency]

## Dependency Chains

### Chain 1: {Feature/Capability Name}
```
D-1 (Foundation)
  ↓
D-2 (Core Logic) ← D-3 (Config)
  ↓
D-4 (UI)
  ↓
D-5 (Testing)
```

**Critical Path**: {Longest chain duration}
**Bottleneck**: {D-X is slowest/riskiest}

## Blocking Issues

### Current Blockers
- **D-{id}**: {Name} - blocking {count} tasks
  - {Status/update}
  - {Action needed}

### Resolved Blockers
- **D-{id}**: {Name} - resolved {date}
  - {How it was resolved}

## Dependency Health Dashboard

| Priority | Total | Resolved | In Progress | Blocked | Pending |
|----------|-------|----------|-------------|---------|---------|
| Critical | {#}   | {#}      | {#}         | {#}     | {#}     |
| High     | {#}   | {#}      | {#}         | {#}     | {#}     |
| Medium   | {#}   | {#}      | {#}         | {#}     | {#}     |
```

### 5. Risk & Mitigation (05-risk-mitigation.md)

```markdown
# Risk Management

## Risk Assessment

### R-{id}: {Risk Title}
**Category**: {Technical | Schedule | Resource | External | Business}
**Probability**: {High (>60%) | Medium (30-60%) | Low (<30%)}
**Impact**: {High | Medium | Low}
**Priority**: {P0 | P1 | P2 | P3}

**Description**:
{What could go wrong}

**Indicators** (early warning signs):
- {Signal 1 that risk is materializing}
- {Signal 2}

**Impact**:
- **Timeline**: {delay estimate}
- **Quality**: {quality impact}
- **Scope**: {feature impact}
- **Cost**: {resource impact}

**Mitigation Strategy** (prevent risk):
- [ ] {Proactive action 1}
- [ ] {Proactive action 2}

**Contingency Plan** (if risk occurs):
1. {Immediate action}
2. {Recovery step}
3. {Alternative approach}

**Owner**: {who monitors this risk}
**Review Cadence**: {how often assessed}

**Status Updates**:
- {Date}: {What's changed}

---

[Repeat for each risk]

## Risk Matrix

| Risk | Probability | Impact | Priority | Status |
|------|-------------|--------|----------|--------|
| R-1  | High        | High   | P0       | 🔄 Monitoring |
| R-2  | Medium      | High   | P1       | ✅ Mitigated |
| ...  | ...         | ...    | ...      | ... |

## Top Risks (Probability × Impact)

1. **R-{id}**: {Name} - {P × I score}
2. **R-{id}**: {Name} - {P × I score}
3. **R-{id}**: {Name} - {P × I score}

## Materialized Risks (Issues)

### Issue I-{id}: {Title}
**Originally**: Risk R-{id}
**Occurred**: {date}
**Response**:
- {What we did}
- {Current status}
- {Resolution plan}
```

## Roadmap Analysis Patterns

### Extracting Timeline Information

Look for:
- Explicit dates: "January 2025", "Q2 2025"
- Relative timings: "after Phase 1", "before launch"
- Duration estimates: "2 weeks", "1 month"
- Checkboxes with status indicators
- Completed vs planned work markers

### Identifying Dependencies

Phrases that indicate dependencies:
- "depends on", "requires", "needs"
- "after", "before", "following"
- "blocks", "blocked by"
- "prerequisite", "foundation for"
- Numbered phases (implies sequence)

### Assessing Complexity

**Simple phases**:
- Few dependencies
- Well-defined scope
- Standard work
- Short duration

**Complex phases**:
- Many dependencies
- Unclear scope
- Novel work
- Long duration
- High risk

### Priority Extraction

Indicators of priority:
- Phase numbering (Phase 1 > Phase 2)
- Explicit labels: "Critical", "Must have"
- "MVP", "Launch blocker"
- Current status (in progress = high priority)
- Dependencies (many dependents = high priority)
