---
type: Source
title: "Jones, McNally & Reynolds (2026) — A constrained-transport embedded boundary method for compressible resistive MHD"
description: "2D cut-cell CT for resistive MHD on Cartesian meshes with static, moving and two-material embedded boundaries: ghost data enters only through edge EMFs, so the divergence stays exact in the active domain while boundary flux is not conserved."
resource: "doi:10.1016/j.jcp.2025.114641"
source_kind: paper
authors: [Jones S.W., McNally C.P., Reynolds M.]
year: 2026
venue: "J. Comput. Phys. 550:114641 (arXiv:2601.04099)"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2026-JCP-Jones-101016jjcp2025114641.pdf"
tags: [constrained-transport, embedded-boundary, cut-cell, ghost-fluid, level-set, resistive-mhd, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper puts an arbitrarily shaped embedded boundary into a
finite-volume, staggered-mesh CT solver for compressible resistive MHD on a
2D Cartesian mesh. The motivation is pulsed-power and magneto-inertial
fusion devices. The base scheme is that of Stone & Gardiner (2009), with
HLL or HLLD fluxes, modified van Leer slopes and SSPRK(2,2).

The cut-cell treatment of Forrer & Jeltsch (1998) avoids the small-cell
time-step problem. It is extended to:
* moving one-sided walls, tracked by a polyline;
* two-sided material interfaces, through a ghost-fluid method and a level
  set.

Compiled as
[embedded-boundary constrained transport](/methods/embedded-boundary-constrained-transport.md).

The file read is the arXiv v1 preprint, which prints the JCP DOI on page 1.
Volume 550 and article number 114641 (April 2026) were verified on Crossref.

# Key claims

1. **Cut cells** (§3). Fluxes are always computed on full Cartesian faces,
   and cut cells are integrated over their full volume. This avoids the
   small-cell time step but gives a local conservation error. Ghost-cell
   states come from reflection in the boundary and bilinear interpolation
   (eqs. 24–33). That interpolation is limited to first order next to empty
   cells, and Dirichlet or Neumann conditions are imposed through
   eqs. 34–36.
2. **The MHD wall** (§4.1). A perfect conductor is imposed through
   Dirichlet conditions on $v$, $B\cdot t = 0$ and $B\cdot n = B_n$. The
   tangential condition is curvature-corrected (eq. 42) to preserve
   current-free $1/R$ fields.
   * The extrapolated ghost $B$ is not solenoidal.
   * No error reaches the active domain, because active faces are updated
     only by the discrete curl of $E$.
   * $J$ is computed on ghost edges too, so that the Ohmic EMF has a curl
     there (eqs. 18–20, 44–49).
3. **Flux at the wall** (§1, §7.4). Magnetic flux is not conserved at the
   embedded boundary, but no monopoles are introduced. Field lines can cross
   into the conductor through evolved cut faces, and every line that enters
   re-emerges. The boundary acts as one with finite numerical resistivity.
4. **Two materials** (§4.2, §6.2). One global $B$ lives on a master mesh,
   and per-material edge EMFs are combined with edge-occupation-fraction
   weights.
   * Separate per-side fields would need a normal–tangential split that is
     accurate only to truncation error, which introduces monopoles.
   * The cost of the single field is numerical diffusion of $B$ across the
     interface.
   * Averaging the per-material EMFs worked better than one EMF from
     averaged velocity and resistivity.
5. **Verification** (§7).
   * Second-order convergence: the cylindrical acoustic wave, the
     $\theta$-pinch and parallel-pinch magnetosonic waves, and resistive
     soak into a slab and into cylinders (axial and azimuthal).
   * First order across a resistivity jump: the two-material slab.
   * Between first and second order on a curved two-material interface.
     There $\nabla\cdot B$ stays at machine precision (about $10^{-18}$ G/cm
     on $128^2$, Fig. 10d).
   * Qualitative tests: field-line drag around conducting bodies, moving-wall
     $\theta$- and parallel-pinch compressions, shock-driven pinch
     compression, a shocked bubble, and a magnetically driven z-pinch.
   * The magnetized runs suppress Richtmyer–Meshkov growth and bubble
     deformation.
6. **Limits** (§8).
   * The method is 2D.
   * The Forrer–Jeltsch cut cells are not conservative.
   * The method diffuses $B$ across material interfaces.
   * There is a curvature bound from the reflection stencil.
   * The base scheme is diffusive in sub-Alfvénic motion and loses
     positivity in strongly shocked low-$\beta$ flows.
   * The authors also tried a cut-cell CT update that is divergence-free in
     each phase but does not conserve interface flux. A method that does
     both is left open.
7. **An erratum on the base scheme** (footnote 2). Eq. (22) of
   Stone & Gardiner (2009) has a typo: its second and third (dissipation)
   terms should carry a negative sign.

# Notation map

| Jones et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B_{x,i-1/2,j}$, $B_{y,i,j-1/2}$ (face averages) | $B_h \in V_h^2$ | $B_z$ is cell-averaged in 2D |
| $E_{z,i-1/2,j-1/2}$ etc. (edge averages) | $E_h \in V_h^1$ | includes Ohmic $\eta J$ |
| eqs. 15–17 | $\partial_t B_h = -C_h E_h$ | |
| $\nabla\cdot(\nabla\times E)=0$ | $D_h^{\mathrm{f}} C_h = 0$ | |
| $J$ on edges (eqs. 18–20) | discrete curl of $B_h$, on $V_h^1$ | no registry symbol |
| $\phi$ | level-set function | not the registry $\psi_h$ |
| $M_0$, $M_\ell$ | master and per-material meshes | |

# Pages created or updated

* Created [Embedded-boundary constrained transport](/methods/embedded-boundary-constrained-transport.md).
* Updated [Constrained transport](/methods/constrained-transport.md): embedded boundaries, with ghost data entering through edge EMFs only.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): non-solenoidal ghost data does not break the invariant, and one field per interface is required.
* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): the base-scheme positivity limit reported for low-$\beta$ shocks.

# Citations

1. `~/papers/mosaic/div-free-amr/2026-JCP-Jones-101016jjcp2025114641.pdf` (doi:10.1016/j.jcp.2025.114641): text extraction, all pages including the reference list (47 entries). Figures were read from their captions and axis text only.
