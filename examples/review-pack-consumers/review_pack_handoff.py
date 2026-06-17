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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build an agent-markitdown review pack and print a reusable agent handoff prompt.",
    )
    parser.add_argument("inputs", nargs="+", help="Local documents to include in the review pack")
    parser.add_argument(
        "-o",
        "--output",
        help="Review-pack markdown output path. Defaults to a temp file.",
    )
    parser.add_argument(
        "--converter-cmd",
        default="agent-markitdown",
        help="Command used to invoke agent-markitdown. Useful for tests or editable checkouts.",
    )
    return parser


def _collect_warnings(payload: dict[str, Any]) -> list[str]:
    warnings: list[str] = []
    for item in payload.get("files", []):
        source = item.get("input_path", "[unknown]")
        for warning in item.get("warnings", []):
            warnings.append(f"{source}: {warning}")
    return warnings


def _default_output_path() -> Path:
    handle = tempfile.NamedTemporaryFile(
        prefix="agent-markitdown-review-pack-",
        suffix=".md",
        delete=False,
    )
    handle.close()
    return Path(handle.name)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    output_path = Path(args.output).expanduser().resolve() if args.output else _default_output_path()
    converter_cmd = shlex.split(args.converter_cmd)
    command = [
        *converter_cmd,
        "review-pack",
        *args.inputs,
        "--output",
        str(output_path),
        "--json",
    ]
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        sys.stderr.write(result.stderr or result.stdout)
        return result.returncode

    payload = json.loads(result.stdout)
    warnings = _collect_warnings(payload)

    print(f"Review pack ready: {output_path}")
    print()
    print("Use this handoff prompt with your agent runtime:")
    print()
    print(f"Read the review pack at {output_path} and use it as the primary document context.")
    print("Keep the original source paths in the pack for provenance.")
    if warnings:
        print("Before relying on the markdown as complete, surface these extraction warnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("No extraction warnings were reported by agent-markitdown.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
