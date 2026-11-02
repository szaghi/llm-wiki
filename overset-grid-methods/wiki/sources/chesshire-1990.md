---
type: Source
title: "Chesshire & Henshaw (1990) — Composite overlapping meshes for the solution of partial differential equations"
description: "Foundational description of composite overlapping grids and the CMPGRD generator: point classification with a signed donor-grid flag, an ordering-based composite-grid algorithm with donor search by Newton inversion, explicit and implicit Lagrange interpolation, a 1-D theory of the required interpolation width versus overlap, IMEX time stepping, and compressible Navier–Stokes verification."
resource: "doi:10.1016/0021-9991(90)90196-8"
source_kind: paper
authors: [Chesshire G., Henshaw W.D.]
year: 1990
venue: "J. Comput. Phys. 90:1-64"
local_file: "/home/stefano/papers/mosaic/overset-chimera/1990_Crossref_Journal_of_Computational_Physics_Chesshire_Composite_overlapping_meshes_for_the_solution_of_partial_dif.pdf"
tags: [composite-grid, overset-grid, domain-connectivity, interpolation, software, compressible]
timestamp: 2026-11-02T11:28:00Z
---

# Summary

Chesshire and Henshaw give the foundational journal description of the
[composite overlapping grid](/definitions/composite-overlapping-grid.md) of
the Kreiss school, which belongs to the [overset grid](/definitions/overset-grid.md)
family, and of the grid generator [CMPGRD](/software/cmpgrd.md). A composite
grid $\mathcal G$ is a set of logically rectangular component grids $G_k$,
each the image $\mathbf x=\mathbf d_k(\mathbf r)$ of the unit square. The
grids cover the domain, overlap where they meet, and are coupled by
interpolation equations.

