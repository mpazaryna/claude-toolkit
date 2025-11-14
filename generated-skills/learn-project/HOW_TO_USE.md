# How to Use the Learn Project Skill

## Quick Start

```
"Analyze the codebase in /path/to/my-project"
"Generate codebase_analysis.md for ~/workspace/api-server"
```

## What This Skill Does

Automatically analyzes your codebase by:
1. Detecting technologies (TypeScript, React, MCP, iOS, etc.)
2. Loading appropriate analysis templates
3. Merging templates into comprehensive analysis
4. Generating detailed `codebase_analysis.md`

## How It Works

### Step 1: Technology Detection

Scans for indicator files:
- `package.json` with `@modelcontextprotocol/sdk` → MCP Server
- `tsconfig.json` → TypeScript
- `wrangler.toml` → Cloudflare Worker
- `jest.config.js` → Jest Testing
- `Package.swift` or `*.xcodeproj` → iOS
- `next.config.js` → Next.js
- `requirements.txt` → Python

### Step 2: Template Loading

Loads templates based on detection:
- Always loads: `assets/base.md`
- Plus detected tech templates:
  - `assets/mcp-server.md`
  - `assets/typescript.md`
  - `assets/cloudflare-worker.md`
  - `assets/jest-testing.md`
  - `assets/ios-swift.md`
  - etc.

### Step 3: Analysis Generation

Creates `codebase_analysis.md` with:
- Project overview
- Technology-specific sections
- File-by-file breakdown
- Architecture diagrams
- Testing analysis
- Recommendations

## Usage Examples

### Example 1: Simple TypeScript Project

```
User: "Analyze the codebase in ~/projects/api-server"

Claude: I'll analyze the codebase.

[Detects:]
- TypeScript (tsconfig.json found)
- Jest (jest.config.js found)

[Loads templates:]
- base.md
- typescript.md
- jest-testing.md

[Generates comprehensive analysis in codebase_analysis.md]

Analysis complete! Created codebase_analysis.md with:
- Project overview
- TypeScript configuration analysis
- Directory structure
- File-by-file breakdown
- Jest testing coverage
- Architecture insights
- Recommendations
```

### Example 2: MCP Server (Cloudflare Worker)

```
User: "Generate codebase analysis for ~/compass"

Claude: Analyzing compass project...

[Detects:]
- MCP Server (@modelcontextprotocol/sdk in package.json)
- Cloudflare Worker (wrangler.jsonc found)
- TypeScript (tsconfig.json found)
- Jest (jest.config.cjs found)

[Loads templates:]
- base.md
- mcp-server.md
- cloudflare-worker.md
- typescript.md
- jest-testing.md

[Generates analysis covering:]
- MCP protocol implementation
- Cloudflare Worker deployment
- TypeScript types and interfaces
- Jest test coverage
- Edge computing patterns
- Integration architecture

Created: codebase_analysis.md (comprehensive multi-technology analysis)
```

### Example 3: iOS Swift Project

```
User: "Analyze /Users/dev/FitTracker-iOS"

Claude: Analyzing iOS project...

[Detects:]
- iOS Swift (Package.swift found)
- Testing (XCTest inferred)

[Loads templates:]
- base.md
- ios-swift.md

[Generates analysis including:]
- Swift package structure
- SwiftUI views and components
- Data models (SwiftData/CoreData)
- Navigation patterns
- Testing coverage
- App architecture (MVVM/MVC)
- iOS-specific recommendations

Created: codebase_analysis.md
```

## Generated Document Structure

The `codebase_analysis.md` includes:

```markdown
# [Project Name] Modular Codebase Analysis

> Last updated: [timestamp]
> Detected Technologies: TypeScript, Jest, MCP Server

## Technology Detection Results
- Project Type: MCP Server
- Tech Stack: TypeScript, Jest, Node.js
- Templates Applied: base, typescript, mcp-server, jest-testing

## Quick Reference
### Primary Entry Points
- src/index.ts
- src/server.ts

### Key Integration Files
- tools/ (MCP tools implementation)
- handlers/ (Request handlers)

## Directory Structure
[Full tree with technology-specific annotations]

## File-by-File Breakdown
[Detailed analysis of each file]

## Architecture Deep Dive
[Technology-specific architecture patterns]

## Testing Analysis
[Jest-specific testing insights]

## Technology Stack
[Comprehensive stack breakdown]

## Visual Architecture Diagram
[ASCII/Mermaid diagram]

## Key Insights & Recommendations
[Technology-specific improvements]
```

## Best Practices

### Do's ✅

- Provide absolute paths to projects
- Run from project root for best results
- Use for understanding new codebases
- Review generated analysis for insights
- Keep analysis updated as project evolves

### Don'ts ❌

- Don't run on non-code directories
- Don't expect analysis without project access
- Don't skip providing FOLDER_PATH

## Common Questions

**Q: What if technology isn't detected?**
A: Falls back to base template. You can request specific tech analysis.

**Q: Can I customize templates?**
A: Yes! Edit files in `assets/` directory.

**Q: Does it modify my code?**
A: No, read-only analysis only.

**Q: How long does analysis take?**
A: Depends on project size. Small projects: 1-2 minutes. Large: 5-10 minutes.

**Q: Can I analyze multiple projects?**
A: Yes, run the command for each project separately.

## Tips

1. **First time with codebase?** Run this skill to get oriented
2. **Onboarding new developers?** Share generated codebase_analysis.md
3. **Tech stack unclear?** Detection phase reveals all technologies
4. **Planning refactoring?** Analysis provides architecture insights
5. **Documentation outdated?** Regenerate analysis

## Related Skills

- **spike-driven-dev** - Use after understanding codebase to plan spikes
- **code-reviewer** - Review specific files identified in analysis

---

Generated by Claude Code Skills Factory
