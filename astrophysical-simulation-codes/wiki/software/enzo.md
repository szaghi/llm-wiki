---
type: Software
title: "Enzo (AMR code for cosmological and astrophysical fluid flow)"
description: "Open-source Cartesian patch-based AMR code in comoving coordinates (version 2.3) with four interchangeable fluid solvers (split PPM, unsplit MUSCL with GLM cleaning, constrained-transport MHD, ZEUS), the dual-energy formalism, subcycled level-by-level time stepping with flux correction, FFT plus grid-by-grid multigrid gravity, and coupled N-body, chemistry, cooling and radiation."
status: established
aliases: [ENZO, Enzo 2.3]
tags: [software, hydro, mhd, amr, cosmology, dual-energy, constrained-transport, divergence-cleaning, riemann-solver, self-gravity, multigrid, gpu, performance, verification, cooling, chemistry]
timestamp: 2026-10-13T00:00:00Z
---

# Enzo

Enzo is an open-source, Cartesian, block-structured AMR code for astrophysical
fluid flow in 1, 2 and 3 dimensions, written in comoving coordinates so that
cosmological expansion is included. The method paper documents Enzo 2.3
([Bryan et al. (2014)](/sources/bryan-2014.md), §1, §2.1).

## Code

* Website `http://enzo-project.org`; development on Bitbucket
  (`https://bitbucket.org/enzo/enzo-dev`) under Mercurial; test and figure
  scripts at `http://bitbucket.org/enzo/enzo-method-paper`. The figures use
  changeset `5d8c412`, which "corresponds to Enzo 2.3" (§1, §11.1.1, §13).
* Described only as "open-source"; no licence name is printed. The
  implementation language is not stated; the GPU port is in "CUDA C/C++"
  (§12.3).
* **Development process** (§11.1.1, §13): an answer-testing framework with
  quick, push and full suites (about 15 min, 1 h and 60 h on a 2013 desktop);
  the push suite is mandatory before acceptance; yt compares field statistics
  with stored "gold standard" results at about single-precision round-off, or
  bitwise for designated tests. All changes are peer-reviewed through pull
  requests; the paper recommends citing the changeset hash.

## Equations

Comoving ideal MHD with gravity (§2.1, eqs. 1–8), with $a$ the scale factor,
$\mathbf v$ the peculiar velocity and magnetic permeability 1:

$$\begin{aligned}
&\partial_t\rho + \tfrac1a\nabla\cdot(\rho\mathbf v) = 0,\\
&\partial_t(\rho\mathbf v) + \tfrac1a\nabla\cdot\left(\rho\mathbf v\mathbf v + \mathsf I\,P^* - \tfrac1a\mathbf B\mathbf B\right) = -\tfrac{\dot a}{a}\rho\mathbf v - \tfrac1a\rho\nabla\Phi,\\
&\partial_t E + \tfrac1a\nabla\cdot\left[(E+P^*)\mathbf v - \tfrac1a\mathbf B(\mathbf B\cdot\mathbf v)\right] = -\tfrac{\dot a}{a}\left(2E - \tfrac{|\mathbf B|^2}{2a}\right) - \tfrac{\rho}{a}\mathbf v\cdot\nabla\Phi + (\text{heating} - \text{cooling} + \text{conduction}),\\
&\partial_t\mathbf B - \tfrac1a\nabla\times(\mathbf v\times\mathbf B) = 0,
\end{aligned}$$

with $E = \frac{p}{\gamma-1} + \frac12\rho|\mathbf v|^2 + \frac{|\mathbf B|^2}{2a}$
and $P^* = p + \frac{|\mathbf B|^2}{2a}$; the Poisson equation has source
$\frac{4\pi G}{a}$ times the total density minus its mean. The
non-cosmological limit is $a=1$, $\dot a=0$. The Dedner solver uses a
different comoving field scaling, which adds a source $-\frac{\dot a}{2a}\mathbf B$
to the induction equation (§4.2). No relativistic solver is described.
Expansion terms are operator-split from all four solvers and integrated with an
implicit time-centred method (§4.1).

