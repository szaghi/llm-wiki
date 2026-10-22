---
type: Benchmark
title: "Two-dimensional Riemann problems"
description: "Four-quadrant Riemann problems of the two-dimensional Euler equations in the Lax–Liu classification, chiefly configurations 3 and 12; used as diagonally symmetric visual tests of resolution, of the jet's sideband and neck instabilities and of scale invariance."
status: established
aliases: [2D Riemann problem, four-quadrant Riemann problem, Lax–Liu configuration 3, Lax–Liu configuration 12]
tags: [benchmark, low-dissipation, weno, teno, central-scheme]
timestamp: 2026-10-21T12:00:00Z
---

# Two-dimensional Riemann problems

A two-dimensional Riemann problem divides the square into four
quadrants, each with a constant state; the sources that number the
configurations follow Lax & Liu (cited by Takagi et al., Luo & Wu,
Deng and Huang et al.; Wang et al. and Chertock et al. take
configuration 3, and Fu 2023 configuration 12, from Kurganov & Tadmor). Two are used in the bundle:
**configuration 3**, in which a jet forms along the diagonal whose
sideband and neck instabilities serve as a resolution gauge, and
**configuration 12**. The data of both are symmetric under the
exchange $x\leftrightarrow y$, $v_1\leftrightarrow v_2$ *(compiler check,
from the tables below)*, so they also test
[symmetry preservation](/properties/symmetry-preservation.md).
All states use $\gamma=1.4$ and are written $(\rho,v_1,v_2,p)$.

## Configuration 3

With the quadrant split at $(x_0,y_0)$:

| Quadrant | State |
|---|---|
| $x>x_0$, $y>y_0$ | $(1.5,\ 0,\ 0,\ 1.5)$ |
| $x<x_0$, $y>y_0$ | $(0.5323,\ 1.206,\ 0,\ 0.3)$ |
| $x<x_0$, $y<y_0$ | $(0.138,\ 1.206,\ 1.206,\ 0.029)$ |
| $x>x_0$, $y<y_0$ | $(0.5323,\ 0,\ 1.206,\ 0.3)$ |

The sources use three placements and several final times:

