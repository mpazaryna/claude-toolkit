# Claude Toolkit

A collection of specialized agents, commands, and templates for enhancing Claude Code's capabilities in understanding, analyzing, and documenting codebases.

## Overview

This toolkit provides structured markdown-based configurations that guide Claude Code through various development tasks. Rather than executable code, it offers:
- **Specialized agents** for code review, documentation fetching, and work summarization
- **Pre-configured commands** for systematic codebase exploration
- **Project templates** for comprehensive analysis of different technology stacks

## Installation & Deployment

> **Note:** This toolkit uses a project-based deployment system rather than global installation. Components are copied to individual projects as needed.

### Quick Start

1. Clone this repository:
```bash
git clone https://github.com/[username]/claude-toolkit.git
cd claude-toolkit
```

2. Add your project to the index:
```bash
./deploy.sh add-project my-app ~/path/to/my-app
```

3. Deploy components:
```bash
# Deploy everything
./deploy.sh deploy-all my-app

# Or deploy specific components
./deploy.sh deploy my-app agent:quality-control-enforcer
./deploy.sh deploy my-app template:paz/acb/typescript
```

### Deployment System

The toolkit includes sophisticated deployment scripts for managing components across multiple projects:

#### **deploy.sh** - Main deployment tool
```bash
# Add a new project
./deploy.sh add-project <name> <path>

# Deploy specific components
./deploy.sh deploy <project> agent:<name>
./deploy.sh deploy <project> command:<path>
./deploy.sh deploy <project> template:<path>

# Deploy all components
./deploy.sh deploy-all <project>

# View projects and status
./deploy.sh list                    # List all projects
./deploy.sh status <project>        # Show deployment details
```

#### **sync.sh** - Keep projects updated
```bash
# Sync a single project
./sync.sh my-app

# Sync all projects
./sync.sh all

# Check what needs updating
./sync.sh check
```

#### **projects.json** - Project index
Maintains a registry of all your projects with:
- Project paths and names
- Deployed components tracking
- Last deployment timestamps
- Custom `.claude` directory locations

### Manual Installation (Alternative)

If you prefer manual copying:
```bash
# Copy specific files to your project's .claude directory
cp claude-toolkit/agents/*.md your-project/.claude/agents/
cp -r claude-toolkit/commands/paz your-project/.claude/commands/
cp claude-toolkit/templates/paz/acb/*.md your-project/.claude/templates/
```

## Components

### Agents

Specialized AI agents with specific roles and behaviors:

| Agent | Purpose |
|-------|---------|
| `quality-control-enforcer` | Reviews code for quality issues, workarounds, and incomplete implementations |
| `research-docs-fetcher` | Fetches and organizes web documentation into structured markdown files |
| `work-completion-summarizer` | Summarizes completed work with clear documentation |

### Commands

Pre-configured workflows for common tasks. Commands are organized under the `paz/` namespace to allow for easy identification and to prevent conflicts when multiple toolkit collections are used together:

#### Prime Commands (`commands/paz/prime/`)
- `mcp_dev.md` - Understanding MCP server codebases
- `web_dev.md` - Understanding web development projects

#### Learning Resources (`commands/paz/learn/`)
- `acb.md` - Agent-Codebase learning material

#### Context Commands (`commands/paz/context/`)
- `rebuild_context.md` - Rebuilding project context
- `rebuild_readme.md` - Regenerating README files

#### Tool Documentation (`commands/paz/tools/`)
- `playwright.md` - Playwright testing guidance

### Templates

Comprehensive analysis structures for different project types. Like commands, templates are namespaced under `paz/` to facilitate organization and allow multiple toolkit collections to coexist:

#### ACB Templates (`templates/paz/acb/`)
- `base.md` - Base codebase analysis template
- `typescript.md` - TypeScript project template
- `cloudflare-worker.md` - Cloudflare Worker template
- `jest-testing.md` - Jest testing template
- `mcp-server.md` - MCP server template
- `ios-swift.md` - iOS Swift project template
- `android-kotlin.md` - Android Kotlin project template

## Usage

### Using Agents

Agents follow a YAML frontmatter format and can be invoked by referencing their name:

```markdown
# Example: Invoke quality control agent
Use the quality-control-enforcer agent to review this implementation
```

### Running Commands

Commands provide structured workflows:

```markdown
# Example: Prime a web development project
Follow the instructions in commands/paz/prime/web_dev.md
```

