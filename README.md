# agent-markitdown

Safe local document-to-markdown preprocessing for agents.

Built for OpenClaw first, but intentionally usable from Claude Code, Codex, Hermes Agent, and anything else that can run a local CLI or Python package.

## What it is

`agent-markitdown` wraps Microsoft's excellent [`markitdown`](https://github.com/microsoft/markitdown) with an agent-oriented safety and workflow layer:

- local files only
- `convert_local()` only
- plugins off by default
- extension allowlist
- size guardrail
- deterministic JSON output
- review-pack generation for LLM handoff

## Why this exists

Raw file uploads are awkward for agent workflows.

For supported document types, agents usually work better when they receive clean markdown instead of a binary attachment or a heavyweight vision/PDF pass.

That means:

- lower context overhead
- easier quoting and summarization
- better portability across agent runtimes
- safer, narrower preprocessing than raw `markitdown convert()`

## What it is not

This package does **not** magically patch every agent runtime on earth.

It gives you a safe preprocessing layer plus integration assets. Each host agent still needs a tiny adapter or instruction layer telling it to run `agent-markitdown` before review.

OpenClaw gets a ready-made skill. Other agents get drop-in snippets.

## Installation

```bash
uv venv .venv
uv pip install --python .venv/bin/python .
# or with test/dev dependencies
uv pip install --python .venv/bin/python '.[dev]'
```

Or from PyPI later:

```bash
pip install agent-markitdown
```

## CLI

### Convert one file to stdout

```bash
agent-markitdown convert ./report.pdf
```

### Convert and emit JSON

```bash
agent-markitdown convert ./report.docx --json
```

### Write sidecar markdown files

```bash
agent-markitdown convert ./report.pdf ./notes.docx --sidecar
```

### Build one review bundle for an agent

```bash
agent-markitdown review-pack ./report.pdf ./notes.docx -o review-pack.md
```

### Health check

```bash
agent-markitdown doctor
```

## Supported extensions

- `.pdf`
- `.docx`
- `.pptx`
- `.xlsx`
- `.xls`
- `.html`, `.htm`
- `.csv`, `.tsv`
- `.json`, `.xml`
- `.txt`, `.md`, `.rtf`
- `.epub`
- `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tif`, `.tiff`, `.webp`

## OpenClaw

See [`integrations/openclaw/SKILL.md`](integrations/openclaw/SKILL.md).

That skill tells OpenClaw to preprocess supported uploaded documents into markdown **before deeper review/summarization work**.

## Other agents

- Claude Code: [`integrations/claude-code/AGENTS.md`](integrations/claude-code/AGENTS.md)
- Codex: [`integrations/codex/AGENTS.md`](integrations/codex/AGENTS.md)
- Hermes Agent: [`integrations/hermes-agent/SKILL.md`](integrations/hermes-agent/SKILL.md)

## Security stance

This package intentionally avoids the broadest `markitdown` surfaces.

- no remote URLs
- no `convert()`
- no plugins unless explicitly enabled
- no ZIP traversal support
- explicit extension allowlist
- configurable size cap

If you're handling untrusted uploads in a server context, keep validating paths and storing uploads in a controlled temp area. This package narrows the blast radius; it does not replace sane host hygiene.

## Attribution

This project depends on and is inspired by Microsoft's `markitdown`, which is MIT licensed.
