---
type: Benchmark
title: "Woodward–Colella interacting blast waves"
description: "One-dimensional Euler problem of two strong blast waves between reflecting walls, pressures 1000, 0.01 and 100, run to t=0.038; a one-dimensional robustness test whose resolution is measured by the resolution of the density peaks and contacts after the blasts collide, also run as a two-dimensional strip on triangles."
status: established
aliases: [interacting blast waves, two blast waves interaction, Woodward–Colella blast wave, blast wave problem]
tags: [benchmark, weno, teno, low-dissipation, positivity]
timestamp: 2026-10-23T20:00:00Z
---

# Woodward–Colella interacting blast waves

Gas at rest with unit density fills $[0,1]$ between two reflecting
walls. Two thin regions at the ends hold pressures five and four orders
of magnitude above the middle, so two strong blast waves run inwards
and interact. By $t=0.038$ the density shows narrow peaks and contacts
(Fu 2021 single out the peak near $x\approx0.78$). The pressure ratio
$10^5$ makes the problem a robustness test, and the height and position
of the density peaks and the sharpness of the contacts measure
resolution against a fine-grid reference. Twenty-six sources of the
bundle run it.

## Setup

The common data, printed by Fu (2021), Takagi et al., Ye et al., Wang
et al. (2023b), Wang et al. (2023c), Zhao et al., Chertock et al., Deng, Huang et al., Li, Shu & Qiu,
Wang et al. (2021), Bezgin et al., Fan et al., Hong, Ye & Ye, Hu,
Yuan & Zhao, Huang, Liang & Fu, Li, Chen & Ren, Liang et al. and Zhou et
al. (Li et al. differ in one value and the two Chamarthi papers in the position of
the right break, see Qualifications),
in $(\rho,v,p)$ with $\gamma=1.4$:

$$
(\rho,v,p)(x,0)=\begin{cases}
(1,\ 0,\ 1000), & 0\le x<0.1,\\
(1,\ 0,\ 0.01), & 0.1\le x<0.9,\\
(1,\ 0,\ 100), & 0.9\le x\le1,
\end{cases}
$$

reflecting walls at $x=0$ and $x=1$, final time $t=0.038$.

