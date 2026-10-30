---
type: Source
title: "Zhang & Shu (2010) — On positivity-preserving high order discontinuous Galerkin schemes for compressible Euler equations on rectangular meshes"
description: "Founding positivity paper for high-order DG and finite-volume Euler schemes: a Gauss–Lobatto decomposition of the cell average proves positive density and pressure of the averages under a reduced CFL, enforced by a conservative, accuracy-preserving two-step scaling limiter; extended to rectangles and tested on vacuum, Leblanc, Sedov and Mach 2000 jet problems."
resource: "doi:10.1016/j.jcp.2010.08.016"
source_kind: paper
authors: [Zhang X., Shu C.-W.]
year: 2010
venue: "J. Comput. Phys. 229(23):8918-8934"
local_file: "/home/stefano/papers/mosaic/weno-teno/2010_Crossref_Journal_of_Computational_Physics_Zhang_On_positivity-preserving_high_order_discontinuous_Galerkin_s.pdf"
tags: [dg, positivity, bound-preserving, limiting, euler-equations]
timestamp: 2026-10-30T08:43:00Z
---

# Summary

Zhang & Shu (2010b) construct finite-volume and
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) schemes of arbitrary order
for the compressible Euler equations whose cell averages stay in the convex admissible
set $G=\{\rho>0,\ p>0\}$. The paper extends the maximum-principle framework of Zhang &
Shu (2010a) and the positivity framework of Perthame & Shu (1996), and founds the
positivity branch of [bound preservation](/properties/bound-preservation.md).

Theorem 2.1 concerns the forward-Euler update of the cell average of a degree-$N$
polynomial with a positivity-preserving two-point flux. If the polynomial lies in $G$
at the $N_{\mathrm{GL}}$ Legendre Gauss–Lobatto points of every cell
($2N_{\mathrm{GL}}-3\ge N$), the new average lies in $G$ under the CFL condition of the
first-order scheme multiplied by the Gauss–Lobatto endpoint weight. The proof writes the
average as the Gauss–Lobatto quadrature and the update as a convex combination of
interior point values and two first-order updates. This is the classic
[cell-average decomposition](/methods/optimal-cell-average-decomposition.md).
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) and multistep methods keep the property
by convexity. Remark 2.4 proves that the first-order global
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md) scheme is positivity preserving for
$a\Delta t/\Delta x\le1$, which relaxes the $\tfrac12$ of Perthame & Shu.

The sufficient condition is enforced by a two-step
[scaling limiter](/methods/zhang-shu-scaling-limiter.md) around the cell average. The
first step scales the density. The second intersects the segment from the average to
each offending point value with the surface $p=\varepsilon$, a quadratic in the segment
parameter. The limiter is conservative and keeps $(N+1)$th order for smooth solutions
away from the boundary of $G^\varepsilon$. §3 extends both to rectangles through a
tensor Gauss × Gauss–Lobatto decomposition.

§4 tests third-order RKDG with SSP-RK3, the positivity limiter and the characteristic
TVB limiter (applied first) on these cases:
[low-density advection](/benchmarks/density-wave-advection.md),
[Sedov blasts](/benchmarks/sedov-blast-wave.md),
[double rarefaction](/benchmarks/double-rarefaction-problem.md) with vacuum,
[Leblanc](/benchmarks/leblanc-shock-tube.md),
[Mach 80 and Mach 2000 jets](/benchmarks/high-mach-astrophysical-jet.md) and
[shock diffraction](/benchmarks/shock-diffraction.md). The positivity limiter allows much
larger TVB parameters than the TVB limiter alone; with zero parameter that limiter is a
[TVD](/definitions/total-variation-diminishing.md) limiter.

# Version read

Version of record, J. Comput. Phys. 229(23):8918–8934, 17 pages, all read. The pages
with equations, tables and figures (pp. 8919–8932) were read from page images, the rest
from the text layer. Received 4 March 2010, revised 6 July 2010, accepted 13 August 2010,
available online 18 August 2010. Page 1 matches the Crossref record. No identity problem.
Bundle label: Zhang & Shu (2010b). The maximum-principle paper (J. Comput. Phys.
229:3091) is Zhang & Shu (2010a), `zhang-2010`, not ingested.

