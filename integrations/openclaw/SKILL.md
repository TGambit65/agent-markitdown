---
name: markitdown
description: Convert uploaded or local documents into markdown before deeper agent review. Use when the user provides a PDF, DOCX, PPTX, XLSX, HTML, CSV, JSON, XML, EPUB, or common image file and wants the text/content extracted, summarized, reviewed, or reused as markdown.
---

# agent-markitdown for OpenClaw

When a user asks to review or summarize a supported document, preprocess it with `agent-markitdown` first when that is cheaper and more reliable than a direct heavyweight document-analysis path.

## Use it for

- `.pdf`
- `.docx`
- `.pptx`
- `.xlsx`, `.xls`
- `.html`, `.csv`, `.json`, `.xml`, `.txt`, `.md`, `.rtf`, `.epub`
- common image formats when markdown extraction is useful

## Preferred flow

1. Locate the uploaded file's local path.
2. Run:

```bash
agent-markitdown convert /path/to/file.pdf --json
```

3. Use the returned markdown as the main review artifact.
4. Preserve the original file path for provenance.
5. If the user wants a reusable artifact, write a sidecar or review pack.

## Reusable artifacts

Write a sidecar markdown file:

```bash
agent-markitdown convert /path/to/file.pdf --sidecar
```

Create one review bundle for multiple docs:

```bash
agent-markitdown review-pack /path/to/file1.pdf /path/to/file2.docx -o /tmp/review-pack.md
```

## Notes

- This tool is local-only by design.
- Plugins are off by default.
- ZIP files are intentionally blocked.
- If the document is badly scanned or the extraction is obviously degraded, say so and switch to a richer OCR/PDF path.
