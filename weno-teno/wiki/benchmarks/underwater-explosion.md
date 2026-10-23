---
type: Benchmark
title: "Underwater explosion"
description: "A gas bubble at a gigapascal and 1250 kg/m³, 0.24 m in diameter, 0.3 m below a free water–air surface: a two-dimensional test of two-phase solvers at density ratios near 1000 and pressure ratios near 10⁴, run by a sharp-interface DG solver, an equilibrium model and a Lagrangian particle method; plus a spherically symmetric one-dimensional explosion bubble."
status: established
aliases: [underwater explosion near a free surface, explosion bubble under a free surface, gas bubble explosion in water]
tags: [benchmark, multiphase, interface-capturing, positivity]
timestamp: 2026-10-23T23:45:00Z
---

# Underwater explosion

A circular bubble of highly compressed gas sits in water at rest just
below a free water–air surface. As Bai & Li describe the flow (§3.6), a
circular shock moves radially outwards while a rarefaction converges to
the bubble centre; when the shock reaches the free surface, a weak shock
enters the air and rarefaction waves appear in the water, and the water
above the bubble is drawn into a liquid film, the "ligament" of Nguyen
et al. (§3.3). The test combines three material regions (explosion
gas, water as a [stiffened gas](/definitions/stiffened-gas-equation-of-state.md),
air), density ratios of about 1000 and pressure ratios of about $10^4$,
and the sources present it as a test of robustness at such ratios and
of interface sharpness. The three sources run the same
geometry: a bubble of diameter $0.24$ m centred $0.3$ m below the free
surface, with the bubble at $\rho=1250$ kg/m³ and $p=1$ GPa ($10^9$ Pa)
and ambient air and water at atmospheric pressure.

## Setups in the sources

| | [Bai & Li (2022)](/sources/bai-2022.md) §3.6 | [Nguyen et al. (2022)](/sources/nguyen-2022.md) §3.3, Table 2 |
|---|---|---|
| Domain | $[0,4]^2$ m, free surface at $y=1.5$ m, bubble centre $(2.0,1.2)$ m | $3\times3$ (also $15\times15$), free surface at $y=0$, bubble centre $y=-0.3$ |
| Bubble | $p=1.0$ GPa, $\rho=1250$ kg/m³ | $(\gamma,\rho,p,p_\infty)=(1.4,\ 1250,\ 10^9,\ 0)$ |
| Water | $\gamma=4.4$, $p_\infty=6.0\times10^8$ Pa, at normal temperature and pressure | $(4.4,\ 1000,\ 101325,\ 6\times10^8)$ |
| Air | $\gamma=1.4$, at normal temperature and pressure | $(1.4,\ 1.225,\ 101325,\ 0)$ |
| Boundaries | not stated | reflecting side and bottom walls, extrapolated top |
| Model and scheme | two Euler systems with a level-set interface, ghost fluids in cut cells, DG of degree 2 ([level-set methods](/methods/level-set-method.md)) | [multicomponent Euler](/definitions/multicomponent-euler-equations.md) in pressure–temperature equilibrium, MUSCL with three limiters, HLLC |
| Grids | $160\times160$ background, three adaptive levels | $150^2$, $300^2$, $600^2$ |
| Output | up to 3.156 ms; density along $x=2$ m at 0.2 ms | 0.5, 1.0, 1.5 ms; up to 12 ms on the large domain |

[Jiang et al. (2024)](/sources/jiang-2024.md) §5.2.2 run the same states,
(bubble, air, water) $=(\rho,p,\gamma,p_\infty)=(1250,10^9,1.4,0)$,
$(1.225,101325,1.4,0)$, $(1000,101325,4.4,6\times10^8)$ in SI units, on
$[-2,2]\times[-1.5,1]$ m with the free surface at $y=0$, the bubble of
radius $0.12$ m centred at $(0,-0.3)$ m and a reflective bottom at
$y=-1.5$ m. Their scheme is a Lagrangian weighted-least-squares particle
method on a single GPU: each particle pair is a 1D Riemann problem solved
with a Roe-type Lagrangian solver, whose left and right states come either
from the particle values (LWLS-RR) or from a fifth-order three-stencil
reconstruction with [WENO-Z+](/methods/weno-z-plus.md)-type weights on
collinear virtual points (LWLS-WENO-Z); each particle carries its own
phase's stiffened-gas law. Initial spacing $0.01$ m with two static
refinement levels ($1/4$ of it in the bubble, $1/2$ on
$0.12<\sqrt{x^2+(y+0.3)^2}<1.1$), about $2.2\times10^5$ particles.

