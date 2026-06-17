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
- extraction warnings
- file-by-file sections
- extracted markdown content

That makes it portable across OpenClaw, Claude Code, Codex, Hermes, and similar runtimes.

## Extraction limits

`agent-markitdown` is a local markdown preprocessing layer, not an OCR system.

Converted files include warnings when extraction looks incomplete:
- very low extracted text warns that scanned or degraded documents may need OCR/vision
- image inputs warn that visual text and layout may not be represented in markdown

Host agents should surface those warnings before relying on the markdown as the full document contents.
