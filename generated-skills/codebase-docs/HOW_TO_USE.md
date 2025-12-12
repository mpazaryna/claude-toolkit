# How to Use This Skill

Hey Claude—I just added the "codebase-docs" skill. Can you analyze this repository and generate documentation?

## Example Invocations

### Analyze Mode (Understanding Codebases)

**Example 1 - Basic Analysis:**
```
Hey Claude—I just added the "codebase-docs" skill. Can you analyze this codebase and help me understand the architecture?
```

**Example 2 - Onboarding Focus:**
```
Hey Claude—I just added the "codebase-docs" skill. Can you create a codebase analysis focused on onboarding new developers?
```

**Example 3 - Specific Technology:**
```
Hey Claude—I just added the "codebase-docs" skill. Can you analyze this TypeScript project and highlight the testing patterns?
```

---

### MOC Mode (Living Documentation)

**Example 1 - Full MOC:**
```
Hey Claude—I just added the "codebase-docs" skill. Can you generate a project MOC with feature documentation?
```

**Example 2 - With Devlog Integration:**
```
Hey Claude—I just added the "codebase-docs" skill. Can you create a MOC that synthesizes our devlog entries into decision records?
```

**Example 3 - Architecture Focus:**
```
Hey Claude—I just added the "codebase-docs" skill. Can you generate architecture documentation in the MOC format?
```

---

### Portfolio Mode (Resume/Interview Ready)

**Example 1 - Basic Portfolio:**
```
Hey Claude—I just added the "codebase-docs" skill. Can you create a PROJECT.md for my portfolio?
```

**Example 2 - With Metrics:**
```
Hey Claude—I just added the "codebase-docs" skill. Can you generate a PROJECT.md? Note that this project serves 500+ daily users and reduced processing time by 70%.
```

**Example 3 - Interview Prep:**
```
Hey Claude—I just added the "codebase-docs" skill. Can you create portfolio documentation with interview talking points and resume bullet points?
```

---

### Combined Modes

**Example 1 - Analysis + Portfolio:**
```
Hey Claude—I just added the "codebase-docs" skill. Can you generate both a codebase analysis and a PROJECT.md?
```

**Example 2 - Complete Documentation:**
```
Hey Claude—I just added the "codebase-docs" skill. Can you create complete documentation using all three modes: analyze, MOC, and portfolio?
```

---

## What to Provide

### For All Modes
- Access to the repository (skill runs in current directory)
- Optional: Specific areas to focus on

### For Portfolio Mode (Optional but Helpful)
- Business metrics (user counts, performance improvements)
- Key challenges you want highlighted
- Target audience (recruiters, technical interviewers)

### For MOC Mode (Optional but Helpful)
- `docs/devlog/` directory with development notes
- Existing architecture decisions to capture

---

## What You'll Get

### Analyze Mode
- `codebase_analysis.md` with:
  - Tech stack breakdown
  - Directory structure analysis
  - File-by-file breakdown of key files
  - Architecture patterns identified
  - Mermaid diagrams
  - Onboarding guidance

### MOC Mode
- `docs/moc/` directory with:
  - `README.md` - Main entry point
  - `features.md` - Feature catalog
  - `architecture.md` - Architecture overview
  - `components.md` - Component maps
  - `decisions.md` - ADRs (if devlog exists)
  - All files use standard markdown links (GitHub compatible)

### Portfolio Mode
- `PROJECT.md` with:
  - Elevator pitch
  - Problem/solution narrative
  - Technical implementation details
  - Key features list
  - Challenges and solutions
  - Resume bullet points
  - Interview talking points

---

## Tips for Best Results

1. **Run in project root** - Skill works best from the repository root
2. **Have a README** - Existing documentation improves analysis quality
3. **Maintain devlog** - `docs/devlog/` entries enhance MOC decision records
4. **Provide metrics** - Business outcomes make portfolio mode more compelling
5. **Be specific** - Tell Claude which mode and any focus areas
6. **Iterate** - Generated docs are starting points; enhance with your insights
