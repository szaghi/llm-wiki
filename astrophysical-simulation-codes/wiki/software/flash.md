---
type: Software
title: "FLASH"
description: "Block-structured AMR code on the PARAMESH library: its first version from the code paper (8-cell blocks, no subcycling, fine-flux sums, Löhner refinement, split direct-Eulerian PPM with a two-shock solver, Helmholtz EOS, nuclear networks, ASCI scaling), and two star-formation configurations: an HLL5R MHD solver, multigrid self-gravity after Ricker (2008), Jeans-length refinement, accreting sink particles with creation checks and (in the 2021 configuration) intrinsic spin, a barotropic piecewise-polytropic closure, and turbulence-driving and protostellar-feedback sub-grid modules."
status: established
aliases: [FLASH code, flash4, FLASH4, FLASH/PARAMESH]
tags: [software, mhd, hydro, amr, self-gravity, multigrid, sink-particles, riemann-solver, equation-of-state, verification, performance]
timestamp: 2026-10-13T00:00:00Z
---

# FLASH

FLASH (Fryxell et al. 2000; Dubey et al. 2008) is a block-based AMR code
built on the PARAMESH library (MacNeice et al. 2000). Its code paper,
[Fryxell et al. (2000)](/sources/fryxell-2000.md), describes the first
version and is summarized in Later uses (batch 8) below. This page collects what two ingested
star-formation papers state about the configurations they ran,
[Federrath et al. (2010)](/sources/federrath-2010.md) (the sink-particle
module) and [Mathew & Federrath (2021)](/sources/mathew-2021.md) (an
application with sinks and sub-grid feedback), together with statements
about FLASH in other ingested sources. Neither paper describes FLASH's
reconstruction scheme or time integrator (the code paper,
[Fryxell et al. (2000)](/sources/fryxell-2000.md), does; see batch 8).

## Code and version

* The version used in [Federrath et al. (2010)](/sources/federrath-2010.md)
  is not stated; the multigrid solver is "implemented in flash v2.5,
  recently refined for v3 by Ricker 2008" (§2.1).
* [Mathew & Federrath (2021)](/sources/mathew-2021.md) run "flash4" and
  give no minor version (§2.1).
* Language, licence and distribution are not stated in either source.
  [Stone et al. (2020)](/sources/stone-2020.md), §3.6.1, compare
  Athena++ with "the public versions" of FLASH, PLUTO and Enzo.

## Equations

* **Ideal MHD with a barotropic closure** (Mathew & Federrath, §2.1,
  eqs. 1–3): continuity, momentum with the Lorentz force and the total
  pressure $P^*$, and induction with $\nabla\cdot\mathbf B = 0$, in
  Gaussian units. The momentum equation carries the self-gravity and
  sink acceleration $\mathbf g$ and a turbulence-driving acceleration. No
  energy equation is solved; the pressure comes from the equation of state
  (§2.4). The paper does not say how $\nabla\cdot\mathbf B$ is controlled.
* **Piecewise-polytropic EOS** (Mathew & Federrath, §2.4, eqs. 5–7). The
  pressure is $c_s^2$ times a power of $\rho$, with $c_s = 0.2$ km s$^{-1}$
  and $\mu = 2.35$; the polytropic exponent is 1 for
  $\rho \le 2.50\times10^{-16}$, 1.1 up to $3.84\times10^{-13}$, 1.4 up to
  $3.84\times10^{-8}$, 1.1 up to $3.84\times10^{-3}$ and $5/3$ above
  (g cm$^{-3}$). The branches follow radiation-hydrodynamic collapse
  calculations (Larson 1969; Masunaga & Inutsuka 2000). Here $c_s$ is an
  isothermal sound speed and the exponent is not a ratio of specific
  heats.
* [Federrath et al. (2010)](/sources/federrath-2010.md) use an isothermal
  gas with $c_s = 0.19$ km s$^{-1}$ in the cluster run (§4) and a
  barotropic EOS with exponents 1, 1.1 and 4/3, breaking at 0.25 and 5.0
  in units of $10^{-15}$ g cm$^{-3}$, in the Boss–Bodenheimer test
  (§3.5, eqs. 30–31).
* [Coleman (2020)](/sources/coleman-2020.md), §1, states that FLASH has
  published no dynamical test of a non-ideal EOS against a known solution
  (asserted).

## Solvers

