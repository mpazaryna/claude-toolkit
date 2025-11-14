---
name: Technical Decision Analysis
description: Analyze technical options with structured comparison, scoring, and ADR generation. Use when making technology choices, architecture decisions, or evaluating implementation approaches.
---

# Technical Decision Analysis

## Instructions

When you invoke this skill, I will help you make evidence-based technical decisions by:

1. **Understanding Context**: What needs to be decided and why it matters
2. **Defining Criteria**: Establish evaluation framework based on decision type
3. **Researching Options**: Gather facts, benchmarks, and real-world usage
4. **Scoring & Comparing**: Create weighted comparison matrix
5. **Generating Recommendation**: Provide clear choice with rationale and tradeoffs
6. **Creating ADR**: Draft Architecture Decision Record for documentation

## Decision Types

**Technology Selection** (e.g., database, framework, library):
- Maturity/stability, Performance, Developer experience
- Documentation/community, Future-proofing, Migration path

**Architecture Decision** (e.g., sync strategy, API design):
- Complexity, Maintainability, Scalability
- User experience, Cost implications

**Implementation Approach** (e.g., how to build feature):
- Time to implement, Code quality, Testability, Flexibility

## Output Format

I will provide:
- Structured analysis of each option (pros, cons, tradeoffs, risks)
- Comparison matrix with weighted scores
- Clear recommendation with rationale
- ADR draft ready to save
- Implementation notes and references

## Best Practices

- Evidence-based: Backed by research and data
- Context-aware: Consider your project constraints
- Explicit about tradeoffs: No option is perfect
- Reversibility-aware: Note if/how decision can change
- Validated: Include how to verify correctness

## Usage

Simply describe your decision:
- "Should I use SwiftData or CoreData for persistence?"
- "Evaluate REST vs GraphQL for our API"
- "Compare authentication approaches: JWT vs sessions"

I'll research options, analyze tradeoffs, and provide a structured recommendation.
