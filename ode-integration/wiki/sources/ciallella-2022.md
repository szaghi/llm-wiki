---
type: Source
title: "Ciallella et al. (2022) — An arbitrary high order and positivity preserving method for the shallow water equations"
description: "Applies modified Patankar deferred correction to a PDE for the first time: the water-height update of a fifth-order well-balanced WENO finite-volume shallow-water scheme is rewritten as a conservative production–destruction system, giving unconditional positivity of the height for one Jacobi-solved sparse linear system per correction."
resource: "doi:10.1016/j.compfluid.2022.105630"
source_kind: paper
authors: [Ciallella M., Micalizzi L., Öffner P., Torlo D.]
year: 2022
venue: "Comput. Fluids 247:105630"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Computers_amp_Fluids_Ciallella_An_arbitrary_high_order_and_positivity_preserving_method_for.pdf"
tags: [positivity, structure-preserving, method-of-lines, implicit-stage-solvers, cfd]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper builds a fifth-order, well-balanced, positivity-preserving finite-volume scheme for the 2D shallow water equations with bathymetry; the construction extends to arbitrary order. Space is discretized by dimension-by-dimension WENO5 with four-point Gauss–Legendre quadrature on each face, a Rusanov flux, the Perthame–Shu / Zhang–Shu positivity limiter, and well-balancing by subtraction of the steady-state residual. These generate the semi-discrete system.

The time-integration contribution is the first application of modified Patankar [deferred correction](/methods/deferred-correction.md) (mPDeC) to a PDE. The finite-volume update of the water height is rewritten as a conservative [production–destruction system](/definitions/production-destruction-system.md). The positive and negative parts of each face flux become production and destruction terms between neighbouring cells. The height is advanced by mPDeC, one of the [modified Patankar methods](/methods/modified-patankar-methods.md), and the momenta by explicit DeC with the same subnodes and corrections. Each correction at each subnode needs one sparse linear system with at most 5 nonzeros per row. It is solved by Jacobi iteration, which keeps the iterates positive where Krylov methods need not (see [implicit-stage solvers](/methods/implicit-stage-solvers.md)).

The height is then unconditionally positive, so [positivity](/properties/positivity-preservation.md) imposes no step restriction. The route through explicit [SSP Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md) with the limiter needs $\nu\le1/12$ for WENO5 and stops at order four. The step is still limited by the explicit DeC used for the momenta, whose stability with the Patankar part is assumed, not analysed. The tests are a $C^\infty$ travelling vortex (a shallow-water analogue of the [isentropic vortex](/benchmarks/isentropic-vortex.md)), lakes at rest (smooth, wet–dry, almost dry, perturbed), circular dry and wet dam breaks, and a wave over a dry island. They show fifth-order convergence, well-balancing to machine precision, and positivity up to $\nu=1.5$ in a dry dam break. The accuracy matches DeC5 and SSPRK(6,4), at an overhead of about 10–18 % over explicit DeC5 with 10–20 Jacobi iterations (worst case 40).

# Version read

arXiv:2110.13509v3 [math.NA], 15 Nov 2022 (dated 16 Nov 2022 under the authors), not the version of record; 35 pages, all read, pp. 9–11 also checked visually. The file prints no journal data or DOI; page 1 matches Crossref, no identity problem. Numbering cited here is that of the arXiv v3.

# Key claims

Notation: $h$ is the step (source $\Delta t$); the water height, the source's $h$, is written $h_{\mathrm w}$ here. The semi-discrete system is $y'=f(y)$, $y\in\mathbb R^d$ (source $S$ unknowns, indices $\alpha,\beta$ written $i,j$). DeC uses $\mathsf M$ subintervals, $K$ corrections, subnode values $Y^{(k)}_m$ and weights $\omega_{mr}$ (source $M$, $y^{m,(k)}$, $\theta^m_r$). $\nu$ is the Courant number (source CFL), and $\nu_{\mathrm{FE}}$ the forward-Euler positivity bound of the limiter.

