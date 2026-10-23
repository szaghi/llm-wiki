---
type: Benchmark
title: "Sod and Lax shock tubes"
description: "The two most often run one-dimensional Euler Riemann problems with exact solutions, Sod's mild tube and Lax's stronger one, run by most sources as the first check of shock and contact capturing; records each source's placement, grid and final time, the printed variants and the multicomponent, stiffened-gas and relaxation relatives."
status: established
aliases: [Sod problem, Sod shock tube, Lax problem, Lax shock tube, Riemann problem of Lax, Lax–Harden problem]
tags: [benchmark, weno, teno, riemann-solver]
timestamp: 2026-10-23T15:15:00Z
---

# Sod and Lax shock tubes

Both are one-dimensional Riemann problems of the Euler equations with
$\gamma=1.4$: two constant states separated by a diaphragm at the
middle of the tube. Each has an exact solution containing a shock and
a contact discontinuity, so the benchmark checks whether a scheme
captures both sharply and without oscillation, before harder problems
are attempted. Lax's data start with a moving left state;
[Huang et al. (2026)](/sources/huang-2026.md) §6.3 describe the problem
as testing a strong shock and contact.

## Sod

$(\rho,v,p)=(1,0,1)$ on the left half of $[0,1]$ and $(0.125,0,0.1)$ on
the right half.