# Key claims

Registry notation. The source writes $\mathbf w=(\rho,m,E)$ for the conserved state ($u$
here) and $u$ ($v$ in 2-D) for the velocity components ($v_1$, $v_2$ here). It writes $k$
for the polynomial degree ($N$ here) and $N$ for the number of Gauss–Lobatto points
($N_{\mathrm{GL}}$ here). The cell index $j$ becomes $i$, and the reconstructed or DG
polynomial $\mathbf q_j(x)$ becomes $u_h\vert_{I_i}$. Further translations: $\alpha_0$
becomes $c_0$, the Lax–Friedrichs coefficient $a_0$ becomes $a$ (global), and
$\lambda=\Delta t/\Delta x$ is kept as $\Delta t/\Delta x$. The Gauss–Lobatto endpoint
weight on $[-\tfrac12,\tfrac12]$ (source $\widehat w_1$, equal to
$1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$) is the registry's boundary weight $\varpi$. The
page-local symbol is $\varepsilon$, the positivity floor
(not the WENO regularization $\epsilon$).

1. The pressure $p(u)=(\gamma-1)\big(E-\tfrac12\lvert\rho v\rvert^2/\rho\big)$ is concave in $u$ for $\rho\ge0$. Jensen's inequality then gives $p(su_1+(1-s)u_2)\ge sp(u_1)+(1-s)p(u_2)$, and $G$ is convex (§1, Eq. (1.3)). **Stated**
2. If density or pressure becomes negative, the system becomes non-hyperbolic and the initial value problem is ill-posed (§1). **Stated**
3. Positivity-preserving first-order fluxes under a standard CFL condition $\frac{\Delta t}{\Delta x}\|(\lvert v\rvert+c)\|_\infty\le c_0$ (Eq. (1.5)) include Godunov [6], Lax–Friedrichs [20], Boltzmann-type [19] and HLL [12] (§1). **Stated**
4. Commonly used high-order schemes (RKDG with a TVB limiter, ENO and WENO finite volume and finite difference) do not in general preserve positivity for Euler (§1). **Stated**
5. Perthame & Shu [20] gave a sufficient condition: the point values $u^\mp_{i\pm1/2}$ and $\bar u^{n+1}_i-\mathsf a_{\mathrm{PS}}(u^-_{i+1/2}+u^+_{i-1/2})$ lie in $G$ under $\frac{\Delta t}{\Delta x}\|(\lvert v\rvert+c)\|_\infty\le\mathsf a_{\mathrm{PS}}c_0$, $\mathsf a_{\mathrm{PS}}\in(0,1]$ (page-local; source $a$). The second quantity is hard to enforce at arbitrary order without destroying accuracy (§1). **Stated**
6. Theorem 2.1: for the update (1.6), if $u_h\vert_{I_i}$ lies in $G$ at all $N_{\mathrm{GL}}$ Gauss–Lobatto points of every cell, with $2N_{\mathrm{GL}}-3\ge N$, then $\bar u^{n+1}_i\in G$ under $\frac{\Delta t}{\Delta x}\|(\lvert v\rvert+c)\|_\infty\le\varpic_0$ (Eq. (2.1)) (§2.1). **Proved**
7. SSP Runge–Kutta [25] and multistep [24] time discretizations keep Theorem 2.1 valid because $G$ is convex (Remark 2.2). **Stated** (by convexity)
8. Any quadrature that includes both cell ends and is exact for degree $N$ works. For $N=2,3$ the authors "have verified that the Gauss–Lobatto quadrature is the best choice", meaning the largest $\varpi$ (Remark 2.3). **Stated** (verification not shown)
9. For the Lax–Friedrichs flux with $a=\|(\lvert v\rvert+c)\|_\infty$, the first-order Lax–Friedrichs scheme is positivity preserving under $\frac{\Delta t}{\Delta x}a\le1$, relaxing the $\tfrac12$ proven in [20] (Remark 2.4). The proof writes the scheme as a convex combination of $u_i$ and $u_{i\pm1}\mp f(u_{i\pm1})/a$ and uses $p\big(u\pm f(u)/a\big)=\Big(1-\frac p\rho\frac{\gamma-1}{2(a\pm v)^2}\Big)\Big(1\pm\frac va\Big)p$, positive since $c\le a-\lvert v\rvert$. **Proved**
10. Table 2.1: with the Lax–Friedrichs flux, the CFL condition (2.1) is $\frac{\Delta t}{\Delta x}a\le\tfrac16$ for $N=2,3$ (points $\{-\tfrac12,0,\tfrac12\}$) and $\le\tfrac1{12}$ for $N=4,5$ (points $\{-\tfrac12,-\tfrac1{\sqrt{20}},\tfrac1{\sqrt{20}},\tfrac12\}$). These are "comparable with and only slightly more restrictive than" the linear-stability CFL of DG [5] (§2.1). **Derived** *(Compiler check, not in the sources: the three- and four-point Gauss–Lobatto weights on $[-\tfrac12,\tfrac12]$ are $(\tfrac16,\tfrac23,\tfrac16)$ and $(\tfrac1{12},\tfrac5{12},\tfrac5{12},\tfrac1{12})$, so the table is $\varpic_0$ with $c_0=1$.)*
11. The density step (2.4)–(2.5) keeps the cell average and gives $\hat\rho(x^{\mathrm{GL}}_\alpha)\ge\varepsilon$. Its accuracy "can be proven following the same lines as in [26]" (§2.2). **Stated**
12. Lemma 2.5: the limited polynomial of (2.10)–(2.11) lies in $G^\varepsilon\subset G$ at every Gauss–Lobatto point (§2.2). **Proved**
13. If the exact solution $u$ is smooth with $d(u,G^\varepsilon)\ge M_{\mathrm d}>0$, where $d(z,G)=\min_{w\in G}\lVert z-w\rVert$ as printed ($M_{\mathrm d}$ page-local; source $M$), then $\lvert1-\theta_2\rvert=O(\Delta x^{N+1})$: the pressure limiter does not destroy accuracy (§2.2, after Lemma 2.5). **Derived** (assumes the overshoot at the limited point is $O(\Delta x^{N+1})$)
14. $\theta_2$ of (2.11) is "mathematically equivalent to" $\min_\alpha t^\alpha_\varepsilon$, where $t^\alpha_\varepsilon$ is the root of the quadratic $p\big((1-t)\bar u^n_i+t\hat u^\alpha\big)=\varepsilon$ (Eq. (2.12)), or 1 (§2.3). **Stated**
15. With SSP time stepping the limiter is applied at every Runge–Kutta stage or every multistep step (§2.3, §3.2). **Stated**
16. For finite-volume WENO the limiter is harder to implement, because WENO gives only nodal values, not polynomials. One may build polynomials from nodal values and cell averages as in [26] (Remark 2.6). **Stated**
17. Enforcing (2.1) rigorously for SSP-RK3 needs a bound on $\|(\lvert v\rvert+c)\|_\infty$ over all three stages from data at $t^n$. In practice the authors multiply the value at $t^n$ by "a factor, for example 2 to 3". The complication does not exist for SSP multistep methods (Remark 2.7). **Stated**
18. Theorem 3.1 (rectangles): if the tensor Gauss × Gauss–Lobatto point values (Gauss in $x$ with Gauss–Lobatto in $y$, and the converse) lie in $G$, the new cell average lies in $G$ under $\frac{\Delta t}{\Delta x}\|(\lvert v_1\rvert+c)\|_\infty+\frac{\Delta t}{\Delta y}\|(\lvert v_2\rvert+c)\|_\infty\le\varpic_0$ (Eq. (3.13)) (§3.1). **Proved** ("following the same lines" as Theorem 2.1)
19. Third-order RKDG ($N=2$) with the positivity limiter reaches third order on the 2-D low-density test ($\min\rho=0.01$), with $L^1$ error $3.11\times10^{-6}$ and $L^\infty$ error $3.28\times10^{-5}$ at $128\times128$, $t=0.1$. The limiter "does get turned on for the coarser meshes" (§4.1, Table 4.1). **Shown**
20. The TVB limiter is still necessary for shocks: without it the DG scheme blows up on the Sedov blast waves even with the positivity limiter. The TVB limiter is applied before the positivity limiter (§4.2). **Shown** (outcome stated, no figure)
21. Without the positivity limiter, DG with the TVB limiter can blow up for TVB parameters $M_i>0$. $M_i=0$ stabilizes it but reduces it to a TVD limiter, first order at extrema, with unsatisfactory results. With the positivity limiter $M_i$ can be tuned "in a much larger range" (§4.2). **Shown** (outcome stated)
22. Double rarefaction with vacuum: without the positivity limiter DG blows up. The TVB limiter alone stabilizes it, with a result poor compared to Fig. 4.3 (§4.3). **Shown** (comparison not plotted)
23. Leblanc: good results with $(M_1,M_2,M_3)=(10^{10},10,10^{10})$ at $N_x=800$ and $(10^{20},100,10^{20})$ at $N_x=6400$. $M_2$ differs because the contact is the second characteristic field. Without the positivity limiter DG is unstable for such $M_i$ (§4.3, Fig. 4.4). **Shown**
24. The Mach 80 and Mach 2000 jets without radiative cooling are computed with $M_i=10^4$ and $10^7$. The Mach 80 result is "comparable to the one in [9]" (§4.4, Figs. 4.5–4.6). **Shown**
25. Shock diffraction: the result is comparable to [4], "with the advantage that negative pressure and density never appear". [4] needed an ad hoc positivity correction to avoid blow-ups (§4.5, Figs. 4.7–4.8). **Shown**
26. The limiter makes the density and pressure of the cell averages positive under a suitable CFL condition at "small additional computational cost". The extension to 3-D is "conceptually straightforward"; triangles need a special quadrature [28] (§5). **Stated**