## Fluid solvers

Four interchangeable solvers (§2.2.2, §4):
* **PPM** (hydro only, §4.1): the direct-Eulerian variant of Colella &
  Woodward (1984), **dimensionally split**, with parabolic reconstruction of
  primitive variables, characteristic domain-of-dependence averaging, and
  optional steepening, flattening and diffusive flux. Interface states are
  "third-order accurate in space and second-order accurate in time"; the
  multidimensional scheme is "formally second-order accurate in space and
  time". The gravity source is time-centred with the average of old and new
  density (eq. 38).
* **MUSCL with Dedner cleaning** (hydro and MHD, §4.2): piecewise-linear
  reconstruction in primitive or conservative variables, HLL/HLLC/HLLD,
  [GLM divergence cleaning](/methods/glm-divergence-cleaning.md) with a
  constant $c_h$; **dimensionally unsplit**, second-order Runge–Kutta in time
  (Shu & Osher 1988). No damping coefficient of the GLM system is printed.
* **MHD-CT** (§4.3; Collins et al. 2010): the Godunov scheme of Li et al.
  (2008) with MUSCL-Hancock and PLM reconstruction and HLLC/HLLD; CT with the
  first-order EMF of Balsara & Spicer (1999) or the second-order methods of
  Gardiner & Stone (2005), without naming which Gardiner–Stone variant.
  Face-centred plus cell-centred (face-averaged) fields. $\nabla\cdot\mathbf B$
  is preserved to machine precision, but monopoles from other sources (e.g.
  ill-posed initial data) persist. See
  [constrained transport](/methods/constrained-transport.md).
* **ZEUS** (hydro only, §4.4): staggered velocities, operator-split source and
  transport steps, van Leer monotonic upwind advection, von Neumann–Richtmyer
  quadratic artificial viscosity (coefficient about 2); "formally second-order
  accurate in space but first-order accurate in time"; evolves internal energy,
  so it does not conserve total energy; shocks spread over 3–4 cells.
