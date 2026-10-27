---
type: Source
title: "Zheng et al. (2022) — A fourth-order conservative semi-Lagrangian finite volume WENO scheme without operator splitting for kinetic and fluid simulations"
description: "Fourth-order, mass-conservative, positivity-preserving semi-Lagrangian finite-volume scheme without dimensional splitting, built on cubic-curved upstream cells and a two-dimensional WENO-ZQ reconstruction, applied to Vlasov models and two-dimensional incompressible Euler flow; no turbulence-modelling content."
resource: "doi:10.1016/j.cma.2022.114973"
source_kind: paper
authors: [Zheng N., Cai X., Qiu J.M., Qiu J.]
year: 2022
venue: "Comput. Methods Appl. Mech. Eng. 395:114973"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Zheng_A_fourth-order_conservative_semi-Lagrangian_finite_volume_WE.pdf"
tags: [weno, semi-lagrangian, finite-volume, vlasov]
timestamp: 2026-10-27T15:53:00Z
---

# Summary

Zheng et al. (2022) build a fourth-order semi-Lagrangian (SL)
finite-volume scheme for two-dimensional linear transport without operator
splitting. Through a fourth-order commutator-free Runge–Kutta exponential
integrator, they extend it to transport whose velocity depends on the
solution. The paper has no turbulence-modelling content: no closure, no LES
or RANS, no turbulence statistics. It enters this bundle only through its
[WENO](/methods/weno-scheme.md) reconstruction.

The new cell average equals the integral of the old solution over the
upstream cell, found by tracing characteristics back over one step. The
upstream cell is approximated by a quadrilateral with cubic edges, each
through the feet of four Gauss–Lobatto points per Eulerian edge. A truly
two-dimensional WENO-ZQ reconstruction gives a cubic polynomial in every
cell. It combines one cubic polynomial on a 13-cell stencil with four
linear ones, with fixed positive linear weights. The curved cell is clipped
against the mesh, and Green's theorem turns each area integral into line
integrals. A Zhang–Shu limiter, using the exact cell minimum, preserves
positivity.

The authors prove mass conservation, positivity (for exact line integrals)
and a fourth-order local truncation error. Unconditional $L^2$ stability
for constant coefficients and the linear reconstruction is checked by
sampling the amplification factor. Against their earlier splitting scheme,
the new scheme keeps fourth order where splitting falls to first order
(guiding-center Kelvin–Helmholtz). It is more accurate per mesh on swirling
deformation and Landau damping, but costs more CPU time on the
constant-coefficient and Landau tests. On the two-dimensional
incompressible Euler vortex patch and double shear layer it preserves
energy and enstrophy better. CFL numbers up to 10.2 are used.

# Version read

Version of record (Elsevier, received 2 February 2022, online 27 April
2022); 28 pages, all read, with the equation pages checked visually. Page 1
matches Crossref.

# Key claims

