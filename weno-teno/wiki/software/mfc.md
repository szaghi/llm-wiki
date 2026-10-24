---
type: Software
title: "MFC"
description: "MFC (Multi-component Flow Code) is an open-source Fortran and Python solver for compressible multi-component, multiphase and bubbly flows: five- and six-equation diffuse-interface models, finite-volume WENO with HLLC and SSP Runge–Kutta; version 5.0 adds immersed boundaries, phase change, MHD, WENO-Z and TENO, low-Mach HLLC fixes and OpenACC/OpenMP GPU offload scaled to exascale machines."
status: established
aliases: [Multi-component Flow Code, MFC 1.0, MFC 3.0, MFC 5.0]
tags: [software, multiphase, interface-capturing, finite-volume, weno, gpu]
timestamp: 2026-10-23T20:43:00Z
---

# MFC

MFC (Multi-component Flow Code) is an open-source solver for
compressible multi-component, multiphase and bubbly flows, written in
Fortran 90 with MPI and driven by Python input scripts, released under
the GNU GPL v3. The bundle has two accounts:
[Bryngelson et al. (2021)](/sources/bryngelson-2021.md), which
describes version 1.0 of the code (the version read is the 2019 arXiv
preprint (v1), not the 2021 published article, so features and numbers
of the sections *Organization* to *Positioning* are those of that
text), and [Wilfong et al. (2026)](/sources/wilfong-2026.md), the
Computer Physics Communications announcement of MFC 5.0, which names the
2021 paper as its previous version (MFC 3.0 in their numbering),
supersedes it, and is written in Fortran 2008 and Python under the MIT
licence (program summary). Its additions are in the section *MFC 5.0*.

## Organization

The package has three Fortran components, pre-process, simulation and
post-process (§2, Table 1). Python dictionaries are written to Fortran
namelists; restart files go to a parallel (Lustre) file system and
output to Silo or HDF5; FFTW serves the cylindrical-coordinate
treatment. Grids are structured Cartesian or cylindrical with
stretching; boundary conditions include characteristic (Thompson),
periodic and free-slip ones; the build is a Makefile with a `test`
target (§2.2). The code was tested on UNIX, macOS and Windows.

## Models

- **Five-equation model** of Kapila et al., with the
  $K\nabla\cdot v$ term in the volume-fraction equation and the Wood
  mixture sound speed, and the variants of Allaire et al. and Massoni
  et al. without it; viscous stresses are included (§3.1). See
  [five- and six-equation models](/definitions/five-equation-model.md).
- **Six-equation model** of Saurel, Petitpas & Berry, with infinite
  pressure relaxation at every Runge–Kutta stage (§3.2, §4.6).
- **Stiffened-gas phases** with liquid constants fitted to
  shock-Hugoniot data (§3; see
  [stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)).
- **Ensemble-averaged dilute bubbly flow** (Zhang–Prosperetti), with
  Keller–Miksis (or Gilmore) single-bubble dynamics, log-normal bubble
  size bins, and reduced models of heat and mass transfer (§3.3). This
  physics lies outside the bundle and is listed only for completeness.
- **One-way acoustic sources** spread on the grid by a Gaussian discrete
  delta (§4.4).

## Numerical method

The method follows Coralic & Colonius (§4):

