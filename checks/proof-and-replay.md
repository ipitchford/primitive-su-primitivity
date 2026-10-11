# Proof and replay boundary

The universal theorem is an informal analytic result. Its proof is in
`paper.md`, `paper.tex` and the six-page `paper.pdf`; finite computation does
not replace that argument. The checked computational layer tests the formulas,
the bounded orbit implementation and several semantic failure modes.

## Public replay

Python 3 and its standard library suffice. From the repository root, replacing
`python` with the selected interpreter:

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

The verifier refuses to replace an existing receipt. Use a fresh output path.

## Checked finite scope

- seven explicit tests pass in normal and optimized Python;
- direct (H=\langle T^2\rangle) enumeration covers
  (N=2,4,6,8,10), totalling the separately reported label counts;
- an independent coefficient dynamic programme checks all 5,050 charge cells
  for lengths 1 through 100;
- primitive-pair counts check the second Jordan totient through 50;
- rank vectors are compared for every even (N=2,\ldots,100);
- the quantitative bound (R_0-R_q\ge N/2) is checked for every nonzero
  sector and every even (N=4,\ldots,100), including equality at
  (N=4,q=2); and
- five semantic negative controls demonstrate sensitivity to a corrupt charge
  cell, the wrong rotation group, the unsupported legacy fixed-object field, a
  quantitative-gap violation, and a rank-only inference at (N=2).

The excluded (N=2) boundary has ranks ((2,1)) but fails the distinct-parent-
pair witness. It is a sanity check, not part of the theorem domain.

The field
`resolved_objects_over_electron_invariant_parent_orbits` counts resolved
contributions above parent (H)-orbits preserved by one-step rotation. It does
not assert that every resolved constituent is individually electron-fixed, and
the theorem does not use this diagnostic.

See `checks/revision-code-audit.md` for the complete check inventory and
assurance limits. The final release receipt records the exact interpreter,
commands, logs, hashes and clean-extraction result.

## Limits

These checks do not prove the all-(N) theorem, establish the categorical
module interpretation, determine electron action within a resolved short
parent orbit, verify a microscopic realisation, or establish historical
novelty. Those are separate proof, physical and literature obligations.
