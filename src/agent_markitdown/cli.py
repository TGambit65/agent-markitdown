from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .converter import (
    DEFAULT_MAX_MB,
    build_review_pack,
    convert_file,
    default_output_path,
    supported_extensions,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agent-markitdown",
        description="Safe local document-to-markdown preprocessing for agents.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    convert = subparsers.add_parser("convert", help="Convert one or more files to markdown")
    convert.add_argument("inputs", nargs="+", help="Local files to convert")
    convert.add_argument("-o", "--output", help="Output file path (single input only)")
    convert.add_argument("--sidecar", action="store_true", help="Write <file><ext>.md next to each source")
    convert.add_argument("--json", action="store_true", help="Emit structured JSON")
    convert.add_argument("--plugins", action="store_true", help="Enable MarkItDown plugins")
    convert.add_argument("--max-mb", type=float, default=DEFAULT_MAX_MB, help=f"Maximum input size in MB (default: {DEFAULT_MAX_MB})")

    pack = subparsers.add_parser("review-pack", help="Create one markdown bundle for agent review")
    pack.add_argument("inputs", nargs="+", help="Local files to convert and bundle")
    pack.add_argument("-o", "--output", help="Output markdown file path")
    pack.add_argument("--json", action="store_true", help="Emit structured JSON instead of plain markdown")
    pack.add_argument("--plugins", action="store_true", help="Enable MarkItDown plugins")
    pack.add_argument("--max-mb", type=float, default=DEFAULT_MAX_MB, help=f"Maximum input size in MB (default: {DEFAULT_MAX_MB})")

    subparsers.add_parser("doctor", help="Show health info")
    subparsers.add_parser("list-types", help="List supported extensions")
    return parser


def _print_json(payload: object) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def _cmd_convert(args: argparse.Namespace) -> int:
    if args.output and len(args.inputs) != 1:
        raise ValueError("--output only supports a single input")
    if args.output and args.sidecar:
        raise ValueError("use either --output or --sidecar, not both")

    reports = []
    for raw_path in args.inputs:
        output_path = None
        if args.output:
            output_path = args.output
        elif args.sidecar:
            output_path = str(default_output_path(raw_path))
        reports.append(
            convert_file(
                raw_path,
                output_path=output_path,
                max_mb=args.max_mb,
                enable_plugins=args.plugins,
            )
        )

    if args.json:
        payload = reports[0].to_dict() if len(reports) == 1 else {"ok": True, "files": [r.to_dict() for r in reports]}
        _print_json(payload)
        return 0

    if args.output or args.sidecar:
        for report in reports:
            if report.output_path:
                print(report.output_path)
        return 0

    if len(reports) != 1:
        raise ValueError("multiple inputs without --json or --sidecar would collide on stdout")
    sys.stdout.write(reports[0].markdown)
    return 0


def _cmd_review_pack(args: argparse.Namespace) -> int:
    reports = [
        convert_file(path, max_mb=args.max_mb, enable_plugins=args.plugins)
        for path in args.inputs
    ]
    pack = build_review_pack(reports)
    if args.output:
        output_path = Path(args.output).expanduser().resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(pack.markdown, encoding="utf-8")

    if args.json:
        payload = pack.to_dict()
        if args.output:
            payload["output_path"] = str(output_path)
        _print_json(payload)
        return 0

    if args.output:
        print(str(output_path))
        return 0

    sys.stdout.write(pack.markdown)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "list-types":
            for suffix in supported_extensions():
                print(suffix)
            return 0
        if args.command == "doctor":
            _print_json(
                {
                    "ok": True,
                    "supported_extensions": list(supported_extensions()),
                    "plugins_default": False,
                    "local_only": True,
                    "subcommands": ["convert", "review-pack", "doctor", "list-types"],
                }
            )
            return 0
        if args.command == "convert":
            return _cmd_convert(args)
        if args.command == "review-pack":
            return _cmd_review_pack(args)
        parser.error(f"unknown command: {args.command}")
    except Exception as exc:  # pragma: no cover
        if getattr(args, "json", False):
            _print_json({"ok": False, "error": str(exc)})
        else:
            print(f"error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
