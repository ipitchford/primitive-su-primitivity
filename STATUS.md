# Release status

Version: `1.1.0-candidate`  
Status date: 11 October 2026  
Scholarly creator: Anonymous  
Anticipated repository: `ipitchford/primitive-su-primitivity`  
Reserved DOI: `10.5281/zenodo.23299598`  
Publication status: reserved draft; not published

The DOI belongs to an unsubmitted Zenodo draft with no published files at the
time of reservation. Reservation, metadata consistency, archive freeze,
provider publication, provider-byte parity, and canonical readback are
distinct gates.

## Scientific status

- The candidate proves a uniform primitivity statement for every even
  $N=2n\ge4$ and every nonzero charge sector, including the bound
  $R_0-R_q\ge N/2$.
- The proof combines a self-contained induction bridge, cyclic module
  resolution, established exact charge counts, strict neutral-rank dominance,
  and an explicit electron-exchanged pair.
- The supplied review recommended minor revisions and found no mathematical
  error in the universal argument. Its requested exposition, attribution,
  factorisation-scope, and auxiliary-diagnostic repairs are tracked in
  [review-response.md](review-response.md).
- The historical central prospective assessment remains 2-star overall, with
  a credible 3-star uncertainty boundary and no supported 4-star case.
- The written argument is not formally verified and has not received
  independent human peer review.

## Evidence state

| Gate | Current evidence | Status |
|---|---|---|
| Supplied source archive | SHA-256 `73bc28c95f806381dc4984224bd4653a92e1f69ab1a02518641b76e3f8b54f30` | identity recorded |
| Extracted source ledger | 25 listed files in the frozen `source/` tree check byte-for-byte | complete for historical source |
| Supplied review archive | SHA-256 `9c7cd4dcbda6358bc01365552deaa1fde273f3e446efc4159d5b8e307796c71e` | private historical evidence; not redistributed |
| Historical review | Minor revisions; no mathematical error found; central 2-star overall | complete for reviewed bytes only |
| Analytic theorem | Written all-$N$, all-nonzero-sector proof in the manuscript | candidate proof; not formal verification |
| Bounded computations | Normal and optimized seven-test suites pass under CPython 3.13.5; direct enumeration covers $N=2,4,6,8,10$; 5,050 independent charge cells and all even ranks through 100 agree; five semantic corruptions are rejected; public evidence replays byte-identically | complete in the recorded local environment; supplementary only |
| Rights map | CC0-1.0 / MIT / third-party `NOASSERTION` boundary documented | complete |
| Fresh package replay | Recorded local replay and public checks are complete; final clean-extraction archive binding remains | pending final package gate |
| Manuscript rendering | Six-page PDF SHA-256 `a8e27f8b1f0e2ec7fb99b7dd70e46105f0842e880325ec657b8eb06a7449b8c2`; two-pass build; zero overfull boxes; every page inspected | complete for current candidate; final manifest binding pending |
| DOI and public release | DOI `10.5281/zenodo.23299598` reserved on an unpublished draft; GitHub/Zenodo publication, parity, and canonical readback remain | reservation complete; publication pending |

The source and review archive hashes establish identity, not correctness or
publication. The historical review does not automatically bind later revised
bytes.

## Pending publication gates

Before any claim that this candidate is public and frozen, the main publication
lane must:

1. bind the completed manuscript and finite-check receipts into the final
   manifest;
2. rerun the package-specific clean-extraction gate against that exact archive;
3. synchronize all coupled metadata with the reserved DOI;
4. generate the complete manifest and checksum ledger;
5. preserve the six-page PDF QA identity during archive creation;
6. obtain green repository CI and bind the immutable tag and assets;
7. verify GitHub and Zenodo asset parity; and
8. perform canonical Evidence Press readback.

A local `DONE` label, a review archive, a green finite replay, or a reserved DOI
does not substitute for these publication gates.
