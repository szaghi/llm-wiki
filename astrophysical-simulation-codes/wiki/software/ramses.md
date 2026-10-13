---
type: Software
title: "RAMSES"
description: "Cell-by-cell AMR code for cosmological N-body and hydrodynamics on Khokhlov's fully threaded oct tree: a 3^d−1-neighbour grading rule with refinement-only criteria, ART-type particle-mesh gravity with an FFT coarse solve and one-way-interface SOR on finer levels, a second-order split or unsplit PLM Godunov scheme with an almost exact Riemann solver and refluxing, a single or level-halving adaptive time step without temporal interpolation, super-comoving coordinates, and verification on force accuracy, Sod, Sedov, a level-jump shock, the Zel'dovich pancake and secondary infall."
status: established
aliases: [RAMSES code, Ramses]
tags: [software, amr, cosmology, hydro, self-gravity, particles, riemann-solver, time-integration, verification]
timestamp: 2026-10-13T00:00:00Z
---

# RAMSES

RAMSES is an N-body and hydrodynamics code for cosmological structure
formation built on cell-by-cell ("tree-based") adaptive mesh refinement.
Its code paper, [Teyssier (2002)](/sources/teyssier-2002.md), describes
the first version and is the source of this page unless stated otherwise;
it was read as the arXiv preprint astro-ph/0111367v1, so section and
equation numbers are those of the preprint. The radiation extension is
[RAMSES-RT](/software/ramses-rt.md). See
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md) for the
comparison with the patch- and block-based codes.

## Code and version

* Fortran 90, optimized for the vector Fujitsu VPP 5000; a shared-memory
  OpenMP version; a distributed-memory domain-decomposition version
  "currently under construction". No scaling data (§5).
* $d$ = 1, 2 or 3 (§2.1). Boundary conditions: periodic, reflecting,
  inflow, outflow (§2.6).
* Planned in 2002: cooling, star formation, supernova feedback and zoom
  initial conditions (§5).

## Mesh

* **Fully threaded tree** (Khokhlov 1998; §2.1). The element is the oct of
  $2^d$ cells, so $N_{\mathrm b} = 2$ and $r_{\mathrm{ref}} = 2$; level
  $l = 0$ is a regular Cartesian coarse grid. The octs of a level form a
  doubly linked list; each oct points to its parent cell, to the $2d$
  neighbouring parent cells at $l-1$ and to its $2^d$ child octs: "17
  integers per oct for dim = 3, or equivalently 2.125 integers per cell".
* **Gather–scatter** (§2.1): per level, octs are gathered from the tree
  into arrays, updated "very efficiently on vector or parallel
  architectures", and scattered back.
* **Grading rule** (§2.1.1): "any oct in the tree structure has to be
  surrounded by $3^{\mathrm{dim}}-1$ neighboring parent cells", a smooth
  transition "even in the diagonal directions". The refinement map is built
  from $l_{\max}$ down: parents of marked or refined children, then their
  $3^d - 1$ neighbours, then the user criteria; a cubic buffer is expanded
  $n_{\mathrm{expand}}$ times around marked cells ("usually ... only once",
  against twice in ART).
* **Refinement only** (§2.1.1): no derefinement criteria are needed, an
  "important difference" from ART and Khokhlov's code.
* **Tree modification** (§2.1.2): incremental, never rebuilt; one pass
  from $l = 0$ up creates children of marked leaves and destroys children
  of unmarked split cells; not vectorizable but touching few octs per step.
* **Ghost zones** (§2.3.1): $n_{\mathrm g} = 2$ per side and direction,
  diagonals included, so $3^d - 1$ neighbouring octs and $6^d$ cells per
  oct stencil. PPM, needing 4 ghost zones, was rejected as "to expensive"
  [sic] for octs; the oct-wise stencil costs about 50 %, 100 % and 200 %
  extra CPU in 1, 2 and 3D on a full Cartesian grid (estimate).

## Time stepping

