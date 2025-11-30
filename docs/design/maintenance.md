# Toolkit Maintenance

This repository includes meta-tooling in the `.claude/` directory for maintaining and extending the toolkit itself. These tools ensure consistency and streamline the process of adding new components.

## Meta Commands (`.claude/commands/`)
- `add-agent.md` - Guided workflow for creating new agents with proper structure and documentation
- `add-template.md` - Streamlined process for adding new ACB templates following established patterns

## Meta Agents (`.claude/agents/`)
- `toolkit-consistency-reviewer` - Validates all components follow patterns, ensures documentation sync, and checks naming conventions

## Using Meta Tools

When working on this toolkit:
1. Use `add-agent.md` command to create new agents with consistent structure
2. Use `add-template.md` command to add technology-specific templates
3. Run `toolkit-consistency-reviewer` agent before commits to ensure everything follows patterns
4. These tools automatically update README and CHANGELOG when adding components

This self-referential approach ensures the toolkit remains organized and maintainable as it grows.

## Inspired By

### [CCPlugins](https://github.com/brennercruvinel/CCPlugins)
An advanced CLI extension for Claude Code that provides professional commands to automate software development workflows. CCPlugins pioneered the approach of using markdown-defined commands stored in `~/.claude/commands/` to transform Claude Code into an intelligent development assistant. It features safety-first design with automatic git checkpoints, multi-agent analysis patterns, and framework-agnostic commands that save developers 4-5 hours per week. This toolkit adopts similar markdown-based configuration patterns while focusing on modular, namespaced components for project-specific integration.

### [ContextKit](https://github.com/FlineDev/ContextKit)
An AI development workflow system that transforms Claude Code from a reactive to a proactive coding partner. ContextKit introduces a structured 4-phase methodology (Business Case → Technical Architecture → Implementation Tasks → Development) with specialized commands and quality agents. It excels at automatic context preservation across chat sessions and provides platform-agnostic project detection. This toolkit shares ContextKit's philosophy of structured workflows and specialized agents, while emphasizing portable, project-specific configurations that can be versioned alongside code.

### [IndyDevDan](https://www.youtube.com/@indydevdan)
A pioneering voice in the AI-assisted development community who pushes the boundaries of advanced context understanding and agentic programming. Through his YouTube channel, IndyDevDan demonstrates innovative techniques for leveraging Claude Code and other AI tools to create sophisticated development workflows. His work focuses on maximizing AI comprehension of complex codebases and enabling truly autonomous programming agents. This toolkit incorporates principles from his explorations in structured context management and agent-based development patterns.

## Acknowledgments

This toolkit is designed specifically for use with [Claude Code](https://claude.ai/code) by Anthropic.