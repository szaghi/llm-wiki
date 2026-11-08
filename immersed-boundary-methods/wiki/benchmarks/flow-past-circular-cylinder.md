---
type: Benchmark
title: "Flow past a circular cylinder"
description: "The standard validation of immersed boundary methods for incompressible flow: steady separated flow at Re = 20–40 and periodic vortex shedding at Re ≈ 100–300, checked through drag and lift coefficients, recirculation length and Strouhal number, plus the impulsively started cylinder and the cylinder in a channel."
status: established
aliases: [circular cylinder, cylinder wake, impulsively started cylinder]
tags: [benchmark, incompressible, vortex-shedding, validation]
timestamp: 2026-11-08T17:31:00Z
---

# Flow past a circular cylinder

A circular cylinder of diameter $D$ in a uniform stream $U_\infty$,
$Re=U_\infty D/\nu$. The wake is steady with a symmetric recirculation below a
critical Reynolds number of about $46$ and sheds vortices periodically above
it; the drag coefficient $C_D$, the amplitude of the lift coefficient $C_L$,
the recirculation length and the Strouhal number $St=fD/U_\infty$ are the
usual comparison quantities ([Ye et al. 1999](/sources/ye-1999.md), §3).

## Uses in the founding sources

| source | method | conditions | reported |
|---|---|---|---|
| [Goldstein et al. (1993)](/sources/goldstein-1993.md) | [feedback forcing](/methods/feedback-forcing.md), spectral | impulsively started, $Re\approx550$, 576 surface points, symmetric half domain | development of the symmetric wake compared with experiments (Bouard and Coutanceau 1980) |
| [Ye et al. (1999)](/sources/ye-1999.md) | [cut cell](/methods/cut-cell-method.md) | free stream $Re=20$–$300$; channel-confined cylinder | $C_D$, recirculation length and $St$ agree with established data; onset of shedding near $Re=46$; in a channel, onset between $Re=225$ and $232$ and $St=0.17$ at $Re=240$, agreeing with Chen et al. |
| [Kim et al. (2001)](/sources/kim-2001.md) | [direct forcing](/methods/direct-forcing.md) with mass source | $Re=40$, $100$; $331\times193$ grid, 30 points per diameter | $C_D$, $C_L$ amplitude and $St$ agree with the body-fitted results of Park et al. (1998); forces from integrating the momentum forcing |

A grid-aligned square cylinder in a channel serves the same purpose for
[volume penalization](/methods/volume-penalization.md) ([Angot et al. 1999](/sources/angot-1999.md), §6:
$Re=40$ steady, $Re=80$ shedding, penalized and Dirichlet solutions
indistinguishable at $\eta=10^{-8}$).

# Citations

- [Goldstein et al. (1993)](/sources/goldstein-1993.md) — examples (start-up cylinder).
- [Ye et al. (1999)](/sources/ye-1999.md) — §3.
- [Angot et al. (1999)](/sources/angot-1999.md) — §6.
- [Kim et al. (2001)](/sources/kim-2001.md) — §3.2, Table I.
