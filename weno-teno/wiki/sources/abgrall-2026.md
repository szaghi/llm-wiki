---
type: Source
title: "Abgrall et al. (2026) — Bound-Preserving Point-Average-Moment PolynomiAl-Interpreted (PAMPA) Scheme: One-Dimensional Case"
description: "A priori bound-preserving version of the third-order 1D PAMPA scheme: high- and low-order fluxes for cell averages and residuals for interface point values are blended with explicit optimal coefficients, and positivity for Euler follows from geometric quasilinearization with a closed-form eigenvalue minimisation."
resource: "doi:10.4208/cicp.oa-2024-0266"
source_kind: paper
authors: [Abgrall R., Jiao M., Liu Y., Wu K.]
year: 2026
venue: "Commun. Comput. Phys. 39:29-58"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Communications_in_Computational_Physics_Abgrall_Bound-Preserving_Point-Average-Moment_PolynomiAl-Interpreted.pdf"
tags: [active-flux, bound-preserving, positivity, limiting, finite-volume]
timestamp: 2026-10-23T15:08:00Z
---

# Summary

The paper makes the one-dimensional third-order
[PAMPA scheme](/methods/pampa-scheme.md) (Point-Average-Moment PolynomiAl-interpreted)
bound preserving. PAMPA is the [Active Flux](/methods/active-flux.md)-type method of
Abgrall whose unknowns are the cell averages $\bar u_i$ and the point values
$u_{i+1/2}$ at the interfaces. The averages are updated in conservative form with the
physical flux of the interface point values; the point values are updated by
non-conservative upwind residuals computed from the parabola through
$u_{i-1/2},\bar u_i,u_{i+1/2}$. The high-order scheme oscillates at discontinuities
and is not [bound preserving](/properties/bound-preservation.md). Earlier PAMPA papers
used an a posteriori [MOOD](/methods/mood-a-posteriori-limiting.md) fallback.

The construction is a priori [convex limiting](/methods/convex-limiting.md). The
average update blends the high-order flux with a local Lax–Friedrichs flux of the
averages; the point update blends each of its two residuals with a first-order
residual built from the point value and the neighbouring average. Point values need
not be conservative, so each residual gets its own coefficient. Both forward-Euler
updates are convex combinations of the old value and intermediate states, so bounds
hold if each intermediate state satisfies them. This gives explicit coefficients for
the global maximum principle (Props. 3.1, 3.2) and for a local maximum principle on
averages, relaxed at smooth extrema by a derivative-based detector. For the Euler
equations, positivity of density and internal energy is enforced through
[geometric quasilinearization](/methods/geometric-quasilinearization.md)
([Wu & Shu (2023)](/sources/wu-2023-b.md)). The optimal internal-energy coefficient
is the inverse spectral radius of a $2\times2$ symmetric matrix (Appendix A).

Tests with [SSP-RK3](/methods/ssp-runge-kutta.md) at CFL 0.2: linear advection
(strict global bounds lower the order to about 2.2–2.6, relaxed bounds restore 3), the
[Jiang–Shu composite waves](/benchmarks/jiang-shu-composite-advection.md), a
[Burgers](/benchmarks/burgers-equation-tests.md) shock, the
[Buckley–Leverett problem](/benchmarks/buckley-leverett-problem.md), a near-vacuum
isentropic problem, [Sod](/benchmarks/sod-and-lax-shock-tubes.md),
[Shu–Osher](/benchmarks/shu-osher-problem.md),
[LeBlanc](/benchmarks/leblanc-shock-tube.md),
[double rarefaction](/benchmarks/double-rarefaction-problem.md) and
[Sedov](/benchmarks/sedov-blast-wave.md). The authors state that the sonic-point
problems reported for the generalized Active Flux of Duan, Barsukow & Klingenberg do
not appear.

# Version read