## Findings

**Interface sharpness and limiters.** Nguyen et al. compare limiters on
the volume fractions: Van Leer diffuses the interface and may
underpredict the bubble height, while superbee and the more compressive
overbee keep sharp interfaces and the thin water ligament above the
bubble; the solution is grid-converged between $300^2$ and $600^2$
(Figs. 11–15). Bai & Li find their results consistent with Shukla's
computation on $1200\times1200$ cells, with a sharper liquid film at
about 1.9 ms, which they attribute to their sharp-interface treatment;
their density profile along $x=2$ m at 0.2 ms agrees with two other
computations except at the bubble centre (Figs. 34–36).

**A particle method against grid-based results.** Jiang et al. find
density and pressure along $x=0$ in agreement with the grid-based results
of Hu et al., Shukla and Shyue that they cite, and LWLS-WENO-Z less
dissipative than LWLS-RR (Figs. 11–12). Their method is non-conservative
(it advances the logarithm of density, velocity and internal energy),
and on smooth data it converges at about second order (2.2–2.35 for
LWLS-WENO-Z), not fifth ([density-wave advection](/benchmarks/density-wave-advection.md)).

**Temperature.** Nguyen et al. start the bubble at $T_0=2779.91$ K,
obtained from their stiffened-gas law, and report a maximum bubble
temperature still about 2750 K at 0.2 ms; their model carries a single
temperature for all phases (Fig. 14). They do not print the heat
capacities, so the value cannot be checked from the paper. Bai & Li do
not print heat capacities for this case either.

**Robustness.** The two grid-based papers present the run as evidence
that the scheme handles high density and pressure ratios with strong
shocks; Jiang et al. present it, with the cavitation bubble near a wall,
as a flow with strong shocks and large volume changes. None reports a
failure, a positivity fix specific to this case or an error norm.

## A spherically symmetric variant

[Paula et al. (2023)](/sources/paula-2023.md) §7.4.3 run a different,
one-dimensional problem after two published computations: a spherical gas
bubble of radius $0.16$ m in unbounded water, computed with a
spherical-symmetry source term. Water is a stiffened gas with
$\gamma=5.5$, $p_\infty=492.115\times10^6$ Pa, at $1025$ kg/m³ and
$10^6$ Pa; the gas has $\gamma=1.4$, $1630$ kg/m³ and $8.381\times10^9$ Pa.
The domain reaches $400$ m, with symmetry at $r=0$ and zero gradient at
$400$ m, on five multiresolution levels with finest cells from
$3.91\times10^{-2}$ to $2.44\times10^{-3}$ m; the CFL number is halved
until $t=10^{-4}$ s. The scheme is their
[discrete equations method](/methods/discrete-equations-method.md) with
time-averaged [THINC](/methods/thinc-reconstruction.md).

They find a minimum bubble radius of about $0.422$ m at $T\approx0.196$ s,
followed by a rebound, in "very good agreement" with a sharp-interface
computation, at an accuracy comparable to it at similar resolution, while a
second published method needs significantly higher resolution. Their
solution converges from above, like the sharp-interface one; the other
converges from below (Fig. 16).

## Qualifications

- Paula et al.'s spherical problem shares only the name with the
  free-surface problem: it has no free surface, a gas pressure of
  $8.381$ GPa instead of 1 GPa and different water constants
  ($\gamma=5.5$, $p_\infty=492.115$ MPa against $4.4$ and $600$ MPa).

- The setups share the geometry and the bubble state but not the
  models (Jiang et al.'s is a sharp, purely Lagrangian two-fluid particle
  model, with an interface repulsive force): a sharp interface with one equation of state per fluid against
  a homogeneous mixture in pressure and temperature equilibrium. Their
  agreement with earlier computations is visual.
- Bai & Li state that the physical parameters are those of their
  bubble-collapse case (§3.5), which prints only $\gamma$ and
  $p_\infty$; the heat capacities that their temperature form of the
  stiffened gas needs are not given for either case.
- The related problem of a shock collapsing a gas bubble in water is on
  the [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
  page; the one-dimensional water–air problems are the
  [gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md).

# Citations

- [Bai & Li (2022)](/sources/bai-2022.md) — §3.6, Figs. 34–36.
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §3.3, Table 2, Figs. 11–15.
- [Paula et al. (2023)](/sources/paula-2023.md) — §7.4.3, Fig. 16: spherically symmetric explosion bubble.
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §5.2.2, Figs. 11–12; §§3.1–3.3, §4.1: Lagrangian WLS particle method with WENO-Z-type reconstruction.
