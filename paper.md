# Primitivity of the SU(2n)₂ₙ superconducting series

Anonymous · Version 1.1.0-candidate · 11 October 2026

Version DOI: https://doi.org/10.5281/zenodo.23299598

Unrefereed written-proof candidate. The supplied 11 October 2026 review
concerns the original version; this revision incorporates its
categorical exposition and attribution corrections. Internal review is
not external peer review or formal verification.

## Abstract

Gao et al. propose a family of charge-$`2ne`$ superconductors obtained
from $`SU(2n)_{2n}`$ by identifying its generating fermionic simple
current with the physical electron. Their proposed primitivity means
that no nonzero flux sector separates into an invertible-superconductor
vortex factor and the dynamical anyon sector. We give a uniform argument
for every $`n>1`$. The full neutral rank exceeds every nonzero-sector
rank by at least $`n`$. An explicit electron-paired object in each
nonzero sector then excludes the remaining Ising-type factor. The rank
inequality follows from established cyclic stabilizer resolution and a
known roots-of-unity count with positive binomial weights. The
construction, definition and counting ingredients are prior work; the
claimed advance is their uniform primitivity application with the
electron-pair obstruction. Finite computations check the formulas but
are not used to establish the universal statement.

## 1. Statement and conventions

Set $`N=2n\ge4`$, and let $`\mathcal D=SU(N)_N`$. Write $`J`$ for the
generating simple current. We consider precisely the charge-one
construction of \[1, Sections V.1 and VII.4\]: stack the atomic
insulator and condense the composite of $`J`$ with its charge-one local
fermion. Write $`\mathcal C_q`$ for the resulting flux sector,
$`q\in\mathbb Z/N`$, with physical electron $`f`$ retained. Put
$`R_q=|\mathcal C_q|`$. The set of dynamical anyon representatives has
size $`R_0/2`$. Indeed, transparency and the ribbon identity give
$`\theta_{fX}=-\theta_X`$, excluding $`fX\cong X`$ for a neutral simple
object. Thus electron fusion acts freely on that sector.

**Theorem.** For every even $`N\ge4`$, $`R_0-R_q\ge N/2`$ for every
$`q\ne0`$. Furthermore, every such sector contains two distinct objects
interchanged by electron fusion. Consequently none admits an
electron-compatible factorization into an invertible-superconductor
vortex sector and the dynamical anyon sector. The family is primitive in
the sense of \[1, Section IV.5\].

The term factorization uses the physical electron and object structure
of \[1\], not an arbitrary numerical factorization of ranks. An
invertible vortex sector has either two Abelian objects exchanged by
$`f`$, or one Ising-type object fixed by $`f`$. Allowing both
possibilities in every sector only strengthens the exclusion. This
includes the Abelian-dressed factors of \[1, Sections IV.1–IV.5\]:
tensoring by an invertible object preserves rank and the electron
action. Electron compatibility preserves the specified physical
electron, not an arbitrary order-two object. No claim about a
microscopic realization or a new family of phases is made.

## 2. Resolved objects and cyclic stabilizers

Integrable affine labels are
``` math
X_N=\{(a_0,\ldots,a_{N-1})\in\mathbb Z_{\ge0}^N:\sum_i a_i=N\}.
```
The action of $`J`$ is cyclic rotation $`T`$; the sector is the charge
$`Q(a)=\sum_i i a_i\pmod N`$. Rotation preserves this charge since the
total label sum is $`N`$. Reversing the monodromy convention replaces
$`q`$ by $`-q`$ and has no effect on the result.

Let $`H=\langle J^2\rangle`$, of order $`N/2`$, and
$`A=\bigoplus_{g\in H}g`$. The simple-current twist is
$`\theta_{J^r}=\exp(\pi i r(N-r))=(-1)^r`$. Thus $`H`$ is bosonic and
mutually local, and its regular algebra is condensable. We retain all
$`A`$-modules, including nonlocal modules representing vortex defects.

