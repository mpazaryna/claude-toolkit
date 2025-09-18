---
description: Create a new agent for the Claude Toolkit
---

# Add New Agent to Claude Toolkit

Create a new specialized agent in the `agents/` directory following the toolkit's established patterns.

## Gather Requirements

Ask the user:
1. **Agent name** (kebab-case, e.g., `code-optimizer`)
2. **Primary purpose** (one sentence)
3. **When to use** (specific scenarios)
4. **Color** for visual identification (red, yellow, green, blue, purple, etc.)
5. **Key behaviors and methodology**

## Create Agent File

Generate the agent file in `agents/[agent-name].md` with this structure:

```yaml
---
name: agent-name
description: When to use this agent (with specific examples)
color: chosen-color
---
```

Follow with:
- Clear instructions in first person
- Specific methodology steps
- Expected outputs
- Examples where helpful

## Update Documentation

1. Add the agent to README.md in the Agents table
2. Update CHANGELOG.md in the Unreleased/Added section
3. Verify the agent follows existing patterns by comparing with:
   - `agents/quality-control-enforcer.md`
   - `agents/research-docs-fetcher.md`
   - `agents/work-completion-summarizer.md`

## Validate

Confirm:
- [ ] Agent file created with proper frontmatter
- [ ] README.md updated with agent description
- [ ] CHANGELOG.md updated
- [ ] Agent name follows kebab-case convention
- [ ] Description clearly states when to use the agent