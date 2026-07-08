---
type: Source
title: "Fromang, Hennebelle & Teyssier (2006) — A high order Godunov scheme with constrained transport and adaptive mesh refinement for astrophysical magnetohydrodynamics"
description: "RAMSES-MHD: MUSCL-Hancock Godunov scheme with CT on tree-based (octree) AMR, with 2D-Riemann EMFs; production evidence on MRI and magnetized core collapse."
resource: "doi:10.1051/0004-6361:20065371"
source_kind: paper
authors: [Fromang S., Hennebelle P., Teyssier R.]
year: 2006
venue: "Astron. Astrophys. 457:371-384"
local_file: "~/papers/mosaic/div-free-amr/2006-A&A-Fromang-10105100046361_20065371.pdf"
tags: [constrained-transport, amr, octree, godunov, production-code, mhd]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The RAMSES-MHD paper: the MUSCL-Hancock Godunov scheme extended to full
ideal MHD with [constrained transport](/methods/constrained-transport.md),
on RAMSES's **tree-based AMR** — a fully threaded tree of "octs" (groups of
8 cells sharing a parent), refined cell-by-cell rather than by rectangular
patches. Following Londrillo & Del Zanna, the MHD system splits into the
Euler subsystem (cell-centered, finite-volume) and the induction subsystem
(face-centered fluxes, edge EMFs). Demonstrated on 1D/2D standard tests and
3D applications (magnetorotational instability in shearing boxes;
magnetized cloud-core collapse).

# Key claims

1. **C-MUSCL predictor + 2D-Riemann corrector**: the predictor interpolates
   EMFs to edges by simple arithmetic averages (cheaper, slightly stronger
   CFL, performance comparable to costlier variants); the corrector
   computes edge EMFs from the **four-state 2D Riemann approximation**
   (after [Londrillo & Del Zanna](/sources/londrillo-delzanna-2000.md)'s
   four-state formula and its nonlinear-solver variants) — with the two Roe
   dissipation contributions explicit ([flux-CT](/methods/flux-ct.md)
   lineage).
2. **Tree-based AMR**, not patches: fully threaded tree, oct granularity,
   unit-cube root; the CT face/edge structure is maintained on the tree.
   The divergence-free prolongation machinery is inherited from the
   companion induction-equation paper (Teyssier, Fromang & Dormy 2006 —
   **not in this corpus**; interface details are compiled only to the
   level this paper states them).
3. **AMR as a resolution instrument for solution selection**: on
   Torrilhon's compound-wave shock tube, uniform grids converge to the
   regular solution only at very large resolution; with AMR at equal CPU
   time the effective resolution reaches $\sim 10^6$-cell equivalence and
   moves the solution decisively toward the regular one — an argument that
   AMR changes *which physics you converge to* at fixed cost.
4. **Solver robustness**: Lax–Friedrichs and Roe variants; Roe slightly
   better on smooth-loop advection energy decay.

# Notation map

| Fromang et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| face-centered $B$, edge EMFs $E_z$ etc. | $B_h \in V_h^2$, $E_h \in V_h^1$ | CT standard |
| cell-centered $W$ incl. averaged $B$ | derived cell copies | from face averages |
| oct / split cell / leaf cell | tree-based AMR vocabulary | contrast patch-based |

# Pages created or updated

* Updated [Block-structured AMR](/definitions/block-structured-amr.md) (tree-based variant distinguished).
* Updated [Constrained transport](/methods/constrained-transport.md) (production deployment on octree AMR).

# Citations

1. `~/papers/mosaic/div-free-amr/2006-A&A-Fromang-10105100046361_20065371.pdf` (doi:10.1051/0004-6361:20065371) — text extraction, pp. 371–384.
