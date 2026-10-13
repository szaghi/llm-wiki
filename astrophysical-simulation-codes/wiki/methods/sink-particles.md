---
type: Method
title: "Sink particles in Eulerian grid codes"
description: "Lagrangian accreting point masses that replace unresolvable gravitational collapse on a grid: creation where gas exceeds a Jeans-derived density threshold (alone, or with converging-flow, potential-minimum, Jeans-instability and boundedness checks), accretion by a Bondi–Hoyle rate or of the bound mass above the threshold, softened gas–particle gravity, particle time-step limits with sub-cycling, and merging."
status: established
aliases: [sink particle, accreting sink particle, Lagrangian sink particle, sinks]
tags: [self-gravity, amr, conservation, time-integration, sink-particles]
timestamp: 2026-10-12T00:00:00Z
---

# Sink particles in Eulerian grid codes

A sink particle is a point mass that replaces gas whose gravitational
collapse can no longer be resolved, accretes from the grid and moves
under gravity. [Krumholz et al. (2004)](/sources/krumholz-2004.md)
introduced moving, accreting sink particles in an Eulerian (AMR or fixed)
grid; before them Eulerian codes had fixed sink cells (Boss & Black 1982),
and SPH had sink particles (Bate et al. 1995).
[Federrath et al. (2010)](/sources/federrath-2010.md) add them to the
block-AMR code FLASH as a subgrid model that cuts off runaway collapse
"in a controlled fashion" once the
[Jeans resolution criterion](/definitions/jeans-resolution-criterion.md)
can no longer be met at the finest level (§1, §2.2.1). Both argue against
the alternative of stiffening the equation of state ("Jeans heating"),
which heats gas that should stay isothermal and shocked gas that is not
collapsing, and shrinks the Courant step
([Federrath et al. (2010)](/sources/federrath-2010.md), §1).

The two implementations, in the notation of the
[registry](/notation.md) ($M_{\mathrm s}$ sink mass, $r_{\mathrm{acc}}$
accretion radius, $\rho_{\mathrm{thr}}$ density threshold):

| | [Krumholz et al. (2004)](/sources/krumholz-2004.md) | [Federrath et al. (2010)](/sources/federrath-2010.md) |
|---|---|---|
| host | unnamed Berkeley/LLNL 3D AMR code (Godunov, multigrid, subcycled) | FLASH (block AMR, multigrid) |
| creation | density above $\rho_{\mathrm{thr}}$ at $N_{\mathrm J} = 4$ | density above $\rho_{\mathrm{thr}}$ plus five more checks |
| $r_{\mathrm{acc}}$ | $4h$ | about $2.5h$ |
| accretion | Bondi–Hoyle rate, kernel-weighted, angular-momentum filter | bound, infalling mass above $\rho_{\mathrm{thr}}$ |
| gas → sink gravity | softened direct sum over cells | interpolated mesh acceleration (cloud-in-cell) |
| sink → gas gravity | not stated | direct sum, spline-softened |
| sink orbits | Bulirsch–Stoer, unsoftened | leapfrog, sub-cycled, spline-softened |
| merging | friends-of-friends within $r_{\mathrm{acc}}$, every step | optional, if bound and converging |

## Creation

**Density threshold.** Both derive the threshold from the Jeans length
$\lambda_{\mathrm J} = \sqrt{\pi c_s^2/(G\rho)}$ at the finest cell size $h$.
* Krumholz et al. create a sink in any cell where
  $\rho > \rho_{\mathrm{thr}} = \pi c_s^2/(N_{\mathrm J}^2 G h^2)$ with
  $N_{\mathrm J} = 4$, i.e. the Truelove condition (their Truelove number 0.25 $= 1/N_{\mathrm J}$), at the
  cell centre with mass $(\rho - \rho_{\mathrm{thr}})h^3$ and a
  proportional share of momentum and energy, leaving the cell at the
  threshold (§2.2, eqs. 5–7). A Jeans-violating cell holds more than about
  $0.07$ Bonnor–Ebert masses, so a sink can form in a stable region; the
  check is ex post facto (such a sink stays tiny) and the remedy is a
  rerun at higher resolution (§2.2, eqs. 8–9).
* Federrath et al. set $\rho_{\mathrm{thr}} = \pi c_s^2/(4Gr_{\mathrm{acc}}^2)$,
  i.e. $\lambda_{\mathrm J} = 2r_{\mathrm{acc}}$ (eq. 32), with
  $r_{\mathrm{acc}}\simeq2.5h$ so that $\lambda_{\mathrm J}$ is resolved
  by 5 cells at the finest level (§4.2.1).

