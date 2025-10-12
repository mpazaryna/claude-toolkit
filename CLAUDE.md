# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Structure

This is a Claude Code plugin repository containing specialized agents, commands, and templates. The project is organized as a collection of Markdown-based configuration files and is distributed as a Claude Code plugin for easy installation across projects.

### Directory Organization

- **.claude-plugin/** - Plugin configuration
  - `plugin.json` - Plugin metadata and configuration
  - `marketplace.json` - Local marketplace configuration for testing

- **agents/** - Specialized AI agents with specific roles and behaviors
  - `quality-control-enforcer.md` - Reviews code for quality issues, workarounds, and incomplete implementations
  - `research-docs-fetcher.md` - Fetches and organizes web documentation into structured markdown files
  - `work-completion-summarizer.md` - Summarizes completed work

- **commands/** - Pre-configured command templates for common tasks
  - **paz/prime/** - Prime commands for understanding codebases
    - `mcp_dev.md` - Understanding MCP server codebases
    - `web_dev.md` - Understanding web development projects
  - **paz/learn/** - Learning resources
    - `acb.md` - Agent-Codebase learning material
  - **paz/context/** - Context rebuilding commands
    - `rebuild_context.md` - Rebuilding project context
    - `rebuild_readme.md` - Regenerating README files
  - **paz/tools/** - Tool-specific documentation
    - `playwright.md` - Playwright testing guidance

- **templates/** - Reusable templates for different project types
  - **paz/acb/** - Agent-Codebase analysis templates
    - `base.md` - Base codebase analysis template
    - `typescript.md` - TypeScript project template
    - `cloudflare-worker.md` - Cloudflare Worker template
    - `jest-testing.md` - Jest testing template
    - `mcp-server.md` - MCP server template
    - `ios-swift.md` - iOS Swift project template

## Key Components

### Agents
Each agent in the `agents/` directory follows a YAML frontmatter format with:
- `name`: Agent identifier
- `description`: When to use the agent (with examples)
- `color`: Visual indicator
- Agent-specific instructions and methodology

### Commands
Commands in `commands/` provide structured workflows with:
- `description`: Command purpose in frontmatter
- Sections like `Run`, `Read`, and `Report` for systematic execution

### Templates
Templates in `templates/` offer comprehensive analysis structures for different project types, focusing on:
- Implementation-ready documentation
- File-by-file breakdowns
- Actionable modification guidance
- Developer workflow integration

## Usage Patterns

1. **Agent Invocation**: Agents are referenced by their name and provide specialized analysis or validation
2. **Command Execution**: Commands guide systematic exploration and documentation of codebases
3. **Template Application**: Templates structure comprehensive codebase analysis for different project types

## Architecture Notes

This repository serves as a Claude Code plugin providing a configuration and template library. It doesn't contain executable code but rather provides structured markdown documents that define:
- Agent behaviors and review criteria
- Command sequences for codebase analysis
- Templates for documenting different types of projects

The plugin is designed to enhance Claude Code's ability to understand, analyze, and document various codebases through structured approaches and specialized agent roles. It can be installed across multiple projects via the Claude Code plugin system, providing consistent tooling and workflows.