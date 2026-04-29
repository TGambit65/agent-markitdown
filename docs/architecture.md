# Architecture

## Core idea

1. Host agent receives a supported document.
2. Host agent runs `agent-markitdown convert ...` or `review-pack ...` locally.
3. The converted markdown becomes the artifact the LLM reviews.
4. The original file remains available for provenance.

## Why markdown first

Most agent runtimes and LLM stacks handle markdown better than raw binary attachments.

Markdown is:
- easy to diff
- easy to chunk
- easy to cite
- cheap to feed back into agent loops

## Review pack format

`review-pack` creates a single markdown file with:
- source metadata
- file-by-file sections
- extracted markdown content

That makes it portable across OpenClaw, Claude Code, Codex, Hermes, and similar runtimes.
