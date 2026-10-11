#!/usr/bin/env python3
"""Replay both production evidence generators and compare every output byte."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class ReplayError(ValueError):
    """A clean evidence-replay invariant failed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ReplayError(message)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def outside_root(path: Path, root: Path, label: str) -> None:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return
    raise ReplayError(f"{label} must be outside the frozen package")


def write_new(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)


def interpreter_facts(python: Path, environment: dict[str, str]) -> dict[str, Any]:
    require(python.is_absolute(), "nominated Python path must be absolute")
    require(python.is_file() and os.access(python, os.X_OK),
            f"nominated Python is not executable: {python}")
    probe = (
        "import json,platform,sys,sysconfig;"
        "print(json.dumps({'executable':sys.executable,'implementation':platform.python_implementation(),"
        "'python':platform.python_version(),'optimization':sys.flags.optimize,"
        "'platform':platform.platform(),'stdlib':sysconfig.get_path('stdlib')},sort_keys=True))"
    )
    completed = subprocess.run([str(python), "-B", "-c", probe], env=environment,
                               capture_output=True, check=False)
    require(completed.returncode == 0 and completed.stderr == b"",
            "nominated Python environment probe failed")
    try:
        return json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        raise ReplayError("nominated Python returned invalid environment JSON") from error


def replay(root: Path, python: Path, mode: str, work_dir: Path) -> dict[str, Any]:
    root = root.resolve()
    work_dir = work_dir.absolute()
    require(root.is_dir(), f"package root is not a directory: {root}")
    outside_root(work_dir, root, "work directory")
    require(not work_dir.exists(), f"refusing to reuse work directory: {work_dir}")
    require(mode in {"normal", "optimized"}, "mode must be normal or optimized")
    expected_optimization = 0 if mode == "normal" else 1
    require(sys.flags.optimize == expected_optimization,
            "wrapper optimization does not match the declared replay mode")

    environment = {
        "LANG": "C",
        "LC_ALL": "C",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0",
        "PYTHONIOENCODING": "utf-8",
        "PYTHONNOUSERSITE": "1",
        "PYTHONOPTIMIZE": str(expected_optimization),
    }
    facts = interpreter_facts(python, environment)
    require(facts.get("optimization") == expected_optimization,
            "child interpreter optimization does not match replay mode")
    work_dir.mkdir(parents=True)

    products: list[dict[str, Any]] = []
    for stem in ("pilot", "formula"):
        script = root / "code" / f"primitive_su_{stem}.py"
        expected = root / "evidence" / f"{stem}.json"
        require(script.is_file() and not script.is_symlink(), f"missing safe script: {script}")
        require(expected.is_file() and not expected.is_symlink(), f"missing safe evidence: {expected}")
        argv = [str(python), "-B", str(script)]
        completed = subprocess.run(argv, cwd=root, env=environment,
                                   capture_output=True, check=False)
        stdout = work_dir / f"{stem}.json"
        stderr = work_dir / f"{stem}.stderr.txt"
        write_new(stdout, completed.stdout)
        write_new(stderr, completed.stderr)
        require(completed.returncode == 0, f"{stem} replay exited {completed.returncode}")
        require(completed.stderr == b"", f"{stem} replay wrote stderr")
        expected_bytes = expected.read_bytes()
        require(completed.stdout == expected_bytes,
                f"{stem} replay is not byte-identical to committed evidence")
        try:
            json.loads(completed.stdout)
        except json.JSONDecodeError as error:
            raise ReplayError(f"{stem} replay returned malformed JSON") from error
        products.append({
            "id": stem,
            "command": argv,
            "expected": str(expected.relative_to(root)),
            "bytes": len(completed.stdout),
            "sha256": sha256_bytes(completed.stdout),
            "byte_identical": True,
            "stderr_bytes": 0,
            "stderr_sha256": sha256_bytes(completed.stderr),
        })

    receipt = {
        "schema": "primitive-su-clean-evidence-replay-v1",
        "verified_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "package": "primitive-su-primitivity",
        "version": "1.1.0-candidate",
        "mode": mode,
        "environment": facts,
        "products": products,
        "result": "production_outputs_are_byte_identical_to_both_frozen_evidence_files",
        "limits": [
            "Finite replay is not the universal analytic proof.",
            "Replay does not verify the categorical interpretation or historical novelty.",
        ],
    }
    encoded = (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode()
    write_new(work_dir / "receipt.json", encoded)
    print(encoded.decode(), end="")
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--python", type=Path, required=True)
    parser.add_argument("--mode", choices=("normal", "optimized"), required=True)
    parser.add_argument("--work-dir", type=Path, required=True)
    args = parser.parse_args()
    # Keep the supplied absolute interpreter path.  Resolving a symlink here
    # would silently change the runtime identity recorded by the gate plan.
    python = args.python.absolute()
    replay(args.root, python, args.mode, args.work_dir)


if __name__ == "__main__":
    try:
        main()
    except ReplayError as error:
        raise SystemExit(f"replay error: {error}") from error
