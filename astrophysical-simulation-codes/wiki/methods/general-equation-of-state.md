---
type: Method
title: "General equations of state in Godunov codes"
description: "How finite-volume Godunov codes replace the ideal-gas law by an arbitrary equation of state: Athena++'s three-function interface and gamma-replacement recipe with log-space bilinear tables and a PVRS wave-speed estimate for HLLC, CASTRO's EOS called on density and internal energy with Newton–Raphson temperature inversion, and the verification of both against exact general-EOS Riemann solutions."
status: established
aliases: [general EOS, non-ideal equation of state, tabulated EOS, tabular EOS, Helmholtz EOS, real-gas EOS]
tags: [hydro, mhd, equation-of-state, riemann-solver, verification]
timestamp: 2026-10-13T00:00:00Z
---

# General equations of state in Godunov codes

An ideal-gas code uses $\gamma$ in a handful of places: to convert
between conserved and primitive variables, in the sound speed for the
Courant condition and the wave speeds, and inside the Riemann solver.
Replacing the ideal-gas law by an arbitrary equation of state (EOS)
therefore means fixing which thermodynamic functions the code may call.
Below, $\Gamma_1 \equiv \partial\ln p/\partial\ln\rho$ at constant entropy $= \rho c_s^2/p$
is the generalized adiabatic index, equal to $\gamma$ for an ideal gas.

## The Athena++ interface

[Coleman (2020)](/sources/coleman-2020.md) (§§2–3) extends
[Athena++](/software/athena-plus-plus.md) to non-relativistic (M)HD with
any EOS for which $(\partial p/\partial\rho)_e > 0$ and
$(\partial p/\partial e)_\rho > 0$, conditions called "sufficient, but not
necessary" for a unique Riemann solution, citing Chen et al. (2019)
(eqs. 4–5; asserted, not proved here).
* **Three functions** (eqs. 13–15): $p(\rho, \rho e)$, $\rho e(\rho, p)$ and
  $c_s^2(\rho, p)$. The code evolves $E$ and uses $p$ as primitive, so it
  obtains $\rho e$ by subtracting the kinetic and magnetic energies from $E$
  before calling the first. $c_s^2$ feeds the Courant condition and the
  Riemann solver. "Any EOS which is able to provide these functions ...
  can work in this framework, even a piecewise EOS." Recorded as printed:
  the text assigns the first two functions to the
  primitive-to-conserved and reverse conversions, the opposite of what
  their arguments imply.
* **Recipe** (eqs. 16–18): every occurrence of $\gamma$ was replaced,
  $p = (\gamma-1)\rho e \Rightarrow p(\rho,\rho e)$,
  $\rho e = p/(\gamma-1) \Rightarrow \rho e(\rho,p)$,
  $c_s^2 = \gamma p/\rho \Rightarrow c_s^2(\rho,p)$; that this preserves
  the characteristic speeds is deferred to Chen et al. (2019). The one
  exception is the Roe-average wave speed (below). Characteristic
  reconstruction does not support a general EOS (footnote 3), which agrees
  with [Stone et al. (2020)](/sources/stone-2020.md), §3.2.1; all runs use
  PLM on primitives with VL2.
* **Tables** (§3.2, eqs. 19–28): $\log(p/\rho e)$, $\log(\rho e/p)$ and
  $\log\Gamma_1$ on a regular grid in $\log\rho$ and in the log of internal
  energy or pressure times $\rho^{\eta_{\mathrm{tab}}}$ (a user exponent),
  interpolated bilinearly, which "guarantees the preservation of
  monotonicity". Off-table requests are extrapolated linearly; floors on
  $p$, $\rho e$ and $\rho$ are recommended. For an ideal gas the three
  quantities are constants, so a $2\times2$ table reproduces the ideal EOS
  "exactly (to machine precision)" (asserted; no data shown).
* **Analytic EOSs in the tests** (§4, §4.4): the hydrogen-ionization EOS
  root-finds $T$ by Brent–Dekker to one part in $10^{12}$ at every call,
  chosen over a table so that table resolution does not contaminate
  convergence; the Helmholtz EOS is evaluated in $(\rho, T)$ with $T$ from
  bisection, secant and Newton–Raphson seeded by the last value.
* **Scope** (§1, §4.4): non-relativistic only; the EOS functions take no
  passive scalars, so composition-dependent tests were not attempted.
  [Stone et al. (2020)](/sources/stone-2020.md) describe the Athena++ EOS
  as any analytic or tabulated pressure of density and internal energy
  (§3.1).

## Wave speeds for HLL-type solvers