**Lemma 1 (induction bridge).** The resolved objects in the charge-one
construction are represented by all $`A`$-modules; the retained electron
acts as the image of $`J`$.

*Proof.* In $`\mathcal E=\mathcal D\boxtimes\mathrm{sVec}`$, let
$`f_{\rm loc}`$ be the external electron and set
``` math
B=\bigoplus_{r\in\mathbb Z/N}J^r\boxtimes f_{\rm loc}^{r}.
```
Its summands have twist one and form a bosonic symmetric pointed
subcategory, with regular commutative separable algebra $`B`$ and even
subalgebra $`A\boxtimes1`$. The action on parent pairs is
$`(a,\epsilon)\mapsto(T^ra,\epsilon+r\bmod2)`$. Every orbit has
parity-zero representatives, related precisely by even rotations; their
stabilizers are the $`H`$-stabilizers. Resolution is preserved because
Frobenius reciprocity identifies
``` math
\begin{aligned}
\operatorname{Hom}_B(\operatorname{Ind}_B(a,1),\operatorname{Ind}_B(b,1))
&\cong\bigoplus_{r\ {\rm even}}\operatorname{Hom}_{\mathcal D}(a,J^rb)\\
&\cong\operatorname{Hom}_A(\operatorname{Ind}_A a,\operatorname{Ind}_A b).
\end{aligned}
```
Odd terms vanish since
$`\operatorname{Hom}_{\mathrm{sVec}}(1,f_{\rm loc})=0`$, and composition
agrees through the even subalgebra. Every module is a summand of an
induced module; odd-parity induction is rewritten using $`Ja`$ with
parity zero. Passing to these summands identifies resolved objects.
Electron fusion changes parity, hence gives $`J`$ or its inverse on
parity-zero representatives; their images agree since $`J^2\in H`$.

The charge-one assignment and original $`Q`$-grading remain in force.
Replacing integer local charge by parity for topological species does
not discard the superconducting charge or flux unit, and is not the
charge-two construction with an independent electron. Only object,
induction and electron-action data are identified here, not the full
crossed-braiding or fusion data. Restricting to local $`A`$-modules
would lose sectors: locality with respect to $`J^2`$ only permits
charges $`0,N/2`$, whereas all $`q`$ are required here. Each orbit and
each of its resolved constituents retains the same $`Q`$.

**Lemma 2 (cyclic resolution count).** An $`H`$-orbit with stabilizer
order $`h`$ contributes exactly $`h`$ simple modules.

*Proof.* The count does not assume that every fixed point splits by its
stabilizer in an arbitrary condensation. If
$`h(a)=|\operatorname{Stab}_H(a)|`$, the endomorphism algebra of the
induced module is a twisted group algebra of that stabilizer \[3, Lemma
4.6 and Proposition 4.7\]. The stabilizer is cyclic. Every complex
projective representation of a finite cyclic group can be made linear:
rescale the operator of a generator so that its appropriate power equals
the identity. Its twisted group algebra therefore has $`h(a)`$ distinct
one-dimensional irreducibles. Hence an $`H`$-orbit resolves into exactly
$`h(a)`$ distinct simple modules. Different orbits have no common
constituent \[3\]. This answers the untwisted-stabilizer caveat
emphasized in \[4\].

An orbit has $`(N/2)/h(a)`$ labels. Distributing its $`h(a)`$ resolved
objects among those labels yields the exact formula
``` math
R_q=\frac2N\sum_{a\in X_N:Q(a)=q}h(a)^2.\tag{1}
```
Equivalently, a full rotation orbit of length $`\ell`$ contributes
$`2N/\ell`$ if $`\ell`$ is even, and $`N/(2\ell)`$ if it is odd. These
are the electron-retaining multiplicities of \[1\]. The proof below does
not require determining the electron permutation of each short-orbit
resolution label.

## 3. Exact charge counts