* Two schemes (§§2.1, 2.3.2): one $\Delta t$ for all levels, or an
  adaptive scheme "similar to a 'W cycle'" in which level $l+1$ takes two
  steps per level-$l$ step and $\Delta t_l$ is reset to the sum of the two
  fine steps, which need not be equal.
* **No temporal interpolation** (§2.3.2): "The coarse solution is assumed
  to remain constant in time during the advance of the fine solution";
  with the adaptive step the coarse–fine boundaries drop "from second to
  first order in time, but the global solution remains second order".
* The single step is "more accurate (but time consuming)" for particles,
  which are first order along trajectories crossing level boundaries under
  the adaptive step (§2.2.5); it was "the fastest solution" for the 3D
  Sedov test (§3.6); the cosmological runs use the adaptive step (§4.2).
* **Limits** (§2.4, eqs. 14–17): the minimum of a fraction of the
  smallest $t_{\mathrm{ff}}$, a fraction of $h_l$ over the largest particle
  speed, about 10 % of $a/\dot a$ (early times), and
  $\nu\,h_l/\max(\vert v_x\vert + c_s, \vert v_y\vert + c_s, \vert v_z\vert + c_s)$
  with $\nu < 1$.

## Hydrodynamics

* Euler equations in conservative form with gravity sources; total fluid
  energy conserved exactly without gravity (§2.3).
* **Scheme** (§§2.3, 2.3.1): second-order piecewise linear Godunov with
  MinMod slopes and characteristic tracing (states corrected for gravity),
  "with or without directional splitting (according to the user's
  choice)", after Colella (1990) and Saltzman (1994); transverse terms in
  the unsplit option. Gravity is a time-centred fractional step (eq. 13).
* **Riemann solver** (§2.3.1): "almost exact", with the contact pressure
  by Newton–Raphson ("typically, for strong shocks 10 Newton-Raphson
  iterations are required for single-precision accuracy of $10^{-7}$") and
  a linear profile inside rarefactions as the only approximation. See
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* **AMR step** (§2.3.2): new fine cells and ghost data by conservative
  interpolation with "a 3D generalization of the Min-Mod limiter (De Zeeuw
  1993)"; coarse–fine fluxes replaced by averages of the fine fluxes
  (refluxing); split cells set to the average of their updated children
  (restriction).

## Gravity and particles

* **Particle-mesh N-body** after ART (§2.2): per-oct particle lists;
  cloud-in-cell deposit per level, including particles from neighbouring
  parent cells, so the level density equals that of a uniform mesh of the
  same resolution; a kick–drift–kick midpoint integrator that reduces to
  leapfrog for constant steps (eqs. 5–7). See
  [particle-mesh gravity](/methods/particle-mesh-gravity.md).
* **Poisson solver** (§2.2.3, eqs. 2–4): FFT on the coarse level with the
  Green function of the $(2d+1)$-point Laplacian; on finer levels the
  "one-way interface" of Jessop et al. and Kravtsov et al., red–black
  Gauss–Seidel with $\omega_{\mathrm{SOR}} \simeq 2/(1+\pi/N)$ (Dirichlet)
  or $2/(1+2\pi/N)$ (periodic), $N$ the mean patch size on AMR levels,
  Dirichlet data linearly reconstructed from level $l-1$, stopped when the
  residual drops by $10^3$. "the coarse grid solution never 'sees' the
  effect of the fine grids ... it can not be better in any way"; a two-way
  scheme is "left for future work". See
  [Poisson solvers on adaptive meshes](/methods/multigrid-self-gravity.md).
* **Forces** (§2.2.4): symmetric 5-point gradient of $\Phi$, interpolated to
  particles by inverse cloud-in-cell, from level $l-1$ for particles whose
  cloud leaves the level.
* **Total energy** with gravity conserved "at the percent level" (§4.3).

## Cosmology and refinement criteria

* **Super-comoving coordinates** (§2.6, eqs. 22–25) after Martel &
  Shapiro (1998): for $\gamma = 5/3$ the equations keep the non-expanding
  form except the Poisson equation; otherwise one extra energy source term.
