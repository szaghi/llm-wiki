---
type: Property
title: "Well-balanced schemes"
description: "A scheme for a balance law is well balanced if a discrete steady state of interest — lake at rest, hydrostatic or stationary flow — survives a time step exactly, so that small perturbations of it are not swamped by truncation error; obtained by matching the source and flux discretizations, by evolving the deviation from a known equilibrium, or by a Riemann solver that resolves the stationary source wave."
status: established
aliases: [well-balancing, C-property, exact preservation of equilibria, hydrostatic balance]
tags: [source-terms, well-balanced, property]
timestamp: 2026-10-12T00:00:00Z
---

# Well-balanced schemes

For a balance law $\partial_t u + \nabla\cdot\mathbf f(u) = \mathbf s(u)$,
a scheme is **well balanced** with respect to a steady state
$u^{\mathrm{eq}}$ if one forward Euler step from the discrete equilibrium
leaves it unchanged. For a hydrostatic state, the mass and energy
equations satisfy this automatically for any consistent flux at zero
velocity. The momentum equation requires the source discretization to
match the flux difference,
$\hat f_{i+1/2} - \hat f_{i-1/2} - h\,\mathbf s_i = 0$
([Edelmann et al. (2021)](/sources/edelmann-2021.md), §4, eqs. 39–44).
Without it, truncation error drives spurious flows that dwarf small
physical perturbations. A 1D isothermal atmosphere without balancing
reaches Mach $10^{-6}$–$10^{-5}$ at once, while every balanced method
stays below $10^{-12}$ (§5.1).

**Exact or approximate.** Most astrophysical well-balanced schemes
preserve a second-order approximation of the hydrostatic state. The α-β
and deviation methods preserve the state itself and are "expected to be
more accurate" ([Edelmann et al. (2021)](/sources/edelmann-2021.md), §§1, 6).

**Routes.**
1. *Rewrite the system.* Cargo–LeRoux introduce a potential that absorbs
   the gravity source and evolve a modified pressure, which turns the
   system into homogeneous Euler equations with a modified equation of
   state. In multi-D the potential exists only when $\mathbf g$ is
   parallel to $\nabla\rho$. Edelmann et al. therefore use a horizontal
   average, which balances only approximately. The method also needs a
   flux that preserves contact discontinuities (§4.1).
2. *Reconstruct relative to the equilibrium profile* (α-β method). Divide
   $\rho$ and $p$ by known hydrostatic profiles, reconstruct, and multiply
   back at the faces. Equilibrium data then give equal left and right
   states, and the source is written so that it cancels the flux
   difference exactly (§4.2).
3. *Evolve the deviation* (deviation method). Discretize the equation for
   $u - u^{\mathrm{eq}}$, with fluxes and sources taken as differences
   from their equilibrium values. Unlike the first two, it balances
   states with non-zero velocity, for example a Keplerian disk kept for
   $10^4$ orbits, and leaves the reconstruction variables free. Its
   claimed compatibility with "arbitrarily high order finite-volume
   codes" is cited, not tested (§§4.3, 5.4).
4. *Resolve the stationary source wave in the Riemann solver.*
   * The [HLLEM](/methods/hllem-riemann-solver.md) solver in
     path-conservative form is exactly well balanced for lake-at-rest
     shallow water: zero eigenvalues give $\delta_p = 1$, and the
     fluctuations vanish for any bottom topography. The velocity error is
     $10^{-15}$ in double and $10^{-31}$ in quadruple precision
     ([Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §3.1.1, Table 1).
   * The augmented Roe solver treats the bed slope as a stationary wave
     ([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §3.1).
   * In [alternative finite-difference WENO](/methods/alternative-finite-difference-weno.md),
     a Riemann solver that keeps stationary contacts makes the whole
     scheme do so ([Balsara et al. (2025)](/sources/balsara-2025.md), §II).

**Interactions found in long runs** ([Edelmann et al. (2021)](/sources/edelmann-2021.md)):
* In 2D stably stratified atmospheres, well-balanced runs with
  [low-Mach fluxes](/methods/low-mach-number-fluxes.md) still let
  perturbations grow exponentially, slowest with the deviation method.
  Dissipative fluxes do not show this growth (§5.1).
* At low Mach the total energy must include the gravitational potential
  energy (§2.1).
* With α-β or deviation balancing, rising-bubble runs reproduce the
  expected scaling of Mach number with perturbation amplitude down to
  about $10^{-6}$. Convection runs reach $\mathrm{Ma}_{\mathrm{rms}} \approx 2\times10^{-4}$
  (§§5.2–5.3).

**Related property.** [Free-stream preservation](/properties/free-stream-preservation.md)
is the same idea for a different steady state: a uniform flow on a
curvilinear grid, kept exactly by consistent metric terms.

# Citations

1. [Edelmann et al. (2021)](/sources/edelmann-2021.md), §§1, 2.1, 4, 5, 6.
2. [Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §3.1.1, Table 1.
3. [Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §3.1.
4. [Balsara et al. (2025)](/sources/balsara-2025.md), §II.
