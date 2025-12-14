# Plan Template: Implementation Plan

Use this template when documenting STEPS to build. Plans are **evolving**—update as work progresses.

---

## Template

```markdown
# {Feature Name} - Implementation Plan

**Project**: {Feature/System Name}
**Status**: {Not Started | In Progress (X% complete) | Complete}
**Owner**: {name}
**Started**: {YYYY-MM-DD}
**Target Completion**: {YYYY-MM-DD}

**Related Documents**:
- **Why**: [ADR-{NNN}](../adr/{NNN}-{feature}.md)
- **How**: [Design Doc](../design/{feature}.md)
- **What**: [Spec](../spec/{feature}.md)
- **Tracking**: [GitHub Issue #{N}]({url})

---

## Current Status

**Completion**: {X%}

### Completed
- {Phase/Task completed}
- {Phase/Task completed}

### In Progress
- {Current work}

### Blocked
- {Blocker description} - {who/what is needed}

### Remaining
- {What's left}

---

## Phase Breakdown

### Phase 0: {Foundation/Setup} {STATUS}

**Goal**: {What this phase achieves}

**Owner**: {name}
**Estimated Time**: {X hours/days}
**Status**: {Not Started | In Progress | Complete}
**Completion Date**: {YYYY-MM-DD if complete}

#### Tasks

- [ ] **{Task 1}**:
  - {Subtask}
  - {Subtask}

- [ ] **{Task 2}**:
  - {Subtask}

#### Success Criteria

- [ ] {How we know this phase is done}
- [ ] {Measurable outcome}

#### Deliverables

- {File/artifact 1}
- {File/artifact 2}

#### Blockers

- {None | Description of blocker}

---

### Phase 1: {Core Implementation} {STATUS}

**Goal**: {What this phase achieves}

**Owner**: {name}
**Estimated Time**: {X hours/days}
**Status**: {Not Started | In Progress | Complete | Blocked by Phase 0}
**Priority**: {High | Medium | Low}

#### Tasks

- [ ] **{Task 1}**:
  {Description}

- [ ] **{Task 2}**:
  {Description}

- [ ] **{Task 3}**:
  {Description}

#### Success Criteria

- [ ] {Criterion 1}
- [ ] {Criterion 2}

#### Deliverables

- {Deliverable 1}
- {Deliverable 2}

#### Blockers

- {Blocked by Phase 0 | None | Description}

---

### Phase 2: {Enhancement/Integration} {STATUS}

{Same structure as Phase 1}

---

### Phase 3: {Polish/Validation} {STATUS}

{Same structure as Phase 1}

---

## Future Phases (Not Yet Planned)

### Phase N: {Future Work}

**Goal**: {High-level goal}
**Status**: Future Work
**Depends on**: Phase {N-1}

**Concept**:
- {Rough idea of what this includes}
- {Will be detailed when earlier phases complete}

---

## Risk & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| {Risk 1} | {High/Med/Low} | {High/Med/Low} | {How to handle} |
| {Risk 2} | {High/Med/Low} | {High/Med/Low} | {How to handle} |

---

## Success Metrics

### Performance
- [ ] {Metric 1}
- [ ] {Metric 2}

### Quality
- [ ] {Metric 1}
- [ ] {Metric 2}

### Developer Experience
- [ ] {Metric 1}

---

## Dependencies

### External Dependencies
- {Dependency 1}: {Status}
- {Dependency 2}: {Status}

### Internal Dependencies
- {Phase X} depends on {Phase Y}
- {Task A} depends on {Task B}

---

## Notes

- {Important note 1}
- {Important note 2}

---

## Updates Log

| Date | Phase | Update |
|------|-------|--------|
| {YYYY-MM-DD} | {Phase} | {What changed} |
| {YYYY-MM-DD} | {Phase} | {What changed} |

---

**Last Updated**: {YYYY-MM-DD} by {name}
```

---

## Key Principles

1. **Evolving**: Update as work progresses
2. **Phase-based**: Break work into sequential phases
3. **Actionable tasks**: Each task is something someone can do
4. **Clear success criteria**: Know when each phase is done
5. **Dependencies explicit**: Show what blocks what
6. **Status tracked**: Current state always visible

## Naming Convention

```
docs/plan/kebab-case-feature-name-implementation.md
```

Examples:
- `composable-agent-implementation.md`
- `auth-system-implementation.md`
- `sync-engine-implementation.md`

## Status Values

**Plan Status**:
- Not Started
- In Progress (X% complete)
- Complete

**Phase Status**:
- Not Started
- In Progress
- Complete
- Blocked by {Phase N}

**Task Status**:
- [ ] Not done
- [x] Done

## Updating the Plan

Update when:
- Phase completes → Mark complete, add completion date
- Blocker found → Add to blockers section
- Task done → Check off task
- Scope changes → Update tasks, note in log
- Timeline shifts → Update estimates, note in log

Always update the Updates Log with what changed.
