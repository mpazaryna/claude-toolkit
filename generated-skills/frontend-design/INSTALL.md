# Installation Guide: Frontend Design Excellence Skill

## Quick Install

### For Claude Code

```bash
# Global installation (available everywhere)
cp -r generated-skills/frontend-design ~/.claude/skills/

# Project-specific installation
cp -r generated-skills/frontend-design .claude/skills/
```

### For Claude Web/Desktop

1. Navigate to Skills settings (if available)
2. Click "Add Custom Skill"
3. Upload the `frontend-design` folder or ZIP file

## Verification

Test the installation:

```
User: "Create a hero section for a SaaS product"

Claude: [Creates hero with distinctive typography, layered gradients,
         staggered animations, and cohesive color system]
```

## Prerequisites

- Claude Code or Claude with Skills support
- No external dependencies required
- Works with pure HTML/CSS

## File Structure

```
frontend-design/
├── SKILL.md           # Main skill definition with design principles
├── README.md          # Overview
├── HOW_TO_USE.md     # Usage examples
└── INSTALL.md        # This file
```

## Usage After Installation

Once installed, invoke the skill when building frontends:

### Direct Invocation

```
"Build a landing page for a developer tool"
"Create a pricing section with good design"
"Design a feature showcase grid"
```

### With Context

```
"Build a hero section for a technical documentation site.
Use a professional, editorial aesthetic."
```

### Specific Components

```
"Create a navigation bar with smooth interactions"
"Design a card component with depth and hover effects"
"Build a code block with syntax highlighting"
```

## Customization

### Add Your Brand Colors

Edit `SKILL.md` to include your brand palette:

```css
:root {
  /* Your brand colors */
  --color-primary: #YourBrandColor;
  --color-accent: #YourAccentColor;
}
```

### Set Preferred Fonts

Customize the typography section:

```markdown
**Your Preferred Fonts**:
- ✅ [Your Display Font]
- ✅ [Your Body Font]
- ✅ [Your Mono Font]
```

### Define Design System

Add your design tokens:

```css
/* Your spacing scale */
--space-xs: 0.5rem;
--space-sm: 1rem;
--space-md: 1.5rem;
/* ... */
```

## Troubleshooting

### Generic Designs Still Appearing

**Problem**: Claude still uses Inter/Roboto

**Solutions:**
1. Explicitly request: "Use distinctive typography, not Inter"
2. Specify context: "This is for a luxury brand"
3. Reference the skill: "Follow frontend-design principles"
4. Be specific: "Use Playfair Display for headings"

### Fonts Not Loading

**Problem**: Custom fonts not appearing

**Solutions:**
1. Use Google Fonts CDN in HTML `<head>`:
   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">
   ```
2. Or use system font fallbacks in CSS:
   ```css
   font-family: 'IBM Plex Sans', -apple-system, sans-serif;
   ```

### Animations Too Heavy

**Problem**: Too many animations, performance issues

**Solutions:**
1. Request: "Minimal, purposeful animations only"
2. Reduce: "Animate page entrance only"
3. Use `prefers-reduced-motion`:
   ```css
   @media (prefers-reduced-motion: reduce) {
     * { animation: none !important; }
   }
   ```

### Colors Not Cohesive

**Problem**: Color palette feels random

**Solutions:**
1. Define upfront: "Use blue as dominant, orange as accent"
2. Request: "Create a cohesive color system"
3. Reference inspiration: "Colors inspired by nature/tech/etc"
4. Use CSS variables consistently

## Team Installation

Share with your team:

### Option 1: Team Repository

```bash
# Add to team design system
cp -r generated-skills/frontend-design team-design-system/claude/

# Team members install
cp -r team-design-system/claude/frontend-design ~/.claude/skills/
```

### Option 2: Project-Level

```bash
# Install in project
mkdir -p .claude/skills
cp -r generated-skills/frontend-design .claude/skills/

# Commit to version control
git add .claude/skills/frontend-design
git commit -m "Add frontend design skill for consistent UI quality"
```

## Integration with Workflow

### Starting New Projects

```bash
# Define design direction first
"Create a design system for a fintech app:
- Professional, trustworthy aesthetic
- Deep blue primary, gold accent
- IBM Plex for technical feel"

# Then build components
"Build hero section following this design system"
```

### Improving Existing UIs

```bash
# Analyze current design
"Review this component and suggest improvements"

# Apply design principles
"Redesign with distinctive typography and layered backgrounds"
```

### Component Library

```bash
# Build consistent components
"Create button variants following design system"
"Build card component with hover effects"
"Design form inputs with good UX"

# Document in Storybook/similar
```

## Best Practices

1. **Define Context Early**: Specify the product type and audience
2. **Establish Mood**: Professional? Playful? Technical? Editorial?
3. **Set Constraints**: Brand colors, accessibility requirements
4. **Iterate**: Request refinements based on feedback
5. **Document**: Save design decisions in CSS variables

## Advanced Usage

### Design System Generation

```bash
# Generate complete design system
"Create a comprehensive design system for a developer platform:
- Typography scale
- Color palette with CSS variables
- Spacing scale
- Component variants"

# Save to design-system.css
```

### Themed Components

```bash
# Create themeable components
"Build a card component that supports light/dark themes using CSS variables"

# Result uses var(--color-*) throughout
```

### Accessibility First

```bash
# Emphasize accessibility
"Create a form with excellent accessibility:
- ARIA labels
- Focus states
- Color contrast > 4.5:1
- Keyboard navigation"
```

## Font Resources

Recommended font sources:

- **Google Fonts**: Free, easy CDN integration
  - fonts.google.com
- **Adobe Fonts**: High-quality, subscription
  - fonts.adobe.com
- **Fontsource**: Self-host with npm
  - fontsource.org

## Inspiration Resources

For contextual design inspiration:

- **Dribbble**: UI design showcase (dribbble.com)
- **Awwwards**: Award-winning web design (awwwards.com)
- **Land-book**: Landing page gallery (land-book.com)
- **Mobbin**: Mobile UI patterns (mobbin.com)

## Uninstall

```bash
# Global installation
rm -rf ~/.claude/skills/frontend-design

# Project-specific
rm -rf .claude/skills/frontend-design
```

## Support

For issues or questions:
- Review `HOW_TO_USE.md` for detailed examples
- Check design principles in SKILL.md
- Adjust guidelines to match your brand

---

Based on [Anthropic's blog post](https://www.claude.com/blog/improving-frontend-design-through-skills)

Generated by Claude Code Skills Factory
