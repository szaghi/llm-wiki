---
type: Source
title: "Pazner (2021) — Sparse invariant domain preserving discontinuous Galerkin methods with subcell convex limiting"
description: "Invariant-domain-preserving nodal DGSEM: a sparsified low-order operator with corrected metric terms and Guermond–Popov graph viscosity gives a p-independent first-order IDP scheme, blended with the high-order DG target by element-wise or dimension-by-dimension subcell convex limiting, with a modal smoothness indicator that relaxes the bounds."
resource: "doi:10.1016/j.cma.2021.113876"
source_kind: paper
authors: [Pazner W.]
year: 2021
venue: "Comput. Methods Appl. Mech. Engrg. 382:113876"
local_file: "/home/stefano/papers/mosaic/weno-teno/2021_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Pazner_Sparse_invariant_domain_preserving_discontinuous_Galerkin_me.pdf"
tags: [dg, limiting, bound-preserving, positivity]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

The paper makes the nodal Gauss–Lobatto [DGSEM](/methods/dgsem.md) (the strong form
on tensor-product elements, the high-order target) invariant domain preserving through
a flux-corrected-transport blend with a low-order scheme, i.e. a form of
[convex limiting](/methods/convex-limiting.md) with the goal of
[bound preservation](/properties/bound-preservation.md) in every convex invariant set
$G$. A Guermond–Popov graph-viscosity scheme built on the dense DG operator couples
each node to $O(N)$ others, and its viscosity grows with $N$. The paper replaces the
weighted differentiation matrix $Q=MD$ of the
[summation-by-parts operator](/operators/summation-by-parts-operator.md) by the
tridiagonal $\widehat Q$ of piecewise-linear hat functions on the Gauss–Lobatto subgrid
(entries $\pm\tfrac12$), which keeps both conservation and the SBP column sums. The
sparse operator breaks the discrete metric identities, so the metric terms are perturbed
by $O(h)$ (a minimum-norm SVD solve) to restore
[free-stream preservation](/properties/free-stream-preservation.md). The local
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md) interface flux merges with the graph
viscosity, and forward Euler becomes a convex combination of bar states. Under a CFL
condition the low-order scheme is IDP, and [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)
extends this in time.

The antidiffusive residuals sum to zero along every line of nodes. They can therefore be
written as differences of subcell-face fluxes, which are limited face by face, a
dimension-by-dimension relative of
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md). This is
conservative and, with $\gamma=2d$, IDP, with no optimisation problem in several
dimensions. For Euler, density is limited by Zalesak's limiter and specific entropy by
a convex line search. A Persson–Peraire modal-decay
[indicator](/definitions/troubled-cell-indicator.md) relaxes local bounds to global ones
in smooth cells. With it the design order is recovered for $N\ge3$; without it the
local maximum principle limits the scheme to first order, as for
[TVD](/definitions/total-variation-diminishing.md) schemes at extrema. Tests:
advection, [solid-body rotation](/benchmarks/solid-body-rotation.md),
[Buckley–Leverett](/benchmarks/buckley-leverett-problem.md),
[2D Burgers](/benchmarks/burgers-equation-tests.md),
[Sod](/benchmarks/sod-and-lax-shock-tubes.md),
[Shu–Osher](/benchmarks/shu-osher-problem.md),
[configuration 12](/benchmarks/two-dimensional-riemann-problems.md) and
[double Mach reflection](/benchmarks/double-mach-reflection.md). At fixed degrees of
freedom, higher $N$ gives better results.

# Version read

arXiv:2004.08503v1 [math.NA], 18 Apr 2020 (LLNL-JRNL-808645), a SIAM-style preprint,
not the CMAME version of record, although the archive file is named after the journal
article. 27 pages, all read; text extraction clean, pp. 9–10 (Eqs. (36)–(47)) checked
visually. Title and author match Crossref. The numbering differs from the published
version: [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) cite the sparsified
matrix as Pazner's Eq. (34) and the conservation condition $\sum_j\hat c_{ij}=0$ as
Eq. (35); in arXiv v1 they are Eq. (23) and Prop. 5. All numbers on this page are those
of arXiv v1.

