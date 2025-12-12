# Installation Guide: Internal Communications Skill

## Quick Install

### For Claude Code

```bash
# Global installation (available in all projects)
cp -r generated-skills/internal-comms ~/.claude/skills/

# Project-specific installation
cp -r generated-skills/internal-comms .claude/skills/
```

### For Claude Web/Desktop

1. Navigate to Skills settings
2. Click "Add Custom Skill"
3. Upload the entire `internal-comms` directory (includes templates)

## Verification

Test the installation:

```
User: "Write a 22A update for my current project"

Claude: "I'll create a Form 22A update using your company's format..."
```

## Prerequisites

- Claude Code or Claude with Skills support
- No external dependencies required

## File Structure

```
internal-comms/
├── SKILL.md                    # Main skill definition
├── README.md                   # Overview
├── HOW_TO_USE.md              # Detailed usage guide
├── INSTALL.md                 # This file
├── LICENSE.txt                # License information
└── examples/                   # Format templates (required)
    ├── form-22a.md            # Full update format
    ├── form-22b.md            # Condensed format
    └── devlog.md              # Developer log format
```

**Important:** Keep all files together! The skill loads templates from the `examples/` directory.

## Customization for Your Company

### Step 1: Review Existing Templates

Check if the example formats match your company's conventions:

```bash
cat generated-skills/internal-comms/examples/form-22a.md
cat generated-skills/internal-comms/examples/form-22b.md
cat generated-skills/internal-comms/examples/devlog.md
```

### Step 2: Customize Templates

Edit the template files to match your company's style:

```bash
# Edit the 22A format
vim ~/.claude/skills/internal-comms/examples/form-22a.md

# Edit the devlog format
vim ~/.claude/skills/internal-comms/examples/devlog.md
```

Add your company's:
- Specific section names
- Required fields
- Tone and voice guidelines
- Formatting preferences
- Example content

### Step 3: Add New Formats

Create additional templates for your company's unique formats:

```bash
# Add a new format
cat > ~/.claude/skills/internal-comms/examples/quarterly-review.md << 'EOF'
# Quarterly Review Format

## Guidelines
- Executive summary (2-3 sentences)
- Key metrics and KPIs
- Major accomplishments
- Challenges and lessons learned
- Next quarter goals

## Structure
[Your template here]
EOF
```

Then update `SKILL.md` to reference the new format:

```yaml
## How to use this skill

To write any internal communication:

1. **Identify the communication type** from the request
2. **Load the appropriate guideline file** from the `examples/` directory:
    - `examples/form-22a.md` - For Progress/Plans/Problems team updates
    - `examples/devlog.md` - For devlogs
    - `examples/form-22b.md` - Baby version of the 22A
    - `examples/quarterly-review.md` - For quarterly reviews  # NEW
    - `examples/general-comms.md` - For anything else
```

## Team Installation

To share with your team:

### Option 1: Shared Repository

```bash
# Add to your team's dotfiles repo
cp -r generated-skills/internal-comms team-dotfiles/claude/skills/

# Team members install
git clone team-dotfiles
cp -r team-dotfiles/claude/skills/internal-comms ~/.claude/skills/
```

### Option 2: Distribution Package

```bash
# Create a distributable package
cd generated-skills
tar -czf internal-comms-skill.tar.gz internal-comms/

# Share the tarball
# Team members extract to their skills directory
tar -xzf internal-comms-skill.tar.gz -C ~/.claude/skills/
```

### Option 3: Company-Wide Installation

If using a shared Claude instance or plugin system:

```bash
# Install to system-wide location
sudo cp -r generated-skills/internal-comms /opt/claude/skills/
```

## Troubleshooting

### Skill Not Recognized

**Problem:** Claude doesn't recognize the skill

**Solutions:**
1. Verify installation path: `ls ~/.claude/skills/internal-comms/SKILL.md`
2. Check YAML frontmatter in `SKILL.md` is valid
3. Try explicit request: "Use internal-comms skill to write a 22A update"
4. Restart Claude Code if using CLI

### Templates Not Loading

**Problem:** Claude can't find the format templates

**Solutions:**
1. Verify `examples/` directory exists: `ls ~/.claude/skills/internal-comms/examples/`
2. Check file names match exactly:
   - `form-22a.md` (not `form-22A.md` or `22a.md`)
   - `form-22b.md`
   - `devlog.md`
3. Ensure files have read permissions: `chmod +r ~/.claude/skills/internal-comms/examples/*`
4. Re-copy the entire directory (not just SKILL.md)

### Wrong Format Generated

**Problem:** Claude uses wrong template for your request

**Solutions:**
1. Be specific: "Write a 22A update" (not just "write an update")
2. Use keywords: "22A", "devlog", "22B condensed"
3. Edit `SKILL.md` to improve format detection keywords

## Updating

To update the skill with new templates or formats:

```bash
# Pull latest changes
cd claude-toolkit
git pull origin main

# Re-copy to skills directory
cp -r generated-skills/internal-comms ~/.claude/skills/

# Verify update
ls -la ~/.claude/skills/internal-comms/
```

## Uninstall

```bash
# Global installation
rm -rf ~/.claude/skills/internal-comms

# Project-specific installation
rm -rf .claude/skills/internal-comms
```

## License

This skill includes a LICENSE.txt file. Review it before distribution:

```bash
cat ~/.claude/skills/internal-comms/LICENSE.txt
```

## Support

For issues or questions:
- Review `HOW_TO_USE.md` for usage guidance
- Check `examples/` directory for format references
- Customize templates to match your company's needs

---

Generated by Claude Code Skills Factory