1. Splitting-based SL schemes multiply subproblems in several dimensions and, without extra step limits or modified splitting, fall to first order on strongly nonlinear problems such as the guiding-center Vlasov model (§1). **Stated**
2. A non-splitting SL finite-difference scheme can lose mass significantly; the mass-conservative non-splitting SL finite-difference scheme of Xiong, Russo & Qiu needs an extra time-step restriction (§1). **Stated**
3. The SL finite-volume update (new average = average of the old solution over the upstream cell) follows exactly from the Reynolds transport theorem (§2, Eqs. 4–5). **Derived**
4. Upstream cells are approximated by cubic-curved quadrilaterals: four Gauss–Lobatto points per Eulerian edge are traced back with fourth-order Runge–Kutta, and a parametric cubic is interpolated through the feet (§2.1, App. A). **Derived**
5. WENO-JS-type reconstructions cannot be used because SL schemes need values at arbitrary points; WENO-ZQ gives a full cubic polynomial per cell, fourth order where smooth and degrading to lower order near discontinuities (§1, §2.2). **Stated**
6. WENO-ZQ parameters: $\epsilon_W=10^{-14}$, linear weights $d_0=0.8$, $d_1=\dots=d_4=0.05$ (§2.2). **Stated**
7. Area integrals over the clipped curved polygons become line integrals by Green's theorem with auxiliary functions $\tilde P$, $\tilde Q$ (Eqs. 18–20); three-point Gauss–Legendre quadrature is exact on mesh-line segments and sixth-order accurate on cubic-curve segments (§2.3.2, Eqs. 17–21). **Stated**
8. Taking the minimum of the reconstruction at Gauss–Legendre points does not suffice for positivity here; the exact cell minimum is found from the critical points, an intersection of conic sections (§2.3.3, Remark 2.1). **Stated** (from numerical tests, no data printed)
9. Proposition 3.1: mass conservation with periodic boundary conditions (§3, Eq. 25). **Proved**
10. Proposition 3.2: with the limiter the scheme preserves positivity if the line integrals are exact (§3). **Proved**
11. Lemmas 3.3–3.5: for $C^4$ velocity and $\Delta t\sim\Delta x\sim\Delta y$, the exact upstream edges are smooth and close to straight mesh-aligned edges (§3, Eqs. 26–40). **Proved**
12. Proposition 3.6: the local error of the updated average is $O(h^4)$ for exact input averages and $C^4$ data (reconstruction $O(h^4)$, quadrature $O(h^6)$, area mismatch of the cubic-curved cell $O(h^6)$); the Runge–Kutta error of the characteristic feet is declared non-dominant (Remark 3.8) (§3, Eqs. 41–47). **Proved**
13. Proposition 3.9: for constant coefficients, periodic boundaries and the linear reconstruction the update is unconditionally $L^2$ stable; $|A|\le1$ is checked on 1000 uniform samples per variable, and the amplification factor $A$ is not written out (§3, App. C). **Shown**
14. Constant-coefficient transport ($T=2$, CFL 10.2): non-splitting $L^2$ errors 1.58E−04 to 3.22E−09 from $40^2$ to $320^2$ (orders 7.55, 4.03, 4.00); splitting 2.23E−05 to 5.43E−11 (orders 6.99, 6.49, 5.17); splitting is "much more efficient" (§4.1, Table 1, Fig. 6). **Shown**
15. Swirling deformation ($T=1.5$): the non-splitting scheme is more accurate per mesh with CPU efficiency "very close" to splitting; the text says fourth order, and Table 2 prints orders 3.47–3.71 up to $1280^2$, then 9.66 and 4.50; temporal order four for both at large CFL (§4.1, Table 2, Fig. 7). **Shown**
16. Swirling deformation with discontinuous data: complex structure captured, positivity kept (§4.1, Figs. 8–10). **Shown**
17. Strong Landau damping ($T=2$, CFL 10.2): non-splitting orders 3.67, 3.98, 4.68, 4.19 ($16^2$ to $256^2$), more accurate per mesh than splitting (2.08, 3.77, 4.53, 3.65), but splitting is more efficient in CPU time (§4.2, Table 4, Fig. 11). **Shown**
18. Weak and strong Landau damping: relative deviations of mass and $L^1$ norm around $10^{-13}$; other invariants are not exactly preserved (§4.2, Fig. 13). **Shown**
19. Guiding-center Kelvin–Helmholtz ($T=5$): non-splitting orders 3.73, 4.66, 4.49, 7.22, 5.14 ($16^2$ to $512^2$), splitting 0.88–0.99; non-splitting "much more efficient"; temporal order four against one (§4.3, Table 5, Fig. 15). **Shown**
20. At $T=40$ the splitting scheme deviates significantly from the reference at CFL 1, while at CFL 0.1 it resembles the non-splitting result at CFL 1 and 10.2 (§4.3, Figs. 16–17). **Shown**
21. Both schemes conserve mass to about $10^{-13}$ on the guiding-center model; the non-splitting scheme preserves energy and enstrophy better (§4.3, Fig. 18). **Shown**
22. Two-dimensional incompressible Euler, vortex patch ($T=10$) and double shear layer ($T=8$), $256^2$, CFL 10.2: non-oscillatory solutions comparable to earlier work; non-splitting preserves energy and enstrophy better (§4.4, Figs. 19–21). **Shown**
23. The scheme is mass conservative, positivity preserving, unconditionally stable in the linearized setting and fourth order in space and time (§5). **Stated**
24. Floating-point truncation can misplace an intersection near a curve end close to a mesh line, or misindex outer segments when a cubic nearly overlaps a mesh line; both "cause chaos" in the integration, and no standard remedy is given (App. B.3). **Stated**

The WENO-ZQ weights (Eqs. 13–15), in the symbols of the
[WENO](/methods/weno-scheme.md) page and registry §11, with
$\mathrm{IS}_0$ the smoothness indicator of the cubic $q_0$,
$\mathrm{IS}_{1..4}$ those of the linear $q_k$, $d_k$ the linear and
$\mathsf w_k$ the nonlinear weights, and $\mathrm{IS}_{\mathrm G}$ the
global indicator:

