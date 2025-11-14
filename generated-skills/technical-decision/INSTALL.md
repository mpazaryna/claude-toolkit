# Installation Guide: Technical Decision Analysis Skill

## Quick Install

### For Claude Code

```bash
# Global installation (available everywhere)
cp -r generated-skills/technical-decision ~/.claude/skills/

# Project-specific installation
cp -r generated-skills/technical-decision .claude/skills/
```

### For Claude Web/Desktop

1. Navigate to Skills settings (if available)
2. Click "Add Custom Skill"
3. Upload the `technical-decision` folder or ZIP file

## Verification

Test the installation:

```
User: "Should I use PostgreSQL or MongoDB for my project?"

Claude: "I'll help you analyze this database decision systematically..."
[Provides structured analysis with comparison matrix and ADR]
```

## Prerequisites

- Claude Code or Claude with Skills support
- Internet access for researching options
- No external dependencies required

## File Structure

```
technical-decision/
├── SKILL.md           # Main skill definition
├── README.md          # Overview
├── HOW_TO_USE.md     # Usage guide
└── INSTALL.md        # This file
```

## Usage After Installation

Once installed, invoke the skill by asking technical decision questions:

### Direct Invocation

```
"Evaluate React vs Vue for our frontend"
"Should we use microservices or monolith architecture?"
"Compare AWS Lambda vs EC2 for our backend"
```

### Structured Request

```
"I need to decide between SwiftData and CoreData for iOS persistence.
Context: 30+ models, on-device only, need iOS 17+ features.
What do you recommend?"
```

### With Specific Criteria

```
"Compare Next.js vs Remix for our web app.
Prioritize: developer experience, performance, deployment flexibility.
Secondary: community support, learning curve."
```

## Customization

### Adjust Evaluation Criteria

Edit `SKILL.md` to add project-specific criteria:

```markdown
**Technology Selection**:
- [Add your team's priorities]
- [Add compliance requirements]
- [Add cost constraints]
```

### Modify ADR Template

Customize the ADR format in `SKILL.md`:

```markdown
# ADR-{N}: {TITLE}

**Status**: Proposed
**Date**: {DATE}
[Add your organization's ADR fields]
```

### Set Default Weights

Define standard weights for common decision types:

```markdown
**Performance-Critical Decisions**:
- Performance: High
- Scalability: High
- Developer Experience: Medium
```

## Troubleshooting

### Skill Not Providing Enough Detail

**Problem**: Analysis feels superficial

**Solutions:**
1. Provide more context about your project
2. Specify evaluation criteria explicitly
3. Ask follow-up questions about specific aspects
4. Request research on particular concerns

### Research Not Deep Enough

**Problem**: Want more technical depth

**Solutions:**
1. Request: "Research performance benchmarks"
2. Ask: "Find real-world case studies"
3. Specify: "Include migration complexity analysis"
4. Provide specific documentation URLs

### Recommendation Unclear

**Problem**: Not sure which option to choose

**Solutions:**
1. Ask: "What's the key differentiator?"
2. Request: "Which option is more reversible?"
3. Clarify constraints: "We need to ship in 2 weeks"
4. Test assumption: "Is scalability really critical for us?"

### ADR Format Doesn't Match Team Standards

**Problem**: Your team uses different ADR template

**Solutions:**
1. Edit `SKILL.md` to match your template
2. Request: "Format this as [your template]"
3. Copy key sections and reformat manually
4. Provide your template as context

## Team Installation

Share with your team:

### Option 1: Team Repository

```bash
# Add to team dotfiles or shared config
cp -r generated-skills/technical-decision team-dotfiles/claude/skills/

# Team members install
cp -r team-dotfiles/claude/skills/technical-decision ~/.claude/skills/
```

### Option 2: Project-Level

```bash
# Install in project .claude/skills/
mkdir -p .claude/skills
cp -r generated-skills/technical-decision .claude/skills/

# Commit to version control
git add .claude/skills/technical-decision
git commit -m "Add technical decision analysis skill"
```

## Integration with Workflow

### During Planning Phase

```bash
# Research options before sprint planning
"Evaluate options for user authentication"
"Compare data caching strategies"

# Document decisions in ADR
mkdir -p docs/architecture/decisions
# Save generated ADR to docs/architecture/decisions/
```

### During Architecture Reviews

```bash
# Analyze proposed approaches
"Review pros/cons of event-driven architecture for our use case"

# Generate ADR for review
# Share with team for feedback
```

### Before Major Refactoring

```bash
# Evaluate refactoring approaches
"Should we migrate to TypeScript incrementally or all at once?"

# Document decision and rationale
# Reference during implementation
```

## Best Practices

1. **Provide Context**: Share project constraints, team size, timeline
2. **Be Specific**: Define what matters most for your decision
3. **Save ADRs**: Create `docs/architecture/decisions/` directory
4. **Review Periodically**: Revisit decisions after 3-6 months
5. **Share with Team**: Use ADRs for onboarding and alignment

## Advanced Usage

### Decision Framework Templates

Create reusable decision frameworks:

```bash
# Save common decision types
echo "Database Selection Criteria: [...]" > .claude/decision-frameworks/database.md

# Reference when making decision
"Use database selection framework to evaluate options"
```

### Comparison Across Multiple Projects

```bash
# Document decisions across projects
mkdir -p ~/tech-decisions/
# Save ADRs with project prefix
# Build knowledge base over time
```

### Integration with Architecture Docs

```bash
# Keep ADRs with architecture docs
docs/
├── architecture/
│   ├── decisions/
│   │   ├── 001-database-choice.md
│   │   ├── 002-auth-strategy.md
│   │   └── 003-deployment-approach.md
│   └── diagrams/
```

## Uninstall

```bash
# Global installation
rm -rf ~/.claude/skills/technical-decision

# Project-specific
rm -rf .claude/skills/technical-decision

# Remove ADRs if desired
rm -rf docs/architecture/decisions/
```

## Support

For issues or questions:
- Review `HOW_TO_USE.md` for detailed examples
- Check decision quality principles in the skill
- Adjust criteria and weights to match your needs

---

Generated by Claude Code Skills Factory