# Key claims

Registry notation (see the notation map): the source's degree $p$ is $N$, its invariant
set $A$ is $G$, its $\lambda_{\max}$ is $a$, its weighted differentiation matrix
$D_{1D}$ is $Q$, its sparse $\widehat D_{1D}$ is $\widehat Q$. The FCT factor $\alpha_i$
keeps the source's convention ($1$ = high order). The metric matrix $GJ^{-1}$ of claims 5–6 is kept as printed (registry $Ja^{(d)}$); its $G$ is not the admissible set.

1. A graph-viscosity IDP method on the full DG operator degrades severely as $N$ grows at fixed degrees of freedom, because each node couples to $O(N)$ others and each connection adds viscosity; the sparsified method does not ($N=3,7,15,31$, 128 DOFs, $\sin(\pi x)$ advected to $t=2$) (§3, §3.4, Fig. 1). **Shown**
2. $\widehat Q$ (Eq. (23)) satisfies the zero row sums (P1) and the SBP column sums (P2) (§3). **Stated** ("easy to see"). *(compiler check, not in the sources: with rows $(-\tfrac12,\tfrac12,0,\dots)$, $(\dots,-\tfrac12,0,\tfrac12,\dots)$ and $(\dots,0,-\tfrac12,\tfrac12)$, $\widehat Q\mathbf 1=0$ and $\widehat Q+\widehat Q^\top=B$, so $\widehat Q$ is itself an SBP operator.)*
3. The DGSEM $Q$ satisfies (P1) $\sum_jQ_{ij}=0$, from $\sum_j\ell_j\equiv1$, and (P2) column sums $-1$ at $j=0$, $+1$ at $j=N$, $0$ otherwise, from the exactness of Gauss–Lobatto quadrature for degree $2N-1$ (Prop. 1, Eq. (8)). **Stated**
4. The discrete weak form (14) and strong form (15) are both conservative (Prop. 2, Eqs. (16)–(21)). **Proved**
5. The strong form preserves constants if the discrete metric identity $\sum_iQ_{i,R}(GJ^{-1})_{ij}=0$ holds (Eq. (22)); the weak form in general does not (curved meshes), so the strong form is the high-order target (Prop. 3, §2.4.2). **Proved**
6. With the sparse operator the metric identities fail; corrected metrics $GJ^{-1}+C$, $C$ the minimum-norm solution of the underdetermined system (27), restore them. The system is solvable because its right-hand side sums to zero by (P1), SBP (28) and (22), and the perturbation is $O(h)$ entrywise (§3.1, Eqs. (25)–(28)). **Derived**
7. The low-order scheme (29) is conservative and constant-preserving (Prop. 4). **Proved**
8. The LLF interface term merges with the graph viscosity into the compact graph form (35), with $\sum_{j\in N(i)}\hat c_{ij}=0$ and a zero-sum graph viscosity (§3.1, Eqs. (30)–(35), Prop. 5). **Derived**
9. The bar states $\breve u_{ij}^{n+1}=\tfrac12(u_i^n+u_j^n)+\frac{\hat c_{ij}}{2\hat d_{ij}}\cdot(f_j^n-f_i^n)$ (38) lie in every convex invariant set containing $u_i^n,u_j^n$ (Prop. 6; proof deferred to Guermond, Popov & Tomas). **Stated**
10. Under the CFL condition (40) the forward-Euler low-order update (39) is a convex combination of bar states and stays in every convex invariant set; SSP Runge–Kutta extends this to high order in time (Prop. 7). **Proved** (see Printed slips for the sign of (40))
11. For variable-velocity advection $\partial_tu+\nabla\cdot(v(x)u)=0$, the bar states (38) need not preserve constants (Prop. 6 "may fail to hold"); modified bar states (42) and viscosity (43) are bound preserving provided the metric correction enforces the discrete divergence-free condition $\sum_j\hat c_{ij}\cdot v_j=0$ (§3.3). **Derived** (the correction procedure is not given)
12. The antidiffusive residuals $r^H_i-r^L_i$ sum to zero over each element (Prop. 8) and along each line of nodes in each direction (Prop. 9, Kronecker structure). **Proved**
13. Subcell limiting (56) with face coefficients $\alpha_{m,k}=\min\{\tilde\alpha_{i_1},\tilde\alpha_{i_2}\}$ is conservative (Prop. 10). **Proved**
14. Subcell convex limiting with $\gamma=2d$ in (60) preserves all prescribed convex invariant sets $G_\ell$ (Prop. 11, convex combination (62)). **Proved**
15. Element-wise limiting does not improve the solution beyond $N=1$ at fixed DOFs (two square waves, 320 DOFs, $N=0,1,3,7$); subcell limiting improves with $N$ (§4.1.4, Fig. 3). **Shown**
16. On solid-body rotation ($25\times25$ elements, $N=3$, half the CFL limit) subcell limiting is less diffusive than element-wise limiting (§4.1.4, Fig. 4). **Shown**
17. For Euler, $G(r)=\{\rho>0,\ e>0,\ s\ge r\}$ is a convex invariant set and an invariant domain of Lax–Friedrichs; the limiter enforces density bounds (Zalesak) and a local minimum principle on specific entropy (convex limiting with a Newton line search, using the convexity of $s$), which also keeps $e>0$ (§4.3, Eqs. (65)–(67)). **Stated** (invariant set cited) / **Derived**
18. The smoothness indicator greatly reduces peak clipping: 4 elements with $N=7$ for a smooth profile, no noticeable oscillation for a discontinuous one ($N=3$, 80 elements) (§4.4, Fig. 5). **Shown**
19. On solid-body rotation ($25\times25$, $N=3$, subcell limiting) the indicator lowers the $L^1$ error by "about 25%", $2.6\times10^{-2}\to1.9\times10^{-2}$, and the range goes from $[0,0.95]$ to $[0,1]$ (§4.4, Fig. 6). **Shown**
20. Convergence (advection of $\sin(2\pi x)$ to $t=1$, eighth-order RK, 8–64 elements): with the indicator the rates are $N+1$ for $N=3,4,5$ (4.00, 5.00, 5.86 at 64 elements); without it about first order (1.00, 1.04, 1.29); $N=0,1$ are unaffected by the indicator (§5.1, Table 1). **Shown**
21. Without the indicator the strictly enforced local maximum principle limits convergence to first order, "consistent with other results reported in the literature" (§5.1). **Shown** / **Stated**
22. TVD schemes are provably at most first-order accurate at smooth extrema (§4.4). **Stated** (cited)
23. Sod (256 DOFs, $N=0,1,3,7$, $t=0.18$): higher $N$ on a coarser mesh resolves the discontinuities, especially the contact, somewhat better; $N=3$ and $N=7$ are largely indistinguishable (§5.2.1, Fig. 7). **Shown**
24. Shu–Osher (512 DOFs, $t=1.8$): the shock is resolved well for every $N$, the smooth structures better at higher $N$; some peak clipping remains on the post-shock oscillations (§5.2.2, Fig. 8). **Shown**
25. Solid-body rotation ($64\times64$, $N=3$, $t=1$): unlimited DG range $[-0.21,1.16]$, $L^1$ error $1.0\times10^{-2}$; low-order IDP $[0,0.66]$, $8.5\times10^{-2}$; subcell FCT $[0,1]$, $1.1\times10^{-2}$, i.e. accuracy comparable to unlimited DG (§5.4, Fig. 10). **Shown**
26. 2D Burgers Riemann problem ($120^2$ DOFs, $N=2,5,11$ on $40^2,20^2,10^2$ elements): well resolved on the coarse mesh, with discontinuities captured even when not aligned with element boundaries (§5.5, Fig. 11). **Shown**
27. Riemann configuration 12 ($N=1$ on $128^2$ against $N=3$ on $64^2$, same DOFs, $t=0.25$): $N=3$ gives sharper interfaces and more small-scale features (§5.6, Fig. 12). **Shown**
28. Double Mach reflection ($2400\times600$ elements, $N=3$, $t=0.275$): the Kelvin–Helmholtz roll-ups near the triple point indicate low dissipation (§5.7, Fig. 13). **Shown**

