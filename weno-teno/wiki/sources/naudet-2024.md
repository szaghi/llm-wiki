---
type: Source
title: "Naudet & Zahr (2024) — A space-time high-order implicit shock tracking method for shock-dominated unsteady flows"
description: "Extends high-order implicit shock tracking (HOIST) to unsteady flows by slab-based space-time DG: space-time Riemann-solver fluxes built from the spatial ones, a simplex-only slab mesh generator, a translating slab top, time scaling, residual- and sensor-driven refinement and shock boundary conditions, tested on Burgers, shallow-water and Euler problems."
resource: "doi:10.1016/j.jcp.2024.112792"
source_kind: paper
authors: [Naudet C.J., Zahr M.J.]
year: 2024
venue: "J. Comput. Phys. 501:112792"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Naudet_A_space-time_high-order_implicit_shock_tracking_method_for_s.pdf"
tags: [shock-tracking, dg, space-time, amr, numerical-flux, unstructured-mesh]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper extends the High-Order Implicit Shock Tracking (HOIST) method of
Zahr, Persson and Huang, an optimization-based
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) method in the family of
[implicit shock tracking](/methods/implicit-shock-tracking.md), from steady to
unsteady problems. HOIST moves the mesh nodes until element faces lie on the
discontinuities, which are then represented by inter-element jumps without limiting
or [artificial viscosity](/methods/artificial-viscosity.md). A time-dependent law in
$d'$ space dimensions is rewritten as a steady law in $d'+1$ dimensions on a
space-time slab, and HOIST is applied slab by slab, without global coupling in time.

There are four contributions. (i) The space-time projected flux Jacobian is the
spatial one scaled by $\lVert n_x\rVert$ and shifted by $n_t$, with the same
eigenvectors. Space-time versions of linearized-Riemann-solver fluxes
([Roe](/methods/roe-riemann-solver.md), Vijayasundaram,
[Rusanov](/methods/lax-friedrichs-flux.md)) then follow from spatial quantities
alone. (ii) A mesh generator builds conforming, simplex-only slab meshes. The spatial
mesh is taken from the top of the previous slab and extruded into prisms. Each prism
is split into simplices by an orientation-independent rule, and curved elements are
handled through the isoparametric map. (iii) HOIST is posed over a slab and solved by
SQP. (iv) Practical additions: a translating slab top, a time scaling that keeps
slabs well shaped, [adaptive refinement](/methods/adaptive-mesh-refinement.md) driven
by the enriched residual and the Persson–Peraire
[sensor](/definitions/troubled-cell-indicator.md), and shock boundary conditions that
remove the known upstream region.

All evidence is numerical, on six problems: three
[Burgers tests](/benchmarks/burgers-equation-tests.md) (an accelerating shock leaving
the domain, shock formation and merging, a 2D curved shock), a
[shallow-water](/definitions/shallow-water-equations.md)
[dam break](/benchmarks/dam-break-problem.md) with wall reflections, the
[Sod tube](/benchmarks/sod-and-lax-shock-tubes.md) run to $t=1$ with reflecting walls,
and the [Shu–Osher problem](/benchmarks/shu-osher-problem.md) to $T=2$. The paper
measures no order of convergence. The shocks satisfy the
[Rankine–Hugoniot condition](/definitions/rankine-hugoniot-condition.md), and the
[carbuncle](/definitions/carbuncle-phenomenon.md) is cited among the shock-capturing
failures that tracking avoids.

# Version read

Version of record (Elsevier typeset; received 8 August 2023, revised 4 December
2023, accepted 21 January 2024, online 26 January 2024), 26 pages, all read. The
calligraphic symbols of pp. 3–6, 13–14 and 20–21 were checked on the page images,
because text extraction drops them. Title, authors, venue and DOI on page 1 match
Crossref. Numbering on this page is that of the version of record.

# Key claims

Registry notation, with page-local symbols: $u$ the state, $f_x(u)$ the
$m\times d'$ spatial flux, $n=(n_x,n_t)$ the space-time unit normal and
$\hat n_x=n_x/\lVert n_x\rVert$; $A_x(u,\hat n_x)=\partial(f_x(u)\hat n_x)/\partial u$
and $A_{xt}(u,n)$ the spatial and space-time projected Jacobians, with eigenvalue
matrix $\Lambda_x$ and right eigenvectors $R$; $h$ the numerical flux; $N$ the DG
degree; $N_{\mathrm{sl}}$ the number of slabs (see the Notation map).