| Source | Domain, split | Grid | Final time | Scheme |
|---|---|---|---|---|
| [Deng (2023)](/sources/deng-2023.md) App. A.10 | $[0,1]^2$, $(0.8,0.8)$ | $600\times600$ | 0.8 | [ROUND](/methods/round-scheme.md) |
| [Huang et al. (2026)](/sources/huang-2026.md) §6.6, Eq. (6.8) | $[0,1]^2$, $(0.8,0.8)$ | $600\times600$ | 0.8 | ROUND, LD-ROUND, [WENO3-NN](/methods/learned-weno-weights.md), WENO5-JS |
| [Wang et al. (2023)](/sources/wang-2023-b.md) Example 5 | $[0,1]^2$, $(0.8,0.8)$, free boundaries | $\Delta x=\Delta y=1/400$ | 0.8 | A-WENO with [adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md) |
| [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.3.2 | not restated | $401\times401$, CFL 0.5 | 0.8 | [WENO-Z+M](/methods/weno-z-plus.md) |
| [Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 5 | $[0,1.2]^2$, $(1,1)$, free boundaries | $\Delta x=\Delta y=3/2500$ | 1 | [LCD central-upwind](/methods/lcd-central-upwind-scheme.md) |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.8.1 | $[0,1]^2$, $(0.5,0.5)$ | $1024\times1024$ | 0.3 | [TENO-THINC](/methods/teno-thinc.md) |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.15 (their "second Riemann problem") | $[0,1]^2$, $(0.5,0.5)$, outflow | $320\times320$ | 0.35 | [OEDG](/methods/oedg.md), third order, data scaled by $\lambda\in\{1,100\}$ |

Contours: Deng 40 from 0.14 to 1.7, Luo & Wu 40 from 0.14 to 1.7,
Huang et al. 43 from 0.135 to 1.75, Wang et al. 35 from 0.1 to 1.8.

## Configuration 12

| Quadrant | State |
|---|---|
| $x>0.5$, $y>0.5$ | $(0.5313,\ 0,\ 0,\ 0.4)$ |
| $x<0.5$, $y>0.5$ | $(1,\ 0.7276,\ 0,\ 1)$ |
| $x<0.5$, $y<0.5$ | $(0.8,\ 0,\ 0,\ 1)$ |
| $x>0.5$, $y<0.5$ | $(1,\ 0,\ 0.7276,\ 1)$ |

as printed by [Takagi et al. (2022)](/sources/takagi-2022.md) §4.8.2,
Eq. (34), who call it configuration 12 after Lax & Liu
($1024\times1024$, $t=0.25$).
[Fu (2023)](/sources/fu-2023.md) Fig. 7 reproduces a configuration-12
run showing the density with the TENO discontinuity flags in $x$ and $y$
(43 contours).
[Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.15 name neither a
configuration number nor Lax & Liu; they call their two problems the
"first" ($320\times320$, $t=0.25$) and "second" ($t=0.35$) Riemann
problems. Their printed states coincide, quadrant by quadrant and with
the same split $(0.5,0.5)$, with Takagi et al.'s Eq. (34)
(configuration 12) and Eq. (33) (configuration 3) *(compiler check, not
in the sources: comparison of the printed states)*; on that basis they
are listed here under those configurations.

## Findings across sources

**Jet instabilities as a dissipation gauge.** On configuration 3 the
lower-dissipation schemes resolve the sideband instability of the jet
and the instability along its neck: the LCD central-upwind scheme
against the earlier central-upwind scheme (Chertock et al., Fig. 5.5),
and the adaptive-diffusion CURH flux against the earlier A-WENO flux
(Wang et al., Fig. 5), with the same wording in both papers. Takagi et
al. find TENO-THINC finer than WENO5-Z and TENO5 on both
configurations, with shocks sharp and stable and symmetry preserved
(Figs. 18–19). Luo & Wu find WENO-Z+ about equal to WENO-Z, and
WENO-Z+M better resolved and more symmetric than WENO-IS-I and WENO-Z9
(Fig. 14). Deng resolves the main structures "with less grid number"
than WENO-JS5 on $600\times600$ (Figs. 24, 35); Huang et al. compare
ROUND and LD-ROUND with WENO3-NN and WENO5-JS on the same grid.

**Discontinuity location.** Fu (2023) uses configuration 12 to show
that the TENO stencil-selection flags locate the discontinuities, the
basis of the hybrid TENO scheme with a TENO-based indicator (§3.4,
Fig. 7).

**Scale invariance.** Peng, Sun & Wu multiply both configurations by a
factor $\lambda=100$ (page-local symbol): the OFDG damping grows, they state, to "$\lambda^2$ times
its original magnitudes" and smooths the features, while OEDG matches
its $\lambda=1$ result (Figs. 10–11).

## Other systems

The same four-quadrant construction appears for other equations:
special-relativistic hydrodynamics ([Cui, Ding & Wu 2024](/sources/cui-2024.md)
Example 4, $\gamma=5/3$, $[0,1]^2$, $400\times400$, $t=0.4$, a
mushroom-like structure; the problem is symmetric about $y=x$, so the
quasi-optimal cell-average decomposition is close to the optimal one,
Table 9); the stiff Baer–Nunziato two-phase model
([Balsara et al. 2024](/sources/balsara-2024.md) §X.b, Table XIV,
$400\times400$, $t=0.15$); and the two-dimensional Burgers equation
([Peng, Sun & Wu 2024](/sources/peng-2024.md) Ex. 5.11, quadrant
values $0.5$, $0.8$, $-1$, $-0.2$, $256^2$, $t=0.5$).

## Qualifications

- Deng compares with WENO-JS5 results "in [65]", a reference on an
  improved third-order WENO-Z scheme.
- The configuration-3 runs differ in split, domain and final time
  ($t=0.3$ to $1$), so the jet is at different stages of development in
  different papers; only the three runs with split $(0.8,0.8)$ and
  $t=0.8$ (Deng, Huang et al., Wang et al.) are directly comparable.
- Evidence is visual throughout.

# Citations

- [Deng (2023)](/sources/deng-2023.md) — App. A.10, Figs. 24, 35.
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.6, Eq. (6.8).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §4, Example 5, Fig. 5.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.3.2, Fig. 14.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §5.2, Ex. 5, Fig. 5.5 (arXiv v2).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.8, Figs. 18–19.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.11, Ex. 5.15, Figs. 10–11 (arXiv v1).
- [Fu (2023)](/sources/fu-2023.md) — §3.4, Fig. 7 (reproduced).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — Example 4, Table 9 (arXiv v1).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §X.b, Table XIV.
