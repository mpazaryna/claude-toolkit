# Synthetic Notes Generator Agent

**Type**: Autonomous Python Agent
**Purpose**: Generate synthetic clinical SOAP notes for training datasets

## Overview

This is a fully autonomous Python agent that generates realistic chiropractic SOAP notes. Unlike skills that use Claude Code as the executor, this agent is pure Python code that runs independently and reports structured results.

## Architecture

```
Orchestrator
    ↓
    Spawns Agent (Python process)
    ↓
SynthNotesAgent.execute(config)
    ├── Loads prompts from synthetic-notes repo
    ├── Calls Anthropic API directly
    ├── Generates notes in batches
    ├── Writes files to batch folders
    └── Returns structured results
    ↓
Orchestrator receives results
```

## Key Characteristics

### Autonomous
- Runs independently without Claude Code
- Makes own API calls to Anthropic
- Manages file operations directly
- No shared context with orchestrator

### Self-Contained
- Single Python file (`agent.py`)
- No external dependencies beyond Anthropic SDK
- Reads prompts from synthetic-notes repo
- Writes outputs to synthetic-notes/output/

### Structured Results
Returns comprehensive execution report:
```python
{
    'status': 'success',
    'notes_generated': 10,
    'batch_folder': 'batch_006',
    'batch_folder_path': '/Users/mpaz/workspace/synthetic-notes/output/batch_006',
    'files_created': ['adult_neck_pain_a3f5d8e2.md', ...],
    'usage': {
        'api_calls': 5,
        'input_tokens': 16225,
        'output_tokens': 9460,
        'total_tokens': 25685,
        'input_cost': 0.2434,
        'output_cost': 0.7095,
        'total_cost': 0.9529
    }
}
```

## Usage

### Via Orchestrator

```python
from claude_toolkit.generated_agents.synth_notes_generator.agent import SynthNotesAgent

# Initialize agent
agent = SynthNotesAgent(
    api_key=os.getenv('ANTHROPIC_API_KEY'),
    synthetic_notes_path='/Users/mpaz/workspace/synthetic-notes'
)

# Execute generation
result = agent.execute({
    'prompt_type': 'adult_neck_pain',
    'total': 10,
    'batch_size': 2
})

# Check results
if result['status'] == 'success':
    print(f"Generated {result['notes_generated']} notes")
    print(f"Cost: ${result['usage']['total_cost']}")
```

### Standalone CLI

```bash
cd /Users/mpaz/workspace/claude-toolkit/generated-agents/synth-notes-generator

python agent.py \
    --prompt-type adult_neck_pain \
    --total 10 \
    --batch-size 2
```

## Configuration

### Required
- `prompt_type` (str) - Clinical scenario to generate

### Optional
- `total` (int, default: 10) - Total notes to generate
- `batch_size` (int, default: 2) - Notes per API call

### Valid Prompt Types

**Adult Cases:**
- adult_trauma
- adult_chronic_lbp
- adult_neck_pain
- adult_sports_injury

**Pediatric Cases:**
- torticollis
- plagiocephaly
- feeding
- wellness

## Output Structure

Notes are saved to auto-numbered batch folders:

```
/Users/mpaz/workspace/synthetic-notes/output/
  batch_001/
    adult_neck_pain_a3f5d8e2.md
    adult_neck_pain_b4g6f9h3.md
  batch_002/
    adult_chronic_lbp_c5h7g0i4.md
```

Each note includes:
- Unique ID (UUID)
- Metadata (prompt type, batch, timestamp)
- Full SOAP note content

## Dependencies

```python
# From standard library
import math, uuid, os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

# External
from anthropic import Anthropic
```

## Error Handling

The agent validates:
- ✅ Prompt type is valid
- ✅ Numeric parameters are positive integers
- ✅ Synthetic-notes repo exists
- ✅ Prompts directory exists
- ✅ API key is available

Returns error dict if validation fails:
```python
{
    'status': 'error',
    'message': 'Invalid prompt_type...'
}
```

## Cost Tracking

Full transparency on API costs:
- Input: $15.00 per million tokens
- Output: $75.00 per million tokens
- Typical batch of 10 notes: $0.50-$2.00

## Comparison to Bash Wrapper Skill

### Old Approach (Bash Wrapper)
```
Orchestrator → Claude Code Agent → run_bash → Python script → Notes
```
- Agent orchestrates subprocess
- Hard to track file creation
- Parses stderr for stats
- Two layers of execution

### New Approach (Python Agent)
```
Orchestrator → Python Agent → Notes
```
- Direct execution
- Native file tracking
- Structured results
- Single layer

## Integration with Orchestrator

The orchestrator will instantiate and execute this agent:

```python
# In orchestrator's agent execution path
from claude_toolkit.generated_agents.synth_notes_generator.agent import SynthNotesAgent

def execute_agent(agent_config, task_config):
    if agent_config['name'] == 'synth-notes-generator':
        agent = SynthNotesAgent()
        return agent.execute(task_config)
```

## Testing

Test the agent standalone:

```bash
python agent.py --prompt-type adult_neck_pain --total 5 --batch-size 2
```

Expected output:
```
[SynthNotesAgent] Starting generation:
  Prompt type: adult_neck_pain
  Total notes: 5
  Batch size: 2
  Batch folder: batch_006
  Generating batch 1/3 (2 notes)...
    ✓ Tokens: 3,245 in / 1,892 out | Cost: $0.1905
  Generating batch 2/3 (2 notes)...
    ✓ Tokens: 3,312 in / 1,945 out | Cost: $0.1968
  Generating batch 3/3 (1 notes)...
    ✓ Tokens: 3,156 in / 1,823 out | Cost: $0.1841
[SynthNotesAgent] Complete!
  Notes generated: 5
  Total cost: $0.5714

✅ Success!
   Batch: batch_006
   Notes: 5
   Cost: $0.5714
```

## Future Enhancements

- [ ] Parallel batch generation
- [ ] Resume from interrupted generation
- [ ] Quality validation hooks
- [ ] Custom prompt template support
- [ ] Batch folder cleanup/management
- [ ] Supabase upload integration

## Files

```
synth-notes-generator/
├── agent.py        # Main agent implementation
├── README.md       # This file
└── AGENT.json      # Agent metadata for orchestrator
```
