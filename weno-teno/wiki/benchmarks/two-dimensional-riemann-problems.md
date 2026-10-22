---
type: Benchmark
title: "Two-dimensional Riemann problems"
description: "Four-quadrant Riemann problems of the two-dimensional Euler equations in the Lax–Liu classification, chiefly configurations 3 and 12 plus a four-contact spiral; used as visual tests of resolution, of the jet's sideband and neck instabilities, of scale invariance and of moving-mesh efficiency, with MHD and Burgers relatives."
status: established
aliases: [2D Riemann problem, four-quadrant Riemann problem, Lax–Liu configuration 3, Lax–Liu configuration 12]
tags: [benchmark, low-dissipation, weno, teno, central-scheme]
timestamp: 2026-10-22T00:00:00Z
---

# Two-dimensional Riemann problems

A two-dimensional Riemann problem divides the square into four
quadrants, each with a constant state; the sources that number the
configurations follow Lax & Liu (cited by Takagi et al., Luo & Wu,
Deng and Huang et al.; Wang et al. (2023) and Chertock et al. take
configuration 3, and Fu 2023 configuration 12, from Kurganov & Tadmor). Three are used in the bundle:
**configuration 3**, in which a jet forms along the diagonal whose
sideband and neck instabilities serve as a resolution gauge,
**configuration 12**, and a configuration of four contacts that roll up
into a spiral. The data of the first two are symmetric under the
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
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.6 ("four shocks") | $[0,1]^2$, $(0.8,0.8)$ | $400\times400$, CFL 0.6 | 0.8 | [multi-resolution WENO](/methods/multi-resolution-weno.md) vs WENO-JS5, WENO-AO5 |

Contours: Deng 40 from 0.14 to 1.7, Luo & Wu 40 from 0.14 to 1.7,
Huang et al. 43 from 0.135 to 1.75, Wang et al. (2023) 35 from 0.1 to 1.8.

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
[Pazner (2021)](/sources/pazner-2021.md) §5.6 prints the same data in
exact form: $\rho=4/5$, $v=0$, $p=1$ on $(0,\tfrac12)^2$; $\rho=1$ with
$v=(3/\sqrt{17},0)$ and $v=(0,3/\sqrt{17})$, $p=1$, in the upper-left
and lower-right quadrants; $\rho=17/32$, $v=0$, $p=2/5$ on
$(\tfrac12,1)^2$ ($3/\sqrt{17}=0.72761$, $17/32=0.53125$, *compiler
check*). He makes the problem periodic on $[0,2]^2$ by reflection about
$(1,1)$ and runs it to $t=0.25$.
[Li, Duan & Tang (2022)](/sources/li-2022-c.md) Ex. 5.3, their "2D
Riemann problem I", print the decimal states of the table above,
citing Brio, Zakharian & Webb (2001), and run to $t=0.25$.
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

## A four-contact configuration

[Li, Duan & Tang (2022)](/sources/li-2022-c.md) Ex. 5.4, their "2D
Riemann problem II", citing Lax & Liu without a configuration number:

| Quadrant | State |
|---|---|
| $x>0.5$, $y>0.5$ | $(1,\ 0.75,\ -0.5,\ 1)$ |
| $x<0.5$, $y>0.5$ | $(2,\ 0.75,\ 0.5,\ 1)$ |
| $x<0.5$, $y<0.5$ | $(1,\ -0.75,\ 0.5,\ 1)$ |
| $x>0.5$, $y<0.5$ | $(3,\ -0.75,\ -0.5,\ 1)$ |

The pressure is uniform and the four initial discontinuities are
contacts, which roll up into a spiral; $t=0.3$. The data are not
symmetric under $x\leftrightarrow y$, $v_1\leftrightarrow v_2$ *(compiler
check)*.

## Findings across sources

