---
schema_version: "1.0"
package: primitive-su-primitivity
version: 1.1.0-candidate
status: candidate-not-published
scholarly_creator: Anonymous
doi: 10.5281/zenodo.23299598
doi_status: reserved-draft-not-published
---

# AI index

This is the machine-oriented entry point for the primitive
$SU(2n)_{2n}$ primitivity candidate. The primary result is a written universal
proof about a previously proposed superconducting family. Bounded computation
is supplementary and must not be treated as proof of the all-parameter claim.

## Exact claims

- [CLAIMS.json](CLAIMS.json) — structured theorem, hypotheses, dependencies,
  evidence, and non-claims.
- [claims.md](claims.md) — human-readable claim and proof-dependency map.
- [paper.tex](paper.tex) — canonical manuscript source.
- [paper.pdf](paper.pdf) — rendered manuscript; use the final QA receipt and
  manifest for its immutable identity.
- [paper.md](paper.md) — accessible manuscript rendering.

## Compact theorem

For $N=2n\ge4$, let $\mathcal C_q$ be the fine charge-$q$ sector of the
specified charge-one $SU(N)_N$ construction with physical electron $f$.
For every $q\ne0$, the manuscript proves both $R_0-R_q\ge N/2$ and the
existence of two distinct objects in $\mathcal C_q$ exchanged by $f$. These
exclude the two electron-compatible invertible-vortex factor types and imply
primitivity.

The dependency chain is: induction bridge (Lemma 1), cyclic resolution and
rank identity (Lemma 2), cited strict charge maximum applied to the fine-sector
rank (Lemma 3), the elementary absolute-gap corollary, the rank--electron
criterion including Abelian dressing (Lemma 4), and a full-period electron
pair (Lemma 5).

## Contribution boundary

- Gao et al. supply the family, charge-one construction, definition of
  primitivity, and proposed all-parameter property.
- Fuchs, Runkel, and Schweigert supply the orbit and twisted-stabiliser
  machinery; cyclic linearisation is an elementary additional step.
- Elashvili, Jibladze, and Pataraia and Muratovic-Ribic and Wang already supply
  the unrestricted charge count; the strict zero-residue maximum follows from
  the former's Proposition 8.
- Closset and collaborators supply close quotient-counting machinery that
  groups fine sectors rather than proving every individual fine-sector
  inequality.

The supported residual claim is a uniform primitivity proof using established
ingredients plus an explicit electron-pair obstruction. Do not describe this
package as a new family, a new counting theory, or a certified first proof.

## Evidence and replay

- [code/primitive_su_pilot.py](code/primitive_su_pilot.py) — direct bounded
  orbit enumeration.
- [code/primitive_su_formula.py](code/primitive_su_formula.py) — independent
  divisor-formula implementation.
- [evidence/pilot.json](evidence/pilot.json) and
  [evidence/formula.json](evidence/formula.json) — retained finite outputs.
- [checks/proof-and-replay.md](checks/proof-and-replay.md) — public proof/replay
  boundary; use the final release receipt for clean-extraction commands and
  environment.
- [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md) and
  [ENVIRONMENT.txt](ENVIRONMENT.txt) — exact recorded local replay summary,
  bound file hashes, and environment limits.

Finite checks cover $N=2,4,6,8,10$ directly, 5,050 independent charge cells,
all even rank vectors through $N=100$, and the absolute gap for every checked
nonzero sector at $4\le N\le100$. Normal and optimized suites reject five
semantic corruptions, and both evidence outputs replay byte-identically. These
checks do not establish the universal theorem, the physical interpretation, or
formal verification.

## Status, assurance, and review

- [STATUS.md](STATUS.md) — completed and pending gates.
- [ASSURANCE.md](ASSURANCE.md) — what each evidence type supports and excludes.
- [PROVENANCE.md](PROVENANCE.md) — frozen source and private-review identities.
- [review-response.md](review-response.md) — public disposition of four major
  and seven minor review comments.
- [ref-assessment.md](ref-assessment.md) — central prospective 2-star assessment,
  credible 3-star uncertainty, and no supported 4-star case.
- [RESEARCH_GATES.json](RESEARCH_GATES.json) — contribution, source, limitation,
  and extension triage.

The supplied review is third-party `NOASSERTION` material and is not shipped.
Internal or AI-assisted review is not human peer review.

The current six-page PDF has SHA-256
`a8e27f8b1f0e2ec7fb99b7dd70e46105f0842e880325ec657b8eb06a7449b8c2`;
[publication/qa.json](publication/qa.json) records successful compilation,
zero overfull boxes, and page-by-page visual inspection. This is presentation
QA, not theorem verification or publication proof.

## Sources and rights

- [SOURCES.md](SOURCES.md), [CITATION_AUDIT.md](CITATION_AUDIT.md), and
  [prior-art.md](prior-art.md) — primary-source roles, exact collisions, and
  bounded search limits.
- [LICENSES.md](LICENSES.md) and [PUBLIC_DOMAIN.md](PUBLIC_DOMAIN.md) — CC0/MIT
  map and third-party exclusions.

## Machine-use cautions

1. Preserve $N\ge4$, the charge-one construction, the fine-sector grading,
   and the electron-compatible factorisation convention.
2. Do not infer pointwise electron fixedness from invariance of an unresolved
   orbit; the final diagnostic label records only what is actually computed.
3. Do not infer global novelty from the bounded negative search.
4. Do not infer public release from local files, hashes, CI, or DOI reservation.
