"""Divisor-formula checks for the primitive SU series."""

from __future__ import annotations

import json
from math import comb, gcd

from primitive_su_pilot import count, require_even_positive_n


def require_positive_integer(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer (bool is not accepted)")
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def divisors(n: int) -> list[int]:
    require_positive_integer(n, "n")
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    require_positive_integer(n, "n")
    sign = 1
    prime = 2
    while prime * prime <= n:
        if n % prime == 0:
            n //= prime
            sign = -sign
            if n % prime == 0:
                return 0
            while n % prime == 0:
                n //= prime
        prime += 1
    return -sign if n > 1 else sign


def ramanujan(e: int, q: int) -> int:
    require_positive_integer(e, "e")
    if isinstance(q, bool) or not isinstance(q, int):
        raise TypeError("q must be an integer (bool is not accepted)")
    return sum(d * mobius(e // d) for d in divisors(gcd(e, q)))


def jordan2(d: int) -> int:
    require_positive_integer(d, "d")
    return sum(mobius(d // a) * a * a for a in divisors(d))


def charge_count(length: int, q: int) -> int:
    require_positive_integer(length, "length")
    if isinstance(q, bool) or not isinstance(q, int):
        raise TypeError("q must be an integer (bool is not accepted)")
    numerator = sum(
        ramanujan(e, q) * comb(2 * length // e - 1, length // e)
        for e in divisors(length)
    )
    if numerator % length:
        raise ArithmeticError("charge-count numerator is not divisible by the length")
    return numerator // length


def ranks(n: int) -> list[int]:
    """Return the sector ranks for one positive even ``N``."""
    require_even_positive_n(n)
    result: list[int] = []
    for q in range(n):
        numerator = 2 * sum(
            jordan2(d) * charge_count(n // d, q // d)
            for d in divisors(n // 2)
            if q % d == 0
        )
        if numerator % n:
            raise ArithmeticError("rank numerator is not divisible by N")
        result.append(numerator // n)
    return result


def evidence_payload() -> dict[str, object]:
    direct_checks = []
    for n in (2, 4, 6, 8, 10):
        calculated = ranks(n)
        enumerated = count(n)["ranks"]
        if calculated != enumerated:
            raise RuntimeError(f"divisor/direct rank mismatch at N={n}")
        direct_checks.append({"N": n, "ranks": calculated, "direct_match": True})

    for n in range(2, 102, 2):
        vector = ranks(n)
        if any(vector[0] <= value for value in vector[1:]):
            raise RuntimeError(f"strict neutral-rank check failed at N={n}")
        if n >= 4 and any(vector[0] - value < n // 2 for value in vector[1:]):
            raise RuntimeError(f"quantitative neutral-rank gap check failed at N={n}")

    n4 = ranks(4)
    if n4[0] - n4[2] != 2:
        raise RuntimeError("the N=4, q=2 lower-bound equality check failed")

    return {
        "schema": "primitive-su-divisor-formula-check-v2",
        "status": "finite formula verification only",
        "scope": {
            "direct_enumeration_N_values": [2, 4, 6, 8, 10],
            "strict_rank_checks_even_N_from": 2,
            "strict_rank_checks_even_N_through": 100,
            "quantitative_gap_checks_even_N_from": 4,
            "quantitative_gap_checks_even_N_through": 100,
            "quantitative_gap_lower_bound": "R_0 - R_q >= N/2 for every nonzero q",
            "input_contract": "ranks(N) accepts positive even integers only",
        },
        "direct_checks": direct_checks,
        "quantitative_gap_equality_witness": {"N": 4, "q": 2, "gap": 2},
        "limits": [
            "Finite verification is not the universal proof.",
            "The checks do not establish the categorical interpretation of the ranks.",
            "The N=2 rank inequality does not supply the distinct electron-pair witness.",
        ],
    }


def main() -> None:
    print(json.dumps(evidence_payload(), indent=2))


if __name__ == "__main__":
    main()
