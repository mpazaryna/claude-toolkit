# {TASK_ID}: {TITLE}

**Status**: 🔄 In Progress
**Created**: {DATE}
**Last Updated**: {DATE}
**Type**: Implementation
**Priority**: {PRIORITY}
**Effort**: {EFFORT}

---

## Context

### From Parent Breakdown
**Source**: `{BREAKDOWN_DIR}/99-next-steps.md#{TASK_ID}`

{EXTRACTED_CONTEXT}

### Why This Work Matters
{WHY_MATTERS}

### Dependencies
**Requires**:
{DEPENDS_ON}

**Enables**:
{BLOCKS_TASKS}

---

## Requirements

### Functional Requirements
- [ ] {REQ_1}
- [ ] {REQ_2}
- [ ] {REQ_3}

### Non-Functional Requirements
- **Performance**: {PERFORMANCE_TARGET}
- **Security**: {SECURITY_REQUIREMENTS}
- **Compatibility**: {COMPATIBILITY_REQUIREMENTS}
- **Maintainability**: {MAINTAINABILITY_NOTES}

### Acceptance Criteria
This task is complete when:
- [ ] {CRITERION_1}
- [ ] {CRITERION_2}
- [ ] {CRITERION_3}
- [ ] Tests passing
- [ ] Code reviewed
- [ ] Documentation updated

---

## Technical Approach

### Architecture
{HIGH_LEVEL_DESIGN}

### Components Involved
- **{COMPONENT_1}**: {role and changes}
- **{COMPONENT_2}**: {role and changes}
- **{COMPONENT_3}**: {role and changes}

### Data Models
{DATA_MODEL_CHANGES}

### APIs/Interfaces
{API_CHANGES}

---

## Implementation Plan

### Phase 1: Setup
- [ ] {SETUP_TASK_1}
- [ ] {SETUP_TASK_2}
- [ ] {SETUP_TASK_3}

**Estimated Time**: {TIME}

### Phase 2: Core Implementation
- [ ] {IMPL_TASK_1}
- [ ] {IMPL_TASK_2}
- [ ] {IMPL_TASK_3}
- [ ] {IMPL_TASK_4}

**Estimated Time**: {TIME}

### Phase 3: Integration
- [ ] {INTEGRATION_TASK_1}
- [ ] {INTEGRATION_TASK_2}
- [ ] {INTEGRATION_TASK_3}

**Estimated Time**: {TIME}

### Phase 4: Testing & Polish
- [ ] {TEST_TASK_1}
- [ ] {TEST_TASK_2}
- [ ] {TEST_TASK_3}
- [ ] {POLISH_TASK_1}

**Estimated Time**: {TIME}

---

## File Changes

### New Files
- `{NEW_FILE_1}` - {purpose}
- `{NEW_FILE_2}` - {purpose}

### Modified Files
- `{MODIFIED_FILE_1}` - {what changes}
- `{MODIFIED_FILE_2}` - {what changes}

### Deleted Files (if any)
- `{DELETED_FILE}` - {why removed}

---

## Code Snippets

### {Component/Feature Name}

**File**: `{FILE_PATH}`

```{language}
{CODE_IMPLEMENTATION}
```

**Notes**:
- {NOTE_1}
- {NOTE_2}

---

## Testing Strategy

### Unit Tests

**File**: `{TEST_FILE}`

Test cases:
- [ ] {TEST_CASE_1}
- [ ] {TEST_CASE_2}
- [ ] {TEST_CASE_3}

**Coverage Target**: {PERCENTAGE}%

### Integration Tests
- [ ] {INTEGRATION_TEST_1}
- [ ] {INTEGRATION_TEST_2}

### Manual Testing
Steps to verify:
1. {MANUAL_STEP_1}
2. {MANUAL_STEP_2}
3. {MANUAL_STEP_3}

**Expected Result**: {WHAT_SHOULD_HAPPEN}

### Edge Cases
- [ ] {EDGE_CASE_1}
- [ ] {EDGE_CASE_2}
- [ ] {EDGE_CASE_3}

---

## Dependencies & Integration

### External Dependencies
- **{LIBRARY/SERVICE}**: {version/config}
  - Installation: `{INSTALL_COMMAND}`
  - Configuration: {CONFIG_NOTES}

### Internal Dependencies
Must complete these first:
- {TASK_ID}: {TASK_TITLE} - {STATUS}

### Integration Points
- **{SYSTEM_A} → {SYSTEM_B}**: {how they connect}
- **{SYSTEM_C}**: {integration details}

---

## Progress Log

### {DATE}: {Milestone/Update}
{WHAT_WAS_DONE}

**Completed**:
- {ITEM_1}
- {ITEM_2}

**Blockers**:
- {BLOCKER_1} - {status/resolution}

**Next Steps**:
- {NEXT_1}
- {NEXT_2}

---

[Add more entries as work progresses]

---

## Risks & Issues

### {RISK/ISSUE_1}
**Type**: Risk | Blocker | Issue
**Impact**: High | Medium | Low
**Status**: Open | Mitigated | Resolved

**Description**: {DETAILS}

**Mitigation/Resolution**:
{HOW_HANDLED}

---

## Documentation

### User Documentation
- [ ] Update `{DOC_FILE}` with {new feature}
- [ ] Add usage examples
- [ ] Update screenshots/diagrams

### Developer Documentation
- [ ] Add inline code comments
- [ ] Update `{TECHNICAL_DOC}` with architecture changes
- [ ] Document any gotchas or edge cases

### API Documentation
- [ ] Document new endpoints/methods
- [ ] Update API reference
- [ ] Add request/response examples

---

## Review Checklist

Before marking complete:

### Code Quality
- [ ] Code follows project style guide
- [ ] No linting errors
- [ ] No compiler warnings
- [ ] Comments added for complex logic
- [ ] Dead code removed

### Testing
- [ ] All tests passing
- [ ] New tests added for new functionality
- [ ] Edge cases covered
- [ ] Manual testing completed

### Documentation
- [ ] User docs updated
- [ ] Developer docs updated
- [ ] API docs updated (if applicable)
- [ ] CHANGELOG updated

### Integration
- [ ] Works with existing features
- [ ] No breaking changes (or documented)
- [ ] Performance acceptable
- [ ] Error handling comprehensive

### Review
- [ ] Code review requested
- [ ] Feedback addressed
- [ ] Approved by {REVIEWER}

---

## Deployment Notes

### Prerequisites
{DEPLOYMENT_PREREQUISITES}

### Deployment Steps
1. {STEP_1}
2. {STEP_2}
3. {STEP_3}

### Rollback Plan
If issues arise:
1. {ROLLBACK_STEP_1}
2. {ROLLBACK_STEP_2}

### Monitoring
After deployment, watch:
- {METRIC_1}
- {METRIC_2}

---

## GitHub Issue Ready

```markdown
# {TITLE}

**Type**: Implementation
**Priority**: {PRIORITY}
**Estimate**: {EFFORT}

## Description
{BRIEF_DESCRIPTION}

## Requirements
- {REQ_1}
- {REQ_2}

## Technical Approach
{ONE_PARAGRAPH_SUMMARY}

## Acceptance Criteria
- [ ] {CRITERION_1}
- [ ] {CRITERION_2}
- [ ] Tests passing

## See Full Plan
Link to this file

## Depends On
- {DEPENDENCY_TASK}

## Blocks
- {BLOCKED_TASK}
```

---

## Notes

- Update progress log as you work
- Check off implementation plan items
- Document any deviations from plan
- Run `/paz:plan:sync` when complete to update parent breakdown