The authors call the composite-grid algorithm "by far, the most important
and most difficult result of this paper". It is a
[domain connectivity](/definitions/domain-connectivity.md) algorithm driven
by the order of the grids: a higher $k$ means higher
[priority](/definitions/grid-hierarchy.md). It classifies every point as a
discretization, interpolation or exterior point
([point classification](/definitions/point-classification.md)) in a flag
$kr$ that carries the donor grid in its sign. The registry's mask $\iota$ is
modelled on this flag. The algorithm needs no hole surfaces: exterior points
are seeded next to physical boundaries and spread by iteration, a form of
[implicit hole cutting](/methods/implicit-hole-cutting.md) (see also
[hole cutting](/methods/hole-cutting.md)). It then deletes unneeded
[interpolation points](/definitions/fringe-point.md) and converts others to
discretization points ([overlap optimization](/methods/overlap-optimization.md)).
The [donor search](/methods/donor-search.md) combines a bounding box, a
nearest-point walk and Newton inversion of $\mathbf d_{k'}$.

[Inter-grid interpolation](/methods/inter-grid-interpolation.md) is
tensor-product Lagrange interpolation in the donor's parameter coordinates,
either [explicit or implicit](/definitions/explicit-and-implicit-interpolation.md).
A 1-D analysis (Lemmas I and II) gives the
[required interpolation width](/results/interpolation-order-requirement.md):
for a second-order solution of a PDE of order $2s$, $q\ge2s+1$ when the
overlap shrinks with $h$ and $q\ge s+1$ when it stays fixed. 1-D and 2-D
Poisson tests confirm it.

The paper also describes elliptic solvers (sparse direct and multigrid), an
implicit–explicit time stepper, and CGNVT, a non-conservative compressible
Navier–Stokes code. CGNVT is verified to second order with a manufactured
solution (the technique Henshaw (1994) calls [twilight-zone flow](/methods/twilight-zone-flow.md)),
on a [cylinder in a channel](/benchmarks/flow-past-circular-cylinder.md), and
tested on a Mach 2 impulsively started cylinder whose bow shock crosses an
interpolation boundary. The paper leaves conservation at interpolation
boundaries to future work ([conservative overset interface](/methods/conservative-overset-interface.md)).
Its solver framework, elliptic solvers and verification approach are the
base on which [incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)
is built.

# Version read

Version of record (Academic Press typeset), J. Comput. Phys. 90, 1–64
(1990), 64 pages, all read. It is a scanned image with an OCR layer that
garbles nearly every display equation. Equations, pseudo-code, tables and
references were read visually from the page images. The page-1 title,
authors (spelled **Chesshire**; the OCR sometimes reads "Cheshire") and
volume match Crossref. The scan prints no DOI. Equation, lemma, table and
page numbers are those of the journal.

# Key claims

Registry notation: the source's $(r,s)$ is $\mathbf r=(r_1,r_2)$; its $D$,
$D_k$ are $\Omega$, $\Omega_k$; its PDE order $2p$ is $2s$; its
discretization order $2r$ is the order $p$; its interpolation width $q$
(CMPGRD's `iw`) is $q$; its flag $kr$ is the mask $\iota$ (see the Notation
map); its overlap $d$ is $d$.

1. A composite grid is a set of logically rectangular curvilinear component grids whose union covers the domain, overlapping where they meet, with the solutions matched by interpolation. Its main advantage is grid generation for complicated geometries (§1, abstract). **Stated**
2. Single-mapping grids have intrinsic limits: forced non-uniform density, global effect of local changes, and a necessary singularity on the boundary if the region "is not doubly connected" (for example, any map from the unit square onto a disc has a singular Jacobian at some corners) (§2, p. 7). **Stated**
3. A patched grid "can in some sense be thought of as an overlapping grid with exactly zero overlap"; overlapping grids are more flexible (§2, p. 8). **Stated**
4. The CMPGRD composite-grid algorithm is "fundamentally different" from those of B. Kreiss and of Benek et al., and is "by far, the most important and most difficult result of this paper" (§3.2, p. 14). **Stated**
5. The composite grid depends on the interpolation width, the discretization width, the minimum overlap and the order of the component grids (§3.2, p. 14, Fig. 9). **Shown** (qualitative)
6. If a valid composite grid exists for some order of the grids, a valid grid "should result for all orderings". This is explicitly not proved (§3.2, p. 16). **Stated**
7. A centred three-point discretization needs one line of interpolation points, a five-point one two lines (§3.2, p. 14). **Stated**
8. Building the composite grid costs $O(n_g^2N_{\mathrm{pts}})$ operations (§3.2, p. 21). **Stated** (estimate)
9. Grid construction took 1.6 s, 3.1 s and 7.2 s for the three cylinder-in-channel grids and 9.3 s for the multi-flap airfoil (IBM 3090VF) (§6.4, p. 55; §6.5, p. 60). **Shown**
10. Explicit interpolation (no donor stencil contains an interpolation point) avoids coupling the interpolation equations at the price of more overlap. Implicit interpolation needs a small sparse solve, factored once, but less overlap and fewer points (§5.2, p. 28). **Stated**
11. Lemma I: for the 1-D model problem of order $2s$ on two overlapping grids with $d\ge ch$, the error is second order provided $q\ge2s+1$ (§5.3, p. 33). **Proved**, assuming the problem with zero interpolation truncation error is well posed, which [21] proves only for $s=1$
12. Lemma II: if $d\ge c$ independently of $h$, second order requires $q\ge s+1$ (§5.3, p. 34). **Proved** (same assumption)
13. General rule (p. 29): for order $p$, $q=sp+1$ if $d\propto h$ and $q=sp/2+1$ if $d=O(1)$, with $sp/2$ interpolation points on each grid and total overlap $d+\tfrac{sp}{2}(h_1+h_2)$. The extension beyond $p=2$ rests on Remark 1, that solving a fourth-order equation to second order is equivalent to solving a second-order equation to fourth order. **Derived** (heuristic for $p>2$)
14. Corollary from Henshaw's thesis: for second-order elliptic equations solved to second order, quadratic interpolation ($q=3$) is needed if the overlap shrinks with $h$, and linear interpolation ($q=2$) suffices if the overlap stays above a constant (§5.3, p. 29). **Stated** (cited)
15. Interpolation equations are not non-essential boundary conditions. Unlike the results of H.-O. Kreiss and Gustafsson, where lower-order boundary conditions can suffice, interpolation must be done to full accuracy (Remark 3, p. 34). **Derived**
16. 1-D tests (Tables I–II): with $d=0.5h$, $q=2s$ gives $\sigma=1.0$ ($s=1$) and $0.79$ ($s=2$), and $q=2s+1$ gives $2.1$ and $2.0$. With $d=0.5$, $q=s$ gives $0.38$ and $1.3$, and $q=s+1$ gives $1.9$ and $2.1$ (pp. 35–36). **Shown**
17. 2-D Poisson tests (Tables III–IV): second-order discretization with $q=2$ gives $\sigma=0.98$ and with $q=3$ $\sigma=2.1$; fourth-order discretization with $q=4$ gives $\sigma=3.2$ and with $q=5$ $\sigma=4.2$. A $3\times3$ stencil is required for second order and a $5\times5$ one for fourth order (p. 41). **Shown**
18. Multigrid on composite grids (CGMG) converges "almost as well" as on a single grid. CMPGRD builds the coarse levels, which are not simply the fine grids with lines removed (§5.5, p. 39). **Stated** (cited)
19. The IMEX scheme (5.10), trapezoidal implicit part plus second-order Adams–Bashforth explicit part, is second order in time. General IMEX multistep schemes follow by extrapolating $\mathbf f$ at level $n+1$ to the required order in the explicit part (§5.6, pp. 42–43). **Derived**
20. The frozen-linearization splitting ($\mathbf f^{\mathrm I}=U_0u_x+\nu u_{xx}$, $\mathbf f^{\mathrm E}=(u-U_0)u_x$) is second order whatever $U_0$ is, and more stable when $U_0$ is close to the current solution (§5.6, p. 44). **Stated**
21. CGNVT is second order: the manufactured-solution Test 1 gives error ratios 2.0–2.2 between grids with spacings in ratio $2:\sqrt2:1$ (Table VI). **Shown**
22. Neither the discretization nor the interpolation is conservative. "If the computed solution is smoothly represented on the grid then the question of conservation is not crucial", but conservation matters when the shock is not resolved; a systematic study is deferred (§6.4, pp. 49–52; §7). **Stated**
23. On the coarsest grid the Mach 2 bow shock "has some difficulty crossing the interpolation boundary"; it is well represented on the two finer grids (Fig. 19a, p. 52). **Shown**
24. Self-convergence ratios $\lVert u_1-u_3\rVert/\lVert u_2-u_3\rVert$ (3 expected for second order) are 2.5–4.8 in the max norm and 2.8–4.0 in $l_2$ (Tables VII–VIII). **Shown**
25. For explicit time stepping, the storage overhead of composite grids over a single-grid code is essentially the flag array ($N_{\mathrm{pts}}$ integers) plus interpolation arrays. In the implicit CGNVT run on the coarsest grid, the sparse solver takes 2,673,907 of 2,802,678 words (Table IX). **Shown**
26. CPU (IBM 3090VF): explicit run 0.11 s/step, 45.9 s to $t=1$; semi-implicit run 0.21 s/step, 42.6 s. The implicit run takes a time step twice as large and is slightly cheaper overall. D. Brown reports interpolation at 11% of the interior update with explicit interpolation on a Cray X-MP (Table X, p. 56). **Shown**/**Stated** (Brown)
27. Multi-flap airfoil: 8101 grid points, 0.725 s/step, 145 s to $t=1$ (Table XI). **Shown**
28. Each component grid can be generated almost independently, and grid spacings should be about equal where grids overlap (§3.1, p. 11). **Stated**
29. Interpolating in the donor's parameter coordinates $\mathbf r'$ makes arbitrary-order interpolation easy and less error-prone (§5.2, p. 28). **Stated**

# Printed slips

- Step 5 pseudo-code (p. 20): "kr(i′, j′, k′) − |kr(i′, j′, k′)|" lacks the assignment arrow of Step 4 ("kr(i′, j′, k′) ← −|kr(i′, j′, k′)|").
- Step 6 pseudo-code (p. 20): "kr(i, j, k) ← |kr(i′, j′, k′)|" uses primed indices, inconsistent with its test "if |kr(i, j, k)| = k" and with the other branch.
- 1-D grid (p. 30): $G^2=\{x^2_i=b-(i-1)h_2\}$ places $x^2_1$ at the boundary $b$, while the interpolation points are $x_{p+j}=x^2_j$, Fig. 14 puts $x^2_1$ at the inner end, and the right boundary condition acts on $v^2_{N_2-j}$.
- Cross distance (p. 34): $\lvert x_i-x_j\rvert=d+(p-i)h_1+(j-p-1)h_2$ gives $d+(p-1)h_2$ at $i=p$, $j=2p$, whereas the definition $d=x_p-x_{2p}$ requires $d$. The counting argument is unaffected.
- Eqs. (5.7)–(5.8) (p. 33): the products $\prod_{i=1}^{2p}\prod_{j\ne i}(x_i-x_j)$ count each pair twice. This contradicts the paper's own statements that $\det A$ has degree $2p-1$ in each $x_j$ and that the denominator has $\binom{2p}{2}$ factors (p. 34), which fit a product over $i<j$.
- p. 32: "$e^1(x_i)=\sum_{i=1}^{p}\alpha^1_{i,j}e^2(x_j)$": the summation index should be $j$.
- Table I (p. 35): caption and header read "$d=0.5$", but the text assigns Table I to the case $d=0.5h$; Table II is the $d=0.5$ case.
- p. 37: the stretched smoothed-corner grid is printed $\mathbf x_1(u(s))+t(r)R(u(s))\mathbf n(u(s))$, with $R$ (the stretching function) where the unstretched form has the width $N(s)$.
- Eq. (5.9c) (p. 41): donor values are printed $\mathbf u(i',j',k;t)$; by (5.3) the donor grid is $k'$.
- Dissipation function (p. 44): $\Phi=2u_x^2+2v_y^2+(v_x+u_y)^2+\lambda(u_x+v_y)^2$, multiplied by $\mu/C_v$, is dimensionally inconsistent; the nondimensional form's $-\tfrac23$ corresponds to $(\lambda/\mu)(u_x+v_y)^2$ *(compiler check, not in the sources)*.
- p. 45: "$\tilde t=t(L_0/u_0)$" is dimensionally inconsistent, since nondimensional time is $tu_0/L_0$ *(compiler check, not in the sources)*.
- Subsonic inflow condition (p. 45): "$\mathbf u\cdot\mathbf n+\rho-g^2_I$", with "$-$" printed for "$=$".
- Table V (p. 49): the finest background grid is printed $139\times199$, while the other entries ($70\times50$, $99\times71$) follow the stated spacing ratio $2:\sqrt2:1$, which would give about $139\times99$ *(compiler check, not in the sources)*.
- Test 2 (p. 49 vs Fig. 19 caption, p. 50): the text compares contours "at times $t=1$ and $t=3$"; the caption shows $t=2$ and $t=3$.
- Table VIII (p. 55), $T$ row, $t=1$: the ratio is printed 3.6, but the printed norms give $0.035/0.012=2.9$ *(compiler check, not in the sources)*.
- Table IX (p. 55): "Total for sparse solver 2,673,907", whereas $72{,}241+2{,}601{,}766=2{,}674{,}007$; the grand total uses the printed subtotal *(compiler check, not in the sources)*.
- Table XI (p. 57): CPU per step 0.725 against the listed components $0.11+0.60=0.71$; in Table X the components add up to the totals.

# Notation map

| Chesshire & Henshaw (1990) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $G$, $G_k$, $k=1..n_g$ | $\mathcal G$, $G_k$, $n_g$ | higher $k$ = higher priority, as in the registry |
| $D$, $D_k$ | $\Omega$, $\Omega_k$ | |
| $\mathbf d_k(r,s)$ | $\mathbf x=\mathbf d_k(\mathbf r)$ | the registry follows this paper |
| $(r,s)$; $(t,u)$ | $\mathbf r=(r_1,r_2)$; stretched coordinates page-local | |
| $(i,j,k)$, $\mathbf x_{ijk}$ | $(\mathbf i,k)$, $\mathbf x^k_{\mathbf i}$ | |
| $rx,sx,ry,sy$ (`rsxy`) | $\partial r_m/\partial x_n$ | |
| $h_r$, $h_s$ | $\Delta r_1$, $\Delta r_2$ | |
| $kr(i,j,k)$: $k$ / $-k'$ / $0$ | $\iota_k(\mathbf i)$: $1$ / $-k'$ / $0$ | donor grid in the sign, as in the registry; a discretization point is $kr=k$ here, $\iota=1$ there |
| discretization (interior, boundary) / interpolation / exterior (unused) point | $\mathcal D_k$ / $\mathcal R_k$ / $\mathcal H_k$ | |
| `iw(m,k1,k2)`, $q$ | $q$ (per direction and grid pair) | width = order of interpolation |
| $\alpha(i',j',i,j)$, $(i_0',j_0')$ | $\alpha_{\mathbf j}$, corner of $\mathcal S_{\mathbf i}$ | Eq. (5.3) |
| $\mathbf r'=(r',s')$ | $\mathbf r'$ | agree |
| $2p$ (PDE order) | $2s$ | **collision**: registry $p$ is the order of accuracy |
| $2r$ (discretization order) | $p$ | **collision**: registry $r$ is a parameter coordinate |
| $d$ (between innermost interpolation points) | $d$ | agree; not the geometric overlap |
| $h_1,h_2$, $G^1,G^2$ (1-D) | $h_k$, $G_1,G_2$ | |
| $D_+D_-$ | $D_{+}D_{-}$ | |
| $\sigma$ | $\sigma$ | least-squares rate, agree |
| $\mathbf f_E$, $\mathbf f_I$ | $\mathbf f^{\mathrm E}$, $\mathbf f^{\mathrm I}$ | |
| $N$ (points; also normal width $N(s)$) | $N_{\mathrm{pts}}$; width page-local | registry reserves $N$ |
| $\mathrm{Re},\mathrm{Pr},\mathrm{Ma},\gamma$ | $Re$, $Pr$, $M$, $\gamma$ | |
| $\alpha$ (Robin coefficient) | page-local | **collision** with the weights $\alpha_{\mathbf j}$ |
| $G_m$, $m=1,2,3$ (§6.4) | composite grids of increasing resolution, page-local | **collision** with $G_k$ |

# Reference list

The paper prints 36 numbered references ([1]–[36], alphabetical by first
author), all merged complete into the [bibliography](/bibliography.md) with
`citedby` including this slug. Many journal references print no title (for
example [1], [5], [7], [8], [18], [20], [23], [24], [29], [30], [32], [33],
[35], [36]) and are entered with a placeholder title. Ref. [3] is Benek et
al., AIAA Paper 83-1944, with no title printed. Ref. [9] is a private
communication (D. L. Brown, 1989). The theses [21], [25], [27] and the
report [26] print no titles. There are no printed duplicates.

# Pages created or updated

Chunk 1 (2026-11-02). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Multi-element airfoils](/benchmarks/multi-element-airfoil.md)
- [Composite overlapping grid](/definitions/composite-overlapping-grid.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Grid hierarchy and priority](/definitions/grid-hierarchy.md)
- [Orphan points](/definitions/orphan-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Patched (zonal) grids](/definitions/patched-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Donor search](/methods/donor-search.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Implicit hole cutting](/methods/implicit-hole-cutting.md)
- [Incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Overlap optimization](/methods/overlap-optimization.md)
- [Twilight-zone flow (manufactured solutions)](/methods/twilight-zone-flow.md)
- [Interpolation order and overlap requirements](/results/interpolation-order-requirement.md)
- [CMPGRD and its solver suite (CGINS, CGNVT, CGES, CGMG, DSK)](/software/cmpgrd.md)