1. Shock capturing (limiting, reconstruction, artificial viscosity) reduces "the order of accuracy of the method near discontinuities, and therefore globally, to first-order", and its accuracy "will always be limited to first-order due to the smooth approximation of discontinuous features" (§1). **Stated**
2. Implicit shock tracking within a method-of-lines time discretization "is most suitable for problems with limited shock motion and cannot handle shock-shock or shock-boundary interactions without complex mesh modifications". Space-time formulations avoid this: a moving shock is a stationary surface in space-time, and shock intersections are triple points (§1). **Stated**
3. $A_{xt}(u,n)=A_x(u,\hat n_x)\lVert n_x\rVert+n_tI_m$, hence $\Lambda_{xt}=\Lambda_x\lVert n_x\rVert+n_tI_m$ with the same eigenvectors $R$ (Eqs. 10, 12). **Derived**
4. Any linearized-Riemann-solver flux $h=\tfrac12\big(f(u^+)n+f(u^-)n\big)+\tfrac12\tilde A(u^+-u^-)$, Eq. (4) (Roe, Vijayasundaram, Rusanov), therefore has a space-time version written entirely in spatial quantities. For Roe, $\tilde A=R\,\lvert\Lambda_x\lVert n_x\rVert+n_tI_m\rvert\,R^{-1}$ at the Roe average (Eq. 15); for Rusanov, the maximum of $\lVert\Lambda_x\lVert n_x\rVert+n_tI_m\rVert_\infty$ over the two traces times $I_m$ (Eqs. 13–17, Remarks 4–5). This removes "one of the implementation burdens associated with space-time methods". **Derived**
5. On the reference slab the numerical flux becomes $\bar h(u^+,u^-,\bar n;\Theta)=\sigma_\Theta\,h\big(u^+,u^-,\sigma_\Theta^{-1}(\det\Theta)\Theta^{-\top}\bar n\big)$, $\sigma_\Theta=\lVert(\det\Theta)\Theta^{-\top}\bar n\rVert$, with $\Theta$ the deformation gradient of the domain map (Eq. 21, after earlier work of the group). **Stated**
6. The meshes are simplex-only because "element removal via edge collapse is well-defined in any dimension and key to robust shock tracking" (§3). **Stated**
7. Splitting every face of the prism and joining the face simplices to a central node gives $N_{d}^{\triangle}=dN_{d-1}^{\triangle}+2$ simplices per prism for $d>2$, with $N_2^{\triangle}=4$, hence $N_3^{\triangle}=14$ and $N_4^{\triangle}=58$. A constrained Delaunay triangulation gives $N_3^{\triangle}=11$ without a central node (Eq. 35, §3.3.1). **Derived**
8. The more expensive splittings ($N_2^{\triangle}=4$ rather than 2, $N_3^{\triangle}=14$ rather than 11) were observed to make shock fitting more robust: the split is close to a uniform refinement, so some face is always a reasonable first guess for the trajectory of a discontinuity (Remark 9). **Stated** (not quantified)
9. Splitting the straight-sided parent element and mapping through the isoparametric map and the continuous domain map gives conforming curved high-order refinements in the physical domain (§3.3, Eqs. 31–34). **Derived**
10. The translation parameter of the slab top (Eq. 37) lets the optimizer place the top boundary on a shock–boundary interaction and keep the slab structure (§4.1, Fig. 7). **Shown** (Figs. 10, 15, 16)
11. With the mesh parametrization fixed (identity) on the slab bottom, the inter-slab interpolation needs no update or linearization at each iteration. It does not interfere with tracking, because discontinuities crossing the bottom were tracked in the previous slab (§4.3). **Stated**
12. Scaling time by $t^\star<1$ (fast waves, thin slabs) or $t^\star>1$ (slow waves, tall slabs) improves the conditioning of the space-time simplices substantially (§4.4, Fig. 8). **Stated** (schematic only)
13. More slabs make tracking easier. For the accelerating Burgers shock on 192 space-time simplices with $N=2$ and geometry degree 2, and $N_{\mathrm{sl}}\in\{1,2,4,8\}$: "As more slabs are added, the residuals converge more rapidly and to deeper tolerances" (§5.1.1, Fig. 9, Remark 11). **Shown**
14. Shock boundary conditions on the same problem ($N_{\mathrm{sl}}=5$, first slab of 24 elements from 6 spatial elements) eliminate "over half of the space-time elements" (§5.1.1, Fig. 11). **Shown**
15. For Burgers shock formation and merging ($N_{\mathrm{sl}}=1$, 96 triangles with $N=2$), eight rounds of adaptive refinement give a 207-triangle mesh. It resolves the formation point and agrees well with a highly refined second-order finite-volume solution at $t=0.1$ (§5.1.2, Figs. 12–13). **Shown**
16. In 2D Burgers (32 spatial triangles, 448 tetrahedra in slab 1 with $N=2$, $N_{\mathrm{sl}}=3$), the initially straight shock curves and is captured by the curved quadratic elements (§5.1.3, Fig. 14). **Shown**
17. In the shallow-water dam break (5 slabs, 32 linear-geometry triangles with $N=2$ in slab 1), the shock and the head and tail of the rarefaction are tracked, and the second slab is stretched in time so that the wall reflections are "represented perfectly" (§5.2, Fig. 15). **Shown**
18. Sod's tube is run to $t=1$, "five times longer than the one usually associated with this problem", with walls ($N_{\mathrm{sl}}=6$, 65 simplices in slab 1). The shock, the contact and the rarefaction head and tail are all tracked from their common origin, "a generalized triple point", together with later shock–shock and shock–contact interactions and wall reflections (§5.3.1, Figs. 16–17). **Shown**
19. When two events occur at nearly but not exactly the same time, the translating top cannot track both on the coarse mesh; HOIST "chose to track the shock-contact interaction because it is the stronger feature". Freeing the time coordinates of the top nodes of slab 4 tracks both, but "causality may be violated", and no constraint enforces it yet (§5.3.1, Fig. 18). **Shown**
20. Shu–Osher with $T=2$, "larger than often seen in the literature": a first pass ($N_{\mathrm{sl}}=5$, 160 simplices in slab 1, stopped at optimality tolerance $10^{-8}$ or 200 SQP iterations) tracks only the main shock. Uniform refinement and removal of the known upstream region reduce 3184 elements to 1500, and a further pass with refinement and shock boundary conditions resolves the shock formation and the post-shock oscillations (§5.3.2, Figs. 19–20). **Shown**
21. The final Shu–Osher solution at $T=2$ has relative $L^2$ error $3.97\times10^{-4}$ against a second-order superbee finite-volume reference on "over $5\times10^4$" cells with adaptive RK4 (§5.3.2, Fig. 21). **Shown**
22. Extrude-then-split is inefficient in $d=3$ and impractical in $d=4$ ($N_3^{\triangle}=14$, $N_4^{\triangle}=58$). Parallelization and preconditioners for the linearized HOIST optimality system are needed (§6). **Stated**

