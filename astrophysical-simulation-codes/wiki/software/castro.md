---
type: Software
title: "CASTRO (compressible astrophysics code on BoxLib AMR)"
description: "BoxLib-based C++/Fortran 90 code for multicomponent compressible hydrodynamics with a general equation of state, reactions and self-gravity, using an unsplit PPM Godunov method with full corner coupling and a two-shock-type Riemann solver on subcycled Berger–Oliger patch AMR with refluxing and a multilevel Poisson synchronization."
status: established
aliases: [CASTRO, Castro]
tags: [software, hydro, amr, unsplit, riemann-solver, self-gravity, multigrid, dual-energy, performance, verification]
timestamp: 2026-10-12T00:00:00Z
---

# CASTRO

CASTRO is an Eulerian, block-structured AMR code for the multicomponent
compressible Euler equations with a general (user-supplied) equation of state,
self-gravity, nuclear reactions and, in a second paper, radiation
([Almgren et al. (2010)](/sources/almgren-2010.md), §1–§2). There is no MHD
and no relativity.

## Code

* Built on BoxLib: C++ for memory management, control flow, communication and
  I/O, Fortran 90 for the numerical kernels and multigrid; data held in
  MultiFab/FAB containers (§7.1). A user guide is cited (CASTRO User Guide
  2009); no repository URL, licence or version number is printed.
* Plotfile/checkpoint format: one directory per dump with an ASCII header,
  written with coordinated multi-stream I/O; about 13 GB/s on single-level
  uniform grids on Franklin (Cray XT4), about 5 GB/s sustained for multilevel
  runs (§7.2–§7.3).

## Equations

Conservative compressible Euler with sources (§2, eqs. 1–6), here written
with the registry's energy density $E$ (the paper writes density times a specific
total energy):

$$\begin{aligned}
&\partial_t\rho + \nabla\cdot(\rho\mathbf v) = s_{\rho},\\
&\partial_t(\rho\mathbf v) + \nabla\cdot(\rho\mathbf v\mathbf v) + \nabla p = \rho\mathbf g + s_{\rho\mathbf v},\\
&\partial_t E + \nabla\cdot\left[(E+p)\mathbf v\right] = \rho\mathbf v\cdot\mathbf g + (\text{nuclear energy release}) + s_{E},
\end{aligned}$$

plus species mass fractions with reaction rates, passively advected scalars,
and auxiliary scalars passed to the equation of state. Gravity enters as a
non-conservative source, not as a flux.
* **EOS** (§3): called with density, specific internal energy and
  composition; gamma law, Helmholtz (Timmes & Swesty 2000) and Lattimer–Swesty
  are shipped; tabular EOSs are inverted by Newton–Raphson.
* **Coordinates** (§1): 1D spherical, 1D/2D cylindrical, 1D/2D/3D Cartesian;
  geometric source terms enter the traced states (§5.2).

## Time integration

* Reactions are Strang-split around the hydro step (half reaction step, hydro
  step, half reaction step; eqs. 12a–c). Fluxes are "purely explicit, based on
  an unsplit Godunov method", "formally second-order in both space and time"
  (§5).
* **Source predictor–corrector** (§5.1, eqs. 15–20): the hydro step uses
  sources at the old time; after it, the Poisson equation is re-solved with the
  new density and the gravity and external sources are corrected by
  $\frac{\Delta t}{2}$ times their change, so they are time-centred. The paper
  contrasts this with FLASH and ENZO, which extrapolate the gravity at
  $t^{n+1/2}$ from $t^n$ and $t^{n-1}$.
* **Post-step fixes** (§5.1): density floor, non-negative renormalized mass
  fractions, an optional velocity sponge, and evolution of the internal energy
  density alongside $E$ when kinetic energy dominates, after Bryan et al.
  (1995) (see [dual-energy formalism](/methods/dual-energy-formalism.md)).
* **Time step** (eqs. 23–24): $\Delta t = \nu\min_i\min_{\mathbf x} h/(|v_i|+c_s)$,
  a minimum over directions (not a sum), $\nu\in(0,1)$ user-set.

## Hydrodynamics

See [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md)
([Almgren et al. (2010)](/sources/almgren-2010.md), §5.2).
* **Reconstruction**: PPM, direction by direction, on primitive variables
  (density, velocity, pressure, internal energy density, species, scalars).
  The default limiter is Colella & Sekora (2008) / McCorquodale & Colella
  (2010), which "avoids reducing the order ... at smooth local extrema" and "is
  insensitive to asymmetries caused by roundoff". Options: unsplit PLM, or the
  Miller & Colella (2002) / Colella–Woodward PPM limiters. A flattening
  coefficient is applied as in FLASH but with the **opposite convention** (1
  means no flattening, 0 first order) (eqs. 27–29).
* **Characteristic tracing** integrates the parabola over each wave's domain
  of dependence (eqs. 30–32); sources, including gravity, enter the traced
  states. Full 3D corner coupling follows Miller & Colella (2002), §4.2.1, and
  is not reproduced in the paper.
* **Riemann solver** (eqs. 33–35; see
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)): a
  Colella–Glaz–Ferguson-type two-shock solver after Bell, Colella &
  Trangenstein (1989), for a general convex EOS, with no EOS call because the
  internal energy density is carried. The star state comes from linearized
  Rankine–Hugoniot relations with Lagrangian sound speeds; sampling uses a
  shock speed or interpolation in a transonic rarefaction. Added: a small
  quadratic artificial viscosity proportional to $\nabla\cdot\mathbf v$
  (coefficient not given) and rescaling of species fluxes to sum to the mass
  flux. No HLLE, HLLC, Roe or LLF option is described.
