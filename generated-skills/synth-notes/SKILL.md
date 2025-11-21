---
name: synth-notes
description: Generate synthetic clinical SOAP notes for training datasets
---

# Synthetic SOAP Notes Generator

Generate realistic chiropractic SOAP notes for clinical training datasets using the synthetic-notes generation system.

## Overview

This skill orchestrates the synthetic-notes generator to create batches of clinically accurate SOAP notes. You will execute the existing Python-based generator, parse its output, and report results to the user.

## Available Prompt Types

### Adult Cases (Ages 18-65+)
- **adult_trauma** - Acute trauma, post-fall injuries, MVA, work accidents with imaging
- **adult_chronic_lbp** - Chronic low back pain, degenerative conditions, SI joint dysfunction
- **adult_neck_pain** - Cervicalgia, tech neck, postural strain, cervicogenic headaches
- **adult_sports_injury** - Sports-related injuries, overuse patterns, athletic performance

### Pediatric Cases (Infants)
- **torticollis** - Congenital, positional, and post-frenectomy torticollis presentations
- **plagiocephaly** - Cranial asymmetry and positional plagiocephaly cases
- **feeding** - Nursing and feeding difficulty presentations
- **wellness** - General wellness exams and preventive care

## User Configuration

Extract from the initial message or ask the user for:
1. **Prompt type** (required) - Which clinical scenario to generate (e.g., "adult_neck_pain")
2. **Total notes** (optional) - Number of notes to generate (default: 10)
3. **Batch size** (optional) - Notes per API call (default: 2)

If not provided in initial message, ask the user to specify the prompt type at minimum.

## Execution Workflow

### Step 1: Validate Configuration

Ensure:
- Prompt type is one of the valid options listed above
- Total notes is a positive integer
- Batch size is a positive integer (typically 2-5 for best quality)

### Step 2: Execute Generator

Use the `run_bash` tool to execute:

```bash
cd /Users/mpaz/workspace/synthetic-notes && uv run python src/main.py --prompt-type {prompt_type} --total {total} --batch-size {batch_size}
```

Replace `{prompt_type}`, `{total}`, and `{batch_size}` with actual values.

**Important**: The generator writes progress to stderr and notes to files. Capture both stdout and stderr.

### Step 3: Parse Output

The generator outputs to stderr with this format:

```
Loading prompts for type: adult_neck_pain...
Generating 10 notes (5 batches of 2)
Batch folder: /Users/mpaz/workspace/synthetic-notes/output/batch_006
...
Generating batch 1 (2 notes, type: adult_neck_pain)...
  ✓ Tokens: 3,245 in / 1,892 out | Cost: $0.1905

...

============================================================
Usage Summary
============================================================
Total API calls: 5
Input tokens:    16,225
Output tokens:   9,460
Total tokens:    25,685
------------------------------------------------------------
Input cost:      $0.2434
Output cost:     $0.7095
Total cost:      $0.9529
============================================================

✓ Generated 10 notes
✓ Saved to /Users/mpaz/.../output/batch_006/
✓ Batch folder: batch_006
```

Extract:
- Batch folder path
- Total notes generated
- Token usage (input/output)
- Total cost

### Step 4: Verify Output

Use `list_files` tool to verify notes were created:

```
path: /Users/mpaz/workspace/synthetic-notes/output/batch_XXX
pattern: *.md
```

Count the markdown files to confirm expected number.

### Step 5: Report Results

Provide a clear summary to the user:

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

## Error Handling

### API Key Missing
If you see: `ANTHROPIC_API_KEY environment variable not set`
- Report to user: "Synthetic-notes requires ANTHROPIC_API_KEY to be set in the environment. Please configure .env file in the synthetic-notes repository."

### Invalid Prompt Type
If the prompt type is not in the valid list:
- Report available prompt types
- Ask user to select a valid option

### Generation Failure
If the command returns non-zero exit code:
- Report the error from stderr
- Suggest checking API quota/credits

### No Files Created
If the batch folder is empty after execution:
- Report the issue
- Check stderr for error messages

## Important Notes

### Cost Transparency
Always report the full cost breakdown. Claude Opus 4 pricing:
- Input: $15.00 per million tokens
- Output: $75.00 per million tokens

A typical batch of 10 notes costs $0.50-$2.00 depending on complexity.

### Batch Folder Auto-Increment
The generator automatically creates the next available batch folder (batch_001, batch_002, etc.). You don't need to manage this.

### Output Location
All notes are saved to: `/Users/mpaz/workspace/synthetic-notes/output/batch_XXX/`

Each note includes metadata header:
- ID (UUID)
- Prompt type
- Batch folder
- Timestamp
- Full SOAP note content

### Quality Expectations
The prompts enforce:
- Anatomically specific findings (not generic descriptions)
- Proper ICD-10 and CPT coding
- Age-appropriate techniques
- Realistic patient histories (brief and vague, like real patients)
- Clinical rationale for treatments

## Example Execution

**User request**: "Generate 6 adult neck pain notes"

**Your execution**:

1. Parse request: prompt_type=adult_neck_pain, total=6, batch_size=2
2. Execute command:
   ```bash
   cd /Users/mpaz/workspace/synthetic-notes && \
     uv run python src/main.py \
       --prompt-type adult_neck_pain \
       --total 6 \
       --batch-size 2
   ```
3. Parse stderr output for batch folder, token usage, costs
4. Verify 6 markdown files created in batch folder
5. Report results with full cost breakdown

## Success Criteria

Task is complete when:
- ✅ Generator executed successfully
- ✅ Expected number of notes generated
- ✅ Batch folder contains all markdown files
- ✅ Cost and usage statistics reported to user
- ✅ No errors occurred

Stop and report results. Do not ask for confirmation after completion.

## Tool Usage Summary

- `run_bash`: Execute the synthetic-notes generator
- `list_files`: Verify notes were created in batch folder
- `read_file`: (Optional) Read sample note to show user

Do not use `write_file` - the generator handles all file writing.
