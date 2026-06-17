# Review-Pack Consumer Examples

These examples show how a host agent can turn one or more local documents into a review-pack handoff.

The pattern is intentionally simple:

1. Run `agent-markitdown review-pack ... --json`.
2. Save the generated markdown bundle.
3. Surface any extraction warnings.
4. Pass the review-pack path and warnings to the agent runtime.

## Generic handoff prompt

```bash
python examples/review-pack-consumers/review_pack_handoff.py \
  ./report.pdf ./notes.docx \
  --output /tmp/agent-markitdown-review-pack.md
```

The script prints a prompt that can be sent to Codex, Claude Code, Hermes Agent, or any similar CLI that can read a local markdown file.

For projects that wrap a specific agent CLI, keep the same warning behavior: never hide a non-empty `warnings` array from the user or downstream model.
