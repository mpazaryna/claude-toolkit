---
name: codebase-docs
description: Generates comprehensive codebase documentation with three modes - analyze (tech-stack-aware deep dive), moc (Map of Content with devlog integration), and portfolio (resume-ready PROJECT.md). Use when documenting projects, onboarding developers, or creating portfolio artifacts.
---

# Codebase Documentation Generator

This skill generates comprehensive documentation for software projects with three distinct modes.

## When to Use This Skill

Use this skill for:
- Understanding new codebases (analyze mode)
- Creating living documentation with decision history (moc mode)
- Building portfolio-ready project documentation (portfolio mode)
- Onboarding new developers
- Documenting architectural decisions
- Preparing for technical interviews

## How to Use This Skill

To generate documentation:

1. **Identify the documentation mode** from the request
2. **Load the appropriate template and example** from the directories:
   - **Analyze Mode** → `templates/analyze-base.md` + tech templates, see `examples/analyze-output.md`
   - **MOC Mode** → `templates/moc.md`, see `examples/moc-output.md`
   - **Portfolio Mode** → `templates/portfolio.md`, see `examples/portfolio-output.md`
3. **Detect technology stack** and load additional tech templates from `templates/tech/`
4. **Follow the template structure** for generating output
5. **Reference the example** for output format and quality standards

If the mode is unclear, ask for clarification or default to **analyze** mode.

## Keywords

codebase analysis, project documentation, MOC, map of content, portfolio, PROJECT.md, onboarding, architecture docs, devlog synthesis, technical overview, resume documentation

---

## Mode Reference

### Analyze Mode
**Trigger phrases**: "analyze", "understand", "technical overview", "onboarding"
**Template**: `templates/analyze-base.md` + detected tech templates
**Example**: `examples/analyze-output.md`
**Output**: `codebase_analysis.md`

### MOC Mode
**Trigger phrases**: "MOC", "map of content", "living documentation", "devlog", "decisions"
**Template**: `templates/moc.md`
**Example**: `examples/moc-output.md`
**Output**: `docs/moc/` directory

### Portfolio Mode
**Trigger phrases**: "portfolio", "PROJECT.md", "resume", "interview", "showcase"
**Template**: `templates/portfolio.md`
**Example**: `examples/portfolio-output.md`
**Output**: `PROJECT.md`

---

## Capabilities

- **Analyze Mode**: Generate developer-focused `codebase_analysis.md` with tech-stack-aware templates
- **MOC Mode**: Create GitHub-compatible `docs/moc/` hierarchy with devlog synthesis and decision history
- **Portfolio Mode**: Produce professional `PROJECT.md` suitable for resumes, interviews, and portfolios
- **Technology Detection**: Auto-detect project type and load appropriate analysis templates
- **Mermaid Diagrams**: Generate architecture visualizations that render on GitHub
- **Composable Outputs**: Each mode produces distinct artifacts that complement each other

## Input Requirements

The skill operates on the **current repository** where it's invoked. No external input required.

**What the skill analyzes:**
- Repository structure and file organization
- Source code files (all languages)
- README files and existing documentation
- Package manifests (package.json, requirements.txt, Cargo.toml, etc.)
- Configuration files (tsconfig.json, wrangler.toml, etc.)
- `docs/devlog/` entries (for MOC mode)
- Git history (when available)

**Optional context you can provide:**
- Specific mode to use (analyze, moc, portfolio)
- Business metrics or outcomes (for portfolio mode)
- Target audience (recruiters, developers, stakeholders)
- Areas of focus (specific features, components)

## Output Formats

### Analyze Mode
**Output**: `codebase_analysis.md` in project root

Sections include:
- Project Overview & Tech Stack
- Directory Structure Analysis
- File-by-File Breakdown
- Architecture Patterns
- Technology-Specific Analysis
- Testing Infrastructure
- Key Insights & Recommendations
- Mermaid Architecture Diagram

### MOC Mode
**Output**: `docs/moc/` directory

```
docs/moc/
├── README.md           # Main entry point (auto-renders on GitHub)
├── features.md         # Feature catalog
├── architecture.md     # Architecture and design decisions
├── components.md       # Component maps
└── decisions.md        # ADRs from devlog (if available)
```

### Portfolio Mode
**Output**: `PROJECT.md` in project root

Sections include:
- Elevator Pitch
- Context & Problem
- Solution & Approach
- Technical Implementation (with Mermaid diagrams)
- Key Features
- Outcomes & Metrics
- Technical Challenges & Solutions
- Learnings & Growth
- Portfolio Use Cases (resume bullets, interview talking points)

## Technology Detection

For **analyze** mode, detect and load tech-specific templates:

| Indicator | Technology | Template |
|-----------|------------|----------|
| `Package.swift` or `*.xcodeproj` | iOS/Swift | `templates/tech/ios-swift.md` |
| `build.gradle.kts` with android | Android/Kotlin | `templates/tech/android-kotlin.md` |
| `wrangler.toml` or `wrangler.jsonc` | Cloudflare Worker | `templates/tech/cloudflare-worker.md` |
| `@modelcontextprotocol/sdk` in package.json | MCP Server | `templates/tech/mcp-server.md` |
| `tsconfig.json` | TypeScript | `templates/tech/typescript.md` |
| `jest.config.js` or `jest.config.cjs` | Jest | `templates/tech/jest-testing.md` |

## Best Practices

1. **Run Analyze first** when joining a new project - understand before documenting
2. **Use MOC for team projects** - living documentation that evolves with the codebase
3. **Use Portfolio after milestones** - capture achievements while context is fresh
4. **Maintain devlog** - `docs/devlog/` entries improve MOC decision documentation
5. **Regenerate periodically** - keep documentation in sync with code
6. **Review and enhance** - generated docs are starting points, add human insights

## Limitations

- **Code understanding** depends on code clarity and existing documentation
- **Business metrics** may need user input (can't infer revenue, user counts)
- **Static snapshot** - reflects point-in-time state, must be regenerated
- **Large monorepos** may need guidance on scope/focus areas
- **Private data** - cannot access analytics, deployment logs, or external systems
- **Subjective decisions** - design rationale may be inferred, not explicit
