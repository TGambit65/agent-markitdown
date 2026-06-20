# agent-markitdown Task List

## Current release work

- [x] Create standalone shared repo in `/home/thoder/projects/agent-markitdown`
- [x] Build safe local converter CLI and review-pack flow
- [x] Add OpenClaw, Claude Code, Codex, and Hermes integration assets
- [x] Push initial public GitHub repo
- [x] Add GitHub Actions CI for tests and package build
- [x] Add release workflow for tagged releases and PyPI publishing
- [x] Tighten README with install, release, and integration guidance
- [x] Add changelog / release checklist
- [x] Verify source and wheel builds locally
- [x] Create and push first release tag
- [x] Publish to PyPI — DONE 2026-06-19. `PYPI_API_TOKEN` secret added by Kelly; v0.1.1 published via release workflow. Live at https://pypi.org/project/agent-markitdown/ and verified installable in a clean venv.
- [x] If PyPI publish blocks, document exact remaining one-time setup cleanly

## Current blocker

- None. v0.1.1 shipped to PyPI 2026-06-19.

## Stretch / follow-up

- [x] Add OCR/degraded-scan warning story for low-text and image inputs
- [x] Optional host-specific auto-preprocess adapters beyond docs
- [x] Example review-pack consumers for more agent frameworks