Limiter as printed (§2.2–2.3), with $u^{\mathrm{GL}}_\alpha$ the value at Gauss–Lobatto point
$\alpha$. The density step is $\hat\rho=\theta_1(\rho_h-\bar\rho)+\bar\rho$ with
$\theta_1=\min\{(\bar\rho-\varepsilon)/(\bar\rho-\rho_{\min}),1\}$ and
$\rho_{\min}=\min_\alpha\rho_h(x^{\mathrm{GL}}_\alpha)$ (no absolute value). The pressure
step sets $G^\varepsilon=\{\rho\ge\varepsilon,\ p\ge\varepsilon\}$ and the segment
$s^\alpha(t)=(1-t)\bar u+t\hat u^\alpha$. Then $\tilde u=\theta_2(\hat u-\bar u)+\bar u$, with
$\theta_2=\min_\alpha\|s^\alpha_\varepsilon-\bar u\|/\|\hat u^\alpha-\bar u\|$, a ratio of
Euclidean distances. All components, including the already limited density, are scaled by
$\theta_2$. The floor is "for example ... $\varepsilon=10^{-13}$" (§2.2), and in the
flowchart $\varepsilon=\min_i\{10^{-13},\bar\rho_i,p(\bar u_i)\}$, one global value. In
2-D the cell average is the blend $\frac{a_1\Delta t/\Delta x}{\mu_{\mathrm{ZS}}}$(Gauss–Lobatto
in $x$) $+\frac{a_2\Delta t/\Delta y}{\mu_{\mathrm{ZS}}}$(Gauss–Lobatto in $y$), with
$\mu_{\mathrm{ZS}}=a_1\Delta t/\Delta x+a_2\Delta t/\Delta y$ (page-local; source $\mu$)
(Eq. (3.11)). The edge integrals use an $L$-point Gauss rule exact for degree $2N+1$.