* **Split versus unsplit** (§8.3, Fig. 9): on single-mode Rayleigh–Taylor, all
  three dimensionally split variants (PLM, old PPM, new PPM) produce spurious
  secondary instabilities, attributed to alternating compression and expansion
  between sweeps; unsplit PLM and old PPM show mild anomalies at the bubble and
  spike tips; unsplit new PPM is cleanest. Unsplit costs about 2× CPU and
  memory in 2D; in 3D slightly less than 2× CPU and under 10% more memory
  thanks to strip-mining.

## Adaptive mesh refinement

From [Almgren et al. (2010)](/sources/almgren-2010.md), §6; see
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* **Structure**: nested levels $l=0$ to the finest; each level is a union of
  non-overlapping rectangular grids of arbitrary size (split by a maximum grid
  size), with an even number of cells per direction; $r_{\mathrm{ref}}\in\{2,4\}$,
  isotropic. Proper nesting with a buffer of 2 coarse cells (ratio 2) or 1
  (ratio 4), "since four ghost cells are needed for the PPM algorithm". **No
  parent–child relation** is required (Fig. 1).
* Tagging by user error estimators, Berger–Rigoutsos clustering, regridding
  every few level steps; new fine data copied or interpolated from coarse (the
  interpolation is not specified); a restart can enlarge the domain (§6.1).
* **Subcycling**: recursive Berger–Oliger stepping with
  $\Delta t_{l+1} = \Delta t_l/r_{\mathrm{ref}}$; synchronization averages fine
  onto coarse and refluxes the coarse cells adjacent to, but not covered by,
  the fine level (Berger & Colella 1989). The order of coarse–fine ghost
  interpolation in space and time is not stated (§6.2.1).

## Self-gravity

See [Poisson solvers for self-gravity on adaptive meshes](/methods/multigrid-self-gravity.md)
and [conservative self-gravity](/methods/conservative-self-gravity.md).
* **Options** (§4): constant $\mathbf g$; monopole (a radial density profile
  per level and time, enclosed mass, interpolated back); full Poisson
  $\nabla^2\Phi = 4\pi G\rho$, $\mathbf g = -\nabla\Phi$, with Dirichlet
  boundary values from the coarsest-level monopole, standard finite
  differences and geometric multigrid V-cycles with red–black Gauss–Seidel; an
  optional point mass.
* **Multilevel synchronization** (§6.2.2–§6.2.3, eqs. 36–40): a composite
  solve at the start and after regridding; level solves at the start and end
  of each level step with a lagged correction (after Miniati & Colella 2007);
  after subcycling, a two-level composite **correction solve** driven by the
  refluxing density change and by a flux register of potential-gradient
  mismatches at the coarse–fine boundary. The resulting gravity correction
  gives momentum and energy "sync sources" applied with $\frac12\Delta t$ on
  both levels; the register is propagated to the next coarser level. The
  correction-solve tolerance equals the final residual of the level solve.

## Parallelization and performance

From [Almgren et al. (2010)](/sources/almgren-2010.md), §7:
* MPI with at least one grid per core per level, or hybrid MPI+OpenMP with one
  larger grid per socket and threads within it. Grids are distributed by a
  knapsack heuristic or a Morton space-filling curve, switching automatically
  on the ratio of grids per level to processors. No GPU (§7.1).
* Weak scaling on jaguarpf, one $64^3$ grid per processor, 8 to 64,000
  processors: "scales excellently" without gravity and with monopole gravity,
  24.8 µs per cell per step per core at 64,000 processors without gravity;
  Poisson gravity scales "relatively good ... up to only 13,824 processors"
  (Fig. 2). The overhead of a two-level AMR run (monopole) relative to the
  ideal factor of 3 is about 5% at 8 processors and 19% at 64,000 (§7.4).
* Hybrid MPI+OpenMP gives "at least a factor of 3" lower linear-solver time on
  a $768^3$ strong-scaling case at large processor counts (no figure).

## Verification

From [Almgren et al. (2010)](/sources/almgren-2010.md), §8 (all qualitative
except the hydrostatic star):
* [Sod shock tube](/benchmarks/sod-shock-tube.md) on 32 cells plus 2 levels of
  ratio 2: "excellent agreement" with the exact solution (§8.1.1, Fig. 3).
* [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md), spherical
  in 1D spherical, 2D cylindrical (r–z) and 3D Cartesian coordinates and cylindrical in
  2D Cartesian, with 3 or 4 levels: density, velocity and pressure match the
  exact solution; internal energy is hardest near the origin (§8.2,
  Figs. 6–8).
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md),
  single mode, $256\times512$, six split/unsplit schemes (§8.3).
* Hydrostatic white dwarf at $192^3$, $384^3$, $768^3$: peak spurious velocity
  below 1% of the central sound speed at the highest resolution, and "clear
  second order convergence in the max norm" of the velocity (§8.4, Fig. 11).
* Also: Toro double rarefaction and strong shock (the text says the pressure
  jump spans "six orders of magnitude"; the printed states give $10^5$),
  homologous dust collapse, a reacting-bubbles comparison with FLASH, and a
  Type Ia supernova demonstration (§8.1.2–§8.1.3, §8.5–§8.7).

# Citations

1. [Almgren et al. (2010)](/sources/almgren-2010.md), §§1–8 (arXiv v1).
