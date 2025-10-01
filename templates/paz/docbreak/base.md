# Base Document Breakdown Template

This template provides the foundation for all document breakdown operations.

## Standard Sections to Extract

### 1. Overview
- Project/feature name
- Purpose and goals
- Target users/audience
- Success criteria

### 2. Scope Definition
- What's included
- What's explicitly excluded
- Boundaries and limitations
- Integration points

### 3. Requirements
- Functional requirements
- Non-functional requirements
- Constraints
- Assumptions

### 4. Dependencies
- Technical dependencies
- Team dependencies
- External dependencies
- Prerequisite work

### 5. Open Questions
- Unresolved decisions
- Areas needing research
- Stakeholder input needed
- Risk factors

### 6. Timeline Indicators
- Explicit dates/deadlines
- Relative timeframes (Q1, Q2, etc.)
- Priority markers (P0, P1, etc.)
- Phase identifiers

## Standard Artifact Structure

### Index Document (00-index.md)
```markdown
# {Document Name} - Breakdown Index

**Source**: {original document path}
**Generated**: {timestamp}
**Type**: {document type}

## Navigation

### Planning Artifacts
{List of generated planning documents with brief descriptions}

### Quick Links
- [Next Steps](99-next-steps.md) - Start here
- [Open Questions](XX-open-questions.md) - Needs decisions
- [Dependencies](XX-dependencies.md) - Prerequisites

## How to Use This Breakdown

1. **Start with context**: Read this index and source document
2. **Review next steps**: Check `99-next-steps.md` for immediate actions
3. **Deep dive**: Read relevant planning artifacts as needed
4. **Track progress**: Update artifacts as work completes
5. **Adapt**: Re-run breakdown when major changes occur

## Document Map

{Visual tree or table showing relationships between artifacts}
```

### Next Steps Document (99-next-steps.md)
```markdown
# Immediate Next Steps

> Prioritized actionable tasks extracted from breakdown

## Priority 1: Start Immediately

### Task 1.1: {Title}
- **Why**: {Context/rationale}
- **What**: {Specific action}
- **Done when**: {Acceptance criteria}
- **Effort**: {small/medium/large}
- **See**: {Link to detailed artifact}

### Task 1.2: {Title}
[Same structure]

## Priority 2: Start After P1

### Task 2.1: {Title}
- **Blocked by**: {P1 task or external dependency}
[Same structure as above]

## Priority 3: Research/Investigation

### Research 3.1: {Title}
- **Question**: {What needs answering}
- **Why it matters**: {Impact on project}
- **Approach**: {Suggested research method}
- **Deadline**: {When decision needed}

## Priority 4: Review/Approval Needed

### Review 4.1: {Title}
- **Needs input from**: {Stakeholder/team}
- **Decision**: {What needs to be decided}
- **Impact**: {What depends on this}

## Task Dependencies

{Optional: Visual graph or list showing task relationships}
```

## Extraction Patterns

### Identifying Actionable Items

Look for these patterns:
- `[ ]` or `[x]` - Explicit checkboxes
- `TODO:` or `FIXME:` - Code-style markers
- `# Phase N:` - Roadmap phases
- Imperative verbs: "Implement", "Create", "Build", "Design"
- Questions ending with `?` - May need research tasks
- `TBD` or `To be determined` - Decision tasks

### Categorizing Complexity

**Small** (< 1 day):
- Single file changes
- Configuration updates
- Documentation updates
- Simple bug fixes

**Medium** (1-3 days):
- New component/module
- API endpoint implementation
- Database schema updates
- Integration tasks

**Large** (> 3 days):
- New features
- Architectural changes
- Major refactoring
- Multi-system integration

### Extracting Context

For each task, capture:
1. **Where it came from** (section/page of source doc)
2. **Why it exists** (goal it serves)
3. **What comes before** (dependencies)
4. **What comes after** (what it enables)
5. **How to verify** (acceptance criteria)

## Quality Checklist

Before completing breakdown:
- [ ] All source document sections analyzed
- [ ] Every checkbox/TODO extracted
- [ ] Dependencies mapped
- [ ] Open questions identified
- [ ] Timeline information captured
- [ ] Index document created
- [ ] Next steps prioritized
- [ ] Cross-references validated
- [ ] Acceptance criteria defined
- [ ] Effort estimates provided
