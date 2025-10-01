# Technical Specification Breakdown Template

For documents containing code, APIs, data models, and architecture.

## Technical Artifacts to Generate

### 1. Data Models Document (01-data-models.md)

```markdown
# Data Models Implementation Guide

> Extracted from: {source document}

## Overview
- Total models to implement: {count}
- Current status: {implemented/planned}
- Storage technology: {e.g., SwiftData, CoreData, PostgreSQL}

## Models by Priority

### Priority 1: Core Models (Start Here)
Models required for basic functionality.

#### Model: {ModelName}
**Source**: {doc section and line numbers}
**Purpose**: {Why this model exists}
**Dependencies**: {Other models this depends on}

**Schema**:
```swift/typescript/python
{Paste the actual model definition from source}
```

**Implementation Tasks**:
- [ ] T-{id}: Create model file/class
- [ ] T-{id}: Add validation logic
- [ ] T-{id}: Write migration (if needed)
- [ ] T-{id}: Create test fixtures
- [ ] T-{id}: Add to API/service layer

**Relationships**:
- {Model A} → {Model B}: {relationship type}

**Validation Rules**:
- {Field}: {constraints}

**Test Scenarios**:
1. Create with valid data
2. Validate required fields
3. Test relationships
4. Edge cases

---

### Priority 2: Feature Models
[Same structure for each model]

### Priority 3: Future/Optional Models
[Same structure]

## Model Relationship Diagram

```
{ASCII or description of relationships}
```

## Implementation Order

1. {Model A} (no dependencies)
2. {Model B} (depends on A)
3. {Model C} (depends on A, B)
...
```

### 2. API/Interface Document (02-apis-interfaces.md)

```markdown
# API & Interface Specifications

## Overview
- Total endpoints/interfaces: {count}
- API style: {REST, GraphQL, RPC, etc.}
- Authentication: {method}

## Endpoints by Feature Area

### Feature: {Area Name}

#### Endpoint: {Method} {Path}
**Source**: {doc reference}
**Purpose**: {What this endpoint does}

**Request**:
```json
{Example request payload}
```

**Response**:
```json
{Example response payload}
```

**Implementation Tasks**:
- [ ] T-{id}: Define route/handler
- [ ] T-{id}: Implement business logic
- [ ] T-{id}: Add validation
- [ ] T-{id}: Write tests (unit + integration)
- [ ] T-{id}: Add documentation

**Error Handling**:
- 400: {scenarios}
- 401: {scenarios}
- 404: {scenarios}
- 500: {scenarios}

**Dependencies**:
- Models: {list}
- Services: {list}
- External APIs: {list}

---

[Repeat for each endpoint]

## Interface Contracts

For internal interfaces/protocols:

### Interface: {Name}
```swift/typescript
{Interface definition}
```

**Implementers**:
- {Class/Module A}
- {Class/Module B}

**Implementation Tasks**:
- [ ] T-{id}: Define interface
- [ ] T-{id}: Implement in {A}
- [ ] T-{id}: Implement in {B}
- [ ] T-{id}: Add tests for conformance
```

### 3. Architecture Decisions (03-architecture-decisions.md)

```markdown
# Architecture Decisions

> Key technical choices and their rationale

## Decision Records

### ADR-{number}: {Title}
**Source**: {doc reference}
**Status**: {Proposed | Accepted | Deprecated}
**Date**: {decision date}

**Context**:
{What situation led to this decision}

**Decision**:
{What was decided}

**Rationale**:
{Why this was chosen over alternatives}

**Alternatives Considered**:
1. {Option A}: {Why rejected}
2. {Option B}: {Why rejected}

**Consequences**:
- Positive: {benefits}
- Negative: {tradeoffs}
- Neutral: {side effects}

**Implementation Tasks**:
- [ ] T-{id}: {What needs to be done to implement this decision}

**Validation Criteria**:
- {How to verify this decision was correct}

---

[Repeat for each decision]

## Open Architecture Questions

### Question: {Title}
**Context**: {Why this matters}
**Options**:
1. {Option A}: {pros/cons}
2. {Option B}: {pros/cons}

**Need to decide by**: {date/milestone}
**Who decides**: {stakeholder}
**Research needed**:
- [ ] T-{id}: {Research task}
```

### 4. Integration Points (04-integration-points.md)

```markdown
# Integration Points

## External Dependencies

### Integration: {Service/API Name}
**Source**: {doc reference}
**Purpose**: {Why we need this}
**Type**: {API, SDK, Library, Service}

**Connection Details**:
- Endpoint: {URL/identifier}
- Authentication: {method}
- Data format: {JSON, XML, etc.}

**Usage in Our System**:
- Used by: {components/modules}
- Frequency: {how often called}
- Criticality: {high/medium/low}

**Implementation Tasks**:
- [ ] T-{id}: Add SDK/client library
- [ ] T-{id}: Configure credentials
- [ ] T-{id}: Implement integration layer
- [ ] T-{id}: Add error handling
- [ ] T-{id}: Add monitoring/logging
- [ ] T-{id}: Write integration tests
- [ ] T-{id}: Document usage patterns

**Failure Scenarios**:
- {What if service is down}
- {What if rate limited}
- {What if data format changes}

**Fallback Strategy**:
{How system behaves when integration fails}

---

[Repeat for each integration]

## Internal Integration Points

### Module: {Name} → {Name}
**Interface**: {How they connect}
**Data Flow**: {What's exchanged}
**Dependencies**: {What must exist first}
```

### 5. Technical Open Questions (05-open-questions.md)

```markdown
# Technical Open Questions

> Unresolved technical decisions that block or affect implementation

## Critical (Need decision before starting)

### Q-{id}: {Question}
**Source**: {doc reference}
**Impact**: {What's blocked by this}
**Category**: {Architecture | Implementation | Performance | Security}

**Context**:
{Background information}

**Options**:
1. {Option A}
   - Pros: {list}
   - Cons: {list}
   - Effort: {estimate}

2. {Option B}
   - Pros: {list}
   - Cons: {list}
   - Effort: {estimate}

**Research Tasks**:
- [ ] T-{id}: {What to investigate}

**Decision Needed By**: {date}
**Decision Maker**: {who}

---

## High Priority

[Same structure for less critical questions]

## Nice to Resolve

[Same structure for questions that have reasonable defaults]

## Decision Log

### Resolved Question: {Title}
**Decided**: {date}
**Decision**: {what was chosen}
**Rationale**: {why}
```

## Technical Analysis Patterns

### Identifying Implementation Complexity

**Simple** (well-defined, standard patterns):
- CRUD operations on models
- Standard API endpoints
- Configuration changes

**Moderate** (requires design work):
- Custom algorithms
- Complex queries
- State management
- Caching strategies

**Complex** (significant R&D):
- New architecture patterns
- Performance optimization
- Security hardening
- ML/AI integration

### Extracting Non-Functional Requirements

Look for mentions of:
- **Performance**: response times, throughput, scalability
- **Security**: authentication, authorization, encryption
- **Reliability**: uptime, error rates, recovery
- **Maintainability**: code quality, testing, documentation
- **Usability**: accessibility, internationalization

### Technology Stack Mapping

Extract from document:
- Programming languages
- Frameworks/libraries
- Databases/storage
- Cloud services
- Development tools
- Testing frameworks
- Deployment platforms

Create tech stack artifact showing:
- What's already chosen
- What needs decision
- What has constraints (e.g., "must be on-device")
