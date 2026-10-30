---
type: Source
title: "Barsukow et al. (2026) — A generalized Active Flux method of arbitrarily high order in two dimensions"
description: "Semi-discrete Active Flux of arbitrary order on 2D Cartesian grids, built as a hybrid finite element with shared node and edge point values plus moments in a serendipity-based minimal space; only Gauss edge points give a stable semi-discretization, and orders 3–7 converge on smooth tests."
resource: "doi:10.1016/j.compfluid.2025.106886"
source_kind: paper
authors: [Barsukow W., Chandrashekar P., Klingenberg C., Lechner L.]
year: 2026
venue: "Comput. Fluids 307:106886"
local_file: "/home/stefano/papers/mosaic/weno-teno/2026_Crossref_Computers_amp_Fluids_Barsukow_A_generalized_Active_Flux_method_of_arbitrarily_high_order_i.pdf"
tags: [active-flux, high-order, stability-analysis, cartesian-grid, finite-element]
timestamp: 2026-10-23T20:30:00Z
---

# Summary

Barsukow et al. (2026) extend the semi-discrete ("generalized")
[Active Flux](/methods/active-flux.md) method, so far of arbitrary order only in 1D
([Abgrall & Barsukow 2023](/sources/abgrall-2023.md)) and third order on 2D Cartesian
grids, to arbitrary order $N+1$ in 2D. The method is a hybrid finite element–finite
volume scheme. Its degrees of freedom are point values at the four nodes and at $N-1$
points per edge, shared between neighbours so that the reconstruction is globally
continuous, plus moments of the solution against monomials, always including the cell
average. Two reconstruction spaces are studied: the tensor space of degree $N$ in each
variable, and a minimal space based on the serendipity space
$\mathbb P^N\oplus\mathrm{span}\{x^Ny,xy^N\}$, which needs far fewer moments.
$\mathbb P^N$ alone is not unisolvent; the minimal space is, as checked with computer
algebra up to order 7.

Point values are evolved in quasilinear form, with Jacobians split by the sign of
their eigenvalues and one-sided derivatives of the reconstruction in the upwind cell;
moments are evolved by the weak form with quadrature, and the conservative update of
the average gives convergence to weak solutions by the
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md). A numerical eigenvalue
analysis for 2D linear advection shows the semi-discretization stable only with Gauss
edge points; uniform and Gauss–Lobatto points give eigenvalues with positive real part
from order 4 on. With [SSP-RK3](/methods/ssp-runge-kutta.md) the maximal CFL numbers
fall from 0.27 (order 3) to 0.088 (order 7), and the stable region in the plane of the
directional CFL numbers changes from a disc to nearly a square.

Tests are smooth only: linear advection of a cone and of a Gaussian (design-order
$L^1$ convergence of cell averages up to order 7), the sine-wave
[linear acoustics test](/benchmarks/linear-acoustics-tests.md) and the low-Mach
[Gresho vortex](/benchmarks/gresho-vortex.md). Limiting for discontinuous problems,
for example with [flux vector splitting](/methods/flux-vector-splitting.md) for the
point-value update as in Duan et al. (2025), is left to future work; the paper adds
nothing on [bound preservation](/properties/bound-preservation.md).

# Version read

The archive file is arXiv:2502.05101v2 [math.NA], 4 December 2025, 31 pages, all read
(pp. 15 and 25–27 also on the page images). It is the preprint of the Computers &
Fluids paper, without journal header or article number; title and authors match the
Crossref record. Every claim, equation and number on this page is that of arXiv v2.

# Key claims

Registry notation: state $u$ (source $q$), flux $(f,g)$ (source $(f^x,f^y)$), cells
$I_{i,j}$ (source $C_{ij}$, indices from 0), cell average $\bar u_{i,j}$, reconstruction
degree $N$ and order $N+1$ as in the registry, eigenvalues $\lambda_l$, $R$ the
right-eigenvector matrix (source $T^x$). Page-local: $u^{(p)}_{i,j}$ the point value
at point $p$, $u^{(k,l)}_{i,j}$ the moment against $x^ky^l$ in reference coordinates,
$\xi_a\in(-\tfrac12,\tfrac12)$ the reference edge-point coordinates, $S^N$ the
serendipity space, GenAF($M_\square$) and GenAF($M_\triangledown$) the tensor-like
and minimal variants, $\nu_x=a_x\Delta t/\Delta x$, $\nu_y=a_y\Delta t/\Delta y$ the
directional CFL numbers, $C_{\mathrm{cfl}}$ and $r_{\mathrm{cfl}}$ the maximal CFL
number and disc radius.