$$\mathrm{IS}_{\mathrm G}=\Big(\frac14\sum_{k=1}^4\big|\mathrm{IS}_0-\mathrm{IS}_k\big|\Big)^2,\qquad \mathsf w_k=\frac{d_k\big(1+\mathrm{IS}_{\mathrm G}/(\mathrm{IS}_k+\epsilon_W)\big)}{\sum_ld_l\big(1+\mathrm{IS}_{\mathrm G}/(\mathrm{IS}_l+\epsilon_W)\big)},$$

$$\tilde u_s=\frac{\mathsf w_0}{d_0}\Big(q_0-\sum_{k=1}^4d_kq_k\Big)+\sum_{k=1}^4\mathsf w_kq_k .$$

# Printed slips

- Table 5 caption: "at T = 5 with CFL = 1"; the text of Example 4.6: "at T = 5 with CFL = 10.2".
- App. C prints "$\kappa_2=\frac{b\Delta t}{\Delta x}$", while (C.1) shifts by $\kappa_2\Delta y$.
- Eq. (23) prints $\theta_{i,j}:=\min\{|\bar u^n_{ij}/(\bar u^n_{ij}-m_{ij})|\}$, a minimum over a single element.
- After Eq. (23): "one has to find the extreme points of $R^{(i,j)}(x,y)$"; $R^{(i,j)}$ is not defined, and Eq. (24) is written for $\tilde u^{(i,j)}$.
- Eq. (15) prints $q_0(x)$ for $q_0(x,y)$; Eq. (12) writes the derivative order $\partial^{|l_1+l_2|}$; Example 4.6 writes the initial condition for $u$ though the model is in $\rho$.
- Remark 2.1: "we can not only compute the minimum value … at the corresponding Gauss–Legendre points".
- Refs. [1] and [23] are the same paper (Lauritzen, Nair & Ullrich 2010); ref. [21] prints no volume or pages.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u(x,y,t)$ | $u_s$ (transported scalar, page-local) | **collision** with the velocity $u$ |
| $(a,b)$ | (advecting velocity, page-local) | |
| $\Delta x$, $\Delta y$, $h$ | $\Delta x$, $\Delta y$, $h$ | $h\sim\Delta x\sim\Delta y\sim\Delta t$ |
| $\Delta$ (Laplacian, Eqs. 60, 64) | $\nabla^2$ | **collision** with the filter width |
| $\mu_i$, $\nu_j$ | (scaled cell coordinates, page-local) | **collision** with $\mu$, $\nu$ (viscosities) |
| $\xi$ | $\xi$ (curve parameter) | also wavenumbers $\xi_1$, $\xi_2$ in App. C |
| $\beta_k$, $\tau$ | $\mathrm{IS}_k$, $\mathrm{IS}_{\mathrm G}$ (smoothness indicators, registry §11 and the WENO page) | **collision** with $\beta(\boldsymbol x)$ and $\tau_{ij}$ |
| $\gamma_k$, $\omega_k$, $\epsilon$ | $d_k$, $\mathsf w_k$, $\epsilon_W$ (linear and nonlinear weights, registry §11; small number, page-local) | **collision** with $\gamma$ and $\omega$ |
| $\tilde u^{(i,j)}$ | $\tilde u_s$ (cell reconstruction, page-local) | **collision:** not a Favre filter |
| $\theta_{i,j}$, $m_{ij}$ | (limiter factor, cell minimum, page-local) | |
| $\kappa_1$, $\kappa_2$, $A$ | (directional Courant numbers, amplification factor, page-local) | **collision** with $\kappa$ (von Kármán constant) |
| $f$, $E$, $\phi$, $\rho$ | (distribution function, electric field, potential, charge density, page-local) | **collision** with $E$ (total energy) and $\rho$ (density) |
| $\omega$, $\psi$, $\mathbf u$ | (scalar vorticity, stream function, velocity of 2-D Euler) | |

# Reference list

39 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Refs. [1] and
[23] are a printed duplicate (Lauritzen et al. 2010) and are one entry. Two
Qiu & Shu 2011 papers ([13], [17]) are keyed in printed order. Ref. [21]
prints no volume or pages. All items parsed.

# Pages created or updated

Chunk 7 (2026-10-26). This source is cited on:

- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
