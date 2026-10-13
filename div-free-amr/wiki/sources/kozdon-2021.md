---
type: Source
title: "Kozdon, Erickson & Wilcox (2021) — Hybridized summation-by-parts finite difference methods"
description: "Imports HDG hybridization into SBP-SAT elliptic solvers: independent trace variables on block faces, Schur elimination of volume unknowns, SPD global systems."
resource: "doi:10.1007/s10915-021-01448-5"
source_kind: paper
authors: [Kozdon J.E., Erickson B.A., Wilcox L.C.]
year: 2021
venue: "J. Sci. Comput. 87:85"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2021-JSC-Kozdon-101007s10915-021-01448-5.pdf"
tags: [sbp, sat, hybridization, elliptic, trace-variables, multi-block]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Imports hybridization/static condensation from the HDG literature into
[SBP-SAT](/methods/sbp-sat.md) for second-order linear elliptic PDEs:
**independent trace variables on block faces** carry all inter-block
coupling (the SATs depend only on traces), so each block's interior
solution is determined by its trace data alone. A Schur complement then
eliminates either set — eliminating volume unknowns leaves a drastically
smaller **symmetric positive definite** global system on the faces, with
per-block inverses embarrassingly independent. Stability proved; accuracy
confirmed numerically. Motivated by earthquake-cycle simulation, where
elliptic solves recur thousands of times.

# Key claims

1. **The interface becomes the unknown**: promoting traces to independent
   variables completes the architectural convergence of SBP-SAT with
   (hybridized) DG — SATs playing numerical fluxes, block faces playing
   element boundaries; the glue-space idea
   ([Kozdon & Wilcox (2015)](/sources/kozdon-wilcox-2015.md)) matured
   into a solver strategy.
2. **SPD by construction**: both local and global problems are symmetric
   positive definite — the energy structure of SBP survives condensation.
3. **Cost geometry**: the trade is block-inverse setup (independent,
   parallel) against a face-only global solve — favorable exactly when
   the same elliptic operator is solved repeatedly.

# Notation map

| Kozdon et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| trace variables on faces | interface DOFs (cf. glue space) | promoted to unknowns |
| local/global problems, Schur | static condensation | HDG import |

# Pages created or updated

* Updated [SBP-SAT technique](/methods/sbp-sat.md) (hybridized/trace-variable formulation).

# Citations

1. `~/papers/mosaic/div-free-amr/2021-JSC-Kozdon-101007s10915-021-01448-5.pdf` (doi:10.1007/s10915-021-01448-5) — text extraction, 28 pp.
