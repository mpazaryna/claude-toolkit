---
description: Create a new ACB template for the Claude Toolkit
---

# Add New ACB Template to Claude Toolkit

Create a new Agent-Codebase analysis template in the `templates/paz/acb/` directory.

## Gather Template Requirements

Ask the user:
1. **Technology/Framework** (e.g., `react-native`, `django`, `rust`)
2. **File extension preference** (e.g., `.tsx`, `.py`, `.rs`)
3. **Key patterns to analyze** (architecture, state management, testing approach)
4. **Specific files to prioritize** (config files, entry points)
5. **Development workflow specifics** (build commands, test runners)

## Create Template Structure

Generate template in `templates/paz/acb/[technology].md` with sections:

### 1. Header
```markdown
# [Technology] ACB Template

Agent-Codebase analysis template for [Technology] projects.
```

### 2. Core Sections to Include
- **Project Overview** - Architecture and structure
- **Key Files** - Entry points and configuration
- **Implementation Patterns** - Framework-specific patterns
- **State Management** (if applicable)
- **Testing Approach**
- **Build & Deploy**
- **Development Workflow**
- **Common Modifications**

### 3. File-by-File Analysis Format
```markdown
## Core Files

### `path/to/file.ext`
**Purpose**: [Brief description]
**Key Patterns**:
- [Pattern 1]
- [Pattern 2]

**Modification Guide**:
- To add [feature]: [specific steps]
- To modify [behavior]: [specific steps]
```

## Reference Existing Templates

Review these templates for consistency:
- `templates/paz/acb/base.md` - Foundation structure
- `templates/paz/acb/typescript.md` - Web framework example
- `templates/paz/acb/ios-swift.md` - Mobile example
- `templates/paz/acb/mcp-server.md` - Server/API example

## Update Documentation

1. Add template to README.md under ACB Templates
2. Update CHANGELOG.md in Unreleased/Added
3. Ensure template follows the established format

## Validate

Confirm:
- [ ] Template created with clear sections
- [ ] File-by-file breakdown included
- [ ] Actionable modification guidance provided
- [ ] README.md updated
- [ ] CHANGELOG.md updated
- [ ] Follows existing template patterns