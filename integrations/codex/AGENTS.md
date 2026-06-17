# agent-markitdown integration for Codex

Before analyzing a supported uploaded/local document, run:

```bash
agent-markitdown convert /path/to/file.pdf --json
```

Prefer the markdown output for quoting, summarizing, and review. Keep the original file path available for provenance.

If the JSON response includes non-empty `warnings`, mention those limits before relying on the markdown as complete. For multi-file review, prefer:

```bash
agent-markitdown review-pack /path/to/file1.pdf /path/to/file2.docx -o /tmp/review-pack.md
```
