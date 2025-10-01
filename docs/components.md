# Components

## Agents

Specialized AI agents with specific roles and behaviors:

| Agent | Purpose |
|-------|---------|
| `quality-control-enforcer` | Reviews code for quality issues, workarounds, and incomplete implementations |
| `research-docs-fetcher` | Fetches and organizes web documentation into structured markdown files |
| `work-completion-summarizer` | Summarizes completed work with clear documentation |

## Commands

Pre-configured workflows for common tasks. Commands are organized under the `paz/` namespace to allow for easy identification and to prevent conflicts when multiple toolkit collections are used together:

### Prime Commands (`commands/paz/prime/`)
- `mcp_dev.md` - Understanding MCP server codebases
- `web_dev.md` - Understanding web development projects

### Learning Resources (`commands/paz/learn/`)
- `acb.md` - Agent-Codebase learning material

### Context Commands (`commands/paz/context/`)
- `rebuild_context.md` - Rebuilding project context
- `rebuild_readme.md` - Regenerating README files

### Tool Documentation (`commands/paz/tools/`)
- `playwright.md` - Playwright testing guidance

## Templates

Comprehensive analysis structures for different project types. Like commands, templates are namespaced under `paz/` to facilitate organization and allow multiple toolkit collections to coexist:

### ACB Templates (`templates/paz/acb/`)
- `base.md` - Base codebase analysis template
- `typescript.md` - TypeScript project template
- `cloudflare-worker.md` - Cloudflare Worker template
- `jest-testing.md` - Jest testing template
- `mcp-server.md` - MCP server template
- `ios-swift.md` - iOS Swift project template
- `android-kotlin.md` - Android Kotlin project template

## Key Features

- **No Code Execution**: Pure markdown configurations for guidance
- **Modular Design**: Pick and choose components as needed
- **Namespaced Organization**: Commands and templates use the `paz/` namespace for better organization and to support multiple toolkit collections
- **Technology-Specific**: Tailored templates for different stacks
- **Workflow Integration**: Designed to enhance developer workflows