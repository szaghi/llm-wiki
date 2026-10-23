---
type: Benchmark
title: "Triple-point problem"
description: "Two-dimensional three-state Riemann problem on [0,7]×[0,3] in which a shock from a high-pressure strip runs along two regions of different density, producing a vortex at the triple point with Kelvin–Helmholtz roll-up; run with one material and with two or three materials of different specific-heat ratio, as a test of interface and small-scale resolution and of multi-phase discretizations."
status: established
aliases: [tri-point problem, triple point shock interaction, three-state Riemann problem]
tags: [benchmark, low-dissipation, multiphase, teno]
timestamp: 2026-10-23T05:41:00Z
---

# Triple-point problem

The triple-point problem is a two-dimensional Riemann problem with three
constant states at rest on $[0,7]\times[0,3]$. A high-pressure strip
$x<1$ drives a shock to the right into two regions of equal low pressure
separated by a horizontal interface at $y=1.5$: one dense, one light.
The shock moves at different speeds in the two regions, so the interface
is sheared and rolls up into a vortex at the point where the three
regions meet, with [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md)
roll-up along it. The sources compare the amount of roll-up resolved
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
[Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.17 (arXiv v2) runs
the two-material version after Pan et al. with the
[five-equation model](/definitions/five-equation-model.md): states
$(\rho,v_1,v_2,p,\gamma)=(1,0,0,1,1.5)$ on $[0,1]\times[0,3]$,
$(1,0,0,0.1,1.4)$ in the lower right and $(0.125,0,0,0.1,1.5)$ on
$[1,7]\times[1.5,3]$, the ratios of specific heats of Li, Duan & Tang;
domain $[0,7]\times[0,3]$, reflective boundaries, $1792\times768$
points, $t=5$. Chamarthi prints the lower-right region as
"$[1,1]\times[0,1.5]$", which is degenerate; the domain and the other
two regions fix it as $[1,7]\times[0,1.5]$ *(compiler check, not in the
sources)*.

[Paula, Adami & Adams (2023)](/sources/paula-2023.md) §7.5 run a
**three-material** version after Pan et al. and earlier work: on
$[0,7]\times[0,3]$ with the triple point at $(1,1.5)$, three ideal gases
$(\rho,v,p,\gamma)=(1,0,1,1.5)$ in the left strip, $(0.125,0,0.1,1.5)$
in the upper right and $(1,0,0.1,1.4)$ in the lower right, each region
a separate phase, symmetry boundaries on all sides, $3584\times1536$
cells, $t=5$, CFL 0.15. The states and ratios of specific heats are
those of Chamarthi and of Li, Duan & Tang; the left strip and the upper
right, which carry the same gas there, are separate phases here.

[Ji, Liang & Fu (2023)](/sources/ji-2023.md) §4.8 run the
single-material version with the states of Liang et al. (printed in
their Fig. 18) and $\gamma=1.4$, on 210,000 ($h\approx1/100$) and
840,000 ($h\approx1/200$) quadrilaterals to $t=5$, with their
unstructured dual-stencil-selection TENO4-D to TENO7-D against
[CWENO](/methods/cweno.md) of the same order in
[UCNS3D](/software/ucns3d.md).
[Trojak & Dzanic (2024)](/sources/trojak-2024.md) §5.1.5 (arXiv v1) run
the two-material version after Galera et al., with the densities and
pressures of the table, $\gamma=1.5$ in the left strip and the upper
right and $1.4$ in the lower right, $c_v=1$ and $c_p=\gamma$ for both
species, slip adiabatic walls on all sides, $\mathbb P_3$ DG on
$2800\times1200$ uniform quadrilaterals, density at $t=1,\dots,6$.

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

**Gradient-based reconstruction for two materials.** Chamarthi uses
HLLC with interface velocities consistent with it in the
volume-fraction equation, and finds no oscillations at the material
interface and the thinnest interface with MIG4
([gradient-based reconstruction](/methods/gradient-based-reconstruction.md)
with an [MP limiter](/methods/monotonicity-preserving-limiter.md)); its
vorticity on $1792\times768$ is comparable to, and in places "much more
enhanced than", that of Pan et al. on $3584\times1536$ (Fig. 23). Chamarthi labels the waves C1–C3, S1,
S2, TS1, TS2 and RS1.

**Discrete equations with interface capturing.** Paula et al. run
their robust [discrete-equations method](/methods/discrete-equations-method.md)
RDEMIC with time-averaged multi-dimensional
[THINC](/methods/thinc-reconstruction.md) for the volume fractions,
WENO3 for the other variables and HLLC. The vortex at the triple point
rolls up all three phases, and thin filaments break up within it into
small-scale structures; the wave system and the interface deformation
are in "very good agreement" with the high-resolution results of Pan et
al. (numerical schlieren and density at $t=3$ and $5$, Fig. 18). The CFL
number is lowered to 0.15 "to prevent loss of positivity", because the
normalisation of the THINC volume fractions for more than two phases
can make their positivity-preserving time integration ineffective; that
positivity design carries no proof (see
[bound preservation](/properties/bound-preservation.md)).

**Unstructured TENO and multi-species entropy filtering.** Ji, Liang
& Fu (2023) find the higher-order TENO-D less dissipative, resolving
the interfacial instability better, and TENO-D better than CWENO of the
same order, "particularly in the vicinity of the tips of the mushroom
structures" (§4.8, Figs. 19–20). Trojak & Dzanic's positivity-preserving
[entropy filter](/methods/entropy-filtering.md) for two-species DG
resolves the Kelvin–Helmholtz roll-up well, and they state that the
results "compare favourably" with Kolev & Rieben, without a
side-by-side figure (Figs. 10–11).

## Qualifications

- All six sources judge by density, vorticity or schlieren-type
  contours; no error measure is given.
- Ji, Liang & Fu (2023) print at the end of their §4.8 a sentence on
  final time $t=0.25$ and a tetrahedral mesh that belongs to their 3D
  explosion of §4.9; the triple-point figures are at $t=5$ on
  quadrilaterals.
- Liang et al. do not state $\gamma$; Li, Duan & Tang are read as arXiv
  v1, not the version of record.
- The single- and two-material versions are different problems: the
  different $\gamma$ of the lower region changes the shock speeds there,
  so their figures are not directly comparable.

# Citations

- [Liang et al. (2022)](/sources/liang-2022.md) — §4.8, Fig. 20.
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Ex. 5.7, Table 5.2 (arXiv v1).
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.17, Eq. (84), Fig. 23 (arXiv v2).
- [Paula, Adami & Adams (2023)](/sources/paula-2023.md) — §7.5, Figs. 17–18.
- [Ji, Liang & Fu (2023)](/sources/ji-2023.md) — §4.8, Figs. 18–20.
- [Trojak & Dzanic (2024)](/sources/trojak-2024.md) — §5.1.5, Figs. 10–11 (arXiv v1).