Test data as printed (§4). Low-density test: $\rho_0=1+0.99\sin(x+y)$, $v=(1,1)$, $p=1$ on
$[0,2\pi]^2$, periodic, $t=0.1$. 1-D Sedov: $\rho=1$, $v=0$, $E=10^{-12}$, centre cell
$E_0/\Delta x$ with $E_0=3.2\times10^6$, $T=0.001$, $N_x=800$, $\Delta x=4/N_x$. 2-D Sedov:
lower-left cell $E=0.244816/(\Delta x\Delta y)$, $T=1$, $\Delta x=\Delta y=1.1/160$,
symmetry at left and bottom. Double rarefaction: $\rho=7$, $v=\mp1$, $p=0.2$, $T=0.6$,
$\Delta x=0.01$, no TVB limiter, from Linde & Roe. Leblanc: $\rho=(2,0.001)$, $v=0$,
$p=(10^9,1)$, $T=10^{-4}$, $\Delta x=20/N_x$. Jets ($\gamma=5/3$): Mach 80 on
$[0,2]\times[-0.5,0.5]$, jet $(\rho,v_1,v_2,p)=(5,30,0,0.4127)$ for $\lvert y\rvert\le0.05$,
ambient $(5,0,0,0.4127)$ (printed in both jet paragraphs), $T=0.07$, $448\times224$. Mach
2000 on $[0,1]\times[-0.25,0.25]$, jet speed 800, $T=0.001$, $640\times320$; both credited
to Ha, Gardner, Gelb & Shu [9]. Shock diffraction: Mach 5.09 shock at $x=0.5$,
$6\le y\le11$, into air of density 1.4 and pressure 1, on
$[0,1]\times[6,11]\cup[1,13]\times[0,11]$, $t=2.3$, $\Delta x=1/32$ and $1/64$, credited
to Cockburn & Shu [4]. The CFL numbers of the runs are not printed.