| Source | Grid | Final time | Notes |
|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.3 | 96 points | 0.2 | exact Riemann reference; [TENO-AA](/methods/adaptive-teno.md) |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.3 | 100 | 0.2 | exact reference; [TENO-THINC](/methods/teno-thinc.md) |
| [Ye et al. (2022)](/sources/ye-2022.md) §4.3, Eq. (43) | 200 | 0.2 | mirrored: $(0.125,0,0.1)$ on the left, $(1,0,1)$ on the right; [AFTENO](/methods/afteno.md) |
| [Deng (2023)](/sources/deng-2023.md) App. A.4 | 200 cells | 0.25 | [ROUND](/methods/round-scheme.md), NewWENO |
| [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) §3.5.3, §5.6 | 100 | 0.1 | [Active Flux](/methods/active-flux.md); states and $\gamma$ not printed |
| [Pazner (2021)](/sources/pazner-2021.md) §5.2.1 | 256 DOFs, $N=0,1,3,7$ ($N=7$ on 32 elements) | 0.18 | on $[-\tfrac12,\tfrac12]$; sparse IDP DG with subcell [convex limiting](/methods/convex-limiting.md) |
| [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) §IV.A | 8 space–time quadrilaterals | 0.2 | on $(-0.5,0.5)$; [MDG+ICE shock tracking](/methods/implicit-shock-tracking.md), $\mathbb P^1$–$\mathbb P^3$ |
| [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) §4.2, Eq. (41) | 200 points | 0.2 | on $[-0.5,0.5]$ (from Fig. 3), $\Delta t=5\times10^{-4}$; ninth-order central scheme with adaptive [artificial dissipation](/methods/artificial-viscosity.md) |
| [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.2, Eq. (29) | 200 | 0.2 | finite-volume [WENO3-NN](/methods/learned-weno-weights.md), LLF, characteristic, TVD-RK3 at CFL 0.6 |
| [Hiejima (2022)](/sources/hiejima-2022.md) §3.1, Eq. (26) | 101 points ($101\times21\times21$) | 0.2 | on $[-0.5,0.5]$; [WCNS](/methods/weighted-compact-nonlinear-scheme.md) of interpolation order 5–11, AUSMDV |
| [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.2.1 | $\mathbb P_3$ on 50 and $\mathbb P_9$ on 20 elements (200 DOFs); $N=20$–$160$ for $\mathbb P_2$–$\mathbb P_7$ | 0.2 | [artificial viscosity](/methods/artificial-viscosity.md) from the temporal residual, $c_\mu=5$ (arXiv v2) |
| [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) §5.1.1 | $\mathbb P_3$, $\mathbb P_5$ at about 200 DOFs; $N=40$–$640$ ($L^1$), $20$–$320$ ($L^2$), and $M=100$–$1600$ DOFs, $\mathbb P_2$–$\mathbb P_7$ | 0.2 | flux reconstruction with [entropy filtering](/methods/entropy-filtering.md) (arXiv v3) |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.3.1 | 100 elements | 0.2 | nodal DG with ANN-predicted artificial viscosity |
| [Sousa & Scalo (2022)](/sources/sousa-2022.md) §5.1 | grid study (grids not printed in the text) | 0.2 | diaphragm at $x=0$; Dirichlet left, Neumann right; compact central scheme with [quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md) vs localized artificial diffusion; $\gamma$ not printed (arXiv v2) |
| [Boscarino et al. (2022)](/sources/boscarino-2022.md) Ex. 5.2 | 50 | 0.2 | reflective boundaries; [semi-implicit all-Mach](/methods/semi-implicit-all-mach-scheme.md) WENO S2T2 and S4T3 at $\varepsilon=1$, CFL 0.25 (arXiv v2) |
| [Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.2 | 100 | 0.2 | on $[-0.5,0.5]$, zero-gradient boundaries; TENO-M6/M8 ([TENO](/methods/targeted-eno.md) with stencil extension); $\gamma$ not printed |
| [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) §4.3 | 100 | 0.2 | five-point TENO with a new [scale sensor](/definitions/scale-sensor.md) vs TENO5-A, TENO5, WENO5-Z (arXiv v1) |
| [Liang et al. (2022)](/sources/liang-2022.md) §4.2 | 100 | 0.2 | [TENO-THINC](/methods/teno-thinc.md)-family scheme |
| [Ji, Liang & Fu (2022)](/sources/ji-2022.md) §5.4, Table 6 ("ST01") | Cartesian strip, $h=1/100$; 1967 triangles | 0.2 | unstructured finite-volume TENO3–6, conservative-variable reconstruction; states printed with a column shift, see Qualifications (preprint) |
| [Lesur et al. (2023)](/sources/lesur-2023.md) §4.1 | 500 | 0.2 | [IDEFIX](/software/idefix.md), Roe solver, linear reconstruction, RK2; left pressure printed $0.1$, see Qualifications (arXiv v1) |
| [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) §8.4 | 10 elements, static $N=5$ or $p$-adaptive $N\in[2,5]$ | 0.2 | Dirichlet; Roe with entropy fix; [$p$-adaptive DG](/methods/hp-adaptation.md) with [FV subcells](/methods/subcell-finite-volume-limiting.md), $N_{\mathrm{FV}}=6$ or 11 |
| [Li, Li, Don & Wang (2023)](/sources/li-2023.md) §3.2 | 200 | 2 | mirrored, on $[-5,5]$: $(0.125,0,0.1)$ on $[-5,0)$, $(1,0,1)$ on $[0,5]$; scale-invariant multi-resolution [A-WENO](/methods/alternative-weno.md) |
| [Huang & Zahr (2022)](/sources/huang-2022.md) §6.4.1 | 108 space–time triangles, 84 after element removal | 0.2 | [implicit shock tracking](/methods/implicit-shock-tracking.md) HOIST, $p=2$ (arXiv v2) |
| [Bezgin et al. (2023)](/sources/bezgin-2023.md) §5.1.2, App. A | 100 | 0.2 | zero-gradient boundaries; [JAX-Fluids](/software/jax-fluids.md) with HLLC (primitive WENO5-JS) and Roe-type characteristic flux splitting (arXiv v1) |
| [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.9 | 200 | 0.2 | [gradient-based](/methods/gradient-based-reconstruction.md) MEG6, MIG4 vs TENO5 (arXiv v2) |
| [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.2 | 200 | 0.2 | MEG7 vs WCNS7M; exact Riemann reference (arXiv v1) |
| [Zhou et al. (2023)](/sources/zhou-2023.md) §5.1, Eq. (34) | 100 | 0.2 | on $[-0.5,0.5]$; six-point [WCNS](/methods/weighted-compact-nonlinear-scheme.md) WCNS-SA vs WCNS-LD, ONL6; HLLC, TVD-RK3, CFL 0.4; reference fifth-order WENO on 4000 cells |
| [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) App. A.2 | 200 | $t/t_0=2$ | data "provided by Jiang and Shu", plotted on $x/L_0\in[-5,5]$; extrapolation boundaries; [WENO-Z](/methods/weno-z.md)3/5/7, TENO5, TENO-A5 in [URANOS](/software/uranos.md); 2000-point reference |
| [Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 6 | 300 cells | 0.2 | modified left state $(1,0.75,1)$, see below; transmissive; fifth-order FV IMWENO-P vs WENO-JS, WENO-Z, WENO-NS, WENO-P, MWENO-P |
| [Qin et al. (2023)](/sources/qin-2023.md) §3.4.2 | two blocks: 160 on $[0,0.75]$, 40 on $(0.75,1]$ | 0.1, 0.2 | multi-resolution [WCNS](/methods/weighted-compact-nonlinear-scheme.md) with [boundary closures](/methods/shock-capturing-boundary-closure.md) at the interface |
| [Tang (2024)](/sources/tang-2024.md) §4.3, Eq. (28) | 200 | 0.2 | mirrored: $(0.125,0,0.1)$ on $[0,0.5]$, $(1,0,1)$ on $(0.5,1]$; [TENO-AZ](/methods/adaptive-teno.md) vs TENO-Z, TENO-A, TENO-LAD, global LF splitting; reference WENO-JS on 4000 |
| [Jiang et al. (2024)](/sources/jiang-2024.md) §4.2.1 | particle spacing $\Delta x_0=0.0025$ | 0.15 | on $[-0.5,0.5]$; Lagrangian weighted-least-squares particles with WENO-Z-type pair states vs the GSPH and WENO-SPH particle methods |
| [Kolluru et al. (2024)](/sources/kolluru-2024.md) §3.4, Eq. (9c) | Chebyshev with a mapping, $N_x=615$ | not stated | on $[-1,1]$, reflecting walls; spectral relaxation; reference HyPar characteristic WENO5 on 8000 (arXiv v2) |
| [Lin & Zhu (2024)](/sources/lin-2024-b.md) Case 3.4 | triangles, $201\times11$ vertices | 2 | strip $[-5,5]\times[-0.025,0.025]$, jump at $x=0$; ALW-MR-WENO-3/4/5 vs [MR-WENO](/methods/multi-resolution-weno.md); fourth entries printed $2.5$ and $0.25$, see Qualifications |
| [Naudet & Zahr (2024)](/sources/naudet-2024.md) §5.3.1, Eq. (57) | six space-time slabs, 65 simplices ($q=1$, $p=2$) in the first | 1 | walls at $x=0$ and $1$; space-time [implicit shock tracking](/methods/implicit-shock-tracking.md); reference second-order FV (superbee) on over $10^5$ elements, adaptive RK4 |
| [Danis et al. (2025)](/sources/danis-2025.md) §5.5 | $N^3$ with $N=5\cdot2^n$, $n=1,\dots,7$ (to $640^3$), CFL 0.5 | 0.2 | on $[0,1]^3$, jump at $x=0.5$; [tensor-train](/methods/tensor-train-weno.md) FD WENO5-JS with global LF splitting (arXiv v1) |
| [Abgrall et al. (2026)](/sources/abgrall-2026.md) Ex. 5 | 200 cells | 0.16 | bound-preserving [PAMPA](/methods/pampa-scheme.md), SSP-RK3 at CFL 0.2 |

Abgrall & Barsukow run Sod with three Active Flux variants: sixth order
at CFL 0.25 (Fig. 19); a fifth-order point setup with a third-order
evolution operator at CFL 0.5 (Fig. 24); and seventh order at CFL 0.01
on a periodic tube with discontinuities at $x=1/3$ and $x=2/3$ (Fig. 28),
which doubles the problem so that periodic boundaries can be used.
Pazner, Luo et al., Hiejima, Hong, Ye & Ye and Sousa & Scalo place the
diaphragm at $x=0$ (of a tube centred on the origin, for the first
four), a shift
of the $[0,1]$ placement. Sousa & Scalo also run a "mirrored Sod" tube
on the periodic interval $[-1,1]$, with $(1,0,1)$ for $|x|<0.5$ and
$(0.125,0,0.1)$ elsewhere, to $t=0.2$ with a Fourier pseudo-spectral
method on 64 to 512 points, used to calibrate their model constants
(App. A); like Abgrall & Barsukow's doubled tube, it makes the problem
periodic. Li, Li, Don & Wang's mirrored run on $[-5,5]$ at $t=2$ is the
mirrored $[0,1]$ tube at $t=0.2$ under $x\mapsto(x+5)/10$,
$t\mapsto t/10$ *(compiler check, not in the sources)*, the same
mirroring as Ye et al.'s. Zhong et al. call their Ex. 6 "Sod's
shock-tube problem" but print a moving left state, $(\rho,v,p)=(1,0.75,1)$
on $[0,0.5)$ against $(0.125,0,0.1)$: a different Riemann problem from
Sod's, whose left gas is at rest. With $N=300$ at $t=0.2$ they find
IMWENO-P, WENO-NS, WENO-P and MWENO-P capturing the discontinuities
better than WENO-JS and WENO-Z, and IMWENO-P slightly ahead of the other
three (Fig. 5).

[Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) Eq. (68)
run the same moving left state with the diaphragm at $x=0.3$ of $[0,1]$,
after Toro, transmissive boundaries, $t=0.2$, 100 cells, CFL 0.9, to
test entropy satisfaction at the sonic rarefaction with ADER schemes of
orders 5 to 10: [AENO](/methods/aeno-reconstruction.md) reconstruction
oscillates significantly near the rarefaction tail at orders 7–10,
AENO-C does not; at orders 9 and 10, in their words, "the tail of the
rarefaction appears slightly disconnected", which a CFL number of about
0.75–0.8 resolves (§7.2, Fig. 14).

[Lin & Chan (2024)](/sources/lin-2024.md) §4.1.1 run the same modified
left state, after Toro's §6.4, with the diaphragm at $x=0.3$:
$(1,0.75,1)$ for $x<0.3$ and $(0.125,0,0.1)$ on the rest of $[0,1]$,
inflow at $x=0$, outflow at $x=1$, $K=50$ and 100 elements of degree
$N=3$, $T=0.2$, $\gamma$ not printed. The left rarefaction is sonic, so
the test probes entropy violation: plain DGSEM shows a jump at the
rarefaction, while entropy-stable DG, DGSEM with a minimum-entropy
limiter and DGSEM with their cell-entropy subcell limiter give a smooth
rarefaction (Fig. 2; see [entropy stability](/properties/entropy-stability.md)).

Naudet & Zahr run Sod with reflecting walls to $t=1$, "five times
longer than the one usually associated with this problem", so that the
waves reflect and interact; their
slices are at $t=0.2$, $0.34$, $0.43$ and $0.54$ (Fig. 17). Lin & Zhu's
$[-5,5]$ placement at $t=2$ is the $[0,1]$ placement at $t=0.2$ under
$x\mapsto(x+5)/10$, $t\mapsto t/10$ *(compiler check, not in the
sources)*.

## Lax

$(\rho,v,p)=(0.445,\ 0.698,\ 3.528)$ on the left and $(0.5,\ 0,\ 0.571)$
on the right. Three placements coexist: $[0,1]$, its shift
$[-\tfrac12,\tfrac12]$, and $[-5,5]$.

| Source | Domain | Grid | Final time | Notes |
|---|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.3 | $[0,1]$ | 96 | 0.14 | right pressure printed $0.5710$ |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.3 | $[0,1]$ | 100 | 0.14 | same |
| [Deng (2023)](/sources/deng-2023.md) App. A.5 | $[0,1]$ | 200 cells | 0.16 | |
| [Huang et al. (2026)](/sources/huang-2026.md) §6.3 | $[0,1]$ | 200 cells | 0.15 (text) / 0.16 (Fig. 8) | ROUND, LD-ROUND, [WENO3-NN](/methods/learned-weno-weights.md) |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.5 | $[-0.5,0.5]$ | 200 cells | 0.16 | moment-based [multi-resolution HWENO](/methods/hermite-weno.md); troubled cells shown in the $x$–$t$ plane |
| [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) §IV.B | $(-0.5,0.5)$ | 8 space–time quadrilaterals | 0.15 | printed $(0.445,\ 0.698876404,\ 3.52773)$; called the "Lax–Harden" problem |
| [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) §4.2 | $[-0.5,0.5]$ | 200 | 0.13 | $\Delta t=10^{-3}$ |
| [Li et al. (2022b)](/sources/li-2022-b.md) §4.3.1, Eq. (39) | $[-5,5]$ | 200 | 1.3 | zero-gradient BCs, CFL 0.5; reference fifth-order WENO-Z with 4000 points |
| [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.2.4, Eq. (16) | $[-5,5]$ | 101 | 1.3 | CFL 0.5 |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.6 | $[-5,5]$ | 256 cells | 1.3 | outflow; data scaled by $\lambda\in\{1,0.01,100\}$ |
| [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.2, Eq. (4.1) | $[-5,5]$ (figures) | 200 cells | 1.3 | positivity-preserving hybrid [HWENO](/methods/hermite-weno.md), Navier–Stokes at $\mathrm{Re}\in\{100,1000,10^4,\infty\}$ |
| [Wang & Don (2022)](/sources/wang-2022-b.md) §3.2.3 | specifications deferred to an earlier paper | | | affine-invariant weights, data scaled |
| [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.2, Eq. (30) | $[0,1]$ | 200 | 0.14 | right pressure printed $0.5710$ |
| [Hiejima (2022)](/sources/hiejima-2022.md) §3.2, Eq. (27) | $[-0.5,0.5]$ | 101 | 0.14 | right pressure printed $0.5710$ |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.3.1 | $[0,1]$ (stated for Sod) | 100 elements | 0.13 | |
| [Boscarino et al. (2022)](/sources/boscarino-2022.md) Ex. 5.2 | $[0,1]$, reflective | 50 | 0.16 | semi-implicit all-Mach WENO at $\varepsilon=1$ |
| [Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.2 | $[-0.5,0.5]$, zero-gradient | 100 | 0.14 | right pressure printed $0.5710$ |
| [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) §4.3 | $[0,1]$ | 100 | 0.14 | right pressure printed $0.5710$ |
| [Liang et al. (2022)](/sources/liang-2022.md) §4.2 | $[0,1]$ | 100 | 0.14 | right pressure printed $0.5710$ |
| [Ji, Liang & Fu (2022)](/sources/ji-2022.md) §5.4 ("ST02") | $[0,1]$ strip | $h=1/100$; 1967 triangles | 0.14 | column shift in Table 6 |
| [Li, Li, Don & Wang (2023)](/sources/li-2023.md) §2.5, §3.2 | $[-5,5]$ | 200 | 1.3 | also scaled by $\lambda\in\{1,10^{-7}\}$ |
| [Bezgin et al. (2023)](/sources/bezgin-2023.md) §5.1.2 | not printed | 100 | 0.14 | data "in references" |
| [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.9 | not printed | 200 | 0.14 | |
| [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.2 | not printed | 200 | 0.14 | text prints "$t=01.4$", Fig. 3 caption $0.14$ |
| [Zhou et al. (2023)](/sources/zhou-2023.md) §5.1, Eq. (36) | $[-0.5,0.5]$ | 100 | 0.14 | right pressure printed $0.5710$ |
| [Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 7 | $[-5,5]$ | 300 cells | 1.3 | WENO-JS lowest resolution, then WENO-Z; IMWENO-P as MWENO-P, marginally above WENO-P and WENO-NS (Fig. 6) |
| [Gaburro et al. (2024)](/sources/gaburro-2024.md) §5.1.3 | $[0,1]\times[0,0.1]$, polygons | $h=1/430$, $P_2$, $P_3$ | 0.14 | quasi-conservative [ADER](/methods/ader-scheme.md)-DG in primitive variables; reference 1D residual distribution on 50,000 points (arXiv v1) |
| [Qin et al. (2023)](/sources/qin-2023.md) §3.4.2 | $[0,1]$, jump at $0.5$ | single domain; two blocks 160 on $[0,0.75]$, 40 on $(0.75,1]$ | 0.14; two blocks also 0.06 | |
| [Kolluru et al. (2024)](/sources/kolluru-2024.md) §3.4, Eq. (9d) | $[-1,1]$, reflecting walls | Chebyshev, $N_x=615$ | first output 0.02 | printed in conserved variables $(0.445,0.311,8.928)$ and $(0.5,0,1.4275)$ |
| [Lin & Zhu (2024)](/sources/lin-2024-b.md) Case 3.3 | $[-0.5,0.5]$ strip, width 0.05, periodic in $y$, $x$-boundary condition not specified | triangles, $201\times11$ vertices | 0.16 | ALW-MR-WENO vs MR-WENO |
| [Zuo & Zhu (2024a)](/sources/zuo-2024.md) Ex. 3.4 | $[-0.5,0.5]$ | 200 | 0.16 | [hybrid](/methods/hybrid-weno.md) MMR-WENO5/7/9 vs MR-WENO and the SHUS-WENO indicator; troubled-cell maps |
| [Fan et al. (2025)](/sources/fan-2025.md) Ex. 3.5 | $[-0.5,0.5]$, outflow | not stated in the text | 0.16 | [HWENO-U](/methods/hermite-weno.md) vs HWENO-M, WENO-ZQ; also data scaled to $(\zeta\rho,v,\zeta p)$, $\zeta\in\{10^{-7},1,10^7\}$ (page-local) |
| [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) §4.3, Eq. (4.7) | $[-5,5]$ | third order, 60 elements (180 DOFs) | 1.6 | DG/FV-[ROUND](/methods/round-scheme.md) on non-uniform subcells vs DG/FV with WENO5-JS on uniform subcells |

The $[-5,5]$ placement at $t=1.3$ corresponds to the $[0,1]$ placement
at $t=0.13$ under the scaling $x\mapsto(x+5)/10$, $t\mapsto t/10$
*(compiler check, not in the sources)*; Sciacovelli et al. stop at
exactly that time, whereas the other $[0,1]$ and $[-\tfrac12,\tfrac12]$
runs stop later, at $0.14$ to $0.16$, so the families compare slightly
different wave positions.

Luo et al.'s digits are those of the conserved state
$(\rho,\rho v,E)=(0.445,\ 0.311,\ 8.928)$ converted with $\gamma=1.4$:
$0.311/0.445=0.698876$ and $0.4\,(8.928-\tfrac12\cdot0.311\cdot0.698876)=3.52773$;
the other sources print the same state rounded *(compiler check, not in
the sources)*.

## Findings across sources

**Contact resolution separates the schemes.** On Sod all schemes agree
with the exact solution, and differences lie at the contact: AFTENO best
and AFWENO-Z better than AFWENO-JS (Ye et al., Fig. 3); TENO-THINC
shocks as sharp as WENO5-Z and TENO5, contacts better resolved (Takagi
et al., Figs. 4–5, also for Lax). Pazner finds that at a fixed 256
degrees of freedom a higher polynomial degree on a coarser mesh
resolves the discontinuities somewhat better, especially the contact,
with $N=3$ and $N=7$ largely indistinguishable (Fig. 7). Sciacovelli et
al. attribute the smearing of their contact to the high-order
dissipation alone, since their shock sensor switches the low-order
term off at the contact, where the pressure is constant (§4.2, Fig. 3).
On Lax, WENO-ZN reduces the dissipation near the shock (Li et al.,
Fig. 4); WENO-Z+M improves shock and contact markedly over WENO-Z and
WENO-Z+, is less oscillatory than WENO-IS-I, while ninth-order WENO-Z9
is less dissipative but more oscillatory (Luo & Wu, Fig. 12). Deng finds
NewWENO less dissipative than WENO-P on both tubes (Fig. 15). Li, Shu &
Qiu report that modifying the first moment in troubled cells gives
"much better resolutions and sharper shock transitions" than the
unmodified sixth-order HWENO on Lax and on their five other shock tests
(Ex. 3.5, Fig. 3.3, comment p. 31).

Tang reports pronounced unphysical oscillations of TENO-A on Sod, and
the TENO-AZ comparable to TENO-LAD and better than TENO-A and TENO-Z
(§4.3, Fig. 6), at the cost of TENO-Z (ratio 1.00; TENO-A 1.19,
TENO-LAD 1.33, Table 5). Jiang et al.'s particle method matches the
exact Sod solution with lower dissipation than the GSPH and WENO-SPH
particle results they compare with (§4.2.1, Fig. 4). On Lax, Gaburro et
al.'s second-order conservative subcell limiter activates "exactly where
the shock wave is located", and the primitive-variable DG elsewhere
leaves no shock-speed error (§5.1.3, Fig. 2; see
[local conservation](/results/local-conservation-flux-form.md)).

TENO variants agree in kind. Hong, Ye & Ye find every scheme stable on
both tubes, with a slight oscillation of WENO-CU6 near the contact;
TENO-M6 matches TENO6 and resolves the contact and the expansion better
than WENO-JS, and TENO-M8 the discontinuities better than WENO9 (§5.2,
Figs. 9–10). Liang et al. report sharper shocks and contacts and a more
accurate rarefaction than their baselines (§4.2, Figs. 7–8). Huang,
Liang & Fu find all four of their schemes free of oscillations
(§4.3, Fig. 6). On a Cartesian strip with conservative-variable
reconstruction, Ji, Liang & Fu see no spurious oscillations and slight
overshoots near the Lax contact; on 1967 triangles the two tubes keep
their one-dimensional symmetry (§5.4, Figs. 5–7); see [symmetry
preservation](/properties/symmetry-preservation.md). Boscarino et al.'s
semi-implicit schemes capture both tubes at $\varepsilon=1$ on 50 cells
"without any observable numerical oscillations" (Ex. 5.2, Fig. 5.2).
Lesur et al. use Sod only to validate the Roe solver of a second-order
finite-volume code against the exact solution (§4.1, Fig. 2). Bezgin et
al. (2023) find their HLLC and Roe setups agreeing "very well" with the
exact solution on both tubes on 100 cells, the HLLC runs with
primitive-variable WENO5-JS slightly oscillatory, which they attribute
to component-wise reconstruction (§5.1.2, Figs. 9–10; see
[characteristic decomposition](/methods/characteristic-decomposition.md)).
Chamarthi (2023a) finds MIG4 capturing the discontinuities in fewer
cells, and Chamarthi (2023b) all schemes capturing rarefaction, contact
and shock without obvious oscillations (Figs. 2–3). Zhou et al. measure
the discontinuity thickness $\Delta\rho/\max_j\lvert\rho_{j+1}-\rho_j\rvert$
(Eq. 35, $\Delta\rho$ the density jump): on Sod WCNS-SA gives the
sharpest shock and contact of their three six-point WCNS, without
oscillations; on Lax WCNS-LD overshoots at the contact and WCNS-SA has
the sharpest contact but a slightly thicker shock (Figs. 8–10).
De Vanna et al. (2023b) find all five shock-capturing schemes of their
code accurate on Sod, improving with the order and from WENO to TENO
(App. A.2, Fig. 12).

**Interfaces of multi-block grids.** Qin et al. use both tubes to pass
a shock through a block interface at $x=0.75$, the spacing jumping
from $0.75/160$ to $0.25/40$ (ratio $4:3$) *(compiler check, not in
the sources)*: the shock locations agree with the exact solution at both
times, the Lax shock sitting at the interface at $t=0.06$ (Figs. 7–8).
On a single domain their scaled smoothness indicators ($\lambda=2$ in
their notation) suppress the oscillations that the unscaled ones
($\lambda=1$) produce on Lax, where WENO-JS and multi-resolution WENO
are also less oscillatory than the unscaled WCNS; they attribute this
to the wide explicit difference stencil of WCNS (Fig. 6). The interface
coupling costs nothing measurable: at 10000 points 283.38 s (one zone)
against 284.55 s (two) on Lax and 189.09 s against 191.42 s on Sod,
serial (Table 13).

**Three-point and very-high-order reconstructions.** Bezgin et al.'s
learned three-point WENO3-NN has a lower $L_1$ error than fifth-order
WENO5-JS on both tubes, with $L_1=L_1^\rho+L_1^v+L_1^p$: on Sod
$1.035\times10^{-2}$ (WENO3-NN2) against $1.106\times10^{-2}$ (WENO5-JS)
and $1.636\times10^{-2}$ (WENO3-JS), on Lax $2.416\times10^{-2}$ against
$2.590\times10^{-2}$ and $3.949\times10^{-2}$; WENO5-Z is best on both
(App. A.6, Table 4). On Lax WENO3-NN2 shows a slight velocity overshoot,
as WENO5-JS does (§4.2, Fig. 9). Hiejima finds that the author's WCNS with
Jiang–Shu weights suppresses oscillations at the Sod shock "even for
the eleventh-order accuracy", whereas the TENO-type weights give a
slight undershoot at the shock and a slight overshoot at the contact
that grow with the order (§3.1, Fig. 2). On Lax the two weightings
differ little, the TENO-type one being slightly better at the contact;
every run overshoots in velocity near $x=-0.25$, a point where the
solution is continuous but not differentiable, and with the cut-off
$C_T=10^{-7}$ the plateau between shock and contact oscillates, which
Hiejima states without a figure (§3.2, Fig. 3).

**Element methods: localization and convergence rate.** For Sod at
200 DOFs, Dzanic, Trojak & Witherden find the artificial viscosity of
the density localized at the shock, with minimal dissipation at the
rarefaction and the contact (§5.2.1, Fig. 4). The $L^1$ density error
converges at first order, rates 0.92, 1.02, 0.87, 0.95, 0.99, 0.85 for
$\mathbb P_2$–$\mathbb P_7$ on 20 to 160 elements, with a marginally lower error at higher order
for fixed DOFs (Table 1). Dzanic & Witherden's entropy filter gives the
same first order, $L^1$ rates 0.91, 0.94, 0.93, 0.92, 0.87, 0.86 and
$L^2$ rates 1.05, 0.98, 1.01, 1.01, 0.98, 1.03 against $N$ (Tables 1–2);
at fixed DOFs the lower order gives a marginally lower error, which
they attribute to more elements and hence a more localized filter
(Tables 3–4, Fig. 2), with minimal smearing of the contact. The two
fixed-DOF trends are opposite but marginal, and belong to two different
shock-capturing devices. Yu & Hesthaven
report spurious oscillations suppressed on both tubes with 100
elements (§5.3.1, Figs. 7–8).

**Explicit viscosity for a central scheme.** Sousa & Scalo find their
quasi-spectral viscosity and localized artificial diffusion both
converge under refinement on Sod, the former giving slightly sharper
discontinuities on equal grids; localized artificial diffusion needs an
explicit Padé filter ($\alpha=0.495$), the quasi-spectral viscosity does
not, although an optional filter ($\alpha=0.499$) attenuates residual
high-wavenumber oscillations (§5.1, Fig. 4).

**$p$-adaptation.** Mossier, Beck & Munz's $p$-adaptive DG with
subcell FV resolves the Sod shock more sharply than the static $N=5$
scheme with 151.6 against 216.0 degrees of freedom per element, using
the highest degree only at the contact and a slightly raised one at the
rarefaction (§8.4, Figs. 8–9). They call this "about 25% less" degrees
of freedom; the printed counts give 29.8 % *(compiler check, not in the
sources)*.

**Shock tracking instead of capturing.** Luo, Absillis & Nourgaliev fit
the shock and the contact as true discontinuities of a space–time mesh
of eight quadrilaterals, six of them degenerate at the diaphragm, and
place the rarefaction head and tail "virtually exactly" with
$\mathbb P^2$ and $\mathbb P^3$ (Figs. 8–11). Their $L^2$ density error
falls, from $\mathbb P^1$ to $\mathbb P^3$, as
$\log_{10}\|\rho-\rho_{\mathrm e}\|=-2.82,\ -4.36,\ -5.67$ on Sod
(slopes 8.75 and 10.48 against $\log_{10}(1/\sqrt{\mathrm{DOFs}})$) and
$-3.38,\ -4.54,\ -5.59$ on Lax (slopes 6.59 and 8.44), which they call
exponential $p$-convergence (Table 1 and the second Table 1); no
shock-capturing scheme is run for comparison. Huang & Zahr's HOIST
method tracks the Sod waves on a space–time mesh of 108 triangles
refined near the diaphragm ($p=2$, geometry $q=1$), removing 24
elements; the features are tracked in order of strength, the shock by
about iteration 27, the contact by 52, the rarefaction head by 66 and
its tail by 106 (§6.4.1, Fig. 29). See
[implicit shock tracking](/methods/implicit-shock-tracking.md).

Naudet & Zahr's space-time HOIST, on Sod between walls, tracks the
shock, the contact and the head and tail of the rarefaction in the first
slab, where they all meet at the diaphragm ("a generalized triple
point"), and then the shock–shock and shock–contact interactions and
the wall reflections (§5.3.1, Figs. 16–17). Where two events occur at
nearly but not exactly the same time, the translating top boundary of a
slab cannot track both on the coarse mesh; the method "chose to track
the shock-contact interaction because it is the stronger feature", and
freeing the temporal coordinates of the top nodes of the slab tracks
both, though "causality may be violated", which no constraint yet
enforces (Fig. 18).

**Spectral relaxation in a Chebyshev basis.** Kolluru et al. solve
both tubes with a Chebyshev pseudo-spectral method with characteristic
boundary conditions, which they find needs no extra boundary treatment.
On Sod the 2/3-dealiased pure pseudo-spectral run destabilizes quickly;
spectral relaxation with the Fejér–Korovkin kernel, parameters
$(0.785,0.99)$, is oscillation-free but slightly overdamped, and with the
de la Vallée-Poussin kernel, $(0.94,0.95)$, closer to the reference with
small bounded oscillations at corners of the profile; Lax shows
the same pattern with $(0.91,0.99)$ and $(1.10,0.98)$ (§3.4, Figs.
14–15). See [artificial and spectral viscosity](/methods/artificial-viscosity.md).

**Multi-resolution WENO of the Zhu group.** Lin & Zhu's ALW-MR-WENO on
triangular strips gives Lax and Sod results comparable to MR-WENO of
the same order, and "can capture the contact discontinuities
precisely" on Sod (Cases 3.3–3.4, Figs. 3.4–3.5). Zuo & Zhu's (2024a) hybrid
MMR-WENO "perform better overall" than the SHUS-WENO hybrid on Lax; both
indicators detect the discontinuities, and theirs is called "more
accurate" from the troubled-cell maps (Ex. 3.4, Figs. 3.4–3.5). Their
MMR/MR CPU-time ratios are 36.8 %, 31.2 % and 35.7 % at orders 5, 7, 9
(Table 3.1).

**Robustness of Hermite WENO at high Reynolds number.** Fan, Zhang &
Qiu run the Lax tube for the compressible Navier–Stokes equations. A
non-hybrid HWENO built on the first two moments, without moment
limiter or positivity limiter, is non-oscillatory at $\mathrm{Re}=100$
but oscillates and loses stability at larger $\mathrm{Re}$ and for
Euler (Fig. 4.1). Their positivity-preserving hybrid HWENO is
non-oscillatory, flags 2.43 % ($\mathrm{Re}=1000$) and 2.68 %
($\mathrm{Re}=\infty$) of the cells as troubled, and never triggers its
positivity limiter, so they attribute the stability on this problem to
the first-moment limiter; a small velocity dent is a numerical artifact
also seen in an earlier finite-volume WENO (Fig. 4.2, Table 4.2).

Fan et al. (2025) find that WENO-ZQ, whose nonlinear weights are not
scale-invariant, over- and undershoots on the unscaled Lax tube, and
that with the scaled data the original weights give oscillations at
$\zeta=10^{-7}$ and extra dissipation at $\zeta=10^7$, while their weights,
with $\tau$, $\beta_k$ and $\epsilon$ normalized by a local mean of
$\lvert\bar u\rvert$, remove both (Figs. 8–9; see below). Deng, Jiang &
Yan find their DG/FV-ROUND less dissipative and less oscillatory on the
Lax tube than the same DG with fifth-order WENO-JS on uniform subcells
(Fig. 13). Abgrall et al. (2026) show the bound-preserving PAMPA Sod
solution (Fig. 5). Danis et al. (2025) capture the shock and contact
sharply in three dimensions; on this rank-1 problem their tensor-train
solver is "more than 1000" times faster than the full-tensor one at
$640^3$, against full-tensor timings extrapolated beyond $160^3$, with a
memory compression below $10^{-5}$ (Fig. 9).

**Scale invariance.** Li, Li, Don & Wang scale the Lax data, density
and pressure, by $\lambda\in\{1,10^{-7}\}$ (page-local symbol), after
Wang & Don: the earlier multi-resolution A-WENO (MR-AWENO) oscillates
at the contact and the shock for both $\lambda$; their new global
indicator alone removes the oscillations at $\lambda=1$ but not at
$10^{-7}$; their scale-invariant MR-AWENO-Si is essentially
non-oscillatory for both (§2.5, Fig. 4). On the unscaled Sod, Lax and
Einfeldt ([123](/benchmarks/double-rarefaction-problem.md)) problems
MR-AWENO already shows strong oscillations near the shock, contact and
rarefaction, which MR-AWENO-Si does not (§3.2, Fig. 5).
Scaling the Lax data by a factor $\lambda$
(page-local symbol) exposes schemes
whose weights depend on the magnitude of the data: OEDG is exactly
scale-invariant, whereas the earlier OFDG smears at $\lambda=100$,
oscillates at $\lambda=0.01$ and undershoots near the shock even at
$\lambda=1$ (Peng et al., Fig. 3). Wang & Don find affine-invariant Z-
and D-type weights essentially identical and non-oscillatory on Lax and
the [123 problem](/benchmarks/double-rarefaction-problem.md) (Fig. 7).
Deng recalls, from an earlier study, that
WENO-Z with $\epsilon=10^{-12}$ and WENO-JS with $\epsilon=10^{-6}$
oscillate on Sod scaled by $\lambda=10^{-7}$ (§1). See [scale invariance](/properties/scale-invariance.md).

## Relatives of the two tubes

The Sod data recur, unchanged or nearly so, in models other than the
single-gas Euler equations.

- **Gas mixtures.** Sciacovelli et al. run both tubes for a single
  species and for an N$_2$ (79 %)–O$_2$ (21 %) mixture and find the two
  solutions superposed (§4.2, Fig. 3). [Renac (2021)](/sources/renac-2021.md)
  §7.2 calls "RP1" a Sod-like problem of the
  [two-component Euler equations](/definitions/multicomponent-euler-equations.md):
  $(Y_1,\rho,v,p)=(0.5,1,0,1)$ and $(0.5,0.125,0,0.1)$, with
  $Y_1$ the mass fraction of component 1, $\gamma_1=1.5$, $\gamma_2=1.3$,
  unit heat capacities, $t=0.2$, entropy-stable DGSEM with $N=3$ on 100
  cells; shocks and contacts are well captured (Figs. 3–4).
- **Stiffened gas and three dimensions.** [Li, Duan & Tang (2022)](/sources/li-2022-c.md)
  run a quasi-two-dimensional [stiffened-gas](/definitions/stiffened-gas-equation-of-state.md)
  tube, $(\rho,v_1,v_2,p)=(1,0,0,1)$ and $(0.75,0,0,0.05)$ with
  stiffening pressure 1 and $\gamma=3$, on $100\times5$ cells to
  $t=0.15$, where their [adaptive moving mesh](/methods/adaptive-moving-mesh.md)
  with multi-resolution WENO beats the uniform mesh with three times as
  many cells near the rarefaction head and the contact (Ex. 5.2,
  Fig. 5.3). Their Ex. 5.6 is a spherical Sod problem, the Sod states
  inside and outside the sphere $r<0.5$ in $[0,1]^3$, $t=0.2$, with a
  second-order TVD solution of the one-dimensional spherical equations
  on 8000 cells as reference: the moving mesh with $100^3$ cells gives
  results comparable to a uniform $200^3$ mesh at 37.2 % of its CPU time
  (Table 5.2).
- **Gravity.** Li, Li, Don & Wang run the Sod states under gravity
  $\phi_x=1$ on $[0,1]$ to $t=0.2$ with $N=100$; their
  non-well-balanced scheme oscillates near the shock and the contact,
  the well-balanced one does not (§5.1, Fig. 9); see [hydrostatic
  equilibrium tests](/benchmarks/hydrostatic-equilibrium-tests.md).
- **Relaxation and gravity.** [Arun, Krishnan & Samantaray (2022)](/sources/arun-2022.md)
  §5.1 solve the barotropic Euler equations with gravity ($\phi(x)=x$)
  and stiff friction relaxation for the Sod densities
  $(\rho,v)=(1,0)$, $(0.125,0)$ on $[0,1]$ to $t=0.2$, CFL 0.45, $\gamma$
  not printed. In the compressible regime the solution converges under
  refinement (100 and 1000 cells, Fig. 1); in the stiff regime it
  matches a first-order porous-medium solver in the parabolic scaling
  and a first-order upwind transport solver in the hyperbolic one
  (Fig. 2). See [asymptotic preservation](/properties/asymptotic-preservation.md).
- **Two-fluid and multispecies tubes.** [Nguyen et al. (2022)](/sources/nguyen-2022.md)
  §3.2 run the Sod states as a gas–gas two-fluid tube, the left gas
  with $\gamma=1.4$ and the right one with $\gamma=1.667$, interface at
  $x=0.5$ of $[0,1]$, on 100 to 800 cells to $t=0.2$ at CFL 0.9 against
  the exact solution; they report no spurious oscillation in pressure,
  density or velocity, and grid convergence (Figs. 6–9). A
  hydrogen–oxygen–argon tube of molar ratio 2:1:7, with
  $(T,v,p)=(400\ \mathrm K,0,8000\ \mathrm{Pa})$ on the left and
  $(1200\ \mathrm K,0,80000\ \mathrm{Pa})$ on the right, to
  $t=40\,\mu$s, is run without reactions by two sources:
  [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) §3.2 on a
  $100\times50$ mm tube with the diaphragm at $x=50$ mm, slip walls and
  three levels of [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
  down to 0.25 mm, whose results on several meshes agree with two
  earlier computations (Fig. 6); and
  [Du & Yang (2022)](/sources/du-2022-b.md) Ex. 6.3 on a 10 cm domain
  with bound-preserving LDG, $k=2$, 400 cells and a 5000-cell
  reference, whose code blows up without the bound-preserving limiter
  (Fig. 6.3). Du & Yang also run a He/N$_2$ tube, $(T,v,p,Y_1,Y_2)=(300\
  \mathrm K,0,10\ \mathrm{atm},1,0)$ for $x\le0.4$ m and $(300\ \mathrm
  K,0,1\ \mathrm{atm},0,1)$ beyond, on 1000 cells to $t=300\,\mu$s, where
  without the limiter $Y_2$ turns negative within $0.5085\,\mu$s and the
  code blows up (Ex. 6.2, Figs. 6.1–6.2).
  [Ching et al. (2025)](/sources/ching-2025.md) §5.3 run the same
  He/N$_2$ tube, after Houim & Kuo, with the reacting-flow
  Navier–Stokes equations and walls at both ends of $[0,1]$ m, $t=300\,\mu$s,
  CFL 0.1: DG of degree 3 on 200 elements without artificial viscosity,
  against a degree-2 reference on 2000 elements. Their entropy limiter
  damps the large-scale pressure, temperature and entropy instabilities
  "significantly better" than the positivity limiter alone, whose
  instabilities are much larger than in single-gas tubes, and the
  Lax–Friedrichs-type viscous flux gives a smaller temperature overshoot
  at the shock than BR2; artificial viscosity alone gives negative
  concentrations, as stated (Figs. 5.5–5.6; see
  [positivity-preserving Navier–Stokes flux](/methods/positivity-preserving-navier-stokes-flux.md)).
  See
  [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
  and [bound preservation](/properties/bound-preservation.md).
- **Two materials on a Lagrangian mesh.** [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md)
  §3.5.5 run the Sod states with $\gamma=1.4$ on the left and
  $\gamma=5/3$ on the right of $[0,1]\times[0,0.1]$, $201\times3$ points
  with the interface on mesh edges (no mixed cells), fixed left and
  right states, reflective top and bottom, to $t=0.2$, with an indirect
  ALE method that rezones without moving the interface nodes and remaps
  every 20 Lagrangian steps with their positivity-preserving
  [conservative remapping](/methods/conservative-remapping.md); the ALE
  method "can handle this multi-material flow problem very well"
  (Fig. 20). Their text gives $201\times3$ points, the Fig. 20 caption
  $N_x=200$, $N_y=3$; $3$ points in $y$ make 2 cells, so the caption's
  $N_y$ does not count cells as $N_x$ does *(compiler check, not in the
  sources)*.
- **Reacting and non-equilibrium air.** [Peyvan et al. (2023)](/sources/peyvan-2023.md)
  (arXiv v1) run three Sod-type tubes for multi-species hypersonic
  flows with their entropy-stable DGSEM. A three-species
  ($\mathrm O$, $\mathrm O_2$, $\mathrm N_2$) tube after Zhang & Shu with
  one dissociation reaction, $(v,p)=(0,1000)$ against $(0,1)$ at a
  uniform 8000 K on $[-1,1]$, $t=10^{-4}$, CFL 0.1, 800 elements of
  degree 3, against ES-DGSEM on 4000: all schemes except a modal
  positivity-preserving DG get the right solution, flux reconstruction
  and spectral difference oscillate, WENO and ES-DGSEM do not but smear
  more (§4.3, Fig. 3). A five-species non-equilibrium tube after
  Grossman & Cinnella, $(T,v,p)=(9000\ \mathrm K,0,195256\ \mathrm{Pa})$
  against $(300\ \mathrm K,0,10^4\ \mathrm{Pa})$ on $[0,1]$, 200 elements,
  CFL 0.01, matches the cited reference in all variables and mass
  fractions (§4.5.1, Fig. 6); they state that flux reconstruction and
  spectral difference with filtering are unstable on it. A third tube
  into the 44 km atmosphere compares equilibrium and finite-rate
  chemistry at driver temperatures 2000–4000 K, which deviate from
  3000 K on (§4.5.2, Fig. 7). See
  [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md).
- **Five-species air in three codes.** [Başkaya et al. (2024)](/sources/baskaya-2024.md)
  §4.4 (author preprint) run the same Grossman–Cinnella tube, the
  driver at 9000 K and 195256 Pa and the driven gas at 300 K and
  $10^4$ Pa, five-species air initially in equilibrium, Park's 1985
  mechanism, on $[0,1]$ m with 600 cells to $t=99$ μs, in three
  finite-volume codes sharing one thermochemistry library: contact,
  shock and expansion are captured and the post-shock density peak
  matches the reference "without any oscillations", one code (CHESS)
  giving slightly more N$_2$ and less N than the other two (Figs. 5–6).
  Two-temperature runs showed "no significant differences", so
  equilibrium results are shown.
- **Single planar shocks.** [Gaburro et al. (2024)](/sources/gaburro-2024.md)
  §5.1.2 run a right-moving shock of Mach 5, 10 or 20 into
  $(\rho,v,p)=(\gamma,0,1)$ on $[0,1.2]\times[0,0.1]$, the post-shock
  state from the normal-shock relations, at $P_2$ and $P_3$ on polygons
  with $h=1/180$ to $t=0.04$: shock position and magnitude are "always
  perfectly captured", with start-up perturbations downstream that they
  attribute to the mismatch between one-dimensional Rankine–Hugoniot and
  discrete two-dimensional jump conditions, as also seen with
  conservative schemes (Fig. 1).
- **Radial Sod in two dimensions.** [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md)
  §4 (arXiv v4) run $(\rho,v_1,v_2,p)=(1,0,0,1)$ for $r\le0.5$ and
  $(0.125,0,0,0.1)$ for $0.5<r\le1$, CFL 0.25, $t=0.25$, with
  deferred-correction residual distribution on triangles. The
  uncorrected continuous-Galerkin scheme with jump stabilization breaks
  down at $t\approx0.16$; with their
  [entropy correction term](/methods/entropy-correction-term.md) it runs
  to $t=0.25$, the two correction variants being indistinguishable
  without zoom (Figs. 1–2). [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md)
  §5.2.2 run the same radial data on $[-1,1]^2$ with periodic
  boundaries, $200\times200$, CFL 1, to $t=0.16$, with their
  fourth-order [kinetic scheme](/methods/discrete-kinetic-relaxation-scheme.md):
  flux limitation and [MOOD](/methods/mood-a-posteriori-limiting.md)
  give almost identical results, MOOD never falls back to first order
  and leaves over- and undershoots at the shock, while the limiter
  removes the overshoot and reduces the undershoot (Figs. 8–9). The
  three-dimensional spherical version of Li, Duan & Tang is listed
  above. [Vilar & Abgrall (2024)](/sources/vilar-2024.md) §4.3.1 (HAL
  preprint) run a polar Sod tube on the sector
  $(r,\theta)\in[0,1]\times[0,\pi/4]$ of unstructured triangles,
  $(1,0,1)$ for $r<0.5$ and $(0.125,0,0.1)$ beyond, $\gamma=1.4$,
  symmetry on the sector sides and outflow at $r=1$, the final time not
  printed in the text, with $\mathbb P^5$ DG and their
  [a posteriori local subcell correction](/methods/mood-a-posteriori-limiting.md)
  on 230 cells and at third order on 10571 cells (Figs. 35–37). The
  two-dimensional and spherical explosions of other sources
  are on the [explosion and implosion page](/benchmarks/explosion-and-implosion-problems.md).
- **Relativistic tubes.** [Chen & Wu (2022)](/sources/chen-2022-b.md)
  Exs. 4.2–4.5 (arXiv v1) run quasi-one-dimensional
  [relativistic](/definitions/relativistic-hydrodynamics.md) Riemann
  problems on thin strips of triangles: $(\rho,v_1,v_2,p)=(1,-0.6,0,10)$
  against $(10,0.5,0,20)$ (two rarefactions and a contact, $t=0.4$);
  $(1,0,0,10^4)$ against $(1,0,0,10^{-8})$ ($t=0.45$, a thin shell between
  shock and contact; without the physical-constraint-preserving limiter
  the run fails within a few steps); and $(10^2,0,0,10^4)$ against
  $(10^2,0,0,10^2)$, rerun with $\rho$ and $p$ scaled by $10^{-2}$ and
  $10^{-4}$. On the scaled problem their scale-invariant weights keep
  $\rho^{(\zeta)}_h-\zeta\rho_h$ (with $\zeta$ the page-local scaling
  factor) at $O(10^{-12})$–$O(10^{-13})$, whereas the original Zhu–Qiu
  weights give $O(10^{-1})$ and $O(10^{-2})$ and overshoot (Ex. 4.4,
  Figs. 6–8), the relativistic counterpart of the Lax scaling test
  above.
- **Two-phase Lax tube.** [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md)
  Ex. 4.6 run the Lax states in the Kapila
  [five-equation model](/definitions/five-equation-model.md), with
  phase densities $0.445$ and $0.5$ on both sides and a volume fraction
  varying linearly, $\phi_1=x+0.5$, on $[-0.5,0.5]$: in
  $(\rho_1,\rho_2,v,p,\phi_1)$, $(0.445,0.5,0.698,3.528,x+0.5)$ for $x<0$
  and $(0.445,0.5,0,0.571,x+0.5)$ for $x>0$, $\gamma_1=1.4$, $\gamma_2=1.6$,
  outflow, 1000 cells, $t=0.17$; both their bound-preserving
  [OEDG](/methods/oedg.md) scheme and its averaging-based variant agree
  with a VFRoe reference on 100,000 cells (Fig. 8).
- **Gas–liquid tubes.** [Wong et al. (2021)](/sources/wong-2021.md) §6.3
  run a water–air "Sod" problem with pressure ratio $10^9/10^5$;
  [Nguyen et al. (2022)](/sources/nguyen-2022.md) §3.2 an air–water tube
  with the same ratio; [Bai & Li (2022)](/sources/bai-2022.md) §3.1
  air–helium and water–air tubes with a sharp-interface DG method. They
  belong with the [gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md).

- **Real gas.** [Weng & Mével (2023)](/sources/weng-2023.md) §4.1
  validate their OpenFOAM real-gas solver on a Sod-type tube with
  driver-to-driven pressure ratio 20, equal temperatures, $\gamma=1.4$
  for the ideal gas and the Redlich–Kwong equation of state with
  non-dimensional attraction and co-volume parameters $A=B=0.1$; 1 mm
  cells, CFL 0.1, output at $t=0.05$ s, domain length not given;
  second-order MUSCL with HLLC. The numerical solution agrees with the
  exact real-gas solution; the real gas gives a much smaller density
  ratio across the tube, a wider expansion fan and a slower contact, and
  a shock Mach number of 1.76 against 1.83 for the ideal gas (Fig. 5).
  Sweeping $B$ from $6\times10^{-4}$ to $0.3$ at $A/B\in\{0.5,1,2\}$, the
  real-gas shock is slower than the ideal-gas one for small $A$, $B$ and
  faster for large ones (Fig. 6, Table 1). They call the shock-speed
  difference 2.1 %, while the two Mach numbers differ by 3.8 %
  *(compiler check, not in the sources)*; which region carries
  $A=B=0.1$ is printed ambiguously.

## Qualifications

- Lesur et al. print the Sod states as $\rho_{\mathrm L}=1$,
  $p_{\mathrm L}=0.1$, $\rho_{\mathrm R}=0.125$, $p_{\mathrm R}=0.1$, $v=0$
  (§4.1). With equal pressures and zero velocity the data are a
  stationary contact and nothing but the contact would appear, whereas
  their Fig. 2 shows a rarefaction, a contact and a shock against the
  analytical solution; the printed $p_{\mathrm L}$ is inconsistent with
  their own run, and the other sources print $p_{\mathrm L}=1$.
- Ji, Liang & Fu's Table 6 prints, under
  $\rho_{\mathrm L},v_{\mathrm L},p_{\mathrm L},\rho_{\mathrm R},v_{\mathrm R},p_{\mathrm R}$,
  the rows "1.0 0.0 1.0 1.0 0.125 0.0" (ST01, Sod) and "0.445 0.698
  3.528 3.528 0.5 0.0" (ST02, Lax), and a strong tube ST03 "1.0 0.0 1000
  1000 1.0 0.0" with $t=0.012$ and diaphragm at $x=0.6$: in every row the
  printed $\rho_{\mathrm R}$ repeats $p_{\mathrm L}$ and $p_{\mathrm R}=0$, a
  degenerate state, so a column is shifted and the right-state values
  cannot be recovered from the table. They also print the strips as
  $[0,0.2]\times[0,1]$ for data defined on $0\le x\le1$.
- Mossier, Beck & Munz state Dirichlet boundaries; Boscarino et al.
  reflective ones; Hong, Ye & Ye zero-gradient ones.
- Luo & Wu print the left Lax pressure as $0.3528$ (Eq. (16)), where
  Fu (2021), Takagi et al., Li et al., Deng, Huang et al., Peng et
  al., Li, Shu & Qiu, Fan et al. and Sciacovelli et al. print $3.528$;
  the paper's text does not show which value was run.
- Huang et al. give $t=0.15$ in the text and $t=0.16$ in the caption of
  Fig. 8.
- Wang & Don's figure of the unscaled tubes includes the Lax problem,
  although their §3.2.3 text list omits it.
- Li et al. compute the Lax reference with fifth-order WENO-Z, the
  other references of the paper with seventh order.
- Fan et al. print both Lax states on "$x\in[0,5)$" and "$x\in[0,5]$"
  (Eq. (4.1)); their figures show $[-5,5]$, so the left state belongs on
  $[-5,0)$. Their text gives CPU savings of the hybrid scheme of 77.68 %
  and 75.08 % "as shown in Table 4.2", whose entries are 71.20 %
  ($\mathrm{Re}=1000$) and 69.98 % ($\mathrm{Re}=\infty$).
- Luo, Absillis & Nourgaliev write "profiles at $t=0.2$" for the Lax
  problem, whose space–time domain ends at $t=0.15$, the time in their
  figure captions.
- Li, Shu & Qiu do not print $\gamma$ for the Lax problem, Arun et
  al. not for their tube, Sousa & Scalo not for Sod.
- Dzanic & Witherden's $L^2$ errors are smaller than their $L^1$ errors
  throughout (e.g. $1.21\times10^{-3}$ against $6.87\times10^{-3}$ at
  $M=100$, $\mathbb P_2$, Tables 3–4), while their printed definitions
  (Eq. (28)), $\frac1M\sum\lvert e_i\rvert$ and
  $\sqrt{\frac1M\sum e_i^2}$ over the same points, satisfy
  $L^2\ge L^1$ by the power-mean inequality *(compiler check, not in the
  sources)*. The $L^2$ norm computed differs from the printed one, or the
  labels are swapped; the rates are unaffected.
- Lin & Zhu print the Sod states as $(\rho,v_1,v_2,p)=(1,0,0,2.5)$ and
  $(0.125,0,0,0.25)$, whereas their Lax case lists the pressure in the
  same slot; $2.5$ and $0.25$ equal the total energies $p/(\gamma-1)$ of
  the Sod states for $\gamma=1.4$ *(compiler check, not in the
  sources)*, and the paper prints no $\gamma$.
- Zuo & Zhu (2024a) write that MMR-WENO saves "nearly 60%" of the CPU
  time on Lax, while their Table 3.1 ratios give savings of 63.2 %,
  68.8 % and 64.3 % *(compiler check, not in the sources)*.
- Kolluru et al. print the pressure as "$p=(\gamma-1)\rho$" below their
  Euler system, without the internal-energy factor, and state no output
  times for Sod; Naudet & Zahr state no $\gamma$ for Sod (1.4 is given
  for their Shu–Osher run).
- Danis et al. compute full-tensor reference timings only up to
  $160^3$ and extrapolate them to $320^3$ and $640^3$; their "1000 times"
  speedup rests on the extrapolation.
- Du & Yang print the H$_2$/O$_2$/Ar diaphragm at $x=0.5$ cm of a 10 cm
  domain, Peng et al. at the middle of their 100 mm tube.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.3 (arXiv v1).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.3, Figs. 4–5.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.3, Eq. (43), Fig. 3.
- [Deng (2023)](/sources/deng-2023.md) — §1; App. A.4–A.5, Fig. 15.
- [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) — §3.5.3 and §5.6, Figs. 19, 24, 28 (author preprint).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.3, Fig. 8.
- [Li et al. (2022b)](/sources/li-2022-b.md) — §4.3.1, Eq. (39), Fig. 4.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.2.4, Eq. (16), Fig. 12.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.6, Fig. 3 (arXiv v1).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.3, Fig. 7.
- [Pazner (2021)](/sources/pazner-2021.md) — §5.2.1, Fig. 7 (arXiv v1).
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §IV.A–IV.B, Figs. 8–17, both tables captioned "Table 1" (author manuscript).
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §4.2, Eq. (41), Fig. 3 (arXiv v1).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — Ex. 3.5, Fig. 3.3; comment p. 31 (arXiv v1).
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — Ex. 4.2, Eq. (4.1), Figs. 4.1–4.2, Table 4.2.
- [Renac (2021)](/sources/renac-2021.md) — §7.2, RP1, Figs. 3–4 (arXiv v3).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Ex. 5.2, Fig. 5.3; Ex. 5.6, Table 5.2 (arXiv v1).
- [Arun, Krishnan & Samantaray (2022)](/sources/arun-2022.md) — §5.1, Eq. (5.2), Figs. 1–2 (arXiv v1).
- [Wong et al. (2021)](/sources/wong-2021.md) — §6.3, Table 6 (arXiv v1).
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4.2, Eqs. (29)–(30), Figs. 8–9; App. A.6, Table 4.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §§3.1–3.2, Eqs. (26)–(27), Figs. 2–3.
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §5.2.1, Table 1, Fig. 4 (arXiv v2).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §5.1.1, Eq. (28), Tables 1–4, Fig. 2 (arXiv v3).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.3.1, Figs. 7–8.
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — §5.1, Fig. 4; App. A, Figs. A.21–A.22 (arXiv v2).
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §3.2, Figs. 6–10.
- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §3.2, Fig. 6 (accepted manuscript).
- [Du & Yang (2022)](/sources/du-2022-b.md) — Exs. 6.2–6.3, Figs. 6.1–6.3.
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §4, Figs. 1–5 (arXiv v4).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Exs. 4.2–4.5, Figs. 4–9 (arXiv v1).
- [Bai & Li (2022)](/sources/bai-2022.md) — §3.1.1–3.1.2, Figs. 8–9.
- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §5.2.2, Figs. 8–9.
- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — Ex. 5.2, Fig. 5.2 (arXiv v2).
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §5.2, Figs. 9–10.
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §6.4.1, Fig. 29 (arXiv v2).
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §4.3, Fig. 6 (arXiv v1).
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §5.4, Table 6, Figs. 5–7 (preprint).
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §4.1, Fig. 2 (arXiv v1).
- [Li, Li, Don & Wang (2023)](/sources/li-2023.md) — §2.5, Fig. 4; §3.2, Fig. 5; §5.1, Fig. 9.
- [Liang et al. (2022)](/sources/liang-2022.md) — §4.2, Figs. 7–8.
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §8.4, Figs. 8–9.
- [Bezgin et al. (2023)](/sources/bezgin-2023.md) — §5.1.2, App. A, Figs. 9–10 (arXiv v1).
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.9 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Ex. 3.2, Figs. 2–3 (arXiv v1).
- [Qin et al. (2023)](/sources/qin-2023.md) — §3.4.2, §3.4.4, Table 13, Figs. 6–8.
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §5.1, Eqs. (34)–(36), Figs. 8–10.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — App. A.2, Fig. 12.
- [Weng & Mével (2023)](/sources/weng-2023.md) — §4.1, Table 1, Figs. 5–6.
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §4.3, Exs. 6–7, Figs. 5–6.
- [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md) — §3.5.5, Fig. 20.
- [Peyvan et al. (2023)](/sources/peyvan-2023.md) — §§4.3, 4.5, Tables 1–2, Figs. 3, 6–7 (arXiv v1).
- [Tang (2024)](/sources/tang-2024.md) — §4.3, Eq. (28), Fig. 6, Table 5.
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §4.2.1, Fig. 4.
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — §5.1.2–§5.1.3, Figs. 1–2 (arXiv v1).
- [Başkaya et al. (2024)](/sources/baskaya-2024.md) — §4.4, Table 5, Figs. 5–6 (author preprint).
- [Kolluru et al. (2024)](/sources/kolluru-2024.md) — §3.4, Eqs. (9a)–(9d), Figs. 14–15, App. B (arXiv v2).
- [Lin & Zhu (2024)](/sources/lin-2024-b.md) — §3, Cases 3.3–3.4, Figs. 3.4–3.5.
- [Lin & Chan (2024)](/sources/lin-2024.md) — §4.1.1, Fig. 2.
- [Naudet & Zahr (2024)](/sources/naudet-2024.md) — §5.3.1, Eq. (57), Figs. 16–18.
- [Zuo & Zhu (2024a)](/sources/zuo-2024.md) — Ex. 3.4, Figs. 3.4–3.5, Table 3.1.
- [Vilar & Abgrall (2024)](/sources/vilar-2024.md) — §4.3.1, Figs. 35–37 (HAL preprint).
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — Ex. 4.6, Fig. 8.
- [Ching et al. (2025)](/sources/ching-2025.md) — §5.3, Eq. (5.4), Figs. 5.5–5.6.
- [Danis et al. (2025)](/sources/danis-2025.md) — §5.5, Fig. 9 (arXiv v1).
- [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) — §4.3, Eq. (4.7), Fig. 13.
- [Fan et al. (2025)](/sources/fan-2025.md) — Ex. 3.5, Figs. 8–9.
- [Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) — §7.2, Eq. (68), Fig. 14.
- [Abgrall et al. (2026)](/sources/abgrall-2026.md) — Ex. 5, Fig. 5.
