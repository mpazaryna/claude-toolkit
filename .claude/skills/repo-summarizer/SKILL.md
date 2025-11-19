---
name: repo-summarizer
description: Analyzes the current repository and generates a comprehensive PROJECT.md portfolio document following a structured template
---

# Repository Summarizer

This skill analyzes a code repository and generates a professional PROJECT.md portfolio document that captures the project's purpose, architecture, technical decisions, challenges, and outcomes in a format suitable for portfolios, resumes, and technical interviews.

## Capabilities

- **Codebase Analysis**: Examines repository structure, code files, and documentation to understand the project
- **Architecture Documentation**: Identifies system architecture, design patterns, and component relationships
- **Technology Stack Extraction**: Catalogs languages, frameworks, libraries, infrastructure, and tools
- **Feature Identification**: Discovers and documents key features and functionality
- **Design Decision Analysis**: Infers rationale behind technical choices and architectural decisions
- **Challenge Extraction**: Identifies technical challenges from code patterns, comments, and commit history
- **Outcome Generation**: Synthesizes project impact and measurable results
- **Portfolio Formatting**: Creates structured, professional documentation ready for multiple use cases

## Input Requirements

This skill operates on the **current repository** where it's invoked. No external input needed, but the skill will analyze:

- Repository structure and file organization
- Code files (all languages)
- README files and documentation
- Package manifests (package.json, requirements.txt, etc.)
- Configuration files
- Git history and commit messages (if available)
- Test files and frameworks
- Deployment configurations

Optional context you can provide:
- Business metrics or outcomes you want to highlight
- Specific challenges you faced
- Target audience for the documentation (recruiters, technical interviewers, etc.)

## Output Format

Generates a **PROJECT.md** file with the following structure:

### Main Sections
1. **Elevator Pitch**: 2-3 sentence summary (what, who, why)
2. **Context & Problem**: Problem statement and domain context
3. **Solution & Approach**: High-level solution and design principles
4. **Technical Implementation**:
   - Architecture overview
   - Technology stack breakdown
   - Key design decisions with rationale
5. **Key Features**: 5-10 most important features
6. **Outcomes & Metrics**: Quantifiable results and impact
7. **Technical Challenges & Solutions**: 3-5 significant challenges with solutions
8. **Learnings & Growth**: Skills developed and insights gained
9. **Future Enhancements**: Roadmap and potential improvements
10. **Project Links**: Repository, demo, documentation links
11. **Tags**: Technology and domain tags for searchability
12. **Portfolio Use Cases**: Quick extraction guides for different contexts

## How to Use

**Basic Invocation:**
```
Hey Claude—I just added the "repo-summarizer" skill. Can you analyze this repository and generate a PROJECT.md file?
```

**With Specific Focus:**
```
Hey Claude—I just added the "repo-summarizer" skill. Can you create a PROJECT.md emphasizing the AI/ML components and system architecture?
```

**With Business Context:**
```
Hey Claude—I just added the "repo-summarizer" skill. Generate a PROJECT.md for this repo. Note that it reduced processing time by 70% and serves 10,000+ users daily.
```

## Analysis Methodology

When invoked, the skill follows this systematic approach:

### 1. Repository Discovery
- Identify project type (web app, CLI tool, library, mobile app, etc.)
- Map directory structure and file organization
- Locate main entry points and core modules
- Identify configuration and build files

### 2. Technology Stack Analysis
- Extract dependencies from manifest files
- Identify frameworks and libraries from imports
- Catalog databases, APIs, and external services
- Document testing frameworks and tools
- Note deployment and infrastructure setup

### 3. Architecture Understanding
- Identify architectural patterns (MVC, microservices, etc.)
- Map component relationships and data flow
- Document system boundaries and integrations
- Analyze code organization and modularity

### 4. Feature Extraction
- Examine main code paths and modules
- Read existing documentation and comments
- Identify user-facing functionality
- Note internal capabilities and utilities

### 5. Challenge Identification
- Look for complex algorithms or custom solutions
- Find performance optimizations
- Identify cross-cutting concerns (security, scalability)
- Note integration challenges and workarounds

### 6. Synthesis & Documentation
- Craft compelling elevator pitch
- Write problem/solution narrative
- Document technical decisions with rationale
- Create feature descriptions
- Generate professional PROJECT.md

## Template Structure

The skill uses this proven template structure:

```markdown
# [Project Name] - Project Portfolio

## Elevator Pitch
[2-3 sentences: What it does, who it's for, why it matters]

## Context & Problem
[Problem statement, domain context, user needs]

## Solution & Approach
[High-level solution, key principles]

## Technical Implementation
### Architecture
### Technology Stack
### Key Design Decisions

## Key Features
[5-10 bullet points]

## Outcomes & Metrics
[Quantifiable results]

## Technical Challenges & Solutions
[3-5 challenges with solutions]

## Learnings & Growth
[Skills and insights]

## Future Enhancements
[Roadmap items]

## Project Links
[Repository, demo, docs]

## Tags
[Technology keywords]

## Portfolio Use Cases
[Quick extraction guides]
```

## Example Template Reference

The skill includes a complete example (GitHub PM project) showing:
- Professional tone and style
- Appropriate technical depth
- Balanced detail across sections
- Effective use of metrics
- Clear challenge/solution narratives
- Portfolio-ready formatting

## Best Practices

1. **Be Thorough**: Examine multiple files to understand the full scope
2. **Balance Detail**: Technical depth without overwhelming readers
3. **Use Specifics**: Concrete examples over vague descriptions
4. **Show Impact**: Include metrics and outcomes whenever possible
5. **Tell Stories**: Frame challenges as narrative problem-solving
6. **Consider Audience**: Write for both technical and non-technical readers
7. **Stay Professional**: Maintain objective, professional tone
8. **Be Honest**: Acknowledge limitations and trade-offs

## Quality Standards

Generated PROJECT.md files should:

✅ **Clarity**: Understandable by diverse audiences
✅ **Completeness**: All template sections filled meaningfully
✅ **Accuracy**: Reflects actual codebase and implementation
✅ **Professionalism**: Portfolio and resume-ready quality
✅ **Actionability**: Provides concrete examples and use cases
✅ **Searchability**: Includes relevant tags and keywords
✅ **Adaptability**: Content easily extracted for different contexts

## Limitations

- **Code Understanding**: Analysis quality depends on code clarity and documentation
- **Business Context**: May need user input for metrics and business outcomes
- **Private Information**: Cannot access metrics, analytics, or deployment data not in code
- **Historical Context**: Limited to what's visible in current repository state
- **Subjective Decisions**: Design decision rationale may be inferred, not explicit
- **Scope Boundaries**: Large monorepos may need guidance on what to include

## When NOT to Use

- Repository has no meaningful code (empty, template-only, trivial)
- Project is proprietary and documentation would expose sensitive information
- Repository is a fork with minimal changes
- Project is in very early stages with no substantial implementation

## Related Skills

Works well with:
- **Code documentation generators**: Provide detailed API docs
- **Architecture diagram tools**: Visual architecture supplements
- **Resume builders**: Extract PROJECT.md content for resumes
- **Portfolio site generators**: Convert PROJECT.md to web content

## Maintenance

Update PROJECT.md when:
- Major features are added
- Architecture significantly changes
- New challenges are solved
- Measurable outcomes improve
- Technology stack evolves

**Recommended**: Quarterly reviews to keep documentation current.
