---
type: Software
title: "MFC"
description: "MFC (Multi-component Flow Code) is an open-source Fortran 90, MPI and Python solver for compressible multi-component, multiphase and bubbly flows: five- and six-equation diffuse-interface models, finite-volume WENO with HLLC and SSP Runge–Kutta, validated on shock–bubble and shock–water-column experiments and scaled to thousands of cores."
status: established
aliases: [Multi-component Flow Code, MFC 1.0]
tags: [software, multiphase, interface-capturing, finite-volume, weno]
timestamp: 2026-10-22T00:00:00Z
---

# MFC

MFC (Multi-component Flow Code) is an open-source solver for
compressible multi-component, multiphase and bubbly flows, written in
Fortran 90 with MPI and driven by Python input scripts, released under
the GNU GPL v3. The bundle's account is
[Bryngelson et al. (2021)](/sources/bryngelson-2021.md), which
describes version 1.0 of the code; the version read is the 2019 arXiv
preprint (v1), not the 2021 published article, so features and numbers
below are those of that text.

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

## Qualifications

- The hardware stated for the scaling runs, 288 nodes of two six-core
  processors (3456 cores), is smaller than the 4096 cores and more that
  the scaling plots show (§7).
- The comparison with ECOGEN rests on one sphericity history (Fig. 4b).
- Which WENO weights MFC 1.0 uses (Jiang–Shu or mapped) is not stated in
  the version read; mapped WENO is cited as background only.

# Citations

- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — program summary; §1–§2, Tables 1–2; §3.1–3.3; §4.1–4.6, Eqs. (23)–(39); §5.1–5.5, Figs. 1–5; §7, Fig. 8 (arXiv v1).