* **Riemann solvers** (§4.1.2): two-shock (PPM only), HLL and HLLC (PPM,
  MUSCL, MHD-CT), HLLD (MHD only). No Roe or LLF. A fallback after Lemaster &
  Stone (2009): if a negative density appears, that cell's fluxes are
  recomputed with HLL and the update redone. See
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md) and
  [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
* **Dual energy** (§4.1.1, eqs. 42–45; see
  [dual-energy formalism](/methods/dual-energy-formalism.md)): an internal
  energy equation, differenced non-conservatively with the old pressure, is
  carried alongside $E$. The pressure comes from $E$ minus the kinetic energy
  where that thermal fraction exceeds $\eta_1 = 10^{-3}$, and from the
  separately evolved internal energy otherwise; the internal energy is reset
  from $E$ where the thermal part relative to the maximum neighbouring total
  energy exceeds $\eta_2 = 0.1$. Motivated by kinetic-to-internal energy
  ratios up to $10^8$ in cosmological flows. Also available with CT, in an
  internal-energy or entropy form (§4.3).

## Adaptive mesh refinement

From [Bryan et al. (2014)](/sources/bryan-2014.md), §3; see
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* **Structure**: Berger–Colella structured AMR with rectangular patches
  ("grids") of variable size from clustering; integer $r_{\mathrm{ref}}$,
  generally 2, "since tests have shown this typically provides the best
  performance". Subgrids start and end on coarse-cell boundaries and lie wholly
  in one parent; no proper-nesting or 2:1 rule beyond that is stated.
* **Ghost cells**: $n_{\mathrm g}=3$ for PPM and ZEUS, 6 for the gravity solver
  (density and potential only).
* **Subcycling**: a recursive level-by-level `EvolveLevel` ("W-cycle"); each
  level takes its own $\Delta t_l$, and finer levels step until they catch up;
  fine steps are not restricted to the coarse step divided by a power of 2
  (Fig. 2).
* **Ghost filling** (§3.1): parent interpolation first, then sibling copies;
  interpolators must be conservative and monotone. The paper describes
  second-order multidimensional linear interpolators limited along cell
  diagonals, including a cloud-in-cell variant that is monotone but not
  conservative and a third-order variant conservative only after a correction
  that may break monotonicity (Appendix).
* **Projection** (§3.3, eq. 26): volume-weighted averaging with an exponent
  $d$, $d-1$ or 1 for cell-, face- or edge-centred data. **Flux correction**
  (§3.4, eq. 27): coarse cells adjacent to, not covered by, a fine region are
  corrected by $\Delta t$ times the coarse flux minus the sum of the fine
  fluxes.
* **CT on AMR** (§4.3): divergence-free prolongation interpolating all three
  face components together (Balsara 2001), using old fine-field data where
  present; the electric field, not $\mathbf B$, is projected fine to coarse and
  used to re-update the parent field.
* **Clustering** (§3.5): Berger & Rigoutsos signature/inflection splitting,
  accepting a proto-subgrid when its flagged fraction is "typically over 30%".
* **Refinement criteria** (§3.6): 13, among them normalized slope (typically
  0.3), baryon or particle mass, shocks, Jeans length (4 cells per Jeans length
  by default), cooling time, shear, optical depth, resistive length,
  metallicity and the Löhner (1987) estimator (default filter $10^{-2}$).
* **Cost model** (§12.2.4, eqs. 113–115): for $r_{\mathrm{ref}}=2$ the cost of
  level $l$ grows with $l$ unless the refined volume fraction drops by more
  than 16 per level; cosmological runs hover near that ratio.

## Gravity, particles and coupled physics

* **Gravity** (§5.1; see
  [Poisson solvers for self-gravity on adaptive meshes](/methods/multigrid-self-gravity.md)):
  the root grid is solved by FFT, periodic or isolated (James 1977). Subgrids
  use a 7-point second-order stencil with Dirichlet boundary values
  interpolated from the parent and are solved by multigrid **grid by grid**,
  with a buffer of 3 parent zones and optional sibling-boundary iterations
  (default 4). The paper admits that this is not a coherent level-wide solve
  and announces a HYPRE-based AMR solver; the effective force resolution is
  about twice the cell size.
* **Particles** (§5.2): particle-mesh with cloud-in-cell deposit,
  drift–kick–drift; particles live on the finest grid covering them.
* **Coupling** (§2.2.12, §6–§9): chemistry and conduction are subcycled;
  everything else shares one level step, the minimum over physics constraints.
  Also: a 12-species non-equilibrium primordial network, primordial and Cloudy
  metal cooling, UV backgrounds, adaptive ray-tracing radiation (Moray),
  flux-limited diffusion radiation (implicit, HYPRE-preconditioned, uniform
  grids only, §7.3), isotropic and anisotropic conduction, and star-formation
  and feedback recipes.
* **Time step** (§9, eqs. 88–96): Courant number typically 0.3–0.5 for hydro
  and about 0.5 for MHD, combined across directions by a harmonic sum (eq. 95,
  "yields a maximum" of 0.8). Recorded as printed: eq. 95 places the Courant
  number in a numerator over a sum of inverse steps that already contain it.

## Parallelization and performance

From [Bryan et al. (2014)](/sources/bryan-2014.md), §12:
* MPI only; a grid is the unit of distribution and lives on one process; the
  root grid is tiled into about as many tiles as processes; refined grids are
  placed with their parent and load-balanced per level by greedy transfer or a
  Hilbert curve. The full hierarchy metadata are replicated on every rank. A
  hybrid MPI+OpenMP version was "under development" (§12.1).
* **Unigrid weak scaling** (Fig. 19), $128^3$ cells per task on Cray XT4: 20%
  drop in cell updates per second per task from 8 to 4,096 tasks, 40% from 8
  to 13,824 tasks; experimental hybrid MPI+OpenMP scales comparably to 98,304
  cores (§12.2.2; Kraken XT5; no figure).
* **AMR strong scaling** (Fig. 20, Table 5): a $512^3$-root cosmology with 6
  levels and $3.04\times10^5$ grids on 128–16,384 cores. Refined levels scale
  well to 2,048 cores with marginal gains at 4,096; the root level degrades
  beyond 1,024 because root tiles are not repartitioned on restart. Limiters:
  boundary setting, the subgrid multigrid solve and hierarchy rebuilding; the
  replicated hierarchy prevented using 12 cores per node (§12.2.3).
* **GPU** (§12.3): the PPM and Dedner solvers are ported to CUDA, with fields
  copied to and from the device around each solver call. On Cray XK6 nodes
  (16-core Opteron + one Tesla K20), $256^3$ cells per node, driven MHD
  turbulence runs about 5× faster per node than on 16 CPU cores, about 80× one
  core (Fig. 22).

## Verification

From [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2; most tests are
qualitative figure comparisons, and no convergence-order study is presented.
* [Sod shock tube](/benchmarks/sod-shock-tube.md), 100 root cells, without and
  with 2 AMR levels; L1 errors unigrid PPM $2.8\times10^{-3}$, ZEUS
  $9.3\times10^{-3}$, MUSCL $7.9\times10^{-3}$; with AMR $9.6\times10^{-4}$,
  $3.8\times10^{-3}$, $2.4\times10^{-3}$ (Fig. 4).
* [Double Mach reflection](/benchmarks/double-mach-reflection.md), PPM,
  $960\times240$ (Fig. 7).
* [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md), 2D,
  $100\times100$ root plus 4 levels: PPM matches the analytic profiles
  "extremely well"; ZEUS lags with a diamond-shaped front (Figs. 8–9).
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md): CT and Dedner show
  "approximately equal effective resolution"; resolution not printed
  (Fig. 14).
* Also: wave pool and shock pool through static refined regions (ZEUS puts the
  shock in the wrong position), point-source gravity and orbit tests,
  self-similar infall, Zel'dovich pancake, one-zone collapse, a photo-evaporating
  clump with Moray, a cosmological ionization front with flux-limited
  diffusion, and anisotropic conduction.

## Comparisons in other sources

* [Almgren et al. (2010)](/sources/almgren-2010.md), §5.1, contrast Castro's
  gravity predictor–corrector with FLASH and Enzo, which they say
  extrapolate the half-step gravity from $t^n$ and $t^{n-1}$; Bryan et al.
  write the gravity source as time-centred (eq. 38) without saying how the
  half-step gravity is formed, so the attribution is not confirmed by
  Enzo's own paper.
* Enzo's implicit flux-limited diffusion module served as the timing reference
  for the explicit M1 module Hyperion of [Athena](/software/athena.md): Enzo's
  time was about constant in resolution (inexact Newton with a
  resolution-independent iteration count), and it could not run 2048 cells
  ([Skinner & Ostriker (2013)](/sources/skinner-2013.md), §4.2).
* [Tomida & Stone (2023)](/sources/tomida-2023.md) (§3.3.1, App. B) class
  Enzo's gravity among level-by-level ("one-way coupling") solvers, which they
  call not self-consistent; their estimate that such solvers are less accurate
  "by more than one order of magnitude" rests on a root-only solve, not on an
  implemented level-by-level solver, and they call it a "rough estimate".
* [Stone et al. (2020)](/sources/stone-2020.md) (§2.2) class Enzo among the
  patch-based AMR codes and claim higher per-core performance for
  [Athena++](/software/athena-plus-plus.md) than the public versions of FLASH,
  PLUTO and Enzo (§3.6.1).

## Later uses (batch 2)

* **Grackle.** The chemistry and cooling library
  [Grackle](/software/grackle.md) was extracted in 2012 from Enzo's cooling
  and chemistry solver, itself from Anninos et al. (1997)
  ([Smith et al. (2017)](/sources/smith-2017.md), §2, §3). This agrees with
  the coupled-physics list above: Grackle carries the same hierarchy of
  primordial networks up to twelve species, Cloudy-based metal cooling
  tables and UV backgrounds, and integrates chemistry and cooling sub-cycled
  inside the step handed over by the host (§3.1–§4). Its primordial
  chemistry is "closely based on" Enzo's, but it includes processes absent
  from Enzo 2.5, for example tunnelling in the collisional dissociation of
  H$_2$ (§3, §3.1). Enzo is one of the 14 listed host codes (§8.2). The
  sub-cycling limits Grackle uses (each sub-step changes the H and electron
  densities, and the internal energy, by at most 10 %; eqs. 9, 11) are
  Grackle's; the paper does not state whether Enzo's built-in solver uses
  the same rule. See
  [integrating cooling and chemistry source terms](/methods/radiative-cooling-integration.md).

## Later uses (batch 4)

[Villasenor et al. (2021)](/sources/villasenor-2021.md) use Enzo as the
main reference code for the cosmology extension of
[Cholla](/software/cholla.md); the Enzo version and solver settings of
these runs are not stated.
* **[Zel'dovich pancake](/benchmarks/zeldovich-pancake.md)** (§3.1,
  Fig. 1): the Bryan et al. set-up reproduced on 256 uniform Cholla
  cells; differences from Enzo at redshift 0 below 10 % in density and
  temperature except at the sharp shock features, about 20 % in velocity
  at the shock fronts, and below 1 % outside the shocks.
* **Dark-matter power spectrum** (§3.2, Fig. 2): agreement below 0.1 % at
  large and below 0.3 % at small scales, once Cholla's FFT solver uses the
  continuous Green's function (minus the inverse squared wavenumber); with
  Cholla's discrete-Laplacian Green's function the small-scale difference
  reaches "as much as ≈ 28%". This is consistent with the continuous
  option of Enzo's root-grid FFT solver listed above (§5.1 of Bryan et
  al.); Villasenor et al. do not state which option the Enzo run used,
  so this is implied by their choice, not stated. See [particle-mesh N-body](/methods/particle-mesh-gravity.md).
