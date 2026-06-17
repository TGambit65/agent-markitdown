# Auto-Preprocess Adapter Examples

These examples show the thin host-side layer that turns document paths into a markdown review pack before handing work to an agent CLI.

The adapter does three things:

1. Runs `agent-markitdown review-pack ... --json`.
2. Writes a prompt that points the agent at the generated review pack.
3. Includes extraction warnings in that prompt so the host does not hide degraded extraction.

## Generate a Codex-oriented prompt

```bash
python examples/auto-preprocess-adapters/agent_cli_prompt_adapter.py \
  --profile codex \
  ./report.pdf ./notes.docx
```

## Write prompt and review pack to stable paths

```bash
python examples/auto-preprocess-adapters/agent_cli_prompt_adapter.py \
  --profile claude-code \
  ./report.pdf \
  --review-pack /tmp/review-pack.md \
  --prompt-output /tmp/agent-prompt.txt
```

The printed prompt can be passed to a host CLI or session API. Keep this as an adapter layer; the core package should remain local-only and agent-agnostic.
