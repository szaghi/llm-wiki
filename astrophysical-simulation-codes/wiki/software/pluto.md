---
type: Software
title: "PLUTO (multiphysics code for astrophysical gas dynamics, with Chombo AMR)"
description: "Godunov-type code for Newtonian and relativistic MHD whose adaptive version couples a cell-centred, dimensionally unsplit second-order CTU scheme with GLM divergence cleaning to the Chombo patch-based AMR library, with subcycling, refluxing, unsplit parabolic terms and a leaf-cell time step for stiff local sources."
status: established
aliases: [PLUTO, PLUTO-CHOMBO, PLUTO-AMR]
tags: [software, mhd, hydro, amr, divergence-cleaning, unsplit, riemann-solver, time-integration, performance, verification]
timestamp: 2026-10-12T00:00:00Z
---

# PLUTO

PLUTO is a code for astrophysical fluid dynamics whose static-grid version is
described in Mignone et al. (2007, "Paper I"). Its adaptive version couples
PLUTO's single-patch integrators to the Chombo AMR library ("PLUTO-CHOMBO")
([Mignone et al. (2012)](/sources/mignone-2012.md), §1, §4).

## Code

* Static and AMR versions are distributed as one package at
  `http://plutocode.ph.unito.it`; Chombo comes from
  `https://seesar.lbl.gov/anag/chombo/` (§7). Chombo is "written in a
  combination of C++ and Fortran77 with MPI" and developed by the ANAG group
  at LBNL (§4).
* PLUTO's version number, implementation language and licence are not
  printed.

## Equations

Newtonian single-fluid MHD with dissipative terms (§2, eq. 1), with
$P^* = p + \tfrac12|\mathbf B|^2$ (no $4\pi$):

$$\begin{aligned}
&\partial_t\rho + \nabla\cdot(\rho\mathbf v) = 0,\\
&\partial_t(\rho\mathbf v) + \nabla\cdot(\rho\mathbf v\mathbf v - \mathbf B\mathbf B) + \nabla P^* = (\text{viscous stress divergence}) + \rho\mathbf g,\\
&\partial_t E + \nabla\cdot\left[(E+P^*)\mathbf v - (\mathbf v\cdot\mathbf B)\mathbf B\right] = (\text{parabolic energy flux divergence}) - (\text{cooling}) + \rho\mathbf v\cdot\mathbf g,\\
&\partial_t\mathbf B - \nabla\times(\mathbf v\times\mathbf B) = -\nabla\times(\text{resistivity}\cdot\mathbf J).
\end{aligned}$$

* Ideal EOS $E = \frac{p}{\gamma-1} + \frac12\rho|\mathbf v|^2 + \frac12|\mathbf B|^2$
  (eq. 2), or barotropic and isothermal alternatives; passive scalars and ion
  fractions (eq. 3).
* Dissipative terms (§2.1.1): viscosity, a diagonal resistivity tensor, and
  saturated anisotropic thermal conduction that blends a classical
  field-aligned flux with a saturated flux (eqs. 6–7; App. A: central
  differences in the diffusive limit, upwinding in the saturated limit).
* Relativistic MHD (§2.2, eqs. 8–11, $c=1$) with an ideal or Taub–Mathews
  equation of state; relativistic dissipative terms are not treated.
* General form (§2.3, eq. 12): hyperbolic fluxes, parabolic fluxes, and
  point-local sources $s(u)$ (gravity, cooling, chemistry, GLM damping).

## Divergence control

PLUTO offers Powell's eight-wave method, face-centred constrained transport
(Paper I) and GLM cleaning, but **the AMR version uses GLM only**
([Mignone et al. (2012)](/sources/mignone-2012.md), §3, eq. 14; see
[GLM divergence cleaning](/methods/glm-divergence-cleaning.md)):

$$\partial_t\mathbf B - \nabla\times(\mathbf v\times\mathbf B) + \nabla\psi = 0,\qquad \partial_t\psi + c_h^2\nabla\cdot\mathbf B = -\frac{c_h^2}{c_p^2}\psi,$$

