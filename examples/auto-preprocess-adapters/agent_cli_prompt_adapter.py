#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


PROFILE_INSTRUCTIONS = {
    "codex": "Use the review pack as the primary document context for this Codex task.",
    "claude-code": "Use the review pack as the primary document context for this Claude Code task.",
    "hermes-agent": "Use the review pack as the primary document context for this Hermes Agent task.",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build an agent-markitdown review pack and emit a host-agent prompt.",
    )
    parser.add_argument(
        "--profile",
        choices=sorted(PROFILE_INSTRUCTIONS),
        required=True,
        help="Host-agent profile used to word the generated prompt.",
    )
    parser.add_argument("inputs", nargs="+", help="Local documents to preprocess")
    parser.add_argument(
        "--review-pack",
        help="Review-pack markdown output path. Defaults to a temp file.",
    )
    parser.add_argument(
        "--prompt-output",
        help="Optional path for the generated prompt. The prompt is always printed.",
    )
    parser.add_argument(
        "--converter-cmd",
        default="agent-markitdown",
        help="Command used to invoke agent-markitdown. Useful for tests or editable checkouts.",
    )
    return parser


def _temp_path(prefix: str, suffix: str) -> Path:
    handle = tempfile.NamedTemporaryFile(prefix=prefix, suffix=suffix, delete=False)
    handle.close()
    return Path(handle.name)


def _collect_warnings(payload: dict[str, Any]) -> list[str]:
    warnings: list[str] = []
    for item in payload.get("files", []):
        source = item.get("input_path", "[unknown]")
        for warning in item.get("warnings", []):
            warnings.append(f"{source}: {warning}")
    return warnings


def _build_prompt(profile: str, review_pack: Path, warnings: list[str]) -> str:
    lines = [
        PROFILE_INSTRUCTIONS[profile],
        f"Read this local review pack: {review_pack}",
        "Preserve source paths from the pack when citing or reporting findings.",
    ]
    if warnings:
        lines.extend(
            [
                "",
                "Surface these extraction warnings before treating the markdown as complete:",
                *[f"- {warning}" for warning in warnings],
            ]
        )
    else:
        lines.extend(["", "agent-markitdown reported no extraction warnings."])
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    review_pack = (
        Path(args.review_pack).expanduser().resolve()
        if args.review_pack
        else _temp_path("agent-markitdown-review-pack-", ".md")
    )
    prompt_output = (
        Path(args.prompt_output).expanduser().resolve()
        if args.prompt_output
        else None
    )
    command = [
        *shlex.split(args.converter_cmd),
        "review-pack",
        *args.inputs,
        "--output",
        str(review_pack),
        "--json",
    ]
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        sys.stderr.write(result.stderr or result.stdout)
        return result.returncode

    payload = json.loads(result.stdout)
    prompt = _build_prompt(args.profile, review_pack, _collect_warnings(payload))
    if prompt_output is not None:
        prompt_output.parent.mkdir(parents=True, exist_ok=True)
        prompt_output.write_text(prompt, encoding="utf-8")
    sys.stdout.write(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