* **Criteria** (§2.5, eqs. 18–21): quasi-Lagrangian density thresholds (a
  mass per cell over $h_l^d$; 5–10 particles per cell for pure N-body,
  40–80 for gas runs), a gradient criterion, a second-derivative variant
  and spatial spheres per level. The AMR overhead "can be as large as a
  factor of 2 to 3", so at most "30 % to 50 %" of the grid can usefully be
  refined (estimate).
* **Shocks need not be refined** (§§3.5, 3.7, 4.2): shocks moving from fine
  to coarse regions show no detectable mesh artefact in the tests, so
  cosmological runs refine on density only. See the batch-10 section of the
  [AMR page](/methods/adaptive-mesh-refinement.md) for the scope of this
  claim against FLASH's oblique-incidence case.

## Verification

From [Teyssier (2002)](/sources/teyssier-2002.md), §§3–4; no convergence
order or error norm is reported for the hydrodynamic tests.
* Point-mass and ΛCDM forces against Ewald-corrected and uniform PM
  references: errors "at the percent level", the level-boundary conditions
  being "the main source of inaccuracy in the N-body scheme" (§§3.1–3.2).
* [Sod shock tube](/benchmarks/sod-shock-tube.md), 6 levels on 64 coarse
  cells, 14 % of the uniform cell count (§3.3); planar and spherical
  [Sedov blasts](/benchmarks/sedov-taylor-blast-wave.md) (§§3.4, 3.6);
  a Mach 5000 shock through a level jump, about 5 % oscillations
  coarse-to-fine and none fine-to-coarse (§3.5); the
  [Zel'dovich pancake](/benchmarks/zeldovich-pancake.md) with and without
  shock refinement (§3.7); Bertschinger's self-similar infall, correct
  "down to a radius of 2 fine cells, the actual resolution limit of the
  code" (§3.8).
* A $256^3$-particle ΛCDM run reaching formal $8192^3$ ($12.21\,h^{-1}$
  kpc), with Layzer–Irvine energy errors of at most 0.5 % (§4).

## Later descriptions in other sources

* [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §§5–5.2, describe
  the 2013 code as starting from one root oct refined uniformly to a
  minimum level (counted from 1), with 2:1 grading, two substeps on level
  $l+1$ per step on $l$, and MPI parallelism; the 2002 paper's
  $3^d - 1$-neighbour rule is stronger than face-wise 2:1 grading. See
  [RAMSES-RT](/software/ramses-rt.md).
* [Stone et al. (2020)](/sources/stone-2020.md), §2.2, and
  [Bryan et al. (2014)](/sources/bryan-2014.md), §1, class RAMSES with ART
  as cell-based AMR; [Tomida & Stone (2023)](/sources/tomida-2023.md),
  §3.3.1, class its Poisson solve as level-by-level, "not
  self-consistent", which the 2002 paper itself concedes.
* [Villasenor et al. (2021)](/sources/villasenor-2021.md), §§3.2–3.3,
  compare Cholla with Ramses on dark-matter and adiabatic-gas power
  spectra; the Ramses version used is not stated.

## Later uses (batch 10)

**Read by yt** ([Turk et al. (2011)](/sources/turk-2011-c.md), §4.1). In 2011 yt read RAMSES natively. Because "RAMSES is based on an octree data structure", yt coalesces its cells into patches with Enzo's subgrid-clustering mechanism, with an efficiency factor "typically set to be 0.2".

# Citations

1. [Teyssier (2002)](/sources/teyssier-2002.md), §§1–5, eqs. 1–27, Tables 1–2 (arXiv v1).
2. [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §§5–5.2 (arXiv v2).
3. [Stone et al. (2020)](/sources/stone-2020.md), §2.2.
4. [Bryan et al. (2014)](/sources/bryan-2014.md), §1 (arXiv v1).
5. [Tomida & Stone (2023)](/sources/tomida-2023.md), §3.3.1 (arXiv v1).
6. [Villasenor et al. (2021)](/sources/villasenor-2021.md), §§3.2–3.3 (arXiv v2).
7. [Turk et al. (2011)](/sources/turk-2011-c.md), §4.1.
