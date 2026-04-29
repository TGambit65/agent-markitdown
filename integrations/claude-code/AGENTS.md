# agent-markitdown integration for Claude Code

When the user asks to review, summarize, or extract from a supported document, convert it to markdown first:

```bash
agent-markitdown convert /path/to/file.pdf --json
```

Use the returned markdown as the main artifact for analysis.

For multi-document review bundles:

```bash
agent-markitdown review-pack /path/to/file1.pdf /path/to/file2.docx -o /tmp/review-pack.md
```