1. mPDeC applied to the water-height equation of a WENO finite-volume semi-discretization makes the fully discrete scheme unconditionally positivity preserving for $h_{\mathrm w}$, for every $h>0$; positivity is inherited from the mPDeC theory of [46], recalled, not re-proved. (Abstract; §4; Conclusion 5.2) **Stated**
2. This is the first application of mPDeC to a PDE; earlier (modified) Patankar methods in fluid codes [30, 31, 40] are Runge–Kutta based, of order at most three, and were used mostly for source, multicomponent or post-processing terms. (§1, footnote 1; §4) **Stated**
3. The finite-volume update of $h_{\mathrm w}$ is a conservative, positive PDS when $p_{ij}$ and $d_{ij}$ are the positive and negative parts of the face fluxes divided by the cell size (Eq. (33)); the matrices are $d\times d$, $d=N_xN_y$, with at most 4 nonzeros per row; the source term vanishes on the height. (§5.1) **Derived**
4. Only small changes of a classical WENO code are needed (subtract the steady flux; define $p_{ij}$, $d_{ij}$), and the construction applies to other high-order finite-volume or finite-difference discretizations. (Remark 5.3; Algorithm 4; §5) **Stated**
5. DeC order: with $\mathsf M$ equispaced subintervals $\mathcal L^2$ has order $\mathsf M+1$, with Gauss–Lobatto subnodes order $2\mathsf M$, and $K=p$ corrections give order $p$; for mPDeC "classically $\mathsf M=p-1$ equispaced subintervals and $K=p$ corrections". (§4.1, after Eqs. (20), (24); §4.3) **Stated**
6. The simulations use $\mathsf M=3$ Gauss–Lobatto subintervals (sixth-order $\mathcal L^2$) and $K=5$ corrections, a fifth-order scheme matching WENO5. (Remark 4.3) **Stated**
7. Each mPDeC correction at each subnode solves $\mathbb M(Y^{(k-1)}_m)Y^{(k)}_m=y_n$ with the matrix (30), at most 5 nonzeros per row. (Remark 4.4, §5.1) **Derived**
8. Jacobi iteration converges on (30) ("it is provable [46, 11]") and keeps every iterate positive; Krylov methods may converge faster but in general do not preserve positivity. (§5.1, Remark 5.1) **Stated**
9. Jacobi at machine-precision tolerance takes "usually 10–20 iterations …, in the worst cases 40", nearly independent of the mesh; the count is driven by $\nu$, since $h\,d_{ij}/y$ and $h\,p_{ij}/y$ scale linearly with it. (§5.1; §6.1; Figs. 6c, 15) **Shown**
10. mPDeC raises the cost "of around 18 %" over DeC at the same $\nu$ (§§5.1, 6.6, 7); the Jacobi solver is "around 10 %" of the total (Remark 5.1); for the vortex on fine meshes the mPDeC5/DeC5 time ratio is "close to 1.1" (§6.1, Fig. 6a). No hardware stated; code not optimized. **Shown**
11. The positivity limiter with forward Euler needs $\nu\le\nu_{\mathrm{FE}}=w_1^{\mathrm{Lobatto}}$, the first Gauss–Lobatto weight of the matching spatial accuracy: $1/12$ for WENO5; SSPRK(5,4) allows about $1.508\,\nu_{\mathrm{FE}}$. (Remark 3.1) **Stated**
12. Explicit SSP Runge–Kutta methods are at most fourth order, so a fifth-order scheme such as DeC5 has no nonnegativity guarantee under any $\nu$; explicit (implicit) SSP Runge–Kutta methods exist only up to order four (six) "for general cases" [27]. (Remarks 3.1, 5.4; §7) **Stated**
13. Arbitrary-order DeC cannot be recast as a convex combination of explicit Euler steps, so explicit DeC with the limiter has no positivity proof even under the strict $\nu$ bound. (§6.6) **Stated**
14. The step restriction of the combined scheme comes only from the explicit DeC of the momenta ($\nu$ of order 1 is used); its stability region is "simply assumed" to be that of explicit DeC, without analysis. (Remark 5.5, §7) **Stated**
15. Combining mPDeC for the height with DeC for the momenta loses no accuracy if both are consistent to the same order; a Taylor expansion of the Patankar weights suffices, "as done in [46]". (Remark 5.5) **Derived** (sketched)
16. Unsteady vortex: DeC5 and mPDeC5 with WENO5 both converge at fifth order in $L^1$ for $h_{\mathrm w}$ and the momenta on meshes $25^2$ to $600^2$, $\nu=0.7$; error against CPU time is almost the same for both, and the cost depends strongly on $\nu$. (§6.1, Figs. 5, 6b) **Shown**
17. Lake at rest (smooth bathymetry): well-balanced runs give "exactly zero" error for DeC5 and mPDeC5; without well-balancing both converge at fifth order, meshes $4^2$ to $128^2$, $\nu=0.9$. (§6.2, Fig. 8) **Shown**
18. Wet–dry lake at rest: DeC5 and SSPRK(6,4) are not positive even with the limiter and need positivity forced at every flux and variable conversion, mPDeC5 does not; all converge at order 2 (solution not $C^1$); mPDeC5 runs at $\nu=1$ and $1.5$, while SSPRK(6,4) at $\nu=1$ "can have problems and might have exploding velocities and water heights". (§6.3, Fig. 9) **Shown**
19. Almost-dry lake at rest: mPDeC5 keeps an order close to five down to errors of about $5\cdot10^{-7}$ (Table 1: height error $5.896\cdot10^{-7}$, order 4.804 at $N_x=1600$), while SSPRK(6,4) plateaus near $10^{-6}$ (Table 2: $9.062\cdot10^{-7}$, order 3.127) because of the extra positivity fixes. (§6.4) **Shown**
20. Perturbed lake at rest: without well-balancing the error from the bathymetry and the dry island swamps the perturbation; with it the perturbation is captured cleanly. (§6.5, Fig. 11) **Shown**
21. Circular dry dam break ($h_{\mathrm w}=2.5$ inside, $10^{-6}$ outside): mPDeC5 runs with $\nu$ up to 1.5 while keeping positivity, at 18 % more CPU time than DeC5. (§6.6) **Shown**
22. Wave over a dry island: repeated wetting and drying without negative heights at $\nu=0.9$ on $400\times120$ cells, "something that we cannot ensure for the DeC5 case"; the Jacobi count grows with $\nu$ from 0.1 to 1.5. (§6.8, Figs. 15–16) **Shown**
23. The extra Jacobi cost is "negligible with respect the cost of decreasing the CFL number of factor of 12" required by the limiter for explicit WENO5. (Remark 5.4) **Stated**
24. WENO5 with four-point Gauss quadrature on the faces has "not been fully described in literature"; its coefficients are given in App. B. (§3.1.1; App. B, Eqs. (53)–(62)) **Derived**
25. The overdetermined system (52) for the WENO linear weights (5 equations, 3 unknowns) has an exact solution. (App. A) **Derived**

