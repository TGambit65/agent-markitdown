# Release Checklist

## Before tagging
- Run `pytest -q`
- Run `uv build`
- Confirm README and CHANGELOG reflect the release
- Confirm integration docs still match actual behavior
- Bump `version` in `pyproject.toml` (single source of truth; `__init__.py` reads it at runtime from package metadata)

## Tag and release
- Create annotated tag: `git tag -a vX.Y.Z -m "vX.Y.Z"`
- Push tag: `git push origin vX.Y.Z`
- Confirm GitHub Actions release workflow completes
- Confirm GitHub release contains wheel and sdist artifacts

## PyPI
- If using API token, set `PYPI_API_TOKEN` repo secret
- If using trusted publishing, configure the project on PyPI and set repo variable `PYPI_TRUSTED_PUBLISHING=true`
- Re-run or re-tag only after PyPI configuration is ready