# Printed slips

- CFL condition (40), "$\Delta t\le\min_i\frac{m_i}{2\hat d_{ii}}$", with $\hat d_{ii}=-\sum_{j\ne i}\hat d_{ij}\le0$ as defined, gives a negative bound; nonnegativity of the coefficient of $u_i^n$ in (39) requires $\Delta t\le m_i/(2\lvert\hat d_{ii}\rvert)$. The same expression recurs in §5 ("$\Delta t=\frac12\min_i\frac{m_i}{2\hat d_{ii}}$").
- Eq. (45) prints the viscosity term as "$-\sum_{j\in E(i)}d_{ij}(u_j-u_i)$" on the right-hand side, the anti-diffusive sign; Eq. (36) has $+\sum_j\hat d_{ij}(u_j^n-u_i^n)$ (checked visually, p. 10).
- Eq. (60): "for all $1\le d\le k$"; should be $1\le k\le d$.
- Prop. 11: "the flux-corrected nodal values $u_i^{n+1}$ $u$ satisfy" (stray "u"); §4.2.2 cites "Proposition (10)" with equation parentheses.
- §3.1: "the discretization (24) is modified to render the resulting method IDP"; the corrected low-order scheme is (29).
- §5.1: "we observe the expected asymptotic rates for all cases except $p=1$", but Table 1 with the indicator gives $p=2$ rates 1.18, 1.36, 1.82 and $p=0$ rates 0.41, 0.63, 0.80: only $p\ge3$ reach $p+1$.
- §5.3, Buckley–Leverett: data printed $u_0=-3$ for $x<0$ and $3$ for $x\ge0$, against Fig. 9, whose $u$-axis spans $[0,1]$, the physical saturation range; the domain is not stated.
- §4.3: $A(r)$ is stated "for any $r\ge0$"; a lower bound on $s=\log(e^{1/(\gamma-1)}\rho^{-1})$ can be negative, and the restriction is not explained.
- Typos: "Caetesian grids" (§5.6), "bounds perserving" (§3.3), "conversation laws" (§2), "visocity" (§1), "would also for the introduction of oscillations" (§4.4, missing word).
- References: [19] and [20] print single-page ranges "531–531" and "119–119"; [50] prints "and et al."; [2] and [26] print "R. Lhner" (Löhner).