*(Compiler checks, not in the sources.)* The mPDeC matrix (30) has diagonal $\ge1$ and nonpositive off-diagonal entries, which is why Jacobi from a positive start stays positive. "Unconditionally positive" covers the height only and inherits from [46]; the limiter is still applied and the scheme is still CFL-limited. The regularized division (32) used near dry states changes the scheme, and the positivity and conservation proofs of [46] assume exact division. The claim that high-order DeC is not a convex combination of Euler steps is not reconciled with Liu, Shu & Zhang [36], cited in §4.1, on SSP deferred correction. Patankar-type stability issues are acknowledged only through refs [32, 61].

# Printed slips

- Eq. (44): "$\rho^2=9((x+2)^2+(x-0.5)^2)$"; the second term is almost certainly $(y-0.5)^2$.
- Eq. (25): index range "$\forall\alpha=1,\dots,I$", where the dimension is $S$ elsewhere.
- §4.1, p. 9: "$\mathcal L^{1,m}(\underline{\boldsymbol y}^{(k)})=\mathcal L^{1,m}(\underline{\boldsymbol y}^{(k-1)})-\mathcal L^{2,m}(\underline{\boldsymbol y}^{(k)})$", inconsistent with Eq. (24), which evaluates $\mathcal L^2$ at iterate $k-1$.
- §4.3: "sketched in Algorithm (24)"; (24) is an equation number.
- Eq. (13): the face flux carries a factor $1/\Delta y$ that is spurious if the weights $w_\theta\in[0,1]$ are normalized.
- Eq. (16): derivative printed $\frac{d^k}{dx^k}$ inside an integral in $\xi$.
- §6.6: "less than $\frac1{12}\mathrm{CFL_{SSPRK}}$" inverts the relation stated in Remark 3.1; §7: "lowered to 1/6 or 1/12" without saying when 1/6 applies; §6.1: "guaranteed to run at any $\mathrm{CFL_{FE}}<1$" mixes the limiter bound with the scheme's Courant number.
- §6: "For all the simulations … periodic boundary conditions", implausible for the dam breaks and the island.
- Overhead printed as "around 18 %" (§§5.1, 6.6, 7) and "about 10 %" (§6.1, Remark 5.1), for different tests.
- Typos: "They hypothesis" (Remark 4.5), "correspoding" (§3.1.1), "recontruction" (App. B).

# Notation map

