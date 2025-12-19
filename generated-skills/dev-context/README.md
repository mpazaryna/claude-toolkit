# dev-context (Lean)

Set up working context for GitHub issues. Create formal ADRs when needed.

## Quick Start

```
"Set up context for issue #115"     → Creates docs/issues/115-*/
"Create ADR for choosing X over Y"  → Creates docs/adr/NNN-*.md
```

## Two Modes

### 1. Issue Working Space (Default)
Creates a lightweight working folder for multi-session tasks:
```
docs/issues/{num}-{short-name}/
├── README.md   # Status, links
├── plan.md     # Implementation approach
└── notes.md    # Working notes
```

### 2. Architecture Decision Record
For major decisions that warrant formal documentation:
```
docs/adr/NNN-decision-name.md
```

## Philosophy

This is a **lean** context skill. Most work doesn't need formal documentation:

| Need | Solution |
|------|----------|
| Task definition | GitHub issue |
| Working notes | `docs/issues/` folder |
| Decision history | Devlogs → `docs/moc/decisions.md` |
| Major architecture decision | ADR (use sparingly) |

## Structure

```
dev-context/
├── skill.md                    # Main skill definition
├── README.md                   # This file
└── references/
    └── templates/
        └── adr.md              # ADR template
```

## Part of the dev-* Family

| Skill | Purpose |
|-------|---------|
| `dev-context` | Set up working space, create ADRs |
| `dev-explore` | Generate/update MOC |
| `dev-reports` | Write devlogs |
| `dev-inquiry` | Technical investigation |

## See Also

- `docs/issues/README.md` - Working space conventions
- `ai_docs/maintenance-workflows.md` - Maintenance cycles
- `docs/moc/decisions.md` - Synthesized decision history