**Jet instabilities as a dissipation gauge.** On configuration 3 the
lower-dissipation schemes resolve the sideband instability of the jet
and the instability along its neck: the LCD central-upwind scheme
against the earlier central-upwind scheme (Chertock et al., Fig. 5.5),
and the adaptive-diffusion CURH flux against the earlier A-WENO flux
(Wang et al. 2023, Fig. 5), with the same wording in both papers. Takagi et
al. find TENO-THINC finer than WENO5-Z and TENO5 on both
configurations, with shocks sharp and stable and symmetry preserved
(Figs. 18–19). Luo & Wu find WENO-Z+ about equal to WENO-Z, and
WENO-Z+M better resolved and more symmetric than WENO-IS-I and WENO-Z9
(Fig. 14). Deng resolves the main structures "with less grid number"
than WENO-JS5 on $600\times600$ (Figs. 24, 35); Huang et al. compare
ROUND and LD-ROUND with WENO3-NN and WENO5-JS on the same grid.

Wang et al. (2021) find both multi-resolution WENO5 schemes capturing
more roll-up than WENO-JS5 and WENO-AO5 on configuration 3 (Fig. 5.12).
Pazner compares $N=1$ on $128^2$ elements with $N=3$ on $64^2$, the same
number of degrees of freedom, on configuration 12: $N=3$ gives sharper
interfaces and better small-scale features (Fig. 12).

**Moving meshes against uniform ones.** Li, Duan & Tang compare their
[adaptive moving mesh](/methods/adaptive-moving-mesh.md) multi-resolution
WENO (MM-WENOMR) with uniform meshes on 4 cores. On configuration 12,
MM-WENOMR on $200^2$ (2 min 56 s) has sharper shocks than the uniform
$500^2$ run (7 min 9 s), at 41.0 % of its CPU time; MM-WENOJS on $200^2$
takes 2 min 37 s. On the four-contact problem MM-WENOMR on $200^2$
(2 min 50 s) costs 21.5 % of the uniform $600^2$ run (13 min 10 s) and
7.6 % more than MM-WENOJS, and resolves more small-scale roll-up
(Ex. 5.3–5.4, Table 5.1).

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
values $0.5$, $0.8$, $-1$, $-0.2$, $256^2$, $t=0.5$; the same quadrant
values in [Pazner 2021](/sources/pazner-2021.md) §5.5, see
[Burgers equation tests](/benchmarks/burgers-equation-tests.md)).

[Kanbar, Touma & Klingenberg (2022)](/sources/kanbar-2022.md) §5.2 run
an ideal-MHD four-state problem with the uniform field $B=(2,0,1)$ and
$(\rho,v_1,v_2,p)=(1,0.75,0.5,1)$ for $x>0,y>0$, $(2,0.75,0.5,1)$ for
$x<0,y>0$, $(1,-0.75,0.5,1)$ for $x<0,y<0$, $(3,-0.75,-0.5,1)$ for
$x>0,y<0$, on $[-1,1]^2$ with $400\times400$ cells to $t=0.8$. Its
hydrodynamic states are those of the four-contact configuration above
except the sign of $v_2$ in the first quadrant ($0.5$ against $-0.5$)
*(compiler check: comparison of the printed states)*. With the
constrained transport step of their
[unstaggered central scheme](/methods/unstaggered-central-scheme.md) the
discrete divergence of $B$ stays at the $10^{-14}$ level, without it it
reaches $O(1)$, while the density is visually the same (Figs. 4–5); see
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

## Qualifications

- Deng compares with WENO-JS5 results "in [65]", a reference on an
  improved third-order WENO-Z scheme.
- The configuration-3 runs differ in split, domain and final time
  ($t=0.3$ to $1$), so the jet is at different stages of development in
  different papers; only the four runs with split $(0.8,0.8)$ and
  $t=0.8$ (Deng, Huang et al., Wang et al. 2023, Wang et al. 2021) are
  directly comparable.
- Li, Duan & Tang's Ex. 5.4 says its monitor function and linear
  weights are those of Ex. 5.2, which states no linear weights; the
  non-default weights $(0.95,0.045,0.005)$ are set in Ex. 5.3.
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
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.6, Fig. 5.12.
- [Pazner (2021)](/sources/pazner-2021.md) — §5.5–5.6, Figs. 11–12 (arXiv v1).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Ex. 5.3–5.4, Table 5.1 (arXiv v1).
- [Kanbar, Touma & Klingenberg (2022)](/sources/kanbar-2022.md) — §5.2, Figs. 4–5 (arXiv v1).