* **Adiabatic gas power spectrum** (§3.3, Figs. 3–4): below 1 % at large
  and below 15 % at small scales.
* **Dual energy** (§2.3, §3.4, Figs. 5–6): Cholla's switch is "similar to
  that used in Enzo"; in the mean-cosmic-temperature test Enzo heats from
  redshift about 15 and follows the virial-temperature estimate below
  redshift 6. See [dual-energy formalism](/methods/dual-energy-formalism.md).
* **Chemistry with a UV background** (§3.5, Figs. 7–8): projected fields
  agree qualitatively at redshift 0; the fitted intergalactic temperature
  at mean density and the slope of the temperature–density relation
  differ by less than 1 %.

## Later uses (batch 6)

* **AMR against the original Berger–Colella design.** The Adaptive mesh
  refinement section above labels Enzo's structure "Berger–Colella
  structured AMR". The primary source,
  [Berger & Colella (1989)](/sources/berger-1989.md), agrees on rectangular
  patches on coarse grid lines, conservative averaging of covered cells and
  the correction of uncovered coarse cells with the fine fluxes (§3; the
  construction behind Enzo's eq. 27). Two Enzo rules are its own, not the
  original's: subgrids wholly inside one parent, where the original's
  proper nesting is "not as stringent as requiring a fine grid to be
  contained in only one coarser level grid" (§2, Fig. 2.1); and a free
  $\Delta t_l$, where the original refines time by exactly the spatial
  ratio, $\Delta t_l/h_l$ equal on all levels (§2). The original also
  clusters by bisection and merging under a minimum flagged fraction of
  about 60 % (§5), not by Berger–Rigoutsos signatures. These qualify the
  label; they contradict nothing either source states. See
  [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* **Which Gardiner–Stone CT.** The MHD-CT entry above notes that Bryan et
  al. do not name the Gardiner & Stone (2005) variant.
  [Gardiner & Stone (2005)](/sources/gardiner-2005.md) give three corner-EMF
  constructions (a Lax–Friedrichs one, $\mathcal E_z^\circ$ and
  $\mathcal E_z^c$), recommend the contact-upwinded $\mathcal E_z^c$ and use
  only it in their second-order tests (§3.2.2, §3.3.1, §5); the paper is 2D
  only. Which one Enzo uses remains unstated. See
  [constrained transport](/methods/constrained-transport.md).

## Later uses (batch 10)

* **yt was built for Enzo.** [Turk et al. (2011)](/sources/turk-2011-c.md)
  describe the analysis toolkit yt as "originally designed exclusively for
  analyzing data from the AMR code Enzo", later generalized through
  per-code frontends (§1, §4). Their paper describes yt's own regression
  tests (§9) but not Enzo's answer-testing framework, so it neither
  confirms nor qualifies the Development process item above, where yt
  compares field statistics with "gold standard" results (Bryan et al.
  2014).
* **In-line analysis** (§6). An embedded Python interpreter per MPI task
  wraps Enzo's memory, with no data movement between tasks; at
  publication this interface existed only for Enzo, motivated by
  Population III data dumps of "as much as 10 gigabytes per time step".
* **Shared clustering mechanism** (§4.1). To read octree codes, yt
  coalesces cells into patches with "the mechanism used by Enzo to create
  subgrid patches" (axis histograms, cuts at zeros and at the strongest
  zero crossings of the second derivative), stopping when the fine-cell
  fraction exceeds an efficiency factor "typically set to be 0.2". The
  Clustering item above (flagged fraction "typically over 30%") is the
  same signature method with a different threshold for a different
  purpose (analysis patches, not simulation grids); no conflict.
* **Particles and output layout** (§4.3, §5.2). Enzo stores particles with
  the finest grid patch containing them, which agrees with the Particles
  item above. Enzo writes one file per processor with load-balanced, not
  spatially local, grids, so yt's image-plane decomposition of
  projections reads from many files; on a $5.5\times10^8$-cell Enzo data
  set ($512^3$ root, six levels) yt's adaptive projections scale from 4 to
  64 processors and its profiles to 128 (§5, Figs. 5–6).

# Citations

1. [Bryan et al. (2014)](/sources/bryan-2014.md), §§1–13, Appendix (arXiv v1).
2. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §4.2 (arXiv v1).
3. [Tomida & Stone (2023)](/sources/tomida-2023.md), §3.3.1, App. B (arXiv v1).
4. [Stone et al. (2020)](/sources/stone-2020.md), §2.2, §3.6.1.
5. [Smith et al. (2017)](/sources/smith-2017.md), §§2–4, 8.2 (arXiv v2).
6. [Villasenor et al. (2021)](/sources/villasenor-2021.md), §§2.3, 3.1–3.5, Figs. 1–8 (arXiv v2).
7. [Berger & Colella (1989)](/sources/berger-1989.md), §§2–3, 5, Fig. 2.1.
8. [Gardiner & Stone (2005)](/sources/gardiner-2005.md), §§3.2.2, 3.3.1, 5 (arXiv v1).
9. [Turk et al. (2011)](/sources/turk-2011-c.md), §§1, 4.1, 4.3, 5, 6, 9, Figs. 5–6.