Version of record (Global-Science Press typeset, Commun. Comput. Phys. 39(1), January
2026; received 31 October 2024, accepted 30 April 2025), 30 pages (journal pp. 29–58),
all read; equations of pp. 34–45 and 46–55 checked on the page images. Page 1 matches
Crossref (title, four authors, volume, pages, DOI 10.4208/cicp.OA-2024-0266). Crossref
dates the work 2025 (online 7 November 2025), while the issue, the running heads and
the copyright line print 2026; by bundle law the slug and `year` take the issue year
2026. The key `abgrall-2025` belongs to a different work, Abgrall, Lin & Liu (Beijing
J. Pure Appl. Math.), cited here as ref. [2]. Numbering cited here is that of this
version.

# Key claims

Registry notation. The source writes cells $[x_j,x_{j+1}]$ with averages
$\bar u_{j+1/2}$ and point values $u_j$ at integer nodes. Here every source index is
shifted by $-\tfrac12$: the cell is $I_i$ with average $\bar u_i$, and its endpoint
values are $u_{i-1/2},u_{i+1/2}$. Page-local symbols: $\hat f^{\mathrm{LO}}_{i+1/2}$ the
local Lax–Friedrichs flux of $\bar u_i,\bar u_{i+1}$ with speed $a_{i+1/2}$ (source
$\alpha_j$); $u^*_{i+1/2}$ its bar state; $\Delta\hat f_{i+1/2}=f(u_{i+1/2})-\hat f^{\mathrm{LO}}_{i+1/2}$;
$a^{\mathrm L}_{i+1/2}$, $a^{\mathrm R}_{i+1/2}$ the speeds between $u_{i+1/2}$ and
$\bar u_i$, $\bar u_{i+1}$ (source $\beta_{j\mp1/2}$); $\vec\Phi_i$, $\overleftarrow\Phi_{i+1}$
the residuals sent to $x_{i+1/2}$ from $I_i$ and $I_{i+1}$; $\mathsf e_{i+1/2}$ the
flux blending coefficient and $\mathsf t^{\mathrm L}_{i+1/2}$, $\mathsf t^{\mathrm R}_{i+1/2}$
the residual blending coefficients (source $\eta_j$, $\theta_{j\mp1/2}$; 1 = high
order, 0 = low order); $\mathring u_{\min},\mathring u_{\max}$ the global bounds from
the initial data.

