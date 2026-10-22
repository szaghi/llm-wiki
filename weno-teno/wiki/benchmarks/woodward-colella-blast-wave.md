---
type: Benchmark
title: "Woodward–Colella interacting blast waves"
description: "One-dimensional Euler problem of two strong blast waves between reflecting walls, pressures 1000, 0.01 and 100, run to t=0.038; a one-dimensional robustness test whose resolution is measured by the resolution of the density peaks and contacts after the blasts collide."
status: established
aliases: [interacting blast waves, two blast waves interaction, Woodward–Colella blast wave, blast wave problem]
tags: [benchmark, weno, teno, low-dissipation, positivity]
timestamp: 2026-10-22T00:00:00Z
---

# Woodward–Colella interacting blast waves

Gas at rest with unit density fills $[0,1]$ between two reflecting
walls. Two thin regions at the ends hold pressures five and four orders
of magnitude above the middle, so two strong blast waves run inwards
and interact. By $t=0.038$ the density shows narrow peaks and contacts
(Fu 2021 single out the peak near $x\approx0.78$). The pressure ratio
$10^5$ makes the problem a robustness test, and the height and position
of the density peaks and the sharpness of the contacts measure
resolution against a fine-grid reference. Fourteen sources of the
bundle run it.

## Setup

The common data, printed by Fu (2021), Takagi et al., Ye et al., Wang
et al. (2023), Chertock et al., Deng, Huang et al., Li, Shu & Qiu and
Wang et al. (2021) (Li et al. differ in one value, see Qualifications),
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
| [Li et al. (2022)](/sources/li-2022-b.md) §4.3.3, Eq. (41) | 400 | WENO7-Z, 4000 | middle pressure printed $0.001$; [WENO-ZN](/methods/weno-zn.md) |
| [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.2.5, Eq. (17) | 401, CFL 0.5 | WENO-Z, 20001 | [WENO-Z+M](/methods/weno-z-plus.md); calibrates its constant |
| [Wang et al. (2023)](/sources/wang-2023-b.md) Example 1 | $\Delta x=1/400$ | OLD scheme, $\Delta x=1/3200$ | A-WENO with [adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md) |
| [Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 4 | $\Delta x=1/400$ | old CU, $\Delta x=1/4000$ | [LCD central-upwind](/methods/lcd-central-upwind-scheme.md) |
| [Deng (2023)](/sources/deng-2023.md) App. A.7 | 400 | — | [ROUND](/methods/round-scheme.md), NewWENO, WENO-JS5 |
| [Huang et al. (2026)](/sources/huang-2026.md) §6.5 | 400 | WENO5, refined mesh | ROUND, LD-ROUND, [WENO3-NN](/methods/learned-weno-weights.md) |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.7 | 640 | LLF, 100,000 | [OEDG](/methods/oedg.md), with and without [characteristic decomposition](/methods/characteristic-decomposition.md) |
| [Balsara et al. (2024)](/sources/balsara-2024.md) §VIII.d | 1000, on $[-0.5,0.5]$ | third order, 10,000 | HLL, CFL 0.8, orders 3, 5, 7 |
| [Wang & Don (2022)](/sources/wang-2022-b.md) §3.2.2–3.2.3 | 800 (scaled variant) | Ai-WENO-Z, 3200 | [affine-invariant weights](/methods/affine-invariant-weno.md) |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.7 | 800 cells, CFL 0.6 | FD WENO5, 16,000 | moment-based [multi-resolution HWENO](/methods/hermite-weno.md), HLLC; boundary conditions not printed |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.4b | 400, CFL 0.6 | WENO-JS5, 20,000 | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5) vs original WENO5-MR, WENO-AO5, WENO-JS5 |

## Findings across sources

**Density-peak resolution.** The new scheme of each paper sharpens the
peaks and contacts of its baseline. Fu (2021) gets a better density peak
at $x\approx0.78$ than WENO-CU6, free of WENO-CU6's pressure oscillations
and velocity overshoot near $x\approx0.86$ (Fig. 6). Takagi et al.
resolve the contact "significantly better" than WENO5-Z and TENO5
(Fig. 8). Li et al. find WENO-ZN less dissipative than WENO-JS and
WENO-Z (Fig. 6); Ye et al. find AFTENO closest to the reference in
density and pressure (Fig. 6); Chertock et al. and Wang et al. (2023) report
"slightly" better resolution of the second density spike with their
new central-upwind fluxes (Figs. 5.4 and 1); Deng finds low-dissipation
ROUND better than WENO-JS5 (Fig. 33). In one dimension Wang et al.
(2023) expect no large gain, because their dissipation switch is
inactive there (§4.1). Li, Shu & Qiu find the HWENO with modified first
moments "much better" resolved and sharper than the unmodified one
(Fig. 3.5, comment p. 31). Wang et al. (2021) find their New WENO5
similar to WENO-AO5, both better than WENO-JS5 and the original
multi-resolution WENO5, at about 0.67 of the latter's cost (0.76 s
against 1.14 s; Fig. 5.8).

**Robustness and the stability margin of very-high-order schemes.**
Luo & Wu use the problem to choose the largest admissible constant of
WENO-Z+M: it runs with 579 and fails with 580 on 401 points, and 579 is
then fixed for all tests (§3.2, Fig. 13); ninth-order WENO-Z fails
outright, so seventh order is shown instead (§5.2.5). Peng et al. find
that the earlier OFDG without characteristic decomposition smears
strongly, whereas OEDG works with or without it (Fig. 4). Balsara et al.
show the shock positions converging at orders 3, 5 and 7 on 1000 zones
(Fig. 10).

**Grid convergence and the TENO cut-off.** Takagi et al. refine from
400 to 3200 points: with $C_T=10^{-4}$ the solution converges
monotonically to the reference, whereas with the default
$C_T=10^{-5}$ a small overshoot appears near the strong contact at the
highest resolutions (Fig. 9). See [TENO](/methods/targeted-eno.md).

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

- Li et al. print the middle pressure as $0.001$ (Eq. (41)) where Fu
  (2021), Takagi et al., Ye et al., Wang et al. (2023), Chertock et
  al., Deng, Huang et al., Li, Shu & Qiu and Wang et al. (2021) print
  $0.01$; whether this is a misprint or the value run cannot be decided
  from the paper.
- Balsara et al. place the problem on $[-0.5,0.5]$; their initial
  states are not recorded on this page.
- Ye et al. give 400 points in the text and $N=1500$ in the caption of
  Fig. 6.
- Wang et al. (2023) compute their reference with the OLD scheme
  against which the NEW one is compared.
- Li, Shu & Qiu print the intervals as open, $(0,0.1)$, $(0.1,0.9)$,
  $(0.9,1)$, and state no boundary conditions or $\gamma$ for this
  problem.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.5, Fig. 6 (arXiv v1).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.5, Figs. 8–9.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.6, Eq. (46), Fig. 6.
- [Li et al. (2022)](/sources/li-2022-b.md) — §4.3.3, Eq. (41), Fig. 6.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §3.2, Fig. 13; §5.2.5, Eq. (17).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §4.1; Example 1, Fig. 1.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §5.1, Ex. 4, Fig. 5.4 (arXiv v2).
- [Deng (2023)](/sources/deng-2023.md) — App. A.7, Figs. 15d, 23, 33.
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.5.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.7, Fig. 4 (arXiv v1).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §VIII.d, Fig. 10.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.2–3.2.3, Figs. 6–7.
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — Ex. 3.7, Fig. 3.5; comment p. 31 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.4b, Fig. 5.8.