Define $`A_L(r)`$ as the number of nonnegative $`L`$-tuples of sum $`L`$
whose weighted sum is $`r\pmod L`$. Let $`J_2(d)`$ be the second Jordan
totient, characterized by $`h^2=\sum_{d\mid h}J_2(d)`$. It is positive:
$`J_2(d)=d^2\prod_{p\mid d}(1-p^{-2})`$.

For $`d\mid N/2`$, the subgroup of $`H`$ of order $`d`$ fixes precisely
the labels formed by repeating a block of length $`L=N/d`$, $`d`$ times.
The block has sum $`L`$, and $`L`$ is even. If its weighted sum is
$`S`$, the full weighted sum is
``` math
dS+\frac{L^2d(d-1)}2\equiv dS\pmod N.
```
The second term is divisible by $`N=dL`$ because $`L`$ is even.
Consequently (1) gives
``` math
R_q=\frac2N\sum_{\substack{d\mid N/2\\d\mid q}}
J_2(d)A_{N/d}(q/d).\tag{2}
```
For $`q=0`$, every divisor is included.

**Lemma 3 (known charge maximum).** For $`r\ne0\pmod L`$,
$`A_L(r)<A_L(0)`$. The self-contained derivation below specializes \[5,
Theorem 1 and Proposition 8\] to $`n=m=L`$, $`k=r`$. Its strict maximum
is also implied by that source’s nonnegative divisor decomposition. The
finite-group form is \[6, Theorem 1\] for $`\mathbb Z/L`$ and multiset
size $`L`$; the neutral count occurs in \[7, pp. 38–39\].

*Proof.* Write $`c_e(r)`$ for the Ramanujan sum over primitive $`e`$-th
roots raised to the power $`-r`$. A roots-of-unity filter gives
``` math
A_L(r)=\frac1L\sum_{e\mid L}c_e(r)
\binom{2L/e-1}{L/e}.\tag{3}
```
Indeed, at an $`L`$-th root $`z`$ of exact order $`e`$,
``` math
\prod_{i=0}^{L-1}(1-tz^i)^{-1}=(1-t^e)^{-L/e}.
```
Its $`t^L`$ coefficient is the binomial coefficient in (3). Grouping the
root filter by exact order proves the identity.

Every $`c_e(r)`$ is real and at most $`\varphi(e)=c_e(0)`$: pair
conjugate roots and bound each real part by one. If $`r\ne0\pmod L`$,
the inequality for $`e=L`$ is strict, since the primitive root
$`\exp(2\pi i/L)`$ raised to $`r`$ is not one. All binomial coefficients
in (3) are positive. Therefore
``` math
A_L(r)<A_L(0)\qquad(r\ne0\pmod L).\tag{4}
```
Compare (2) at $`q\ne0`$ and at zero. Each included term is at most the
corresponding zero-sector term by (4); omitted terms are nonnegative.
The $`d=1`$ term is strictly smaller. Thus $`R_q<R_0`$, uniformly in
$`N`$ and $`q`$.

**Corollary (absolute rank gap).** For every even $`N\ge4`$ and
$`0<q<N`$, $`R_0-R_q\ge N/2`$.

*Proof.* For every $`d\mid N/2`$ with $`d\mid q`$, we have
$`0<q/d<N/d`$. Lemma 3 and integrality imply
$`A_{N/d}(0)-A_{N/d}(q/d)\ge1`$. If $`d\nmid q`$, the omitted neutral
term satisfies $`A_{N/d}(0)\ge1`$, witnessed by the block
$`(N/d,0,\ldots,0)`$. Subtracting equation (2) sectorwise therefore
gives
``` math
R_0-R_q\ge\frac2N\sum_{d\mid N/2}J_2(d)
 =\frac2N\left(\frac N2\right)^2=\frac N2.
```
This is an elementary quantitative consequence of the known strict
charge maximum and the resolved-rank formula, not a new counting theory.
Equality occurs at $`N=4,q=2`$, since $`8-6=2`$. No classification of
all equality cases is asserted.

