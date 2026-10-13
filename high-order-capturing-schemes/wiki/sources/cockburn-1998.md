---
type: Source
title: "Cockburn & Shu (1998) — The Runge–Kutta discontinuous Galerkin method for conservation laws V: multidimensional systems"
description: "Extends RKDG to multidimensional nonlinear systems (2D Euler) on rectangles and triangles: P^1/P^2 DG with Lax–Friedrichs fluxes and quadrature-exactness conditions, SSP Runge–Kutta of order k+1 with a limiter after every stage, and a practical TVB minmod slope limiter applied to the linear part in local characteristic variables (M = 50); double Mach reflection, forward step and shock diffraction."
resource: "doi:10.1006/jcph.1998.5892"
source_kind: paper
authors: [Cockburn B., Shu C.-W.]
year: 1998
venue: "J. Comput. Phys. 141:199–224"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1998-JCP-Cockburn-101006jcph19985892.pdf"
tags: [dg, rkdg, limiter, tvb, euler, unstructured, characteristic]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The fifth paper of the RKDG series extends the Runge–Kutta discontinuous
Galerkin method to multidimensional nonlinear systems, with the 2D Euler
equations as the application. The space discretization is DG with
polynomials of total degree $K = 1, 2$ in each element, quadrature for
edge and volume integrals, and a local or global Lax–Friedrichs flux. The
time discretization is the SSP Runge–Kutta method of order $K + 1$, with a
limiter applied after every stage. The authors present a practical
generalized slope limiter as the main contribution: a TVB-corrected minmod
on the linear part, applied in local characteristic variables, on
rectangles and on triangles, with the higher-order part discarded only
where the linear part is limited. They call it simpler than, and better in
practice than, the theoretically justified limiter of part IV. In the
double Mach reflection, $P^2$ on a mesh half as fine per direction matches
$P^1$ at the Mach stems, for about 2.1 times less CPU time; triangles and
rectangles perform alike. Merged into the new
[RKDG](/methods/rkdg.md) page.

# Key claims

1. **Scheme** (§2.1, eqs. 2.1–2.4). The approximation space is the set
   of functions that are polynomials of degree $K$ in each element. The
   weak form is discretized with an edge quadrature (2.2) and a volume
   quadrature (2.3). The flux normal to an edge is replaced by a numerical
   flux $\hat f(a, b)$: two-point, Lipschitz, consistent, conservative,
   monotone in the scalar case, an exact or approximate Riemann solver for
   systems. Initial data are the $L^2$ projection.
2. **Lax–Friedrichs flux** (eq. 2.5, §3.1).
   $\hat f(a, b) = \tfrac12\left[\mathbf f(a)\cdot\mathbf n + \mathbf f(b)\cdot\mathbf n - \alpha_{i+1/2}(b - a)\right]$,
   with $\alpha_{i+1/2}$ an estimate of the largest absolute eigenvalue of
   the normal Jacobian near the edge. Local recipe (triangles; rectangles
   in Examples 4.1–4.2): the larger of its values at the means of the two
   elements sharing the edge. Global recipe (rectangles, Example 4.3): the
   maximum over the grid line; more dissipative but more robust,
   "especially for problems involving low velocities and low
   density/pressure near wall boundaries".
3. **Accuracy and quadrature** (§§2.1, 3.2, citing part II, Prop. 2.1).
   The DG approximation of $\nabla\cdot\mathbf f(u)$ is of order $K + 1$
   if the edge quadrature is exact for degree $2K + 1$ and the volume
   quadrature for degree $2K$. With $K = 0$ and an edge rule exact for
   constants the scheme is a monotone finite-volume scheme (scalar case):
   DG is "a high-order accurate extension of finite volume, monotone
   schemes".
