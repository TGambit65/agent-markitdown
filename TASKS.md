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
- [ ] BLOCKED-EXTERNAL Publish to PyPI once credentials or trusted publishing are ready. Owner: Kelly/repo admin. Next: add `PYPI_API_TOKEN` secret or set `PYPI_TRUSTED_PUBLISHING=true` plus PyPI trusted-publisher setup.
- [x] If PyPI publish blocks, document exact remaining one-time setup cleanly

## Current blocker

- BLOCKED-EXTERNAL Publish to PyPI. Owner: Kelly/repo admin. Next: add `PYPI_API_TOKEN` secret or set `PYPI_TRUSTED_PUBLISHING=true` plus PyPI trusted-publisher setup. Current state: GitHub Actions release workflow is ready, but this repo currently has neither the secret nor the trusted-publishing configuration yet.

## Stretch / follow-up

- [x] Add OCR/degraded-scan warning story for low-text and image inputs
- [x] Optional host-specific auto-preprocess adapters beyond docs
- [x] Example review-pack consumers for more agent frameworks
