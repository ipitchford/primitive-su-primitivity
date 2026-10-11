# Citation audit

Audit date: 11 October 2026. This record distinguishes imported results from
the manuscript's residual application and records source-version conventions.

## 1. Originating family and target definition

**Citation:** Gao, Wang, Yang, Han, and Vishwanath,
*SC-sharp: superconductivity intertwined with topological order*,
arXiv:2610.10679v1.

**Inspected:** Sections IV.5 and VII.4 and the closing open-directions
paragraph.

**Supports:** the charge-one construction, fine flux sectors, physical
electron, definition of primitivity, and the statement that a rigorous proof
for the proposed series is deferred.

**Does not support:** a priority claim for this package or the absence of
simultaneous work.

## 2. Earlier construction and version convention

**Citation:** Gao, Wang, Yang, and Wu,
*Topological Charge-2ne Superconductors*, arXiv:2512.21325v4.

**Supports:** the family construction and later electron-retaining
fixed-point convention. Version 4 is load-bearing: the package does not use an
older fourfold $N=4$ split.

## 3. Exact charge-count formula and strict maximum

**Citation:** Elashvili, Jibladze, and Pataraia,
*Combinatorics of necklaces and "Hermite reciprocity"* (1999), Theorem 1,
equation (4), and Proposition 8.

**Checked relationship:** set their $n=m=L$ and $k=r$; after
$\binom{2u}{u}=2\binom{2u-1}{u}$, their formula is exactly the manuscript's
$A_L(r)$ identity. Proposition 8 expresses the counts as nonnegative divisor
sums. For $0<r<L$, the neutral sum has the additional $d=L$ term
$a_1(1,1)=1$, so $A_L(0)>A_L(r)$ and indeed the integer difference is at
least one.

**Treatment:** exact prior-art collision. The manuscript's derivation is
self-contained exposition, not a novelty claim.

**Corroborating routes:** Muratovic-Ribic and Wang, arXiv:1305.3259, Theorem 1,
give the same all-charge count for finite abelian groups; Brualdi and Newman
(1970), pp. 37-39, give the neutral count.

## 4. Cyclic fixed-point resolution

**Citation:** Fuchs, Runkel, and Schweigert, hep-th/0403157, Lemma 4.6 and
Proposition 4.7, with Remark 4.10; Bantay, hep-th/9611194.

**Supports:** simple-current orbit equivalence, disjoint constituents, and the
twisted stabiliser algebra, together with the warning that full stabiliser
size is not generally the resolved multiplicity.

**Manuscript-specific step:** because the stabiliser here is cyclic, its
projective cocycle can be linearised, producing $h$ one-dimensional
irreducibles. That elementary step is stated separately and is not
misattributed to the cited proposition.

## 5. Closset quotient-count comparison

**Citations:** Closset, Furrer, Keyes, and Khlaif, arXiv:2501.11665v3,
Sections 3.1.1-3.1.4; Closset, Furrer, and Khlaif,
arXiv:2405.18141v4, Section 3.4.

**Convention check:** their supersymmetric level is $K=k+N$. This package has
$k=N$, hence $K=2N$, and uses subgroup order $r=N/2$. Their quotient selection
groups fine charges $0$ and $N/2$, so the relevant printed count is
$R_0+R_{N/2}$, not $R_0$. Numerically it is $14=8+6$ for $N=4$ and
$60=32+28$ for $N=6$.

**Implication:** the papers are substantial methodological predecessors for
charge/orbit/stabiliser/Jordan counting. The inspected formulas do not by
themselves state every fine-sector inequality or the all-sector physical
electron-pair obstruction.

## 6. Reusable criterion and quantitative gap

The standalone rank-plus-electron obstruction is presented as an elementary
abstraction of the originating factor definition. It is not cited as a new
categorical theory.

The corollary $R_0-R_q\ge N/2$ uses the integer gap of at least one from the
Elashvili--Jibladze--Pataraia decomposition in every applicable divisor term,
the positivity of omitted neutral terms, and the standard identity
$\sum_{d\mid m}J_2(d)=m^2$. It is described as an elementary corollary of
prior counting plus the package's resolved-rank formula. No equality
classification or rating uplift is inferred.

## Internal consistency and limits

- The supported contribution sentence in the paper, README, claims, and source
  record must remain identical in substance.
- `first`, `new family`, `new counting theory`, and absolute priority language
  are unsupported.
- The current search is bounded and unusually exposed to indexing delay
  because the originating proposal was four days old.
- Bibliographic existence and finite numerical agreement do not validate the
  imported categorical interpretation.