4. **Time stepping** (§2.2, Table 1, read from the page image). Shu–Osher
   form with $\mathcal L$ including boundary data at stage times
   $t^n + \mathsf c\,\Delta t$. Order 2: $a_{10} = 1$, $b_{10} = 1$;
   $a_{20} = a_{21} = \tfrac12$, $b_{20} = 0$, $b_{21} = \tfrac12$; stage
   times $0, 1$. Order 3: $a_{10} = b_{10} = 1$;
   $a_{20} = \tfrac34$, $a_{21} = \tfrac14$, $b_{21} = \tfrac14$;
   $a_{30} = \tfrac13$, $a_{32} = \tfrac23$, $b_{32} = \tfrac23$; stage
   times $0, 1, \tfrac12$. Both have $\max b_{ik}/a_{ik} = 1$, i.e.
   $\mathcal C = 1$; RK2 is used with $P^1$, RK3 with $P^2$. The mass
   matrix is block diagonal (diagonal for a locally orthogonal basis).
5. **Limiter in the time loop** (§2.3). The limiting operator is applied
   to the initial projection and to every Runge–Kutta stage.
6. **Limiting only the linear part** (§2.3). Stated as an assumption,
   whose justification is "still an open problem": spurious oscillations
   are present in the solution only if present in its $P^1$ part (its
   $L^2$ projection on degree 1). If the limiter leaves the $P^1$ part
   unchanged, nothing is limited and the higher moments are kept;
   otherwise the higher-order part is discarded and the limited $P^1$ part
   is used. The limiter therefore need only be defined on degree 1.
7. **Required limiter properties** (§3.4). (1) Accuracy: a linear function
   is unchanged. (2) Conservation: the element mean is unchanged. (3) Slope
   limiting: the gradient is not increased.
8. **Rectangles: TVB minmod** (§3.4.1, eqs. 3.3–3.7, read from the page
   image). For the $P^1$ part, with mean $\bar u_{i,j}$ and linear
   moments $\hat u^{(10)}_{i,j}$, $\hat u^{(01)}_{i,j}$ (scaled Legendre
   basis), the face deviation $\tfrac12\hat u^{(10)}_{i,j}$ is replaced by
   $\operatorname{minmod}_M\left(\tfrac12\hat u^{(10)}_{i,j},\ \bar u_{i+1,j} - \bar u_{i,j},\ \bar u_{i,j} - \bar u_{i-1,j}\right)$
   with threshold $M h_x^2$, and likewise in $y$. The correction avoids
   limiting at smooth extrema, where the slopes are $O(h^2)$. An estimate
   of $M$ from second derivatives is in part II; "Usually, the numerical
   results are not sensitive to the choice of M in a large range. In all
   the calculations in this paper we take M to be 50."
9. **Characteristic limiting** (§3.4.1). For systems, the slope and the
   two mean differences are multiplied by $L$, the left eigenvectors of
   the $x$-Jacobian at the element mean, limited componentwise, and
   multiplied back by $R$; likewise in $y$. On triangles the Jacobian is
   taken in the direction from the barycentre to each edge midpoint.
10. **Triangles** (§3.4.2, Fig. 3.1, read from the page image). For each
    edge midpoint, the deviation of the solution there from the element
    mean is compared, through $\operatorname{minmod}_M$, with a factor
    greater than 1 (1.5 in the runs) times a combination of the mean
    differences to two neighbours. Its coefficients are geometric: the
    nonnegative coefficients that write the vector from the element's
    barycentre to the edge midpoint as a combination of the vectors to the
    two neighbours' barycentres. If the three limited deviations sum to zero they
    define the limited $P^1$ function in the edge-midpoint nodal basis.
    Otherwise the positive ones are scaled by $\min(1, N/P)$ and the
    negative ones by $\min(1, P/N)$, with $P$ and $N$ the sums of the
    positive parts and of the absolute negative parts, so the result sums
    to zero, which is conservation in that basis. Properties 1–3 are
    called "very easy to see".
11. **Quadrature and bases** (§§3.2–3.3). Rectangles: 2-point Gauss on
    edges for $P^1$, 3-point for $P^2$; a $P^1$ interior rule reusing the
    8 edge Gauss points plus the centre; $3\times3$ tensor Gauss for
    $P^2$; orthogonal scaled-Legendre basis, diagonal mass matrices.
    Triangles: the same edge rules; the three edge midpoints for the $P^1$
    interior, a 7-point rule exact for degree 5 for $P^2$; $P^1$ nodal at
    edge midpoints (diagonal mass matrix), $P^2$ nodal at midpoints and
    vertices (full mass matrix).
