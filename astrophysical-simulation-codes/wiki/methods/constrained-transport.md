---
type: Method
title: "Constrained transport"
description: "Staggered discretization of the induction equation: face-area-averaged magnetic field updated from edge-centred EMFs, which keeps the discrete divergence of each cell at its initial value to round-off; production codes build the edge EMFs from the face Godunov fluxes (Gardiner–Stone upwind construction or Balsara–Spicer averaging) and, on AMR, add area-weighted restriction, divergence-free prolongation and an EMF correction at coarse–fine edges."
status: established
aliases: [CT, upwind constrained transport, staggered-mesh constrained transport, face-centred constrained transport, MHD-CT]
tags: [mhd, constrained-transport, amr, conservation]
timestamp: 2026-10-12T00:00:00Z
---

# Constrained transport

Constrained transport (CT) evolves $\mathbf B$ from the induction equation
$\partial_t\mathbf B + \nabla\times\boldsymbol{\mathcal E} = 0$, $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$,
on a staggered mesh. Four codes in this bundle use it:
[Athena](/software/athena.md), [Athena++](/software/athena-plus-plus.md),
[Enzo](/software/enzo.md) (its MHD-CT solver) and [GAMER](/software/gamer.md).
[PLUTO](/software/pluto.md) has CT on static grids but not in its AMR
version (below).

## Staggering and what is preserved

* $\rho$, $\rho\mathbf v$ and $E$ are cell-centred volume averages. Each
  component of $\mathbf B$ is an area average on the faces normal to it.
  The EMF components are time- and line-averaged on cell edges
  ([Stone et al. (2008)](/sources/stone-2008.md), §3, eqs. 16–24;
  [Zhang et al. (2018)](/sources/zhang-2018.md), §3.1, eqs. 10–15, Fig. 1;
  [Bryan et al. (2014)](/sources/bryan-2014.md), §4.3).
* The CT difference equations keep the cell-volume-averaged divergence of
  the face field exactly at zero. Equivalently, they conserve the magnetic
  flux through each cell (Stone et al. 2008, §3, eq. 25). Zhang et al.
  write it as $(\nabla\cdot\mathbf B)^{n+1}_{i,j,k} = (\nabla\cdot\mathbf B)^{n}_{i,j,k}$ (eq. 16).
  Bryan et al. state machine-precision preservation and add that
  monopoles from other sources, such as ill-posed initial conditions,
  persist (§4.3).
* The cell-centred field used by the Riemann solvers is the arithmetic
  mean of the two face values (Stone et al. 2008, eqs. 26–28; Bryan et
  al. 2014, §4.3). Enzo's update has four steps: Riemann problem with the
  cell-centred field, edge EMF from the fluxes, curl update of the face
  field, re-averaging to the cell centre (Bryan et al. 2014, §4.3).
* The staggered field makes the ghost zone one cell wider than for pure
  hydrodynamics in GAMER (Zhang et al. 2018, §3.1).
* Stated cost of the design: face-centred CT "complicates the
  implementation of the algorithm, and the interface to AMR drivers"
  (Stone et al. 2008, §3.2).

## Edge EMFs from face fluxes

The Godunov fluxes of the induction equation give EMFs at face centres;
CT needs them on edges.
* **Upwind-gradient construction (Gardiner & Stone 2005).**
  [Stone et al. (2008)](/sources/stone-2008.md) (§5.3, eqs. 79–81) set
  the edge EMF to the arithmetic mean of the four adjacent face-centred
  EMFs plus, in each transverse direction, $h/8$ times the difference of
  two EMF derivatives taken on either side of the edge. Each derivative
  is a one-sided difference to a cell-centre reference EMF computed from
  the cell-centred $\mathbf v$ and $\mathbf B$, e.g.
  $$\left(\partial_y\mathcal E_z\right)_{i,j-1/4} = \frac{2\left(\mathcal E_{z,i,j} - \mathcal E_{z,i,j-1/2}\right)}{h}\qquad\text{(eq. 81)},$$
  and is upwinded by the sign of the contact (mass-flux) velocity at the
  face, with the mean of both sides when that velocity is zero (eq. 80).
  The paper allows different cell sizes per direction. "Simple arithmetic
  averaging does not work for the unsplit integrators adopted here"
  (§5, citing Gardiner & Stone 2005).
* [Athena++](/software/athena-plus-plus.md) uses the upwind CT of
  Gardiner & Stone (2005, 2008) and does not restate the recipe
  ([Stone et al. (2020)](/sources/stone-2020.md), §3.1).
* [Enzo](/software/enzo.md)'s MHD-CT offers the first-order EMF method of
  Balsara & Spicer (1999) and the second-order methods of Gardiner &
  Stone (2005), without naming which Gardiner–Stone variant is used
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §4.3).
* [GAMER](/software/gamer.md) evaluates the edge EMF "from the electric
  field at the cell interface ... together with the magnetic field at the
  cell interface and the velocity at the cell center"; it names no
  variant and does not cite Gardiner & Stone
  ([Zhang et al. (2018)](/sources/zhang-2018.md), §3.2, CTU step 3).
* **Order.** Athena++'s default CT is second order, so the overall error
  stays $\mathcal O(h^2)$ even with PPM reconstruction; a fully
  fourth-order scheme is deferred to Felker & Stone (2018)
  (Stone et al. 2020, §3.2.1).

