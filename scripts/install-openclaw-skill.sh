#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_DIR="${1:-$HOME/.claudeagent/workspace/skills/markitdown}"
mkdir -p "$TARGET_DIR"
cp "$REPO_ROOT/integrations/openclaw/SKILL.md" "$TARGET_DIR/SKILL.md"
echo "Installed OpenClaw skill to $TARGET_DIR/SKILL.md"
