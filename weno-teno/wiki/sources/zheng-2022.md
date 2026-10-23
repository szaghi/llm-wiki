---
type: Source
title: "Zheng et al. (2022) — A fourth-order conservative semi-Lagrangian finite volume WENO scheme without operator splitting for kinetic and fluid simulations"
description: "Fourth-order, mass-conservative, positivity-preserving 2D semi-Lagrangian finite-volume scheme without dimensional splitting: cubic-curved upstream cells, a 13-cell WENO-ZQ polynomial reconstruction, clipping with Green line integrals and a CF4 exponential integrator, applied to Vlasov–Poisson, guiding-center and incompressible Euler flows."
resource: "doi:10.1016/j.cma.2022.114973"
source_kind: paper
authors: [Zheng N., Cai X., Qiu J.-M., Qiu J.]
year: 2022
venue: "Comput. Methods Appl. Mech. Eng. 395:114973"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Zheng_A_fourth-order_conservative_semi-Lagrangian_finite_volume_WE.pdf"
tags: [semi-lagrangian, finite-volume, weno, cweno, positivity]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

The paper builds a fourth-order, mass-conservative
[semi-Lagrangian finite-volume WENO scheme](/methods/semi-lagrangian-finite-volume.md)
for 2D linear transport $\partial_tu+\partial_x(v_1u)+\partial_y(v_2u)=0$, without
operator (dimensional) splitting. It is applied to nonlinear kinetic and fluid
models: the 1D1V Vlasov–Poisson system, the guiding-center Vlasov model, and the
2D incompressible Euler equations in vorticity–stream-function form.

