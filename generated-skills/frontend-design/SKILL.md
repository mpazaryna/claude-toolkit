---
name: Frontend Design Excellence
description: Create distinctive, well-designed frontends instead of generic interfaces. Use when building UI components, landing pages, or web applications that need strong visual design.
---

# Frontend Design Excellence

## Purpose

Avoid generic "AI slop" designs. Create distinctive, contextually appropriate frontends with strong aesthetic choices.

## Design Principles

### Typography

**Avoid Generic Fonts**:
- ❌ Inter, Roboto, Arial, Helvetica
- ❌ System fonts as primary choice

**Use Distinctive Choices**:
- ✅ IBM Plex Sans/Mono - Technical, modern
- ✅ JetBrains Mono - Code-focused, geometric
- ✅ Playfair Display - Elegant, editorial
- ✅ Space Grotesk - Distinctive, contemporary
- ✅ Crimson Pro - Refined, readable

**Typography Hierarchy**:
```css
/* Strong scale with purpose */
--font-display: /* Large headings */
--font-heading: /* Section titles */
--font-body: /* Primary content */
--font-mono: /* Code, technical */

/* Intentional sizes */
--text-xs: 0.75rem;
--text-sm: 0.875rem;
--text-base: 1rem;
--text-lg: 1.125rem;
--text-xl: 1.25rem;
--text-2xl: 1.5rem;
--text-3xl: 1.875rem;
--text-4xl: 2.25rem;
```

### Color & Theme

**Cohesive Aesthetic with CSS Variables**:
```css
:root {
  /* Dominant color with variations */
  --color-primary: /* Main brand color */
  --color-primary-dark: /* Hover states */
  --color-primary-light: /* Backgrounds */

  /* Sharp accent for contrast */
  --color-accent: /* Calls-to-action */

  /* Atmospheric neutrals */
  --color-bg-base: /* Main background */
  --color-bg-elevated: /* Cards, panels */
  --color-surface: /* Interactive elements */

  /* Text hierarchy */
  --color-text-primary: /* Main content */
  --color-text-secondary: /* Supporting text */
  --color-text-muted: /* Subtle elements */
}
```

**Avoid**:
- ❌ Timid pastel-only palettes
- ❌ All-gray interfaces
- ❌ Random color selections

**Prefer**:
- ✅ Dominant color + sharp accent
- ✅ Cultural/contextual inspiration
- ✅ Intentional contrast ratios
- ✅ Dark mode considerations

### Motion & Animation

**High-Impact Moments** (CSS-only):
```css
/* Page entrance */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Staggered reveals */
.stagger-item:nth-child(1) { animation-delay: 0ms; }
.stagger-item:nth-child(2) { animation-delay: 100ms; }
.stagger-item:nth-child(3) { animation-delay: 200ms; }

/* Smooth interactions */
.interactive {
  transition: transform 200ms ease-out,
              box-shadow 200ms ease-out;
}

.interactive:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}
```

**Avoid**:
- ❌ Scattered micro-interactions everywhere
- ❌ JavaScript-heavy animations
- ❌ Jarring, bouncy effects

**Prefer**:
- ✅ CSS-only animations
- ✅ Staggered reveals for lists
- ✅ Purposeful entrance animations
- ✅ Smooth, subtle hover states

### Backgrounds & Depth

**Layered, Atmospheric Backgrounds**:
```css
/* Gradient depth */
.hero {
  background: linear-gradient(
    135deg,
    var(--color-primary) 0%,
    var(--color-primary-dark) 100%
  );
}

/* Geometric patterns */
.pattern-bg {
  background-image:
    radial-gradient(circle at 20% 50%,
      rgba(255,255,255,0.1) 0%,
      transparent 50%),
    radial-gradient(circle at 80% 80%,
      rgba(255,255,255,0.05) 0%,
      transparent 50%);
}

/* Subtle texture */
.textured {
  background-image:
    url("data:image/svg+xml,%3Csvg width='20' height='20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0h20v20H0z' fill='none'/%3E%3Cpath d='M10 0v20M0 10h20' stroke='rgba(255,255,255,0.02)' stroke-width='1'/%3E%3C/svg%3E");
}
```

**Avoid**:
- ❌ Solid color backgrounds only
- ❌ Flat, dimensionless design
- ❌ Stock gradient tools defaults

**Prefer**:
- ✅ Layered gradients
- ✅ Geometric patterns
- ✅ Subtle textures
- ✅ Atmospheric depth

## Implementation Workflow

### 1. Establish Design Direction

Before writing code, define:
- **Context**: What is this frontend for?
- **Audience**: Who will use it?
- **Mood**: Professional? Playful? Technical? Editorial?

### 2. Select Typography

Choose fonts that match the mood:
- **Technical/Developer tools**: IBM Plex, JetBrains Mono
- **Editorial/Content**: Playfair Display, Crimson Pro
- **Modern/Startup**: Space Grotesk, Cabinet Grotesk
- **Elegant/Refined**: Cormorant, Libre Baskerville

### 3. Build Color System

Create CSS variables with:
- 1 dominant color (with variations)
- 1 sharp accent color
- 3-4 neutral shades
- Consider cultural/contextual inspiration

### 4. Add Purposeful Motion

Animate only:
- Initial page load (entrance)
- List reveals (staggered)
- Important interactions (hover, focus)

Keep it CSS-only and subtle.

### 5. Create Depth with Backgrounds

Layer:
- Base gradient or color
- Geometric patterns
- Subtle overlays
- Atmospheric effects

## Code Quality Standards

**Always Include**:
- CSS variables for theming
- Responsive design (mobile-first)
- Semantic HTML
- Accessibility (ARIA labels, focus states)
- Dark mode support

**Component Structure**:
```html
<!-- Semantic, accessible markup -->
<section class="hero" role="banner">
  <h1 class="hero__title">Distinctive Heading</h1>
  <p class="hero__subtitle">Clear hierarchy</p>
  <button class="btn btn--primary">
    Clear CTA
  </button>
</section>
```

## Examples of Excellence

**Hero Section**:
- Layered gradient background
- Playfair Display for heading
- Staggered fade-in animation
- Sharp accent CTA button

**Feature Grid**:
- IBM Plex for technical content
- Subtle hover lift animations
- Geometric pattern overlay
- CSS variable theming

**Code Block**:
- JetBrains Mono font
- Syntax highlighting colors from theme
- Subtle shadow for depth
- Copy button with smooth interaction

## Anti-Patterns to Avoid

1. **Generic Font Stack**: Don't default to Inter/Roboto
2. **All Gray Everything**: Add color with intention
3. **Flat Design Only**: Layer gradients and patterns
4. **Animation Overload**: Purposeful motion only
5. **Ignoring Context**: Design for the specific use case

## Quick Checklist

Before finalizing any frontend:

- [ ] Distinctive typography chosen (not Inter/Roboto)
- [ ] CSS variables defined for theme
- [ ] Dominant color + sharp accent selected
- [ ] Background has depth (gradient/pattern)
- [ ] Entrance animations implemented (CSS-only)
- [ ] Hover states are smooth and purposeful
- [ ] Mobile responsive
- [ ] Accessible (ARIA, focus states, contrast)
- [ ] Dark mode considered

## Remember

The goal is to create frontends that feel **designed**, not **generated**. Every choice should be intentional and contextually appropriate.
