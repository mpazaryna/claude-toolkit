# {TASK_ID}: {TITLE}

**Status**: 🔄 In Progress
**Created**: {DATE}
**Last Updated**: {DATE}
**Type**: Research
**Priority**: {PRIORITY}
**Effort**: {EFFORT}

---

## Context

### From Parent Breakdown
**Source**: `{BREAKDOWN_DIR}/99-next-steps.md#{TASK_ID}`

{EXTRACTED_CONTEXT}

### Why This Research Matters
{WHY_MATTERS}

### What Depends on This
{BLOCKS_TASKS}

---

## Research Questions

### Primary Questions
1. {QUESTION_1}
2. {QUESTION_2}
3. {QUESTION_3}

### Secondary Questions
- {QUESTION_A}
- {QUESTION_B}

---

## Research Plan

### Approach
{SUGGESTED_APPROACH}

### Information Sources
- [ ] {SOURCE_1} (e.g., Official documentation)
- [ ] {SOURCE_2} (e.g., API reference)
- [ ] {SOURCE_3} (e.g., Community examples)
- [ ] {SOURCE_4} (e.g., Performance benchmarks)

### Success Criteria
Research is complete when:
- [ ] All primary questions answered
- [ ] Proof-of-concept validated (if applicable)
- [ ] Recommendation documented
- [ ] Findings shared with team

---

## Findings

### {TOPIC_1}

#### Summary
{HIGH_LEVEL_FINDINGS}

#### Details
{DETAILED_FINDINGS}

**Source**: {URL_OR_REFERENCE}
**Date Reviewed**: {DATE}
**Key Takeaways**:
- {TAKEAWAY_1}
- {TAKEAWAY_2}
- {TAKEAWAY_3}

**Code Example** (if applicable):
```{language}
{CODE_SNIPPET}
```

**Caveats/Limitations**:
- {LIMITATION_1}
- {LIMITATION_2}

---

### {TOPIC_2}

[Same structure as Topic 1]

---

### {TOPIC_3}

[Same structure]

---

## Proof of Concept

### Objective
{WHAT_TO_VALIDATE}

### Setup
```bash
{SETUP_COMMANDS}
```

### Code
```{language}
{POC_CODE}
```

### Results
{WHAT_HAPPENED}

**Performance**:
- {METRIC_1}: {value}
- {METRIC_2}: {value}

**Observations**:
- {OBSERVATION_1}
- {OBSERVATION_2}

**Verdict**: ✅ Viable | ⚠️ Needs Work | ❌ Not Feasible

---

## Comparison Matrix

If evaluating multiple options:

| Feature | {Option A} | {Option B} | {Option C} |
|---------|-----------|-----------|-----------|
| {Feature 1} | {value} | {value} | {value} |
| {Feature 2} | {value} | {value} | {value} |
| {Feature 3} | {value} | {value} | {value} |
| **Pros** | {list} | {list} | {list} |
| **Cons** | {list} | {list} | {list} |

---

## Recommendations

### Recommended Approach
{WHAT_TO_DO}

### Rationale
{WHY_THIS_APPROACH}

### Implementation Considerations
1. {CONSIDERATION_1}
2. {CONSIDERATION_2}
3. {CONSIDERATION_3}

### Risks & Mitigation
- **Risk**: {RISK_1}
  - **Mitigation**: {HOW_TO_MITIGATE}
- **Risk**: {RISK_2}
  - **Mitigation**: {HOW_TO_MITIGATE}

### Alternative Approaches
If recommended approach doesn't work:
1. {ALTERNATIVE_1}: {when to use}
2. {ALTERNATIVE_2}: {when to use}

---

## Open Questions

Questions that remain unanswered:
- [ ] {OPEN_QUESTION_1}
- [ ] {OPEN_QUESTION_2}

**Impact if unresolved**: {LOW/MEDIUM/HIGH}

**Next steps for resolution**:
- {STEP_1}
- {STEP_2}

---

## References

### Documentation
- [{Title}]({URL}) - {brief description}
- [{Title}]({URL}) - {brief description}

### Articles/Tutorials
- [{Title}]({URL}) - {brief description}
- [{Title}]({URL}) - {brief description}

### Code Examples
- [{Title}]({URL}) - {brief description}
- [{Title}]({URL}) - {brief description}

### Related Issues/Discussions
- [{Title}]({URL}) - {brief description}

---

## Impact Analysis

### Files to Update
Based on research findings:
- [ ] `{FILE_1}` - {what to add/change}
- [ ] `{FILE_2}` - {what to add/change}
- [ ] `{BREAKDOWN_DIR}/99-next-steps.md` - Mark {TASK_ID} complete

### New Tasks Created
Research revealed additional work needed:
- {NEW_TASK_1}
- {NEW_TASK_2}

### Tasks Unblocked
- {UNBLOCKED_TASK_1}
- {UNBLOCKED_TASK_2}

---

## Timeline Impact

**Original Estimate**: {EFFORT}
**Actual Effort**: {ACTUAL_TIME_SPENT}

**Findings Impact on Schedule**:
- {IMPACT_1}
- {IMPACT_2}

---

## GitHub Issue Ready

```markdown
# {TITLE}

**Type**: Research
**Priority**: {PRIORITY}
**Estimate**: {EFFORT}

## Research Questions
1. {QUESTION_1}
2. {QUESTION_2}

## Findings Summary
{BRIEF_SUMMARY_OF_KEY_FINDINGS}

## Recommendation
{ONE_LINE_RECOMMENDATION}

## See Full Research
Link to this file or paste relevant sections

## Acceptance Criteria
- [ ] All primary questions answered
- [ ] Proof-of-concept completed (if applicable)
- [ ] Recommendation documented
- [ ] Implementation approach validated
```

---

## Notes

- Update findings as you research
- Add code snippets and examples
- Link to external resources
- Document dead-ends (what didn't work)
- Run `/paz:plan:sync` when complete to update parent breakdown
