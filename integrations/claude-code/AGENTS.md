# agent-markitdown integration for Claude Code

When the user asks to review, summarize, or extract from a supported document, convert it to markdown first:

```bash
agent-markitdown convert /path/to/file.pdf --json
```

Use the returned markdown as the main artifact for analysis.

Check the JSON `warnings` array. If it is non-empty, tell the user what may be missing and use OCR, PDF-native analysis, or vision when the missing content matters.

For multi-document review bundles:

```bash
agent-markitdown review-pack /path/to/file1.pdf /path/to/file2.docx -o /tmp/review-pack.md
```