Inside an [unsplit integrator](/methods/unsplit-godunov-integrators.md)
the edge EMFs are built twice per step. In 2D CTU+CT the in-plane face
fields are first advanced by $\Delta t/2$ with CT for the corrector
states, then the corner EMFs are rebuilt from the second Riemann solve
(Stone et al. 2008, §5.1, steps 3–7, eqs. 74–75; Zhang et al. 2018,
§3.2).

## CT on adaptive meshes

Face- and edge-centred data need their own inter-level operators.
* **Restriction.** Face fields are area-weighted averages of the fine
  faces (Stone et al. 2020, §2.1.5, eq. 3; Zhang et al. 2018, §3.3). In
  Enzo's projection the averaging weight is $r_{\mathrm{ref}}^{-(d-1)}$
  for face-centred and $r_{\mathrm{ref}}^{-1}$ for edge-centred data
  (Bryan et al. 2014, §3.3, eq. 26).
* **Prolongation.** Athena++ uses the divergence-preserving prolongation
  of Tóth & Roe (2002), extended to nonuniform and curvilinear meshes "in
  finite-area fashion", and does not overwrite fine faces that already
  exist (Stone et al. 2020, §2.1.5). Enzo and GAMER use Balsara (2001).
  Enzo interpolates all three face components together and uses the old
  fine field where present (Bryan et al. 2014, §4.3). GAMER's 2D
  illustration interpolates the fine faces lying on coarse faces
  piecewise linearly with the coarse face average preserved, then fixes
  the interior faces with two quadratic polynomials whose 10 coefficients
  come from 7 independent face-matching equations and 3 from requiring
  zero divergence (Zhang et al. 2018, §3.3, Fig. 2, eq. 17).
* **EMF correction.** On an edge shared by coarse and fine blocks,
  Athena++ replaces the coarse EMF so that the coarse EMF times the coarse
  edge length equals the sum of the fine EMFs times their lengths; fine
  edges without a coarse counterpart are unused, and on shared edges the
  fine EMFs are averaged first (Stone et al. 2020, §2.1.4, eq. 1,
  Figs. 7–8). GAMER corrects the coarse face field with the EMF
  differences on coarse–fine "interedges" (Zhang et al. 2018, §3.3).
  Enzo projects the electric field, not $\mathbf B$, from fine to coarse
  and re-updates the parent field with it (Bryan et al. 2014, §4.3,
  citing Balsara & Spicer 1999 and Collins et al. 2010).
* **Shared edges without refinement.** Athena++ also replaces EMFs on
  edges shared by same-level `MeshBlock`s with their arithmetic mean:
  round-off, nondeterministic MPI ordering and non-ANSI optimizations
  otherwise create divergence errors "that CT never removes"
  (Stone et al. 2020, §2.1.4, §2.1.1). The polar boundary likewise
  averages EMFs on radial edges touching the pole (§2.3).
* **Avoiding CT under AMR.** PLUTO's AMR version uses
  [GLM cleaning](/methods/glm-divergence-cleaning.md) only. The stated
  reason is the care the staggered field needs in prolongation and
  restriction at fine–coarse interfaces
  ([Mignone et al. (2012)](/sources/mignone-2012.md), §1, §3, §7).
* In general relativity Athena++ keeps the same CT discretization with
  $\sqrt{-g}$-weighted lengths, areas and volumes (Stone et al. 2020, §4).

## Evidence

* **[Field-loop advection](/benchmarks/field-loop-advection.md).** Athena,
  2D, 256×128, PLM, Roe: the loop shape is "preserved extremely well";
  with uniform $v_z \ne 0$, $B_z$ stays zero to round-off. In 3D the
  axial component of an inclined loop stays zero to truncation error
  (Stone et al. 2008, §8.4, Fig. 21; §8.6, Fig. 34). Athena++ advects a
  loop through the pole of a spherical-polar grid with the structure
  "well preserved" (Stone et al. 2020, §3.5.2, Fig. 29).
* **[Linear waves](/benchmarks/linear-wave-convergence.md).** CT codes
  converge at second order in all MHD wave families, on oblique 3D grids
  (Stone et al. 2008, §8.6, Fig. 32; Zhang et al. 2018, §5.1(i), Fig. 4)
  and with AMR (Stone et al. 2020, §3.4.1, Fig. 19).
* **ABC field relaxation (GAMER, AMR).** Total energy is conserved to
  machine precision and magnetic helicity to better than 98 % over
  32 crossing times (Zhang et al. 2018, §5.1(v)).
* **[Orszag–Tang](/benchmarks/orszag-tang-vortex.md).** Enzo's CT and
  Dedner solvers give "approximately equal effective resolution"; the
  resolution is not printed (Bryan et al. 2014, §11.2.10, Fig. 14).
* **[MHD blast](/benchmarks/mhd-blast-wave.md).** Athena calls CTU+CT
  "robust for low-β flows" after isothermal runs at $\beta = 0.02$
  (Stone et al. 2008, §8.4, Figs. 28–30).

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §3, §5.1, §5.3, §8.4, §8.6.
2. [Stone et al. (2020)](/sources/stone-2020.md), §2.1.1, §2.1.4–2.1.5, §2.3, §3.1, §3.2.1, §3.4.1, §3.5.2, §4.
3. [Bryan et al. (2014)](/sources/bryan-2014.md), §3.3, §4.3, §11.2.10 (arXiv v1).
4. [Zhang et al. (2018)](/sources/zhang-2018.md), §3.1–3.3, §5.1 (arXiv v4).
5. [Mignone et al. (2012)](/sources/mignone-2012.md), §1, §3, §7.
