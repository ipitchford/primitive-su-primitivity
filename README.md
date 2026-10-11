# Primitivity of the $SU(2n)_{2n}$ superconducting series

This repository is the `1.1.0-candidate` public research package for a
uniform primitivity theorem about the charge-$2ne$ superconducting series
proposed by Gao and collaborators. The scholarly creator is **Anonymous**.
Ian Pitchford is the repository maintainer and publisher, not an inferred
scholarly contributor.

This is an unrefereed release candidate. The anticipated public repository is
`https://github.com/ipitchford/primitive-su-primitivity`. The version DOI
`10.5281/zenodo.23299598` is reserved on an unpublished draft record. A local
package, a review disposition, or a DOI reservation is not publication.

## Main result

Put $N=2n\ge 4$ and consider the charge-one construction based on
$SU(N)_N$, with the physical electron retained. Let $\mathcal C_q$ be the
resolved flux sector of charge $q\in\mathbb Z/N$, let
$R_q=|\mathcal C_q|$, and let $f$ denote electron fusion.

The manuscript proves that, for every nonzero $q$:

1. $R_0-R_q\ge N/2$; and
2. $\mathcal C_q$ contains two distinct simple objects exchanged by $f$.

The first obstruction excludes a two-object invertible vortex factor. The
second excludes the remaining one-object Ising possibility. The same
obstructions survive Abelian dressing under the electron-compatible
factorisation convention of the originating construction. Consequently every
member of the series with $n>1$ is primitive in the stated sense.

The family, the physical construction, the definition of primitivity, cyclic
fixed-point resolution, and the exact charge-counting formula are prior work.
The claimed contribution is their assembly into a uniform, all-sector
primitivity proof, including the electron-pair obstruction. The bounded search
did not locate an earlier complete proof of that exact statement; this is not
a universal priority claim.

## Proof architecture

- Lemma 1 identifies the charge-one fermionic construction with the
  even-subgroup module description used in the count.
- Lemma 2 proves that a parent-label orbit with cyclic stabiliser of order $h$
  resolves into exactly $h$ simple modules, yielding
  $R_q=(2/N)\sum_{Q(a)=q}h(a)^2$.
- Lemma 3 applies established exact charge-counting results to show that the
  zero residue is the strict maximum. The following corollary keeps the
  integer gap in every divisor summand and obtains $R_0-R_q\ge N/2$.
- Lemma 4 isolates the elementary rank--electron obstruction, including the
  Abelian-dressed factor types permitted by the originating definition.
- Lemma 5 uses the label $a_0=N-1$, $a_q=1$ to produce two distinct simple
  objects exchanged by the electron in every nonzero sector.

The proof is a written analytic argument. It has not been formalised in a
proof assistant and has not received independent human peer review.

## Finite checks

The public Python programs and independent verifier implement bounded exact
diagnostics. Direct label enumeration covers $N=2,4,6,8,10$; independent
charge counts cover 5,050 cells through length 100; exact rank comparisons
cover every even $N\le100$; and the quantitative gap is checked for every
nonzero sector at even $4\le N\le100$. Five semantic corruptions are rejected
in normal and optimized runs. These exact integer checks catch convention and
implementation errors; no finite range establishes the universal theorem or
its physical interpretation. Fresh clean-extraction replay remains a distinct
package-freeze gate.

## Start here

- [paper.tex](paper.tex), [paper.pdf](paper.pdf), and [paper.md](paper.md) —
  manuscript source and reader formats.
- [CLAIMS.json](CLAIMS.json) and [claims.md](claims.md) — exact statements,
  dependencies, evidence, and non-claims.
- [AI_INDEX.md](AI_INDEX.md) — machine-oriented package navigation.
- [STATUS.md](STATUS.md) and [ASSURANCE.md](ASSURANCE.md) — current state and
  evidence boundaries.
- [review-response.md](review-response.md) — point-by-point disposition of the
  supplied review without redistributing it.
- [SOURCES.md](SOURCES.md), [CITATION_AUDIT.md](CITATION_AUDIT.md), and
  [prior-art.md](prior-art.md) — source roles and bounded contribution
  comparison.
- [PROVENANCE.md](PROVENANCE.md) and [LICENSES.md](LICENSES.md) — frozen-source,
  role, and rights records.
- [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md) and
  [ENVIRONMENT.txt](ENVIRONMENT.txt) — recorded local commands, finite scope,
  file identities, environment, and explicit clean-freeze boundary.

## Review and quality boundary

The supplied AI-assisted review recommended minor revisions and found no
mathematical error in the universal argument. Its central prospective
assessment was 2-star overall, with a credible specialist uncertainty toward
3-star if the result's importance is judged more strongly. It found no
supported 4-star case. The retained standalone obstruction lemma is an
elementary abstraction of the same proof mechanism; its inclusion, and the
elementary quantitative rank-gap corollary, do not by themselves raise
originality, significance, or the historical quality assessment.
This is neither human peer review nor an official REF decision.

## Rights

Original non-code contents are dedicated under CC0-1.0. Original executable
code is licensed under MIT. Cited works, archived service metadata, and the
supplied third-party review are not relicensed or redistributed here. See
[LICENSES.md](LICENSES.md).