The HOIST problem on a slab (Eqs. 38–40) minimizes
$\tfrac12\lVert\mathsf R(\mathbf u,\boldsymbol\phi(\mathbf y))\rVert_2^2+\kappa_{\mathrm m}^2f_{\mathrm{msh}}(\mathbf y)$
subject to $\mathsf r(\mathbf u,\boldsymbol\phi(\mathbf y))=0$, where $\mathsf r$ is
the space-time DG residual, $\mathsf R$ the residual enriched with test degree
$N+1$, $f_{\mathrm{msh}}$ a mesh-distortion penalty and $\kappa_{\mathrm m}>0$ its
weight. The refinement set (Eqs. 43–45) holds the elements with
$\lVert\mathsf R_K\rVert\ge c_1\max_K\lVert\mathsf R_K\rVert$ or
$s^{\mathrm{PP}}_K\ge c_2\max_Ks^{\mathrm{PP}}_K$, with $c_1=c_2=0.01$ and
$s^{\mathrm{PP}}_K=\log_{10}\big(\lVert\chi_h-\Pi_{N-1}\chi_h\rVert_{L^2(K)}/\lVert\chi_h\rVert_{L^2(K)}\big)$,
$\chi_h$ the first component of $u_h$ (page-local).

*(Compiler check, not in the sources.)* The left Shu–Osher state
$(\rho,v,p)=(3.857143,2.629369,10.3333)$ is the Rankine–Hugoniot post-shock state of
a Mach 3 shock running into $(1,0,1)$ with $\gamma=1.4$: density ratio
$2.4\cdot9/5.6=3.857143$, $p=1+\tfrac{2.8}{2.4}\cdot8=10.3333$,
$v=3\sqrt{1.4}\,(1-1/3.857143)=2.6294$. From Eq. (49) the accelerating Burgers shock
reaches $x=1$ at $\sqrt{1+3t}=7/4$, i.e. $t=0.6875$, inside the fifth slab when
$N_{\mathrm{sl}}=8$ and $\Delta t=0.15$.

