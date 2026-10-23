---
type: Benchmark
title: "Woodward–Colella interacting blast waves"
description: "One-dimensional Euler problem of two strong blast waves between reflecting walls, pressures 1000, 0.01 and 100, run to t=0.038; a one-dimensional robustness test whose resolution is measured by the resolution of the density peaks and contacts after the blasts collide, also run as a two-dimensional strip on triangles."
status: established
aliases: [interacting blast waves, two blast waves interaction, Woodward–Colella blast wave, blast wave problem]
tags: [benchmark, weno, teno, low-dissipation, positivity]
timestamp: 2026-10-23T15:15:00Z
---

# Woodward–Colella interacting blast waves

Gas at rest with unit density fills $[0,1]$ between two reflecting
walls. Two thin regions at the ends hold pressures five and four orders
of magnitude above the middle, so two strong blast waves run inwards
and interact. By $t=0.038$ the density shows narrow peaks and contacts
(Fu 2021 single out the peak near $x\approx0.78$). The pressure ratio
$10^5$ makes the problem a robustness test, and the height and position
of the density peaks and the sharpness of the contacts measure
resolution against a fine-grid reference. Thirty-six sources of the
bundle run it, and two more run its left half as a single blast.

## Setup

The common data, printed by Fu (2021), Takagi et al., Ye et al., Wang
et al. (2023b), Wang et al. (2023c), Zhao et al., Chertock et al., Deng, Huang et al., Li, Shu & Qiu,
Wang et al. (2021), Bezgin et al., Fan et al., Hong, Ye & Ye, Hu,
Yuan & Zhao, Huang, Liang & Fu, Li, Chen & Ren, Liang et al., Zhou et
al., Kolluru et al., Lin & Zhu, Zhang & Zhu, Zuo & Zhu (2024b), Chu et al. (2025a), Deng, Jiang & Yan and Fan et al. (2025) (Li et al. differ in one value and the two Chamarthi papers in the position of
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
| [Tang (2024)](/sources/tang-2024.md) §4.3, Eq. (31) | 200, CFL 0.2 | WENO-JS, 4000 | global LF splitting; [TENO-AZ](/methods/adaptive-teno.md) vs TENO-Z, TENO-A, TENO-LAD; boundary conditions not stated |
| [Cernetic et al. (2023)](/sources/cernetic-2023.md) §5.3 | 100 cells at degree 1, 3, 7; 400 cells at degree 1; $f_{\mathrm{CFL}}=0.3$ | same code, 10,000 cells | modal DG with an evolved [artificial-viscosity](/methods/artificial-viscosity.md) field, HLLC; middle pressure printed $0.1$, boundaries not stated (arXiv v2) |
| [Gaburro et al. (2024)](/sources/gaburro-2024.md) §5.1.5 | strip $[0,1]\times[0,0.1]$, polygons, $h=1/1080$, $P_2$, $P_3$ | 1D residual distribution, 50,000 points | quasi-conservative [ADER](/methods/ader-scheme.md)-DG in primitive variables with conservative subcell correction at shocks (arXiv v1) |
| [Kolluru et al. (2024)](/sources/kolluru-2024.md) §3.4, Eq. (9f) | $N_x=1599$, Chebyshev | CLAWPACK HLLE, 8000 cells | spectral relaxation with Fejér–Korovkin and de la Vallée-Poussin kernels ([artificial and spectral viscosity](/methods/artificial-viscosity.md)) (arXiv v2) |
| [Lin & Zhu (2024)](/sources/lin-2024-b.md) Case 3.6 | triangles, 401 vertices along $[0,1]$, strip of width 0.025 | FD WENO5, 20000 | ALW-MR-WENO-3/4/5 vs [MR-WENO](/methods/multi-resolution-weno.md), characteristic-wise, CFL 0.6 |
| [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) Ex. 3.6 | 1200 points or cells | WENO-JS5, 2000 | GMR-WENO3/5/7 vs MR-WENO; boundary conditions and $\gamma$ not printed |
| [Zuo & Zhu (2024b)](/sources/zuo-2024-b.md) Ex. 3.4 | 800 | WENO-JS5, 20000 | [hybrid](/methods/hybrid-weno.md) HMR-WENO5/7/9 vs MR-WENO, CFL 0.6; boundary conditions not stated |
| [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.4, Eq. (55) | 600, CFL 0.2 | exact | right region printed from $x=0.8$; MEG7 (conservative and primitive) vs seventh-order mapped WCNS7M (arXiv v1) |
| [Chu et al. (2025a)](/sources/chu-2025.md) Example 3 | $\Delta x=1/400$, SSP-RK3, CFL 0.4 | LDCU, $\Delta x=1/4000$ | adaptive [low-dissipation central-upwind](/methods/low-dissipation-central-upwind-scheme.md) A-MM, A-WLR (indicator constant 0.1) vs LDCU (arXiv v1) |
| [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) §4.3, Eq. (4.4) | third-order DG, 130 elements (390 DOFs) | high-order FV, 2000 cells | DG with non-uniform [ROUND](/methods/round-scheme.md) subcell limiting |
| [Fan et al. (2025)](/sources/fan-2025.md) Ex. 3.6 | not stated in the text, CFL 0.6 | classical WENO, 2001 | moment-based finite-volume [HWENO-U](/methods/hermite-weno.md) vs HWENO-M, WENO-ZQ |

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

**A hard case for spectral methods.** Kolluru et al. call the
problem "a challenging test case for purely spectral methods" and know
of no shock-capturing spectral scheme tested on it (a scheme of Cai &
Shu that reports good results uses ENO interpolation near
discontinuities and is not purely spectral, as they note). Their dealiased pseudo-spectral
run destabilizes at once; spectral relaxation with the de la
Vallée-Poussin kernel destabilizes "for virtually every choice" of its
parameters, because its oscillations make $\rho$ and $p$ negative so that
the sound speed cannot be computed; with the positive Fejér–Korovkin
kernel it stays positive and stable and is accurate until $t=0.032$,
but does not resolve the fine structure after the interaction (§3.4,
Fig. 17).

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

**Adaptive TENO, DG at equal degrees of freedom, primitive-variable
DG.** Tang must run at CFL 0.2 because TENO-A and TENO-LAD fail above
it; TENO-A shows pronounced unphysical oscillations, and TENO-AZ is
comparable to TENO-LAD and better than TENO-A and TENO-Z (§4.3, Fig. 9);
Tang's CPU-time ratios to TENO-Z are 1.03 (TENO-AZ), 1.30 (TENO-A) and
1.10 (TENO-LAD) (Table 5). Cernetic et al. find the profile improving
with the degree at 100 cells, the degree-7 run on 100 cells matching
the degree-1 run on 400 cells, which has the same number of degrees of
freedom; Krivodonova's moment limiter, as they cite it, is "marginally
better" at low order, and an eighth-order WENO of the literature on 400
cells is closer to the reference with half the degrees of freedom of
their degree-7 run. They conclude that
discontinuities converge at first order and that high-order DG gives
"no magic solution" for them (Figs. 7–8; see
[discontinuous Galerkin](/methods/discontinuous-galerkin.md)). Gaburro
et al. find all waves and shock positions correct against the
residual-distribution reference and visual convergence from $P_2$ to
$P_3$ (Fig. 4), with the conservative update confined to the
shock-triggered subcells.

**A Riemann-solver-free scheme at the contact.** Chu et al. (2025a)
find the minmod-indicator scheme A-MM better than the Minmod2-limited
LDCU scheme and the weak-local-residual scheme A-WLR better still, with
"superb resolution" of the contact near $x=0.6$; they state that A-WLR
is, to their knowledge, "the first Riemann-problem solver-free scheme"
to resolve that contact sharply (Fig. 4.4). Deng, Jiang & Yan find their third-order DG/FV-ROUND on 390
DOFs competitive with a ninth-order DG with first-order subcell
correction of Vilar on 540 DOFs, as published, and slightly better at
the contact at $x=0.6$ (Fig. 9). Fan et al. (2025) find HWENO-U better
resolved than HWENO-M and WENO-ZQ (Fig. 10), at a total CPU time between
the two (Table 7).

**Multi-resolution WENO of the Zhu group.** Lin & Zhu (Case 3.6, Fig.
3.7), Zhang & Zhu (Ex. 3.6, Figs. 3.11–3.12) and Zuo & Zhu (2024b,
Ex. 3.4, Figs. 3.4–3.5) compare their schemes with MR-WENO of the same
order on this problem: Lin & Zhu find the two-stencil ALW schemes
comparable, Zhang & Zhu say GMR-WENO "perform better", and Zuo & Zhu (2024b)
show the HMR-WENO density against the reference with the troubled cells
and call the scheme "adept at identifying the troubled cells". The
costs: 5274.56 s for ALW-MR-WENO-5 against 8343.94 s for MR-WENO-5
(ratio 0.63; Lin & Zhu, Table 3.1, hardware not stated), and 1.3388,
2.9974 and 7.9915 s for HMR-WENO against 3.7314, 6.6907 and 10.310 s for
MR-WENO at orders 5, 7, 9 (Zuo & Zhu 2024b, Table 3.1, a laptop).

## Single blast

[Jiang et al. (2024)](/sources/jiang-2024.md) §5.1.2 run the left half
of the problem as a single blast on $[-0.5,0.5]$: $(\rho,p)=(1,1000)$ on
the left and $(1,0.01)$ on the right, at rest, to $t=0.012$, with
particle spacing $\Delta x_0=0.0025$, against a WENO-Z run on 5000
points: their Lagrangian weighted-least-squares particle method with
WENO-Z-type pair states captures pressure and internal energy close to
the reference (Fig. 7). There is no interaction of two blasts, so the
run tests the strong pressure ratio only.

[Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) Eq. (69) run
the same left half on $[0,1]$, $(1,0,1000)$ for $x<0.5$ and $(1,0,0.01)$
beyond, transmissive boundaries, to $t=0.012$ on 200 cells at CFL 0.9,
with ADER finite-volume schemes of orders 5 to 10; they recall that the
exact solution has a shock with pressure ratio 46000 and Mach number
198. With Jiang–Shu WENO reconstruction, orders 5 and 6 oscillate
significantly at the contact and orders 7 to 10 crash on negative
pressures or densities for every CFL number tried in $[0.2,0.9]$; their
[AENO-C reconstruction](/methods/aeno-reconstruction.md) shows no visible
spurious oscillations at any order (Fig. 15), and at sixth order it is
nearly twice as efficient as WENO in CPU time to an $L^1$ error of
$0.01$ (Fig. 16). They run the half problem because the full two-blast
problem gives negative pressures with their high-order schemes,
AENO-C included, around $t\approx0.028$, when the shocks collide, as
stated (§7.2); see [ADER](/methods/ader-scheme.md).

## Two-dimensional strip on triangles

Zhao et al. §4.5 run the same data on $[0,1]\times[0,0.25]$ with
reflecting boundaries on all sides, on a triangular mesh with $h=1/400$,
CFL 0.8, $t=0.038$, with their fourth-order compact gas-kinetic scheme,
and plot density and velocity along the horizontal centreline against
a reference, as a robustness test on unstructured meshes (Fig. 8). Lin
& Zhu's Case 3.6 is likewise a thin strip of triangles, 401 vertices
along $[0,1]$ and 11 across $[-0.0125,0.0125]$, run as a 1D problem.

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

- Kolluru et al. give the Fejér–Korovkin parameters as $(1.35,0.99)$ in
  the text and $(1.355,0.999)$ in the Fig. 17 caption.
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
- Cernetic et al. print the middle pressure as $0.1$, ten times the
  $0.01$ of the other sources, and mix order and degree in their text
  ("order $p=2,4,8$" for the runs their Fig. 7 labels $p=1,3,7$); the
  degrees above follow the figure.
- Tang's Table 5 prints the TENO-A ratio 1.30 on this problem, where
  Tang's times give $2.0913/1.5552=1.345$ *(compiler check, not in the
  sources)*.
- Gaburro et al. call the problem "a standard low energy benchmark".
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
- [Chu et al. (2025a)](/sources/chu-2025.md) — §4.1, Example 3, Fig. 4.4 (arXiv v1).
- [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) — §4.3, Eq. (4.4), Fig. 9.
- [Fan et al. (2025)](/sources/fan-2025.md) — Ex. 3.6, Fig. 10, Table 7.
- [Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) — §7.2, Eq. (69), Figs. 15–16.
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
- [Tang (2024)](/sources/tang-2024.md) — §4.3, Eq. (31), Fig. 9, Table 5.
- [Cernetic et al. (2023)](/sources/cernetic-2023.md) — §2.5, §5.3, Figs. 7–8 (arXiv v2).
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — §5.1.5, Fig. 4 (arXiv v1).
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §5.1.2, Fig. 7.
- [Kolluru et al. (2024)](/sources/kolluru-2024.md) — §3.4, Eq. (9f), Fig. 17 (arXiv v2).
- [Lin & Zhu (2024)](/sources/lin-2024-b.md) — Case 3.6, Fig. 3.7, Table 3.1.
- [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) — Ex. 3.6, Figs. 3.11–3.12.
- [Zuo & Zhu (2024b)](/sources/zuo-2024-b.md) — Ex. 3.4, Figs. 3.4–3.5, Table 3.1.