([Coleman (2020)](/sources/coleman-2020.md), §3.3, §5, App. A; see
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md).)
* **HLLC.** The Roe-average estimate needs a fourth EOS function, the
  sound speed at the Roe-averaged density and enthalpy (eq. A4); the Hu et
  al. (2009) variant also needs four. Athena++ now defaults to a
  generalized primitive-variable (PVRS) estimate (Toro 1999) that needs
  only the three: from arithmetic means of the left and right densities
  and sound speeds, a linearized star pressure and velocity, star
  densities, $\Gamma_1$ at each star state, and a shock factor that
  scales each outer sound speed when the star pressure exceeds that side's
  pressure (eqs. A8–A17). Measured "significant reduction of errors and
  improved convergence" on the double-shock tests, with no loss for the
  ideal gas. Recorded as printed: eq. A11 writes $p_{x,R}$, $p_{x,L}$ where
  $p_R$, $p_L$ are presumably meant.
* **HLLD** keeps the Miyoshi & Kusano (2005) estimate; PVRS "is not
  readily extendable to MHD". On the double shocks HLLD errors are up to
  3× those of HLLC with PVRS, and HLLC with the HLLD estimator reproduces
  this, so the estimator is blamed (§5.2).
* **HLLE**, with every estimator tried, "did not converge to the correct
  solution" on the two hydrogen double-shock tests, and was a few tens of
  per cent worse than HLLC on the others; with the Roe estimator it does
  converge on their ideal-gas analogues (§5.1.4, footnote 10, §6). So
  HLLE is extended to a general EOS, as
  [Stone et al. (2020)](/sources/stone-2020.md), §3.2.2, state, but it
  fails to converge on general-EOS double shocks; Coleman's abstract and
  §6 recommend only HLLC and HLLD.

## CASTRO

[CASTRO](/software/castro.md) was built for a general EOS from the start.
* The EOS is called with density, specific internal energy and
  composition; gamma law, Helmholtz (Timmes & Swesty 2000) and
  Lattimer–Swesty are shipped, and tabular EOSs are inverted by
  Newton–Raphson ([Almgren et al. (2010)](/sources/almgren-2010.md), §3).
* Its two-shock-type Riemann solver carries $\rho e$ and needs no EOS call
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §5.2).
* In the white-dwarf merger runs the Helmholtz EOS inverts
  $(\rho, e)\to T$ by Newton–Raphson with default relative tolerance
  $10^{-8}$; on non-convergence a temperature floor (typically $10^5$ K)
  applies ([Katz et al. (2016)](/sources/katz-2016.md), §2.2).
* **Energy-consistency choice** (§2.2): either keep $e$ and accept
  thermodynamic inconsistency with the floored $T$ (the original CASTRO
  behaviour), or reset $e$ to match $T$, which is more accurate in strong
  1D shocks that reach the floor but drifts total energy over long runs
  through the resets and the Newton tolerance. Katz et al. keep $e$.
  Their energy conservation in binary orbits is worse than that of
  Marcello & Tohline (2012) because negative internal energies are reset to
  the temperature floor (§4.4).

[Coleman (2020)](/sources/coleman-2020.md) (§1) says CASTRO ran similar
general-EOS tests (Zingale & Katz 2015, not ingested) but is hydro-only,
and calls Athena++ "the first publicly-available open-source MHD code"
whose general-EOS capability is verified with a test suite (asserted).

## Verification against exact general-EOS solutions

[Coleman (2020)](/sources/coleman-2020.md) (§4, Tables 2–4, App. B–C)
publishes exact constant states for 1D problems run at
$N = 64$–$2048$ cells, Courant number 0.4, $L_1$ and $L_2$ errors per
cell:
* **Hydrogen-ionization EOS** (Saha), six hydrodynamic Riemann problems:
  two Sod-like, two asymmetric shock–shock, two rarefaction–rarefaction.
  Near-linear convergence except the shock–shock pair, whose errors are
  "nearly constant for $512\le N\le2048$" (§5.1.2). The paper attributes
  the stall to cells straddling the shocks, whose averaged
  $(\rho, p)$ give a $\Gamma_1$ below its value on either side because
  $\Gamma_1$ is non-monotonic there, by about the same amount at $N = 64$
  and $N = 2048$: a limitation of "finite volume methods without front
  tracking" (interpretation, not demonstrated).
* **MHD Riemann problem** with the Ryu & Jones (1995) test-2a states and
  the hydrogen EOS: all seven waves are discontinuities, so the exact
  solution solves 49 jump conditions; near-linear convergence with HLLD
  (§4.2).
* **Linear waves** in the hydrogen EOS at a temperature where $\Gamma_1$
  varies fastest: sound and fast magnetosonic modes converge near second
  order (§4.3; see
  [linear wave convergence](/benchmarks/linear-wave-convergence.md)).
* **Helmholtz EOS**: a Sod-like problem converges well; a shock–shock
  problem behaves better than its hydrogen analogues (§4.4).
* Serna & Marquina (2014) van der Waals tests give "comparable results" by
  visual comparison (§4).

## Later uses (batch 8)

