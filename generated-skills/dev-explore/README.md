# dev-explore

Codebase exploration and interconnected documentation generation.

## What This Skill Does

Systematically explores codebases and generates documentation with three modes:

| Mode | Output | Best For |
|------|--------|----------|
| **analyze** | `codebase_analysis.md` | Understanding new codebases, onboarding |
| **moc** | `docs/moc/` hierarchy | Living documentation, decision history |
| **portfolio** | `PROJECT.md` | Resumes, interviews, showcasing work |

## When to Use

- Onboarding to an unfamiliar codebase
- Creating living documentation that evolves with code
- Preparing portfolio artifacts for job hunting
- Documenting architectural decisions
- Generating onboarding materials for new team members

## Related Skills

This skill is part of the `dev-*` family:

- **dev-inquiry** - Investigation and technical decisions
- **dev-explore** (this skill) - Codebase understanding
- **dev-reports** - Journals and status reports
- **dev-context** - ADR/Design/Spec/Plan scaffolding

## Quick Example

```
"Help me understand this codebase"
→ Analyze mode
→ Generates codebase_analysis.md with architecture diagrams

"Create a map of content for this project"
→ MOC mode
→ Generates docs/moc/ with interconnected documentation

"I need a PROJECT.md for my portfolio"
→ Portfolio mode
→ Generates resume-ready documentation
```

## Technology Support

Auto-detects and loads specialized templates for:
- iOS/Swift
- Android/Kotlin
- Cloudflare Workers
- MCP Servers
- TypeScript
- Jest Testing

## Installation

```bash
cp -r dev-explore/ /path/to/your/project/.claude/skills/
```

## Folder Structure

```
dev-explore/
├── SKILL.md              # Orchestrator
├── README.md             # This file
├── HOW_TO_USE.md         # Usage examples
├── templates/            # Output templates
│   ├── analyze-base.md
│   ├── moc.md
│   ├── portfolio.md
│   └── tech/             # Technology-specific
└── examples/             # Full output examples
```
