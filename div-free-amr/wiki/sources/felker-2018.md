---
type: Source
title: "Felker & Stone (2018) — A fourth-order accurate finite volume method for ideal MHD via upwind constrained transport"
description: "Fourth-order FV MHD on the McCorquodale-Colella base with UCT carried at the same order (PPM4 corner reconstruction, HLL four-state corner EMF); shows why the Athena E^c EMF caps at second order and that it is second-order UCT in limiting cases."
resource: "doi:10.1016/j.jcp.2018.08.025"
source_kind: paper
authors: [Felker K.G., Stone J.M.]
year: 2018
venue: "J. Comput. Phys. 375:1365-1400 (arXiv:1711.07439)"
local_file: "~/papers/mosaic/div-free-amr/2018-JCP-Felker-101016jjcp201808025.pdf"
tags: [constrained-transport, upwind-emf, high-order, finite-volume, athena, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The authors build a fourth-order, method-of-lines finite-volume MHD scheme,
RK4+PPM, and compare it throughout with Athena++'s second-order VL2+PLM.
* **Fluid part.** The base is the McCorquodale–Colella fourth-order FV
  method: transverse-Laplacian average↔point conversions, PPM4 with a
  smooth-extremum-preserving limiter, and point-value flux quadrature. It
  is integrated with SSP-RK4 (5 stages) or RK3.
* **Magnetic part.** The field is evolved by
  [upwind constrained transport](/methods/upwind-constrained-transport.md)
  carried at the same order. The face averages of $B_h$ stay the primary
  data, so the invariant $D_h^{\mathrm{f}} B_h = 0$
  ([notation](/notation.md)) holds by construction.
* **Scope.** Uniform Cartesian grids only. AMR, with fourth-order
  prolongation and restriction compatible with the mapped-grid formalism,
  is stated as future work.

The file read is the arXiv v2 preprint. Volume and pages were verified on
Crossref.

# Key claims

1. **Why $\mathcal{E}^c$ cannot be raised to fourth order** (§4).
   * Four steps of the GS05 corner-EMF scheme are second order:
     1. a second-order Taylor estimate of the corner EMF;
     2. midpoint face EMFs;
     3. the cell field as the mean of its faces;
     4. upwinded slopes that difference a 1D Riemann flux against a
        cell-centered reference $E$.
   * Steps 1–3 can be raised. Step 4 captures only a dimensionally split
     corner fan and caps the order at two. Appendix A argues this also
     makes it fail on planar waves along the grid diagonals.
   * A fourth-order CT therefore needs the UCT construction
     ([flux-CT](/methods/flux-ct.md)).
2. **$\mathcal{E}^c$ is second-order UCT in limiting cases** (Appendix A).
   With HLL face fluxes, the GS05 corner EMF agrees to second order with
   the HLL-UCT four-state formula in two cases:
   * a stationary domain;
   * supersonic grid-aligned flow, which additionally requires identical
     Riemann states of $B_2$.
   
   In general the two cannot match exactly.
3. **Fourth-order UCT** (§4.1–4.2).
   * Corner EMF states come from PPM4 transverse reconstruction of the face
     Riemann states of $v$ and $B$. The two independent velocity estimates
     are averaged, because limited 1D reconstructions need not commute.
   * The corner value is chosen by the HLL-UCT formula, with Einfeldt
     wavespeeds taken from the four adjacent face solves.
   * The cell-averaged $B$ the fluid needs is recovered from the face
     averages by an unlimited fourth-order "inverse reconstruction": a
     transverse Laplacian, then a longitudinal interpolation, then a
     Laplacian.
4. **Initialization at round-off** (§5.1). Face averages are set from
   analytic $A$ at corners. Naive differencing lost significance in double
   precision; reordering the operations fixed the convergence floor.
5. **Results** (§5).
   * Linear waves of all MHD families: fourth order, with nearly four
     orders of magnitude less error than VL2+PLM at $N_{x_1} = 128$.
   * Circularly polarized Alfvén waves, standing and traveling, in 2D and
     3D: fourth order.
   * 3D field loop with $v_z \ne 0$: $B_z$ stays below machine epsilon
     ([field loop](/benchmarks/field-loop-advection.md)).
   * Brio–Wu and RJ2a need characteristic reconstruction to avoid
     oscillations.
   * Orszag–Tang, blast and rotor at $500^2$ are robust.
6. **Record corrections.**
   * $\mathcal{E}^\circ$ has been misidentified as the final GS05 scheme in
     later literature (the authors name Balsara 2014).
   * Sign typos in the lower-corner rewrites of GS05 eq. 41: Athena 2008
     eq. 79 and Stone–Gardiner 2009 eq. 22.
   * The 3D linear-wave eigenvectors should be taken from GS05 Appendix A,
     not GS08.
   * Typos in the Colella–Sekora, Colella et al. 2011 and original PPM
     limiter formulas.

# Notation map

| Felker & Stone (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\langle B_1\rangle_{i\pm1/2,j}$ (face averages) | $B_h \in V_h^2$ | primary field data |
| $\langle E_3\rangle_{i-1/2,j-1/2}$ | $E_h \in V_h^1$ | corner (2D) or edge (3D) EMF |
| eqs. (28a)–(28b) | $\partial_t B_h = -C_h E_h$ | Stokes form; preserves $D_h^{\mathrm{f}} B_h$ |
| $E_z^\circ, E_z^\alpha, E_z^c$ | $\mathcal{E}^\circ, \mathcal{E}^\alpha, \mathcal{E}^c$ | GS05 names, kept |
| $Q^{R_1L_2}$ etc. | four corner states | LD2004's $Q^{NW}$ etc. renamed |
| $\langle\cdot\rangle$ vs. unbracketed | average vs. point value | |
| $\Delta^{\perp,d}$ | transverse Laplacian | no registry symbol |

# Pages created or updated

* Updated [Upwind constrained transport](/methods/upwind-constrained-transport.md): the fourth-order FV realization, and the relation to $\mathcal{E}^c$.
* Updated [Flux-CT and the Godunov CT variants](/methods/flux-ct.md): the second-order ceiling of $\mathcal{E}^c$.
* Updated [Field-loop advection](/benchmarks/field-loop-advection.md): the 3D fourth-order run.

# Citations

1. `~/papers/mosaic/div-free-amr/2018-JCP-Felker-101016jjcp201808025.pdf` (doi:10.1016/j.jcp.2018.08.025): text extraction, all pages including Appendix A and the reference list (64 entries).
