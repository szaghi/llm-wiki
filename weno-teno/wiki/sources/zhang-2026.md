---
type: Source
title: "Zhang et al. (2026) — A hybrid MR-WENO scheme with a simplified troubled-cell indicator for hyperbolic conservation laws"
description: "Fifth-order finite-difference hybrid SHMR-WENO: multi-resolution WENO with characteristic decomposition only in cells flagged by a shifted sign test on the derivative of a quadratic interpolant of three point values, the linear upwind flux elsewhere; fewer flagged cells and 0.42–0.78 of the MR-WENO CPU time."
resource: "doi:10.1016/j.camwa.2026.01.017"
source_kind: paper
authors: [Zhang J., Tao Z., Zhu J., Qiu J.]
year: 2026
venue: "Comput. Math. Appl. 207:1-14"
local_file: "/home/stefano/papers/mosaic/weno-teno/2026_Crossref_Computers_and_Mathematics_with_Applications_Zhang_A_hybrid_MR-WENO_scheme_with_a_simplified_troubled-cell.pdf"
tags: [weno, hybrid-scheme, troubled-cell, finite-difference]
timestamp: 2026-11-01T18:56:00Z
---

# Summary

Zhang et al. (2026a) (Zhang, Tao, Zhu & Qiu) build SHMR-WENO, a fifth-order
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
[hybrid scheme](/methods/hybrid-weno.md) for one- and two-dimensional hyperbolic conservation laws. The
nonlinear reconstruction is the fifth-order [multi-resolution WENO](/methods/multi-resolution-weno.md)
(MR-WENO) of Zhu & Shu (2018), with [WENO-Z](/methods/weno-z.md)-type weights and positive linear weights
$\bar d_{l,k}=10^l$; it runs, with [characteristic decomposition](/methods/characteristic-decomposition.md),
only in troubled cells. Elsewhere the flux is the linear value of the quartic on the five-point stencil,
taken component-wise.

The contribution is a "simplified" [troubled-cell indicator](/definitions/troubled-cell-indicator.md).
The baseline hybrid of Wang, Tian, Zhu & Zhao (2023), called HMR-WENO in this paper, searches a quartic
interpolant numerically for extreme points. Here a quadratic interpolant of the three point values
$u_{i-1},u_i,u_{i+1}$ is used: its derivative is linear, so whether it has an extremum in
$[x_{i-3/2},x_{i+3/2}]$ is decided by the signs of the scaled derivative at the two ends, each shifted
by $\pm\Delta x$. In 2D a cell is troubled if flagged in either direction; for the Euler equations the
indicator acts on the density. The name HMR-WENO here is not the HMR-WENO of
[Zuo & Zhu (2024b)](/sources/zuo-2024-b.md), a different hybrid.

The evidence is numerical (Lax–Friedrichs splitting, [SSP-RK3](/methods/ssp-runge-kutta.md) at CFL 0.6).
On a 2D $\gamma=3$ Euler accuracy test whose density solves 2D
[Burgers](/benchmarks/burgers-equation-tests.md), MR-WENO and both hybrids print identical fifth-order
errors and the hybrids flag no cell. On 1D Burgers, the Lax problem
([shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)), the [Shu–Osher](/benchmarks/shu-osher-problem.md)
and [Woodward–Colella](/benchmarks/woodward-colella-blast-wave.md) problems, 2D Burgers,
[double Mach reflection](/benchmarks/double-mach-reflection.md) and the
[forward-facing step](/benchmarks/forward-facing-step.md), SHMR-WENO flags 0.73–7.69 % of cells against
1.14–9.21 % for HMR-WENO, and runs in 0.42–0.78 of the MR-WENO CPU time against 0.48–0.88. Resolution
claims are visual. No theorem is stated.

# Version read

Version of record (Elsevier typeset, pp. 1–14; received 4 June 2025, revised 11 November 2025, accepted
10 January 2026, online 19 January 2026), 14 pages, all read; pp. 3–5 (MR-WENO review, troubled-cell
criterion, Tables 1–3) checked visually. Page 1 matches Crossref (title, four authors, venue, DOI).
Numbering cited here is that of this version.

# Key claims

