---
type: Benchmark
title: "Underwater explosion"
description: "A gas bubble at a gigapascal and 1250 kg/m³, 0.24 m in diameter, 0.3 m below a free water–air surface: the two-dimensional test of compressible two-phase solvers at density ratios near 1000 and pressure ratios near 10⁴, run by a sharp-interface DG solver and a pressure–temperature-equilibrium finite-volume model."
status: established
aliases: [underwater explosion near a free surface, explosion bubble under a free surface, gas bubble explosion in water]
tags: [benchmark, multiphase, interface-capturing, positivity]
timestamp: 2026-10-22T20:00:00Z
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
and both sources present it as a test of robustness at such ratios and
of interface sharpness. The two sources run the same
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

**Temperature.** Nguyen et al. start the bubble at $T_0=2779.91$ K,
obtained from their stiffened-gas law, and report a maximum bubble
temperature still about 2750 K at 0.2 ms; their model carries a single
temperature for all phases (Fig. 14). They do not print the heat
capacities, so the value cannot be checked from the paper. Bai & Li do
not print heat capacities for this case either.

**Robustness.** Both papers present the run as evidence that the scheme
handles high density and pressure ratios with strong shocks; neither
reports a failure, a positivity fix specific to this case or an error
norm.

## Qualifications

- The two setups share the geometry and the bubble state but not the
  models: a sharp interface with one equation of state per fluid against
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
