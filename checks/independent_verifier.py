#!/usr/bin/env python3
"""Independent finite checks for the primitive SU computational evidence.

The direct rank calculation constructs H=<T^2> orbits.  The charge calculation
uses a coefficient dynamic programme.  Neither algorithm uses the production
pilot's full-rotation multiplicities or the production formula's Ramanujan and
Mobius implementation while constructing its independent results.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from itertools import combinations
import importlib.util
import json
from math import comb, gcd
from pathlib import Path
import platform
import sys
from typing import Callable


DIRECT_N_VALUES = (2, 4, 6, 8, 10)
DP_MAX_LENGTH = 100
JORDAN_MAX = 50
INVARIANT_FIELD = "resolved_objects_over_electron_invariant_parent_orbits"
LEGACY_FIELD = "electron_fixed"


class VerificationError(RuntimeError):
    """Raised when an exact computational obligation fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def weak_compositions(total: int, slots: int):
    """Generate weak compositions using separator positions."""
    for bars in combinations(range(total + slots - 1), slots - 1):
        boundaries = (-1,) + bars + (total + slots - 1,)
        yield tuple(
            boundaries[index + 1] - boundaries[index] - 1
            for index in range(slots)
        )


def rotate(label: tuple[int, ...], steps: int) -> tuple[int, ...]:
    steps %= len(label)
    return label[steps:] + label[:steps]


def label_charge(label: tuple[int, ...]) -> int:
    return sum(index * value for index, value in enumerate(label)) % len(label)


