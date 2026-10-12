---
type: Software
title: "Athena (astrophysical MHD code)"
description: "Second-order, directionally unsplit Godunov code for compressible ideal MHD and hydrodynamics in C and Fortran 95, with face-centred upwind constrained transport, CTU+CT and VL+CT integrators, HLLE/HLLC/HLLD/Roe solvers and MPI domain decomposition, extended by the two-moment M1 radiation module Hyperion."
status: established
aliases: [ATHENA, Athena (C), Hyperion]
tags: [software, mhd, hydro, constrained-transport, unsplit, riemann-solver, radiation, reduced-speed-of-light, performance, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Athena

Athena is a second-order, directionally unsplit, higher-order Godunov code
for compressible ideal MHD and hydrodynamics. Conserved variables are
cell-centred volume averages; the magnetic field is a set of face-centred
area averages evolved by [constrained transport](/methods/constrained-transport.md).
The method paper presents itself as the implementation reference for the
Gardiner–Stone CT algorithms in 2D (2005) and 3D (2008), and names three
novelties: a corner-EMF construction from the face Godunov fluxes,
characteristic-tracing PLM/PPM reconstruction extended to multidimensional
MHD with $\nabla\cdot\mathbf B$ source terms in the interface states, and the
extension of two unsplit integrators (CTU+CT, VL+CT) to MHD
([Stone et al. (2008)](/sources/stone-2008.md), §1). Its successor is
[Athena++](/software/athena-plus-plus.md).

## Code

* Two implementations: the original **C** code and a **Fortran 95** version.
  The C build uses an autoconf `configure` script, the Fortran 95 build a Perl
  script `buildathena`; input files use NAMELIST (Fortran 95) or a NAMELIST-like
  format (C). The only external library is MPI (MPICH or OpenMPI)
  ([Stone et al. (2008)](/sources/stone-2008.md), §7).
* The code is "freely available for download on the web" (abstract, §9); no
  URL, version number or licence is printed.
* Design priorities: modularity, documentation, ANSI standards and simple
  control of options. Riemann solvers, reconstruction, conserved–primitive
  conversion, boundary conditions, output and integrators are separate
  functions with common interfaces; all problem-specific code sits in one file
  (§7).

## Equations

Ideal MHD in conservative form, in units with magnetic permeability 1
(§2, eqs. 1–5):

$$\begin{aligned}
&\partial_t\rho + \nabla\cdot(\rho\mathbf v) = 0,\\
&\partial_t(\rho\mathbf v) + \nabla\cdot(\rho\mathbf v\mathbf v - \mathbf B\mathbf B + P^*\mathsf I) = 0,\\
&\partial_t E + \nabla\cdot\left[(E+P^*)\mathbf v - \mathbf B(\mathbf B\cdot\mathbf v)\right] = 0,\\
&\partial_t\mathbf B - \nabla\times(\mathbf v\times\mathbf B) = 0,
\end{aligned}$$

with $E = \frac{p}{\gamma-1} + \frac12\rho|\mathbf v|^2 + \frac12|\mathbf B|^2$.
* Four regimes: hydro or MHD, each with an adiabatic or a
  barotropic/isothermal equation of state; the barotropic case drops the
  energy equation (§2).
* Cartesian coordinates only; curvilinear coordinates, relativistic MHD and
  full-transport radiation MHD are listed as "underway" (§2, §9).
* Recorded as printed: §2 uses permeability-1 units, while App. A3 and the
  Orszag–Tang set-up carry $\sqrt{4\pi}$ factors (Gaps of the reading).

## Discretization and constrained transport

* Uniform Cartesian grid ("easily extended to nonuniform grids"); the
  finite-volume update uses time- and area-averaged fluxes, and the paper's
  half-integer time superscripts denote time averages, not midpoint values
  (§3, eqs. 11–15).
* Face-centred area-averaged $\mathbf B$ is advanced by the CT difference
  equations with edge-centred, time- and line-averaged EMFs
  $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$ (eqs. 16–24). CT keeps
  the cell-volume-averaged divergence (eq. 25) exactly zero; the cell-centred
  field is the arithmetic mean of the two face values (eqs. 26–28).
* **Corner EMF (§5.3, eqs. 79–81).** The edge EMF is the average of the four
  adjacent face EMFs plus gradient corrections. Each face gradient is
  upwinded by the sign of the contact (mass-flux) velocity, with the average
  of both sides when that velocity is zero, and is formed against a
  cell-centre reference EMF. The paper states that "simple arithmetic
  averaging does not work for the unsplit integrators adopted here" (§5).
* Stated cost of face-centred CT: it "complicates the implementation of the
  algorithm, and the interface to AMR drivers" (§3.2).

## Reconstruction

* Always in primitive variables. On the CTU+CT path, slopes are limited in
  characteristic variables, followed by characteristic tracing over
  $\Delta t/2$ (§4.2).
* **PLM**: monotonized-central limiter in characteristic variables (eq. 38).
  For HLL-family solvers an extra correction for waves moving away from the
  interface is added (eqs. 44–45); without it the flux would be first order.
  It is not added for the Roe or exact solvers (§4.2.2).
* **PPM**: Colella–Woodward parabolic interpolation and monotonicity
  conditions (eqs. 46–60); the Colella–Sekora extremum-preserving limiters
  are an option (§4.2.3).
* The algorithm is formally second order; "third-order" PPM lowers the error
  amplitude. Stated lesson: "improving the convergence rate of the
  reconstruction algorithm is not always the best way to improve the overall
  accuracy of the solution" (§4.2.3). Athena restricts itself to second order
  in space and time, citing Greenough & Rider (2003) on accuracy per cost
  (§3.1).
* The VL+CT path needs no characteristic tracing and no eigen-decomposition;
  the paper calls it a better fit for complex physics such as relativistic MHD
  (§4.2).

## Riemann solvers

See [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
([Stone et al. (2008)](/sources/stone-2008.md), §4.3).
* **HLLE**, with wave-speed bounds from the extreme Roe eigenvalues and the
  one-sided fast speeds (eqs. 61–63); positive-definite in 1D.
* **HLLC** (Batten et al. wave speeds), "highly recommended" for adiabatic
  hydro.
* **HLLD** (Miyoshi & Kusano 2005), as accurate as Roe and "much faster",
  "the best choice for many MHD applications".
* **Roe** (Cargo & Gallice for MHD; eqs. 64–68). If Roe gives a negative
  density or pressure in an intermediate state, that interface alone is
  recomputed with HLLE (or an exact solver) (§4.3.2, §8.1).
* **Exact solver** for isothermal hydro only. LLF and FORCE are mentioned as
  possible, not described as implemented options.
* **H-correction** for the carbuncle instability (Sanders et al. 1998,
  App. C): each wave speed in the Roe dissipation is bounded below by the
  maximum of a half wave-speed difference over a five-point (2D) or
  nine-point (3D) "H" stencil; it is applied only to the final
  multidimensional fluxes, and for HLL-type solvers the wave-speed bounds are
  modified instead.

## Integrators

See [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
* **2D CTU+CT** (§5.1, steps 1–11): reconstruct and solve Riemann problems in
  each direction; corner EMFs at $t^n$; correct the interface states over
  $\Delta t/2$ with transverse flux gradients plus $\nabla\cdot\mathbf B$
  source terms, advancing in-plane face fields by $\Delta t/2$ with CT;
  cell-centre reference EMF at $t^{n+1/2}$; second Riemann solve (with the
  H-correction if needed); corner EMFs; full update. The time step is
  $\Delta t = \nu\min\left(h/(|v_x|+c_f),\,h/(|v_y|+c_f)\right)$ with
  $\nu\le1$ (eq. 78; the paper allows different cell sizes per direction). The 2D scheme
  reduces exactly to the 1D algorithm for grid-aligned flow.
* **3D CTU+CT** (§6): the full CTU needs 12 Riemann solves per cell per step
  for stability up to $\nu\le1$; Athena's primary 3D integrator is the
  **six-solve** variant, stable for $\nu\le1/2$ (eq. 95), found "as accurate
  as the twelve-solve method" at about the same cost and "dramatically
  simpler to implement". Its transverse correction limits the
  $\nabla\cdot\mathbf B$ source terms with minmod (eqs. 88–89). The 3D scheme
  reduces exactly to 2D or 1D for flows with that symmetry (§6, §9).
* **VL+CT**: a MUSCL-Hancock-like predictor–corrector, detailed in Stone &
  Gardiner (2008). CTU+CT is "generally less diffusive and more accurate";
  VL+CT "has definite advantages" for some applications (§1).

## Mesh

* The described base is a uniform Cartesian grid with MPI domain
  decomposition. The code is "designed to be easily extensible" to static and
  adaptive mesh refinement; the AMR implementation with CTU+CT "will be given
  in a future communication" (§1, §9).
* One AMR run is shown: the magnetic Rayleigh–Taylor test with "five levels
  of refinement", base grid $8\times16$, effective finest resolution
  $256\times512$ (§8.4, Fig. 27). No refluxing, subcycling, block size,
  nesting or load-balancing details are given; the paper only states that
  conservation at fine/coarse boundaries is needed (Berger & Colella 1989).

## Physics modules

* Fixed-potential gravity source terms that conserve total energy exactly,
  and self-gravity that conserves total momentum exactly, both described in a
  Gardiner & Stone paper "in preparation"; shearing box; anisotropic thermal
  conduction; ionizing radiation transfer (Krumholz et al. 2007); passive
  scalars ([Stone et al. (2008)](/sources/stone-2008.md), §8.3, §8.4, §9). The
  source-coupling scheme (split or unsplit) is not described.

### Hyperion: two-moment radiation hydrodynamics

[Skinner & Ostriker (2013)](/sources/skinner-2013.md) add Hyperion, a gray
two-moment radiation hydrodynamics module, to Athena. The abstract states
that it "will be made freely available on the Web"; no URL, licence or
version is printed.
* **Equations** (§2.1, eq. 8): lab-frame gas equations plus the zeroth and
  first radiation moments in the mixed frame, gray, without scattering, with
  all source terms kept to first order in $|\mathbf v|/c$ times optical
  depth. The reduced speed $\hat c$ multiplies only the radiation time
  derivatives; the true $c$ stays in the sources and in the flux-to-energy
  ratio. When $\hat c\neq c$ total energy and momentum are not conserved; the
  conserved combinations are $E + (c/\hat c)E_{\mathrm r}$ and
  $\rho\mathbf v + \mathbf F_{\mathrm r}/(\hat c c)$ (§2.1). MHD terms "can be
  added" through Athena's CT but are not exercised; gravity enters only as a
  given $\Phi$.
* **Closure**: local M1, $\mathsf f_{\mathrm E} = \tfrac{1-\chi_{\mathrm E}}{2}\mathsf I + \tfrac{3\chi_{\mathrm E}-1}{2}\hat{\mathbf n}\hat{\mathbf n}$
  with $\chi_{\mathrm E} = \frac{3+4f_{\mathrm r}^2}{5+2\sqrt{4-3f_{\mathrm r}^2}}$
  (§2.3, eqs. 11–17); see [M1 radiation transport](/methods/m1-radiation-transport.md).
* **Transport** (§3.3): Athena's VL integrator (MUSCL-Hancock) with
  piecewise-linear reconstruction and an HLL solver. The named contribution is
  a closed-form expression for the M1 eigenvalues in multiple dimensions
  (eq. 41); only the two extreme eigenvalues are used. The reconstruction
  variables are not stated.
* **Splitting** (§3.1): gas and radiation are operator-split, formally first
  order in time; Strang splitting was "not found particularly advantageous".
  Radiation is subcycled, about $\hat c$ over the maximum gas signal speed
  times per gas step, under the
  [reduced speed of light](/definitions/reduced-speed-of-light.md). The gas
  Courant number is "usually 0.4" for VL. Gas integrator: unsplit VL or CTU
  (§3.4).
* **Energy exchange** (§3.4, eqs. 44–50): integrated locally and implicitly as
  a θ-scheme that reduces to a quartic in the gas internal energy, solved by
  Newton–Raphson with bisection fallback, default tolerance $10^{-10}$.
  Recorded as printed: the text says this step uses the gas time step, while
  eqs. 47 and 49 are written with the radiation time step.
* **RSLA criterion** (§3.2, eq. 35): $\hat c$ much larger than the maximum gas
  signal speed times $\max\{1,\tau_{\max}\}$. The RSLA is not viable in the
  dynamic diffusion regime and is "generally" practical for optical depths
  $\lesssim10$ (§5).
* **Scope**: dimensionally unsplit in 1D, 2D and 3D, MPI-parallel, uniform
  Cartesian grids only; no scaling data, threading, GPU or mesh refinement
  (abstract, §3.4, §5).
* **Tests**: nine verification tests (§4), among them a radiation linear wave
  with "nearly second-order" convergence in 1D, 2D and 3D
  ([linear wave convergence](/benchmarks/linear-wave-convergence.md);
  §4.1.2, Fig. 4). A 1D Marshak-wave timing comparison with Enzo's implicit
  flux-limited diffusion shows Hyperion's wall time growing linearly with the
  number of cells while Enzo's is about constant (§4.2; the text gives 16 to
  2048 cells, the Fig. 7 caption 32 to 2048).

## Parallelization and performance

From [Stone et al. (2008)](/sources/stone-2008.md), §7:
* Data layout (C version): a per-cell struct holding all variables, stored in
  3D arrays of structs; work is done on 1D pencils to help vectorization.
* The unsplit integrator stores left/right states and fluxes at every
  interface of the 3D grid, which raises memory use and lowers cache
  performance.
* About 10× more flops per cell than ZEUS, but only about 4× slower with
  HLLD. Table 1 (C, 3D, $128^3$, gcc -O3, 2.2 GHz Opteron), in $10^3$ cell
  updates per CPU second:

  | Physics | Roe | HLLC | HLLD |
  |---|---|---|---|
  | Isothermal hydro | 328 | 340 | — |
  | Adiabatic hydro | 224 | 242 | — |
  | Isothermal MHD | 108 | — | 124 |
  | Adiabatic MHD | 85.9 | — | 97.6 |

  ZEUS (F77) gives $404\times10^3$ for adiabatic MHD at $128^3$.
* MPI domain decomposition with ghost-cell swaps once per step. MHD with
  third-order reconstruction needs $n_{\mathrm g}=4$, more with the
  H-correction. Boundary exchange is sequential in $x$, $y$, $z$, so no
  corner (diagonal) messages are needed.
* Weak scaling on Red Storm (Cray XT-3), $32^3$ or $64^3$ cells per
  processor: efficiency "above 85%" up to 20,000 processors, called
  "essentially perfect weak scaling" (Fig. 6). No threading or GPU support.

## Verification

All with CTU+CT unless stated ([Stone et al. (2008)](/sources/stone-2008.md), §8):
* [Linear wave convergence](/benchmarks/linear-wave-convergence.md): hydro and
  MHD in 1D, second order for all wave families; oblique 3D MHD waves second
  order in all families (Figs. 7, 12, 32).
* [Sod shock tube](/benchmarks/sod-shock-tube.md) (Fig. 8), judged no longer
  "a discriminating test".
* [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md) (Fig. 13; the text
  says 800 zones, the caption 400).
* [Double Mach reflection](/benchmarks/double-mach-reflection.md) (Fig. 16).
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md):
  the Liska–Wendroff single-mode hydro case (Fig. 18) and the magnetic case on
  AMR (Fig. 27).
* [Field-loop advection](/benchmarks/field-loop-advection.md) in 2D and two 3D
  variants (Figs. 21, 34).
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (Figs. 22–24).
* [MHD blast wave](/benchmarks/mhd-blast-wave.md), 2D adiabatic and
  isothermal, and 3D (Figs. 28–30, 36).
* Also: Woodward–Colella interacting blast waves, Shu–Osher, Einfeldt strong
  rarefaction, Torrilhon, Ryu–Jones 2a (also oblique in 3D) and 4d,
  Liska–Wendroff implosion, circularly polarized Alfvén wave, MHD rotor, Noh
  3D strong shock.

## Assessments in later sources

* [Athena++](/software/athena-plus-plus.md) is a from-scratch C++ rewrite of
  Athena that keeps the finite-volume and upwind-CT algorithms but does not
  implement CTU ([Stone et al. (2020)](/sources/stone-2020.md), §1, §3.2.3).
  In the stratified Kelvin–Helmholtz benchmark of Lecoanet et al. (2015),
  Athena (CTU+PPM, split diffusion) needed $16384\times32768$ cells to converge
  to the Dedalus solution, against $8192\times16384$ for Athena++ with RK3+PPM
  (§3.3.6).
* The discretization of the gravitational stress tensor used in Athena and
  Athena++ v19.0 does not yield a curl-free gravity and produces anomalous
  accelerations near massive bodies with light atmospheres
  ([Mullen, Hanawa & Gammie (2021)](/sources/mullen-2021.md), §2.3.1, §3.3;
  see [conservative self-gravity](/methods/conservative-self-gravity.md)).
* [GAMER](/software/gamer.md) adopts Athena's two unsplit schemes, CTU+CT and
  VL+CT, for its MHD solver
  ([Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §3.2).

## Later uses (batch 2)

* **Conservative total-energy self-gravity.**
  [Jiang et al. (2013)](/sources/jiang-2013.md) add to Athena's unsplit CTU
  algorithm a self-gravity coupling that conserves total energy (internal
  plus kinetic plus $\tfrac12\rho\Phi$) to round-off, with a gravitational
  energy flux and a second Poisson-type solve per step for $\partial_t\Phi$
  driven by the Riemann mass fluxes (§§2–3); see
  [conservative self-gravity](/methods/conservative-self-gravity.md). They
  state that the conservative momentum equation with the gravitational
  stress tensor $\mathsf T_{\mathbf g}$ "has already been implemented in
  many grid-based codes, such as Athena" (§1), which agrees with the
  momentum-conserving self-gravity listed under Physics modules. The runs
  are hydrodynamic only, with HLLC, Courant number 0.8, periodic boundaries
  and an FFT Poisson solver; the paper asserts without a test that MHD does
  not change the gravity implementation, gives no Athena version, and does
  not say whether the option is in a public release (§3, §4). Tests: 1D and
  2D [Jeans waves](/benchmarks/jeans-wave.md) and Jeans collapse, and a 3D
  collapsing polytrope (§4).
* **The stress tensor judged by a Castro paper.**
  [Katz et al. (2016)](/sources/katz-2016.md), §2.3.1, note that the
  stress-tensor momentum source "is used by Jiang et al. (2013) for ATHENA"
  and conserves momentum to round-off, but reject it for
  [Castro](/software/castro.md): the divergence of the discrete acceleration
  "is no longer guaranteed to equal the zone density", and the mixing of
  acceleration components lets truncation error imply a density "much
  different than the zone's actual density", harmful in low-density ambient
  gas (asserted, no test). They also avoid Jiang et al.'s total-energy
  variable, because recovering $E$ by subtracting the potential energy in
  low-density regions gives "unphysical energies or temperatures".

## Later uses (batch 3)

* **Athena's VL+CT in a GPU code.** [Cholla](/software/cholla.md) adopts
  the VL+CT integrator of Stone & Gardiner (2009) as its default, replacing
  CTU as "more robust than the CTU algorithm described in Schneider &
  Robertson (2015)", with HLLD fluxes
  ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.2). Its edge-EMF
  figure is "based on Figure 5 of Stone et al. 2008", and its PLM projects
  onto characteristic variables with the eigenvectors of
  [Stone et al. (2008)](/sources/stone-2008.md) (§2.2.4, §2.2.6). Measured
  on Cholla's VL+CT: formally limited to $\nu \le 0.5$, it is not stable at
  0.5 but stable at 0.4, and is typically run at 0.3 (§2.2.1, footnote 4).
* **Comparisons Cholla draws with Athena results.** PPM linear-wave errors
  "comparable to" Stone & Gardiner (2009) (§3.1.1); field-loop
  magnetic-energy dissipation "comparable" to Stone et al. (2008)
  (§3.1.3); the Felker & Stone (2018) PPM "significantly reduces
  oscillations" in the Brio–Wu problem compared with the PPM of Stone et
  al. (2008) (§3.1.4); the 3D Orszag–Tang vortex is compared qualitatively
  with Stone et al. (2008), Fig. 22 (§3.1.6). In the 3D MHD blast wave
  "Like Stone & Gardiner (2009), we find instabilities if β is decreased by
  a factor of 10", i.e. at plasma beta 0.02 (§3.1.5). This does not
  contradict Athena's "robust for low-β flows" above, which refers to
  CTU+CT with an isothermal equation of state
  ([Stone et al. (2008)](/sources/stone-2008.md), §8.4); Cholla's run is
  adiabatic VL+CT.
* **IDEFIX.** Its default edge EMF is the Gardiner–Stone upwind variant,
  "similar to Athena", selectable at run time
  ([Lesur et al. (2023)](/sources/lesur-2023.md), §2.4); its double Mach
  reflection is compared visually with Stone et al. (2008), Fig. 16
  (§4.1), and its Orszag–Tang cuts are taken at $y = 0.316$ and 0.425
  against Athena's 0.3125 and 0.427 (§4.2). See [IDEFIX](/software/idefix.md).
* **AthenaK.** The AthenaK paper cites Stone et al. (2008) as an earlier
  version in the Athena lineage and, like Athena++, does not implement CTU,
  which "does not extend easily to the relativistic equations of motion"
  ([Stone et al. (2026)](/sources/stone-2026.md), §3). See
  [AthenaK](/software/athenak.md).

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §§1–9, App. C (journal version).
2. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §§2–5 (arXiv v1).
3. [Stone et al. (2020)](/sources/stone-2020.md), §1, §3.2.3, §3.3.6.
4. [Mullen, Hanawa & Gammie (2021)](/sources/mullen-2021.md), §2.3.1, §3.3 (arXiv v1).
5. [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §3.2 (arXiv v4).
6. [Jiang et al. (2013)](/sources/jiang-2013.md), §§1–4 (arXiv v2).
7. [Katz et al. (2016)](/sources/katz-2016.md), §2.3.1 (arXiv v2).
8. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.2, §2.2.1, §2.2.4, §2.2.6, §3.1.1, §3.1.3–§3.1.6 (arXiv v2).
9. [Lesur et al. (2023)](/sources/lesur-2023.md), §2.4, §4.1, §4.2 (arXiv v1).
10. [Stone et al. (2026)](/sources/stone-2026.md), §3 (arXiv v1).
