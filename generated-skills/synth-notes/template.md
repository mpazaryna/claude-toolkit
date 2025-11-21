# Example: SOAP Notes Generation Result

This shows the expected output format when reporting results to the user.

## Success Case

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
  adult_neck_pain_c5i8h1j4.md
  adult_neck_pain_d6j9i2k5.md
  adult_neck_pain_e7k0j3l6.md
  adult_neck_pain_f8l1k4m7.md
  adult_neck_pain_g9m2l5n8.md
  adult_neck_pain_h0n3m6o9.md
  adult_neck_pain_i1o4n7p0.md
  adult_neck_pain_j2p5o8q1.md
```

## Generated Note Structure

Each markdown file contains:

```markdown
# SOAP Note

**ID:** a3f5d8e2-b4g6-4f9h-81ca-8c23ac17ac27
**Prompt Type:** adult_neck_pain
**Batch:** batch_006
**Generated:** 20251120_143052

---

## Subjective

42-year-old female presents with neck pain that started about 5 days ago.
Pain is currently 6/10, described as aching and stiff. States "I don't
remember doing anything specific, just woke up with it." Pain is mostly
on the right side of neck. Worse when turning head to the right and
looking down at computer. Better with heat. Tried ibuprofen with minimal
relief. Works as an insurance adjuster, spends 8-9 hours daily at computer.

## Objective

Posture: Forward head position, bilateral shoulder protraction
ROM: Cervical flexion 45/60 degrees, extension 50/70 degrees, right
rotation 60/80 degrees with pain, left rotation 70/80 degrees...

## Assessment

1. Cervicalgia | M54.2
2. Segmental dysfunction, cervical region | M99.01
3. Muscle spasm of neck | M62.838

## Plan

- Diversified adjustment C2-3, C5-6 right
- Drop table adjustment T1-2
- Manual therapy to right upper trapezius, levator scapulae...

## Billing

- 99203 (New patient, moderate complexity)
- 98940 (CMT, 1-2 regions)
- 97140 (Manual therapy, 1 unit)
- 97010 (Hot pack)
```

## Error Cases

### API Key Missing

```
❌ Error: ANTHROPIC_API_KEY Not Found

The synthetic-notes generator requires an Anthropic API key to be set.

Please configure the .env file in:
/Users/mpaz/workspace/synthetic-notes/.env

Add the line:
ANTHROPIC_API_KEY=your_api_key_here

Then run the skill again.
```

### Invalid Prompt Type

```
❌ Error: Invalid Prompt Type

Prompt type 'invalid_type' not recognized.

Available prompt types:

Adult Cases:
  - adult_trauma
  - adult_chronic_lbp
  - adult_neck_pain
  - adult_sports_injury

Pediatric Cases:
  - torticollis
  - plagiocephaly
  - feeding
  - wellness

Please select a valid prompt type and try again.
```

### Generation Failed

```
❌ Error: Generation Failed

Command exited with code 1

Error output:
Error generating batch 1: Rate limit exceeded. Please try again later.

Suggestions:
- Check your Anthropic API quota/credits
- Reduce batch size and try again
- Wait a few minutes and retry
```

## Progress Reporting

During execution, show progress if output is available:

```
⏳ Generating SOAP notes...

Prompt type: adult_neck_pain
Total notes: 10
Batch size: 2

Loading prompts...
Creating batch folder: batch_006
Generating batch 1 of 5...
  ✓ Tokens: 3,245 in / 1,892 out | Cost: $0.19
Generating batch 2 of 5...
  ✓ Tokens: 3,312 in / 1,945 out | Cost: $0.20
...
```