**Further checks** ([Federrath et al. (2010)](/sources/federrath-2010.md),
§2.2, eqs. 3–12). The gas in a spherical control volume of radius
$r_{\mathrm{acc}}$ around a cell above the threshold must also be
1. on the finest refinement level;
2. converging along **each** principal axis toward the centre, not only
   in total divergence as in Krumholz et al.;
3. at a minimum of the potential at the centre;
4. Jeans-unstable: gravitational energy above twice the thermal energy,
   with the magnetic energy added to the thermal side when fields are
   present;
5. bound: gravitational, thermal, kinetic (relative to the centre of mass)
   and magnetic energies sum to a negative value;
6. outside $r_{\mathrm{acc}}$ of every existing sink.

The order "does not matter"; the cheapest run first. The new sink takes
the control-volume gas and sits at its centre of mass. In test runs the
potential-minimum check alone "prevents almost all spurious sink
particles"; the Jeans and boundedness checks remain necessary in
shock-dominated, high-dispersion flows and with magnetic fields
(§2.2.8; qualitative, no numbers).

**Why the checks** (§2.2.8, §4.3, §5). A density threshold alone creates
spurious sinks in supersonic turbulence whenever it lies below the
opacity limit (about $10^{-14}$ g cm$^{-3}$), because shocks exceed it
without the gas being bound. Krumholz et al. (2004), Wang et al. (2010)
and Padoan & Nordlund (2009) use a threshold plus a converging-flow check
(and, for the two AMR codes, a refinement check); "a significantly larger
number of sink particles is typically created", which the first two
absorb by merging. In the turbulent cluster test, a threshold-only FLASH
run overestimates the number of fragments "by more than one order of
magnitude" and the accreted mass by 133%, 51%, 19% and 14% at
$t/t_{\mathrm{ff}} = 0.8$, 0.9, 1.0 and 1.1 (§4.3, Fig. 14). This is
Federrath et al.'s assessment; Krumholz et al. do not run a turbulent
test.

## Accretion

**Bondi–Hoyle rate** ([Krumholz et al. (2004)](/sources/krumholz-2004.md),
§2.4, eqs. 10–15). With the Bondi–Hoyle radius
$r_{\mathrm{BH}} = GM_{\mathrm s}/(v_\infty^2 + c_{s,\infty}^2)$, the rate is
the Ruffert interpolation
$$\dot M = 4\pi\rho_\infty r_{\mathrm{BH}}^2\left(\lambda_{\mathrm B}^2c_{s,\infty}^2 + v_\infty^2\right)^{1/2},\qquad \lambda_{\mathrm B} = \exp(3/2)/4\approx1.120,$$
with $v_\infty$ the sink velocity relative to its host cell and
$c_{s,\infty}$ the host-cell sound speed. $\rho_\infty$ is the
kernel-weighted mean density in the accretion zone divided by the Bondi
density profile at $1.2h/r_{\mathrm{BH}}$; the factor 1.2 is empirical.
* The zone is every cell within $r_{\mathrm{acc}} = 4h$ ("based on
  experiments"), weighted by $\exp(-r^2/r_K^2)$, $r$ the distance from the sink, with a kernel radius
  between $h/4$ and $r_{\mathrm{acc}}/2$ set by $r_{\mathrm{BH}}$.
* **Angular-momentum filter**: each cell is split into $8^3$ ballistic
  test particles, and the cell's share is reduced by the fraction whose
  closest approach exceeds $h/4$ (eq. 15; recorded as printed, the
  closest-approach formula is dimensionally inconsistent in the preprint).
  At most 25% of a cell's mass may be removed per step.
* Only the radial part of each cell's momentum in the sink frame is
  removed, so the gas keeps its angular momentum and the sink accretes
  none; the sink takes the opposite momentum change, and the specific
  thermal energy is held fixed. The authors claim this "conserves mass,
  momentum, and angular momentum to machine precision" (asserted, no
  measurement); total energy is not claimed.
* **Self-correction** (§3.3): if the formula misestimates the rate, gas
  piles up in or drains from the zone, $\rho_\infty$ adjusts, and the rate
  converges to what the hydrodynamics delivers, so formula details matter
  little when $r_{\mathrm{BH}}$ is resolved (argued, supported by the
  Mach-3 test below).