The update is an exact identity (Reynolds' transport theorem): the cell average at
$t^{n+1}$ equals the integral of $u(\cdot,t^n)$ over the upstream cell, the
characteristic foot of the Eulerian cell, divided by the cell area. Three
ingredients make this fourth order. (i) Each upstream cell is approximated by a
cubic-curved quadrilateral. Its edges are parametric cubics through the feet of
the four Gauss–Lobatto points of each Eulerian edge, traced back by RK4. (ii) A
2D cell-average WENO-ZQ reconstruction (after Zhu and Qiu) recovers a full
$\mathbb P^3$ polynomial per cell from a 13-cell stencil. It blends this
polynomial nonlinearly with four $\mathbb P^1$ polynomials in
[CWENO](/methods/cweno.md) form, with linear weights $d_0=0.8$,
$d_{1..4}=0.05$, [smoothness indicators](/definitions/smoothness-indicator.md) and
[WENO-Z](/methods/weno-z.md)-type weights. Classical
[WENO-JS](/methods/weno-js-reconstruction.md) is ruled out because it gives values
only at fixed points. (iii) A clipping algorithm cuts the upstream cell by the
Eulerian mesh, and the integrals are evaluated as line integrals by Green's
theorem. A [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
gives [positivity](/properties/bound-preservation.md), with the polynomial
minimum found exactly. For solution-dependent velocities the step sits inside the
fourth-order commutator-free exponential integrator CF4.

The analysis gives mass conservation and positivity (with exact line integrals), a
one-step error $O(h^4)$, and $L^2$ stability for constant coefficients with linear
reconstruction. The stability bound is checked by sampling the amplification
factor, not proved analytically. Mass conservation comes from the remap identity,
not from a flux form ([local conservation](/results/local-conservation-flux-form.md)).
The tests run at CFL 10.2 against the authors' fourth-order dimensionally split
scheme. The split scheme is better on constant-coefficient transport and cheaper on
Landau damping. On the guiding-center
[Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md) it
drops to first order, while the non-split scheme keeps fourth order.

# Version read

Version of record (Elsevier typeset, CMAME 395:114973; received 2 Feb 2022,
accepted 5 Apr 2022, online 27 Apr 2022). It has 28 pages, all read; pp. 5–8,
15–16 and 26 were checked visually for the WENO-ZQ formulas, the positivity
limiter, the CF4 tableau and the stability proof. Page 1 matches Crossref (title,
authors, venue, DOI). Equation, table and figure numbers are those of this version.

# Key claims

Registry notation: the source's velocity $(a,b)$ becomes $(v_1,v_2)$, its linear
weights $\gamma_k$ become $d_k$, its high-order polynomial $q_0$ and its candidates $q_k$
become $P_{\mathrm{opt}}$ and $P_k$, as on the [CWENO](/methods/cweno.md) page, and its CFL
number becomes $\nu$; $h\sim\Delta x\sim\Delta y\sim\Delta t$
(see the Notation map).

1. Splitting-based semi-Lagrangian schemes in multi-D need many subproblems, especially with fourth-order splitting. Without a time-step restriction or a modified splitting, "the accuracy of the splitting-based schemes decays to first order for some strongly nonlinear problems such as the guiding center Vlasov model" (§1, citing [19]). **Stated** (and shown in Table 5)
2. Semi-Lagrangian finite-difference schemes that interpolate point values "may lead to significant loss of total mass", and the conservative non-split semi-Lagrangian finite-difference scheme of [21] needs an extra time-step restriction for stability (§1). **Stated**
3. Classical WENO-JS cannot serve a semi-Lagrangian scheme, which needs reconstructed values "at any spatial position", while WENO-JS gives values only at specific points. WENO-ZQ, with positive linear weights summing to one, gives a full $\mathbb P^3$ polynomial per cell (§1, §2.2). **Stated**
4. The update is the exact identity $\frac{1}{\Delta x_i\Delta y_j}\iint_{I_{i,j}}u(x,y,t^{n+1})\,dx\,dy=\frac{1}{\Delta x_i\Delta y_j}\iint_{I^\star_{i,j}}u(x,y,t^n)\,dx\,dy$, from Reynolds' transport theorem (§2, (4)–(5)). **Derived**
5. Upstream cells are cubic-curved quadrilaterals: four Gauss–Lobatto points per Eulerian edge are traced back to $t^n$ by RK4 on the characteristic equations (3), and each edge is the parametric cubic through their feet (§2.1, (6), App. A). **Stated** (construction)
6. WENO-ZQ is fourth order in smooth regions and "automatically decays to a lower order polynomial reconstruction" at discontinuities, in "a similar spirit with p-adaptive DG methods" (§1, §2.2). **Stated**; oscillation-free results **Shown** (Figs. 9–10, 19)
7. The reconstruction reproduces the cell average, $a_1^{(i,j)}=\bar u^n_{i,j}$ (16), which the proof of Prop. 3.1 uses. **Derived**
8. Three-point Gauss–Legendre quadrature of the Green line integrals is exact on inner segments (straight mesh lines, polynomial integrand of degree at most 4) and "of sixth-order accuracy" on outer, cubic-curved segments (§2.3.2). **Stated**
9. Prop. 3.1 (mass conservation): with periodic boundaries the scheme conserves total mass, because the inner-segment integrals are exact and cancel and the reconstruction is conservative ((25)). **Proved**
10. Prop. 3.2 (positivity): with the limiter of §2.3.3 the scheme preserves positivity "if the line integrals in (17) are exactly evaluated". **Proved** (short argument; conditional on exact quadrature)
11. Remark 2.1: for the positivity limiter the polynomial minimum $m_{ij}$ cannot be taken at Gauss–Legendre points only, as in Zhang and Shu's survey, because the integration uses Green's formula. It is found by solving $\partial_x\tilde u^{(i,j)}=\partial_y\tilde u^{(i,j)}=0$, two quadratics, that is, by intersecting conic sections ((24)). **Shown** ("our numerical test"; no data printed)
12. Lemmas 3.3–3.5: for $v_1,v_2\in C^4$ and $\Delta t\sim\Delta x\sim\Delta y$, the exact upstream image of an Eulerian edge satisfies $dX/d\alpha=1+O(\Delta t)$, $dY/d\alpha=O(\Delta t)$, and its higher derivatives (orders 2–4) are $O(\Delta t)$. In a frame aligned with the chord through its end feet it is a graph $y'=g(x')$ with $g^{(k)}=O(h)$, $k=1,\dots,4$ ((27)–(40)). **Proved**
13. Prop. 3.6 (error analysis): if the input cell averages are exact and $u,v_1,v_2\in C^4$, one step satisfies $\big\lvert\frac{1}{\Delta x\Delta y}\iint_{I_{i,j}}u(x,y,t^{n+1})\,dx\,dy-\bar u^{n+1}_{i,j}\big\rvert=O(h^4)$. The proof combines a reconstruction error $O(h^4)$ (referred to Zhu and Qiu), a quadrature error $O(h^6)$, $\lvert I^\star_{i,j}\rvert=O(h^2)$, and a symmetric-difference area $O(h^6)$ between exact and cubic upstream cells ((41)–(47)). The RK4 error of the feet is dismissed as "not dominant" (Remark 3.8, no proof). **Proved**. *(Compiler check, not in the sources)*: a one-step error $O(h^4)$ with $\Delta t\sim h$, accumulated over $O(1/h)$ steps, bounds the global error by $O(h^3)$ only; the global fourth order rests on the tables.
14. Remark 3.7: the exact upstream edges are "smooth curves close to vertical or horizontal straight edges", quantified by Lemmas 3.3 and 3.5. **Proved**
15. Prop. 3.9 ($L^2$ stability): with fourth-order *linear* reconstruction, the update is unconditionally stable for constant-coefficient transport with periodic boundaries. App. C reduces the Courant numbers to $0\le\nu_1,\nu_2\le1$ by integer shifts and checks $\lvert\mathsf A(\nu_1,\nu_2,\vartheta_1,\vartheta_2)\rvert\le1$ on 1000 uniform samples of each variable. The amplification factor is not printed ("extremely complicated"). **Shown** (a numerically checked von Neumann condition, labelled a proof by the authors)
16. Constant-coefficient transport (Ex. 4.1, Table 1, $T=2$, no temporal error): the non-split scheme is fourth order (rates 7.55, 4.03, 4.00 from $40^2$ to $320^2$; $L^2$ error $3.22\times10^{-9}$ on $320^2$). The split scheme is fifth order ($5.43\times10^{-11}$ on $320^2$) and "much more efficient" (Fig. 6). **Shown**
17. Swirling deformation flow (Ex. 4.2, Table 2, $t=1.5$): the non-split rates are 3.47–3.71 up to $1280^2$, then 9.66 and 4.50, and the text says "Fourth order accuracy is observed". The non-split scheme is more accurate than the split one on the same mesh up to $640^2$, with "very close" CPU efficiency (Fig. 7a). Both have fourth temporal order at large CFL numbers (Fig. 7b, $160^2$). **Shown**
18. Strong Landau damping (Ex. 4.3, Table 4, $T=2$, CFL 10.2): non-split rates 3.67, 3.98, 4.68, 4.19 ($2.90\times10^{-8}$ on $256^2$), more accurate than the split scheme on the same mesh; the split scheme is cheaper in CPU time (Fig. 11a). Both have fourth temporal order (Fig. 11b, $128^2$). **Shown**
19. The relative deviations of mass and $L^1$ norm are about $10^{-13}$ for weak and strong Landau damping (Fig. 13, $v_{\max}=10$), confirming conservation and positivity. Energy, entropy and the $L^p$ norms are not exactly preserved, "similar to the results in [5,24]" (data not shown). **Shown**
20. Guiding-center Kelvin–Helmholtz (Ex. 4.6, Table 5, $T=5$): non-split rates 3.73, 4.66, 4.49, 7.22, 5.14 ($8.89\times10^{-11}$ on $512^2$); the split scheme converges at first order (0.88–0.99). The non-split scheme is "much more efficient" (Fig. 15a), with temporal order four against one (Fig. 15b). **Shown**
21. Kelvin–Helmholtz at $T=40$: the non-split scheme at CFL 1 and 10.2 matches the literature; the split scheme agrees at CFL 0.1 but deviates significantly at CFL 1 (Figs. 16–17). **Shown**
22. At CFL 10.2, energy and enstrophy deviations are smaller for the non-split scheme on Kelvin–Helmholtz (Fig. 18), the vortex patch (Fig. 20) and the shear flow (Fig. 21); the mass deviation is about $10^{-13}$ for both schemes. **Shown**
23. The scheme is "mass conservative, Positivity-preserving, unconditionally stable under linearized settings, and fourth-order accurate in both space and time" (§5). **Stated** (summary of the above)

# Printed slips

- Refs. [1] and [23] are the same work (Lauritzen, Nair and Ullrich, CSLAM, J. Comput. Phys. 229 (2010) 1401–1424), printed twice.
- Eq. (12): the sums run over $l_1+l_2\le3$ (resp. $\le1$) and so include the zeroth-order term, the squared polynomial itself; Jiang–Shu-type indicators start at derivatives of order 1. The paper does not comment.
- Eq. (15): "$q_0(x)$" should be $q_0(x,y)$.
- Eq. (23): $\theta_{i,j}:=\min\{\lvert\bar u^n_{ij}/(\bar u^n_{ij}-m_{ij})\rvert\}$ has a single argument; the Zhang–Shu factor is $\min\{\lvert\cdot\rvert,1\}$.
- §2.3.3, after (23): "find the extreme points of $R^{(i,j)}(x,y)$"; $R^{(i,j)}$ is undefined, and $\tilde u^{(i,j)}$ is meant.
- Eq. (53) against Table 3 (CF4): (53) advances the fourth stage and both output exponentials by $\frac12\Delta t$. *(Compiler check, not in the sources)*: the velocity combinations of those three exponentials have coefficient sums $\frac12$ ($-\frac12+1$; $\frac14+\frac16+\frac16-\frac1{12}$; $-\frac1{12}+\frac16+\frac16+\frac14$). With $\frac12\Delta t$ a step would advance $\frac12\Delta t$ in total, and the fourth stage, started from the $t^n+\frac12\Delta t$ stage, would not reach $t^n+\Delta t$. The full $\Delta t$ is presumably meant in those three places.
- Table 5 caption: "at T = 5 with CFL = 1"; the text of Ex. 4.6 says CFL 10.2.
- App. C: "$\kappa_2=\frac{b\Delta t}{\Delta x}$" should have $\Delta y$ (harmless when $\Delta x=\Delta y$).
- Typos: "six-order approximation" (§3), "spitting-based" (Ex. 4.2).
- $\omega$ is the vorticity in §4.4 and $\omega_k$ the WENO weights in §2.2.

# Notation map

| Zheng et al. 2022 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$ | $u$ | transported density |
| $(a,b)$ | $(v_1,v_2)$ | velocity field; **collision** with the wave speed $a$ |
| $I_{i,j}$, $\bar u^n_{i,j}$ | same | Eulerian cell and cell average; finite volume |
| $(X,Y)$ | same (local) | backward characteristics from $(x,y,t^{n+1})$ |
| $I^\star_{i,j}$, $\tilde I^\star_{i,j}$, $I^{\star\star}_{i,j}$ | same (local) | exact, cubic-curved and straight-sided upstream cells |
| $v^\star_k$ | same (local) | feet of the four Gauss–Lobatto points of an edge |
| $\xi$, $(\xi,\eta)$ | same (local) | edge parameter and chord frame; **collision** with the DG nodes $\xi_j$ and the entropy $\eta$ |
| $f(x')$ (Lemma 3.5) | $g(x')$ (local) | edge as a graph over its chord |
| $\mu_i$, $\nu_j$ | $\hat x$, $\hat y$ (local) | $(x-x_i)/\Delta x$, $(y-y_j)/\Delta y$; **collision** with $\mu$ and the CFL number $\nu$ |
| $v^l$, $l=1..13$ | $\varphi_l$ (local) | Legendre-type basis; $l\le10$ spans $\mathbb P^3$ |
| $\tilde q_0$, $q_0$, $q_k$ | $\tilde P_{\mathrm{opt}}$, $P_{\mathrm{opt}}$, $P_k$ (local) | 13-cell polynomial, its $\mathbb P^3$ projection, $\mathbb P^1$ candidates; $P_0$ is then the CWENO central candidate $(P_{\mathrm{opt}}-\sum_kd_kP_k)/d_0$; **collision** with the weight exponent $q$ |
| $\gamma_k$ | $d_k$ | linear weights, $\gamma_0=0.8$, $\gamma_{1..4}=0.05$; **collision** with $\gamma$ |
| $\beta_k$ | $\beta_k$ | 2D indicators (12) |
| $\tau$ | $\tau$ | $\big(\frac14\sum_{k=1}^4\lvert\beta_0-\beta_k\rvert\big)^2$, not $\tau_5$ |
| $\bar\omega_k$, $\omega_k$ | $\alpha_k$, $\omega_k$ | $\alpha_k=d_k\big(1+\tau/(\beta_k+\epsilon)\big)$ |
| $\epsilon=10^{-14}$ | $\epsilon$ | |
| $a^{(i,j)}_l$ | same (local) | coefficients of the reconstruction $\tilde u^{(i,j)}$ |
| $\mathcal L^k$, $\mathcal S^k$ | same (local) | outer and inner integral segments |
| $\tilde P$, $\tilde Q$ | same (local) | Green potentials; **collision**: registry $Q=MD$ |
| $\theta_{i,j}$, $m_{ij}$ | $\theta$, $m_{ij}$ | Zhang–Shu factor and cell minimum |
| $h$ | $h\sim\Delta x\sim\Delta y\sim\Delta t$ (local) | **collision** with the two-point flux $h$ |
| CFL | $\nu$ | $\Delta t=\nu/(\max\lvert v_1\rvert/\Delta x+\max\lvert v_2\rvert/\Delta y)$; 10.2 by default |
| $\kappa_1$, $\kappa_2$ | $\nu_1$, $\nu_2$ (local) | directional Courant numbers; **collision** with the kinetic energy $\kappa$ |
| $\zeta_1$, $\zeta_2$ | $\vartheta_1$, $\vartheta_2$ | reduced wavenumbers |
| $A$ | $\mathsf A$ (local) | amplification factor; not printed |
| $f(x,v,t)$, $E$, $\phi$, $\rho$ | same (local) | Vlasov distribution, electric field, potential, charge density; **collision** with the flux $f$ and the total energy $E$ |
| $\omega$, $\psi$, $\mathbf u$ | same (local) | vorticity, stream function, velocity of §4.4; **collision** with $\omega_k$ and $\psi$ |
| $SLWENO(\mathbf V,\tau)$ | same (local) | semi-Lagrangian evolution over a step $\tau$; not the indicator $\tau$ |

# Reference list

The paper prints 39 references, numbered [1]–[39]. The list is merged complete into
the [bibliography](/bibliography.md), with `citedby` including `zheng-2022`. [23]
is a printed duplicate of [1] (Lauritzen, Nair and Ullrich, CSLAM, 2010). [13] and
[17] are two works of Qiu and coauthors from 2011. [21] (Xiong, Russo and Qiu, J.
Sci. Comput., 2019) prints no volume or pages, and [39] (Shoucri, Internat. J.
Numer. Methods Engrg. 17) is recorded with the printed year 2010. No DOIs or arXiv
identifiers are printed. No item is unparseable.

# Pages created or updated

Chunk 2 (2026-10-22), cited further in chunks 3–7 (2026-10-22/23). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Central WENO (CWENO)](/methods/cweno.md)
* [Conservative semi-Lagrangian finite-volume WENO](/methods/semi-lagrangian-finite-volume.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
