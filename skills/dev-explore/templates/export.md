# Export Mode Template

Consolidate project documentation into numbered files for external LLM tools.

## Output Structure

Create the following files in `docs/exports/`:

```
docs/exports/
├── 01-project-overview.md        # CLAUDE.md content
├── 02-architecture-decisions.md  # All ADRs from docs/adr/
├── 03-design-docs.md             # docs/design/*.md (non-MLX)
├── 04-mlx-system.md              # docs/design/mlx/**/*.md
├── 05-devlog-current.md          # docs/devlog/*.md (non-archived)
├── 06-devlog-archive.md          # docs/devlog/archive/**/*.md
├── 07-specs.md                   # docs/specs/*.md
└── 08-uml.md                     # docs/uml/*.md
```

## Process

### Phase 1: Clear Output Directory

```bash
rm -rf docs/exports/*
mkdir -p docs/exports
```

### Phase 2: Generate Each File

For each output file:
1. Write a header describing the category
2. For each source file in the category:
   - Add separator: `---`
   - Add source header: `# Source: {relative_path}`
   - Add separator: `---`
   - Append file contents

### File Generation Details

#### 01-project-overview.md
```markdown
# PAB Project Overview

This file consolidates the main project documentation and orientation materials.

---
# Source: CLAUDE.md
---

{CLAUDE.md content}
```

#### 02-architecture-decisions.md
**Sources**: `docs/adr/*.md`
```markdown
# Architecture Decision Records

Key architectural decisions documented as ADRs.

---
# Source: docs/adr/ADR-001-no-viewmodels-in-swiftui.md
---

{file content}

---
# Source: docs/adr/ADR-002-agentic-development-patterns.md
---

{file content}

... repeat for each ADR
```

#### 03-design-docs.md
**Sources**: `docs/design/*.md`, `docs/design/diagrams/*.md`
(Excludes `docs/design/mlx/`)
```markdown
# Design Documentation

Technical design documents, data models, and schemas.

{concatenated files with source headers}
```

#### 04-mlx-system.md
**Sources**: `docs/design/mlx/*.md`, `docs/design/mlx/archive/*.md`
```markdown
# MLX System Documentation

MLX model integration, SOAP generation workflow, and Apple Intelligence integration.

{concatenated files with source headers}
```

#### 05-devlog-current.md
**Sources**: `docs/devlog/*.md` (files only, not archive/)
```markdown
# Current Development Logs

Recent development logs and technical decisions.

{concatenated files with source headers}
```

#### 06-devlog-archive.md
**Sources**: `docs/devlog/archive/**/*.md`
```markdown
# Archived Development Logs

Historical development logs from previous quarters.

{concatenated files with source headers}
```

#### 07-specs.md
**Sources**: `docs/specs/*.md`
```markdown
# Issue Specs

Multi-session issue tracking and implementation specs.

{concatenated files with source headers}
```

#### 08-uml.md
**Sources**: `docs/uml/*.md`
```markdown
# UML Diagrams

Component and architecture diagrams.

{concatenated files with source headers}
```

## File Header Format

Each output file starts with:
```markdown
# {Category Title}

{Brief description of what this file contains.}
```

## Source File Format

Each source file is included as:
```markdown

---
# Source: {relative/path/to/file.md}
---

{file contents}
```

## Best Practices

1. **Run after major changes** - Regenerate when docs are significantly updated
2. **Verify file sizes** - Large files may need splitting for some tools
3. **Check for stale content** - Review before uploading to external tools
4. **Git-ignore exports** - Consider adding `docs/exports/` to `.gitignore` if regenerated frequently
