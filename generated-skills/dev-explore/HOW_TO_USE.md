# How to Use dev-explore

## Basic Usage

Describe what you need:

```
"Help me understand this codebase"
"Create living documentation for this project"
"Generate a PROJECT.md for my portfolio"
```

## Modes

### Analyze Mode
For understanding new codebases:

```
"Analyze this codebase and help me understand the architecture"
"Create a codebase analysis focused on onboarding"
"Analyze this TypeScript project and highlight testing patterns"
```

**Output**: `codebase_analysis.md` with tech stack, architecture, file breakdowns, diagrams

### MOC Mode (Map of Content)
For living documentation with interconnected files:

```
"Generate a project MOC with feature documentation"
"Create a MOC that synthesizes our devlog entries"
"Generate architecture documentation in MOC format"
```

**Output**: `docs/moc/` directory with README, features, architecture, components, decisions

### Portfolio Mode
For resume and interview preparation:

```
"Create a PROJECT.md for my portfolio"
"Generate portfolio documentation with interview talking points"
"Create a PROJECT.md - this project serves 500+ daily users"
```

**Output**: `PROJECT.md` with elevator pitch, challenges, resume bullets, talking points

## Combined Modes

```
"Generate both a codebase analysis and a PROJECT.md"
"Create complete documentation using all three modes"
```

## Tips for Best Results

1. **Run from project root** - Works best with full repository access
2. **Have a README** - Existing docs improve analysis quality
3. **Maintain devlog** - `docs/devlog/` entries enhance MOC decisions
4. **Provide metrics** - Business outcomes make portfolio mode compelling
5. **Be specific** - Tell which mode and any focus areas
6. **Iterate** - Generated docs are starting points; enhance with your insights

## What to Provide

### For All Modes
- Access to the repository (run in project directory)
- Optional: Specific areas to focus on

### For Portfolio Mode
- Business metrics (user counts, performance improvements)
- Key challenges you want highlighted
- Target audience (recruiters, technical interviewers)

### For MOC Mode
- `docs/devlog/` directory with development notes
- Existing architecture decisions to capture
