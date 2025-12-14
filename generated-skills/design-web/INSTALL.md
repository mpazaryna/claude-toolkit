# Installing design-web

## Quick Install

Copy the skill folder to your project's `.claude/skills/` directory:

```bash
cp -r design-web/ /path/to/your/project/.claude/skills/
```

## Manual Install

1. Create the skills directory if it doesn't exist:
   ```bash
   mkdir -p .claude/skills
   ```

2. Copy the entire `design-web` folder:
   ```bash
   cp -r /path/to/design-web .claude/skills/
   ```

## Verify Installation

The structure should look like:

```
.claude/
└── skills/
    └── design-web/
        ├── SKILL.md              # Orchestrator
        ├── README.md             # Overview
        ├── HOW_TO_USE.md         # Usage guide
        ├── INSTALL.md            # This file
        └── references/
            ├── css-system.md     # Variables, theming
            ├── components.md     # UI components
            ├── backgrounds.md    # Gradients, patterns
            └── responsive.md     # Mobile-first layouts
```

## Related Skills

For complete design coverage, also install:

- `design-principles` - Design theory and fundamentals
- `design-swiftui` - SwiftUI/iOS implementation
- `design-review` - Audit and submission prep

## Usage

Once installed, Claude will use this skill when you ask for web implementation:

```
"Set up CSS for my new project"
"Build me a card component"
"Add a gradient background"
"Make this layout responsive"
```
