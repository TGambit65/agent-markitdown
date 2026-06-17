---
name: agent-markitdown
description: Preprocess supported local documents into markdown before deeper review or summarization work.
---

Use:

```bash
agent-markitdown convert /path/to/file.pdf --json
```

Use the returned markdown as the main review artifact. If `warnings` is non-empty, surface those warnings and use OCR, PDF-native analysis, or vision when the markdown may be incomplete.

For multiple documents:

```bash
agent-markitdown review-pack /path/to/file1.pdf /path/to/file2.docx -o /tmp/review-pack.md
```
