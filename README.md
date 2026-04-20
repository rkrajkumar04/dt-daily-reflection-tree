# The Daily Reflection Tree

This repository contains a deterministic end-of-day reflection agent designed for the DT Fellowship assignment. The product is a fixed decision tree, not an LLM runtime experience.

## Repository Structure

- `tree/reflection-tree.json`: main tree data file
- `tree/tree-diagram.md`: Mermaid diagram of the branching structure
- `agent/run.py`: runnable CLI agent that loads the tree from file
- `transcripts/persona-1-transcript.md`: sample transcript for a more victim / entitled / self-focused path
- `transcripts/persona-2-transcript.md`: sample transcript for a more victor / contributing / altrocentric path
- `write-up.md`: design rationale and source grounding

## Design Notes

The tree moves through three axes in sequence:

1. Locus: external to internal
2. Orientation: entitlement to contribution
3. Radius: self-focused to altrocentric

Every question has fixed options. Every branch is deterministic. Reflections are static templates with interpolation from prior answers and computed dominant axis labels.

## How To Run

Requirements:

- Python 3.9+

Run:

```bash
python3 agent/run.py
```

Optionally pass a custom tree file:

```bash
python3 agent/run.py tree/reflection-tree.json
```

## How The Agent Works

- Loads the tree data from JSON
- Starts at `START`
- Renders question nodes and waits for a fixed-option choice
- Auto-advances through start, decision, bridge, reflection, summary, and end nodes
- Stores answers by node ID
- Tallies axis signals from chosen options
- Computes the dominant pole for each axis
- Interpolates placeholders such as `{OPEN_TONE.answer}` and `{axis1.dominantLabel}`

## Submission Notes

Part A is fully covered by:

- the tree data file
- the visual tree diagram
- the design write-up

Part B bonus is covered by:

- the runnable CLI agent
- the sample transcripts
