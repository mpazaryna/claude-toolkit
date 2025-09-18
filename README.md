# Claude Toolkit

A collection of specialized agents, commands, and templates for enhancing Claude Code's capabilities in understanding, analyzing, and documenting codebases.

## Overview

This toolkit provides structured markdown-based configurations that guide Claude Code through various development tasks. Rather than executable code, it offers:
- **Specialized agents** for code review, documentation fetching, and work summarization
- **Pre-configured commands** for systematic codebase exploration
- **Project templates** for comprehensive analysis of different technology stacks

## Installation

> **Note:** Installation currently requires manual copying of files into individual projects. Symlinks and default Claude location integration may be addressed in future updates.

### Manual Installation

1. Clone this repository:
```bash
git clone https://github.com/[username]/claude-toolkit.git
```

2. Copy the desired files into your project:
```bash
# Copy specific agents
cp claude-toolkit/agents/quality-control-enforcer.md your-project/.claude

# Copy commands
cp -r claude-toolkit/commands/paz your-project/.claude

# Copy templates
cp claude-toolkit/templates/paz/acb/typescript.md your-project/.claude
```

3. Reference the files in your Claude Code sessions as needed

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