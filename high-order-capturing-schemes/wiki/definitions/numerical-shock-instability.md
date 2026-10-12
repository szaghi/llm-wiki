---
type: Definition
title: "Numerical shock instability (carbuncle and related anomalies)"
description: "Spurious growth of small perturbations inside a captured strong shock aligned with the grid: the carbuncle ahead of a blunt body, odd–even decoupling along a moving shock, the kinked Mach stem and the one-dimensional steady-shock limit cycle; it strikes low-dissipation complete Riemann solvers and is studied almost only at first and second order."
status: established
aliases: [carbuncle, carbuncle phenomenon, odd–even decoupling, kinked Mach stem, shock instability, one-dimensional carbuncle]
tags: [riemann-solver, shock-instability, robustness, definition]
timestamp: 2026-10-12T00:00:00Z
---

# Numerical shock instability

A **numerical shock instability** amplifies small perturbations inside a
captured strong shock where the physical problem would damp them. The
symptoms are a saw-tooth (alternating odd/even cell) variation along the
shock front, polluted post-shock states, residuals that stop converging
in steady problems, and at worst the destruction of the shock. It affects
strong shocks aligned with the grid in two or more dimensions. It depends
on the Riemann solver, the Mach number, the cell aspect ratio, the
numerical shock structure, upstream perturbations and the order of the
scheme ([Simon & Mandal (2019)](/sources/simon-2019.md), §1;
[Simon & Mandal (2019b)](/sources/simon-2019-b.md), §1).

**Manifestations**, each with its standard test:
* **Carbuncle**: "a protuberance grows ahead of the bow shock along the
  stagnation line" in steady blunt-body flow
  ([Xie et al. (2021)](/sources/xie-2021.md), §1); see the
  [hypersonic blunt-body test](/benchmarks/hypersonic-blunt-body.md).
  Kitamura & Shima class a run as a carbuncle when the shock oscillates
  over four or more cells in the streamwise direction
  ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §IV.A).