1. The BP PAMPA scheme needs no explicit reconstruction inside each element, which makes the construction flexible (Abstract; Conclusions). **Stated**
2. The first-order PAMPA scheme (local Lax–Friedrichs flux for averages, Eqs. (2.1a)–(2.3); Lax–Friedrichs-type residuals mixing point values and averages, Eqs. (2.4)–(2.5)) is bound preserving under $\frac{\Delta t}{\Delta x}\max a_{i+1/2}\le\tfrac12$, $\frac{\Delta t}{\Delta x}\max a^{\mathrm{L,R}}_{i+1/2}\le\tfrac12$ and $L\frac{\Delta t}{\Delta x}\le1$, $L$ the Lipschitz constant of the flux (§2). **Stated** (from refs. [1,2])
3. The high-order residuals are $\vec\Phi^{\mathrm{HO}}_i=a^+(u_{i-1/2}-3\bar u_i+2u_{i+1/2})$ and $\overleftarrow\Phi^{\mathrm{HO}}_{i+1}=a^-(-2u_{i+1/2}+3\bar u_{i+1}-u_{i+3/2})$, $a^\pm$ the positive and negative parts of $f'(u_{i+1/2})$ (for systems $R\Lambda^\pm L$), from the derivative of the parabola through $u_{i-1/2},\bar u_i,u_{i+1/2}$ (Eqs. (2.7)–(2.9)). **Derived**
4. With the blended flux $\hat f_{i+1/2}=\hat f^{\mathrm{LO}}_{i+1/2}+\mathsf e_{i+1/2}\Delta\hat f_{i+1/2}$ (Eq. (3.1)), the forward-Euler average update is the convex combination $\bar u^{n+1}_i=(1-\tfrac{\Delta t}{\Delta x}(a_{i-1/2}+a_{i+1/2}))\bar u^n_i+\tfrac{\Delta t}{\Delta x}a_{i-1/2}\tilde u^{\mathrm L}_i+\tfrac{\Delta t}{\Delta x}a_{i+1/2}\tilde u^{\mathrm R}_i$, with $\tilde u^{\mathrm L}_i=u^*_{i-1/2}+\mathsf e_{i-1/2}\Delta\hat f_{i-1/2}/a_{i-1/2}$ and $\tilde u^{\mathrm R}_i=u^*_{i+1/2}-\mathsf e_{i+1/2}\Delta\hat f_{i+1/2}/a_{i+1/2}$, under $\Delta t\le\Delta x/(a_{i-1/2}+a_{i+1/2})$ (§3.1, Eqs. (3.3)–(3.4)). **Derived**
5. The bar state $u^*_{i+1/2}$ lies between $\bar u_i$ and $\bar u_{i+1}$ (§3.1). **Stated** (from the choice (2.3) of the speed)
6. Prop. 3.1: with $\mathsf e_{i+1/2}=\min\big(1,\frac{a_{i+1/2}}{\lvert\Delta\hat f_{i+1/2}\rvert}\min(\mathring u_{\max}-u^*_{i+1/2},\,u^*_{i+1/2}-\mathring u_{\min})\big)$ (Eq. (3.5)), averages in $[\mathring u_{\min},\mathring u_{\max}]$ stay there. **Proved** (the time-step condition of claim 4 is stated before (3.5), not in the proposition)
7. Prop. 3.2: the analogous coefficients $\mathsf t^{\mathrm L}_{i+1/2}$, $\mathsf t^{\mathrm R}_{i+1/2}$ (Eqs. (3.13)–(3.14)), built from the bar states of $(\bar u_i,u_{i+1/2})$ and $(u_{i+1/2},\bar u_{i+1})$, make the point update (3.9) bound preserving. **Proved** (for $\mathsf t^{\mathrm L}$ only; the other case "omitted for saving space")
8. Two different blending coefficients can be used for the two residuals of one point value, because conservation is not needed for point values (§3.2). **Stated**
9. The two-sided minimum in (3.13), which uses $\lvert\Delta\vec\Phi\rvert$, covers a wrong estimate of the upwind direction that may flip the sign of $\Delta\vec\Phi$, "especially in the transonic case" (§3.2, end of proof). **Stated**
10. Local maximum principle on averages: with local bounds over $\bar u_i$ and the bar states $u^*_{i\pm1/2}$ (Eq. (3.17)) and coefficients chosen by the sign of $\Delta\hat f_{i+1/2}$ (Eq. (3.18)), the intermediate states stay within the local bounds of their cells (§3.3). **Proved** (formula called standard, after Kuzmin and Vilar)
11. A smooth-extrema detector (from refs. [3,31]) compares the derivatives of the cell parabola at the cell ends with those of the neighbouring parabolas; where it marks the cell as smooth only the global bounds are imposed. No local maximum principle and no detector are applied to point values, and no problem from this was observed (§3.3, Algorithm 1). **Stated** / **Shown**
12. For Euler, the invariant domain $\{\rho>0,\ \rho e>0\}$ equals its geometric-quasilinearization form $\{\rho>0,\ \varphi(u;v_*)>0\ \forall v_*\in\mathbb R\}$, $\varphi(u;v_*)=u\cdot(\tfrac12v_*^2,-v_*,1)^\top$, because $\varphi=\rho e+\tfrac12\rho(v-v_*)^2$ (§3.4, Eq. (3.19), following [Wu & Shu (2023)](/sources/wu-2023-b.md)). **Derived** *(compiler check, not in the sources: the identity follows from $E=\rho e+\tfrac12\rho v^2$.)*
13. The internal-energy coefficient is $\mathsf e^{e}_{i+1/2}=a_{i+1/2}\min_{v_*}\varphi(u^*_{i+1/2};v_*)/\lvert\varphi(\Delta\hat f_{i+1/2};v_*)\rvert$ (analogously for the residuals), and the final coefficient is the minimum of the density and internal-energy coefficients (§3.4). **Derived**
14. The minimum over $v_*$ of a ratio $Q(v_*)/\lvert P(v_*)\rvert$ of quadratics with $Q>0$ equals $\big(\max_{\lambda\in\sigma(\mathsf B^{-1/2}\mathsf A\mathsf B^{-1/2})}\lvert\lambda\rvert\big)^{-1}$, $\mathsf A$, $\mathsf B$ the $2\times2$ symmetric matrices of $P$ and $Q$ (Appendix A). **Derived** (Rayleigh-quotient argument)
15. The optimal-coefficient analysis by geometric quasilinearization carries over to several dimensions, in a separate paper (§1). **Stated**
16. The BP PAMPA scheme does not show the transonic issues of refs. [9,19], which required careful flux vector splitting in [9]; the Burgers results are "obtained without sonic point transition" (§1, Ex. 2). **Stated** / **Shown** (Burgers only)
17. The Jacobian splitting of PAMPA for Euler may give non-physical solutions (observed in refs. [9,19]); "our BP technique cures completely this problem" (§2). **Stated** / **Shown** (Euler tests)
18. Strict global bounds lower the linear-advection rates (cell averages, finest step $\Delta x=1.25\times10^{-3}$) to 2.61 ($L^1$), 2.18 ($L^2$), 1.78 ($L^\infty$); point values 2.61, 2.20, 1.81 (Table 1). **Shown**
19. With relaxed bounds, tolerance $\max(10^{-4},10^{-3}(\mathring u_{\max}-\mathring u_{\min}))$ "as usually taken in MOOD papers", third order is restored: rates 3.00 in all norms on the finer meshes, for averages and point values (Table 2). The loss of Table 1 is attributed to the strict global bounds; the coefficients may be below one even for smooth data (Ex. 1, Remark 4.1). **Shown**
20. Burgers self-steepening shock: without limiting the PAMPA solution shows a spike, with strict or relaxed bound-preserving limiting it does not (Ex. 2, Fig. 2). **Shown**
21. Near-vacuum isentropic problem ($\gamma=3$, initial minima $\rho=5\times10^{-6}$, $p=1.25\times10^{-16}$): density and pressure stay positive; without limiting the third-order scheme "quickly blows up" (Ex. 4, Fig. 4). **Shown** (the blow-up is not plotted)
22. Isentropic density errors (Table 3): rates 2.85, 2.86, 2.82, 1.73 ($L^1$); 2.77, 2.82, 2.92, 2.25 ($L^2$); 2.65, 2.84, 2.99, 2.37 ($L^\infty$); the drop on the finest mesh is attributed to the local positivity correction. **Shown**
23. LeBlanc: the scheme runs to $t=6$ on 500 cells; 500/1000/5000-cell runs converge to the exact solution, whose shock the authors place at $x=8$ (Ex. 7, Figs. 7–8; see Printed slips). Double rarefaction: non-oscillatory with a near-vacuum centre (Ex. 8); Sedov: "satisfactory results, without any numerical defects" (Ex. 9). **Shown**
24. PAMPA converges to a weak solution under Lax–Wendroff-type assumptions (§2). **Stated** (from ref. [1])

