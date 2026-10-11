"""Bounded orbit-count diagnostic for the primitive SU series.

This program checks finite affine-label orbit counts. It does not prove the
all-parameter theorem or determine the electron action on individual resolved
constituents above a short parent orbit.
"""

from __future__ import annotations

from collections import Counter
import json


def require_even_positive_n(n: int) -> None:
    """Reject inputs outside the supported even-positive rank domain."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("N must be an integer (bool is not accepted)")
    if n <= 0 or n % 2:
        raise ValueError("N must be a positive even integer")


def compositions(total: int, slots: int, prefix: tuple[int, ...] = ()):
    if slots == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, slots - 1, prefix + (value,))


def rotate(label: tuple[int, ...], steps: int) -> tuple[int, ...]:
    steps %= len(label)
    return label[steps:] + label[:steps]


def parent_pair_witness(n: int, q: int) -> dict[str, object]:
    label = tuple(n - 1 if i == 0 else 1 if i == q else 0 for i in range(n))
    full_orbit = {rotate(label, steps) for steps in range(n)}
    even_orbit = {rotate(label, steps) for steps in range(0, n, 2)}
    result = {
        "q": q,
        "label": list(label),
        "full_period": len(full_orbit),
        "even_subgroup_stabiliser_order": (n // 2) // len(even_orbit),
        "one_step_rotation_has_distinct_even_orbit": rotate(label, 1) not in even_orbit,
    }
    if n >= 4 and (
        result["full_period"] != n
        or not result["one_step_rotation_has_distinct_even_orbit"]
    ):
        raise RuntimeError("the full-period parent-pair witness check failed")
    return result


def count(n: int) -> dict[str, object]:
    """Return the bounded orbit diagnostic for one positive even ``N``."""
    require_even_positive_n(n)
    orbits = [Counter() for _ in range(n)]
    labels = 0
    for label in compositions(n, n):
        labels += 1
        rotations = {rotate(label, steps) for steps in range(n)}
        if label != min(rotations):
            continue
        q = sum(i * value for i, value in enumerate(label)) % n
        if any(
            sum(i * value for i, value in enumerate(rotated)) % n != q
            for rotated in rotations
        ):
            raise RuntimeError("rotation changed the charge sector")
        orbits[q][len(rotations)] += 1

    ranks: list[int] = []
    invariant_parent_contributions: list[int] = []
    for sector in orbits:
        invariant = sum(
            multiplicity * (n // (2 * length))
            for length, multiplicity in sector.items()
            if length % 2
        )
        rank = invariant + sum(
            multiplicity * (2 * n // length)
            for length, multiplicity in sector.items()
            if length % 2 == 0
        )
        ranks.append(rank)
        invariant_parent_contributions.append(invariant)

    accounted_labels = sum(
        length * multiplicity
        for sector in orbits
        for length, multiplicity in sector.items()
    )
    if accounted_labels != labels:
        raise RuntimeError("orbit decomposition did not account for every label")

    return {
        "N": n,
        "labels": labels,
        "orbit_counts": [
            {str(length): multiplicity for length, multiplicity in sector.items()}
            for sector in orbits
        ],
        "ranks": ranks,
        "resolved_objects_over_electron_invariant_parent_orbits":
            invariant_parent_contributions,
        "rank_strictly_below_neutral_sectors": [
            q for q in range(1, n) if ranks[q] < ranks[0]
        ],
        "parent_pair_witnesses": [parent_pair_witness(n, q) for q in range(1, n)],
    }


def evidence_payload() -> dict[str, object]:
    values = [2, 4, 6, 8, 10]
    return {
        "schema": "primitive-su-bounded-orbit-diagnostic-v2",
        "status": "bounded computational diagnostic only",
        "scope": {
            "N_values": values,
            "input_contract": "count(N) accepts positive even integers only",
            "purpose": "finite orbit/rank checks and the excluded N=2 boundary sanity check",
        },
        "field_definitions": {
            "resolved_objects_over_electron_invariant_parent_orbits": (
                "resolved contributions above parent H-orbits preserved by one-step "
                "rotation; this does not count individually electron-fixed resolved objects"
            ),
            "parent_pair_witnesses": (
                "parent-label orbit facts; the N>=4 entries have full period and a "
                "distinct even-subgroup orbit after one-step rotation"
            ),
        },
        "limits": [
            "Finite enumeration is not the universal proof.",
            "The computation assumes the separately audited cyclic-resolution interpretation.",
            "It does not determine the electron permutation within a resolved short orbit.",
            "The N=2 boundary passes strict rank dominance but fails the distinct-pair witness.",
        ],
        "results": [count(n) for n in values],
    }


def main() -> None:
    payload = evidence_payload()
    if payload["results"][1]["ranks"] != [8, 4, 6, 4]:
        raise RuntimeError("N=4 rank regression")
    if payload["results"][2]["ranks"] != [32, 25, 26, 28, 26, 25]:
        raise RuntimeError("N=6 rank regression")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
