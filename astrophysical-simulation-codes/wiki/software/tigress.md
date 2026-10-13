---
type: Software
title: "TIGRESS (Athena framework for the star-forming shearing-box ISM)"
description: "Set of physics modules in the Athena MHD code for a vertically stratified, self-gravitating, magnetized shearing-box patch of a galactic disc: implicit sub-cycled cooling with time-variable FUV heating, Larson–Penston-threshold sink/star particles with a symplectic shearing-box integrator, stochastic supernovae with a resolution-adaptive three-way feedback prescription, verified by module unit tests and a 2–64 pc resolution study."
status: established
aliases: [TIGRESS, Three-phase Interstellar medium in Galaxies Resolving Evolution with Star formation and Supernova feedback]
tags: [software, mhd, sink-particles, cooling, self-gravity, constrained-transport, riemann-solver, time-integration, verification]
timestamp: 2026-10-12T00:00:00Z
---

# TIGRESS

TIGRESS ("Three-phase Interstellar medium in Galaxies Resolving Evolution
with Star formation and Supernova feedback") is not a standalone code but a
set of physics modules built into [Athena](/software/athena.md). It
simulates a local, vertically stratified shearing-box patch of a galactic
disc containing the self-gravitating, magnetized, three-phase interstellar
medium (ISM), with star formation and supernova (SN) feedback computed
self-consistently ([Kim & Ostriker (2017)](/sources/kim-2017.md), abstract,
§2). The named contributions are the sink/star particle module, the
time-variable heating, the SN event generator and the SN feedback
prescription; each has a unit test (§2).

## Code

* Host code: Athena (Stone et al. 2008); the software statement also lists
  STARBURST99 for population synthesis and Python analysis tools (yt,
  astropy, numpy and others) (p. 32).
* No Athena version, no code-availability statement for the TIGRESS
  modules, and no wall-clock, core-hour or scaling figures are printed.
  The runs used Princeton's "TIGRESS" cluster and NASA NAS.

## Equations

Ideal MHD in a local shearing box (Gaussian units in the paper): continuity
$\partial_t\rho + \nabla\cdot(\rho\mathbf v) = 0$; momentum with Coriolis
force and the gradient of a total potential (self-gravity, a fixed
external potential of stellar disc and dark matter, and the tidal potential
of the rotating frame); total energy with the same potential terms and a
net cooling sink, the cooling rate minus the photoelectric heating rate;
induction $\partial_t\mathbf B = \nabla\times(\mathbf v\times\mathbf B)$;
and Poisson's equation $\nabla^2\Phi = 4\pi G\rho$ with the particle
density added to $\rho$ (§2.1, eqs. 1–6). The logarithmic shear rate of
the rotation curve is 1. Particle mass is deposited on the nearest $3^3$
cells by triangular-shaped-cloud (TSC) assignment. There is no explicit
conduction, viscosity or Ohmic resistivity (§2.1).

## Hydrodynamics and gravity

From [Kim & Ostriker (2017)](/sources/kim-2017.md), §2.1:
* Athena's directionally unsplit Godunov scheme with
  [constrained transport](/methods/constrained-transport.md), using the van
  Leer predictor–corrector of Stone & Gardiner (2009), piecewise-linear
  reconstruction and the Roe solver (see
  [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md),
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
* **H-correction** (Sanders et al. 1998) "when the difference in signal
  speed is larger than 20 km s⁻¹", against the carbuncle in SN blast waves.
* **First-order flux correction** (Lemaster & Stone 2009) "to cells with
  negative pressure and/or density after the second-order update", which
  strong rarefactions in the turbulence can produce. The fallback flux and
  reconstruction are not stated.
* Self-gravity by FFT, with shearing-periodic horizontal boundaries (Gammie
  2001) and vacuum vertical boundaries (Koyama & Ostriker 2009); uniform
  grid, no mesh refinement.

## Cooling and heating

* Net cooling is "solved fully implicitly in an operator-split manner
  before the integrator step", sub-cycled when the cooling time, thermal
  energy over net cooling rate, is shorter than $\Delta t$, with "an
  adaptive time step corresponding to the instantaneous cooling time"
  (§2.1). The root-finder and tolerance are not stated. See
  [cooling integration](/methods/radiative-cooling-integration.md).
* $\Lambda(T)$: the Koyama & Inutsuka (2002) fit below $10^{4.2}$ K and
  Sutherland & Dopita (1993) collisional-ionization-equilibrium cooling at
  solar metallicity above (§2.1, Fig. 1).
* $\mu(T)$ is interpolated between 1.295 (atomic) and 0.618 (ionized) and
  found "iteratively for a given pair of P and ρ". No chemistry and no
  molecular gas (§2.1).
* FUV photoelectric heating is uniform in space and varies in time with
  the FUV luminosity of the star particles (STARBURST99, Kroupa IMF),
  scaled down in ionized gas through $\mu(T)$ (§2.3.1, eq. 24). There is
  no radiative transfer; ray tracing is "underway" (footnote 1).

## Sink/star particles

A modified Gong & Ostriker (2013) scheme (§2.2); see
[sink particles](/methods/sink-particles.md).
* **Creation** (§2.2.1, eq. 7): density above the Larson–Penston threshold
  $\rho_{\mathrm{thr}} = 8.86\,c_s^2/(\pi Gh^2)$, with $c_s$ here the
  isothermal sound speed $(p/\rho)^{1/2}$; a potential minimum over the
  $3^3$ control volume; convergence along every axis, "not simply
  ∇·v < 0". Control-volume radius $1.5h$; no creation within twice that of
  another particle. No Jeans-instability or boundedness checks (see the
  [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md)).
* **Accretion** (§2.2.2, eqs. 9–11): only when the particle-frame mass
  fluxes on the control-volume faces converge along all three axes, at
  $t^{n+1/2}$; the accreted mass and momentum are the Riemann fluxes
  through the control-volume boundary plus the change of the control volume
  when the particle crosses cells. Accretion stops at the particle's first
  SN. Merging within twice the control radius.
* **Ageing** (§2.2.3–2.2.4, eq. 12): particles are "growing" (younger than
  about 4 Myr), "feedback" (to 40 Myr), "passive" or massless "runaway";
  the mean age is mass-weighted on accretion.
* **Integrator** (§2.2.5, eqs. 13–21): explicit, implicit and semi-implicit
  kick–drift–kick "are not symplectic in a shearing box"; the code uses the
  Quinn et al. (2010) symplectic integrator generalized to an arbitrary
  shear rate. Each step starts with the previous step's second kick,
  because self-gravity at $t^{n+1}$ needs the updated gas, and positions
  are advanced before the MHD step.

## Supernova feedback

* **Events** (§2.3.2, eqs. 25–27): a particle fires a SN when its expected
  number per step exceeds a uniform random number; one SN per 95.5
  $M_\odot$ of new stars. Runaway OB stars from binaries (binary fraction
  2/3) are launched with velocities after Eldridge et al. (2011). Type Ia
  SNe are neglected.
* **Prescription** (§2.3.3). The feedback radius starts at $3h$ and grows
  by $h/2$; the ratio of the enclosed mass (gas plus 10 $M_\odot$ of
  ejecta) to the shell-formation mass of Kim & Ostriker (2015a) selects:
  momentum injection if the ratio exceeds 1 at the smallest radius;
  $10^{51}$ erg injected as about 72% thermal and 28% kinetic (Sedov–Taylor
  stage) if it lies between 0.027 and 1; pure kinetic ejecta if it stays
  below 0.027 at the largest radius. The energy modes first reset the
  region to its mean density, momentum and internal energy. The 0.027
  criterion corresponds to a cell size one tenth of the shell-formation
  radius at a feedback radius $3h$; a ratio near 1 (cell size about one
  third of that radius) is "marginal" and "unsafe" without the reset,
  because of overcooling.

## Verification

From [Kim & Ostriker (2017)](/sources/kim-2017.md):
* **Non-isothermal sphere collapse** (§2.2.1, Fig. 2), at $h = 0.031$ and
  0.078 pc: the profile approaches Larson–Penston with infall near $-3$
  times the isothermal sound speed; with the sink criterion both
  resolutions give "essentially the same" profiles, without it
  "unphysical overshoots of density and out-of-equilibrium temperature"
  appear. Qualitative.
* **Epicyclic orbit** (§2.2.5, Fig. 4): the Quinn et al. integrator
  conserves orbit energy and has smaller phase errors than semi-implicit
  kick–drift–kick; the mean phase error converges at second order in
  $\Delta t$.
* **Single radiative SN remnant** (§2.3.3, Fig. 6), $h = 4$ pc: the final
  momentum is within 25% of the Kim & Ostriker (2015a) fit "for all values
  of the density"; pure thermal injection underestimates and pure kinetic
  injection overestimates it in unresolved remnants. This is a radiative
  remnant measured by final momentum, not the adiabatic Sedov–Taylor
  benchmark.
* **Resolution study** (§4, Figs. 13–18): Solar-neighbourhood models at
  $h$ = 2, 4, 8, 16, 32 and 64 pc. The verdict: "all these ISM properties
  are converged at ∆x ≤ 8 pc", while "At low resolution (∆x ≥ 16 pc), the
  detailed ISM properties as well as the mean SFR cannot be properly
  captured" (abstract, §5). Some quantities (velocity dispersion, scale
  height) converge already at 16 pc; at 64 pc the star formation rate is
  "several times larger" and the gas undergoes "thermal runaway". Recorded
  as printed: the Fig. 14, 16 and 17 captions put convergence at
  $h \le 16$ pc, the abstract, §5 and the Fig. 18 caption at 8 pc.
* **Resolution and SN treatment** (§2.2.1, §4, Fig. 3, footnote 6): collapse
  is captured in Solar-neighbourhood conditions only for $h < 20$ pc;
  instantaneous sink-to-star conversion is stated valid up to $h = 8$ pc;
  when overlapping remnants were forbidden, low-resolution runs diverged
  the other way, and "with insufficient resolution, the ISM properties
  fail to converge in unpredictable ways."

## Stated limitations

* The resolution requirements are "particular to the Solar neighborhood
  model"; denser environments need finer cells (§5).
* Numerical diffusion acts as a "numerical conductivity" larger than the
  physical one, thickening the cold/warm interface and shifting phase
  fractions at low resolution; for this reason the cold and unstable
  phases are combined in the convergence measures (§3, footnote 4).
* No radiative transfer, chemistry, Type Ia SNe or explicit diffusion
  (§2.1, §2.3).

# Citations

1. [Kim & Ostriker (2017)](/sources/kim-2017.md), abstract, §§2–5,
   eqs. 1–27, Figs. 1–18, footnotes 1, 4, 6 (arXiv v2).
