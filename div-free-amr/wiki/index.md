---
okf_version: "0.1"
---

# div-free-amr — Knowledge Bundle

Discrete divergence constraints ($D_h B_h = 0$ in MHD, incompressibility
in CFD) across numerical discretizations, with particular depth on
high-order methods and block-structured AMR refinement interfaces.
**Corpus: 82 sources compiled**: 80 published works, one preprint and one code record
(see the [update log](/log.md)).

**Start here:** the [Notation registry](/notation.md) — normative for
every page — then follow the reading guide.

## Reading guide

1. **The invariant and its taxonomy.**
   [Exact discrete divergence](/properties/exact-discrete-divergence.md)
   is the bundle's center: exact-algebraic (CT) vs tolerance (projection)
   vs truncation (eight-wave) vs controlled (GLM) vs local-only (DG), and
   why the *stencil* is part of any exactness claim.
   [Secondary conservation](/properties/secondary-conservation.md) frames
   it; [free-stream preservation](/properties/free-stream-preservation.md)
   is its sibling.
2. **Where the placement discipline comes from.**
   [Staggered grid](/definitions/staggered-grid.md) (MAC/Yee origins,
   including the necessity-vs-eliminability `Contradictions`),
   [orientation](/definitions/orientation.md) (why primal–dual pairs
   exist), and the same structure in five languages:
   [support-operator/mimetic FD](/definitions/support-operator-method.md),
   [Whitney forms](/definitions/whitney-forms.md),
   [FIT](/methods/finite-integration-technique.md),
   [DEC](/definitions/discrete-exterior-calculus.md),
   [FEEC](/definitions/finite-element-exterior-calculus.md) — with the
   [discrete exactness theorems](/results/discrete-exactness-theorems.md)
   as the shared payoff.
3. **The methods.** [Constrained transport](/methods/constrained-transport.md)
   and its [Godunov variants](/methods/flux-ct.md), the
   [upwind CT](/methods/upwind-constrained-transport.md) design (staggered
   data in every flux, which cancels monopoles), with
   [divergence-free reconstruction](/methods/divergence-free-reconstruction.md);
   [projection](/methods/projection-method.md) and its
   [AMR form](/methods/amr-projection-method.md);
   [eight-wave](/methods/eight-wave.md);
   [GLM cleaning](/methods/glm-divergence-cleaning.md);
   [vector-potential evolution](/methods/vector-potential-evolution.md);
   [mimetic spectral elements](/methods/mimetic-spectral-elements.md)
   (high order + pointwise exactness, conforming meshes).
4. **The AMR interface problem** — the bundle's central question.
   [Block-structured AMR](/definitions/block-structured-amr.md) and
   [refluxing](/methods/refluxing.md);
   [$P_D$](/operators/divergence-free-prolongation.md) and the
   [electric-field correction](/methods/electric-field-correction.md);
   the decisive negative/limiting results:
   [transfer locality limits](/results/transfer-operator-locality-limits.md)
   and the resolved
   [CT–FV equivalence dispute](/results/ct-finite-volume-equivalence.md).
   Production evidence on the collocated side (hypothesis-grade, from the
   [ADAM](/software/adam.md) record): the
   [seam divergence source](/results/collocated-seam-divergence-source.md)
   (exact interior, convergent-but-secular seam, five failed local fixes) and
   the [point-value restriction bound](/results/point-value-restriction-compatibility.md).
5. **The SBP route to high order.**
   [SBP](/definitions/summation-by-parts.md) (incl. convergence-gain
   theory), [SBP-SAT](/methods/sbp-sat.md), and
   [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md)
   at 2:1 interfaces — with the accuracy bound, its order-preserving
   circumvention, and the nonlinear (entropy) caveat: every preserved
   property imposes its own condition on the transfer operators.
6. **Hard limits.**
   [Conservation–orthogonality incompatibility](/results/conservation-orthogonality-incompatibility.md),
   [SBP operator existence](/results/sbp-operator-existence.md),
   [MFD convergence](/results/mfd-convergence.md) (2:1 interfaces as
   degenerate polyhedra), and the production evidence that the
   constraint-control choice changes physics
   ([field-loop advection](/benchmarks/field-loop-advection.md);
   [rotated shock tube](/benchmarks/rotated-shock-tube.md)).

## Catalog

* [Definitions](/definitions/index.md) — precise domain terms.
* [Properties](/properties/index.md) — constraints and invariants a method can hold.
* [Operators](/operators/index.md) — discrete operators and their algebraic identities.
* [Methods](/methods/index.md) — algorithms and schemes.
* [Results](/results/index.md) — theorems, proved properties, impossibility results.
* [Benchmarks](/benchmarks/index.md) — standard test problems.
* [Software](/software/index.md) — codes embodying the methods (ADAM; other production evidence lives on Source pages).
* [Sources](/sources/index.md) — one page per ingested source, with notation maps.
* [Bibliography](/bibliography.md) — complete citation record: every work cited
  by an ingested source, ingested or not, with the citation graph (generated
  from `bibliography.bib`).

## Change history

* [Update log](/log.md) — dated journal of every ingestion and revision.
