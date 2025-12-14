---
name: dev-explore
description: Explore and understand codebases with interconnected documentation. Use when onboarding to a new project, creating living documentation (MOC), or generating portfolio artifacts.
---

# dev-explore

Systematic codebase exploration and documentation generation.

## Scope

This skill covers **codebase understanding**—exploring unfamiliar code, generating analysis, and creating interconnected documentation. Part of the `dev-*` family alongside `dev-inquiry`, `dev-reports`, and `dev-context`.

## Routing

Based on what you need, I'll reference the appropriate mode:

### Analyze Mode
**When**: Understanding a new codebase, onboarding
**Template**: `templates/analyze-base.md` + tech-specific templates
**Output**: `codebase_analysis.md`

Generates:
- Tech stack breakdown
- Directory structure analysis
- File-by-file breakdown
- Architecture patterns
- Mermaid diagrams

### MOC Mode (Map of Content)
**When**: Creating living documentation with decision history
**Template**: `templates/moc.md`
**Output**: `docs/moc/` directory

Generates interconnected docs:
```
docs/moc/
├── README.md        # Entry point
├── features.md      # Feature catalog
├── architecture.md  # Design decisions
├── components.md    # Component maps
└── decisions.md     # ADRs from devlog
```

### Portfolio Mode
**When**: Resume/interview preparation, showcasing work
**Template**: `templates/portfolio.md`
**Output**: `PROJECT.md`

Generates:
- Elevator pitch
- Problem/solution narrative
- Technical implementation
- Resume bullet points
- Interview talking points

## How to Use

1. **Identify the mode** from the request
2. **Load the appropriate template** from `templates/`
3. **Detect technology stack** and load tech templates from `templates/tech/`
4. **Reference examples** in `examples/` for output quality

Default to **analyze** mode if unclear.

## Technology Detection

Auto-detect and load specialized templates:

| Indicator | Technology | Template |
|-----------|------------|----------|
| `Package.swift`, `*.xcodeproj` | iOS/Swift | `templates/tech/ios-swift.md` |
| `build.gradle.kts` with android | Android/Kotlin | `templates/tech/android-kotlin.md` |
| `wrangler.toml` | Cloudflare Worker | `templates/tech/cloudflare-worker.md` |
| `@modelcontextprotocol/sdk` | MCP Server | `templates/tech/mcp-server.md` |
| `tsconfig.json` | TypeScript | `templates/tech/typescript.md` |
| `jest.config.js` | Jest | `templates/tech/jest-testing.md` |

## Best Practices

1. **Run Analyze first** when joining a project
2. **Use MOC for team projects** with ongoing development
3. **Use Portfolio after milestones** while context is fresh
4. **Maintain devlog** (`docs/devlog/`) for better MOC decision synthesis
5. **Regenerate periodically** to keep docs in sync

## Related Skills

- **dev-inquiry** - Investigation and technical decisions
- **dev-reports** - Journals and status reports
- **dev-context** - ADR/Design/Spec/Plan scaffolding
