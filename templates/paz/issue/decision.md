# {TASK_ID}: {TITLE}

**Status**: 🔄 In Progress
**Created**: {DATE}
**Last Updated**: {DATE}
**Type**: Decision
**Priority**: {PRIORITY}
**Effort**: {EFFORT}

---

## Context

### From Parent Breakdown
**Source**: `{BREAKDOWN_DIR}/99-next-steps.md#{TASK_ID}`

{EXTRACTED_CONTEXT}

### Why This Decision Matters
{WHY_MATTERS}

### What's Blocked
{BLOCKS_TASKS}

---

## Decision Framework

### Problem Statement
{PROBLEM_STATEMENT}

### Decision Criteria
What matters most for this decision:
1. {CRITERION_1}
2. {CRITERION_2}
3. {CRITERION_3}

### Options Analysis

{COMPARISON_MATRIX}

#### Option 1: {OPTION_1_NAME}

**Description**: {DESCRIPTION}

**Pros**:
- {PRO_1}
- {PRO_2}
- {PRO_3}

**Cons**:
- {CON_1}
- {CON_2}

**Effort**: {EFFORT_ESTIMATE}

**Risk**: {RISK_LEVEL}
- {RISK_DETAILS}

**Score vs Criteria**:
- Criterion 1: {SCORE}/5
- Criterion 2: {SCORE}/5
- Criterion 3: {SCORE}/5

---

#### Option 2: {OPTION_2_NAME}

[Same structure as Option 1]

---

#### Option 3: {OPTION_3_NAME} (if applicable)

[Same structure]

---

### Comparison Matrix

| Criterion | Weight | Option 1 | Option 2 | Option 3 |
|-----------|--------|----------|----------|----------|
| {Criterion 1} | {high/med/low} | {score} | {score} | {score} |
| {Criterion 2} | {high/med/low} | {score} | {score} | {score} |
| {Criterion 3} | {high/med/low} | {score} | {score} | {score} |
| **Total** | | {total} | {total} | {total} |

---

## Research & Investigation

### Questions to Answer
- [ ] {QUESTION_1}
- [ ] {QUESTION_2}
- [ ] {QUESTION_3}

### Research Log

#### {DATE}: {Finding Title}
{FINDINGS}

**Source**: {URL or reference}
**Relevance**: {How this impacts the decision}

---

[Add more research entries as you investigate]

---

## Recommendation

### Selected Option
**Choice**: {SELECTED_OPTION}

### Rationale
{WHY_THIS_OPTION}

Key factors:
1. {FACTOR_1}
2. {FACTOR_2}
3. {FACTOR_3}

### Tradeoffs Accepted
- {TRADEOFF_1}: We accept this because {reason}
- {TRADEOFF_2}: We accept this because {reason}

### Implementation Notes
{NOTES_FOR_IMPLEMENTATION}

---

## Architecture Decision Record (ADR)

### ADR-{NUMBER}: {TITLE}

**Status**: Proposed | Accepted | Deprecated
**Date**: {DECISION_DATE}
**Deciders**: {WHO_DECIDED}

**Context**:
{BACKGROUND_AND_CONTEXT}

**Decision**:
We will {DECISION_STATEMENT}.

**Consequences**:
- **Positive**: {BENEFITS}
- **Negative**: {DRAWBACKS}
- **Neutral**: {OTHER_EFFECTS}

**Alternatives Considered**:
- {OPTION_A}: Rejected because {reason}
- {OPTION_B}: Rejected because {reason}

---

## Impact Analysis

### Files to Update
- [ ] `{FILE_1}` - {what to change}
- [ ] `{FILE_2}` - {what to change}
- [ ] Parent: `{BREAKDOWN_DIR}/99-next-steps.md` - Mark {TASK_ID} complete
- [ ] Architecture: `{BREAKDOWN_DIR}/05-architecture-decisions.md` - Add ADR

### Tasks Unblocked
Once this decision is made and documented:
- {UNBLOCKED_TASK_1}
- {UNBLOCKED_TASK_2}
- {UNBLOCKED_TASK_3}

### Downstream Effects
{CASCADING_IMPACTS}

---

## Validation

### How to Verify This Was the Right Decision
- {VALIDATION_1}
- {VALIDATION_2}

### Reversibility
- **Can we change this later?**: {YES/NO}
- **Cost to reverse**: {LOW/MEDIUM/HIGH}
- **When to reconsider**: {TRIGGER_CONDITIONS}

---

## GitHub Issue Ready

```markdown
# {TITLE}

**Type**: Decision
**Priority**: {PRIORITY}
**Estimate**: {EFFORT}

## Problem
{PROBLEM_STATEMENT}

## Options
1. {OPTION_1} - {one-line summary}
2. {OPTION_2} - {one-line summary}

## Recommendation
{SELECTED_OPTION} because {brief rationale}

## See Full Analysis
Link to this file or paste relevant sections

## Acceptance Criteria
- [ ] Decision documented with rationale
- [ ] ADR created and reviewed
- [ ] Impacted files updated
- [ ] Dependent tasks unblocked
```

---

## Notes

- Add research findings as you investigate
- Update status when decision finalized
- Copy ADR section to architecture decisions doc
- Run `/paz:plan:sync` when complete to update parent breakdown
