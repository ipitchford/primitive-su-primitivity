# Claims and evidence

Version `1.1.0-candidate` is an unrefereed analytic proof candidate.
[CLAIMS.json](CLAIMS.json) is the machine-readable map; this file gives the
same boundary in compact form.

## Theorem

For every even $N=2n\ge4$ and every nonzero fine charge
$q\in\mathbb Z/N$ in the specified charge-one construction:

1. the resolved sector rank satisfies $R_0-R_q\ge N/2$; and
2. the sector contains two distinct simple objects exchanged by the physical
   electron.

These facts exclude the two allowed electron-compatible invertible-vortex
factor types, including their Abelian-dressed versions. Hence the proposed
$SU(2n)_{2n}$ series is primitive in the originating definition.

## Dependency chain

1. **Induction bridge — Lemma 1.** The fermionic condensate's parity-zero
   representatives are the resolved modules of the even subgroup
   $H=\langle J^2\rangle$, with the original charge grading and electron action
   retained.
2. **Cyclic resolution — Lemma 2.** A stabiliser of order $h$ resolves into
   $h$ simple modules, giving
   $R_q=(2/N)\sum_{Q(a)=q}h(a)^2$.
3. **Known charge maximum — Lemma 3.** A Jordan-totient expansion and cited
   exact charge counts imply $R_q<R_0$ for nonzero $q$. The unrestricted
   count and strict zero-residue maximum are established prior results, not
   claimed as new here.
4. **Absolute rank gap — Corollary.** Integrality gives at least one unit in
   every relevant charge-count difference, omitted neutral terms are at least
   one, and $\sum_{d\mid m}J_2(d)=m^2$ gives $R_0-R_q\ge N/2$. No equality
   classification is claimed.
5. **Rank--electron obstruction — Lemma 4.** Rank mismatch excludes the
   two-object invertible-vortex factor, while a nontrivial electron two-cycle
   excludes the one-object electron-fixed factor. Invertible Abelian dressing
   changes neither obstruction.
6. **Electron pair — Lemma 5.** The full-period label
   $a_0=N-1$, $a_q=1$ supplies a nontrivial electron two-cycle in every
   nonzero sector.

## Finite computation

The public programs reproduce rank vectors at $N=4,6,8,10$ by direct orbit
enumeration and by the divisor formula. The formula implementation checks
strict neutral dominance through even $N=100$. Those results are exact but
bounded; they detect errors and do not prove the universal statement or its
physical semantics.

## Contribution boundary

The family, construction, definition, cyclic resolution, and exact charge
formula are prior work. The supported contribution language is:

> We give a uniform proof of the primitivity proposed by Gao et al., using
> established cyclic-resolution and charge-counting results together with an
> explicit electron-pair obstruction in every nonzero flux sector.

The bounded search found no complete collision for that exact conjunction.
It does not establish absolute priority.

## Explicit non-claims

The release does not claim a new family, a new counting theory, a full
categorical or fusion-rule classification, a microscopic realisation,
experimental validation, formal verification, human peer review, official
REF status, 4-star quality, or completed publication.
