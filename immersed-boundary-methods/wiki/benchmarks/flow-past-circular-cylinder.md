---
type: Benchmark
title: "Flow past a circular cylinder"
description: "The standard validation of immersed boundary methods for incompressible flow: steady separated flow at Re = 20–40 and periodic vortex shedding at Re ≈ 100–300, checked through drag and lift coefficients, recirculation length and Strouhal number, plus the impulsively started cylinder and the cylinder in a channel."
status: established
aliases: [circular cylinder, cylinder wake, impulsively started cylinder]
tags: [benchmark, incompressible, vortex-shedding, validation]
timestamp: 2026-11-08T18:10:00Z
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

## Later uses

| source | method | conditions | reported |
|---|---|---|---|
| [Tseng & Ferziger (2003)](/sources/tseng-2003.md) | [ghost cell](/methods/ghost-cell-method.md) | $Re=20$, $40$, $100$ | $C_D$, recirculation length, $St$ close to body-fitted results; second-order convergence |
| [Uhlmann (2005)](/sources/uhlmann-2005.md) | Lagrangian [direct forcing](/methods/direct-forcing.md) | $Re=100$, $D/h=38.4$; oscillating cylinder $Re=185$ | $St$ within 4 %, mean $C_D$ overpredicted by 11 %; smooth drag versus position |
| [Ghias et al. (2007)](/sources/ghias-2007.md) | compressible ghost cell, curvilinear grid | $Re$ up to $3900$ (3-D), $M=0.4$ at $Re=80$ | $C_D$, base pressure and $St$ against spectral and experimental data |
| [Taira & Colonius (2007)](/sources/taira-2007.md) | [IB projection](/methods/immersed-boundary-projection-method.md) | $Re=20$, $40$, $200$; impulsive start | wake dimensions, $C_D$, $C_L$, $St$; stable near CFL 1 |
| [Mittal et al. (2008)](/sources/mittal-2008.md) | ghost cell | range of $Re$; suddenly accelerated cylinder $Re=550$ | $C_D$, base pressure, $St$ against spectral results |

[Mittal & Iaccarino (2005)](/sources/mittal-2005.md) use the
low-Reynolds-number cylinder of Lai and Peskin to illustrate the spurious
elasticity of soft tethers in continuous forcing.

## Uses in chunk 3

- [Griffith & Patankar (2020)](/sources/griffith-2020.md): $Re=200$ with the
  set-up of Taira and Colonius; lift, drag and Strouhal numbers agree, and the
  immersed boundary method shows spurious interior flow that the immersed
  interface method removes.
- [Natarajan et al. (2022)](/sources/natarajan-2022.md): moving embedded
  boundary, cylinder translating at $Re=40$, in-line oscillation at $Re=100$,
  transverse oscillation at $Re=185$.
- [Ou et al. (2022)](/sources/ou-2022.md): directional ghost cells; flow and
  heat transfer at $Re=20$, $40$ with Dirichlet, Neumann and Robin thermal
  conditions (Nusselt numbers against Pan), nearly second-order convergence.

# Citations

- [Goldstein et al. (1993)](/sources/goldstein-1993.md) — examples (start-up cylinder).
- [Ye et al. (1999)](/sources/ye-1999.md) — §3.
- [Angot et al. (1999)](/sources/angot-1999.md) — §6.
- [Kim et al. (2001)](/sources/kim-2001.md) — §3.2, Table I.
- [Tseng & Ferziger (2003)](/sources/tseng-2003.md) — §3.
- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — continuous-forcing section.
- [Uhlmann (2005)](/sources/uhlmann-2005.md) — §5.
- [Ghias et al. (2007)](/sources/ghias-2007.md) — §3.
- [Taira & Colonius (2007)](/sources/taira-2007.md) — §5.
- [Mittal et al. (2008)](/sources/mittal-2008.md) — §3.
- [Griffith & Patankar (2020)](/sources/griffith-2020.md) — benchmarks.
- [Natarajan et al. (2022)](/sources/natarajan-2022.md) — §3.
- [Ou et al. (2022)](/sources/ou-2022.md) — §3.
