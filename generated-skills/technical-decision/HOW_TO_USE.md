# How to Use the Technical Decision Analysis Skill

## Quick Start

Ask technical decision questions directly:

```
"Should I use PostgreSQL or MongoDB?"
"Evaluate REST vs GraphQL for our API"
"Compare authentication: JWT vs sessions vs OAuth"
```

## What This Skill Does

The Technical Decision Analysis skill provides systematic, evidence-based guidance for technology choices. It:
- Researches options thoroughly using web sources
- Scores options against relevant criteria
- Provides clear recommendations with rationale
- Documents decisions as ADRs
- Notes tradeoffs and risks explicitly

## Usage Patterns

### Pattern 1: Simple Technology Choice

**When**: Choosing between specific technologies

```
User: "Should I use SwiftData or CoreData for iOS persistence?"

Skill: [Provides structured analysis]

## Decision Analysis: iOS Persistence Layer

### Context
Choosing persistence layer for iOS app impacts:
- Development speed and maintainability
- Performance and memory usage
- iOS version compatibility
- Future flexibility

### Options Evaluated

#### Option 1: SwiftData
**Description**: Modern Swift-first persistence framework (iOS 17+)

**Pros**:
- Native Swift syntax, no NSManagedObject boilerplate
- Automatic @Model macro reduces code
- Better type safety
- Modern async/await support
- Easier to learn for Swift developers

**Cons**:
- iOS 17+ only (limits deployment targets)
- Less mature, fewer production battle-tests
- Smaller community and fewer Stack Overflow answers
- Migration from CoreData requires rewrite

**Best For**: New iOS 17+ projects, Swift-focused teams

**Score**: 3.8/5

---

#### Option 2: CoreData
**Description**: Mature object graph persistence framework (iOS 3+)

**Pros**:
- Battle-tested since 2009
- Extensive documentation and community knowledge
- Works on older iOS versions
- Proven performance at scale
- Rich migration tooling

**Cons**:
- Verbose Objective-C heritage
- Steep learning curve
- More boilerplate code
- Manual thread management complexity

**Best For**: Apps supporting iOS < 17, large existing codebases

**Score**: 3.5/5

---

### Comparison Matrix

| Criterion | Weight | SwiftData | CoreData |
|-----------|--------|-----------|----------|
| Modern syntax | High | 5/5 | 2/5 |
| Maturity | High | 2/5 | 5/5 |
| Performance | Medium | 4/5 | 5/5 |
| Community support | Medium | 2/5 | 5/5 |
| iOS compatibility | High | 3/5 | 5/5 |

### Recommendation

**Selected**: CoreData

**Rationale**:
While SwiftData offers superior developer experience, CoreData's maturity and broader iOS compatibility make it safer for production use.

Key factors:
1. **iOS Compatibility**: SwiftData's iOS 17+ requirement excludes ~40% of users
2. **Production Stability**: CoreData's 14-year track record reduces risk
3. **Community Support**: Easier to find solutions to problems

**Tradeoffs Accepted**:
- More boilerplate code: We accept because reliability > convenience
- Steeper learning curve: Mitigated by extensive documentation

**Risks**:
- Team frustration with verbose syntax: Mitigate with code generation tools
- SwiftData becomes standard: Plan migration in 2026 when iOS 17 dominates

**Validation**:
- Prototype with 5 complex models
- Test migration scenarios
- Verify performance with realistic data

**Reversibility**: Difficult (3-5 week migration)

### ADR Draft

```markdown
# ADR-001: CoreData for Persistence Layer

**Status**: Proposed
**Date**: 2025-11-14

**Context**:
Need persistence layer for iOS app with 30+ data models. Team has
moderate iOS experience. Must support iOS 15+.

**Decision**:
We will use CoreData for our persistence layer.

**Rationale**:
- iOS 15+ compatibility required (SwiftData needs iOS 17+)
- Proven stability for production apps
- Extensive community resources for troubleshooting
- Team can learn from abundant documentation

**Consequences**:
- Positive: Stable, proven, wide iOS support
- Negative: More boilerplate than SwiftData
- Neutral: Industry standard approach

**Alternatives Considered**:
- SwiftData: Rejected due to iOS 17+ requirement
- Realm: Rejected due to third-party dependency
```

### Implementation Notes

1. Set up CoreData stack with NSPersistentContainer
2. Create .xcdatamodeld file for schema
3. Use lightweight migrations for schema changes
4. Implement background context for imports
5. Add unit tests for model layer

### References

- [CoreData Programming Guide](https://developer.apple.com/documentation/coredata)
- [Performance Best Practices](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/Performance.html)
- [SwiftData vs CoreData Comparison](https://www.hackingwithswift.com/quick-start/swiftdata)
```

### Pattern 2: Architecture Decision

**When**: Making structural or design choices

```
User: "How should we handle offline sync: optimistic or pessimistic?"

Skill: [Analyzes sync strategies]

## Decision Analysis: Offline Sync Strategy

### Context
Choosing sync strategy impacts:
- User experience during poor connectivity
- Conflict resolution complexity
- Data consistency guarantees
- Implementation effort

[... detailed analysis of each approach ...]

### Recommendation

**Selected**: Optimistic with Conflict Resolution

**Rationale**:
Better UX (immediate feedback) outweighs conflict complexity for our use case.

**Tradeoffs Accepted**:
- Must handle conflicts: Accept because conflicts rare in single-user app
- More complex testing: Mitigate with conflict simulation framework

[... complete ADR and implementation guidance ...]
```

### Pattern 3: Multiple Options Comparison

