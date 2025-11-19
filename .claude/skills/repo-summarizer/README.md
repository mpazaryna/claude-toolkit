# Repo Summarizer - Claude Skill

**Version**: 1.0.0

Analyzes your repository and generates a comprehensive PROJECT.md portfolio document following a proven template structure.

## Overview

The Repo Summarizer skill automatically examines your codebase and creates professional project documentation suitable for:
- **Portfolio websites** - Showcase your work with comprehensive project pages
- **Resume bullets** - Extract achievements and technical highlights
- **Technical interviews** - Reference challenges, solutions, and design decisions
- **LinkedIn projects** - Create compelling project descriptions
- **GitHub profiles** - Link to detailed PROJECT.md documentation

## What It Does

1. **Analyzes Your Repository**:
   - Examines code structure and architecture
   - Identifies technology stack and frameworks
   - Discovers key features and functionality
   - Infers design decisions and patterns

2. **Generates PROJECT.md** with:
   - Elevator pitch (2-3 sentences)
   - Problem/solution narrative
   - Technical implementation details
   - Key features list
   - Outcomes and metrics
   - Technical challenges and solutions
   - Learnings and future enhancements
   - Portfolio use case guides

3. **Provides Portfolio-Ready Content**:
   - Professional tone and formatting
   - Balanced technical depth
   - Multiple extraction options for different contexts
   - Searchable technology tags

## Installation

### Option 1: Quick Install (Recommended)

If you have Claude Code CLI or Claude app:

```bash
# From this directory
claude skills install .
```

### Option 2: Manual Installation

Copy the `repo-summarizer` folder to your Claude skills directory:

**For Claude Code:**
```bash
# Project-level installation
mkdir -p .claude/skills
cp -r repo-summarizer .claude/skills/

# User-level installation (available in all projects)
mkdir -p ~/.claude/skills
cp -r repo-summarizer ~/.claude/skills/
```

**For Claude Desktop App:**
```bash
# macOS
cp -r repo-summarizer ~/Library/Application\ Support/Claude/skills/

# Windows
copy repo-summarizer %APPDATA%\Claude\skills\

# Linux
cp -r repo-summarizer ~/.config/claude/skills/
```

### Option 3: From ZIP

Unzip `repo-summarizer.zip` and follow Option 2 instructions.

## Quick Start

Navigate to any repository and invoke the skill:

```
Hey Claude—I just added the "repo-summarizer" skill. Can you analyze this repository and generate a PROJECT.md?
```

That's it! The skill will:
1. Analyze your codebase
2. Generate comprehensive PROJECT.md
3. Place it in your repository root

## Usage Examples

### Basic Usage
```
Hey Claude—I just added the "repo-summarizer" skill. Create a PROJECT.md for this repository.
```

### With Business Context
```
Hey Claude—I just added the "repo-summarizer" skill. Generate a PROJECT.md. Context: This tool reduced deployment time by 70% and serves 5,000+ users daily.
```

### Focused Analysis
```
Hey Claude—I just added the "repo-summarizer" skill. Create a PROJECT.md emphasizing the microservices architecture and real-time processing.
```

### For Specific Audience
```
Hey Claude—I just added the "repo-summarizer" skill. Generate a PROJECT.md for technical recruiters, focusing on system design and problem-solving.
```

## What You Get

A complete **PROJECT.md** file containing:

- ✅ **Elevator Pitch** - Concise project summary
- ✅ **Context & Problem** - Problem statement and background
- ✅ **Solution & Approach** - Your approach and principles
- ✅ **Technical Implementation** - Architecture, stack, design decisions
- ✅ **Key Features** - 5-10 most important capabilities
- ✅ **Outcomes & Metrics** - Quantifiable results and impact
- ✅ **Technical Challenges & Solutions** - Problem-solving narratives
- ✅ **Learnings & Growth** - Skills and insights gained
- ✅ **Future Enhancements** - Roadmap and next steps
- ✅ **Project Links** - Repository, demo, documentation
- ✅ **Tags** - Technology keywords for searchability
- ✅ **Portfolio Use Cases** - Quick extraction guides

## File Structure

```
repo-summarizer/
├── SKILL.md                    # Main skill definition and instructions
├── HOW_TO_USE.md              # Detailed usage examples
├── README.md                  # This file - installation guide
├── sample_input.json          # Example input structure
└── expected_output.json       # Example output structure
```

## Template Reference

The skill uses a battle-tested template structure with:
- **Proven format** used by professional developers
- **Multiple use cases** - extract content for different contexts
- **Balanced depth** - technical without overwhelming
- **Portfolio ready** - professional quality output

See the included template files for the complete structure and a real-world example (GitHub PM project).

## Tips for Best Results

1. **Provide Business Metrics**: The skill can infer technical details but needs your help with:
   - User/adoption numbers
   - Performance improvements
   - Time savings
   - Business impact

2. **Specify Focus Areas**: Tell Claude what to emphasize:
   - Architecture and system design
   - Specific technologies or patterns
   - Problem-solving and challenges
   - Innovation or novel approaches

3. **Define Your Audience**: Mention who will read this:
   - Technical recruiters
   - Potential investors
   - Open-source community
   - Portfolio visitors

4. **Review and Enhance**: After generation:
   - Verify technical accuracy
   - Add missing metrics
   - Update project links
   - Refine based on your goals

## Common Workflows

### Portfolio Update
```bash
# Generate PROJECT.md for each portfolio project
cd ~/projects/awesome-app
# Invoke repo-summarizer skill
# Review and commit PROJECT.md
```

### Job Search Prep
```bash
# Generate docs for key projects
# Extract "Technical Challenges & Solutions" for interview prep
# Use tags to match job requirements
```

### Quarterly Documentation
```bash
# Re-run skill to capture new features
# Update metrics with latest data
# Add new challenges solved
# Refresh future enhancements
```

## Customization

The skill is flexible and adapts to your needs:

- **Focus**: Emphasize specific technologies or aspects
- **Tone**: Adjust for technical vs. business audiences
- **Depth**: Control level of technical detail
- **Context**: Incorporate business metrics and outcomes

## Requirements

- Claude Code CLI or Claude Desktop App
- A code repository to analyze (any language/framework)
- Optional: Business context and metrics for richer output

## Limitations

- Requires meaningful codebase (not empty or trivial projects)
- Business metrics and outcomes require user input
- Cannot access external analytics or deployment data
- Best suited for completed or substantially developed projects

## Support

For issues or questions:
1. Check `HOW_TO_USE.md` for detailed examples
2. Review `SKILL.md` for methodology and capabilities
3. Ensure repository has sufficient code and structure

## Version History

**v1.0.0** (2025-11-19)
- Initial release
- Complete template structure
- Comprehensive analysis methodology
- Portfolio use case guides
- Sample templates and examples

## License

This skill is part of the Claude Skills library and follows the same license as your Claude subscription.

---

**Ready to create professional project documentation in minutes!**

For detailed usage examples, see `HOW_TO_USE.md`.
