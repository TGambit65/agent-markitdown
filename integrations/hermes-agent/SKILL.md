---
name: agent-markitdown
description: Preprocess supported local documents into markdown before deeper review or summarization work.
---

Use:

```bash
agent-markitdown convert /path/to/file.pdf --json
```

For multiple documents:

```bash
agent-markitdown review-pack /path/to/file1.pdf /path/to/file2.docx -o /tmp/review-pack.md
```