* **Failure mode** (§3.2, §5): the error peaks when the Bondi radius is
  comparable to $r_{\mathrm{acc}}$ (up to 24%, Table 1); "one ought not
  use it in cases where the flow at the sink particle is transitioning
  from subsonic to supersonic". With AMR one can refine until the Bondi
  radius exceeds $r_{\mathrm{acc}}$.

**Mass above the threshold** ([Federrath et al. (2010)](/sources/federrath-2010.md),
§2.3, eq. 13). A cell inside $r_{\mathrm{acc}}$ offers
$(\rho - \rho_{\mathrm{thr}})$ times its volume. The increment is accreted
only if it is bound to the sink plus the remaining gas inside
$r_{\mathrm{acc}}$ and has negative radial velocity; where accretion radii
overlap it goes to the sink to which it is most strongly bound. Inside an
inner radius covering only the central cell, gas is accreted unchecked.
Cells inside $r_{\mathrm{acc}}$ are thus left at $\rho_{\mathrm{thr}}$.
Accretion conserves mass and linear momentum, the sink being moved to the
centre of mass of the particle–gas system.

**Angular momentum** ([Federrath et al. (2010)](/sources/federrath-2010.md),
App. B, eqs. B1–B6; elementary proof). Mass and linear momentum of an
accretion or merger event are conserved by construction, but angular
momentum in general is not: conservation requires a position condition
that cannot hold when the angular momentum is not orthogonal to the
centre-of-mass velocity, and placing the sink at the centre of mass does
not satisfy it. "This is the case for any implementation of accreting
sink particles"; the only fix is an intrinsic sink spin. Recorded as
printed: §2.3 states that the FLASH accretion conserves angular momentum,
App. B that it cannot without spin, and the paper does not say whether
the FLASH sinks carry spin. The rotating-core test conserves it "to
within 2%" (§3.5).

## Gravity and motion

* **Krumholz et al.** (§2.5, eqs. 16–17): gas acts on a sink through a
  Plummer-softened direct sum over cells, softening $2h$ for
  $r_{\mathrm{acc}} = 4h$, with the host cell and its neighbours split
  into $8^3$ points; sink–sink orbits are integrated over $\Delta t$ by
  adaptive Bulirsch–Stoer with error control, unsoftened. Time step:
  $\max|\mathbf v_{\mathrm s}|\Delta t < 0.5h$, "usually less stringent"
  than the gas Courant condition. How sink gravity acts on the gas, and
  where accretion and the kick sit in the hydro step, are **not stated**.
  A binary with eccentricity 0.998 keeps its semi-major axis to about 1%
  and eccentricity to about 0.1% over several orbits.
* **Federrath et al.** (§2.4–§2.5, eqs. 14–23, App. A): gas–gas gravity by
  the multigrid Poisson solve; gas → sink by first-order cloud-in-cell
  interpolation of the mesh acceleration (TSC or tricubic gave no
  significant difference); sink → gas and sink–sink by direct sums. Sink
  potentials are **not** in the Poisson source. Softening is the cubic
  spline of Monaghan & Lattanzio (1985), exactly Newtonian beyond
  $r_{\mathrm{soft}}$ (set to $r_{\mathrm{acc}}$ in the cluster run). The
  sinks→gas direct sum cost was negligible up to $10^3$ sinks. Leapfrog
  with four step limits (Courant; gas acceleration; a sink moves at most
  half a cell; sink–sink acceleration). The last was measured up to three
  orders of magnitude below the others, so the sinks are **sub-cycled**
  with the gas frozen, which the paper calls "absolutely necessary" (§2.5,
  §3.1).
* **Orbit tests** (Federrath et al., §3.1, Figs. 2–4): a circular binary
  stays circular for 1000 orbits; an elliptical one shows about 1°
  perihelion shift after about 100 orbits with sub-cycling and about 21°
  after ten orbits without it; a softened pass-through pair conserves
  energy over 1000 oscillations with sub-cycling and escapes after about
  68 without.
* **Gas → sink on AMR** (§3.2, Figs. 5–6): test sinks orbiting in a static
  singular isothermal sphere have circular velocities 1–2% below analytic;
  orbits broaden after about 100 inner orbits as the multigrid potential
  loses spherical symmetry near the Cartesian boundaries.

## Merging

