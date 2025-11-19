# How to Use the Repo Summarizer Skill

Hey Claude—I just added the "repo-summarizer" skill. Can you analyze this repository and generate a PROJECT.md file?

## Example Invocations

### Example 1: Basic Analysis
```
Hey Claude—I just added the "repo-summarizer" skill. Can you analyze this repository and create a comprehensive PROJECT.md?
```

**What happens:**
- Claude examines the entire codebase
- Identifies architecture, tech stack, features
- Generates complete PROJECT.md with all sections
- Places file in repository root

---

### Example 2: Focused Analysis
```
Hey Claude—I just added the "repo-summarizer" skill. Can you generate a PROJECT.md emphasizing the microservices architecture and API design decisions?
```

**What happens:**
- Claude focuses analysis on architecture and APIs
- Still generates all sections but highlights specified areas
- Provides deeper detail in architecture and design decisions sections

---

### Example 3: With Business Context
```
Hey Claude—I just added the "repo-summarizer" skill. Create a PROJECT.md for this repository. Context: This tool reduced our deployment time from 2 hours to 15 minutes and is used by 50+ developers daily.
```

**What happens:**
- Claude incorporates your metrics into Outcomes & Metrics section
- Uses business impact to inform Elevator Pitch
- Generates PROJECT.md with quantifiable results

---

### Example 4: Portfolio-Focused
```
Hey Claude—I just added the "repo-summarizer" skill. I'm updating my portfolio and need a PROJECT.md that would impress technical recruiters. Focus on system design and problem-solving.
```

**What happens:**
- Claude emphasizes Technical Challenges & Solutions
- Highlights architectural decisions and trade-offs
- Creates recruiter-friendly narrative

---

### Example 5: Update Existing
```
Hey Claude—I just added the "repo-summarizer" skill. We have an existing PROJECT.md but it's outdated. Can you regenerate it based on the current codebase?
```

**What happens:**
- Claude analyzes current state of repository
- Generates fresh PROJECT.md reflecting latest changes
- Preserves any custom metrics or context from old version if you specify

---

## What to Provide

### Required
- **Nothing!** The skill analyzes the current repository automatically

### Optional (Enhances Output)
- **Business metrics**: User counts, performance improvements, time savings
- **Specific focus areas**: Architecture, features, challenges you want emphasized
- **Target audience**: Recruiters, investors, technical interviewers, open-source community
- **Known challenges**: Technical problems you solved that might not be obvious from code

### Examples of Helpful Context
```
"This reduced API response time by 80%"
"Used by 10,000+ users in production"
"Won company hackathon for innovation"
"Migrated legacy system serving 1M requests/day"
"First implementation of this pattern at our company"
```

---

## What You'll Get

### Complete PROJECT.md File
Location: Root of your repository (`./PROJECT.md`)

### Includes All Sections:
1. ✅ **Elevator Pitch** - Concise 2-3 sentence summary
2. ✅ **Context & Problem** - Problem statement and background
3. ✅ **Solution & Approach** - Your solution and approach
4. ✅ **Technical Implementation** - Architecture, stack, design decisions
5. ✅ **Key Features** - 5-10 most important capabilities
6. ✅ **Outcomes & Metrics** - Quantifiable results
7. ✅ **Technical Challenges & Solutions** - 3-5 problem/solution narratives
8. ✅ **Learnings & Growth** - Skills and insights gained
9. ✅ **Future Enhancements** - Roadmap items
10. ✅ **Project Links** - Repository, demo, documentation
11. ✅ **Tags** - Searchable technology keywords
12. ✅ **Portfolio Use Cases** - Quick extraction guides

### Ready for Multiple Uses:
- **Resume**: Extract "Elevator Pitch" + "Outcomes & Metrics" + "Technology Stack"
- **Technical Interview**: Reference "Technical Challenges & Solutions"
- **Portfolio Website**: Use "Context & Problem" + "Solution & Approach" + "Key Features"
- **LinkedIn**: Use "Elevator Pitch" + key features + tags
- **GitHub Profile**: Link with elevator pitch as preview

---

## Tips for Best Results

### 1. Run from Repository Root
```bash
cd /path/to/your/project
# Then invoke Claude with the skill
```

### 2. Provide Business Context
The skill can infer technical details, but you should provide:
- User/adoption metrics
- Performance improvements
- Business impact
- Time savings

### 3. Specify Your Audience
Tell Claude who will read this:
- "For technical recruiters"
- "For potential investors"
- "For open-source contributors"
- "For my portfolio website"

### 4. Highlight What Matters
If you have specific achievements, mention them:
- Novel algorithms or approaches
- Complex integrations
- Performance optimizations
- Scale achievements

### 5. Review and Refine
After generation:
- Review for accuracy
- Add missing metrics
- Adjust tone if needed
- Update links section

---

## Common Workflows

### Initial Project Documentation
```
1. Complete your project
2. Invoke repo-summarizer skill
3. Review generated PROJECT.md
4. Add any missing business context
5. Commit to repository
```

### Portfolio Update
```
1. Run repo-summarizer on each portfolio project
2. Use "Portfolio Use Cases" section to extract content
3. Update resume with "Elevator Pitch" + "Outcomes"
4. Update portfolio site with full PROJECT.md content
5. Add GitHub README link to PROJECT.md
```

### Job Search Prep
```
1. Generate PROJECT.md for key projects
2. Extract "Technical Challenges & Solutions" for interview prep
3. Use "Tags" to match job requirements
4. Reference specific sections during technical interviews
```

### Quarterly Updates
```
1. Re-run skill to capture new features
2. Update Outcomes & Metrics with latest data
3. Add new challenges/solutions
4. Refresh Future Enhancements section
```

---

## Customization Options

### Focus Areas
```
"Focus on the AI/ML components"
"Emphasize the database architecture"
"Highlight the real-time processing pipeline"
"Detail the security implementation"
```

### Tone Adjustments
```
"Make it more technical for senior developer audience"
"Keep it high-level for executive summary"
"Balance technical and business perspectives"
```

### Length Preferences
```
"Keep it concise - one page equivalent"
"Provide comprehensive detail"
"Medium depth - suitable for portfolio site"
```

---

## Troubleshooting

### "The generated PROJECT.md is too generic"
**Solution**: Provide specific context about challenges, metrics, and unique aspects

### "Missing important features"
**Solution**: Explicitly mention features you want highlighted

### "Technical details are too shallow/deep"
**Solution**: Specify your target audience and adjust depth accordingly

### "Outcomes section is weak"
**Solution**: Provide concrete metrics: user counts, performance gains, time savings

---

## Next Steps After Generation

1. **Review Accuracy**: Verify technical details match implementation
2. **Add Metrics**: Fill in quantifiable outcomes if not auto-detected
3. **Update Links**: Add actual URLs for repository, demo, docs
4. **Refine Tags**: Add any missing technology or domain keywords
5. **Extract Content**: Use "Portfolio Use Cases" for resume/LinkedIn/website
6. **Commit**: Add PROJECT.md to your repository
7. **Share**: Link to PROJECT.md from README or portfolio

---

**Generated PROJECT.md is portfolio-ready, professional, and adaptable for resumes, interviews, and technical showcases!**
