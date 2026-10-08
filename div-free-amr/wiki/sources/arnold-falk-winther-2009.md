---
type: Source
title: "Arnold, Falk & Winther (2009) — Finite element exterior calculus: from Hodge theory to numerical stability"
description: "The abstract FEEC stability theory: on closed Hilbert complexes, a subcomplex plus a bounded cochain projection yield inherited cohomology and stable Hodge-Laplacian discretization."
resource: "arXiv:0906.4325 (Bull. AMS 47:281-354, 2010)"
source_kind: paper
authors: [Arnold D.N., Falk R.S., Winther R.]
year: 2009
venue: "arXiv:0906.4325v3; Bull. Amer. Math. Soc. 47:281-354 (2010), doi:10.1090/S0273-0979-10-01278-4"
local_file: "~/papers/mosaic/div-free-amr/2009-arXiv-Arnold-1048550arXiv09064325.pdf"
tags: [feec, hilbert-complex, stability, hodge, cohomology, cochain-projection]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The mature, abstract form of
[FEEC](/definitions/finite-element-exterior-calculus.md): well-posedness
lives in the Hodge theory of a **closed Hilbert complex** (differentials
with closed range), and discretization is stable when the Hodge-theoretic
structure transfers to the discrete level. The **master criterion**: finite
element spaces must (i) form a *subcomplex* of the Hilbert complex and
(ii) admit a *bounded cochain projection* onto it (plus a minor consistency
condition). Under these hypotheses the subcomplex inherits the cohomology —
the projections induce an isomorphism of harmonic forms with error
estimates — and the Galerkin discretization of the abstract Hodge Laplacian
(in mixed/saddle-point form) is stable. The de Rham complex is then the
canonical instance: Koszul-built families, degrees of freedom, bounded
projections constructed, hypotheses verified. The elasticity complex (with
a *second-order* differential) shows the framework's reach beyond de Rham.

**Coverage of this ingestion (scoped):** §§1, 3 (framework and abstract
theory) read closely; §§2, 4–7 at the level of the introduction's
statements; detailed proofs and the elasticity development not compiled.

# Key claims

1. **Two hypotheses suffice** — subcomplex + bounded cochain projection:
   "the natural hypotheses to establish the stability of the corresponding
   discrete Hodge Laplacian." Stability is *transferred structure*, not a
   per-scheme estimate.
2. **Closedness is the well-posedness carrier**: the abstract Hodge
   Laplacian's saddle-point problem is well-posed on *closed* Hilbert
   complexes; harmonic spaces ≅ cohomology groups.
3. **Cohomology inheritance with rates**: under the hypotheses, discrete
   harmonic forms approximate harmonic forms with error bounds — the
   quantitative upgrade over the qualitative exactness statements of the
   discrete-object frameworks
   ([discrete exactness theorems](/results/discrete-exactness-theorems.md)).
4. **Lineage acknowledged**: Whitney's 1957 complex is, in this
   terminology, already a finite element de Rham subcomplex — built for
   geometry (proving de Rham's theorem), repurposed for numerics.

# Notation map

| AFW 2009 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| Hilbert complex $(W^k, d^k)$ | abstraction over $V_h^k$ chains | continuous level |
| bounded cochain projection $\pi_h$ | commuting interpolation $\Pi$ (Hiptmair) made norm-bounded | the stability-carrying property |
| harmonic forms $\mathfrak{H}^k$ | cohomology representatives | Betti-dimensional |

# Pages created or updated

* Updated [FEEC](/definitions/finite-element-exterior-calculus.md) (master stability criterion made precise).

# Citations

1. `~/papers/mosaic/div-free-amr/2009-arXiv-Arnold-1048550arXiv09064325.pdf` (arXiv:0906.4325) — scoped read: §§1, 3 closely; remainder at introduction level.