* **FLASH's first version.** [Fryxell et al. (2000)](/sources/fryxell-2000.md), §4, ships three EOS: a gamma law, the analytic Nadyozhin EOS (maximum error about 0.1 %) and the Helmholtz EOS (recommended). The Helmholtz table is a biquintic Hermite fit, consistent "to the limits of IEEE 64 bit arithmetic", with typical error about $10^{-7}$. It covers $10^{-10}$ to $10^{11}$ g cm$^{-3}$ in $\rho Y_{\mathrm e}$ and $10^4$ to $10^{11}$ K, 211 × 71 points, about 1 MB, and runs about twice as fast as Nadyozhin. Each EOS is called in temperature and density, with temperature found by Newton–Raphson in 2–4 iterations. The hydro needs both $\gamma$ and $\Gamma_1$ (§3.1). All tests in the paper use the gamma law (§7), in agreement with Coleman (2020).

## Later uses (batch 10)

### Transported indices: the Colella–Glaz design

[Colella & Glaz (1985)](/sources/colella-1985.md) give the earliest
general-EOS Godunov design in the bundle, and the one FLASH's first
version follows (batch 8). It is the opposite strategy to Athena++'s
three-function interface above: instead of calling the EOS wherever an
ideal-gas code uses $\gamma$, it carries two dimensionless indices as extra
variables and models the EOS locally between calls.
* **Two indices** (eqs. 7–8): $\Gamma_1 = \rho c_s^2/p$ and an energy index
  $p/(\rho e) + 1$. "For polytropic gases, [the energy index] is the ratio
  of specific heats and [equals $\Gamma_1$]. Neither statement is true in
  general." The registry $\gamma$ is the ideal-gas constant; the energy
  index has no registry symbol (Source page, Notation map).
* **Minimum EOS information** (§2, pp. 272–273): "only one evaluation of the
  pressure per mesh point per dimension per time step", plus $\Gamma_1$; the
  derivatives of $p$ with respect to $e$ and $1/\rho$ are not needed when
  the Riemann problem is solved by secant iteration, which the paper
  prefers because such derivatives "often are not available in real gas
  equation of state software". The stated premise: the energy index "is a
  slowly varying function of the thermodynamic variables for real gases",
  staying between 1 and 5/3 while $p$, $\rho$, $e$ vary over many orders of
  magnitude; compressible water "might" need another parametrization.
* **Index transport** (eqs. 26–27, 31–32): across a wave the energy index
  changes by $\left(1 - \text{energy index}/\Gamma_1\right)(\text{energy
  index} - 1)$ times the relative pressure jump, with means of the two
  sides, to third order in the jump; the result is clipped to bounds such
  as the extremes over neighbouring cells. In the Eulerian scheme the
  index must also be interpolated and traced to the interface, because the
  energy flux needs it (eqs. 47–48); in the Lagrangian scheme piecewise
  constant indices suffice (eq. 41).
* **The limiter is called critical** (§4, p. 288): in compressible water,
  with an order-of-magnitude jump of the energy index across the shock,
  "the limiting of [the index] given by (32) is critical to the success of
  the algorithm" (asserted; no data shown). Coleman's stall on the hydrogen
  double shocks, attributed to a non-monotonic $\Gamma_1$ in
  shock-straddling cells (above), concerns indices in cells that straddle
  a jump as well; the two papers do not discuss each other's case, and the
  link is this page's observation, not a claim of either source.
* **Admissibility** (§1, after eq. 4): $p$ decreasing in specific volume
  and increasing in $e$ is "sufficient [17] but not necessary [20]" for
  hyperbolicity and a unique Riemann solution, with convexity assumed. This
  is the same pair of conditions that Coleman (2020) states as
  $(\partial p/\partial\rho)_e > 0$ and $(\partial p/\partial e)_\rho > 0$,
  "sufficient, but not necessary", citing Chen et al. (2019); the 1985
  statement is earlier and agrees.
* **Tabulated EOS** (§4): sound speeds from numerically differentiated
  tabulated pressure (Gilmore air) gave "the same stability and
  robustness" as analytic sound speeds (Hansen); differentiating a sparse
  table might cause instabilities. In the Mach-reflection test the three
  EOSs (ideal gas with $\gamma = 1.4$, Gilmore, Hansen) change the flow
  details, and only Hansen matches the measured wall density "within
  2–3 %" (§3).
* **Cost** (§4): about 40 % more than the polytropic algorithm on a Cray 1,
  excluding the EOS call, which itself costs more than that increase; see
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).

# Citations

1. [Coleman (2020)](/sources/coleman-2020.md), §§1–6, eqs. 4–28,
   Tables 2–4, App. A–C (arXiv v3).
2. [Almgren et al. (2010)](/sources/almgren-2010.md), §§3, 5.2 (arXiv v1).
3. [Katz et al. (2016)](/sources/katz-2016.md), §§2.2, 4.4 (arXiv v2).
4. [Stone et al. (2020)](/sources/stone-2020.md), §§3.1–3.2.2.
5. [Fryxell et al. (2000)](/sources/fryxell-2000.md), §§3.1, 4–4.4, 7.
6. [Colella & Glaz (1985)](/sources/colella-1985.md), §§1–4, eqs. 4–8, 26–35, 41, 47–48, pp. 272–275, 288.