* **Riemann solver.** The 5-wave HLL5R approximate Riemann solver
  (Waagan et al. 2011), which "has comparable accuracy to the standard
  FLASH-Roe solver, but it is more efficient and has a better stability"
  ([Mathew & Federrath (2021)](/sources/mathew-2021.md), §2.1; stated by
  citation, not measured there). See
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* **Time step.** The hydrodynamic step is
  $\nu\,h/\max(\vert\mathbf v\vert, c_s)$ over the mesh, with the
  fastest magnetosonic speed in MHD, and is also limited by the sink
  particles (below) ([Federrath et al. (2010)](/sources/federrath-2010.md),
  §2.5, eq. 20).
* **As described by Castro's authors.** FLASH extrapolates the
  gravitational acceleration to $t^{n+1/2}$ from $t^n$ and $t^{n-1}$,
  where Castro uses a predictor–corrector, and FLASH's flattening
  coefficient has the opposite convention to Castro's
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §5.1, §5.2,
  eqs. 27–29). Castro's reacting-bubbles test is compared with FLASH 2.5
  using split PPM, with "excellent agreement" of the temperature and
  $^{24}$Mg contours at 2.5 s (§8.6, Figs. 13–14).

## Mesh and AMR

* **Block-based AMR.** [Stone et al. (2020)](/sources/stone-2020.md),
  §2.2, class FLASH/PARAMESH with NIRVANA, DISPATCH and Athena++ as
  block-based; [Bryan et al. (2014)](/sources/bryan-2014.md), §1, contrast
  FLASH's fixed blocks with Enzo's variable-size patches. Mathew &
  Federrath cite Berger & Colella (1989) for the AMR (§2.1). See
  [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* **Jeans refinement.** Federrath et al. keep at least 12 cells per Jeans
  length on every level below the finest and 5 on the finest (§4.2.1);
  their gravity test refines at 6 and derefines above 12 (§3.2). Mathew &
  Federrath keep $N_{\mathrm J} \ge 16$ on all levels below the finest,
  "to prevent underestimation of the turbulent energy and to resolve the
  local collapse reasonably well" (citing Federrath et al. 2011), and 5 on
  the finest through the sink size (§2.3). See the
  [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md).
* **Other criteria.** Every cell within a sink's accretion radius is kept
  at the finest level (Federrath et al., §2.2.2); the cluster run adds
  shock refinement (§4.2). Mathew & Federrath name no criterion other
  than the Jeans one.
* **Grids run.** Federrath et al.: $32^3$ root plus 2 levels (gas–sink
  gravity test, §3.2); $128^3$ root plus 2 levels, effective $512^3$
  (cluster, §4.2). Mathew & Federrath: a 2 pc periodic box at effective
  $N = 4096$, finest $h = 100$ AU; root size and level count not stated
  (§2.6, Table 1).

## Self-gravity

* Gas self-gravity by multigrid (Ricker 2008), with isolated boundaries
  in Federrath et al.'s tests; a tree solver is an alternative
  ([Federrath et al. (2010)](/sources/federrath-2010.md), §§2.1, 2.4,
  eq. 14; [Mathew & Federrath (2021)](/sources/mathew-2021.md), §2.1).
* [Tomida & Stone (2023)](/sources/tomida-2023.md), footnote 4,
  describe Ricker's FLASH solver as a direct solve on blocks combined
  with an inter-level correction rather than a multigrid over the whole
  hierarchy.
* In Federrath et al.'s static singular-isothermal-sphere test the
  potential loses spherical symmetry near the Cartesian boundaries, so
  test orbits broaden after 10–100 orbits (§3.2, Figs. 5–6). See
  [Poisson solvers on adaptive meshes](/methods/multigrid-self-gravity.md).

## Sink particles

The sink module is described on
[sink particles](/methods/sink-particles.md). In brief:
* **Creation** at the finest level when a control volume of radius
  $r_{\mathrm{acc}}$ exceeds
  $\rho_{\mathrm{thr}} = \pi c_s^2/(4Gr_{\mathrm{acc}}^2)$, i.e.
  $\lambda_{\mathrm J} = 2r_{\mathrm{acc}}$, and passes converging-flow,
  potential-minimum, Jeans-instability, boundedness and proximity checks
  ([Federrath et al. (2010)](/sources/federrath-2010.md), §2.2, eq. 32).
  Mathew & Federrath use the same threshold and the same checks, with
  $2r_{\mathrm{acc}} = 5h$ and $r_{\mathrm{acc}} = 250$ AU, and allow no new
  sink within 250 AU of an existing one (§§2.3, 5.2).
* **Accretion** of the mass above $\rho_{\mathrm{thr}}$, if bound and
  infalling (Federrath et al., §2.3). In the 2021 configuration mass,
  linear and angular momentum are updated at each accretion step, and
  "In order to conserve total angular momentum, an intrinsic angular
  momentum (spin) is introduced for the sink particle, which stores the
  accreted angular momentum"; the spin sets the outflow axis
  ([Mathew & Federrath (2021)](/sources/mathew-2021.md), §2.3). The 2010
  paper does not say whether its sinks carry spin (App. B, §2.3).
* **Gravity.** Federrath et al. split it four ways: multigrid gas–gas,
  cloud-in-cell gas-to-sink, direct-sum sink-to-gas and sink–sink, with
  cubic-spline softening (§2.4). Mathew & Federrath state that all sink
  interactions with the gas and between sinks are "calculated by direct
  summation over all the sink particles and grid cells", softened within
  the accretion radius (§§2.3, 5.2): a different wording of the gas-to-sink
  term, for a later code version.
* **Integration.** A variable-step leapfrog, subcycled for close
  encounters (Federrath et al., §2.5); "A second-order leapfrog
  integrator" (Mathew & Federrath, §2.3).

## Sub-grid modules in the 2021 configuration

From [Mathew & Federrath (2021)](/sources/mathew-2021.md):
* **Turbulence driving** (§2.2): a stochastic Ornstein–Uhlenbeck
  acceleration field added as a momentum and energy source, at wavenumbers
  1 to 3 (units of $2\pi$ over the box size), with a driving parameter of
  0.5 mixing compressive and solenoidal modes, driven continuously.
* **Polar radiative heating** (§2.5.1; Mathew & Federrath 2020): no
  radiative transfer is solved; an equilibrium heating temperature is
  computed from each sink's luminosity attenuated through an analytic
  disc model, and the pressure is the fourth-power sum of the polytropic
  and heating pressures, applied in the momentum equation.
* **Jets and outflows** (§2.5.2; Federrath et al. 2014): momentum
  injected in two cones of $30^\circ$ opening and radial extent $16h$,
  with smoothing "to prevent numerical artifacts"; ejected mass 0.3 of
  $\dot M\,\Delta t$, speed 100 km s$^{-1}$ times
  $(M_{\mathrm s}/0.5\,M_\odot)^{1/2}$, and 0.9 of the accreted angular
  momentum returned. Its resolution independence is cited, not tested.

## Parallelization and performance

* Federrath et al.'s turbulent-cluster run took about 10,300 CPU h on 128
  CPUs of HLRB-II, against about 2,400 CPU h on 16 CPUs for the SPH code;
  with about 30 times as many resolution elements, FLASH was 6–8× cheaper
  per element (§4.3.4, measured).
* [Stone et al. (2020)](/sources/stone-2020.md), §3.6.1, claim a per-core
  throughput for Athena++ above the public FLASH "in some cases by as much
  as a factor of 10" (no FLASH measurement printed).
* Mathew & Federrath report no performance numbers.

## Verification

From [Federrath et al. (2010)](/sources/federrath-2010.md), §§3–4: two-body
orbits (circular, elliptical, head-on), gas–sink gravity on a static
singular isothermal sphere, Bonnor–Ebert collapse, the
[singular isothermal sphere collapse](/benchmarks/singular-isothermal-sphere-collapse.md)
(accretion rate about $1.5\times10^{-4}\,M_\odot$ yr$^{-1}$ against
$1.45\times10^{-4}$), the Boss–Bodenheimer rotating core (angular momentum
conserved "to within 2%"), and a $100\,M_\odot$ turbulent cluster against
an SPH code (49 against 50 sinks at equal formation efficiency). The
module tests concern the sinks and gravity, not the MHD solver.

[Mathew & Federrath (2021)](/sources/mathew-2021.md) run no verification
test and no resolution study: two ensembles of ten turbulence
realizations at one resolution, identical except for the outflow module
(§3, Table 1).

## Limitations stated

* Mathew & Federrath name resolution as the main caveat: the peak of the
  sink mass distribution is overestimated by about 2, close binaries are
  unresolved, and about 10–20 AU would be needed to capture the peak if it
  is set by the first core (§6.1). They argue that ten realizations and
  sub-grid models give statistically converged results "in a
  cost-efficient way" (§§3, 6.2).
* Federrath et al. find it "hard to maintain perfect spherical symmetry
  for more than 10-100 sink particle orbits" with the multigrid potential
  (§3.2).

## Later uses (batch 6)

* **What the Berger & Colella citation covers.** The Mesh and AMR section
  records that Mathew & Federrath cite Berger & Colella (1989) for FLASH's
  AMR. The primary source, [Berger & Colella (1989)](/sources/berger-1989.md),
  describes logically rectangular patches of variable size, built by
  clustering flagged cells (bisection and merging under an efficiency
  threshold) and allowed to overlap on one level (§§2, 5), not the
  fixed-size blocks that [Stone et al. (2020)](/sources/stone-2020.md) and
  [Bryan et al. (2014)](/sources/bryan-2014.md) attribute to
  FLASH/PARAMESH. The citation names the AMR family; FLASH's block design
  is not the paper's. No FLASH source in this bundle states whether FLASH
  subcycles or how it corrects coarse–fine fluxes, so the agreement on
  those points cannot be checked. See
  [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

## Later uses (batch 8)

### The first version in its code paper

[Fryxell et al. (2000)](/sources/fryxell-2000.md) describe FLASH's
"first version" (Abstract, §9); the Fig. 22 caption names "FLASH 1.5" as
"the current development version". Everything in this subsection is from
that paper and concerns that version.

* **Code** (§§1, 6). A modular MPI code in single-program-multiple-data
  style for compressible reactive flow (X-ray bursts, classical novae,
  Type Ia supernovae). Modules and submodules carry inherited sources and
  stubs; a `setup` script assembles a build, with problem and system
  directories overriding sources by filename; runtime parameters are read
  as `variable = value`. Data are shared through common blocks, and
  Fortran 90 derived types are announced for the next version (§6,
  Figs. 21–23).
* **Mesh** (§2, Figs. 1–4). PARAMESH blocks of $N_{\mathrm b} = 8$ cells
  per direction with $n_{\mathrm g} = 4$ guard cells (PPM "requires four
  guard cells at each spatial boundary"), cell-centred data only, in an
  oct- or quad-tree; $r_{\mathrm{ref}} = 2$ and "a jump of no more than
  one refinement level across adjacent blocks"; guard cells at a
  refinement jump by quadratic interpolation; a work-weighted Morton-curve
  redistribution after each change of refinement. The memory overhead of
  identical blocks is "rarely more than about 30%". The authors class
  PARAMESH as block-structured AMR, "similar to" De Zeeuw & Powell (1993),
  and set it apart from Berger-style subgrids. See
  [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* **Refinement criterion** (§2, eqs. 1–3). Löhner's normalized second
  derivative with noise filter 0.01, on density, pressure and temperature,
  every four steps by default; a block refines above 0.8 and derefines
  below 0.2.
* **Hydrodynamics** (§3). Split, direct-Eulerian [PPM](/methods/ppm.md)
  from PROMETHEUS, with contact steepening (on density and composition),
  flattening (1 = first-order Godunov), characteristic tracing, a
  two-shock Riemann solver iterated by Newton–Raphson, and a secant
  iteration with the two adiabatic indices of Colella & Glaz for a general
  EOS (§§3.1–3.1.7); interface mass fractions are clipped and renormalized
  (§3.1.8). Sweeps alternate order every step; a Lapidus viscosity of
  coefficient 0.1 is added (§3.2). The scheme is "formally accurate to only
  second order in both space and time". See
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* **EOS** (§4). Gamma law, the analytic Nadyozhin EOS and the tabulated
  Helmholtz-free-energy EOS (recommended; thermodynamically consistent "to
  the limits of IEEE 64 bit arithmetic", about twice as fast as
  Nadyozhin), each called with temperature and density, the temperature
  found by Newton–Raphson "in two to four iterations". See
  [general equations of state](/methods/general-equation-of-state.md).
* **Nuclear burning** (§5). Hard-wired α-chain and hydrogen-burning
  networks (7, 13, 19 and 17 isotopes), integrated by a variable-order
  Bader–Deuflhard method with the MA28 sparse solver, operator split from
  the hydro.
* **Gravity.** Only an external field; the source is time-centred as the
  average of the old- and new-time products of density and acceleration
  (§3.1.8, eqs. 93, 96, read from the text layer only). Self-gravity is a
  future module (§9).
* **Verification** (§7). Hydro only, gamma law: advection of square and
  Gaussian pulses, the [Sod shock tube](/benchmarks/sod-shock-tube.md)
  (2–3 zones per discontinuity, 1–2 % errors, a few percent more along the
  diagonal, attributed to splitting), a strong shock tube, the
  [Sedov blast](/benchmarks/sedov-taylor-blast-wave.md) in 2D and 3D, the
  Woodward–Colella interacting blast waves (L1 self-convergence "only
  linear"), the Emery Mach 3 step and a shock crossing a forced refinement
  jump. No Courant number is printed.
* **Performance** (§8). On ASCI Red weak scaling is "nearly perfect ...
  up to 1024 processors when one processor per node is used"; AMR at fixed
  work scales worse than a uniform grid because guard-cell communication
  grows relative to computation; AMR beats the uniform grid "beyond a
  refinement level of six (corresponding to a uniform mesh with 512 cells
  per side)", and only while at most 60 % (2D) or 40 % (3D) of the mesh is
  maximally refined (§§8.2–8.4).

### Open points of this page answered

* **Reconstruction and time integrator** (introduction above). For the
  first version: split direct-Eulerian PPM with alternating sweeps (§3.2).
  The later configurations of Federrath et al. and Mathew & Federrath are
  still undescribed on this point.
* **Subcycling and coarse–fine fluxes** (Later uses, batch 6). The first
  version does not subcycle: "The FLASH code does not currently take
  advantage of this capability of PARAMESH" (§2), for reasons of memory
  and load balance, with no measurement. At a refinement jump the fine
  face fluxes are summed and replace the coarse flux (Fig. 4); area
  weighting is not stated. Later versions are not covered.
* **AMR family** (Mesh and AMR, Later uses batch 6). The authors' own
  classification is block-structured AMR, distinct from Berger's subgrids
  (§2). This agrees with [Stone et al. (2020)](/sources/stone-2020.md) and
  [Bryan et al. (2014)](/sources/bryan-2014.md), and confirms that the
  citation of Berger & Colella (1989) by Mathew & Federrath names the
  family, not FLASH's design.
* **Flattening convention** (Solvers, as described by Castro's authors).
  The primary source agrees: a coefficient of 0 leaves the edge values
  unchanged and 1 gives first-order Godunov (§3.1.3, eqs. 49–50).
* **Gravity time-centring** (Solvers, as described by Castro's authors).
  [Almgren et al. (2010)](/sources/almgren-2010.md) describe an
  extrapolation of the acceleration from $t^n$ and $t^{n-1}$; the first
  version has only an external field and time-centres the source as the
  average of old- and new-time products. Different code versions;
  Almgren et al. do not date their statement. A qualification, not a
  contradiction.
* **Non-ideal EOS tests** ([Coleman (2020)](/sources/coleman-2020.md)).
  The code paper agrees: all its tests use the gamma law, and general-EOS
  tests are deferred to "a subsequent paper" (§7).
* **Throughput comparison** ([Stone et al. (2020)](/sources/stone-2020.md),
  §3.6.1). The code paper prints no zone-cycles per second, so the
  factor-10 claim cannot be checked against it.
* **Language.** Fortran, with MPI; PARAMESH is "a package of FORTRAN 90
  subroutines" (§2).

## Later uses (batch 9)

The interacting-blast-wave run now has a benchmark page, [interacting blast waves](/benchmarks/interacting-blast-waves.md); Woodward & Colella's finest-pair rates are PPMDE 1.07, PPMLR 0.98, all others ≤ 0.85 (Table I), which agrees with "only PPM achieved even linear convergence". On the Emery step, Woodward & Colella (p. 131) give a corner treatment (four plus two zones reset to the corner entropy and enthalpy) whose absence produces the numerical boundary layer and spurious Mach reflections that FLASH reports.

# Citations

1. [Federrath et al. (2010)](/sources/federrath-2010.md), §§2.1–2.5, 3–4, 4.2.1, 4.3.4, eqs. 14, 20, 30–32, App. B (arXiv v2).
2. [Mathew & Federrath (2021)](/sources/mathew-2021.md), §§2.1–2.6, 3, 5.2, 6.1–6.2, Table 1 (arXiv v2).
3. [Stone et al. (2020)](/sources/stone-2020.md), §§2.2, 3.6.1.
4. [Bryan et al. (2014)](/sources/bryan-2014.md), §1 (arXiv v1).
5. [Almgren et al. (2010)](/sources/almgren-2010.md), §§5.1–5.2, 8.6 (arXiv v1 numbering).
6. [Tomida & Stone (2023)](/sources/tomida-2023.md), footnote 4 (arXiv v1).
7. [Coleman (2020)](/sources/coleman-2020.md), §1 (arXiv v3).
8. [Berger & Colella (1989)](/sources/berger-1989.md), §§2, 5.
9. [Fryxell et al. (2000)](/sources/fryxell-2000.md), §§1–9, eqs. 1–3, 25–26, 33–53, 93, 96, Figs. 1–4, 22.
10. [Woodward & Colella (1984)](/sources/woodward-1984.md), p. 131, Table I.
