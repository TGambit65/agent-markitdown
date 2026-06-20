# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

## [0.1.2] - 2026-06-20

### Added
- `--version` flag and a `version` field in `doctor` output.

### Fixed
- `__version__` is now derived from installed package metadata (single source of truth), fixing the stale `0.1.0` it reported while the package was `0.1.1`.

## [0.1.1] - 2026-06-19

### Added
- Extraction warnings for low-text results and image inputs that may need OCR/vision fallback.
- Example review-pack handoff consumer for Codex, Claude Code, Hermes, and similar local agent CLIs.
- Example host-side auto-preprocess adapter that emits profile-specific agent prompts.

### Fixed
- Python 3.10 support and clean source builds.

## [0.1.0] - 2026-04-28

### Added
- Initial `agent-markitdown` CLI with safe local-only conversion
- `review-pack` markdown bundle output for multi-document agent review
- OpenClaw, Claude Code, Codex, and Hermes integration assets
- Test coverage for DOCX, PDF, doctor, bundling, and guardrail behavior
- GitHub Actions CI and release workflows