## 4. Excluding the remaining factor

**Lemma 4 (rank–electron obstruction).** Suppose the neutral simple
objects carry a free physical-electron involution, with $`D=R_0/2`$
dynamical representatives. Suppose the permitted electron-compatible
vortex factors have either two objects exchanged by that electron, or
one electron-fixed object, with products counted over the $`D`$
representatives. A sector of rank different from $`R_0`$ containing an
electron-moved object admits neither factorization. The conclusion is
unchanged by invertible Abelian dressing.

*Proof.* The two-object product has $`2D=R_0`$ objects. In the
one-object product, the specified electron fixes every product object.
Both conclusions contradict the respective hypotheses. Tensoring by an
invertible dressing object is a bijection on simple objects and
intertwines the specified electron action, so does not alter either
obstruction. This criterion is an elementary unpacking of the two
allowed factor types, not a classification of other possible
factorizations or a new general condensation theorem.

**Lemma 5 (full-period electron pair).** Every nonzero sector contains
distinct simple objects exchanged by the physical electron.

*Proof.* For any $`1\le q<N`$, take $`a_0=N-1`$, $`a_q=1`$, with all
other entries zero. This label has charge $`q`$. Its unique largest
entry forces its full rotation period to be $`N`$, so its stabilizer in
$`H`$ is trivial. Its induced module is simple. The rotated label $`Ta`$
is in a different $`H`$-orbit: equality $`Ta=T^{2j}a`$ would give an odd
rotation fixing a full-period label. The two induced modules are
distinct and exchanged by the image of $`J`$, namely $`f`$. This
contradicts the one-object factor. Both possible factor types are
excluded in every nonzero sector, proving the theorem.

The restriction $`N\ge4`$ matters. At $`N=2`$, the chosen label is
$`(1,1)`$, which has no unique largest entry. This is the familiar
invertible Ising case and is not part of the claim.

## 5. Checks, scope and prior work

The boundary case $`N=2`$ has ranks $`(2,1)`$: it passes the strict rank
test but its proposed witness $`(1,1)`$ is fixed. It therefore
demonstrates why the electron-pair obstruction is indispensable.

Direct label enumeration and the separately implemented divisor formula
give full rank vectors $`(8,4,6,4)`$ for $`N=4`$ and
$`(32,25,26,28,26,25)`$ for $`N=6`$, reproducing \[1\]. They also agree
at $`N=8,10`$; divisor-formula inequalities were checked through
$`N=100`$. These exact integer calculations detect convention and coding
errors, but no finite check substitutes for Sections 2–4. The auxiliary
diagnostic counts resolved objects lying over $`J`$-invariant
$`H`$-orbits. It does not determine whether each resolved constituent is
individually electron-fixed: electron fusion may permute constituents
over an invariant orbit. Neither rank checks nor the full-period witness
relies on that diagnostic. Exported rank functions support positive even
$`N`$, with $`N=2`$ retained only as a boundary check; the theorem
requires $`N\ge4`$.

The family was constructed in \[2\], and \[1\] proposes its primitivity
while leaving a general proof open. Cyclic module resolution is
established machinery \[3,4\], and the charge count and strict maximum
have exact predecessors \[5–7\]. Our claimed addition is their
application with the full-period electron pair, closing that particular
all-parameter primitivity gap. We do not claim a new condensation
theory, a full classification, computed fusion rules, experimental
realization, or an independently assessed contribution rating.

Version control matters for comparison: \[2\] v1 assigned four objects
to the all-ones $`N=4`$ fixed point; v4 corrects that count to two, in
agreement with \[1\]. The calculations here retain the physical electron
and use the later convention throughout, specifically \[2, supplementary
equation (S24), PDF p. 11\].