# Printed slips

- p. 35, properties of the basis: the second row prints "$\ell_0(1)=0,\ \ell_1(1)=1,\ \int_0^1\ell_1\,dx=0$"; the first entry repeats $\ell_0(1)=0$ from the first row. *(Compiler check, not in the sources: the row's subject needs $\ell_1(0)=0$, which holds for the printed $\ell_1=x(3x-2)$.)*
- p. 38, proof of Prop. 3.1, first display: "$\alpha_j(u^*_{j+1}-\mathring u_{\min})\ge\eta_j\Delta\mathcal F_j\ge\alpha_j(u^*_j-\mathring u_{\max})$"; by (3.6) and the next display the $u^*_{j+1}$ should be $u^*_j$.
- p. 44, last positivity constraint: "$\mathbf u^*_{j+1/2}\cdot\boldsymbol\nu-\theta^e_{j+1/2}\frac{\Delta\vec\Phi_{j+1/2}\cdot\boldsymbol\nu}{\beta_{j+1/2}}>0$" uses the right-going $\vec\Phi_{j+1/2}$, where (3.7), (3.11) and the $\theta^e_{j+1/2}$ formula on the same page use the left-going $\overleftarrow\Phi_{j+1/2}$.
- pp. 43–44: the point-value bar states are written $\rho^*_{j\mp1/2}$, $\mathbf u^*_{j\mp1/2}$, whereas §3.2 defines them as $u^{*,L}_j$, $u^{*,R}_j$ (3.12); $u^*_{j+1/2}$ is not otherwise defined.
- p. 43, derivation of (3.19): "$\rho\frac{\nu^2}{2}-\nu m+E=e+\frac\rho2(u-\nu)^2$" writes $u$ for the velocity, which the same line calls $v$ ($m=\rho v$).
- pp. 54–55, Sedov setup: "$x_i=i\Delta x$, with $\Delta x=2/N$, $N=401$ and $-N\le i\le N$". *(Compiler check, not in the sources: these nodes span $[-2,2]$ with $2N+1$ points, which does not fit "the cell $[x_0,x_1]=[-\Delta x/2,\Delta x/2]$" (that needs $x_0=-\Delta x/2$), the "401 cells" of Fig. 10 or the plots on $[-1,1]$.)*
- p. 55, Sedov data: the point values carry $p_i=e_{\min}/(\gamma-1)$ while the cells carry $E_i=\rho_ie_{\min}$; with the paper's $p=(\gamma-1)e$ of §1 the point pressure would be $(\gamma-1)e_{\min}$. The central-cell line "$(\rho_i,\rho_iv_i,\rho_i\frac{e_{\max}}{\gamma-1})=(1,0,\frac{\rho_ie_{\max}}{\gamma-1})$" is tautological in its third component. The paper's $e$ is the internal energy per unit volume in (1.2) and per unit mass here.
- Typos: "BP-PAMAPA" and "BP PAMAPA" (p. 46, Table 1 caption), "restrict GMP" (Fig. 3 caption), "Burger's equation" (pp. 45, 48), "$u(x,t)\in\mathbb R^n$" against "$\mathbb R^p$" (p. 30); in the references "A posterior correction" ([31]), "Computationa Fluid Dynamics" ([14]), "J. von Neuman", "Peirls", "Magree" ([5]).
- Not printed: the definition of the CFL number. By §4.2, LeBlanc runs at $\gamma=1.4$ and the double rarefaction at $\gamma=5/3$.
- p. 52, Ex. 7: "It is known that at time $t=6$, the shock wave should be located at $x=8$." *(Compiler check, not in the sources: an exact Riemann solve of the printed data $(1,0,0.1(\gamma-1))$ / $(0.001,0,10^{-7}(\gamma-1))$ at $x=3$ puts the shock at $x\approx7.98$ for $\gamma=5/3$ and at $x\approx7.12$ for the $\gamma=1.4$ that §4.2 assigns to the example.)* Either the stated position or the stated $\gamma$ is a slip; the paper does not say which $\gamma$ its exact solution in Fig. 8 uses.

# Notation map

| Abgrall et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $[x_j,x_{j+1}]$, $\bar u_{j+1/2}$ | $I_i$, $\bar u_i$ | **index shift** $-\tfrac12$: source cells carry half indices, nodes integer ones |
| $u_j$ (point value at node $x_j$) | $u_{i+1/2}$ | one shared value per interface (Active Flux) |
| $\lambda=\Delta t/\Delta x$ | $\Delta t/\Delta x$ | **collision** with the eigenvalues $\lambda_l$ |
| $\mathcal F^{LO}_j$, $\alpha_j$ | $\hat f^{\mathrm{LO}}_{i+1/2}$, $a_{i+1/2}$ (local) | LLF flux of neighbouring averages |
| $\beta_{j\mp1/2}$ | $a^{\mathrm L}_{i+1/2}$, $a^{\mathrm R}_{i+1/2}$ (local) | **collision** with the smoothness indicators $\beta_k$ |
| $\vec\Phi_{j-1/2}$, $\overleftarrow\Phi_{j+1/2}$ | $\vec\Phi_i$, $\overleftarrow\Phi_{i+1}$ (local) | residuals sent to the node; superscripts LO, HO |
| $a_j=f'(u_j)$, $a_j^\pm$; $J^\pm=R\Lambda^\pm R^{-1}$ | $a^\pm$; $R\Lambda^\pm L$ | upwind split at the node |
| $\ell_0,\ell_{1/2},\ell_1$ | basis of the cell parabola (local) | not the Lagrange basis $\ell_j$ of DGSEM pages |
| $\Delta\mathcal F_j$, $\Delta\vec\Phi$, $\Delta\overleftarrow\Phi$ | $\Delta\hat f_{i+1/2}$, … (local) | high minus low order |
| $\eta_j$ | $\mathsf e_{i+1/2}$ (local) | **collision** with the entropy $\eta$ |
| $\theta_{j\mp1/2}$ | $\mathsf t^{\mathrm L}_{i+1/2}$, $\mathsf t^{\mathrm R}_{i+1/2}$ (local) | **collision** with the Zhang–Shu factor $\theta$ |
| $u^*_j$; $u^{*,L}_j$, $u^{*,R}_j$ | $u^*_{i+1/2}$; bar states at the node (local) | "first-order finite volume Riemann intermediate states" |
| $\tilde u^L$, $\tilde u^R$ | $\tilde u^{\mathrm L}$, $\tilde u^{\mathrm R}$ (local) | **collision** with the normalized variables $\tilde u_i$ |
| $\mathring u_{\min}$, $\mathring u_{\max}$; $u^{\min}_{j+1/2}$, $u^{\max}_{j+1/2}$ | global and local bounds (local) | |
| $\xi_L$, $\xi_R$, $\zeta'$ | smooth-extrema factors, derivatives of the cell parabola (local) | **collision** of $\zeta$ with the characteristic variables |
| $\mathcal D$, $\mathcal D_\nu$ | $G$ and its GQL form | |
| $\nu$, $\boldsymbol\nu=(\nu^2/2,-\nu,1)^\top$ | $v_*$, $n(v_*)$ | **collision** of $\nu$ with the CFL number |
| $e$ (internal energy per volume, $p=(\gamma-1)e$) | $\rho e$ | **collision**: registry $e$ is specific |
| $u$ in (3.19), $v$ | $v$ | velocity |
| $Q,P$; $A,B,C$; $\rho(C)$ | $Q,P$; $\mathsf A,\mathsf B,\mathsf C$ (local) | **collision** of $\rho(C)$ with the density |
| GMP, LMP | global, local maximum principle | |

# Reference list

The paper prints 35 references, numbered [1]–[35] in alphabetical order. The list is
merged complete into the [bibliography](/bibliography.md), with `citedby` including
`abgrall-2026`. Ref. [24] (Liu, SIAM J. Sci. Comput., "in press", arXiv:2409.12606) is
printed in pre-publication form and kept as its own entry. Refs. [13] and [14] are two
AIAA 2011 papers by Eyman & Roe, suffixed in printed order. Ref. [33] is Wu & Shu's
geometric-quasilinearization paper, the ingested source
[Wu & Shu (2023)](/sources/wu-2023-b.md). Several printed keys belong to other works
in the bundle (refs. [1], [2], [3] of Abgrall and refs. [24], [25] of Liu) and were
disambiguated by venue. No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23), cited further in chunk 10 (2026-10-23). This source is cited on:

* [Active Flux](/methods/active-flux.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Buckley–Leverett problem](/benchmarks/buckley-leverett-problem.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Cell-average to point-value conversion](/operators/cell-average-point-value-conversion.md)
* [Convex limiting and invariant-domain-preserving schemes](/methods/convex-limiting.md)
* [Double rarefaction (123) problem](/benchmarks/double-rarefaction-problem.md)
* [Geometric quasilinearization (GQL)](/methods/geometric-quasilinearization.md)
* [Jiang–Shu composite-wave advection](/benchmarks/jiang-shu-composite-advection.md)
* [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md)
* [PAMPA scheme](/methods/pampa-scheme.md)
* [Sedov blast wave](/benchmarks/sedov-blast-wave.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
