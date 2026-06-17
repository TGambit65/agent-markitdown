from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
REVIEW_PACK_HANDOFF = ROOT / "examples" / "review-pack-consumers" / "review_pack_handoff.py"
AUTO_PREPROCESS_ADAPTER = (
    ROOT / "examples" / "auto-preprocess-adapters" / "agent_cli_prompt_adapter.py"
)


def test_review_pack_handoff_prints_prompt_and_warnings(tmp_path: Path) -> None:
    source = tmp_path / "short.txt"
    output = tmp_path / "pack.md"
    source.write_text("tiny", encoding="utf-8")
    env = os.environ.copy()
    env["PYTHONPATH"] = str(SRC)

    result = subprocess.run(
        [
            sys.executable,
            str(REVIEW_PACK_HANDOFF),
            str(source),
            "--output",
            str(output),
            "--converter-cmd",
            f"{sys.executable} -m agent_markitdown.cli",
        ],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert output.exists()
    assert "Review pack ready:" in result.stdout
    assert "surface these extraction warnings" in result.stdout
    assert "Extraction produced very little text" in result.stdout


def test_auto_preprocess_adapter_writes_profile_prompt_and_warnings(tmp_path: Path) -> None:
    source = tmp_path / "short.txt"
    review_pack = tmp_path / "pack.md"
    prompt_output = tmp_path / "prompt.txt"
    source.write_text("tiny", encoding="utf-8")
    env = os.environ.copy()
    env["PYTHONPATH"] = str(SRC)

    result = subprocess.run(
        [
            sys.executable,
            str(AUTO_PREPROCESS_ADAPTER),
            "--profile",
            "codex",
            str(source),
            "--review-pack",
            str(review_pack),
            "--prompt-output",
            str(prompt_output),
            "--converter-cmd",
            f"{sys.executable} -m agent_markitdown.cli",
        ],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert review_pack.exists()
    assert prompt_output.exists()
    prompt = prompt_output.read_text(encoding="utf-8")
    assert result.stdout == prompt
    assert "Codex task" in prompt
    assert f"Read this local review pack: {review_pack}" in prompt
    assert "Surface these extraction warnings" in prompt
    assert "Extraction produced very little text" in prompt