| Source | Cells / points | Reference | Notes |
|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.5 | 400 | WENO5-JS, 2500 | Roe flux with entropy fix; [TENO-AA](/methods/adaptive-teno.md) vs [WENO-CU6](/methods/weno-cu6.md) |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.5 | 400, also 800–3200 | WENO5-JS, 32000 | CFL 0.35, Roe splitting with entropy fix; [TENO-THINC](/methods/teno-thinc.md) |
| [Ye et al. (2022)](/sources/ye-2022.md) §4.6, Eq. (46) | 400 (text) | WENO-JS, 2500 | [AFTENO](/methods/afteno.md), AFWENO |
| [Li et al. (2022b)](/sources/li-2022-b.md) §4.3.3, Eq. (41) | 400 | WENO7-Z, 4000 | middle pressure printed $0.001$; [WENO-ZN](/methods/weno-zn.md) |
| [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.2.5, Eq. (17) | 401, CFL 0.5 | WENO-Z, 20001 | [WENO-Z+M](/methods/weno-z-plus.md); calibrates its constant |
| [Wang et al. (2023b)](/sources/wang-2023-b.md) Example 1 | $\Delta x=1/400$ | OLD scheme, $\Delta x=1/3200$ | A-WENO with [adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md) |
| [Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 4 | $\Delta x=1/400$ | old CU, $\Delta x=1/4000$ | [LCD central-upwind](/methods/lcd-central-upwind-scheme.md) |
| [Deng (2023)](/sources/deng-2023.md) App. A.7 | 400 | — | [ROUND](/methods/round-scheme.md), NewWENO, WENO-JS5 |
| [Huang et al. (2026)](/sources/huang-2026.md) §6.5 | 400 | WENO5, refined mesh | ROUND, LD-ROUND, [WENO3-NN](/methods/learned-weno-weights.md) |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.7 | 640 | LLF, 100,000 | [OEDG](/methods/oedg.md), with and without [characteristic decomposition](/methods/characteristic-decomposition.md) |
| [Balsara et al. (2024)](/sources/balsara-2024.md) §VIII.d | 1000, on $[-0.5,0.5]$ | third order, 10,000 | HLL, CFL 0.8, orders 3, 5, 7 |
| [Wang & Don (2022)](/sources/wang-2022-b.md) §3.2.2–3.2.3 | 800 (scaled variant) | Ai-WENO-Z, 3200 | [affine-invariant weights](/methods/affine-invariant-weno.md) |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.7 | 800 cells, CFL 0.6 | FD WENO5, 16,000 | moment-based [multi-resolution HWENO](/methods/hermite-weno.md), HLLC; boundary conditions not printed |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.4b | 400, CFL 0.6 | WENO-JS5, 20,000 | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5) vs original WENO5-MR, WENO-AO5, WENO-JS5 |
| [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.3, Eq. (32) | 400, 800; CFL 0.6 | — | [WENO3-NN](/methods/learned-weno-weights.md) vs WENO3-JS, WENO3-Z, WENO3-N, WENO5-JS, WENO5-Z; LLF, characteristic |
| [Fan et al. (2023)](/sources/fan-2023.md) Ex. 3.4 | not recorded | classical WENO, 2001 | finite-difference [Hermite WENO](/methods/hermite-weno.md) HWENO-R vs HWENO-L and WENO-ZQ; linear-weight study |
| [Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.3 | 400 | WENO-JS, 2000 | TENO-M6/M8 ([TENO](/methods/targeted-eno.md) with stencil extension) vs TENO6/8, [WENO-CU6](/methods/weno-cu6.md), WENO-JS, WENO7, WENO9 |
| [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) §5.2, Eq. (5.2) | 500, CFL 0.9 | — | second-order MUSCL with [HLL-family](/methods/hll-riemann-solvers.md) solvers HLLE, HLLEM, RHLLEM-LD; boundaries not stated |
| [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) §4.4 | 400, CFL 0.35 | WENO5-JS, 2000 | Roe flux with entropy fix; five-point TENO with a new [scale sensor](/definitions/scale-sensor.md) vs [TENO5-A](/methods/adaptive-teno.md), TENO5, WENO5-Z |
| [Li, Chen & Ren (2022)](/sources/li-2022.md) §4.2 | 400, CFL 0.6 | WENO-Z, 2000 | MDAD-HY ([MDCD](/methods/mdcd-scheme.md)-type hybrid) with switch threshold $\psi_c=0.5$; TENO-HY with $C_T=10^{-5}$ |
| [Liang et al. (2022)](/sources/liang-2022.md) §4.3 | 400 | WENO5-JS, 2500 | Roe flux with entropy fix; [TENO-THINC](/methods/teno-thinc.md)-family scheme vs TENO5-THINC, TENO5 ($C_T=10^{-4}$), WENO5-Z |
| [Zhou et al. (2023)](/sources/zhou-2023.md) §5.3, Eq. (38) | 400, CFL 0.4 | fifth-order WENO, 4000 | HLLC, TVD-RK3; six-point [WCNS](/methods/weighted-compact-nonlinear-scheme.md) WCNS-SA vs WCNS-LD and ONL6 |
| [Wang et al. (2023c)](/sources/wang-2023-c.md) Example 4.4 | 800, CFL 0.6 | WENO-JS, 20000 | hybrid multi-resolution [WCNS](/methods/weighted-compact-nonlinear-scheme.md) vs MR-WCNS and WENO-JS; boundary conditions not stated, intervals printed open |
| [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) §4.2 | 400 | — | eighth-order compact [gas-kinetic scheme](/methods/gas-kinetic-scheme.md) at CFL 0.4 and 0.8 vs the authors' earlier compact scheme (arXiv v1) |
| [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.13, Eq. (80) | 600, CFL 0.2 | exact | right region printed from $x=0.8$, see Qualifications; [gradient-based](/methods/gradient-based-reconstruction.md) MIG4, MEG6 vs TENO5 (arXiv v2) |
| [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.4, Eq. (55) | 600, CFL 0.2 | exact | right region printed from $x=0.8$; MEG7 (conservative and primitive) vs seventh-order mapped WCNS7M (arXiv v1) |

## Findings across sources

**Density-peak resolution.** The new scheme of each paper sharpens the
peaks and contacts of its baseline. Fu (2021) gets a better density peak
at $x\approx0.78$ than WENO-CU6, free of WENO-CU6's pressure oscillations
and velocity overshoot near $x\approx0.86$ (Fig. 6). Takagi et al.
resolve the contact "significantly better" than WENO5-Z and TENO5
(Fig. 8). Li et al. find WENO-ZN less dissipative than WENO-JS and
WENO-Z (Fig. 6); Ye et al. find AFTENO closest to the reference in
density and pressure (Fig. 6); Chertock et al. and Wang et al. (2023b) report
"slightly" better resolution of the second density spike with their
new central-upwind fluxes (Figs. 5.4 and 1); Deng finds low-dissipation
ROUND better than WENO-JS5 (Fig. 33). In one dimension Wang et al.
(2023b) expect no large gain, because their dissipation switch is
inactive there (§4.1). Li, Shu & Qiu find the HWENO with modified first
moments "much better" resolved and sharper than the unmodified one
(Fig. 3.5, comment p. 31). Wang et al. (2021) find their New WENO5
similar to WENO-AO5, both better than WENO-JS5 and the original
multi-resolution WENO5, at about 0.67 of the latter's cost (0.76 s
against 1.14 s; Fig. 5.8). Among TENO variants, Hong, Ye & Ye find
TENO6 and TENO-M6 alike and much better than WENO-JS near the valley at
$x\approx0.75$ and the peak at $0.78$, WENO-CU6 overshooting near the
left peak at $0.65$, and TENO8/TENO-M8 less dissipative than WENO7 and
slightly better than WENO9 (§5.3, Fig. 11); Huang, Liang & Fu find
TENO5-A and their scale-sensor scheme better than WENO5-Z and TENO5 at
the $0.78$ peak (§4.4, Fig. 7); Liang et al. capture the shocks as
sharply as WENO5-Z and TENO5 and resolve the peak "slightly better"
(§4.3, Fig. 9). Fan et al. find HWENO-R and HWENO-L better than WENO-ZQ
and HWENO-R slightly better than HWENO-L (Ex. 3.4, Fig. 3.4). With only
a second-order MUSCL reconstruction, Hu, Yuan & Zhao find their
RHLLEM-LD Riemann solver giving "obviously higher resolution for all
waves" than HLLE and HLLEM (§5.2, Fig. 5.2): the problem also ranks
Riemann solvers, not only reconstructions.

Chamarthi (2023a) finds MIG4 and MEG6 predicting the density extrema
"virtually identical[ly]" and better than TENO5, and MIG4 capturing the
velocity discontinuity at $x\approx0.87$ within one cell, where TENO5
and MEG6 need more (Fig. 17). Chamarthi (2023b) finds all schemes free
of oscillations, the density extrema best predicted by MEG7 with
primitive variables, and the same discontinuity captured with fewer
cells by MEG7 than by WCNS7M (Fig. 6).
Wang et al. (2023c) find their hybrid multi-resolution WCNS better
than the original MR-WCNS and WENO-JS on the same grid, its switch
marking the two shock structures over time, at 0.81 of WENO-JS's CPU
time against 1.64 for MR-WCNS (Fig. 4.6, Table 5.1).
Zhou et al. obtain stable solutions with all three of their six-point
WCNS, ONL6 and WCNS-SA giving a slightly better density than WCNS-LD at
the valley and the second peak (§5.3, Fig. 12).

**Robustness and the stability margin of very-high-order schemes.**
Luo & Wu use the problem to choose the largest admissible constant of
WENO-Z+M: it runs with 579 and fails with 580 on 401 points, and 579 is
then fixed for all tests (§3.2, Fig. 13); ninth-order WENO-Z fails
outright, so seventh order is shown instead (§5.2.5). Peng et al. find
that the earlier OFDG without characteristic decomposition smears
strongly, whereas OEDG works with or without it (Fig. 4). Balsara et al.
show the shock positions converging at orders 3, 5 and 7 on 1000 zones
(Fig. 10).

**Time-step limit of compact schemes.** Zhao et al. use the problem
to show that their compact gas-kinetic scheme, which evolves separate
left and right interface states and limits the high-order time
derivatives of the flux, runs at CFL 0.8 where their earlier
eighth-order compact scheme with the same reconstruction "can only use
CFL number 0.2" (Fig. 5).

**A cut-off for learned weights.** Bezgin et al. use the problem to
motivate the test-time "ENO layer" of WENO3-NN, a TENO-like cut-off
($2\times10^{-4}$) followed by renormalization: the network alone
cannot output essentially zero weights, because its softmax output
saturates, so spurious oscillations pass and at these very strong
shocks it can reconstruct negative densities or pressures (§3.2,
App. A.4, Fig. 21). With the cut-off, WENO3-NN on 400 points is similar
to WENO3-JS on 800 and gives the best density of the three-point schemes
(§4.3, Fig. 11).

**Grid convergence and the TENO cut-off.** Takagi et al. refine from
400 to 3200 points: with $C_T=10^{-4}$ the solution converges
monotonically to the reference, whereas with the default
$C_T=10^{-5}$ a small overshoot appears near the strong contact at the
highest resolutions (Fig. 9). Liang et al. likewise run TENO5 with
$C_T=10^{-4}$, which it needs "to run stably" here (§4.3), while Li,
Chen & Ren run their TENO-HY comparator with $C_T=10^{-5}$ and tune
their hybrid's switch threshold per problem ($\psi_c=0.5$ here,
against 0.4 and 0.8 on the [Sedov problem](/benchmarks/sedov-blast-wave.md);
§4.2). See [TENO](/methods/targeted-eno.md).

**Linear weights.** Fan et al. use the problem to study the linear
weights of HWENO-R, which they state may be arbitrary positive numbers
summing to one: nine flux sets G1–G9 and nine derivative-limiter sets
D1–D9 (Table 3.4) show that the resolution depends strongly on them,
and they recommend the linear weights $(0.99,0.005,0.005)$ for the
flux and $(0.9,0.05,0.05)$ for the limiter, central-to-side ratios in
$[100,300]$ and $[10,30]$ respectively giving similar results (§3, Ex. 3.4,
Figs. 3.5–3.7). The caption of Table 3.4 reads "(Gk,Dk)", the text
"(Dk,Gk)".

## Two-dimensional strip on triangles

Zhao et al. §4.5 run the same data on $[0,1]\times[0,0.25]$ with
reflecting boundaries on all sides, on a triangular mesh with $h=1/400$,
CFL 0.8, $t=0.038$, with their fourth-order compact gas-kinetic scheme,
and plot density and velocity along the horizontal centreline against
a reference, as a robustness test on unstructured meshes (Fig. 8).

## Scaled variant

[Wang & Don (2022)](/sources/wang-2022-b.md) §3.2.2 test
[scale invariance](/properties/scale-invariance.md) with the data
$(\rho,v,p)=(0,0,P_\infty)+\lambda\,(1,0,10^3)$, $\lambda\,(1,0,10^{-2})$,
$\lambda\,(1,0,10^2)$ on the three intervals, with scaling factor
$\lambda=10^{-7}$ and offset $P_\infty=1$ (page-local symbols), $t=0.001$, 800 points, $\epsilon=10^{-12}$ (so
$\epsilon>\lambda^2$). Classical WENO-Z oscillates at both strong and
weak shocks, a scale-invariant variant reduces but does not remove the
oscillations, and the affine-invariant WENO-Z is essentially
non-oscillatory (Fig. 6). Their §3.2.3 then runs the unscaled problem
with specifications deferred to an earlier paper (Fig. 7).

## Qualifications

- Chamarthi (2023a) and (2023b) both print the low-pressure region as
  $0.1\le x<0.8$ and the right high-pressure region as $0.8\le x\le1.0$
  (Eqs. (80) and (55)), against $0.1\le x<0.9$ and $0.9\le x\le1$ in all
  other sources, while citing Woodward & Colella; with the printed data
  the right reservoir holds twice the energy of the common setup
  *(compiler check, not in the sources)*. The papers compare with an
  exact solution without saying for which data, so whether $0.8$ is a
  printed slip or the data run cannot be decided from them.

- Li et al. print the middle pressure as $0.001$ (Eq. (41)) where Fu
  (2021), Takagi et al., Ye et al., Wang et al. (2023b), Chertock et
  al., Deng, Huang et al., Li, Shu & Qiu, Wang et al. (2021) and
  Bezgin et al. print $0.01$; whether this is a misprint or the value run cannot be decided
  from the paper.
- Balsara et al. place the problem on $[-0.5,0.5]$; their initial
  states are not recorded on this page.
- Hu, Yuan & Zhao print the intervals $[0,0.1]$, $(0.1,0.9]$, $(0.9,1]$
  and Li, Chen & Ren $(0,0.1]$, $(0.1,0.9]$, $(0.9,1]$; Hu et al. state
  no boundary conditions.
- Huang, Liang & Fu attribute the problem to "Woodward and Colella" while
  their reference list prints only Woodward as author.
- Ye et al. give 400 points in the text and $N=1500$ in the caption of
  Fig. 6.
- Zhao et al. write in the text that their earlier scheme "can only use
  CFL number 0.2", while the legend of their Fig. 5 shows it at CFL 0.1
  (arXiv v1).
- Wang et al. (2023b) compute their reference with the OLD scheme
  against which the NEW one is compared.
- Li, Shu & Qiu print the intervals as open, $(0,0.1)$, $(0.1,0.9)$,
  $(0.9,1)$, and state no boundary conditions or $\gamma$ for this
  problem.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.5, Fig. 6 (arXiv v1).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.5, Figs. 8–9.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.6, Eq. (46), Fig. 6.
- [Li et al. (2022b)](/sources/li-2022-b.md) — §4.3.3, Eq. (41), Fig. 6.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §3.2, Fig. 13; §5.2.5, Eq. (17).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4.1; Example 1, Fig. 1.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §5.1, Ex. 4, Fig. 5.4 (arXiv v2).
- [Deng (2023)](/sources/deng-2023.md) — App. A.7, Figs. 15d, 23, 33.
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.5.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.7, Fig. 4 (arXiv v1).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §VIII.d, Fig. 10.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.2–3.2.3, Figs. 6–7.
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — Ex. 3.7, Fig. 3.5; comment p. 31 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.4b, Fig. 5.8.
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §3.2; §4.3, Eq. (32), Fig. 11; App. A.4, Fig. 21.
- [Fan et al. (2023)](/sources/fan-2023.md) — §3, Ex. 3.4, Table 3.4, Figs. 3.4–3.7.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §5.3, Fig. 11.
- [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) — §5.2, Eq. (5.2), Fig. 5.2.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §4.4, Fig. 7 (arXiv v1).
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §4.2, Fig. 17.
- [Liang et al. (2022)](/sources/liang-2022.md) — §4.3, Fig. 9.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.13, Eq. (80), Fig. 17 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Ex. 3.4, Eq. (55), Fig. 6 (arXiv v1).
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §5.3, Eq. (38), Fig. 12.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — Example 4.4, Eq. (4.4), Fig. 4.6, Table 5.1.
- [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) — §4.2, §4.5, Figs. 5, 8 (arXiv v1).