Registry notation: the source's linear weights $\gamma_{l,k}$, $\bar\gamma_{l,k}$ are $d_{l,k}$,
$\bar d_{l,k}$; its $\bar\omega$ is $\alpha$; $\varepsilon$ is $\epsilon$; velocities $\mu,\nu$ are
$v_1,v_2$; its global indicator $\tau_2$ is written $\tau^{\mathrm{MR}}$ and the auxiliary $\tau_1$ of
$\beta_0$ is kept (page-local). The indicator interpolant $\phi$ is $g$ (degree
$n_{\mathrm g}=2$, as for Zuo & Zhu's tests in the registry), its coefficients $a_k$ are kept (page-local), and the scaled end derivatives are
$D_{\mathrm L}=\Delta x\,g'(x_{i-3/2})$, $D_{\mathrm R}=\Delta x\,g'(x_{i+3/2})$ (page-local).

1. SHMR-WENO applies MR-WENO, with characteristic decomposition for systems, only in troubled cells and the linear fifth-order flux $q_2(x_{i+1/2})$, component-wise, elsewhere, saving both the nonlinear weights and the characteristic projection (§2.2, Remarks 1–2, §4). **Stated**
2. The indicator uses a quadratic interpolant of $u_{i-1},u_i,u_{i+1}$ instead of the quartic of Wang, Tian, Zhu & Zhao (2023); it is "much simpler" and reduces the number of troubled cells and the CPU time (Abstract, §1, §2.2). **Stated** (structure) / **Shown** (counts, timings)
3. Because $g'$ is linear, the signs of $g'$ at $x_{i-3/2}$ and $x_{i+3/2}$ decide whether $g$ has an extremum in $[x_{i-3/2},x_{i+3/2}]$ (§2.2). **Derived** (elementary)
4. Testing the smaller interval $[x_{i-1/2},x_{i+1/2}]$ "would result in unphysical oscillations due to the insufficient number of troubled-cells" (§2.2). **Stated** (no run shown)
5. The scaled derivative $\Delta x\,g'$ is used "in order to avoid the situation where the denominator $\Delta x$ is very small"; it has the signs of $g'$ (§2.2). **Stated**
6. Criterion: $I_i$ is troubled iff $(D_{\mathrm L}-\Delta x)(D_{\mathrm R}-\Delta x)<0$ and $(D_{\mathrm L}+\Delta x)(D_{\mathrm R}+\Delta x)<0$ (§2.2, p. 5). **Stated** (definition) *(Compiler check, not in the sources: interpolation gives $a_1=\tfrac12(u_{i+1}-u_{i-1})$, $a_2=\tfrac12(u_{i+1}-2u_i+u_{i-1})$, so $D_{\mathrm L}=a_1-3a_2=-u_{i+1}+3u_i-2u_{i-1}$ and $D_{\mathrm R}=a_1+3a_2=2u_{i+1}-3u_i+u_{i-1}$. The two products are negative together iff $\max(D_{\mathrm L},D_{\mathrm R})>\Delta x$ and $\min(D_{\mathrm L},D_{\mathrm R})<-\Delta x$: a sign change with a dead band of half-width $\Delta x$, not the plain sign test of the prose. $D_{\mathrm L},D_{\mathrm R}$ carry the units of $u$ and $\Delta x$ a length, so under $u\mapsto\sigma u$ the flags change: the criterion is not [scale-invariant](/properties/scale-invariance.md).)*
7. In 2D a cell is troubled if flagged in either direction; reconstruction is dimension by dimension (Remark 1). **Stated**
8. For the Euler equations the indicator is built from $\rho$, for scalar laws from $u$ (Remark 3). **Stated**
9. The scheme inherits from the earlier hybrid "compact reconstruction, low numerical dissipation, robustness and arbitrary linear weights" (§1, §4). **Stated**
10. MR-WENO background: the linear weights may be any positive numbers summing to one, here $\bar d_{l,k}=10^l$, so the same set serves every point and [negative linear weights](/methods/negative-linear-weights.md) are avoided (§1, §2.1). **Stated**
11. MR-WENO background: $\beta_1,\beta_2$ are Jiang–Shu [smoothness indicators](/definitions/smoothness-indicator.md); $\beta_0$ of the constant is built from the two-cell differences, $\beta_0=\big(\omega_{1\mathrm L}(\bar u_i-\bar u_{i-1})+\omega_{1\mathrm R}(\bar u_{i+1}-\bar u_i)\big)^2$ with Z-type weights and adaptive linear weights $\tfrac{10}{11}$ or $\tfrac1{11}$; $\tau^{\mathrm{MR}}=\big(\tfrac12(|\beta_0-\beta_2|+|\beta_1-\beta_2|)\big)^2$ and $\alpha_l=d_{l,2}\big(1+\tau^{\mathrm{MR}}/(\beta_l+\epsilon)\big)$, $\epsilon=10^{-10}$ (§2.1). **Stated** (background)
12. 2D Euler, $\gamma=3$, $T=3$, $80^2$–$200^2$, $\Delta t\propto\Delta x^{5/3}$: MR-WENO, SHMR-WENO and HMR-WENO print identical density errors, from $L^1=4.73\times10^{-6}$, $L^\infty=7.86\times10^{-5}$ to $L^1=5.84\times10^{-8}$ (order 4.94) and $L^\infty=1.26\times10^{-6}$ (order 5.03) (Table 1, §3.1). **Shown**
13. On this smooth test the hybrids flag no cell and "are effectively equivalent to directly employing linear reconstruction"; SHMR-WENO is the cheapest in error against CPU time "since the lower-degree polynomial is used" (§3.1, Fig. 1). **Shown** (figure, no numbers)
14. Troubled-cell percentages SHMR / HMR: 1D Burgers 2.03 / 3.26; Lax 5.67 / 7.49; Shu–Osher 5.61 / 6.46; blast waves 3.42 / 4.54; 2D Burgers 0.73 / 1.14; double Mach reflection 2.94 / 3.60; forward step 7.69 / 9.21 (Table 2). **Shown**
15. CPU seconds MR-WENO / SHMR-WENO (ratio) / HMR-WENO (ratio): 1D Burgers 0.0365 / 0.0286 (0.78) / 0.0321 (0.88); Lax 0.6613 / 0.3603 (0.54) / 0.3988 (0.60); Shu–Osher 3.5814 / 1.7544 (0.49) / 1.9490 (0.54); blast waves 26.381 / 12.815 (0.49) / 14.347 (0.54); 2D Burgers 46.037 / 34.758 (0.76) / 38.751 (0.84); double Mach reflection 113153 / 47482 (0.42) / 54055 (0.48); forward step 106863 / 45407 (0.42) / 51097 (0.48) (Table 3; no hardware stated). **Shown** *(Compiler check, not in the sources: e.g. $47482/113153=0.420$, $54055/113153=0.478$; the printed ratios follow from the printed times.)*
16. "In summary, the SHMR-WENO scheme outperforms the other schemes in terms of efficiency" (§3.2). **Shown** (Tables 2–3)
17. 1D Burgers, Lax and Shu–Osher: all schemes comparable, non-oscillatory (Examples 3.2–3.4, Figs. 2–4). **Shown** (visual)
18. Blast waves: the hybrids are "closer to the reference solution at $x\in[0.75,0.8]$" than MR-WENO (Example 3.5, Fig. 5). **Shown** (visual)
19. Double Mach reflection: SHMR-WENO "has slightly better resolution than the other schemes" and identifies troubled cells more efficiently than HMR-WENO (Example 3.7, Figs. 7–9). **Shown** (visual)
20. Forward step: fewer flags than HMR-WENO "due to the lower-degree polynomial" and "superior capability in resolving fine local structures" (Example 3.8, Figs. 10–11). **Shown** (visual)
21. For quintic or higher-degree polynomials exact extreme-point location is "not only time-consuming but often unavailable" (§1). **Stated**
22. Future work: triangular meshes (§4). **Stated**

# Printed slips

- §2.2: "the fifth-order polynomial $q_2(x)$ in (2.5)": $q_2$ matches five cell averages and has degree 4; "fifth-order" is its accuracy.
- §2.1: $\tau_2$ is called "the absolute difference between smoothness indicators", but it is the square of the mean of two absolute differences.
- The prose describes a plain sign test of the scaled derivative, while the printed criterion adds the $\pm\Delta x$ shifts (Key claim 6); the shifts are not discussed.
- §2.2 does not say which cell's flag decides the flux $\hat f^-_{i+1/2}$, whose stencil is centred on $I_{i+1}$.
- Symbol overloads: $\gamma$ (linear weights and ratio of specific heats), $p$ (reconstruction polynomial and pressure), $q$ (time-step exponent and polynomials $q_k$).
- Typos: "Admas and Shariff" (Adams), "a serious of" (series), "auxilary", "sings" (signs); Example 3.8 is "the step forward problem" in the text and "Forward step problem" in Tables 2–3.

# Notation map

| Zhang et al. (2026a) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$, $I_i$, $x_i$, $\Delta x$ | same | finite-difference point values |
| $h(x)$ | Shu–Osher function | **$h$ is the two-point flux in the registry** |
| $f^\pm=\tfrac12(f\pm\alpha u)$, $\alpha=\max\lvert f'\rvert$ | $f^\pm=\tfrac12(f\pm au)$ | global or local not stated |
| $\bar\eta_i$ | $f^\pm(u_i)$ | data of the flux reconstruction |
| $q_k$, $p_k$ | kept | MR-WENO polynomials, as on [multi-resolution WENO](/methods/multi-resolution-weno.md) |
| $\gamma_{l,k}$, $\bar\gamma_{l,k}=10^l$ | $d_{l,k}$, $\bar d_{l,k}$ | **$\gamma$ is the ratio of specific heats** |
| $\gamma_{1L}$, $\gamma_{1R}$, $\beta_{1L}$, $\beta_{1R}$, $\tau_1$ | kept (page-local) | auxiliaries of $\beta_0$ |
| $\beta_k$ | $\beta_k$ | Jiang–Shu form for $k=1,2$ |
| $\tau_2$ | $\tau^{\mathrm{MR}}$ (page-local) | squared mean of two absolute differences, exponent 1 |
| $\bar\omega_{l,2}$, $\omega_{l,2}$, $\varepsilon$ | $\alpha_l$, $\omega_l$, $\epsilon$ | $\epsilon=10^{-10}$ |
| $\phi$, $\varphi_k$, $a_k$ | $g$ ($n_{\mathrm g}=2$), $((x-x_i)/\Delta x)^k$, $a_k$ (page-local) | **$\phi$ is the volume fraction or potential, $a$ the wave speed** |
| $\hat\phi'(x_{i\mp3/2})$ | $D_{\mathrm L}$, $D_{\mathrm R}$ (page-local) | scaled end derivatives |
| $\mathcal L$, $C_{cfl}$ | $\mathcal L$, $\nu$ | CFL 0.6 |
| $q$ (time step) | kept | $\Delta t\propto\Delta x^q$, $q=5/3$ for accuracy tests; **$q$ is the weight exponent in the registry** |
| $\rho,\mu,\nu,E,p$ | $\rho,v_1,v_2,E,p$ | **$\nu$ is the CFL number** |
| HMR-WENO | MR-WENO + indicator of Wang, Tian, Zhu & Zhao (2023) | **not the HMR-WENO of [Zuo & Zhu (2024b)](/sources/zuo-2024-b.md)** |

# Reference list

32 printed references in numbered style ([1]–[32]), all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `zhang-2026`; no DOIs are printed. Ref. [2], Wang, Tian,
Zhu & Zhao (Commun. Nonlinear Sci. Numer. Simul. 126:107439, 2023), shares its first-author–year key with
the different ingested source `wang-2023` and is identified by venue, volume and page. Ref. [23] (J.
Comput. Phys. 508:112996) is the ingested [Zuo & Zhu (2024a)](/sources/zuo-2024.md). Ref. [3], Harten et
al., prints volume 131, pages 3–47 (those of the 1997 reprint) with the year 1987 of the original and is
identified by volume and page. Same-first-author–year works: Zhu (2017), J. Sci. Comput. 73 ([17]) and SIAM J.
Sci. Comput. 39 ([22]). No printed duplicates.

# Pages created or updated

Chunk 13 (2026-11-01). This source is cited on:

* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [Multi-resolution WENO](/methods/multi-resolution-weno.md)
* [Negative linear weights](/methods/negative-linear-weights.md)
* [Scale and affine invariance](/properties/scale-invariance.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