Krumholz et al. group all sinks by friends-of-friends with linking length
$r_{\mathrm{acc}}$ at the end of each step and replace each group by one
particle at its centre of mass; the merger radius must be at least the
accretion radius, because overlapping accretion zones are undefined
(§2.3, §2.4.2). Federrath et al. merge optionally, when each sink lies
within the other's $r_{\mathrm{acc}}$ and the pair is bound and
converging; the merged sink inherits linear and angular momentum (§3.5).

## Tests

* [Singular isothermal sphere collapse](/benchmarks/singular-isothermal-sphere-collapse.md):
  accretion rates within about 1% (Krumholz et al., §3.1) and about 3%
  (Federrath et al., §3.4) of the Shu (1977) value.
* **Bondi accretion** at $r_{\mathrm B}/h$ from 0.1 to 10: errors $+1.1\%$,
  $-0.6\%$, $-12.2\%$, $-24.4\%$ and $-2.3\%$ (Krumholz et al., §3.2,
  Table 1); single source.
* **Mach-3 Bondi–Hoyle accretion** with finest cells $r_{\mathrm{BH}}/50$:
  mean rate $1.17$ times the formula after about six Bondi–Hoyle times, in
  agreement with Ruffert (1996) (Krumholz et al., §3.3); single source.
* **Keplerian disc** around a sink: the evacuated inner region is slightly
  smaller with accretion than without, so the sink adds no artificial
  angular-momentum transport (Krumholz et al., §3.4.1, Fig. 6); a fitted
  numerical-viscosity law for the Cartesian code follows (§3.4.2).
* **Bonnor–Ebert sphere** and **Boss–Bodenheimer rotating core**
  (Federrath et al., §§3.3, 3.5): qualitative agreement with earlier work;
  in the core, two sinks form at $1.26\,t_{\mathrm{ff}}$ and merge later.
* **Turbulent cluster, FLASH versus SPH** (Federrath et al., §4):
  $100\,M_\odot$, rms Mach about 4.5, same $\rho_{\mathrm{thr}}$ and
  $r_{\mathrm{acc}}$ (490 AU) in both codes. At $t/t_{\mathrm{ff}} = 1.1$
  FLASH has 49 sinks and $26.3\,M_\odot$ accreted, SPH 61 and
  $36.7\,M_\odot$; compared at equal formation efficiency (about 26%) the
  counts are 49 and 50 with a KS probability of 55%. FLASH used about
  10,300 CPU h on 128 CPUs and SPH about 2,400 on 16, but FLASH is 6–8×
  cheaper per resolution element.

Neither paper reports a convergence study in $r_{\mathrm{acc}}$ or
$N_{\mathrm J}$.

## Later uses (batch 4)

Two later implementations, one in a different host code and one a later
configuration of the FLASH module:

| | [Kim & Ostriker (2017)](/sources/kim-2017.md) | [Mathew & Federrath (2021)](/sources/mathew-2021.md) |
|---|---|---|
| host | [TIGRESS](/software/tigress.md) in [Athena](/software/athena.md): uniform grid, shearing box, FFT gravity | [FLASH](/software/flash.md) 4: PARAMESH block AMR, multigrid gravity |
| creation | Larson–Penston threshold, potential minimum, convergence along every axis | $\rho_{\mathrm{thr}} = \pi c_s^2/(4Gr_{\mathrm{acc}}^2)$ plus the checks of Federrath et al. (2010) |
| $r_{\mathrm{acc}}$ | control volume of $3^3$ cells, radius $1.5h$ | $2.5h$ ($2r_{\mathrm{acc}} = 5h$), 250 AU |
| accretion | Riemann mass and momentum fluxes through the control-volume boundary, only under three-axis convergence | mass, linear and angular momentum updated each accretion step; sink moved to the centre of mass |
| gravity | particle mass deposited by TSC into the Poisson source | "direct summation over all the sink particles and grid cells"; softened within $r_{\mathrm{acc}}$ |
| sink orbits | Quinn et al. (2010) symplectic kick–drift–kick, generalized to shear | second-order leapfrog |
| merging | within twice the control radius, at the centre of mass | not stated |
| spin | not stated | intrinsic spin |

### TIGRESS (Kim & Ostriker 2017)