1. A semi-discrete generalized Active Flux of arbitrary order $N+1$ on 2D Cartesian grids follows from shared point values at nodes and edges and higher moments, keeping a globally continuous reconstruction, a compact stencil, the cell average among the degrees of freedom, and a minimal number of degrees of freedom (§3, Def. 2). **Derived**
2. $N+1$ shared point values per edge (4 nodes and $N-1$ edge points, $4N$ per cell) are needed for the reconstruction to be a unique degree-$N$ polynomial on each edge and globally $C^0$; per cell, one node and $2(N-1)$ edge points are updated (§3.2, Eq. (9)). **Derived**
3. The tensor-like space $\mathbb Q^N$ has $(N+1)^2$ degrees of freedom, $4N$ point values and $(N-1)^2$ moments $\{0\le k,l\le N-2\}$, and reduces at order 3 to the Cartesian Active Flux reconstruction of Barsukow et al. (2019) and Helzel et al. (2019) (§3.3.1, Eqs. (13), (19)). **Derived**
4. The minimal space is $S^N\oplus\mathrm{span}\{x^2y^2\}$ for $N=2,3$ and $S^N=\mathbb P^N\oplus\mathrm{span}\{x^Ny,xy^N\}$ for $N\ge4$, $\lvert S^N\rvert=\tfrac12(N+1)(N+2)+2$, with $\tfrac12(N-3)(N-2)$ moments against $\mathbb P^{N-4}$ (Eqs. (20)–(21), Table 2). **Derived**
5. $\mathbb P^N$ is not unisolvent on Cartesian cells (checked with Mathematica for $N=5,6$), and for $N=4$ neither is $\mathbb P^4\oplus\mathrm{span}\{x^3y^2,x^2y^3\}$ (§3.3.2). **Shown** (computer algebra)
6. The minimal basis (20) is unisolvent up to order 7 (§3.3.2). **Shown** (computer algebra; no proof for general $N$)
7. Degrees of freedom of GenAF($M_\triangledown$) (point values + moments): order 3, $8+1$; 4, $12+1$; 5, $16+1$; 6, $20+3$; 7, $24+6$ (Table 2). **Derived**
8. With uniformly distributed edge points the semi-discrete method is not stable, as with the additional interior point values of the 1D method of [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md), where the points had to move toward the interfaces (§4.1). **Shown**
9. With Gauss edge points GenAF($M_\triangledown$) is stable at every tested order 3–7: $\mathrm{Re}\,\lambda<\epsilon$, with eigenvalues of $\lvert\mathrm{Re}\,\lambda\rvert<\epsilon$ at least semisimple, $\epsilon=5\cdot10^{-13}$ (orders 3–5), $10^{-12}$ (6), $5\cdot10^{-12}$ (7), for advection angles $\theta\in[0,\pi/2]$ in steps of $\pi/64$ and $N_x=N_y\in\{3,5,10\}$ (§4.1). **Shown** (numerical spectrum)
10. Uniform and Gauss–Lobatto edge points give unstable semi-discretizations for orders 4–7: eigenvalues with positive real part for every tested $\theta$ at orders 5–7 and for $\theta=0,\pi/2$ at order 4; at order 3 the distributions coincide (§4.1). **Shown**
11. The eigenvalues scale with the grid size, $h\lambda$ being grid independent (§4.1, Fig. 6). **Shown**
12. GenAF($M_\square$) at orders 4 and 5 is again stable only with Gauss edge points (§4.1, Remark). **Shown**
13. The semi-discrete advection operator is diagonalizable to the same tolerances (§4.2). **Shown**
14. With SSP-RK3, $C_{\mathrm{cfl}}=0.27$, $0.20$, $0.17$, $0.12$, $0.088$ at orders 3–7, defined at $a_x=a_y$ with $h=0.1$ (Eq. (42), Table 3). **Shown**
15. The stable time step depends on the direction of advection as well as its magnitude: at order 3 (and about 4) the stable region is a disc $\nu_x^2+\nu_y^2\le r_{\mathrm{cfl}}^2$, $r_{\mathrm{cfl}}=\sqrt2C_{\mathrm{cfl}}$, so $\Delta t\le r_{\mathrm{cfl}}\min\{\Delta x,\Delta y\}/\lvert a\rvert$; at higher orders it is close to the square $\max\{\nu_x,\nu_y\}\le C_{\mathrm{cfl}}$ (Eqs. (43)–(46), Fig. 8). **Shown**
16. The order-5 region is almost square; orders 4 and 5 add only interface point values, which favour the maximal advection speed, and the interior moments added at orders 6 and 7 round the corners again (§4.2, Remark). **Shown** (interpretation **Stated**)
17. GenAF($M_\square$) with RK3 has nearly circular stable regions, $C_{\mathrm{cfl}}\approx0.14$ at order 4 and $0.089$ at order 5: smaller than $M_\triangledown$ but less direction dependent (§4.2, Remark). **Shown**
18. For $M_\square$ the maximal CFL number along $x$ or $y$ is about that of the 1D hybrid method of Abgrall & Barsukow (Appl. Math. Comput. 2023, Method A, RK3) at orders 3–5 (§4.2). **Stated**
19. Barsukow, Klingenberg, Kunik and Lechner (2025) derived $c\Delta t/\min\{\Delta x,\Delta y\}<0.28$ by Fourier analysis for third-order generalized Active Flux applied to 2D linear acoustics, "a similar result" (§4.2). **Stated** (cited)
20. Gaussian advection with $\nu(h_i)=\nu(h_1)(h_i/h_1)^{(N-2)/3}$, so that $\Delta t^3=O(h^{N+1})$, gives final $L^1$ orders of cell averages 2.98, 4.02, 4.98, 6.01, 7.00 at orders 3–7, finest errors $1.92\cdot10^{-6}$, $2.98\cdot10^{-8}$, $3.34\cdot10^{-9}$, $4.81\cdot10^{-11}$ ($h=1/256$) and $5.60\cdot10^{-11}$ (order 7, $h=0.00625$) (§5.1, Table 4). **Shown**
21. Cone advection to $t=5$ on $101^2$ cells resolves the apex better at higher order (§5.1, Fig. 10). **Shown** (qualitative)
22. Acoustic sine wave to $t=5$ on $60^2$ and Gresho vortex ($M=0.1$) to $t=1$ on $51^2$: higher orders are closer to the exact solution (§5.2, §5.3, Figs. 12–15). **Shown** (qualitative)
23. Gauss edge points were used for the linear and nonlinear systems of the examples, with no instability observed (§4.1). **Shown** (qualitative)
24. Classical Active Flux is a one-stage fully discrete method; the Runge–Kutta stages widen the effective stencil of generalized Active Flux, which Roe (2021) linked to a smaller maximal CFL number; the 2025 acoustics paper shows similarities of the classical and generalized third-order methods, such as stationarity preservation (§1). **Stated** (cited)
25. Discontinuous problems need limiting, for example that of Duan et al. (2025) for third-order Active Flux, with flux vector splitting in the point-value update; left to future work (§5, §6). **Stated**