**When**: Evaluating 3+ alternatives

```
User: "Compare these frontend frameworks: React, Vue, Svelte, Solid"

Skill: [Comprehensive comparison]

## Decision Analysis: Frontend Framework Selection

### Options Evaluated

#### Option 1: React
[Full analysis]

#### Option 2: Vue
[Full analysis]

#### Option 3: Svelte
[Full analysis]

#### Option 4: Solid
[Full analysis]

### Comparison Matrix

| Criterion | Weight | React | Vue | Svelte | Solid |
|-----------|--------|-------|-----|--------|-------|
| Ecosystem size | High | 5/5 | 4/5 | 3/5 | 2/5 |
| Performance | High | 3/5 | 4/5 | 5/5 | 5/5 |
| Learning curve | Medium | 3/5 | 4/5 | 5/5 | 3/5 |
| Job market | Low | 5/5 | 4/5 | 2/5 | 1/5 |
| DX | Medium | 4/5 | 5/5 | 5/5 | 4/5 |

### Recommendation

**Selected**: Vue

**Rationale**:
Balances React's ecosystem with better DX and performance.
[... detailed reasoning ...]
```

### Pattern 4: With Custom Criteria

**When**: You have specific evaluation needs

```
User: "Compare AWS Lambda vs EC2 for our backend.
Criteria: cost at scale, cold start latency, debugging experience, vendor lock-in."

Skill: [Uses provided criteria]

### Comparison Matrix

| Criterion | Weight | Lambda | EC2 |
|-----------|--------|--------|-----|
| Cost at scale | High | 4/5 | 3/5 |
| Cold start latency | High | 2/5 | 5/5 |
| Debugging experience | Medium | 2/5 | 4/5 |
| Vendor lock-in | Medium | 2/5 | 4/5 |

[... analysis using your criteria ...]
```

### Pattern 5: Decision Validation

**When**: Validating an existing choice

```
User: "We chose MongoDB. Can you validate this was the right choice?
Context: High write volume, flexible schema, document-oriented data."

Skill: [Analyzes context and validates]

## Decision Validation: MongoDB Selection

### Context Alignment
✅ High write volume → MongoDB's write performance advantage
✅ Flexible schema → Document model fits well
✅ Document-oriented → Natural fit for MongoDB

### Risks to Monitor
⚠️ Join complexity if relationships increase
⚠️ Transaction requirements (MongoDB 4.0+ needed)

### Recommendation
**Status**: VALIDATED

Your choice aligns well with stated requirements. MongoDB is appropriate for this use case.

**Watch for**:
- If relational queries increase → Consider adding read replicas
- If ACID transactions needed → Ensure MongoDB 4.0+ with replica sets
```

## Decision Quality Principles

### Good Decisions Are

1. **Evidence-Based**
   - Research actual performance benchmarks
   - Find real-world usage examples
   - Cite documentation and case studies

2. **Context-Aware**
   - Consider team expertise
   - Account for project timeline
   - Factor in budget constraints
   - Respect deployment targets

3. **Explicit About Tradeoffs**
   - Every option has downsides
   - State what you're accepting
   - Explain why tradeoffs are acceptable

4. **Reversible-Aware**
   - Can you change later?
   - How hard would migration be?
   - Prefer reversible choices when uncertain

5. **Validated**
   - How will you know if decision was right?
   - What metrics confirm success?
   - When should you revisit?

### What to Avoid

❌ **Personal Preference Alone**
"I like React" → Not sufficient rationale

❌ **Ignoring Context**
"X worked for Google" → Your context differs

❌ **Hiding Tradeoffs**
Every choice has downsides; acknowledge them

❌ **Ignoring Reversibility**
How hard is it to change this later?

❌ **Not Considering Team**
Can your team actually use this technology?

### When Uncertain

The skill will:
- Admit when evidence is insufficient
- Suggest proof-of-concept to validate
- Recommend more reversible option
- Flag need for expert consultation

## Advanced Usage

### Building Decision History

```bash
# Save ADRs for reference
mkdir -p docs/decisions
# Copy generated ADRs
# Review periodically to learn patterns
```

### Combining with Research Skill

```bash
# First: Research technologies
"Research Next.js App Router in depth"

# Then: Make decision using research
"Using the Next.js research, compare Next.js vs Remix"
```

### Progressive Refinement

```bash
# Start broad
"Compare SQL vs NoSQL databases"

# Get recommendation
# Narrow down

# Go specific
"Compare PostgreSQL vs MySQL for our use case"
```

## Tips for Best Results

1. **Provide Context**: Share constraints, team size, timeline
2. **State Priorities**: What matters most for your project?
3. **Be Specific**: "User authentication" vs "OAuth for SaaS app"
4. **Question Results**: Ask "why" to understand rationale
5. **Save ADRs**: Build institutional knowledge

## Common Questions

**Q: How does the skill research options?**
A: Uses WebFetch and WebSearch to gather documentation, benchmarks, and real-world usage examples.

**Q: Can I override the recommendation?**
A: Absolutely. The skill provides analysis; you make the final call.

**Q: What if the comparison seems biased?**
A: Request "Provide counterarguments for [option]" or "What's the best case for [alternative]?"

**Q: How accurate are the scores?**
A: Scores are estimates based on research. Use as guidance, not absolute truth.

**Q: Should I always follow the recommendation?**
A: No. Consider it expert advice, but you know your context best.

## Related Skills

- **research-agent** - Gather in-depth documentation before deciding
- **commit-helper** - Document decision in commit message
- **code-reviewer** - Validate implementation matches decision

---

Generated by Claude Code Skills Factory
