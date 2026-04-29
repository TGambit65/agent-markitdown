# Publishing

`agent-markitdown` supports two PyPI publishing paths through GitHub Actions:

## Option 1: API token

1. Create the project or token on PyPI.
2. Add `PYPI_API_TOKEN` as a GitHub Actions secret.
3. Push a tag like `v0.1.0`.
4. The release workflow will publish automatically.

## Option 2: Trusted publishing

1. Configure this GitHub repository as a trusted publisher for the PyPI project.
2. Set repository variable `PYPI_TRUSTED_PUBLISHING=true`.
3. Push a release tag.
4. The release workflow will publish using GitHub OIDC.

## Notes

- If neither token nor trusted publishing is configured, the release workflow still builds artifacts and creates a GitHub release, but PyPI publish steps are skipped.
- The safest first move is to get CI green, then configure PyPI, then push the release tag.