*(Compiler check, not in the sources: the degree-4 interpolant through
$\{-\tfrac12,-\xi,0,\xi,\tfrac12\}$ with $\xi=\tfrac12\sqrt{3/5}$, the three
Gauss–Legendre points of the edge plus the two nodes, has derivative weights
$(1,-1.88,2.67,-14.79,13)$ at $+\tfrac12$ and $(1.5,-3.23,0,3.23,-1.5)$ at $0$, the
rows printed in Fig. 5(a) and 5(c): "Gauss points" are Gauss–Legendre nodes on the
edge, and the edge set with its nodes is not a Gauss–Lobatto set.)*

# Printed slips

- **Acoustics exact solution** (§5.2, p. 25): printed $p=\frac1c\cos(2\pi ct)(\sin2\pi x+\sin2\pi y)$, $v=\frac1c\sin(2\pi ct)(\cos2\pi x,\cos2\pi y)^\top$ for $\partial_tp+c\nabla\cdot v=0$, $\partial_tv+c\nabla p=0$. *(Compiler check, not in the sources: substitution gives $\partial_tp+c\nabla\cdot v=-4\pi\sin(2\pi ct)(\sin2\pi x+\sin2\pi y)$ and $\partial_tv+c\nabla p=4\pi\cos(2\pi ct)(\cos2\pi x,\cos2\pi y)^\top$; both vanish when the sign of $v$ is reversed.)* [Calhoun et al. (2023)](/sources/calhoun-2023.md) print the initial pressure with a leading minus, $p(x,y,0)=-\frac1c(\sin2\pi x+\sin2\pi y)$. The comparison at $t=5$, where $v=0$ and $p=p(0)$, is not affected.
- **Gresho vortex velocity** (§5.3, p. 27): printed $v=\frac{5r}{r}(-y-0.5,\ x-0.5)^\top$, and likewise for $0.2\le r<0.4$. *(Compiler check, not in the sources: the azimuthal direction about $(0.5,0.5)$ is $(-(y-0.5),x-0.5)/r$; the printed first component is not tangential, and should read $0.5-y$.)*
- **Fig. 5(b)** (p. 15): the weights of $(D^-_x)$ at the node, on the top edge of the cell to the right, are printed $-13,\ 1.88,\ -2.67,\ 14.79,\ -1$. *(Compiler check, not in the sources: the derivative of the interpolant above at $-\tfrac12$ has weights $-13,\ 14.79,\ -2.67,\ 1.88,\ -1$; the two inner labels are swapped.)*
- §3.4: "$(D^+_x)^{(p)}_{ij}q=(D^-_x)^{(p)}_{ij}=\dots$" drops the $q$ after $(D^-_x)$; "non-postive" (§4.1).

