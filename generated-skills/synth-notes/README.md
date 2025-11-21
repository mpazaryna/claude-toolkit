# Synthetic SOAP Notes Generator Skill

Generate realistic chiropractic SOAP notes for clinical training datasets.

## Purpose

This skill provides orchestrator integration for the synthetic-notes generation system. It allows you to generate batches of clinically accurate SOAP notes through the orchestrator's interactive menu or CLI.

## What It Does

The skill:
1. Accepts configuration (prompt type, total notes, batch size)
2. Executes the synthetic-notes Python generator
3. Parses output and tracks costs
4. Reports results with full token usage and cost breakdown

## Usage via Orchestrator

### Interactive Mode

```bash
cd /Users/mpaz/workspace/orchestrator
uv run python orchestrator.py --interactive
# Select skill: synth-notes
# Configure: prompt_type, total, batch_size
```

### CLI Mode

```bash
cd /Users/mpaz/workspace/orchestrator
uv run python orchestrator.py --skill synth-notes
```

When prompted or via initial message, specify:
- **Prompt type**: adult_neck_pain, adult_chronic_lbp, torticollis, etc.
- **Total notes**: Number to generate (default: 10)
- **Batch size**: Notes per API call (default: 2)

## Available Prompt Types

### Adult Cases
- `adult_trauma` - Acute trauma and injuries
- `adult_chronic_lbp` - Chronic low back pain
- `adult_neck_pain` - Neck pain and cervicalgia
- `adult_sports_injury` - Sports-related injuries

### Pediatric Cases
- `torticollis` - Infant torticollis
- `plagiocephaly` - Cranial asymmetry
- `feeding` - Feeding difficulties
- `wellness` - Wellness exams

## Output Structure

Notes are saved to auto-numbered batch folders:

```
/Users/mpaz/workspace/synthetic-notes/output/
  batch_001/
    adult_neck_pain_a3f5d8e2.md
    adult_neck_pain_b4g6f9h3.md
  batch_002/
    adult_chronic_lbp_c5h7g0i4.md
    ...
```

Each note includes:
- Unique ID (UUID)
- Metadata (prompt type, batch, timestamp)
- Full SOAP note (Subjective, Objective, Assessment, Plan, Billing)

## Cost Tracking

The skill reports full cost breakdown using Claude Opus 4 pricing:
- Input: $15.00 per million tokens
- Output: $75.00 per million tokens

Typical costs:
- 10 notes: $0.50 - $2.00
- 50 notes: $2.50 - $10.00

## Requirements

- Synthetic-notes repository at `/Users/mpaz/workspace/synthetic-notes`
- `ANTHROPIC_API_KEY` set in synthetic-notes `.env` file
- `uv` package manager installed

## How It Works

The skill is an intelligent wrapper that:
1. Validates user configuration
2. Executes the proven synthetic-notes Python generator via `run_bash`
3. Parses stderr output for statistics
4. Verifies output files were created
5. Reports comprehensive results

This approach:
- ✅ Leverages existing proven generation logic
- ✅ Provides unified orchestrator interface
- ✅ Maintains separation of concerns
- ✅ Enables interactive configuration

## Example Output

```
✅ SOAP Notes Generation Complete

Batch folder: batch_006
Location: /Users/mpaz/workspace/synthetic-notes/output/batch_006/
Notes generated: 10
Prompt type: adult_neck_pain

Token Usage:
  Input tokens:  16,225
  Output tokens: 9,460
  Total tokens:  25,685

Cost:
  Input cost:  $0.24
  Output cost: $0.71
  Total cost:  $0.95

Files created:
  adult_neck_pain_a3f5d8e2.md
  adult_neck_pain_b4g6f9h3.md
  ...
```

## Architecture

This skill demonstrates the **orchestrator wrapper pattern**:

```
User → Orchestrator (interactive menu)
     → synth-notes skill (SKILL.md instructions)
     → Claude Code agent (autonomous execution)
     → run_bash tool (execute Python script)
     → synthetic-notes generator (proven logic)
     → Output parsing & reporting
     → User sees results
```

The skill doesn't reimplement generation logic - it orchestrates the existing system and provides a better UX layer.

## Skill Development Pattern

This skill can serve as a template for integrating other standalone tools into the orchestrator:

1. Create SKILL.md with clear instructions
2. Use `run_bash` to execute existing tools
3. Parse tool output for key information
4. Verify results with file system tools
5. Report comprehensive results to user

The agent handles error cases, user interaction, and result formatting.
