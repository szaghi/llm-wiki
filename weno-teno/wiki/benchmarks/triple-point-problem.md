---
type: Benchmark
title: "Triple-point problem"
description: "Two-dimensional three-state Riemann problem on [0,7]×[0,3] in which a shock from a high-pressure strip runs along two regions of different density, producing a vortex at the triple point with Kelvin–Helmholtz roll-up; run with one material and with two materials of different specific-heat ratio, as a test of interface and small-scale resolution."
status: established
aliases: [tri-point problem, triple point shock interaction, three-state Riemann problem]
tags: [benchmark, low-dissipation, multiphase, teno]
timestamp: 2026-10-23T10:00:00Z
---

# Triple-point problem

The triple-point problem is a two-dimensional Riemann problem with three
constant states at rest on $[0,7]\times[0,3]$. A high-pressure strip
$x<1$ drives a shock to the right into two regions of equal low pressure
separated by a horizontal interface at $y=1.5$: one dense, one light.
The shock moves at different speeds in the two regions, so the interface
is sheared and rolls up into a vortex at the point where the three
regions meet, with [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md)
roll-up along it. Both sources compare the amount of roll-up resolved
on a given grid, and the two-material version also tests a
multicomponent discretization.

## Data

| Region | [Liang et al. (2022)](/sources/liang-2022.md) §4.8: $(\rho,v_1,v_2,p)$ | [Li, Duan & Tang (2022)](/sources/li-2022-c.md) Ex. 5.7: component densities, $v$, $p$ |
|---|---|---|
| $x<1$ | $(1,0,0,1)$ | component 1, density $1$, $p=1$ |
| $x>1$, $y>1.5$ | $(0.125,0,0,0.1)$ | component 1, density $0.125$, $p=0.1$ |
| $x>1$, $y<1.5$ | $(1,0,0,0.1)$ | component 2, density $1$, $p=0.1$ |
| ratio of specific heats | not stated | component 1: 1.5; component 2: 1.4 |
| boundaries | outflow on the right, reflective elsewhere | not restated |
| grid, final time | $350\times150$, $t=5$ | $350\times150$ adaptive moving mesh against uniform $1050\times450$; $t=3.5$ and $5$ |

The geometry, densities and pressures are the same in both. Liang et al.
run a **single-material** version; Li, Duan & Tang run the
**two-material** version they cite to Galera et al., with the lower
right region filled by a second ideal gas. They write the state as the
two partial densities, each region holding a partial density $10^{-5}$
of the other component to avoid exact zeros, and $c_v=1$.

## Findings

**Low-dissipation TENO.** Liang et al. compare their TENO scheme with a
local interpolation-like tanh flux at detected discontinuities (see
[TENO-THINC](/methods/teno-thinc.md)) against WENO5-Z, TENO5 and
TENO5-THINC: the new scheme resolves more interfacial and small-scale
structure and sharper shocks (Fig. 20).

**Adaptive moving mesh and entropy stability.** Li, Duan & Tang run
their entropy-stable fifth-order scheme with multi-resolution WENO
dissipation on an [adaptive moving mesh](/methods/adaptive-moving-mesh.md)
(MM-WENOMR), monitor function on the density, on 32 cores. On
$350\times150$ it resolves the Kelvin–Helmholtz roll-up better than the
uniform $1050\times450$ mesh and than the moving mesh with WENO-JS
dissipation. CPU times are 3 min 21 s (MM-WENOMR), 3 min 3 s
(MM-WENOJS), 49 s (uniform $350\times150$) and 18 min 7 s (uniform
$1050\times450$) (Table 5.2). They state that MM-WENOMR takes 18.9 % of
the CPU time "of MM-WENOMR with $1050\times450$ cells"; the table has no
moving-mesh run of that size, the comparison is with the uniform mesh,
and $201/1087$ is 18.5 % *(compiler check, not in the sources)*. See
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
and [entropy stability](/properties/entropy-stability.md).

## Qualifications

- Both sources judge by density or schlieren-type contours; no error
  measure is given.
- Liang et al. do not state $\gamma$; Li, Duan & Tang are read as arXiv
  v1, not the version of record.
- The single- and two-material versions are different problems: the
  different $\gamma$ of the lower region changes the shock speeds there,
  so their figures are not directly comparable.

# Citations

- [Liang et al. (2022)](/sources/liang-2022.md) — §4.8, Fig. 20.
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Ex. 5.7, Table 5.2 (arXiv v1).