### Applying Templates

Templates structure comprehensive codebase analysis:

```markdown
# Example: Analyze a TypeScript project
Apply the template from templates/paz/acb/typescript.md
```

## Structure

```
claude-toolkit/
├── agents/                      # Specialized AI agents
│   ├── quality-control-enforcer.md
│   ├── research-docs-fetcher.md
│   └── work-completion-summarizer.md
├── commands/                    # Pre-configured workflows
│   └── paz/
│       ├── prime/              # Codebase understanding
│       ├── learn/              # Learning resources
│       ├── context/            # Context rebuilding
│       └── tools/              # Tool-specific docs
├── templates/                   # Project analysis templates
│   └── paz/
│       └── acb/                # Agent-Codebase templates
└── CLAUDE.md                    # Claude Code instructions

```

## Key Features

- **No Code Execution**: Pure markdown configurations for guidance
- **Modular Design**: Pick and choose components as needed
- **Namespaced Organization**: Commands and templates use the `paz/` namespace for better organization and to support multiple toolkit collections
- **Technology-Specific**: Tailored templates for different stacks
- **Workflow Integration**: Designed to enhance developer workflows

## Toolkit Maintenance

This repository includes meta-tooling in the `.claude/` directory for maintaining and extending the toolkit itself. These tools ensure consistency and streamline the process of adding new components.

### Meta Commands (`.claude/commands/`)
- `add-agent.md` - Guided workflow for creating new agents with proper structure and documentation
- `add-template.md` - Streamlined process for adding new ACB templates following established patterns

### Meta Agents (`.claude/agents/`)
- `toolkit-consistency-reviewer` - Validates all components follow patterns, ensures documentation sync, and checks naming conventions

### Using Meta Tools

When working on this toolkit:
1. Use `add-agent.md` command to create new agents with consistent structure
2. Use `add-template.md` command to add technology-specific templates
3. Run `toolkit-consistency-reviewer` agent before commits to ensure everything follows patterns
4. These tools automatically update README and CHANGELOG when adding components

This self-referential approach ensures the toolkit remains organized and maintainable as it grows.

## Usage Philosophy

This is a personal toolkit optimized for my specific workflows and development practices. While shared publicly for transparency and inspiration, it's not designed as a community project.

**Feel free to:**
- Fork and adapt any components for your own use
- Take individual files that solve your specific needs
- Use this as inspiration for building your own toolkit collection
- Run these tools alongside other collections like CCPlugins or ContextKit

**Please note:**
- This repository reflects my personal development preferences and workflows
- Pull requests are not accepted as this is maintained for personal use
- The structure and content may change based on my evolving needs
- Consider creating your own namespaced collection for your specific requirements

## Inspired By

### [CCPlugins](https://github.com/brennercruvinel/CCPlugins)
An advanced CLI extension for Claude Code that provides professional commands to automate software development workflows. CCPlugins pioneered the approach of using markdown-defined commands stored in `~/.claude/commands/` to transform Claude Code into an intelligent development assistant. It features safety-first design with automatic git checkpoints, multi-agent analysis patterns, and framework-agnostic commands that save developers 4-5 hours per week. This toolkit adopts similar markdown-based configuration patterns while focusing on modular, namespaced components for project-specific integration.

### [ContextKit](https://github.com/FlineDev/ContextKit)
An AI development workflow system that transforms Claude Code from a reactive to a proactive coding partner. ContextKit introduces a structured 4-phase methodology (Business Case → Technical Architecture → Implementation Tasks → Development) with specialized commands and quality agents. It excels at automatic context preservation across chat sessions and provides platform-agnostic project detection. This toolkit shares ContextKit's philosophy of structured workflows and specialized agents, while emphasizing portable, project-specific configurations that can be versioned alongside code.

### [IndyDevDan](https://www.youtube.com/@indydevdan)
A pioneering voice in the AI-assisted development community who pushes the boundaries of advanced context understanding and agentic programming. Through his YouTube channel, IndyDevDan demonstrates innovative techniques for leveraging Claude Code and other AI tools to create sophisticated development workflows. His work focuses on maximizing AI comprehension of complex codebases and enabling truly autonomous programming agents. This toolkit incorporates principles from his explorations in structured context management and agent-based development patterns.

## Acknowledgments

This toolkit is designed specifically for use with [Claude Code](https://claude.ai/code) by Anthropic.