def direct_h_enumeration(n: int) -> dict[str, object]:
    seen: set[tuple[int, ...]] = set()
    ranks = [0] * n
    invariant_parent_contributions = [0] * n
    charge_cells = [0] * n
    for label in weak_compositions(n, n):
        q = label_charge(label)
        charge_cells[q] += 1
        if label in seen:
            continue
        orbit = {rotate(label, step) for step in range(0, n, 2)}
        seen.update(orbit)
        require({label_charge(item) for item in orbit} == {q}, "H orbit changed charge")
        stabiliser = sum(
            rotate(label, step) == label for step in range(0, n, 2)
        )
        require(len(orbit) * stabiliser == n // 2, "H orbit-stabiliser failure")
        ranks[q] += stabiliser
        if rotate(label, 1) in orbit:
            invariant_parent_contributions[q] += stabiliser

    expected_labels = comb(2 * n - 1, n - 1)
    require(len(seen) == expected_labels, "direct enumeration lost labels")
    return {
        "N": n,
        "labels": expected_labels,
        "ranks": ranks,
        "charge_cells": charge_cells,
        INVARIANT_FIELD: invariant_parent_contributions,
    }


def full_rotation_orbit_count_negative_control(n: int) -> list[int]:
    """Intentionally wrong replacement of H by the full rotation group."""
    seen: set[tuple[int, ...]] = set()
    counts = [0] * n
    for label in weak_compositions(n, n):
        if label in seen:
            continue
        orbit = {rotate(label, step) for step in range(n)}
        seen.update(orbit)
        counts[label_charge(label)] += 1
    return counts


def charge_dp(length: int) -> list[int]:
    """Extract degree ``length`` coefficients modulo z^length-1."""
    table = [[0] * length for _ in range(length + 1)]
    table[0][0] = 1
    for weight in range(length):
        for degree in range(1, length + 1):
            previous = table[degree - 1]
            current = table[degree]
            for residue, value in enumerate(previous):
                current[(residue + weight) % length] += value
    counts = table[length]
    validate_charge_table(length, counts)
    return counts


def validate_charge_table(length: int, counts: list[int]) -> None:
    require(len(counts) == length, "charge table has the wrong length")
    require(
        all(isinstance(value, int) and not isinstance(value, bool) and value >= 0
            for value in counts),
        "charge table contains a nonnegative-integer violation",
    )
    require(sum(counts) == comb(2 * length - 1, length), "stars-and-bars total failed")
    require(
        counts == [counts[(-residue) % length] for residue in range(length)],
        "charge-conjugation symmetry failed",
    )


def jordan_by_primitive_pairs(d: int) -> int:
    return sum(
        gcd(gcd(x, y), d) == 1
        for x in range(d)
        for y in range(d)
    )


def divisors(n: int) -> list[int]:
    return [value for value in range(1, n + 1) if n % value == 0]


def assemble_ranks(n: int, charge_tables: dict[int, list[int]], jordan: dict[int, int]) -> list[int]:
    result = []
    for q in range(n):
        numerator = 2 * sum(
            jordan[d] * charge_tables[n // d][q // d]
            for d in divisors(n // 2)
            if q % d == 0
        )
        require(numerator % n == 0, "independent rank numerator is not integral")
        result.append(numerator // n)
    return result


def validate_quantitative_gap(n: int, vector: list[int]) -> None:
    require(n >= 4 and n % 2 == 0, "quantitative gap check requires even N>=4")
    require(len(vector) == n, "rank vector length differs from N")
    require(
        all(vector[0] - value >= n // 2 for value in vector[1:]),
        "quantitative neutral-rank lower bound failed",
    )


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_pilot_payload(payload: dict[str, object]) -> None:
    require(payload.get("schema") == "primitive-su-bounded-orbit-diagnostic-v2",
            "pilot evidence schema mismatch")
    require(isinstance(payload.get("limits"), list) and payload["limits"],
            "pilot evidence lacks scope limits")
    results = payload.get("results")
    require(isinstance(results, list) and len(results) == len(DIRECT_N_VALUES),
            "pilot evidence has the wrong result domain")
    for row in results:
        require(isinstance(row, dict), "pilot evidence row is not an object")
        require(LEGACY_FIELD not in row, "legacy fixed-object field is forbidden")
        require(INVARIANT_FIELD in row, "accurately scoped invariant-parent field is missing")
    n2 = results[0]
    require(n2.get("N") == 2 and n2.get("ranks") == [2, 1], "N=2 ranks changed")
    witnesses = n2.get("parent_pair_witnesses")
    require(isinstance(witnesses, list) and len(witnesses) == 1, "N=2 witness missing")
    require(not witnesses[0].get("one_step_rotation_has_distinct_even_orbit"),
            "N=2 must not pass the distinct-parent-pair witness")


def expect_detection(action: Callable[[], None], name: str) -> dict[str, object]:
    try:
        action()
    except VerificationError as error:
        return {"id": name, "detected": True, "diagnostic": str(error)}
    raise VerificationError(f"negative control escaped detection: {name}")


def verify(root: Path) -> dict[str, object]:
    root = root.resolve()
    code = root / "code"
    evidence = root / "evidence"
    required = [
        code / "primitive_su_pilot.py",
        code / "primitive_su_formula.py",
        evidence / "pilot.json",
        evidence / "formula.json",
    ]
    require(all(path.is_file() and not path.is_symlink() for path in required),
            "required production input is missing or unsafe")

    direct = {n: direct_h_enumeration(n) for n in DIRECT_N_VALUES}
    charge_tables = {length: charge_dp(length) for length in range(1, DP_MAX_LENGTH + 1)}
    jordan = {d: jordan_by_primitive_pairs(d) for d in range(1, JORDAN_MAX + 1)}
    for h in range(1, JORDAN_MAX + 1):
        require(sum(jordan[d] for d in divisors(h)) == h * h,
                "Jordan divisor identity failed")
    assembled = {
        n: assemble_ranks(n, charge_tables, jordan)
        for n in range(2, 102, 2)
    }
    for n, vector in assembled.items():
        require(all(vector[0] > value for value in vector[1:]),
                "strict finite neutral-rank dominance failed")
        if n >= 4:
            validate_quantitative_gap(n, vector)
    require(assembled[4][0] - assembled[4][2] == 2,
            "N=4, q=2 quantitative-gap equality changed")

    sys.path.insert(0, str(code))
    try:
        pilot = load_module(code / "primitive_su_pilot.py", "public_primitive_su_pilot")
        formula = load_module(code / "primitive_su_formula.py", "public_primitive_su_formula")
    finally:
        sys.path.pop(0)

    for n, independent in direct.items():
        produced = pilot.count(n)
        require(produced["ranks"] == independent["ranks"], f"direct rank mismatch at N={n}")
        require(
            produced[INVARIANT_FIELD] == independent[INVARIANT_FIELD],
            f"invariant-parent contribution mismatch at N={n}",
        )
        require(independent["charge_cells"] == charge_tables[n],
                f"direct/DP charge mismatch at N={n}")
    for length, counts in charge_tables.items():
        require(
            all(formula.charge_count(length, q) == counts[q] for q in range(length)),
            f"formula/DP charge mismatch at length={length}",
        )
    for d, value in jordan.items():
        require(formula.jordan2(d) == value, f"Jordan mismatch at d={d}")
    for n, vector in assembled.items():
        require(formula.ranks(n) == vector, f"rank assembly mismatch at N={n}")

    pilot_payload = json.loads((evidence / "pilot.json").read_text(encoding="utf-8"))
    formula_payload = json.loads((evidence / "formula.json").read_text(encoding="utf-8"))
    validate_pilot_payload(pilot_payload)
    require(pilot_payload == pilot.evidence_payload(), "pilot evidence is not freshly reproducible")
    require(formula_payload == formula.evidence_payload(), "formula evidence is not freshly reproducible")

    corrupted_charge = charge_tables[4].copy()
    corrupted_charge[0] += 1
    corrupted_gap = direct[4]["ranks"].copy()
    corrupted_gap[2] = corrupted_gap[0] - 1
    corrupted_payload = deepcopy(pilot_payload)
    corrupted_payload["results"][0][LEGACY_FIELD] = [0, 1]
    negative_controls = [
        expect_detection(
            lambda: validate_charge_table(4, corrupted_charge),
            "corrupted-charge-cell",
        ),
        expect_detection(
            lambda: require(
                full_rotation_orbit_count_negative_control(4) == direct[4]["ranks"],
                "replacing H=<T^2> by full rotations changes the rank result",
            ),
            "wrong-rotation-group",
        ),
        expect_detection(
            lambda: validate_pilot_payload(corrupted_payload),
            "legacy-fixed-object-field",
        ),
        expect_detection(
            lambda: validate_quantitative_gap(4, corrupted_gap),
            "quantitative-gap-corruption",
        ),
        expect_detection(
            lambda: require(
                direct[2]["ranks"][0] > direct[2]["ranks"][1]
                and pilot_payload["results"][0]["parent_pair_witnesses"][0][
                    "one_step_rotation_has_distinct_even_orbit"
                ],
                "rank dominance alone cannot pass the N=2 pair boundary",
            ),
            "rank-only-N2-inference",
        ),
    ]

    return {
        "schema": "primitive-su-independent-computational-verification-v1",
        "status": "passed",
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "optimization": sys.flags.optimize,
        },
        "scope": {
            "direct_H_enumeration_N_values": list(DIRECT_N_VALUES),
            "direct_labels_by_N": {str(n): direct[n]["labels"] for n in DIRECT_N_VALUES},
            "DP_lengths": [1, DP_MAX_LENGTH],
            "DP_charge_cells": sum(range(1, DP_MAX_LENGTH + 1)),
            "Jordan_coprime_pair_values_through": JORDAN_MAX,
            "rank_comparisons_even_N": [2, 100],
            "quantitative_gap_comparisons_even_N": [4, 100],
            "quantitative_gap_lower_bound": "R_0 - R_q >= N/2 for every nonzero q",
        },
        "direct_ranks": {str(n): direct[n]["ranks"] for n in DIRECT_N_VALUES},
        "N2_sanity": {
            "ranks": direct[2]["ranks"],
            "strict_rank_dominance": direct[2]["ranks"][0] > direct[2]["ranks"][1],
            "distinct_parent_pair_witness": False,
        },
        "quantitative_gap_equality_witness": {"N": 4, "q": 2, "gap": 2},
        "negative_controls": negative_controls,
        "evidence_reproduced": ["evidence/pilot.json", "evidence/formula.json"],
        "limits": [
            "Finite computations do not prove the all-parameter theorem.",
            "The verifier assumes the separately audited cyclic-resolution interpretation.",
            "It does not determine the electron action inside resolved short parent orbits.",
            "It does not verify the physical factorisation classification or historical novelty.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="write a new receipt; existing paths are refused")
    args = parser.parse_args()
    result = verify(args.root)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        output = args.output.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    try:
        main()
    except VerificationError as error:
        raise SystemExit(f"verification error: {error}") from error
