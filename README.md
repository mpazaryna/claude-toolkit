# Claude Toolkit

A collection of specialized agents, commands, and templates for enhancing Claude Code's capabilities in understanding, analyzing, and documenting codebases.

## Overview

This toolkit provides structured markdown-based configurations that guide Claude Code through various development tasks. Rather than executable code, it offers:
- **Factory System** - Meta-generator for creating Skills, Prompts, Agents, Commands, and Hooks
- **Specialized agents** for code review, documentation fetching, and work summarization
- **Pre-configured commands** for systematic codebase exploration
- **Project templates** for comprehensive analysis of different technology stacks

### Factory System (Meta-Generator)

The toolkit includes a powerful factory system that helps you build custom Claude Code components:
- Use `/build` to create Skills, Prompts, Agents, Commands, or Hooks
- Guided question-and-answer process (4-11 questions depending on component type)
- Generates complete, validated, production-ready output
- Self-contained in `.claude/` directory for easy portability

## Installation

### As a Claude Code Plugin (Recommended)

1. Add the local marketplace:
```bash
claude-code plugin marketplace add /path/to/claude-toolkit/.claude-plugin
```

2. Install the plugin:
```bash
claude-code plugin install claude-toolkit@claude-toolkit-local
```

The plugin will now be available across all your projects!

### Manual Installation (Legacy)

1. Clone this repository:
```bash
git clone https://github.com/mpazaryna/claude-toolkit.git
cd claude-toolkit
```

2. Add your project to the index:
```bash
./deploy.sh add-project my-app ~/path/to/my-app
```

3. Deploy components:
```bash
./deploy.sh deploy-all my-app
```

## Documentation

- **[Installation & Deployment](docs/installation.md)** - Complete setup and deployment guide
- **[Components](docs/components.md)** - Detailed overview of agents, commands, and templates
- **[Usage](docs/usage.md)** - How to use the toolkit in your projects
- **[Maintenance](docs/maintenance.md)** - Meta-tooling and inspiration

## Structure

```
claude-toolkit/
├── .claude/                     # Core configuration (portable, self-contained)
│   ├── agents/                 # Factory guide agents
│   │   ├── factory-guide.md   # Main orchestrator
│   │   ├── skills-guide.md    # Skills builder
│   │   ├── prompts-guide.md   # Prompts generator
│   │   ├── agents-guide.md    # Agents builder
│   │   ├── commands-guide.md  # Commands builder
│   │   └── hooks-guide.md     # Hooks builder
│   ├── commands/               # Slash commands
│   │   ├── build.md           # /build command
│   │   └── git/
│   │       └── is.md          # /git:is command
│   └── templates/              # Factory templates (self-contained)
│       ├── SKILLS_FACTORY_PROMPT.md
│       ├── PROMPTS_FACTORY_PROMPT.md
│       ├── AGENTS_FACTORY_PROMPT.md
│       ├── MASTER_SLASH_COMMANDS_PROMPT.md
│       └── HOOKS_FACTORY_PROMPT.md
├── .claude-plugin/              # Plugin configuration
│   ├── plugin.json             # Plugin metadata
│   └── marketplace.json        # Local marketplace config
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
├── generated-commands/          # Output for generated commands
├── generated-skills/            # Output for generated skills
└── CLAUDE.md                    # Claude Code instructions

```

## Key Features

- **Meta-Generator Factory**: Build custom Skills, Prompts, Agents, Commands, and Hooks via `/build` command
- **Portable & Self-Contained**: The `.claude/` directory has everything needed - copy to any project for instant meta-generator functionality
- **Claude Code Plugin**: Installable plugin for easy distribution across projects
- **No Code Execution**: Pure markdown configurations for guidance
- **Modular Design**: Pick and choose components as needed
- **Namespaced Organization**: Commands and templates use the `paz/` namespace for better organization and to support multiple toolkit collections
- **Technology-Specific**: Tailored templates for different stacks
- **Workflow Integration**: Designed to enhance developer workflows
- **Shareable**: Easy to share with teams via marketplace distribution

### Quick Portability Example

Copy the factory system to any project:
```bash
cp -r .claude/ ~/my-new-project/
cd ~/my-new-project
# Now use /build to generate components
```


```bash
/plugin marketplace add https://github.com/mpazaryna/claude-toolkit  
```

# Small bump

Will this get registered inside of Linear?