* **Odd–even decoupling**: a moving, grid-aligned shock in a duct whose
  centreline is perturbed alternately loses its profile
  ([Quirk's test](/benchmarks/quirk-odd-even-test.md)).
* **Kinked Mach stem**: in the [double Mach reflection](/benchmarks/double-mach-reflection.md)
  a first-order low-dissipation solver kinks the Mach stem and forms a
  spurious triple point ([Simon & Mandal (2019)](/sources/simon-2019.md), §9.5;
  [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.2;
  [Xie et al. (2021)](/sources/xie-2021.md), §6.3). The reflected-shock
  stem of the [forward-facing step](/benchmarks/forward-facing-step.md)
  kinks the same way ([Simon & Mandal (2019)](/sources/simon-2019.md), §9.7).
* **One-dimensional carbuncle**: a steady 1D shock captured with one
  interior point. For some sub-cell shock positions its intermediate
  state oscillates, sheds waves and enters a limit cycle
  ([stationary normal shock](/benchmarks/stationary-normal-shock.md);
  [Xie et al. (2021)](/sources/xie-2021.md), §3.1.2). Navas-Montilla &
  Murillo relate it to the [slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md):
  some Hugoniot-admissible stationary shocks are numerically unstable
  ([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §4.2).
* **Post-shock oscillations** behind a diffracted shock
  ([Xie et al. (2021)](/sources/xie-2021.md), §6.2;
  [shock diffraction](/benchmarks/shock-diffraction.md)).

**Which solvers.** Complete solvers that resolve the contact and shear
waves exactly are vulnerable: Godunov's exact solver, Roe, HLLC,
[HLLEM](/methods/hllem-riemann-solver.md) and the augmented Roe solver
for shallow water. HLL and HLLE, which dissipate the linear waves, are
robust ([Simon & Mandal (2019)](/sources/simon-2019.md), §4.1;
[Simon & Mandal (2019b)](/sources/simon-2019-b.md), §4;
[Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §4.2.1),
and Godunov, Roe, HLLEM and HLLC all fail Xie et al.'s carbuncle tests
([Xie et al. (2021)](/sources/xie-2021.md), §6).
How robust HLLE is remains disputed; see `Contradictions` on the
[Riemann-solver page](/methods/approximate-riemann-solvers.md). Kitamura
& Shima sort first-order fluxes into three groups. Roe, even with an
entropy fix, is vulnerable and stands for Godunov and HLLC. AUSM+-up,
LDFSS and SLAU are in the middle. Van Leer's flux-vector splitting,
AUSMPW+, RoeM2 and SLAU2 are "almost (but not perfectly) free" of
anomalies ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§II.B, III.E).
Gressier and Moschetta conjectured that an upwind scheme cannot resolve
contacts exactly and be free of shock instability. Simon & Mandal claim
that their pressure-sensor HLLC variant "suggests that it is possible to
circumvent" the conjecture. The evidence is tests and a linear analysis,
not a proof ([Simon & Mandal (2019)](/sources/simon-2019.md), §§4.1, 10).

**Proposed mechanisms.** None is proved, and they are not mutually
exclusive:
1. *Anti-diffusion cancels the HLL dissipation on transverse faces.*
   Write HLLC or HLLEM as HLL plus an anti-diffusive term. On faces
   transverse to a perturbed normal shock, that term is of the same order
   as the HLL dissipation and cancels its damping of density and
   normal-velocity perturbations. A linear saw-tooth analysis with mean
   state $\rho = p = 1$ gives one-step amplification factors $1$, $1$ and
   $1 - 2\nu_y$ for the density, normal-velocity and pressure
   perturbations, against $1 - 2\nu_y$ for all three with HLLE. The
   pressure perturbation keeps feeding a residual density perturbation
   ([Simon & Mandal (2019)](/sources/simon-2019.md), eqs. 23–26;
   [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §5, Table 1). When
   density or velocity varies along the front, so does the mass flux, and
   the shock bulges.
2. *Too little entropy production inside the numerical shock.* For a
   steady shock with a single interior point, instability is "inevitable"
   for some shock positions. Raising the entropy of the intermediate cell
   stabilizes it beyond a threshold that depends on the Mach number. The
   paper does this by reducing the anti-diffusion on the pressure part of
   the entropy wave. The idea is motivated by the entropy overshoot of the
   viscous shock profile; the argument is heuristic
   ([Xie et al. (2021)](/sources/xie-2021.md), §§3.2–3.5).
3. *Shock-position jumps and cross flow.* A slightly curved shock is
   represented by one-cell jumps, and its position can jump by up to two
   cells. A jump triggers cross flow, then a downstream recirculation
   that grows into the carbuncle. The authors call the mechanism "still
   not clear" ([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §4.2).
4. *The numerical shock structure.* The state inside a captured shock is
   a numerical artifact that leaves the Hugoniot curve. Fluxes that
   capture the shock within one cell (Roe, AUSM+-up, LDFSS) are the ones
   sensitive to shock speed ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§I, IV.B).

**Shock speed matters.** Quirk's moving-shock test does not certify a
flux for stationary shocks. On a map of shock Mach number $M_s$ against
propagation Mach number $M_{\mathrm{prop}}$, the most severe case for
sharp-capturing fluxes is the slowly moving shock,
$0 < M_{\mathrm{prop}} < M_{\mathrm{sig}} \approx 0.44\,M_s$ for
$\gamma = 1.4$, where downstream noise can catch up with the shock
([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§III.B, IV.B, V).

**Order of accuracy.** Every batch-8 source studies first-order schemes,
some also second order, and none uses WENO. They cite two claims without
testing them. Gressier: higher order reduces the instability but does not
remove it ([Simon & Mandal (2019)](/sources/simon-2019.md), §9;
[Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7). Unnamed earlier
work: second order makes post-shock oscillations of moving shocks more
likely and carbuncles of stationary shocks less likely, depending on the
slope limiter ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §II.B).
At high order, [Balsara & Shu (2000)](/sources/balsara-2000.md) see a mild
carbuncle with Roe-type (RF) fluxes where the normal shock of the double Mach
reflection meets the wall, and remove it by switching to Lax–Friedrichs
near shocks ([conservative finite difference](/methods/conservative-finite-difference.md)).
For remedies, see [cures for numerical shock instability](/methods/shock-instability-cures.md).

# Citations

1. [Simon & Mandal (2019)](/sources/simon-2019.md), §§1, 4.1, 6, 9, 10.
2. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §§1, 4, 5, 7.
3. [Xie et al. (2021)](/sources/xie-2021.md), §§1, 3, 6.
4. [Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§I–V.
5. [Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §4.2.
6. [Balsara & Shu (2000)](/sources/balsara-2000.md).