# Printed slips

- **Eq. (47) against Eqs. (48)–(49)** *(compiler check, not in the sources)*: (47) prints $w_0=\mu_1H(-x)-\mu_2H(x)$, i.e. $-3$ for $x>0$. At $t=0$, (48) gives $w=\mu_2(x-1)$ for $x>0$, which equals $-3$ only at $x=0$. Eq. (48) solves Burgers on each side, and with $s=\sqrt{1+\mu_2t}$, Eq. (49) gives $x_s-1=s(\mu_1s-\mu_1-\mu_2)/\mu_2$, so $\tfrac12\big(\mu_1+\mu_2(x_s-1)/(1+\mu_2t)\big)=\mu_1-(\mu_1+\mu_2)/(2s)=x_s'(t)$: (48)–(49) satisfy Rankine–Hugoniot and belong to the initial data $w_0=\mu_1H(-x)+\mu_2(x-1)H(x)$. Eq. (47) as printed is inconsistent with them.
- §5.1.1: "$x_s$ … is the shock speed"; in (48)–(49) $x_s$ is the shock position. Same paragraph: "the point where the shock exists the right boundary" (exits).
- Remark 10: "there are several ways to split $\mathcal Q^d_0$ into $N_3=4$ simplices … each prism must be split into four simplices". *(Compiler check, not in the sources:)* without added points every triangulation of a triangular prism has three tetrahedra, which the printed "4" and "four" contradict.
- §5.3.2: "extruding a spatial mesh of 20 elements and splitting the quadrilaterals to produce 160 quadratic … space-time simplices". *(Compiler check, not in the sources:)* with the four-triangle split of Remark 9, 20 quadrilaterals give 80 triangles; the other 1D cases follow the factor 4 (6→24 in §5.1.1, 8→32 in §5.2). Either slab 1 has two layers in time or the number is a slip; the text does not decide.
- Eq. (39) writes $f_{\mathrm{msh}}(\boldsymbol y^s)$; the superscript $s$ is never defined.
- §2.4 calls the reference domain $\Omega_0$ once; elsewhere it is $\bar\Omega$. Eq. (26) writes $\nabla\bar\psi_h$ for $\bar\nabla\bar\psi_h$ and the traces without bars.
- Typos: "the space-time Jacobian and be related" (§2.2), "linear Rimean problem" (Remark 4).
- §5.3.2 "over $5\times10^4$" lacks its noun; §5.2 uses $\eta$ for the free-surface height and $\eta_x$ for the normal in one sentence; §5.3.1 does not state $\gamma$ for Sod (1.4 is stated only for Shu–Osher).

# Notation map