From [Kim & Ostriker (2017)](/sources/kim-2017.md), §2.2, a modified
Gong & Ostriker (2013) scheme:
* **Threshold** (§2.2.1, eq. 7): the Larson–Penston density at half a
  cell, $\rho_{\mathrm{thr}} = 8.86\,c_s^2/(\pi Gh^2)$, with $c_s$ the
  isothermal sound speed $(p/\rho)^{1/2}$. Rationale: the Larson–Penston
  solution is an attractor of collapse for arbitrary turbulent flows, and
  its asymptote guarantees supersonic infall at $-3.28$ times the
  isothermal sound speed. The paper notes that the Truelove threshold has
  "the same parameter dependence, but with a coefficient of π/16 instead
  of 8.86/π"; the ratio of the printed coefficients (computed here, not
  stated) is about 14, so this threshold is about 14 times the
  $N_{\mathrm J} = 4$ density bound of Krumholz et al.
* **Checks.** Convergence is required along every axis, "not simply
  ∇·v < 0", which agrees with check 2 of Federrath et al. above; a
  potential minimum over the control volume agrees with check 3; no
  creation within twice the control radius of an existing particle
  corresponds to check 6. Of the potential-minimum and convergence checks
  the authors note that "if the resolution is high enough, the additional
  criteria are essentially always satisfied (see GO13)". The
  Jeans-instability and boundedness checks (4 and 5) are absent and not
  discussed.
* **Creation step.** The control volume is reset like ghost zones (face,
  side and corner cells average 1, 2 and 3 contact cells, the host cell
  6), with the shear velocity removed before averaging and restored
  after; magnetic fields are not reset; the particle takes the mass and
  momentum difference.
* **Accretion** (§2.2.2, eqs. 9–11): the face-summed, particle-frame mass
  fluxes must point into the control volume on both sides along all three
  axes, evaluated at $t^{n+1/2}$; mass and momentum accretion are the
  Riemann fluxes through the control-volume boundary, plus the change of
  control volume when the particle crosses cells. Particle positions are
  advanced before the MHD step to preserve Galilean invariance. Accretion
  stops at the particle's first supernova.
* **Gravity and orbits.** Particle density enters the Poisson source by
  TSC deposition on $3^3$ cells (§2.1), unlike Federrath et al., whose
  sink potentials are not in the Poisson source. Explicit, implicit and
  semi-implicit kick–drift–kick "are not symplectic in a shearing box";
  the Quinn et al. (2010) integrator is used, and each step starts with the
  previous step's second kick because self-gravity at $t^{n+1}$ needs the
  updated gas (§2.2.5). In the epicyclic-orbit test it conserves energy
  where explicit and implicit kick–drift–kick drift secularly, and its
  mean phase error converges at second order in $\Delta t$ (Fig. 4).
* **Tests.** In a collapsing non-isothermal sphere at $h = 0.031$ and
  0.078 pc, the sink criterion gives "essentially the same" profiles at
  both resolutions, while without sinks "unphysical overshoots of density
  and out-of-equilibrium temperature" appear (§2.2.1, Fig. 2;
  qualitative). The control radius is not varied; the paper's resolution
  study (2 to 64 pc) is of the whole ISM system (see
  [TIGRESS](/software/tigress.md)).
* **Spurious sinks: an open question, not a contradiction.** Federrath
  et al. (2010) state that the Jeans and boundedness checks remain
  necessary in shock-dominated, high-dispersion flows, that "magnetic
  effects are not taken into account by the potential minimum check, but
  are covered with the Jeans instability and bound state checks", and that
  the extra checks "are only necessary, if sink particles are created at
  densities below the opacity limit (about $10^{-14}$ g cm$^{-3}$)"
  (§2.2); they measure a large excess of sinks with a threshold alone
  (§4.3). TIGRESS creates sinks far below the opacity limit, in
  magnetized, supernova-driven turbulence, without those two checks, so it
  is in the regime where Federrath et al. call them necessary. Kim &
  Ostriker make no counter-claim and report no spurious-sink test; no
  source measures spurious sinks in this scheme.

### FLASH, later configuration (Mathew & Federrath 2021)