| Ciallella et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$ | $h$ | |
| $h$ | $h_{\mathrm w}$ (page-local) | **water height; collides with the registry step $h$** |
| $u$, $v$, $b$, $\eta=h+b$, $g$ | kept | velocities, bathymetry, free surface, gravity; **$\eta$ is not the registry entropy** |
| $y'=f(y)$, $y\in\mathbb R^S$ | $y'=f(y)$, $y\in\mathbb R^d$ | **$S$ also names the source term $\mathbf S$** |
| $\alpha$, $\beta$ (component indices) | $i$, $j$ | **not Shu–Osher or multistep coefficients** |
| $p_{\alpha,\beta}$, $d_{\alpha,\beta}$ | $p_{ij}$, $d_{ij}$ | conservative iff $p_{ij}=d_{ji}$ |
| $t^n$, $y^n$ | $t_n$, $y_n$ | |
| $M$, $t^m$, $m$ | $\mathsf M$, $t_{n,m}$, $m$ | subintervals and subnodes |
| $y^{m,(k)}$, $\underline{\boldsymbol y}^{(k)}$ | $Y^{(k)}_m$, $\mathbf Y^{(k)}$ | |
| $K$, $(k)$ | $K$, $k$ | corrections |
| $\theta^m_r$ | $\omega_{mr}$ | DeC weights on the unit interval, possibly negative |
| $\beta^m=(t^m-t^0)/(t^M-t^0)$ | $c_m$ | forward-Euler fraction in $\mathcal L^1$ |
| $\mathcal L^1$, $\mathcal L^2$ | kept | low- and high-order DeC operators |
| $y^{m,(k-1)}_\beta$ in the Patankar weight | $\varpi_j=Y^{(k-1)}_{m,j}$ | Patankar weight denominator: previous correction at the same subnode |
| $\gamma(\alpha,\beta,\theta)$ | $\varsigma(i,j)$ (page-local) | index selector by the sign of the weight, as on [modified Patankar methods](/methods/modified-patankar-methods.md); **renamed: the registry $\gamma$ is the tree density** |
| $\mathbb M(y^{m,(k-1)})$ | kept, page-local | **mPDeC system matrix, not the registry mass matrix $M$** |
| CFL, $\mathrm{CFL_{FE}}$ | $\nu$, $\nu_{\mathrm{FE}}$ | **$\nu_{\mathrm{FE}}$ is a Courant bound, not the SSP coefficient $\mathcal C$**; $\nu_{\mathrm{SSPRK(5,4)}}\approx1.508\,\nu_{\mathrm{FE}}$ |
| $\varepsilon$ | kept, page-local | minimum water height and division tolerance ($10^{-6}$ or $10^{-30}$); **not the registry stiffness parameter** |
| $d_m$, $\omega_m$, $\beta_m$, $\epsilon$ | kept, page-local | WENO linear and nonlinear weights, smoothness indicators; **$d_m$ collides with $d_{ij}$, $\omega_m$ with $\omega_{mr}$** |
| $p$, $r$ (WENO) | kept, page-local | WENO order $p=2r-1$; $p$ is also the time order |

# Reference list

67 printed references, numbered [1]–[67]. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` ciallella-2022. [29] is the ingested source [Han Veiga et al. (2021)](/sources/hanveiga-2021.md). [61] is the arXiv preprint of [Torlo et al. (2022)](/sources/torlo-2022.md), kept as its own entry (torlo-2021-b), as are the other arXiv preprints [3], [5], [32] and [53] (abgrall-2021, abgrall-2019-b, izgin-2022-b, ricchiuto-2021); [32] is distinct from its published version izgin-2022 (ESAIM: M2AN). [18] (ciallella-2021-b) and [43] are code repositories, and [45] is a habilitation thesis. [63] prints the author of [29] as "M. H. Veiga" (keyed veiga-2021 by that spelling). [43] and [44] spell the same author "Núñez-de la Rosa" and "Núnez-De La Rosa". [4], [31], [33] and [34] print the online-first form, pages without volume, and are merged into the entries abgrall-2023, huang-2019-c and kopecz-2018, which carry the published volumes, and kopecz-2019-b, which has none; [36] (Liu, Shu & Zhang 2008) prints no volume. No printed duplicates; no unparseable item.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Deferred correction (DeC)](/methods/deferred-correction.md)
* [Invariant-domain preserving high-order time stepping (explicit and IMEX)](/methods/invariant-domain-preserving-time-stepping.md)
* [Modified Patankar methods (MPRK, MPDeC, MP linear multistep, Patankar predictor–corrector)](/methods/modified-patankar-methods.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Production–destruction systems](/definitions/production-destruction-system.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