| Naudet & Zahr 2024 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U_x$, $U$, $W$, $W_x$ | $u$ | state; $W$ is a generic flux argument, not primitive variables |
| $\mathcal F_x$ ($m\times d'$), $\mathcal F=[\mathcal F_x\ W]$ | $f_x$, space-time flux $[f_x\ u]$ (local) | $f^{(d)}$ are the columns of $f_x$ |
| $\mathcal S_x$, $\mathcal S$ | $S(u)$ | **collision**: the source's $S$ is also the number of slabs |
| $S$ (number of slabs), $\Delta t$ | $N_{\mathrm{sl}}$ (local), slab height | |
| $m$ | $m$ | agree |
| $d'$, $d=d'+1$ | $d'$, $d'+1$ | **collision**: registry $d$ is a direction index |
| $\eta=(n_x,n_t)$, $\eta_x$ | $n=(n_x,n_t)$, $\hat n_x$ (local) | **collision** with the entropy $\eta$ |
| $B_x$, $B$ | $A_x$, $A_{xt}$ (local) | projected flux Jacobians; **collision** with the SBP boundary matrix $B$ |
| $V_x$, $V_x^{-1}$, $\Lambda_x$ | $R$, $L$, $\Lambda_x=\mathrm{diag}(\lambda_l)$ | |
| $\tilde B_x$, $\tilde B$ | $\tilde A$ (local) | dissipation matrix of the linearized Riemann solver |
| $\hat U(W^+,W^-)$, $\hat W$ | Roe average | the hat also marks nondimensional quantities in §4.4 |
| $\mathcal H_x$, $\mathcal H$, $\bar{\mathcal H}$ | $h$, $\bar h$ | **collision** of trace labels: the source's $W^+$ is the interior and $W^-$ the exterior trace, not the registry's right and left states |
| $\mathcal G$, $G$, $g$ | domain map, $\Theta$, $\det\Theta$ (local) | **collision**: registry $G$ is the admissible set |
| $\sigma$ (Eq. 21) | $\sigma_\Theta$ (local) | not the affine scaling $\sigma$ |
| $p$ | $N$ | DG solution degree; the source writes pressure $P$ |
| $q$ | geometry degree (local) | **collision** with the weight exponent $q$; $q$ is also the placeholder for $g$ |
| $p'$ | $N+1$ | test degree of the enriched residual |
| $\boldsymbol r$, $\boldsymbol R$ | $\mathsf r$, $\mathsf R$ (local) | standard and enriched residuals; **collision** with $r$ and the eigenvector matrix $R$ |
| $\boldsymbol u$, $\boldsymbol x$, $\boldsymbol y$, $\boldsymbol\phi$ | $\mathbf u$, $\mathbf x$, $\mathbf y$, $\boldsymbol\phi$ (local) | solution DoFs, nodal coordinates, free mesh DoFs, parametrization |
| $\zeta$ | translation of the slab top (local) | not the characteristic variables $\zeta$ |
| $\kappa$ | $\kappa_{\mathrm m}$ (local) | **collision** with the kinetic energy $\kappa$ |
| $N_d$ | $N_d^{\triangle}$ (local) | simplices per prism; **collision** with the DG degree $N$ |
| $s_{\bar K}$, $\chi$, $\Pi_{p-1}$ | $s^{\mathrm{PP}}_K$, first state component, $\Pi_{N-1}$ | Persson–Peraire sensor in $\log_{10}$ form; **collision** with the entropy $s$ |
| $\epsilon$ (optimality tolerance) | tolerance | not the WENO $\epsilon$ |
| $D_x^\star$, $t^\star$, $C$ | length, time and state scales | |
| $\rho$ (shallow water) | geopotential $gH$ (local) | **collision** with the density $\rho$ |
| $H$, $h$, $\eta$ (shallow water) | total depth, bed, free surface | $H$ is also the Heaviside function in §5.1.1; **collision** with the enthalpy $H$ and the flux $h$ |
| $P$, $\check c$ | $p$, $c$ | pressure, sound speed |
| $\beta$ | Burgers direction (local) | not $\beta_k$ |
| $\mu_1$, $\mu_2$, $x_s$ | states and position of the Burgers shock | |

# Reference list

The paper prints 58 references, numbered [1]–[58] and sorted alphabetically by first
author. The list is merged complete into the [bibliography](/bibliography.md), with
`citedby` including `naudet-2024`. Same-author same-year works take suffixes in
printed order (Corrigan 2019 [10]/[11], Kercher 2021 [22]/[23], Zahr 2020 [56]/[58]).
Ref. [19] (Huang, Naudet & Zahr, arXiv:2304.11427, 2023) is a different work from the
ingested `huang-2023` and is keyed apart; ref. [20] is the ingested
[Huang & Zahr (2022)](/sources/huang-2022.md). Refs. [19] and [40] are arXiv
preprints. Ref. [1] prints an article number without volume, and ref. [7] prints
"June 2007, AIAA Paper 2006-3959" (recorded as printed). No item is unparseable.

# Pages created or updated

Chunk 8 (2026-10-23), cited further in chunk 9 (2026-10-23). This source is cited on:

* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Dam-break problems](/benchmarks/dam-break-problem.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Implicit shock tracking and moving DG (MDG-ICE)](/methods/implicit-shock-tracking.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Shallow-water equations](/definitions/shallow-water-equations.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