12. **CFL** (§4). $\nu = 0.3$ for $P^1$ and $0.18$ for $P^2$, against
    the 1D von Neumann limits $1/3$ and $1/5$ (part II). On rectangles the
    Courant number is the maximum of
    $\left[(\vert v_x\vert + c)/h_x + (\vert v_y\vert + c)/h_y\right]\Delta t$
    at local means; on triangles the more conservative
    $\max(\vert\mathbf v\vert + c)\,\vert\partial\mathcal T\vert\,\Delta t/\vert\mathcal T\vert$
    with the perimeter $\vert\partial\mathcal T\vert$.
13. **Positivity corrections** (§4, Examples 4.2–4.3, read from the page
    images). Triangles: negative density or total energy at an edge
    midpoint is brought to $10^{-10}$ by further limiting "in a
    conservative way" (no formula printed). Rectangles, $P^1$: if
    $\bar u - \tfrac12\left(\vert\hat u^{(10)}\vert + \vert\hat u^{(01)}\vert\right) < \tfrac12\bar u$,
    for density or total energy separately, both slopes are scaled so
    that the left side equals $\tfrac12\bar u$; momenta are unchanged.
    Rectangles, $P^2$: if
    $\bar u - \tfrac12\left(\vert\hat u^{(10)}\vert + \vert\hat u^{(01)}\vert\right) - \tfrac14\vert\hat u^{(11)}\vert - \tfrac16\left(\vert\hat u^{(20)}\vert + \vert\hat u^{(02)}\vert\right) < 0$
    for density or total energy, all higher moments of all four components
    are scaled by the smaller of the two factors that make it zero
    (registry translation of the printed criteria, compiler's). Claimed
    conservative and not degrading formal accuracy, without proof.
14. **Conclusions** (§5). For fine flow features a higher-order method
    gives better CPU performance at equal resolution; triangles and
    rectangles perform similarly.
15. **The series** (§1). Part I: 1D, $P^1$, TVDM. Part II: general $K$,
    TVBM, formally of order $K + 1$. Part III: 1D systems. Part IV:
    multi-D scalar, a local maximum principle on fairly general
    triangulations independent of $K$. Jiang & Shu: a cell entropy
    inequality for the square entropy, any order and triangulation,
    semidiscrete, without limiters, implying $L^2$ stability.

# Tests

All 2D Euler; $\gamma$ is not printed. $P^1$ with RK2, $P^2$ with RK3,
$M = 50$. No convergence-order test is presented; the order $K + 1$ rests
on the earlier parts.

1. **Double Mach reflection** (Example 4.1, Figs. 4.1–4.3). Woodward and
   Colella's set-up on $[0, 4]\times[0, 1]$ to $t = 0.2$, rectangles,
   local Lax–Friedrichs; meshes $240\times60$ to $1920\times480$
   ($h = 1/60$ to $1/480$); 30 density contours from 1.3965 to 22.682. No
   significant $P^1$/$P^2$ difference in whole-domain plots. At the Mach
   stems, $P^2$ at $h = 1/240$ has qualitatively the resolution of $P^1$
   at $h = 1/480$, and $P^2$ at $1/480$ is much better than $P^1$ at
   $1/480$. Half the mesh per direction is 8 times fewer space–time cells
   in 2D; the net CPU saving is about 2.1, "even more significant for 3D"
   ([double Mach reflection](/benchmarks/double-mach-reflection.md)).
2. **Forward-facing step** (Example 4.2, Figs. 4.4–4.10). Mach 3, tunnel
   1 wide and 3 long, step 0.2 high at 0.6, $t = 4$; **no modification
   near the corner**, which is known to cause an erroneous entropy layer
   and a spurious Mach stem on the downstream bottom wall, decreasing with
   refinement. Rectangles, $h = 1/40$ to $1/320$, local Lax–Friedrichs;
   30 density contours from 0.090338 to 6.2365. $P^2$ improves on $P^1$,
   especially the slip line from the triple point. Triangles with corner
   refinement (near-corner to far size ratio 1, 1/2, 1/4, 1/8): strong
   spurious entropy production at the corner pollutes the downstream flow
   and decreases with corner refinement; triangles match rectangles of
   about the same density but needed the positivity correction
   ([forward-facing step](/benchmarks/forward-facing-step.md)).
3. **Shock diffraction at a backward-facing corner** (Example 4.3, Figs.
   4.11–4.12). Mach 5.09 shock at $x = 0.5$, $6 \le y \le 11$, into
   $\rho = 1.4$, $p = 1$; inflow at $x = 0$, outflow at $x = 13$,
   reflecting walls along the step, **Neumann** conditions at the bottom
   ($1 \le x \le 13$, $y = 0$) and top ($y = 11$); no corner treatment;
   $t = 2.3$; rectangles $h = 1/10$ to $1/80$, global Lax–Friedrichs; 20
   contours from 0.066227 to 7.0668. "It is easy to get negative density
   and/or pressure"; the positivity correction was needed for $P^1$ and
   $P^2$. No quantitative comparison
   ([shock diffraction](/benchmarks/shock-diffraction.md)).

# Notation map

| Cockburn & Shu (1998) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $f(u) = (f_1,\dots,f_d)$, $\mathrm{div}\,f$ | $u$, $\mathbf f(u)$, $\nabla\cdot\mathbf f$ | |
| $K$ (element), $\mathcal T_h$ | words ("element"); $\mathcal T$ for a triangle | **collision**: registry $K$ is the polynomial degree |
| $k$, $P^k$ | $K$, $P^K$ | $P^K$ registered at the 2026-10-13 deep lint |
| $u_h$, $V_h$, $u^1_h$ | $\mathcal P_i$; words (DG space, $P^1$ part) | |
| $\bar u_{ij}$, $\bar u_K$ | $\bar u_{i,j}$ | |
| $u_x$, $u_y$ (coefficients of $(x - x_i)/(\Delta x_i/2)$) | $\tfrac12\hat u^{(10)}$, $\tfrac12\hat u^{(01)}$ | the face deviation from the mean |
| $u_{xy}$, $u_{xx}$, $u_{yy}$ | $\tfrac14\hat u^{(11)}$, $\tfrac14\hat u^{(20)}$, $\tfrac14\hat u^{(02)}$ | $\phi^2 - \tfrac13 = 4P_2(\zeta)$ |
| $\Delta x_i$, $\Delta y_j$ | $h_x$, $h_y$ | |
| $h_{e,K}(a, b)$ | $\hat f(a, b)$ | **collision**: registry $h$ is the spacing |
| $\alpha_{e,K}$ | $\alpha_{i+1/2}$ (local), $\alpha$ (global) | |
| $n_{e,K}$ | $\mathbf n$ | |
| $\omega_l$, $x_{el}$, $\omega_j$, $x_{Kj}$ | $w_G$, $x_G$ | **collision**: nonlinear weights $\omega_k$ |
| $L_h(u_h, \gamma_h)$ | $\mathcal L(u)$ | |
| $\gamma_h$ (boundary data) | $g(t)$ | **collision**: ratio of specific heats $\gamma$ |
| $\alpha_{il}$, $\beta_{il}$ | $a_{ik}$, $b_{ik}$ | **collisions**: $\alpha$, $\beta_k$ |
| $d_l$ | $\mathsf c_i$ (stage time fraction) | **collision**: linear weights $d_k$ |
| $\Lambda\Pi_h$ | words ("the limiter") | **collisions**: $\Lambda$, $\Pi$ |
| $\bar m$, $m$, $M$ | $\operatorname{minmod}_M$, $\operatorname{minmod}$, $M$ | |
| $R$, $R^{-1}$, $\Lambda$ | $R$, $L$, $\Lambda$ | |
| $m_i$, $b_i$, $K_0,\dots,K_3$ | words (edge midpoints, barycentres, neighbours) | $m_i$ collides with the system size $m$ |
| $\alpha_1$, $\alpha_2$; $\nu = 1.5$; $\theta^\pm$, pos, neg | words | collide with $\alpha$, CFL $\nu$, limiter $\theta$ |
| $\Delta_i$, $\hat\Delta_i$ | words | collide with the PPM jump $\Delta u_i$ |
| $\varphi_i$, $\xi_i$ (nodal bases), $S$, $M$ (mass matrices) | words | collide with $\phi_i$, $\xi$, $S$, the TVB $M$ |
| CFL | $\nu$ | |
| $\sigma$ (corner size ratio) | words | collides with the flux-limiter $\sigma$ |
| Mach 10, 5.09 | $M_s$ | |

# Pages created or updated

* Created [Runge–Kutta discontinuous Galerkin method (RKDG)](/methods/rkdg.md).
* Updated [WENO limiters for DG](/methods/weno-limited-dg.md) (batch-16
  block: the multi-D TVB limiter at its source, characteristic limiting,
  the $P^1$-part rule, triangles, the choice of $M$).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md)
  (batch-16 block: the DG runs, and the $P^2$/$P^1$ mesh factor as
  Cockburn and Shu state it).
