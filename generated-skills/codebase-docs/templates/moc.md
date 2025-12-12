# MOC (Map of Content) Generation Template

Generate a GitHub-compatible documentation hierarchy with devlog synthesis and decision history.

## Output Structure

Create the following files in `docs/moc/`:

```
docs/moc/
├── README.md           # Main entry point (auto-renders on GitHub)
├── features.md         # Feature catalog with implementation status
├── architecture.md     # Architecture and design decisions
├── components.md       # Component maps and relationships
└── decisions.md        # ADRs and decision history (if devlog exists)
```

## Phase 1: Project Discovery

Scan the project root for:
- Configuration files (package.json, requirements.txt, etc.)
- Main source directories
- Technology stack indicators
- Existing documentation in `docs/`
- Devlog entries in `docs/devlog/`

## Phase 2: Devlog Analysis

If `docs/devlog/` exists:
1. Read all entries chronologically
2. Extract decision rationale
3. Identify "roads not taken" with reasoning
4. Note project evolution and pivots
5. Capture ongoing work context

## Phase 3: Feature Extraction

For each implemented feature:
1. Map feature to source files
2. Extract description from code/comments
3. Document current capabilities (NOT plans)
4. Create feature dependency graph

## Phase 4: Generate Documents

### README.md (Main Entry Point)

```yaml
---
title: [Project Name] Documentation
type: moc
generated: YYYY-MM-DD
last_updated: YYYY-MM-DD
project: [Project Name]
---
```

```markdown
# [Project Name] - Documentation Hub

> Last generated: [date]

## Overview
[2-3 sentence project description from package.json/README]

## Quick Navigation

- [Features](./features.md) - What the project does
- [Architecture](./architecture.md) - How it's built
- [Components](./components.md) - Module breakdown
- [Decisions](./decisions.md) - Why it's built this way

## Tech Stack
[Brief tech stack summary with links to source]

## Getting Started
[Link to main README or setup instructions]
```

### features.md

```yaml
---
title: Feature Catalog
type: moc-features
generated: YYYY-MM-DD
project: [Project Name]
---
```

```markdown
# Feature Catalog

## Core Features

### [Feature Name]
**Status**: Implemented | In Progress
**Source**: [Link to implementation file](../../src/path/to/file.ts)
**Description**: [What it does]
**Dependencies**: [Other features/components it relies on]

[Repeat for each feature]

## Feature Diagram

​```mermaid
graph LR
    A[Feature A] --> B[Feature B]
    B --> C[Feature C]
    A --> C
​```
```

### architecture.md

```yaml
---
title: Architecture Overview
type: moc-architecture
generated: YYYY-MM-DD
project: [Project Name]
---
```

```markdown
# Architecture Overview

## System Architecture

​```mermaid
flowchart TB
    subgraph "Layer 1"
        A[Component A]
    end
    subgraph "Layer 2"
        B[Component B]
        C[Component C]
    end
    A --> B
    A --> C
​```

## Design Principles
[Key architectural principles followed]

## Data Flow
[How data moves through the system]

## Technology Choices

| Area | Choice | Rationale |
|------|--------|-----------|
| [Area] | [Tech] | [Why] |

## Integration Points
[External services, APIs, dependencies]
```

### components.md

```yaml
---
title: Component Map
type: moc-components
generated: YYYY-MM-DD
project: [Project Name]
---
```

```markdown
# Component Map

## Component Overview

​```mermaid
graph TB
    subgraph Core
        A[Component A]
        B[Component B]
    end
    subgraph Services
        C[Service C]
    end
    A --> C
    B --> C
​```

## Component Details

### [Component Name]
**Location**: [Link to directory](../../src/component/)
**Purpose**: [What it does]
**Public Interface**: [Key exports/APIs]
**Dependencies**: [What it uses]
**Used By**: [What uses it]

[Repeat for each major component]
```

### decisions.md

```yaml
---
title: Decision History
type: moc-decisions
generated: YYYY-MM-DD
project: [Project Name]
---
```

```markdown
# Decision History

## Architectural Decision Records

### ADR-001: [Decision Title]
**Date**: YYYY-MM-DD
**Status**: Accepted | Superseded | Deprecated
**Context**: [Why this decision was needed]
**Decision**: [What was decided]
**Consequences**: [Impact of this decision]
**Alternatives Considered**:
- [Alternative 1]: [Why rejected]
- [Alternative 2]: [Why rejected]

[Repeat for each significant decision from devlog]

## Decision Timeline

| Date | Decision | Impact |
|------|----------|--------|
| [Date] | [Brief] | [Area affected] |
```

## Link Format Guidelines

**DO:**
- Use `[Text](./path/to/file.md)` for same-level links
- Use `[Text](../../src/file.ts)` for source code links
- Use relative paths from document location
- Include file extensions

**DON'T:**
- Use wiki-links `[[like this]]`
- Use absolute paths
- Omit file extensions
- Link to non-existent files

## Mermaid Diagram Types

Use appropriate diagram types:
- **flowchart TB/LR** - Architecture, data flow
- **graph TB/LR** - Component relationships
- **sequenceDiagram** - Request/response flows
- **classDiagram** - Data models