# Notation map

| Pazner (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$, $Q_p$ | $N$, $\mathbb Q^N$ | polynomial degree; **$p$ is also the pressure in §§4.3, 5** |
| $F(u)$, $n_c$, $d$ | $f^{(d)}(u)$, $m$, $d$ | flux, number of components, dimension |
| $u_i$ | $u_i$ | nodal value at a Gauss–Lobatto node; agrees |
| $\xi_i$, $w_i$, $\phi_i$ | $\xi_j$, $\mathsf w_j$, $\ell_j$ | nodes, weights, Lagrange basis on the reference element $[0,1]$, not $[-1,1]$ |
| $M_{1D}$ | $M$ | diagonal mass matrix |
| $D_{1D}=(w_i\phi_j'(\xi_i))$ | $Q=MD$ | **the source's $D$ is the weighted (SBP $Q$) matrix, not the registry's $D$** |
| $\widehat D_{1D}$, $\widehat D_{i,R}$ | $\widehat Q$, $\widehat Q_{i,R}$ | sparsified matrix, Eq. (23) in arXiv v1 |
| $B_{e,R}$ | $B$ | boundary matrices |
| $T_K$, $J$, $G=\mathrm{diag}(\det J)$, $GJ^{-1}$ | $J$, $Ja^{(d)}$ | metric terms; **the source's $G$ is a Jacobian matrix, the registry's $G$ the admissible set** |
| $\hat F$, $\lambda$, $\lambda_{\max}$ | $h^{\mathrm{LF}}$, $a$, $a_{\max}$ | LLF flux and wave-speed bound; $a_{\max}(u_i,u_j,n_{ij})$ page-local on [convex limiting](/methods/convex-limiting.md) |
| $A$, $A_\ell$, $A(r)$ | $G$, $G_\ell$, $G(r)$ | convex invariant sets; **$A$ is the flux Jacobian in the registry** |
| $c_{ij}$, $b_{ij}$, $\hat c_{ij}$ | kept | graph coefficients, weak-form sign ($+\hat c\cdot f$ on the right-hand side) |
| $d_{ij}$, $\hat d_{ij}$, $\hat d_{ii}$ | kept | graph viscosity; **$d$ collides with the linear weights $d_k$** |
| $E(i)$, $B(i)$, $N(i)$ | kept | in-element, face-neighbour and combined stencils; **$N(i)$ is not the degree $N$** |
| $m_i$ | kept | lumped nodal mass |
| $\bar u_{ij}^{n+1}$ | $\breve u_{ij}$ | bar states; **the registry's $\bar u$ is a cell average**, so concept pages write $\breve u$ |
| $u^H$, $u^L$, $r^H_i$, $r^L_i$, $r_{i,k}$, $r_{m,k}$ | kept | high/low-order updates, residuals, nodal and subcell-face antidiffusive fluxes; **$r$ collides with the stencil size $r$** |
| $\alpha_i$, $\tilde\alpha_i$, $\alpha_{m,k}$ | kept | FCT limiting factors, **$1$ = high order, opposite to the registry blending coefficient $\alpha$ ($0$ = DG)** |
| $\gamma=2d$ (Eq. (60)) | $\Gamma=2d$ | **collides with the ratio of specific heats $\gamma=1.4$ in the same paper** |
| $\beta(x)$ (§3.3) | $v(x)$ | advection velocity; **$\beta$ is the smoothness indicator in the registry** |
| $e$, $E$, $H$ | $e$, $E/\rho$, $H$ | **the source's $E$ is the specific total energy; $\rho E$ is the registry's $E$** |
| $s=\log(e^{1/(\gamma-1)}\rho^{-1})$ | $s=\ln(p\rho^{-\gamma})$ | *(compiler check, not in the sources: $s_{\text{Pazner}}=\frac{1}{\gamma-1}\big(s-\ln(\gamma-1)\big)$ for an ideal gas, an increasing affine map, so the two minimum principles coincide)* |
| $s_K$, $\varepsilon_K$, $s_0$, $\kappa$ | $\mathbb S_K$, $\varepsilon_K$, $\mathbb S_0$, $\Delta_{\mathbb S}$ | modal smoothness indicator and ramp ([troubled-cell indicator](/definitions/troubled-cell-indicator.md)); **$s_K$ collides with the entropy $s$, $\kappa$ with the kinetic energy** |
| $g_{\min}$, $g_{\max}$ | kept | global bounds; not the constraint functions $g_i$ |

# Reference list

54 printed references, numbered [1]–[54] in SIAM style, sorted alphabetically, all
parsed and merged complete into the [bibliography](/bibliography.md) with `citedby`
`pazner-2021`. Venue-less items: [1] MFEM (arXiv:1911.09220), [9] Franco et al. 2019,
[39] Pazner & Persson 2018. Same-author same-year pairs take suffixes in printed order
(Pazner 2018 [39]/[40], Moura 2017 [34]/[35], Kuzmin 2020 [27]/[28]). Printed oddities
are kept as printed ([19], [20] single-page ranges; [2], [26] "Lhner"; [50] "and et
al."; [29] without pages). No printed duplicates.

# Pages created or updated

Chunk 2 (2026-10-22), cited further in chunks 3–10 (2026-10-22/23). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Buckley–Leverett problem](/benchmarks/buckley-leverett-problem.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Convex limiting and invariant-domain-preserving schemes](/methods/convex-limiting.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Free-stream preservation](/properties/free-stream-preservation.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Solid-body rotation](/benchmarks/solid-body-rotation.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