* Updated [TVD / SSP Runge–Kutta methods](/methods/ssp-runge-kutta.md)
  (batch-16 block: RK order $K + 1$, limiter after every stage, boundary
  data at stage times).
* Updated [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md) (batch-16 block: RKDG without corner treatment, Example 4.2).
* Updated [Shock diffraction at a backward-facing corner](/benchmarks/shock-diffraction.md) (batch-16 block: the DG runs, Example 4.3).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1998-JCP-Cockburn-101006jcph19985892.pdf`.
   * **Version read.** The publisher's typeset journal version, 26 pages
     (pp. 199–224), Article No. CP985892; received May 30, 1997, revised
     December 9, 1997.
   * **Identity.** doi:10.1006/jcph.1998.5892, checked on Crossref: "The
     Runge–Kutta Discontinuous Galerkin Method for Conservation Laws V",
     J. Comput. Phys. 141(2):199–224, April 1998, authors Cockburn and
     Shu, reference count 37. Page 1 adds "— Multidimensional Systems".
   * **How it was read.** Text layer for prose; Table 1, eqs. 3.6–3.7, the
     triangular limiter (pp. 209–210) and the positivity criteria
     (pp. 219–220) from rendered page images (pp. 204, 209, 210, 219,
     220).
   * **Recorded as printed.**
     - $\gamma$ is not printed for any test.
     - The triangle positivity correction is described ("further limiting
       … in a conservative way") without a formula.
     - The $P^2$ triangle mass matrix is printed (§3.3.2) but not
       reproduced here.
     - Results are contour plots only: no error tables and no
       convergence-order test.
   * **Reference list:** 37 entries, all merged. The LDG paper ("to
     appear", no year) is `cockburn-1998-c`, a suffix because its citing
     date collides with this source's slug. Atkins & Shu's ICASE report is
     merged into `atkins-1998-b`; Bassi & Rebay ("J. Comput. Phys., to
     appear") into `bassi-1997-b`; Lowrie, Roe & van Leer's preprint
     ("Space-time discontinuous Galerkin: I") is `lowrie-1998-b`, distinct
     from `lowrie-1998`. The two Shu 1988 works were keyed in printed order
     and swapped by vol:page (SIAM J. Sci. Stat. Comput. 9:1073 →
     `shu-1988-b`, J. Comput. Phys. 77:439 → `shu-1988`). Berger &
     Colella, printed "M. Berger and A. Colella", is `berger-1989` by
     vol:page. Ref. 19 prints the title "High-order accurate discontinuous
     discontinuous finite element solution of the 2D Euler equations" and
     ref. 30 "A construction to the great Riemann solver debate" (Quirk,
     `quirk-1994`); both recorded as printed. Bibliography: 3184 entries.
