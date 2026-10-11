#!/usr/bin/env python3
"""Verify exact release-file closure against MANIFEST.json and SHA256SUMS."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any


EXPECTED_PACKAGE = "primitive-su-primitivity"
EXPECTED_VERSION = "1.1.0-candidate"
CONTROL_FILES = {"MANIFEST.json", "SHA256SUMS"}
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")


class CheckError(ValueError):
    """A release-closure invariant failed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def exact_keys(value: Any, expected: set[str], where: str) -> None:
    require(type(value) is dict, f"{where}: expected object")
    actual = set(value)
    require(actual == expected,
            f"{where}: keys differ; missing={sorted(expected - actual)}, "
            f"extra={sorted(actual - expected)}")


def safe_relative_path(value: Any, where: str) -> str:
    require(type(value) is str and value and "\\" not in value,
            f"{where}: invalid path text")
    path = PurePosixPath(value)
    require(not path.is_absolute() and value == path.as_posix(),
            f"{where}: path is not canonical POSIX-relative")
    require(all(part not in ("", ".", "..") for part in path.parts),
            f"{where}: unsafe path")
    require(value not in CONTROL_FILES, f"{where}: control file must not list itself")
    return value


def parse_manifest(path: Path) -> list[dict[str, Any]]:
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=strict_object)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise CheckError(f"cannot read strict JSON manifest: {error}") from error
    exact_keys(manifest, {"schemaVersion", "package", "version", "scope", "files"},
               "MANIFEST.json")
    require(manifest["schemaVersion"] == "1.0", "unsupported manifest schemaVersion")
    require(manifest["package"] == EXPECTED_PACKAGE, "manifest package mismatch")
    require(manifest["version"] == EXPECTED_VERSION, "manifest version mismatch")
    require(manifest["scope"] == "Every shipped payload except MANIFEST.json and SHA256SUMS.",
            "manifest scope mismatch")
    require(type(manifest["files"]) is list and manifest["files"],
            "manifest files must be a nonempty array")
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, row in enumerate(manifest["files"]):
        where = f"MANIFEST.json.files[{index}]"
        exact_keys(row, {"path", "size_bytes", "sha256"}, where)
        relative = safe_relative_path(row["path"], f"{where}.path")
        require(relative not in seen, f"{where}: duplicate path")
        seen.add(relative)
        require(type(row["size_bytes"]) is int and row["size_bytes"] >= 0,
                f"{where}: invalid size")
        require(type(row["sha256"]) is str and SHA256_RE.fullmatch(row["sha256"]) is not None,
                f"{where}: invalid SHA-256")
        rows.append(row)
    require([row["path"] for row in rows] == sorted(seen),
            "manifest rows are not path-sorted")
    return rows


def parse_checksum_list(path: Path) -> list[tuple[str, str]]:
    try:
        text = path.read_text(encoding="ascii")
    except (OSError, UnicodeDecodeError) as error:
        raise CheckError(f"cannot read SHA256SUMS: {error}") from error
    require(text.endswith("\n"), "SHA256SUMS lacks terminal newline")
    result: list[tuple[str, str]] = []
    seen: set[str] = set()
    for number, line in enumerate(text.splitlines(), start=1):
        require(len(line) >= 67 and line[64:66] == "  ",
                f"SHA256SUMS:{number}: invalid format")
        digest, relative = line[:64], line[66:]
        require(SHA256_RE.fullmatch(digest) is not None,
                f"SHA256SUMS:{number}: invalid SHA-256")
        relative = safe_relative_path(relative, f"SHA256SUMS:{number}")
        require(relative not in seen, f"SHA256SUMS:{number}: duplicate path")
        seen.add(relative)
        result.append((digest, relative))
    require(bool(result), "SHA256SUMS is empty")
    return result


def actual_files(root: Path) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        require(not path.is_symlink(), f"package contains symlink: {relative}")
        if path.is_dir():
            continue
        require(path.is_file(), f"package contains unsupported object: {relative}")
        if relative not in CONTROL_FILES:
            result[relative] = path
    return result


def outside_root(path: Path, root: Path, label: str) -> None:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return
    raise CheckError(f"{label} must be outside the frozen package")


def write_new(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)


def verify(root: Path, output: Path | None) -> dict[str, Any]:
    root = root.resolve()
    require(root.is_dir(), f"package root is not a directory: {root}")
    for name in sorted(CONTROL_FILES):
        path = root / name
        require(path.is_file() and not path.is_symlink(), f"missing regular {name}")
    if output is not None:
        require(not output.exists(), f"refusing to overwrite output: {output}")
        outside_root(output, root, "output")

    rows = parse_manifest(root / "MANIFEST.json")
    expected = {row["path"]: row for row in rows}
    sums = parse_checksum_list(root / "SHA256SUMS")
    require(sums == [(row["sha256"], row["path"]) for row in rows],
            "SHA256SUMS does not exactly reproduce manifest rows")
    actual = actual_files(root)
    require(set(actual) == set(expected),
            f"package closure differs; missing={sorted(set(expected) - set(actual))}, "
            f"unexpected={sorted(set(actual) - set(expected))}")
    total = 0
    for relative, row in expected.items():
        path = actual[relative]
        require(path.stat().st_size == row["size_bytes"], f"{relative}: size mismatch")
        require(sha256_file(path) == row["sha256"], f"{relative}: SHA-256 mismatch")
        total += row["size_bytes"]
    receipt = {
        "schema": "primitive-su-package-manifest-check-v1",
        "verified_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "package": EXPECTED_PACKAGE,
        "version": EXPECTED_VERSION,
        "optimization": sys.flags.optimize,
        "files": len(rows),
        "payload_bytes": total,
        "manifest_sha256": sha256_file(root / "MANIFEST.json"),
        "sha256sums_sha256": sha256_file(root / "SHA256SUMS"),
        "symlinks": 0,
        "unexpected_files": 0,
        "result": "complete_file_closure_matches_manifest_and_checksum_list",
    }
    encoded = (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode()
    if output is not None:
        write_new(output, encoded)
    print(encoded.decode(), end="")
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).absolute().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    verify(args.root, args.output.absolute() if args.output is not None else None)


if __name__ == "__main__":
    try:
        main()
    except CheckError as error:
        raise SystemExit(f"check error: {error}") from error
