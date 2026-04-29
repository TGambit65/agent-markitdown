# Project Context

## Purpose
`agent-markitdown` is a small, portable preprocessing layer that converts supported local documents into markdown before deeper agent review. It is built for OpenClaw first, but it must stay agent-agnostic enough for Claude Code, Codex, Hermes Agent, and similar local-first agent runtimes.

## Stack
- Python 3.10+
- Packaging/build: Hatchling
- Primary dependency: `markitdown`
- Test stack: `pytest`, `python-docx`, `reportlab`
- CI/CD: GitHub Actions

## Critical Rules
- Local files only by default; no remote URL fetching in core flows.
- Use `MarkItDown.convert_local()` rather than the broad `convert()` surface.
- Keep plugins off by default; any widening must be explicit and documented.
- Preserve deterministic JSON output so agents can script around results.
- OpenClaw support matters, but core package behavior must not depend on OpenClaw internals.

## Architecture Constraints
- Core package lives under `src/agent_markitdown/` and stays free of agent-specific imports.
- Agent integrations live under `integrations/` as thin adapter docs/assets.
- `review-pack` is the portable interchange surface for multi-file review handoff.
- Security guardrails belong in the converter layer, not just in docs.

## File Conventions
- Core code: `src/agent_markitdown/`
- Tests: `tests/`
- Integration-specific instructions/assets: `integrations/<agent>/`
- High-signal docs only: `README.md`, `docs/`, `project-context.md`, `TASKS.md`

## Testing Expectations
- Keep CLI subprocess tests for the real user path.
- Cover at least one DOCX path, one PDF path, one bundling path, and guardrail failures.
- Run `pytest` before every release-facing commit.
- Build artifacts locally before tagging a release.

## Anti-Patterns / Non-Goals
- Do not silently expand into remote fetching or broad untrusted I/O.
- Do not hardwire OpenClaw-specific behavior into the package core.
- Do not market “automatic preprocessing” unless the host integration actually wires it in.
- Do not treat OCR-heavy or degraded scans as solved when they are not.
