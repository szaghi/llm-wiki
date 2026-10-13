---
type: Source
title: "Balsara (2004) — Second-order-accurate schemes for magnetohydrodynamics with divergence-free reconstruction"
description: "Consolidates divergence-free MHD scheme design: four open issues resolved via reconstruction-based zone averages, face-variable limiting, C0 normal continuity, and directly evaluated edge EMFs."
resource: "doi:10.1086/381377"
source_kind: paper
authors: [Balsara D.S.]
year: 2004
venue: "Astrophys. J. Suppl. Ser. 151:149-184"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2004-ApJS-Balsara-103847.pdf"
tags: [constrained-transport, divergence-constraint, reconstruction, weno, unsplit, curvilinear, unstructured]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The consolidation paper of divergence-free Godunov MHD: identifies **four
unresolved issues** in the field and resolves each using the
[divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
machinery of Balsara (2001). Adds a new staggered-mesh time update with
edge EMFs evaluated *directly* (no spatial averaging), second- and
third-order accurate in time, dimensionally unsplit; extends the
reconstruction (TVD and WENO $r=2,3$ variants, characteristic limiting,
genuinely multidimensional Barth-type interpolation) to cylindrical,
spherical, and tetrahedral meshes — with appendix formulas that
simultaneously enable AMR in those geometries. Implemented in the RIEMANN
framework; extensive tests including low-$\beta$ magnetospheric flows.

Identifier note: the local filename's DOI tag (`103847`) does **not** match
the actual DOI — identity was verified against page 1 and Crossref
(10.1086/381377, ApJS 151:149–184). Filename hints are untrusted.

# Key claims

The four issues (§1, verbatim in essence) and their resolutions:

1. **Zone-centered field from face data**: arithmetic averaging has no
   theoretical warrant; the *volume average of the reconstruction
   polynomial* is the principled answer (e.g.
   $\bar B_x = (B_x^+ + B_x^-)/2 - a_{xx}\Delta x^2/6$) — resolved by
   reconstruction.
2. **Limit the fundamental variables**: TVD/WENO limiting belongs on the
   *face-centered* fields being evolved, not only on derived zone-centered
   copies — the divergence-free reconstruction admits exactly this, and
   reduces to classical TVD under 1D variation (inheriting TVD stability
   theory).
3. **$C^0$ normal continuity instead of an eighth wave**: the
   reconstruction keeps the normal field component continuous at zone
   faces, eliminating the jump that made seven-wave Riemann solvers
   ill-defined — "thereby eliminating the need for an eight-wave model,"
   with the monopole-free physics invoked against source-term
   formulations ([eight-wave page](/methods/eight-wave.md), Contradictions
   context).
4. **Edge EMFs without averaging**: exploiting the electric-field/flux
   dualism, the EMF is produced directly at zone edges from the
   multidimensional structure of the Riemann data — replacing the
   averaging of [flux-CT](/methods/flux-ct.md)-type schemes; the same
   construction carries to tetrahedral meshes.

Further: local conservation of area-weighted face fields in their
coordinate planes is demonstrated (correcting Falle's 2002 claim that
divergence-free schemes lack conservation properties); accuracy is shown
independent of Riemann-solver quality (dissipation is not); unsplit
schemes beat dimensionally split ones on dissipation; the paper explicitly
lays the roadmap to better-than-second-order divergence-free schemes.

# Notation map

| Balsara (2004) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| face fields $B^{\pm}_x$ etc., edge $E$ | $B_h \in V_h^2$, $E_h \in V_h^1$ | as in Balsara (2001) |
| $a_{xx}, b_{yy}, \dots$ polynomial coefficients | reconstruction coefficients | constrained by pointwise solenoidality |
| $\bar B_x$ volume averages | cell-collocated derived copies | *derived from* face data, never independently evolved |
| dual $E$/flux relation | $E_h$ from Godunov flux components | direct edge evaluation, no averaging |

# Pages created or updated

* Updated [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md) (consolidation: face-variable limiting, WENO variants, curvilinear/unstructured extension, volume-average rule).
* Updated [Flux-CT and the Godunov CT variants](/methods/flux-ct.md) (direct edge-EMF evaluation superseding averaging).
* Updated [Eight-wave formulation](/methods/eight-wave.md) (Issue-3 critique: C0 normal continuity removes the motivation).

# Citations

1. `~/papers/mosaic/div-free-amr/2004-ApJS-Balsara-103847.pdf` (doi:10.1086/381377) — text extraction, pp. 149–184.