- **Finite-volume WENO.** Cell averages, with first-, third- or
  fifth-order WENO reconstruction of primitive (default), conservative
  or characteristic variables at faces, applied direction by direction
  (§2.2, §4.1). The paper does not print the weights, stencils or
  smoothness indicators. See [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
  and [characteristic decomposition](/methods/characteristic-decomposition.md).
- **Face quadrature.** Face fluxes and source terms are integrated with
  a $2\times2$ Gauss rule on each face, which the authors show to be
  necessary for fifth-order convergence in more than one dimension
  ([isentropic vortex](/benchmarks/isentropic-vortex.md); §4.1,
  Eqs. 29–32, §5.4).
- **Riemann solvers.** HLLC by default, HLL and exact solvers as options
  (see [HLL-family solvers](/methods/hll-riemann-solvers.md)).
- **Volume-fraction safeguards.** Clipping of the volume fractions to
  $[0,1]$ with renormalization, applied only to the evaluation of
  mixture properties, and an optional limiter that blends the WENO flux
  with a first-order flux according to a ratio of consecutive
  volume-fraction differences, with minmod, MC, ospre, superbee, Sweby,
  van Albada or van Leer limiter functions (§4.2; see
  [TVD limiters](/definitions/total-variation-diminishing.md)).
- **Cylindrical coordinates.** Extra $1/r$ source terms, no modified
  WENO weights in the azimuthal direction, the axis at a cell face, an
  even number of azimuthal cells and a spectral filter near the axis to
  relax the time-step limit; verified second-order (§4.3).
- **Time stepping.** The three-stage third-order TVD Runge–Kutta method
  of Gottlieb & Shu by default, orders 1 to 5 available (§4.5; see
  [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

## Verification, validation and performance

- **Validation against experiments.** Mach 1.22 air shock on a helium
  bubble (feature velocities within 10 %, generally about 5 %, of
  experiment; [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)),
  Mach 1.47 shock on a water cylinder against interferograms and a
  water-droplet aerobreakup
  ([shock–water-column interaction](/benchmarks/shock-water-column.md)),
  and a spherical air-bubble collapse whose radius follows Keller–Miksis
  and whose sphericity WENO keeps better than the MUSCL scheme of the
  ECOGEN code with the same model (§5.1–5.3, Figs. 1–4).
- **Verification.** Second- versus fifth-order convergence on the
  steady isentropic vortex with midpoint versus Gauss face quadrature,
  and the kinetic-energy dissipation rate of the
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) against
  Brachet et al.'s spectral solution (§5.4, Fig. 5). One-dimensional
  interface advection, a Mach 8.96 helium–air shock–interface problem,
  a gas–liquid shock tube and bubble-screen acoustics are recalled from
  earlier papers, not rerun (§5.5).
- **Parallel performance.** Strong scaling and speedup on a $500^3$ grid
  and weak scaling at $50^3$ cells per core, near ideal up to 4096
  cores, where results "deviate slightly from ideal" (§7, Fig. 8).

## Positioning by the authors

Bryngelson et al. contrast MFC with ECOGEN, "built upon an intrinsically
low-order MUSCL scheme", and with OpenFOAM, whose higher-order and
interface-capturing models are "only available via links to external
forked projects" (§1). They describe high-order WENO weight
modifications for cylindrical coordinates in the literature as
"generally complex" and prone to "numerical stability issues", and do
not adopt them (§4.3).

## MFC 5.0

Wilfong et al. state that the core diffuse-interface method is unchanged
from the previous version apart from performance, testing and added
physics (§2.1, §3): finite-volume cell averages after Coralic & Colonius,
WENO reconstruction of the face states (fifth order with Henrick et al.'s
[mapped weights](/methods/mapped-weno.md)), HLL or HLLC fluxes, TVD/SSP
Runge–Kutta and Thompson characteristic boundaries, with the flux
evaluated at the face centre (§3.1–3.4). The variables reconstructed are
not stated.

**Added physics** (§4.1):

- ghost-cell [immersed boundaries](/methods/immersed-boundary-method.md)
  with analytic or STL/OBJ vector level sets (§4.1.1–4.1.2);
- $N$-fluid phase change by infinite-rate pT and pTg relaxation solved by
  Newton's method, for the five- and the
  [six-equation model](/definitions/six-equation-model.md) (§4.1.3);
- Euler–Euler sub-grid bubbles by a conditional quadrature method of
  moments and Euler–Lagrange bubbles with Keller–Miksis dynamics
  (§4.1.4–4.1.5), and hypo- and hyperelastic solids (§4.1.6), outside the
  bundle;
- multispecies reacting gas with thermochemistry generated as Fortran by
  Pyrometheus ([multicomponent Euler equations](/definitions/multicomponent-euler-equations.md);
  §4.1.7);
- two-material surface tension in the six-equation model (§4.1.8;
  [oscillating droplet](/benchmarks/oscillating-droplet.md));
- ideal MHD with the HLLD solver of Miyoshi & Kusano, and relativistic
  MHD after Mignone & Bodo ([HLL-family solvers](/methods/hll-riemann-solvers.md),
  [relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md);
  §4.1.9–4.1.10, §4.2.5). No divergence control for the magnetic field is
  described ([divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

**Added numerics** (§4.2):

- [WENO-Z](/methods/weno-z.md) and [TENO](/methods/targeted-eno.md)
  weights at orders 3, 5 and 7, with a generic order-$(2k-1)$
  reconstruction on non-uniform grids written in cell-average differences
  $f_{j+1}-f_j$, which lowers the term counts from $k$ to $k-1$ for each
  candidate value and from $k(k+1)/2$ to $(k-1)k/2$ for each smoothness
  indicator, all coefficients precomputed (§4.2.2). The WENO-Z weights use
  $\tau=\lvert\beta_0-\beta_{k-1}\rvert$ at every order, with $q$ "typically
  set to 1 for fifth-order reconstruction"; the TENO measure is printed
  as $d_k\big(1+\tau/(\beta_k+\epsilon)\big)^6$, i.e. the registry's $\gamma_k$ with
  $C=1$, $q=6$ and an extra linear-weight factor, with "$K-2$ candidate
  stencils of increasing width" for a $K$th-order scheme; no values of
  $C_T$ or $\epsilon$ are printed. All three families recover their design
  orders on 1D linear advection (Fig. 12).
- generalized characteristic relaxation boundary conditions after
  Pirozzoli & Colonius (§4.2.1);
- Strang splitting with an adaptive embedded third/second-order
  Runge–Kutta pair for stiff bubble sources, which runs a bubble collapse
  at a 100 times larger step than the unsplit scheme (§4.2.3;
  [operator splitting](/methods/operator-splitting.md));
- two low-Mach corrections of HLLC, Thornber et al.'s velocity
  modification and Chen et al.'s anti-dissipation pressure correction,
  both with $z=\min\big(\max(\lvert v_L\rvert/c_L,\lvert v_R\rvert/c_R),1\big)$
  (page-local $z$, $v_L$, $v_R$, $c_L$, $c_R$ the face-normal velocities and
  sound speeds of the two states), which keep the
  [Gresho vortex](/benchmarks/gresho-vortex.md) "to visual accuracy" from
  $M=10^{-1}$ to $10^{-4}$ where plain HLLC does not (§4.2.4, Fig. 14).

**Software and performance** (§4.3). One source serves OpenACC and
OpenMP offload through Fypp macros, with the innermost loop over the
equations serialized; OpenACC is preferred on NVIDIA and AMD GPUs and
OpenMP used where AMD unified shared memory is needed (§4.3.1, Listings
1–4). Packing arrays for coalesced access before the WENO and Riemann
kernels gives a "ten-fold speedup", and compile-time case constants about
2× on CPUs and 10× on GPUs (§4.3.1, §4.3.6; stated). The grind time
(ns per grid point, equation and right-hand-side evaluation; 3D
two-species five-equation model, 8 equations, WENO5 with HLLC) is 0.32 on
a GH200, 0.38 on an H100 SXM5, 0.55 on an MI250X, 0.62 on an A100 and 1.2
on the best CPU, a 192-core AMD EPYC 9965 (Table 2). The WENO and
Riemann kernels reach 37 % and 14 % of peak on an A100 (Fig. 15). Weak
scaling stays at 95–99 % efficiency to 65,536 MI250X GCDs (Frontier) and
196,608 MI300A XCDs (El Capitan), and strong scaling with GPU-aware MPI
at 92 % for a 16-fold increase on Frontier (Figs. 17–18). The authors
report "the largest-to-date public CFD simulation at 200 trillion grid
points", a 2025 Gordon Bell finalist (§1.2, cited), and run
demonstrations up to $1600^3$ (Taylor–Green, Re 1600, Ma 0.1) and more than
$8\times10^9$ cells (shock–helium bubble) (§5;
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)).
Continuous integration runs the test suite against golden files on
several compilers, on CPUs and GPUs (§4.3.5).

**Evidence for the method** (§3.5, §4.1). Design orders 1, 3 and 5 on a
1D two-component periodic advection with HLL and HLLC (Fig. 1;
[material-interface advection](/benchmarks/material-interface-advection.md));
HLLD matching Miyoshi & Kusano's
[Brio–Wu](/benchmarks/brio-wu-shock-tube.md) profile and expected
convergence on a smooth Alfvén wave with WENO3 and WENO5 (Figs. 10–11;
[circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md));
a reactive shock tube against Martínez-Ferrer et al.
([shock-induced combustion](/benchmarks/shock-induced-combustion.md));
evaporation-front speeds of n-dodecane against Simões-Moreira & Shepherd
(Fig. 3). The demonstrations of §5 are stated to be capability runs,
validated by earlier work.

## Qualifications

- The hardware stated for the scaling runs, 288 nodes of two six-core
  processors (3456 cores), is smaller than the 4096 cores and more that
  the scaling plots show (§7).
- The comparison with ECOGEN rests on one sphericity history (Fig. 4b).
- Which WENO weights MFC 1.0 uses (Jiang–Shu or mapped) is not stated in
  the version read; mapped WENO is cited as background only. The MFC 5.0
  paper states that fifth order "is maintained through mapped weights"
  (Wilfong et al., §3.2.1).
- Wilfong et al. count "over 300 regression tests" (Abstract, §7) and
  "over 500" (§4, §4.3.5); describe the performance case as "8M grid
  points (158-cubed 3D uniform grid)", where $158^3\approx3.9\times10^6$
  *(compiler check, not in the sources)*; and print Kapila's coefficient
  with a sum in the numerator, which cannot hold for both phases (see
  [five-equation model](/definitions/five-equation-model.md)). Their
  TENO count "$K-2$ candidate stencils" gives one stencil at order 3, and
  Fig. 12 includes third-order TENO *(compiler check, not in the sources)*. Their characteristic-boundary
  split $\lambda\pm n_x\lvert\lambda\rvert$ is printed without a factor
  $\tfrac12$ (§4.2.1).
- The scaling and grind-time figures measure the code, not the
  discretization: no accuracy-per-cost comparison between WENO-JS,
  WENO-Z and TENO is given.

# Citations

- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — program summary; §1–§2, Tables 1–2; §3.1–3.3; §4.1–4.6, Eqs. (23)–(39); §5.1–5.5, Figs. 1–5; §7, Fig. 8 (arXiv v1).
- [Wilfong et al. (2026)](/sources/wilfong-2026.md) — program summary; §1.2; §2.1; §3.1–3.5, Fig. 1; §4.1.1–4.1.10, Figs. 2–11; §4.2.1–4.2.5, Figs. 12–14; §4.3.1–4.3.7, Table 2, Figs. 15–18; §5; §7.
