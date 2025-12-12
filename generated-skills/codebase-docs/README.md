# Codebase Documentation Generator

A comprehensive Claude Skill for generating project documentation with three modes: technical analysis, Map of Content (MOC), and portfolio-ready artifacts.

## What This Skill Does

| Mode | Output | Best For |
|------|--------|----------|
| **analyze** | `codebase_analysis.md` | Understanding new codebases, onboarding developers |
| **moc** | `docs/moc/` hierarchy | Living documentation, decision history, devlog synthesis |
| **portfolio** | `PROJECT.md` | Resumes, interviews, showcasing work |

## Installation

### Option 1: Copy to Project (Recommended)

Copy the skill folder to your project's `.claude/skills/` directory:

```bash
# From the claude-toolkit repository
cp -r generated-skills/codebase-docs /path/to/your-project/.claude/skills/

# Create the skills directory if it doesn't exist
mkdir -p /path/to/your-project/.claude/skills
cp -r generated-skills/codebase-docs /path/to/your-project/.claude/skills/
```

### Option 2: Copy to Global Skills

For use across all projects:

```bash
# Copy to global Claude skills directory
cp -r generated-skills/codebase-docs ~/.claude/skills/
```

### Option 3: Symlink (Development)

For active development on the skill itself:

```bash
ln -s /path/to/claude-toolkit/generated-skills/codebase-docs ~/.claude/skills/codebase-docs
```

## Verification

After installation, verify Claude recognizes the skill:

```
Hey Claude—I just added the "codebase-docs" skill. What modes are available?
```

Claude should respond describing the three modes (analyze, moc, portfolio).

## Folder Structure

```
codebase-docs/
├── skill.md                      # Main skill definition
├── README.md                     # This file
├── HOW_TO_USE.md                 # Usage examples
├── sample_input.json             # Example input scenarios
├── expected_output_analyze.md    # Sample analyze mode output
├── expected_output_moc.md        # Sample MOC mode output
├── expected_output_portfolio.md  # Sample portfolio mode output
├── templates/                    # Output templates
│   ├── analyze-base.md           # Base analysis structure
│   ├── moc.md                    # MOC generation workflow
│   ├── portfolio.md              # Portfolio document structure
│   └── tech/                     # Technology-specific templates
│       ├── ios-swift.md
│       ├── android-kotlin.md
│       ├── cloudflare-worker.md
│       ├── mcp-server.md
│       ├── typescript.md
│       └── jest-testing.md
└── examples/                     # Full output examples (deprecated, see expected_output_*.md)
```

## Quick Start

1. **Install the skill** (see Installation above)
2. **Navigate to a project** you want to document
3. **Invoke Claude** with one of these:

```
# Understand a codebase
Hey Claude—I just added the "codebase-docs" skill. Can you analyze this codebase?

# Create living documentation
Hey Claude—I just added the "codebase-docs" skill. Can you generate a project MOC?

# Create portfolio documentation
Hey Claude—I just added the "codebase-docs" skill. Can you create a PROJECT.md for my portfolio?
```

## Technology Support

The skill auto-detects and loads specialized templates for:

- iOS/Swift (Package.swift, *.xcodeproj)
- Android/Kotlin (build.gradle.kts with android)
- Cloudflare Workers (wrangler.toml)
- MCP Servers (@modelcontextprotocol/sdk)
- TypeScript (tsconfig.json)
- Jest Testing (jest.config.js)

## Related Skills

This skill consolidates functionality from:
- `learn-project` - Technology-specific analysis templates
- `project-moc-generator` - MOC documentation with devlog synthesis
- `repo-summarizer` - Portfolio-ready PROJECT.md generation

## License

MIT - See LICENSE for details.

## Version History

- **1.0.0** - Initial consolidated release combining learn-project, project-moc-generator, and repo-summarizer
