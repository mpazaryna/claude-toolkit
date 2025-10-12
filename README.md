# Claude Toolkit

A collection of specialized agents, commands, and templates for enhancing Claude Code's capabilities in understanding, analyzing, and documenting codebases.

## Overview

This toolkit provides structured markdown-based configurations that guide Claude Code through various development tasks. Rather than executable code, it offers:
- **Specialized agents** for code review, documentation fetching, and work summarization
- **Pre-configured commands** for systematic codebase exploration
- **Project templates** for comprehensive analysis of different technology stacks

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
└── CLAUDE.md                    # Claude Code instructions

```

## Key Features

- **Claude Code Plugin**: Installable plugin for easy distribution across projects
- **No Code Execution**: Pure markdown configurations for guidance
- **Modular Design**: Pick and choose components as needed
- **Namespaced Organization**: Commands and templates use the `paz/` namespace for better organization and to support multiple toolkit collections
- **Technology-Specific**: Tailored templates for different stacks
- **Workflow Integration**: Designed to enhance developer workflows
- **Shareable**: Easy to share with teams via marketplace distribution