# Notation map

| Barsukow et al. (arXiv v2) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$, $s$ | $u$, $m$ | **collision**: source $q$ is the state, registry $q$ the weight exponent |
| $f=(f^x,f^y)$ | $(f,g)$, $f^{(d)}$ | |
| $C_{ij}$, $\bar q_{ij}=q^{(0,0)}_{ij}$ | $I_{i,j}$, $\bar u_{i,j}$ | indices from 0 |
| $q^{(p)}_{ij}$, $x^{(p)}_{ij}$, $I_N$, $I_E$, $I_P$, $I_M$, $I_{dof}$ | point values and index sets (local) | |
| $q^{(k,l)}_{ij}$, $b_{k,l}$, $A_{k,l}$ | $u^{(k,l)}_{i,j}$, monomial, normalization (local) | not the Hermite moment $\bar u^{(1)}_i$ |
| $\xi_a$ | reference edge-point coordinate (local) | **collision** with the DG nodes $\xi_j$; here Gauss–Legendre points of an edge |
| $N$ | $N$, order $N+1$ | agree |
| $P^N$, $P^{N,N}$, $S^N$ | $\mathbb P^N$, $\mathbb Q^N$, $S^N$ (local) | |
| $Df^x$, $T^x$, $\lambda_{x,k}$, $\lambda^\pm$ | $A$, $R$, $\lambda_l$, $\max(0,\lambda)$, $\min(0,\lambda)$ | Jacobian sign splitting |
| $(D^\pm_x)^{(p)}_{ij}$ | upwind derivative (local) | "+" from the cell on the left or below |
| $A$, $\lambda_i$ | semi-discrete linear operator, its eigenvalues | **collision** with the flux Jacobian $A$ |
| $a=(a_x,a_y)=(\cos\theta,\sin\theta)$ | advection velocity | **collision** of $a$ with the maximum wave speed, and of $\theta$ with the Zhang–Shu factor |
| $cfl_x$, $cfl_y$, $C_{cfl}$, $r_{cfl}$ | $\nu_x$, $\nu_y$, $C_{\mathrm{cfl}}$, $r_{\mathrm{cfl}}$ | |
| $G(z)$ | RK3 stability polynomial | **collision** with the admissible set $G$ |
| $\mathbf v$, $c$, $p$, $\rho$, $E$, $M$ | $v$, $c$, $p$, $\rho$, $E$, $M$ | agree |

# Reference list

The arXiv v2 prints 35 references with alphabetic labels ([AB23a], [BEK+17], …),
sorted by label. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` including `barsukow-2026`. [AB23b]
(Extensions of Active Flux to arbitrary order, ESAIM M2AN 57) is the ingested
[Abgrall & Barsukow (2023)](/sources/abgrall-2023.md), while [AB23a] (the hybrid
finite element–finite volume method, Appl. Math. Comput. 447) takes a separate key.
[ABK25] (semi-discrete Active Flux for Euler, J. Sci. Comput. 102) and [ALL25]
(triangular meshes) are matched by venue, as are [Bar20] (J. Sci. Comput. 86), [Van77]
(van Leer part IV) and the PhD thesis [He21], whose printed-order keys collide with
different works in the bibliography. [CHLM24] is the ingested
[Chudzik et al. (2024)](/sources/chudzik-2024.md). [BKKL25] is printed without volume
or pages; [Wol23] (Mathematica) has a corporate author. No item is unparseable.

# Pages created or updated

Chunk 10 (2026-10-23), cited further in chunks 11–12 (2026-10-24/30). This source is cited on:

* [Active Flux](/methods/active-flux.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Flux vector splitting](/methods/flux-vector-splitting.md)
* [Gresho vortex](/benchmarks/gresho-vortex.md)
* [Linear acoustics tests](/benchmarks/linear-acoustics-tests.md)
* [Matrix stability analysis of shock-capturing schemes](/methods/matrix-stability-analysis.md)
* [PAMPA scheme](/methods/pampa-scheme.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Stationary contact preservation](/properties/stationary-contact-preservation.md)
