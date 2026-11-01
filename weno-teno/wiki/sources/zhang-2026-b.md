---
type: Source
title: "Zhang et al. (2026) — Sixth-Order Finite Volume Hermite WENO Schemes with Adaptive Linear Weights"
description: "Sixth-order finite-volume Hermite WENO in CWENO form, one quintic plus two (1D) or four (2D, least squares) linear polynomials, with scale-invariant Z-type weights and a big-stencil linear weight switched among 10^2, 10^4, 10^6 by a ratio of the global indicator to the small-stencil indicators."
resource: "doi:10.1007/s10915-026-03477-4"
source_kind: paper
authors: [Zhang J., Tao Z., Zhu J.]
year: 2026
venue: "J. Sci. Comput. 109:72"
local_file: "/home/stefano/papers/mosaic/weno-teno/2026_Crossref_Journal_of_Scientific_Computing_Zhang_Sixth-Order_Finite_Volume_Hermite_WENO_Schemes_with_Adap.pdf"
tags: [weno, hermite-weno, weno-weights, scale-invariance, finite-volume]
timestamp: 2026-11-01T18:54:00Z
---

# Summary

Zhang et al. (2026b) (Zhang, Tao & Zhu) build a sixth-order finite-volume
[Hermite WENO](/methods/hermite-weno.md) for 1D and 2D hyperbolic conservation laws on the Qiu–Shu data:
the cell averages $\bar u_i$ and the cell averages $\bar v_i$ of $v=\partial_xu$ (in 2D also of
$\partial_yu$), the derivative obeying $\partial_tv+\partial_x(f'(u)v)=0$. The reconstruction is of
[CWENO](/methods/cweno.md) form: one quintic on $\{I_{i-1},I_i,I_{i+1}\}$ fitted to three averages and three
derivative averages, plus two linear polynomials on the two-cell stencils; in 2D a quintic on the
$3\times3$ block and four linear polynomials on the $2\times2$ sub-blocks, all by least squares with
$\bar u_{i,j}$ kept exactly ("truly two-dimensional"). Any positive linear weights keep sixth order. The
interface derivative values are the linear values of the quintic.

Two further ingredients are claimed. The [WENO-Z](/methods/weno-z.md)-type weights are normalized by
$u_{\mathrm{hp}}$, the squared mean absolute cell average of the stencil, following Don et al. (2022) and
[Fan et al. (2025a)](/sources/fan-2025.md), and Remark 1 proves them
[scale-invariant](/properties/scale-invariance.md). And the big-stencil linear weight is adaptive:
$\bar d_3\in\{10^2,10^4,10^6\}$ (ALW-I) or $\{10^2,10^6\}$ (ALW-II), switched by
$\mathrm{pf}=\sqrt\tau/\overline{\beta}_{\text{small}}$; "informal" Taylor and step-function analyses
place $\mathrm{pf}$ near $0$, $10/3$ or $3004/125$ in smooth regions and above $94.91$ or $2319.47$ at a
jump. This adaptive switch is a different idea from the "adaptive linear weights" of Lin & Zhu's CWENO
variant, which keep the name on the [CWENO](/methods/cweno.md) page.

Evidence: sixth-order tables on 1D and 2D [Burgers](/benchmarks/burgers-equation-tests.md) and $\gamma=3$
Euler data with error–CPU plots; the Lax problem and a scaled Lax problem
([shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)), [Shu–Osher](/benchmarks/shu-osher-problem.md),
[Woodward–Colella](/benchmarks/woodward-colella-blast-wave.md), a
[2D Riemann problem](/benchmarks/two-dimensional-riemann-problems.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md) and the
[Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md). HWENO-ALW-I gives the finest
structures; on double Mach reflection it matches the [multi-resolution WENO](/methods/multi-resolution-weno.md)
of Zhu & Shu run on a mesh of equal unknowns in about a quarter of its CPU time.

# Version read

Version of record (Springer typeset; received 9 December 2025, revised 6 September 2026, accepted
7 September 2026, online 3 October 2026), 36 pages, all read; pp. 4–9 and 11–16, where the text layer loses
primes, bars and absolute values, read visually. Page 1 matches Crossref (title, three authors, venue,
DOI). Numbering cited here is that of this version.

# Key claims

Registry notation: the source's linear weights $\gamma_k$, $\bar\gamma_k$ are $d_k$, $\bar d_k$; $\bar\omega_k$
is $\alpha_k$; $\varepsilon$ is $\epsilon$; the scaling constant $\zeta$ is $\sigma$; velocities $\mu,\nu$ are
$v_1,v_2$. The global indicator $\tau$, the scale factor $u_{\mathrm{hp}}$ and the switch $\mathrm{pf}$ are
page-local, as are the derivative averages $\bar v_i$ (and $\bar w_{i,j}$ of $\partial_yu$). In 1D the big
polynomial is $p_3$, in 2D $p_5$.

1. A sixth-order finite-volume HWENO can be built from one quintic and two (1D) or four (2D) linear polynomials, simpler than the multi-resolution HWENO of Li, Shu & Qiu and compact and truly two-dimensional in 2D (§1, §2.1.1, §2.2.1). **Stated**
2. Sixth order in smooth regions: $\omega_k-d_k=O(\Delta x^4)$, so $u-p=O(\Delta x^6)+O(\Delta x^4)\,O(\Delta x^2)=O(\Delta x^6)$ (Remark 2; 2D: Remark 5). **Derived**
3. In 1D, $\beta_k=u'^2\Delta x^2+O(\Delta x^3)$ ($k=1,2$) and $\beta_3=u'^2\Delta x^2+O(\Delta x^4)$ when $u'\ne0$; $\beta_k=C\Delta x^4+O(\Delta x^5)$, $\beta_3=C_3\Delta x^4+O(\Delta x^6)$, $C\ne C_3$, when $u'=0$; so $\tau=O(\Delta x^6)$ or $O(\Delta x^8)$ (Remark 2). **Derived**
4. The weights $\alpha_k=d_k\big(1+\tau/(\beta_ku_{\mathrm{hp}}+\epsilon u_{\mathrm{hp}}^2)\big)$, $\tau=\big(\tfrac12(|\beta_3-\beta_1|+|\beta_3-\beta_2|)\big)^2$, $u_{\mathrm{hp}}=\big(\tfrac13(|\bar u_{i-1}|+|\bar u_i|+|\bar u_{i+1}|)\big)^2+10^{-40}$, $\epsilon=10^{-10}$, satisfy $\alpha_k[\sigma u]=\alpha_k[u]$ for constant $\sigma>0$, since $u_{\mathrm{hp}}$ and $\beta_k$ scale as $\sigma^2$ and $\tau$ as $\sigma^4$ (Eqs. (2.11)–(2.13), Remark 1). **Proved** (the $10^{-40}$ floor is neglected)
5. For the Euler equations the [characteristic decomposition](/methods/characteristic-decomposition.md) of $f'(u)$ is applied to both $u$ and $v$, and $u_{\mathrm{hp}}$ of every component is computed from the density; "robust and effective in our numerical experiment" (Remarks 3, 6). **Stated**
6. ALW-I: $\mathrm{pf}=\sqrt\tau/\big(\tfrac12(\beta_1+\beta_2)\big)$ and $\bar d_3=10^2$ if $\mathrm{pf}>10^3$, $10^4$ if $1<\mathrm{pf}\le10^3$, $10^6$ if $\mathrm{pf}\le1$, with $\bar d_1=\bar d_2=1$ (Eqs. (2.15)–(2.16); 2D (2.32)–(2.33)); ALW-II: $10^2$ if $\mathrm{pf}>50$, $10^6$ otherwise (§2.1.3, §2.2.3). **Stated** (definition)
7. 1D smooth, $u'\ne0$: $\mathrm{pf}=O(\Delta x)$, so $\bar d_3=10^6$ (§2.1.2, Case 1). **Derived**
8. 1D smooth, $u'=0\ne u''$: $\sqrt\tau=\tfrac56u''^2\Delta x^4+O(\Delta x^5)$, $\beta_k=\tfrac14u''^2\Delta x^4+O(\Delta x^5)$, $\mathrm{pf}=\tfrac{10}3+O(\Delta x)$, so $\bar d_3=10^4$ (Case 2). **Derived** *(Compiler check, not in the sources: $\tfrac56/\tfrac14=\tfrac{10}3$.)*
9. 1D smooth, $u'=u''=0\ne u'''$: $\mathrm{pf}=\tfrac{3004}{125}+O(\Delta x)\approx24.03$, so $\bar d_3=10^4$ (Case 3). **Derived** *(Compiler check, not in the sources: $\tfrac{1043}{960}-\tfrac{25}{576}=\tfrac{751}{720}$ and $\tfrac{751}{720}\big/\tfrac{25}{576}=\tfrac{3004}{125}$.)*
10. Step of height $C_d$ inside $I_i$ at $x_{i-1/2}+a\Delta x$, $a\in[0,1)$: $\mathrm{pf}=\tfrac{67349}{105}+\tfrac{563825}{336(1-2a+2a^2)}\ge\tfrac{1298903}{560}\approx2319.47$, so $\bar d_3=10^2$ (Case 4.1). **Derived** *(Compiler check, not in the sources: $1-2a+2a^2\le1$ on $[0,1)$ with equality at $a=0$, and $\tfrac{67349}{105}+\tfrac{563825}{336}=\tfrac{1298903}{560}$.)*
11. Step inside $I_{i+1}$: $\mathrm{pf}=\tfrac{1140361}{560(a-1)^2}+\tfrac{5074889}{420(a-1)}+\tfrac{4324591}{240}$, minimum $\approx94.91$ at $a\approx0.66$, $\mathrm{pf}=10^3$ at $a_{1,2}\approx0.57,\,0.72$; $\bar d_3=10^4$ on $[a_1,a_2]$, $10^2$ elsewhere (Case 4.2). **Derived** *(Compiler check, not in the sources: minimizing the printed expression on a grid of $[0,1)$ gives $94.912$ at $a=0.663$ and the crossings $0.565$, $0.725$.)*
12. Hence $\bar d_3\in\{10^6,10^4\}$ in smooth regions and $\{10^2,10^4\}$ near discontinuities; the authors call these "informal explanations" (end of §2.1.2). **Derived** (informal)
13. If all small-stencil $\beta_k$ vanish, $\mathrm{pf}$ is undefined and $\bar d_3=10^6$ is set (Remark 4). **Stated**
14. 2D: $\nabla u\ne0$ gives $\bar d_5=10^6$; at $u_x=u_y=0$, $\mathrm{pf}=\max\big(\tfrac{10}3+\tfrac23\cdot\tfrac{11u_{xy}^2}{9u_{xx}^2+8u_{xy}^2+9u_{yy}^2},\,\tfrac{|12u_{xy}(u_{xx}+u_{yy})|}{9u_{xx}^2+8u_{xy}^2+9u_{yy}^2}\big)+O(\Delta x)$, "usually" between 1 and $10^3$, so $\bar d_5=10^4$; a step in $x$ reproduces the 1D values (§2.2.2, Cases 1–4). **Derived**
15. The criterion reuses $\tau$ and $\beta_k$, whereas the adaptive weights of Lin et al. (2023) and [Lin & Zhu (2024)](/sources/lin-2024-b.md) are "based on both point values and cell averages, and the point values need to be recalculated multiple times", and the 2D criterion is truly two-dimensional where Lin et al. (2023) work dimension by dimension (Remark 7). **Stated**
16. Reflective boundary values of the derivative averages follow from the parity of each conserved variable: derivatives of even variables are odd and vice versa (Remark 8). **Derived**
17. 1D Burgers ($T=0.5/\pi$, $N=100$–$200$): all four schemes reach the design order; at $N=200$, $L^1$ is $6.08\times10^{-11}$ (HWENO-MR), $3.96\times10^{-10}$ (FLW), $6.00\times10^{-11}$ (ALW-I), $5.68\times10^{-11}$ (ALW-II); ALW-I/II are the most efficient in error against CPU time (Table 1, Fig. 4). **Shown**
18. 1D and 2D Euler with $\gamma=3$ and 2D Burgers: design order for all schemes; ALW-I/II more efficient than HWENO-MR (Tables 2–4, Figs. 5–7). **Shown**
19. Lax problem: HWENO-MR and HWENO-ALW-I resolve best; the triplets $(10^2,10^4,10^6)$, $(10^2,10^5,10^8)$, $(10^1,10^5,10^9)$ give comparable results (Figs. 9–10). **Shown**
20. Lax data scaled to $(\sigma\rho,v_1,\sigma p)$: at $\sigma=10^{-6}$ the schemes without scale invariance oscillate and those with it are almost oscillation-free; at $\sigma=10^6$ all are non-oscillatory (Fig. 11). **Shown**
21. Shu–Osher ($N=400$) and blast waves ($N=800$): ALW-I resolves the entropy waves best and is best in $x\in[0.56,0.62]$, while HWENO-MR has slightly higher peaks in $x\in[0.75,0.8]$ (Figs. 12–15). **Shown**
22. 2D Riemann problem ($400^2$), double Mach reflection ($1920\times480$) and Rayleigh–Taylor ($240\times960$): ALW-I resolves finer structures than the other three (Figs. 17, 18, 20). **Shown**
23. Double Mach reflection: ALW-I takes 45.44 h on $1920\times480$, 125 % of WENO-MR's 36.35 h, with higher resolution; WENO-MR on $3324\times831$ (about the same unknowns) reaches comparable resolution in 187.62 h, 413 % of ALW-I (Fig. 19; hardware not stated). **Shown** *(Compiler check, not in the sources: $45.44/36.35=1.250$, $187.62/45.44=4.129$.)*
24. HWENO-MR with the standard weights $\bar d_{l_1,l_2}=10^{l_1-1}$ of Li, Shu & Qiu "fails to simulate" the Rayleigh–Taylor problem; the result shown uses $4^{l_1-1}$ (Example 3.12; failure not plotted). **Stated**
25. Any positive linear weights summing to one may be used, "which can avoid the generation of the negative weights" ([negative linear weights](/methods/negative-linear-weights.md); §4). **Stated**

The accuracy tables print identical columns: in Table 4 (2D Euler) the four schemes have the same errors in
every entry, and in Table 2 (1D Euler) HWENO-ALW-II equals HWENO-MR in every entry. The paper does not
comment on this.

# Printed slips

- Example 3.12 (p. 31): "At the top and bottom boundaries, we set the values as $(\rho,\mu,\nu,p)=(2,0,0,1)$ and $(\rho,\mu,\nu,p)=(1,0,0,2.5)$, respectively." *(Compiler check, not in the sources: the printed initial data give $\rho=2$, $p=2y+1=1$ at $y=0$ and $\rho=1$, $p=y+\tfrac32=2.5$ at $y=1$, so the pairing of "top and bottom … respectively" is reversed.)*
- Remark 5 (p. 13): "$\omega_k-\gamma_k=O(\sum_{s+r=4}\Delta x^s\Delta y^r),\ 1,\cdots,5$", with "$k=$" missing; its case split "$u_xu_y\ne0$" / "$u_x=u_y=0$" leaves out the case where exactly one of $u_x,u_y$ vanishes (treated as Case 2 of §2.2.2).
- Table 2: the $L^\infty$ order cell of HWENO-FLW at $N=100$ is empty where other tables print "–".
- §1: "Li at el.".

# Notation map

| Zhang et al. (2026b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $\bar u_i$, $I_i$, $\Delta x$ | same | finite volume |
| $v=u_x$, $w=u_y$; $\bar v_i$, $\bar w_{ij}$ | kept (page-local) | derivative averages; **$w$ is the entropy variable in the registry** |
| $h(u,v)=f'(u)v$; $q,r,s$ | kept (page-local) | fluxes of the derivative equations; **$h$ is the two-point flux, $q$ the weight exponent** |
| $\hat f(a,b)$, $\alpha=\max\lvert f'\rvert$ | $h^{\mathrm{LF}}$, $a$ | local Lax–Friedrichs; same speed for $\hat h$ |
| $u^\mp_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | same convention |
| $I_1,\dots,I_9$ | kept | $3\times3$ block, $I_5=I_{ij}$ |
| $p_1,p_2,p_3$ (1D), $p_1,\dots,p_5$ (2D) | kept | big polynomial last |
| $r$ (in $\beta_k$) | polynomial degree (page-local) | **$r$ is the stencil size in the registry** |
| $\gamma_k$, $\bar\gamma_k$ | $d_k$, $\bar d_k$ | **$\gamma$ is the ratio of specific heats** |
| $\bar\omega_k$, $\omega_k$, $\varepsilon$ | $\alpha_k$, $\omega_k$, $\epsilon$ | $\epsilon=10^{-10}$ |
| $\tau$ | $\tau$ (page-local) | squared mean of $\lvert\beta_{\text{big}}-\beta_k\rvert$, not the registry's $\tau_5$ |
| $u_{hp}$ | $u_{\mathrm{hp}}$ (page-local) | density-based for Euler |
| $\zeta$ | $\sigma$ | scaling of [scale invariance](/properties/scale-invariance.md) |
| $pf$ | $\mathrm{pf}$ (page-local) | switch of the adaptive weights |
| $C_d$, $x_d$, $a$ | kept (page-local) | step height, position, offset; **$a$ is the wave speed** |
| $\mathcal M_1,\dots,\mathcal M_4$ | kept (page-local) | quadratic forms of the 2D Case 3 |
| $\lambda_l$, $\omega_l$ (Gauss) | kept | **$\omega_l$ collides with the nonlinear weights** |
| $C_{cfl}$, $q$ | $\nu$, kept | CFL 0.6, $\Delta t\propto\Delta x^q$, $q=2$ in accuracy tests |
| $\mu$, $\nu$ | $v_1$, $v_2$ | **$\nu$ is the CFL number** |

# Reference list

33 printed references in numbered style ([1]–[33], alphabetical), all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `zhang-2026-b`. Ref. [9] (Fan et al., J. Sci. Comput. 102,
2025, printed without article number) is the ingested [Fan et al. (2025a)](/sources/fan-2025.md); ref. [18]
is the ingested [Lin & Zhu (2024)](/sources/lin-2024-b.md); ref. [17], Lin et al. (J. Comput. Phys.
493:112471, 2023), is not the ingested `lin-2023`. Ref. [10], Harten et al., prints volume 131, pages 3–47
(the 1997 reprint) with the year 1987 and is identified by volume and page; ref. [8] (Dumbser et al.,
SIAM J. Sci. Comput. 39) has no pages. No printed duplicates.

# Pages created or updated

Chunk 13 (2026-11-01). This source is cited on:

* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Central WENO (CWENO)](/methods/cweno.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Hermite WENO](/methods/hermite-weno.md)
* [Multi-resolution WENO](/methods/multi-resolution-weno.md)
* [Negative linear weights](/methods/negative-linear-weights.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Scale and affine invariance](/properties/scale-invariance.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
