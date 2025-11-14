# How to Use the Frontend Design Excellence Skill

## Quick Start

Simply ask Claude to build frontend components with good design:

```
"Create a hero section for a SaaS product"
"Build a feature showcase with distinctive design"
"Design a pricing table that doesn't look generic"
```

## What This Skill Does

The Frontend Design Excellence skill transforms generic "AI slop" interfaces into distinctive, well-designed frontends by guiding Claude through four key dimensions:

1. **Typography**: Choose distinctive fonts over generic defaults
2. **Color**: Build cohesive palettes with CSS variables
3. **Motion**: Add purposeful CSS-only animations
4. **Backgrounds**: Create atmospheric depth with gradients and patterns

## Usage Patterns

### Pattern 1: Building a Hero Section

**Generic Request**:
```
User: "Create a hero section"
```

**Result Without Skill**: Inter font, solid background, no animations

**With Frontend Design Skill**:
```
User: "Create a hero section for a developer tool"

Claude: [Generates hero with:]
- Playfair Display or IBM Plex for distinctive typography
- Layered gradient background with geometric patterns
- Staggered fade-in animations for title and CTA
- CSS variables for theming
- Smooth hover effects on CTA button
```

**Example Output**:
```html
<section class="hero">
  <div class="hero__content">
    <h1 class="hero__title animate-fade-in">
      Build Better APIs, Faster
    </h1>
    <p class="hero__subtitle animate-fade-in-delay-1">
      The developer-first API platform
    </p>
    <button class="btn btn--primary animate-fade-in-delay-2">
      Get Started →
    </button>
  </div>
</section>

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&display=swap');

:root {
  --color-primary: #0066ff;
  --color-primary-dark: #0052cc;
  --color-accent: #ff6b35;
  --color-bg: #0a0e27;
  --font-display: 'IBM Plex Sans', sans-serif;
}

.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,
    var(--color-bg) 0%,
    #1a1f3a 100%
  );
  background-image:
    radial-gradient(circle at 20% 50%,
      rgba(0, 102, 255, 0.1) 0%,
      transparent 50%),
    radial-gradient(circle at 80% 80%,
      rgba(255, 107, 53, 0.05) 0%,
      transparent 50%);
}

.hero__title {
  font-family: var(--font-display);
  font-size: 3.5rem;
  font-weight: 700;
  color: white;
  margin-bottom: 1rem;
}

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

.animate-fade-in {
  animation: fadeInUp 0.6s ease-out forwards;
}

.animate-fade-in-delay-1 {
  animation: fadeInUp 0.6s ease-out 0.1s forwards;
  opacity: 0;
}

.btn--primary {
  background: var(--color-accent);
  color: white;
  padding: 1rem 2rem;
  border-radius: 8px;
  border: none;
  font-weight: 600;
  cursor: pointer;
  transition: transform 200ms ease-out,
              box-shadow 200ms ease-out;
}

.btn--primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255, 107, 53, 0.3);
}
</style>
```

### Pattern 2: Feature Grid

**Request**:
```
User: "Build a 3-column feature grid for a technical product"
```

**With Skill**:
```html
<section class="features">
  <div class="features__grid">
    <article class="feature-card">
      <div class="feature-card__icon">⚡</div>
      <h3 class="feature-card__title">Lightning Fast</h3>
      <p class="feature-card__description">
        Sub-100ms response times at scale
      </p>
    </article>
    <!-- More cards... -->
  </div>
</section>

<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&display=swap');

.feature-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 2rem;
  transition: transform 200ms ease-out,
              box-shadow 200ms ease-out;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.2);
  border-color: rgba(0, 102, 255, 0.3);
}

.feature-card__title {
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--color-primary);
}
</style>
```

### Pattern 3: Code Block Display

**Request**:
```
User: "Create a code block showcase for documentation"
```

**With Skill**:
```html
<div class="code-showcase">
  <div class="code-showcase__header">
    <span class="code-showcase__label">example.ts</span>
    <button class="code-showcase__copy">Copy</button>
  </div>
  <pre class="code-showcase__content"><code>// Your code here</code></pre>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono&display=swap');

.code-showcase {
  background: linear-gradient(135deg,
    #1e1e1e 0%,
    #2d2d2d 100%
  );
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.code-showcase__content {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.9rem;
  padding: 1.5rem;
  margin: 0;
  overflow-x: auto;
}

.code-showcase__copy {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  transition: background 200ms ease-out;
}

.code-showcase__copy:hover {
  background: rgba(255, 255, 255, 0.15);
}
</style>
```

### Pattern 4: Navigation Bar

**Request**:
```
User: "Design a navigation bar for a modern web app"
```

