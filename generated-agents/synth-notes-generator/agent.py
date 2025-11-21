"""
Synthetic Notes Generator Agent

Autonomous agent for generating synthetic clinical SOAP notes.
This agent operates independently, making API calls and managing file operations
to create batches of realistic chiropractic documentation.
"""

import math
import uuid
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List
from anthropic import Anthropic


class SynthNotesAgent:
    """
    Autonomous agent for SOAP note generation.

    This agent:
    - Reads prompt templates from synthetic-notes repo
    - Calls Anthropic API to generate notes
    - Writes notes to batch folders
    - Tracks usage and costs
    - Reports comprehensive results
    """

    # Pricing constants (Claude Opus 4)
    PRICE_PER_MILLION_INPUT = 15.00
    PRICE_PER_MILLION_OUTPUT = 75.00

    # Valid prompt types
    ADULT_PROMPTS = ["adult_trauma", "adult_chronic_lbp", "adult_neck_pain", "adult_sports_injury"]
    PEDIATRIC_PROMPTS = ["torticollis", "plagiocephaly", "feeding", "wellness"]
    ALL_PROMPTS = ADULT_PROMPTS + PEDIATRIC_PROMPTS

    def __init__(self, api_key: str = None, synthetic_notes_path: str = None):
        """
        Initialize agent.

        Args:
            api_key: Anthropic API key (default: from ANTHROPIC_API_KEY env var)
            synthetic_notes_path: Path to synthetic-notes repo (default: ~/workspace/synthetic-notes)
        """
        # Initialize Anthropic client
        self.client = Anthropic(api_key=api_key or os.getenv('ANTHROPIC_API_KEY'))

        # Determine synthetic-notes path
        if synthetic_notes_path:
            self.synth_notes_path = Path(synthetic_notes_path)
        else:
            self.synth_notes_path = Path.home() / "workspace" / "synthetic-notes"

        self.prompts_dir = self.synth_notes_path / "prompts"
        self.output_dir = self.synth_notes_path / "output"

        # Verify paths exist
        if not self.synth_notes_path.exists():
            raise FileNotFoundError(f"Synthetic-notes repo not found at: {self.synth_notes_path}")
        if not self.prompts_dir.exists():
            raise FileNotFoundError(f"Prompts directory not found at: {self.prompts_dir}")

        # Usage tracking
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.batch_calls = 0

    def execute(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute autonomous note generation.

        Args:
            config: {
                'prompt_type': str (required) - e.g. 'adult_neck_pain'
                'total': int (default: 10) - total notes to generate
                'batch_size': int (default: 2) - notes per API call
            }

        Returns:
            dict with execution results:
            {
                'status': 'success' | 'error',
                'notes_generated': int,
                'batch_folder': str,
                'batch_folder_path': str,
                'files_created': List[str],
                'usage': {
                    'api_calls': int,
                    'input_tokens': int,
                    'output_tokens': int,
                    'total_tokens': int,
                    'input_cost': float,
                    'output_cost': float,
                    'total_cost': float
                },
                'message': str (if error)
            }
        """
        try:
            # Validate and extract config
            prompt_type = config.get('prompt_type')
            if not prompt_type:
                return self._error("Missing required parameter: prompt_type")

            if prompt_type not in self.ALL_PROMPTS:
                return self._error(
                    f"Invalid prompt_type '{prompt_type}'. "
                    f"Valid options: {', '.join(self.ALL_PROMPTS)}"
                )

            total = config.get('total', 10)
            batch_size = config.get('batch_size', 2)

            # Validate numeric params
            if not isinstance(total, int) or total <= 0:
                return self._error(f"Invalid total: {total}. Must be positive integer.")
            if not isinstance(batch_size, int) or batch_size <= 0:
                return self._error(f"Invalid batch_size: {batch_size}. Must be positive integer.")

            print(f"[SynthNotesAgent] Starting generation:")
            print(f"  Prompt type: {prompt_type}")
            print(f"  Total notes: {total}")
            print(f"  Batch size: {batch_size}")

            # Load prompts
            system_prompt = self._load_prompts(prompt_type)

            # Determine batch folder
            batch_folder_name = self._get_next_batch_folder()
            batch_folder_path = self.output_dir / batch_folder_name

            print(f"  Batch folder: {batch_folder_name}")

            # Create batch folder
            batch_folder_path.mkdir(parents=True, exist_ok=True)

            # Generate notes in batches
            all_notes = []
            num_batches = math.ceil(total / batch_size)

            for batch_num in range(1, num_batches + 1):
                notes_in_batch = min(batch_size, total - len(all_notes))
                print(f"  Generating batch {batch_num}/{num_batches} ({notes_in_batch} notes)...")

                batch_notes = self._generate_batch(
                    system_prompt=system_prompt,
                    prompt_type=prompt_type,
                    batch_size=notes_in_batch,
                    batch_number=batch_num
                )

                all_notes.extend(batch_notes)

                # Early exit if we have enough notes
                if len(all_notes) >= total:
                    break

            # Write notes to files
            files_created = []
            for note in all_notes[:total]:  # Limit to requested total
                filename = self._write_note(note, batch_folder_path, batch_folder_name)
                files_created.append(filename)

            # Calculate costs
            usage_stats = self._calculate_usage()

            print(f"[SynthNotesAgent] Complete!")
            print(f"  Notes generated: {len(files_created)}")
            print(f"  Total cost: ${usage_stats['total_cost']:.4f}")

            return {
                'status': 'success',
                'notes_generated': len(files_created),
                'batch_folder': batch_folder_name,
                'batch_folder_path': str(batch_folder_path),
                'files_created': files_created,
                'usage': usage_stats
            }

        except Exception as e:
            import traceback
            traceback.print_exc()
            return self._error(f"Execution failed: {str(e)}")

    def _load_prompts(self, prompt_type: str) -> str:
        """Load and combine base + condition prompts."""
        # Determine base prompt
        if prompt_type in self.ADULT_PROMPTS:
            base_file = self.prompts_dir / "adult_base_system.md"
        else:
            base_file = self.prompts_dir / "base_system.md"

        # Read base prompt
        if not base_file.exists():
            raise FileNotFoundError(f"Base prompt not found: {base_file}")

        with open(base_file, 'r', encoding='utf-8') as f:
            base_prompt = f.read()

        # Read condition-specific prompt
        condition_file = self.prompts_dir / f"{prompt_type}.md"
        if not condition_file.exists():
            raise FileNotFoundError(f"Condition prompt not found: {condition_file}")

        with open(condition_file, 'r', encoding='utf-8') as f:
            condition_prompt = f.read()

        # Combine prompts
        return f"{base_prompt}\n\n---\n\n{condition_prompt}"

    def _get_next_batch_folder(self) -> str:
        """Find next available batch folder number."""
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

        batch_num = 1
        while True:
            batch_folder_name = f"batch_{batch_num:03d}"
            batch_path = self.output_dir / batch_folder_name
            if not batch_path.exists():
                return batch_folder_name
            batch_num += 1

    def _generate_batch(
        self,
        system_prompt: str,
        prompt_type: str,
        batch_size: int,
        batch_number: int
    ) -> List[Dict[str, Any]]:
        """Generate a batch of notes via Anthropic API."""
        # Determine patient type
        patient_type = "adult" if prompt_type in self.ADULT_PROMPTS else "pediatric"

        # Construct user prompt
        user_prompt = f"""Generate {batch_size} synthetic {patient_type} chiropractic SOAP notes based on the focus areas described above.

Separate each note with ---NEXT NOTE--- delimiter.
Output ONLY the notes, nothing else."""

        # Call Anthropic API
        response = self.client.messages.create(
            model="claude-opus-4-1-20250805",
            max_tokens=8000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}]
        )

        # Track usage
        self.total_input_tokens += response.usage.input_tokens
        self.total_output_tokens += response.usage.output_tokens
        self.batch_calls += 1

        # Calculate batch cost
        batch_cost = (
            (response.usage.input_tokens / 1_000_000 * self.PRICE_PER_MILLION_INPUT) +
            (response.usage.output_tokens / 1_000_000 * self.PRICE_PER_MILLION_OUTPUT)
        )

        print(f"    ✓ Tokens: {response.usage.input_tokens:,} in / {response.usage.output_tokens:,} out | Cost: ${batch_cost:.4f}")

        # Parse response
        raw_text = response.content[0].text
        notes_raw = raw_text.split("---NEXT NOTE---")

        notes = []
        for note_text in notes_raw:
            note_text = note_text.strip()
            if note_text:  # Skip empty strings
                notes.append({
                    'guid': str(uuid.uuid4()),
                    'content': note_text,
                    'prompt_type': prompt_type
                })

        return notes

    def _write_note(self, note: Dict[str, Any], batch_folder: Path, batch_folder_name: str) -> str:
        """Write a single note to file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        short_guid = note['guid'][:8]
        filename = f"{note['prompt_type']}_{short_guid}.md"
        filepath = batch_folder / filename

        # Create markdown content with metadata
        content = f"""# SOAP Note

**ID:** {note['guid']}
**Prompt Type:** {note['prompt_type']}
**Batch:** {batch_folder_name}
**Generated:** {timestamp}

---

{note['content']}
"""

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return filename

    def _calculate_usage(self) -> Dict[str, Any]:
        """Calculate usage statistics and costs."""
        input_cost = (self.total_input_tokens / 1_000_000) * self.PRICE_PER_MILLION_INPUT
        output_cost = (self.total_output_tokens / 1_000_000) * self.PRICE_PER_MILLION_OUTPUT
        total_cost = input_cost + output_cost

        return {
            'api_calls': self.batch_calls,
            'input_tokens': self.total_input_tokens,
            'output_tokens': self.total_output_tokens,
            'total_tokens': self.total_input_tokens + self.total_output_tokens,
            'input_cost': round(input_cost, 4),
            'output_cost': round(output_cost, 4),
            'total_cost': round(total_cost, 4)
        }

    def _error(self, message: str) -> Dict[str, Any]:
        """Return error result."""
        return {
            'status': 'error',
            'message': message
        }


def main():
    """CLI entry point for testing."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate synthetic SOAP notes")
    parser.add_argument('--prompt-type', required=True, choices=SynthNotesAgent.ALL_PROMPTS)
    parser.add_argument('--total', type=int, default=10)
    parser.add_argument('--batch-size', type=int, default=2)

    args = parser.parse_args()

    agent = SynthNotesAgent()
    result = agent.execute({
        'prompt_type': args.prompt_type,
        'total': args.total,
        'batch_size': args.batch_size
    })

    if result['status'] == 'success':
        print(f"\n✅ Success!")
        print(f"   Batch: {result['batch_folder']}")
        print(f"   Notes: {result['notes_generated']}")
        print(f"   Cost: ${result['usage']['total_cost']}")
    else:
        print(f"\n❌ Error: {result['message']}")


if __name__ == '__main__':
    main()