Closset and collaborators \[8, Section 3.4 and Section 4.1; 9, Section
3.1.4\] give close charge, orbit, stabilizer and Jordan-totient counting
machinery. Their supersymmetric level is $`K=k+N`$, so our bosonic level
$`k=N`$ corresponds to $`K=2N`$, with gauged subgroup order $`N/2`$.
Their subgroup-neutral quotient counts combine fine charges: the
corresponding count is $`R_q+R_{q+N/2}`$, up to charge sign convention,
rather than an individual $`R_q`$. For example, the zero-theta counts
are $`14=8+6`$ at $`N=4`$ and $`60=32+28`$ at $`N=6`$. These printed
coarse counts alone do not separate charge zero from $`N/2`$, or supply
the electron-pair obstruction. Their broader formalism remains an
important counting predecessor, not a claim of methodological
independence here. No complete earlier primitivity proof was found in
the bounded source comparison conducted on 11 October 2026; this is not
a certification of historical priority.

## Declarations

The scholarly creator is Anonymous. AI-assisted preparation includes
review remediation, source comparison and internal mathematical checks.
No human research contribution is inferred from publication authority.
The manuscript is a theoretical candidate, not a claim of microscopic
realization, experimental validation or formal verification. Supplied
review assessments remain tied to their inspected versions.

## References

1.  Z.-Q. Gao, Y.-Q. Wang, H. Yang, Z. Han and A. Vishwanath, *SC-sharp:
    superconductivity intertwined with topological order*,
    [arXiv:2610.10679v1](https://arxiv.org/html/2610.10679v1), 2026.

2.  Z.-Q. Gao, Y.-Q. Wang, H. Yang and C. Wu, *Topological Charge-2ne
    Superconductors*,
    [arXiv:2512.21325v4](https://arxiv.org/html/2512.21325v4), 2026.

3.  J. Fuchs, I. Runkel and C. Schweigert, *TFT construction of RCFT
    correlators III: Simple currents*,
    [hep-th/0403157](https://arxiv.org/pdf/hep-th/0403157), 2004.

4.  P. Bantay, *The Untwisted Stabilizer in Simple Current Extensions*,
    [hep-th/9611194](https://arxiv.org/pdf/hep-th/9611194), 1996.

5.  A. Elashvili, M. Jibladze and D. Pataraia, *Combinatorics of
    necklaces and “Hermite reciprocity”*, Journal of Algebraic
    Combinatorics 10 (1999), 173–188, Theorem 1 and Proposition 8.
    <https://rmi.tsu.ge/~jib/pubs/elajipa.pdf>.

6.  A. Muratović-Ribić and Q. Wang, *The multisubset sum problem for
    finite abelian groups*,
    [arXiv:1305.3259](https://arxiv.org/pdf/1305.3259), 2013, Theorem 1.

7.  R. A. Brualdi and M. Newman, *An enumeration problem for a
    congruence equation*, Journal of Research of the National Bureau of
    Standards, Section B, 74B (1970), 37–40.
    <https://nvlpubs.nist.gov/nistpubs/jres/74B/jresv74Bn1p37_A1b.pdf>.

8.  C. Closset, E. Furrer and O. Khlaif, *One-form symmetries and the 3d
    N=2 A-model: Topologically twisted indices and CS theories*, SciPost
    Physics 18 (2025), 066.
    [doi:10.21468/SciPostPhys.18.2.066](https://doi.org/10.21468/SciPostPhys.18.2.066).
    Inspected version:
    [arXiv:2405.18141v4](https://arxiv.org/html/2405.18141v4), Sections
    3.4 and 4.1, equations (3.85), (3.95) and (3.101).

9.  C. Closset, E. Furrer, A. Keyes and O. Khlaif, *The 3d A-model and
    generalised symmetries, Part I: Bosonic Chern–Simons theories*,
    SciPost Physics 19 (2025), 106. Inspected version:
    [arXiv:2501.11665v3](https://arxiv.org/html/2501.11665v3), Section
    3.1.4.
