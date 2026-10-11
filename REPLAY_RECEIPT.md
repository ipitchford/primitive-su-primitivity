# Computational replay receipt

Package version: `1.1.0-candidate`  
Recorded local run: 11 October 2026  
Result: passed in the recorded local environment  
Final clean-extraction package gate: pending

## Environment

The recorded run used CPython 3.13.5 on
`macOS-27.0.1-arm64-arm-64bit-Mach-O`, with the Python standard library only.
See [ENVIRONMENT.txt](ENVIRONMENT.txt). Commands were run from the repository
root with `LANG=C`, `LC_ALL=C`, `PYTHONDONTWRITEBYTECODE=1`,
`PYTHONHASHSEED=0`, and the stated `PYTHONOPTIMIZE` value.

## Commands and results

1. `PYTHONOPTIMIZE=0 python -B checks/test_primitive_su.py` — exit 0; seven
   tests passed.
2. `PYTHONOPTIMIZE=1 python -B checks/test_primitive_su.py` — exit 0; the same
   seven tests passed with assertions disabled.
3. `PYTHONOPTIMIZE=0 python -B checks/independent_verifier.py --root .
   --output <fresh-path>` — exit 0.
4. The same verifier command with `PYTHONOPTIMIZE=1` — exit 0.
5. `python -B code/primitive_su_pilot.py` — exit 0; output byte-identical to
   `evidence/pilot.json`.
6. `python -B code/primitive_su_formula.py` — exit 0; output byte-identical to
   `evidence/formula.json`.

The verifier refuses to overwrite an existing receipt. Exact copyable commands
and finite-scope details are in
[checks/proof-and-replay.md](checks/proof-and-replay.md).

## Verified finite scope

- Direct $H=\langle T^2\rangle$ enumeration covers $N=2,4,6,8,10$, with
  respectively 3, 35, 462, 6,435 and 92,378 labels.
- An independent coefficient dynamic programme checks all 5,050 charge cells
  for lengths 1 through 100.
- Independent primitive-pair counts check $J_2(d)$ through $d=50$.
- Rank vectors agree for every even $N$ from 2 through 100.
- The quantitative bound $R_0-R_q\ge N/2$ holds for every checked nonzero
  sector and every even $N$ from 4 through 100; $N=4,q=2$ is an equality
  witness.
- The excluded $N=2$ case has ranks $(2,1)$ but fails the distinct-parent
  pair witness.
- Five semantic corruptions are rejected in normal and optimized modes: a
  wrong charge cell, the wrong rotation group, the legacy fixed-object field,
  a quantitative-gap violation, and a rank-only inference at $N=2$.

## Bound file identities

| File | SHA-256 |
|---|---|
| `code/primitive_su_pilot.py` | `9f450368acedf011a7dc6f687309a31eabe8b2bbaa06e00e0aabd2409f5ea3ae` |
| `code/primitive_su_formula.py` | `3953dc09223771b02e33f79b855dcfd3c6f8508d09a471ce878db6fc50f33e42` |
| `checks/test_primitive_su.py` | `3cf1eab0d30177ba7060a1fcc171a22067af35c9169d8ba41297d9ee7831be5b` |
| `checks/independent_verifier.py` | `3379afc480f19055f5dba472fbf9274c00088faa05e5ad16a409634a96e1abaa` |
| `checks/proof-and-replay.md` | `32a9dae5f00b566c4e63d844b31c1ee781006b4cd4c78e6c231cb8d6b98e6572` |
| `checks/revision-code-audit.md` | `12df3c5b2b8a8f8d892b33c913b61d206fe43a41dbc981601efe72afd2727356` |
| `evidence/pilot.json` | `d6d5ae10bbe473dd6e8ecb3974481c48e9680ea85cc2c595d805c01c499661be` |
| `evidence/formula.json` | `3145bc4f23fef9c2a2da2c53f53c5e0ec902e56c2eb5c58421c56c8cb1d518a5` |

The retained local aggregate assurance record outside the public repository
has SHA-256
`08c9cd67da8e95b35020db379557f95ec1c09a579669db06960b3128b6240cb0`.
It records normal and optimized independent receipt hashes
`7287681a3e389641175703f11aaf6cd22a49ff5183869e1f037a7a2da8e5ed96`
and
`3d743414ca95718430138f38e056a3ea8fb4024b758d80cec2ec6778040d21ae`.
Those local receipts are provenance for this summary, not shipped public
payloads and not substitutes for the final clean-extraction gate.

## Assurance boundary

These are exact finite diagnostics. They do not prove the all-parameter
theorem, establish the physical-to-categorical bridge, determine electron
action within a resolved short parent orbit, verify a microscopic
realisation, establish novelty, constitute independent human review, or prove
publication. The analytic proof is in the manuscript. Final manifest and
archive binding, green remote CI, provider publication, asset parity, and
canonical readback remain separate gates.