# Printed slips

- p. 8921, end of the proof of Theorem 2.1: "therefore $\mathbf H_1$ and $\mathbf H_2$ are in the set $G$", whereas the quantities defined in Eqs. (2.2)–(2.3) are $\mathbf H_1$ and $\mathbf H_N$.
- p. 8926, Theorem 3.1: the conclusion prints $\overline{\mathbf w}^{n+1}_j\in G$, whereas the 2-D cell average is $\overline{\mathbf w}^{n+1}_{ij}$.
- p. 8927, Eq. (3.18): $\tilde{\mathbf q}_{ij}(x,y)=\theta_2(\widehat{\mathbf q}_{ij}(x)-\overline{\mathbf w}^n_{ij})+\overline{\mathbf w}^n_{ij}$, with the argument $(x)$ for $(x,y)$.
- p. 8927, 2-D flowchart, last bullet: "under the CFL condition (2.1)", whereas the 2-D condition is (3.13).
- p. 8928, Table 4.1: the last $L^\infty$ order is printed as 3.02. *(Compiler check, not in the sources: $\log_2(2.83\times10^{-4}/3.28\times10^{-5})=3.109$, and the rounding intervals of the printed errors allow 3.104–3.114. The other printed orders agree with the printed errors to within rounding.)*
- p. 8923, accuracy argument after Lemma 2.5: $d(z,G)=\min_{w\in G}\lVert z-w\rVert$ is the distance to the set, and the assumption is printed as $d(v(x,t^n),G^\varepsilon)\ge M>0$. *(Compiler check, not in the sources: for a state inside $G^\varepsilon$ this distance is $0$, so the assumption as printed cannot hold; the argument uses the distance to the boundary $\partial G^\varepsilon$.)*
- p. 8925: "Subscripts or superscripts $\beta$ and $\gamma$ will be used only for Gauss quadrature points", while $\gamma$ is also the ratio of specific heats. $M$ (distance bound in §2.2, TVB constant in §4.2) and $N$ (Gauss–Lobatto points, number of cells in §4) carry two meanings each.

# Notation map