**With Skill**:
```html
<nav class="navbar">
  <div class="navbar__container">
    <a href="/" class="navbar__logo">YourBrand</a>
    <ul class="navbar__menu">
      <li><a href="#features" class="navbar__link">Features</a></li>
      <li><a href="#pricing" class="navbar__link">Pricing</a></li>
      <li><a href="#docs" class="navbar__link">Docs</a></li>
    </ul>
    <button class="btn btn--primary btn--sm">Sign Up</button>
  </div>
</nav>

<style>
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  background: rgba(10, 14, 39, 0.8);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  z-index: 1000;
}

.navbar__link {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  transition: color 200ms ease-out,
              background 200ms ease-out;
}

.navbar__link:hover {
  color: white;
  background: rgba(255, 255, 255, 0.1);
}
</style>
```

### Pattern 5: Pricing Section

**Request**:
```
User: "Create a pricing section with 3 tiers"
```

**With Skill**:
```html
<section class="pricing">
  <h2 class="pricing__title">Simple, Transparent Pricing</h2>
  <div class="pricing__grid">
    <div class="pricing-card">
      <h3 class="pricing-card__name">Starter</h3>
      <div class="pricing-card__price">
        <span class="pricing-card__amount">$9</span>
        <span class="pricing-card__period">/month</span>
      </div>
      <ul class="pricing-card__features">
        <li>✓ 10,000 requests</li>
        <li>✓ Basic support</li>
        <li>✓ 99.9% uptime</li>
      </ul>
      <button class="btn btn--outline">Get Started</button>
    </div>
    <!-- More tiers... -->
  </div>
</section>

<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');

.pricing {
  padding: 6rem 2rem;
  background: linear-gradient(180deg,
    #0a0e27 0%,
    #1a1f3a 100%
  );
}

.pricing__title {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  color: white;
  margin-bottom: 3rem;
}

.pricing-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 2.5rem;
  transition: transform 300ms ease-out,
              border-color 300ms ease-out;
}

.pricing-card:hover {
  transform: scale(1.05);
  border-color: var(--color-primary);
}

.pricing-card__amount {
  font-size: 3rem;
  font-weight: 700;
  color: var(--color-accent);
}
</style>
```

## Design Contexts

### Technical/Developer Products

```
User: "Create a landing page for a developer API"

Claude uses:
- IBM Plex Sans or JetBrains Mono
- Dark background with blue/teal accents
- Code-focused aesthetic
- Geometric patterns
```

### Editorial/Content Sites

```
User: "Design a blog header"

Claude uses:
- Playfair Display or Crimson Pro
- Elegant, readable typography
- Refined color palette
- Spacious layout
```

### Modern SaaS

```
User: "Build a SaaS product homepage"

Claude uses:
- Space Grotesk or Cabinet Grotesk
- Vibrant gradients
- Contemporary aesthetic
- Smooth animations
```

## Best Practices

### 1. Provide Context

❌ **Too Generic**:
```
"Create a hero section"
```

✅ **Better**:
```
"Create a hero section for a B2B SaaS analytics platform targeting enterprise customers"
```

### 2. Specify Mood

```
"Design with a professional, trustworthy aesthetic"
"Create a playful, energetic design"
"Build with a minimalist, technical feel"
```

### 3. Request Specific Fonts

```
"Use IBM Plex for a technical aesthetic"
"Use Playfair Display for an editorial feel"
"Choose distinctive fonts appropriate for a luxury brand"
```

### 4. Define Color Direction

```
"Use deep blue as primary, gold as accent"
"Inspired by nature - greens and earth tones"
"High-contrast dark theme with vibrant accents"
```

## Common Questions

**Q: Will this work with frameworks like React/Vue?**
A: Yes! The CSS and design principles apply to any framework. Just request component-specific markup.

**Q: Can I use my own brand colors?**
A: Absolutely. Specify your brand palette and Claude will use it while maintaining design quality.

**Q: Are the designs accessible?**
A: Yes, the skill emphasizes accessibility including contrast ratios, ARIA labels, and focus states.

**Q: Can I customize the font choices?**
A: Yes, edit SKILL.md to add your preferred fonts, or specify fonts in your request.

**Q: Does this work for dark mode?**
A: Yes, designs use CSS variables making theme switching straightforward.

## Tips for Best Results

1. **Be Specific About Context**: "developer tool" vs "luxury e-commerce"
2. **Define Your Audience**: B2B enterprise, tech-savvy consumers, etc.
3. **Request Iterations**: "Make it more refined" or "Add more energy"
4. **Combine with Research**: Research design trends for your industry first
5. **Save Design Systems**: Create reusable CSS variable sets

## Related Skills

- **research-agent** - Research design trends and best practices
- **technical-decision** - Decide between design approaches
- **commit-helper** - Document design decisions in commits

---

Based on [Anthropic's blog post](https://www.claude.com/blog/improving-frontend-design-through-skills)

Generated by Claude Code Skills Factory
