---
type: Source
title: "Stone, Gardiner, Teuben, Hawley & Simon (2008) — Athena: a new code for astrophysical MHD"
description: "Code paper for Athena: second-order unsplit Godunov MHD (CTU+CT and VL+CT) with face-centred fields and the Gardiner-Stone edge-EMF construction, a full 1D-3D test suite, and the field-loop checks that separate round-off from truncation-level preservation."
resource: "doi:10.1086/588755"
source_kind: paper
authors: [Stone J.M., Gardiner T.A., Teuben P., Hawley J.F., Simon J.B.]
year: 2008
venue: "Astrophys. J. Suppl. 178:137-177"
local_file: "~/papers/mosaic/div-free-amr/2008-ApJS-Stone-101086588755.pdf"
tags: [constrained-transport, production-code, godunov, unsplit, riemann-solver, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

This is the reference description of Athena. It is a second-order,
directionally unsplit Godunov code for ideal MHD:
* volume-averaged cell variables and area-averaged face fields;
* CT through the Gardiner–Stone construction of edge EMFs from the
  Godunov fluxes;
* CTU+CT (the default, less diffusive) and the simpler VL+CT
  predictor–corrector;
* PLM or PPM reconstruction in characteristic variables;
* HLLE, HLLC, HLLD and Roe solvers.

The mathematics of the integrators is in
[Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md) and
[Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md). This paper is
about implementation, parallel layout and the test suite. Extending
Athena to SMR and AMR is the stated motivation, and that extension is left
to future work. It is merged into
[constrained transport](/methods/constrained-transport.md),
[field-loop advection](/benchmarks/field-loop-advection.md) and
[positivity–divergence coupling](/results/positivity-divergence-coupling.md).

This paper is in tier C of the ingestion list (context: codes). The user
asked for it to be added.

# Key claims

1. **Why face-centred fields** (§3). The area-averaged discretization
   conserves the magnetic flux through each cell, equivalently the
   cell-integrated monopole density. Of the many discrete divergences this
   is argued to be the one consistent with a finite-volume scheme. The
   price is complexity, especially at AMR interfaces.
2. **No dimensional splitting for conservative MHD** (§5). All field
   components must evolve together for the constraint to hold, and the
   split alternative needs non-conservative $\nabla\cdot B$ terms (Powell).
3. **Divergence is invisible in 1D** (§4). In 1D the normal field is
   constant and CT is not needed, so any rigorous MHD test suite must be
   multidimensional.
4. **The EMF construction** (§5.3). The edge EMFs come from the Godunov
   face fluxes plus cell-centred reference fields, upwinded by the contact
   mode, so the scheme reduces exactly to its 1D form for grid-aligned
   flow.
5. **Riemann solvers** (§4.3). The HLLE intermediate state is positive, so
   it gives positive first-order 1D schemes and serves as a fallback when
   Roe fails. In multiple dimensions at higher order, positivity "depends
   on the details of the multidimensional integrator". HLLD is about as
   accurate as Roe and much faster.
6. **Tests** (§8). The suite covers linear-wave convergence, shock tubes, a
   blast wave in a strongly magnetized medium, Orszag–Tang, the rotor, and
   magnetic Rayleigh–Taylor with AMR. Field loops:
   * a 2D loop keeps its shape;
   * a 3D loop with its axis along a grid direction keeps $B_z = 0$ to
     round-off;
   * an inclined 3D loop keeps the axial component zero only to truncation
     error.
7. **Parallel scaling** (§7). Weak scaling is nearly perfect beyond $10^4$
   processors.

# Notation map

| Stone et al. (2008) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B_{x,i-1/2,j,k}$ etc. (face averages) | $B_h \in V_h^2$ | |
| $\mathcal E_{z,i-1/2,j-1/2}$ etc. (line-averaged EMFs) | $E_h \in V_h^1$ | |
| eqs. 16–18 | $\partial_t B_h = -C_h E_h$ | |
| cell-volume average of the divergence (eq. 25) | $D_h^{\mathrm{f}} B_h$ | |
| CTU+CT, VL+CT | unsplit integrators | |

# Pages created or updated

* Updated [Constrained transport](/methods/constrained-transport.md): the Athena code paper's cautions on 1D tests and the face-centred discretization.
* Updated [Field-loop advection](/benchmarks/field-loop-advection.md): round-off versus truncation-level preservation for aligned and inclined loops.
* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): the HLL-family statement, added to the scoped reading of the open `Contradictions` entry.

# Citations

1. `~/papers/mosaic/div-free-amr/2008-ApJS-Stone-101086588755.pdf` (doi:10.1086/588755): text extraction. The algorithm sections and the divergence-relevant tests (§§3–6, 8.4) were read in full. Most of the solver and reconstruction steps, the eigensystems of Appendices A–B and the 1D hydrodynamic tests were read in outline, because they repeat material of GS05 and GS08. The reference list (81 entries) was extracted from the two-column layout and checked line by line.
