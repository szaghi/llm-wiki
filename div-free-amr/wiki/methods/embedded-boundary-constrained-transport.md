---
type: Method
title: "Embedded-boundary constrained transport"
description: "Staggered CT on a Cartesian mesh cut by a non-conforming boundary or material interface: edge EMFs on every edge, ghost data entering only through them, so the divergence is exact in the active domain while flux is not conserved at the boundary."
status: established
aliases: [cut-cell CT, CT embedded boundary]
tags: [constrained-transport, embedded-boundary, cut-cell, ghost-fluid, resistive-mhd, divergence-constraint]
timestamp: 2026-10-08T00:00:00Z
---

# Embedded-boundary constrained transport

The method runs [constrained transport](/methods/constrained-transport.md)
on a uniform Cartesian mesh cut by a boundary that does not conform to it.
The boundary is a static or moving wall, or a two-sided material interface.
It is due to [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md), who
build it on the Stone–Gardiner unsplit Godunov CT scheme for resistive MHD,
in 2D.

## Construction

1. **No small-cell problem.** Hydrodynamic fluxes use the Forrer–Jeltsch
   cut-cell method. Fluxes are always computed on the full Cartesian faces,
   and cut cells are integrated as full cells. The time step is therefore
   not limited by small cut fragments. The price is a local conservation
   error in the boundary cells.
2. **Ghost data by reflection.** Each ghost cell or ghost face is reflected
   in the boundary into a virtual point. The state there is bilinearly
   interpolated, dropping to first order if the stencil touches an empty
   cell. A Dirichlet or Neumann condition then fixes the ghost value. Face
   components of $B_h$ are interpolated from same-orientation faces.
3. **A perfect-conductor wall.** The wall imposes $v = v_b$, zero
   tangential field and a given normal field. The tangential condition is
   curvature-corrected so that a current-free $1/R$ field is reproduced
   discretely. Plain linear extrapolation would create a spurious current
   there.
4. **The same CT update everywhere.** $E_h$ is computed identically on
   active, cut and ghost edges, with upwind dissipation and the Ohmic term
   $\eta J$. Faces bounding active or cut cells are updated by
   $\partial_t B_h = -C_h E_h$.
5. **Two materials, one field.** Each material has its own mesh and ghost
   fluid. There is a single global $B_h$ on a master mesh, and each
   material's edge EMF is combined into one $E_h$ per edge, weighted by edge
   occupation fraction.

## Divergence and flux

* **The invariant holds in the active domain.** Ghost fields are
  extrapolated, so they are not solenoidal in the ghost cells. They enter
  the active faces only through $E_h$, and every active-face increment is a
  curl. $D_h^{\mathrm{f}}B_h = 0$ is therefore preserved there
  ([exact discrete divergence](/properties/exact-discrete-divergence.md)).
  The authors measure $\nabla\cdot B \approx 10^{-18}$ (G/cm) on $128^2$
  for a two-material problem with a non-mesh-aligned interface.
* **Flux is not conserved at the boundary.** Field lines can be advected
  through the evolved faces of cut cells into a perfect conductor. Each line
  that enters re-emerges elsewhere, so no monopole forms. The wall behaves
  like one with a finite numerical resistivity set by the boundary scheme's
  truncation error.
* **Two fields would create monopoles.** Evolving separate fields on each
  side of an interface needs a normal–tangential split. That split is
  accurate only to truncation error and leaves divergence well above
  roundoff. One field with averaged edge EMFs avoids this. The cost is
  numerical diffusion of $B$ across the interface. The authors found that
  separate per-material EMFs, averaged, gave better results than one EMF
  built from averaged velocity and resistivity.
* **Variant noted, not developed.** The authors report a cut-cell CT update
  that is divergence-free inside each phase but does not conserve flux at
  the interface. It reduces the diffusion, at the cost of a mismatch across
  the interface. A cut-cell method that achieves both is stated as open.

*Compiler reading:* the mechanism is the one behind the
[electric-field correction](/methods/electric-field-correction.md). Data from
the other side of a seam, here the ghost region or the other material, enters
the constrained field only through one single-valued $E_h$ per edge. Since
$D_h^{\mathrm{f}} C_h = 0$ holds for any $E_h$, the quality of the boundary
condition controls accuracy and flux conservation, not the divergence. The
fraction-weighted EMF average plays the role of the fine-to-coarse EMF sum
at an AMR seam.

## Accuracy and limits

* Second-order convergence on smooth tests: acoustic and magnetosonic
  standing waves in a cylinder, resistive field soak into slabs and
  cylinders. With a jump in resistivity it is first order, as expected.
* Moving walls compress $\theta$- and parallel pinches. The mass and
  $B_z$-flux conservation errors are nearly equal, since both are solved
  in very similar ways in 2D. The in-plane flux has its own boundary
  conservation error.
* 2D only. The authors expect 3D to be straightforward.
* The limits they report are inherited from the base scheme. One is
  excessive diffusion in sub-Alfvénic interface motion. The other is loss of
  thermal-pressure positivity in strongly shocked low-$\beta$ flows
  ([positivity–divergence coupling](/results/positivity-divergence-coupling.md)).

# Citations

1. [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md), §§3–4, 6, 7.4, 7.9, 8.