with the damping source operator-split (§3.1). The stated rationale is to
avoid the cost of elliptic cleaning and the care that staggered fields need in
prolongation and restriction at fine–coarse interfaces (§1, §7; contrast
[constrained transport](/methods/constrained-transport.md)). In the
relativistic rotor, divergence errors are "transported out of the domain at
the speed of light", i.e. $c_h=1$ there (§6.3). How $c_h$ and $c_p$ are set
for Newtonian runs is not stated in this paper (deferred to Mignone &
Tzeferacos 2010).

## Integrator and reconstruction

See [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
* **CTU** (Colella 1990) as in Mignone & Tzeferacos (2010): cell-centred,
  dimensionally unsplit, second order; Riemann problems are solved between
  corner-coupled time-centred states, with **six Riemann solves per zone per
  step** in 3D (§3.1, eqs. 15–18).
* **Unsplit parabolic terms** (a novelty, §3.1, eqs. 19–21): the corner states
  include the parabolic increments, with transverse hyperbolic fluxes from
  first-order Godunov fluxes between cell-centred states and parabolic fluxes
  by second-order central differences. Cooling, chemistry and GLM damping are
  operator-split.
* **Time step** (eq. 23): the Courant number combines the maximum signal speed
  over $h$ and twice the maximum diffusion coefficient over $h^2$; stability
  requires $\nu\le1$ in 2D and $\nu\le1/2$ in 3D. A source-limited step
  (eq. 24) caps the relative change of pressure and species per step.
* **Characteristic normal predictors** (§3.2): primitive variables projected
  on left eigenvectors and extrapolated to $t^n+\Delta t/2$ with an upwind
  limiter; two reference-state choices are given, and the paper notes both may
  reduce formal second order in smooth flow. Reconstructions: PPM (eqs. 33–37,
  "fourth-order" interface values), the third-order improved WENO of Yamaleev
  & Carpenter (2009), and linear TVD with MC, harmonic (van Leer), van Albada
  or MinMod limiters.
* **Primitive predictor** (§3.3, eqs. 43–44): a characteristic-free
  MUSCL–Hancock half step that needs no eigen-decomposition; the default for
  the relativistic tests.
* **Riemann solvers** (§3.1): Rusanov (LLF), HLL, HLLC and HLLD for MHD and
  relativistic MHD; Roe for hydro and MHD only. See
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* **Shock-adaptive hybrid** (App. B, eq. B1): zones flagged by a large
  pressure jump together with compression switch to HLL, and their stencil
  neighbours to MinMod reconstruction; stated to preserve second order, off in
  the tests unless stated.

## Adaptive mesh refinement

From [Mignone et al. (2012)](/sources/mignone-2012.md), §4; see
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* **Structure**: Chombo block-structured (patch-based) AMR, levels $l=0$ to
  $l_{\max}$, Berger–Rigoutsos clustering, integer refinement ratio
  $r_{\mathrm{ref}}$ per level (2 and 4 used, mixed, e.g. 2:4:4). Patches are
  disjoint and **properly nested**: a level-$(l+1)$ cell is separated from
  level $l-1$ by at least one row of level-$l$ cells.
* **Subcycling** in time, $\Delta t_l = \Delta t_{l-1}/r_{\mathrm{ref}}$, with
  optional extra substeps and a recursive level advance (Fig. 4).
* **Ghost cells** from physical boundaries, same-level exchange or coarse
  interpolation, with linear time interpolation of coarse data (eq. 46).
* **Prolongation**: conservative piecewise-linear in volume coordinates with
  MC-limited central slopes (eq. 45). **Restriction**: volume-weighted average
  (eq. 47). **Refluxing**: the coarse flux is replaced by the space–time
  average of the fine fluxes (eqs. 48–49).
* **Coordinates** in PLUTO-CHOMBO: Cartesian and cylindrical (r, z) only
  (Table 1).
* **Refinement criterion** (§4.1, eqs. 50–51): Löhner's (1987) normalized
  second-derivative error norm, default filter 0.01; a cell is tagged above a
  threshold.
* **Leaf-cell source time step** (§4.2, eqs. 52–53, a novelty): standard
  practice forces every level to the root step divided by $2^l$, which makes
  fine levels take steps $2^l$ times smaller than a mesh-independent source
  time scale needs. PLUTO evaluates the source-limited step on leaf cells only,
  because covered cells are overwritten by restriction; the expected speed-up
  is about $2^l$, valid provided projection (restriction) precedes regridding.

## Parallelization

* MPI only; each level is parallelized independently by distributing boxes;
  there is no intra-box parallelism; the load is the number of grid points per
  box, balanced by Chombo's Kernighan–Lin knapsack solver (§4.3).
* Empirical rule: parallel performance deteriorates when the number of blocks
  per level approaches the number of processors, or when the ideal workload
  per processor approaches the maximum box size; smaller maximum boxes and
  fewer levels with larger ratios help (§4.3).
* Strong scaling: resistive reconnection, efficiency above 0.8 below 256
  processors (§5.3, Fig. 14); 3D magnetic Rayleigh–Taylor, above 0.8 up to 512
  processors, about 0.61 (2 levels) versus 0.44 (4 levels) at 1024 cores
  (§5.5, Fig. 18); relativistic rotor, above 0.7 below 256 (§6.3); 3D spherical
  relativistic blast, frozen-flux scaling 32–2048 processors, above 0.75 with
  maximum box 20 (27,661 blocks) and worse with box 40 (§6.5, Fig. 30);
  relativistic Kelvin–Helmholtz, degrading below 3–4 blocks per processor
  (§6.6).
* AMR versus uniform CPU gains: 1D Torrilhon problem 1, 1.7, 3.3, 7.0, 15.9,
  32.3 up to 5 levels and 1977.8 at 10 levels, the static time inferred from
  ideal scaling (Table 2); 1D relativistic shock tube 3.4, 7.9, 15.2, 27.8,
  50.4 (Table 3); inclined Alfvén test 1.6 to 8.1 (Table 4); 3D rotated shock
  tube about 23 (§5.1.2); relativistic Kelvin–Helmholtz about 40 (§6.6).
* Machines: IBM Power 6 p575 and IBM BlueGene/P (CINECA); an 8-core Xeon
  workstation for §5.1.2 (Acknowledgements).

## Verification

From [Mignone et al. (2012)](/sources/mignone-2012.md), §5–§6. The paper
reports no convergence-order study; its "second-order" claims are not
measured there.
* [Field-loop advection](/benchmarks/field-loop-advection.md), $64\times32$
  base with 2–4 levels: the retained magnetic energy rises from about 94% to
  about 98% of the initial value with more levels (§5.2, Fig. 11).
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md),
  3D magnetic, base $16\times32\times16$ with 4 levels of ratio 2 or 2 of
  ratio 4: anisotropic suppression of small scales with field strength (§5.5,
  Fig. 17).
* Also: Torrilhon shock tube (pseudo-convergence to an irregular solution
  cured by resolution, §5.1.1), Ryu–Jones 3D rotated shock tube, GEM-like
  resistive reconnection (Sweet–Parker scaling reproduced), Gardiner–Stone
  current sheet, MHD shock–cloud with anisotropic conduction, radiative shocks
  in stellar jets, and relativistic tests: shock tube, inclined generic Alfvén
  test, rotor, cylindrical and spherical magnetized blast waves,
  Kelvin–Helmholtz, shock–cloud, and a 3D magnetized jet (§6).

## Comparisons in other sources

* [Stone et al. (2020)](/sources/stone-2020.md) (§2.2) class PLUTO among the
  patch-based Berger–Oliger/Berger–Colella AMR codes, and claim that
  [Athena++](/software/athena-plus-plus.md) has a higher per-core performance
  than the public versions of FLASH, PLUTO and Enzo, "in some cases by as much
  as a factor of 10" (§3.6.1).

# Citations

1. [Mignone et al. (2012)](/sources/mignone-2012.md), §§1–7, App. A–B (journal version).
2. [Stone et al. (2020)](/sources/stone-2020.md), §2.2, §3.6.1.
