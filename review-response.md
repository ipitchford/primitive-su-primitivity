# Response to the supplied review

Version `1.1.0-candidate`, 11 October 2026.

This is a public disposition of the supplied AI-assisted review of the
original four-page manuscript. The third-party review itself is private
`NOASSERTION` material and is not reproduced or relicensed here. The revised
manuscript remains unrefereed and has not received independent human peer
review.

The review recommended minor revisions and identified four major comments and
seven minor comments. Every requested repair is closed in the candidate, as
set out below. The historical prospective assessment remains 2-star overall,
with credible specialist uncertainty toward 3-star and no supported 4-star
case; revision closure is not a rating uplift.

## Major comments

### 1. Put the physical-to-categorical bridge in the paper — closed

Section 2 now contains **Lemma 1 (induction bridge)**. It introduces the
diagonal bosonic algebra in the product with `sVec`, identifies its even
subalgebra with the sum over $H=\langle J^2\rangle$, and uses the induced-module
Hom-space correspondence to explain why parity-zero representatives are the
resolved $A$-modules. It states separately that the original charge-one
assignment, fine $Q$-grading, and the action of $J$ as the retained physical
electron remain in force. The result counts all resolved $A$-modules, not only
local modules. No reconstruction of full crossed braiding is claimed.

### 2. Correct the attribution of the counting ingredients — closed

Section 3 now names **Lemma 3 (known charge maximum)** and distinguishes the
manuscript's application from established mathematics. The unrestricted
$A_L(r)$ formula and roots-of-unity route are attributed to
Elashvili--Jibladze--Pataraia, with Muratovic-Ribic--Wang as a second exact
finite-group route and Brualdi--Newman for the neutral count. The strict
zero-residue maximum is identified as an immediate consequence of the 1999
Proposition 8. The comparison with Closset and collaborators records the level
conversion $k=N$, $K=2N$, subgroup order $N/2$, and the fact that their printed
quotient count groups $R_0+R_{N/2}$ rather than proving every fine-sector
inequality. The short derivation is retained for readability, not claimed as a
new counting formula.

### 3. Explicitly cover Abelian-dressed factors — closed

Section 4 now isolates **Lemma 4 (rank--electron obstruction)**. Rank mismatch
excludes the two-object invertible-vortex factor, while a nontrivial electron
two-cycle excludes the one-object electron-fixed factor. The lemma states that
invertible Abelian dressing preserves the relevant rank and electron action,
and therefore cannot evade either obstruction. Its hypotheses remain the
electron-compatible factorisation convention of the originating definition;
no unrestricted factorisation classification is asserted.

### 4. Make the auxiliary electron-fixed output match the evidence — closed

The unsupported `electron_fixed` output has been removed. The public bounded
diagnostic now reports
`resolved_objects_over_electron_invariant_parent_orbits`: a count of resolved
contributions over parent $H$-orbits preserved by one-step rotation. It does
not say that every resolved constituent is individually fixed. The obsolete
conditional exclusion field based on the stronger interpretation has also
been removed. Tests reject reintroduction of the legacy field in normal and
optimized modes. The universal theorem does not depend on this diagnostic.

## Minor comments

1. **Discoverable title — closed.** The title is now *Primitivity of the
   $SU(2n)_{2n}$ superconducting series*.
2. **Named lemmas — closed.** The induction bridge, cyclic resolution count,
   known charge maximum, rank--electron obstruction, and full-period electron
   pair are named Lemmas 1--5. The quantitative rank gap is a named corollary.
3. **Positive-weight wording — closed.** The text says the binomial weights
   are positive; it does not call the Ramanujan sums positive.
4. **$N=2$ sanity check — closed.** The manuscript and computational audit
   record ranks $(2,1)$ at $N=2$ and the failure of the distinct-parent pair
   witness. This explains why rank dominance alone is insufficient and why
   $N=2$ is outside the theorem.
5. **Exported input contract — closed.** Public `count(N)` and `ranks(N)`
   accept positive even integers only, reject invalid integers with
   `ValueError`, reject invalid types (including `bool`) with `TypeError`, and
   retain load-bearing checks under optimized Python.
6. **Status chronology — closed.** Public status distinguishes the original
   source, the dated supplied review, the revised candidate, DOI reservation,
   and the still-pending publication gates. The original review does not bind
   later bytes automatically.
7. **Versioned references and locators — closed.** Versioned arXiv references,
   theorem/proposition locators, corrected public paths, and the source-version
   convention are recorded in [SOURCES.md](SOURCES.md) and
   [CITATION_AUDIT.md](CITATION_AUDIT.md).

## Optional and bounded extensions

The suggested reusable criterion was adopted as Lemma 4 because it is a short,
transparent abstraction of the same two obstructions. It is presented as an
elementary criterion, not a new categorical theory.

The candidate also proves the quantitative corollary
$R_0-R_q\ge N/2$. Each applicable exact charge-count difference is an integer
of at least one; each omitted neutral term is at least one; and
$\sum_{d\mid m}J_2(d)=m^2$ with $m=N/2$ gives the bound. The example
$N=4,q=2$ attains equality. No general equality classification is claimed.
This is an elementary corollary of established charge counting plus the
resolved-rank formula, not a new counting theory or a basis for automatic
quality uplift.

The review did not require a larger numerical sweep, full fusion tables, a
microscopic model, or proof-assistant formalisation. Those remain outside this
candidate. Finite computation is reported only as supplementary diagnostic
evidence; it does not replace the analytic proof.

## Final disposition

All eleven requested manuscript, attribution, scope, diagnostic, metadata, and
code-contract repairs are implemented in `1.1.0-candidate`. Local mathematical
and computational checks support the revised claim within their stated scope.
Final PDF identity, clean-extraction package gating, remote CI, provider
publication, asset parity, and canonical readback remain separate release
obligations.
