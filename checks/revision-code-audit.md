# Revised computational assurance

## Result

The revised finite checks passed under CPython 3.13.5 in normal mode and with
`PYTHONOPTIMIZE=1`. The two checked evidence files reproduce byte for byte.
The runtime uses only the Python standard library.

This is computational assurance for the stated finite scope. It is not a
formal proof of the all-parameter theorem, and it does not establish the
categorical interpretation or the physical factorisation classification.

## Public-code changes

- `count(N)` and `ranks(N)` now accept positive even integers only. Invalid
  integer values raise `ValueError`; invalid types, including `bool`, raise
  `TypeError`. Load-bearing internal checks use explicit exceptions and remain
  active under optimized Python.
- The former `electron_fixed` output has been removed. The replacement key is
  `resolved_objects_over_electron_invariant_parent_orbits`. It counts resolved
  contributions above parent (H)-orbits preserved by one-step rotation; it
  does **not** claim that every resolved constituent is individually fixed by
  the electron.
- The obsolete conditional exclusion field, which depended on the stronger
  interpretation, has also been removed. The universal theorem does not use
  either diagnostic.
- Both evidence files carry explicit finite scope and limitation notes.

## Independent finite checks

`independent_verifier.py` constructs its comparison values before importing
the production modules.

| Check | Exact finite scope |
|---|---|
| Direct (H=\langle T^2\rangle) enumeration | (N=2,4,6,8,10), respectively 3, 35, 462, 6,435 and 92,378 labels |
| Charge coefficient dynamic programme | all 5,050 residue cells for lengths 1 through 100 |
| Jordan totient from primitive pairs | every (d\le 50) |
| Rank comparison | every even (N\) from 2 through 100 |
| Quantitative gap | (R_0-R_q\ge N/2) for every checked even (N=4,\ldots,100) and every nonzero (q) |

The quantitative lower bound attains equality at (N=4,q=2), where the gap
is 2. No equality classification is claimed.

At the excluded boundary (N=2), the ranks are ((2,1)), so strict rank
dominance holds, while the parent witness ((1,1)) has period one and does not
move to a distinct even-subgroup orbit. This confirms that a rank-only
inference would be insufficient and that (N=2) is not part of the theorem.

Five semantic negative controls were required to fail:

1. corrupt one dynamic-programme charge cell;
2. replace (H=\langle T^2\rangle) by the full rotation group;
3. reintroduce the unsupported legacy fixed-object field;
4. violate the quantitative gap at (N=4,q=2);
5. infer the pair obstruction from the (N=2) rank inequality alone.

All five corruptions were detected in normal and optimized runs.

## Replay commands

Run from the repository root with a selected Python executable in place of
`python`:

```sh
env LANG=C LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 PYTHONOPTIMIZE=0 \
  python -B checks/test_primitive_su.py

env LANG=C LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 PYTHONOPTIMIZE=1 \
  python -B checks/test_primitive_su.py

env LANG=C LC_ALL=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 PYTHONOPTIMIZE=0 \
  python -B checks/independent_verifier.py --root . --output /fresh/path/receipt.json

python -B code/primitive_su_pilot.py > /fresh/path/pilot.json
python -B code/primitive_su_formula.py > /fresh/path/formula.json
cmp evidence/pilot.json /fresh/path/pilot.json
cmp evidence/formula.json /fresh/path/formula.json
```

The verifier refuses to overwrite an existing receipt. Use a fresh output path.
The GitHub workflow repeats normal and optimized tests, byte reproduction and
the independent verifier. Remote CI remains pending until the repository is
published.

## Evidence boundary

The original `source/` and supplied `review/` trees remained byte-identical
during this work. Revised public evidence is confined to the repository copy.
Finite agreement does not prove the all-(N) statement, determine the electron
permutation inside resolved short parent orbits, validate a microscopic model,
or establish novelty. Those obligations require the separately retained proof
and literature audits.