| Zhang & Shu (2010b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf w=(\rho,m,E)^T$, $(\rho,m,n,E)^T$ | $u=(\rho,\rho v,E)$ | $m,n$ the momenta |
| $u$, $v$ | $v_1$, $v_2$ | **collision**: source $u$ is the velocity |
| $\mathbf f$, $\mathbf g$ | $f$, $g$ ($f^{(1)},f^{(2)}$) | |
| $\mathbf h$, $\mathbf h_1$, $\mathbf h_2$ | $h(u^-,u^+)$ per direction | Lax–Friedrichs with global coefficients |
| $a_0$, $a_1$, $a_2$ | $a$ (global, per direction) | $\|(\lvert v_d\rvert+c)\|_\infty$ |
| $\alpha_0$ | $c_0$ | first-order positivity CFL constant, 1 for Lax–Friedrichs |
| $\lambda$, $\lambda_1$, $\lambda_2$ | $\Delta t/\Delta x$, $\Delta t/\Delta y$ | **collision** with the eigenvalues $\lambda_l$ |
| $k$ | $N$ | polynomial degree, order $N+1$ |
| $N$ | $N_{\mathrm{GL}}$ | **collision**: registry $N$ is the degree; source $N$ is also the number of cells in §4 ($N_x$ here) |
| $\widehat x^\alpha_j$, $\widehat w_\alpha$ | $x^{\mathrm{GL}}_\alpha$, Gauss–Lobatto weights on $[-\tfrac12,\tfrac12]$ | endpoint weight $\varpi$ (page-local); registry $\mathsf w_j$ |
| $x^\beta_i$, $w_\beta$, $L$ | Gauss points, weights, count | |
| $\mathbf q_j(x)$ | $u_h\vert_{I_i}$ | DG or reconstructed polynomial |
| $\overline{\mathbf w}^n_j$, $\mathbf w^\pm_{j+1/2}$ | $\bar u^n_i$, $u^\pm_{i+1/2}$ | source $-$ from the left cell: agrees with the registry |
| $\mathbf H_1$, $\mathbf H_N$ | first-order-type updates | |
| $\theta_1$, $\theta_2$ | $\theta$ (two steps) | |
| $\varepsilon$ | $\varepsilon$ (page-local floor) | not $\epsilon$ |
| $G$, $G^\varepsilon$ | $G$, $G^\varepsilon$ | agree |
| $\mathbf s^\alpha(t)$, $t^\alpha_\varepsilon$ | $s^\alpha(t)$, $t^\alpha_\varepsilon$ (page-local) | |
| $\mu$ | $\mu_{\mathrm{ZS}}$ (page-local) | **collision** with the affine translation $\mu$ |
| $M_i$, $\overline m$ | TVB parameters, TVB-corrected minmod | **collision** of $M$ with the Mach number |
| $a$ (Perthame–Shu) | $\mathsf a_{\mathrm{PS}}$ (page-local) | |

# Reference list

The paper prints 28 references, numbered [1]–[28], alphabetical by first author. The
list is merged complete into the [bibliography](/bibliography.md), with `citedby`
including `zhang-2010-b`. [10] is [Harten (1983a)](/sources/harten-1983.md); [12] (Harten,
Lax & van Leer, SIAM Rev.) is a distinct work. Several entries are mapped to the ingested
sources: [25] (Shu & Osher, J. Comput. Phys. 77) is [Shu & Osher (1988)](/sources/shu-1988.md);
[11] is [Harten et al. (1987a)](/sources/harten-1987.md); [13] is
[Jiang & Shu (1996)](/sources/jiang-1996.md); [17] is [Liu et al. (1994)](/sources/liu-1994.md).
[24] (Shu, SIAM J. Sci. Stat. Comput. 9) is the distinct work Shu (1988). [26] is Zhang &
Shu (2010a). [27] (Zhang & Shu, SIAM J. Numer. Anal. 48:772–795) is a third Zhang & Shu
2010 work, distinct from this paper. [15] (Linde & Roe) prints no year, only "AIAA
Paper-97-2098". [28] (Zhang, Xia & Shu) is printed as "submitted for publication" without
a year. [9] (Ha, Gardner, Gelb & Shu) prints J. Sci. Comput. 24 (2005) 597–612. No item is
unparseable.

# Pages created or updated

Chunk 12 (2026-10-30). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Double rarefaction (123) problem](/benchmarks/double-rarefaction-problem.md)
* [High-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md)
* [Optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
* [Sedov blast wave](/benchmarks/sedov-blast-wave.md)
* [Shock diffraction](/benchmarks/shock-diffraction.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