From [Mathew & Federrath (2021)](/sources/mathew-2021.md), §2.3, a
production star-cluster configuration of the FLASH sinks:
* $\rho_{\mathrm{thr}} = \pi c_s^2/(G\lambda_{\mathrm J}^2) = \pi c_s^2/(4Gr_{\mathrm{acc}}^2)$
  with $r_{\mathrm{acc}} = \lambda_{\mathrm J}/2$ (eq. 4), plus "a series of
  tests as described by" Federrath et al. (2010; cited there as 2010c).
  $2r_{\mathrm{acc}} = 5h$ at the finest level, which "ensures that the
  Truelove et al. (1997) criterion is satisfied", with $h = 100$ AU and
  $r_{\mathrm{acc}} = 250$ AU; this agrees with the $r_{\mathrm{acc}}\simeq2.5h$
  of Federrath et al. above. Recorded as printed: Table 1 gives
  $\rho_{\mathrm{thr}} = 3.8\times10^{-16}$ g cm⁻³, while eq. 4 with the
  printed $c_s = 0.2$ km s⁻¹ and $r_{\mathrm{acc}} = 250$ AU gives about
  $3.4\times10^{-16}$ (recomputed at ingestion; the paper does not
  explain the difference).
* **Spin.** "In order to conserve total angular momentum, an intrinsic
  angular momentum (spin) is introduced for the sink particle, which stores
  the accreted angular momentum"; the spin sets the axis of the sub-grid
  outflow module, which returns a fraction 0.9 of the accreted angular
  momentum to the outflow (§2.3, §2.5.2). This answers, for the 2021 FLASH
  configuration (following Federrath et al. 2014), the open note above that
  Federrath et al. (2010) do not say whether the FLASH sinks carry spin; it
  agrees with their App. B argument that spin is required. It does not
  document the 2010 module itself.
* **Gravity.** Sink–gas and sink–sink interactions are "calculated by
  direct summation over all the sink particles and grid cells", with the
  potential "softened within the accretion radius" (§2.3, §5.2), and the
  sinks are advanced by "A second-order leapfrog integrator". The wording
  reads as a direct sum also for gas → sink, where Federrath et al. (2010)
  interpolate the mesh acceleration by cloud-in-cell. Different code
  versions and terse wording: recorded as stated differently, not as a
  contradiction.
* No new sink forms within 250 AU of an existing one (§5.2), as in check 6.
* **No convergence study.** One resolution ($h = 100$ AU); the authors
  name resolution as the main caveat (peak of the mass distribution
  overestimated by about 2, close binaries unresolved; §6.1), and call the
  separation distribution below about 200 AU "only a lower limit" (§5.2).
  Neither batch-4 paper varies $r_{\mathrm{acc}}$ or $N_{\mathrm J}$.

## Contradictions

* **Angular momentum of accretion.** *Open.*
  [Federrath et al. (2010)](/sources/federrath-2010.md), App. B, state
  that angular momentum cannot in general be conserved by "any
  implementation of accreting sink particles" without an intrinsic spin,
  and list Krumholz et al. (2004) among the implementations that carry
  one. [Krumholz et al. (2004)](/sources/krumholz-2004.md), §2.4.2 (arXiv
  preprint read), describe no sink spin; they remove only radial momentum,
  leave the angular momentum in the gas, and assert conservation of mass,
  momentum and angular momentum to machine precision, without a
  measurement. The two statements disagree on what the 2004 scheme does;
  the published 2004 text has not been checked. *Compiler hypothesis,
  not a source claim:* the 2004 claim can be checked algebraically, since
  radial kicks to the gas and the opposite kick to the sink both act along
  lines through the sink and so cancel in the total angular momentum
  without any spin. The entry closes on the published 2004 text or by the
  human.
  * *Later evidence (batch 4), not closing.*
    [Mathew & Federrath (2021)](/sources/mathew-2021.md), §2.3, state that
    the (later) FLASH sinks carry an intrinsic spin "In order to conserve
    total angular momentum". This agrees with the App. B argument of
    Federrath et al. for FLASH, but says nothing about the 2004 Krumholz
    et al. scheme; the entry stays open.

# Citations

1. [Krumholz et al. (2004)](/sources/krumholz-2004.md), §§1–3, 5,
   eqs. 5–17, Table 1 (arXiv preprint v1).
2. [Federrath et al. (2010)](/sources/federrath-2010.md), §§1–5,
   eqs. 1–33, Apps. A–B (arXiv v2).
3. [Kim & Ostriker (2017)](/sources/kim-2017.md), §§2.1–2.2, eqs. 7–21,
   Figs. 2, 4 (arXiv v2).
4. [Mathew & Federrath (2021)](/sources/mathew-2021.md), §§2.3, 2.5.2,
   5.2, 6.1, eq. 4, Table 1 (arXiv v2).
