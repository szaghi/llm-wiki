---
type: Source
title: "Kiechle et al. (2025) — A positivity-preserving Active Flux method for the Vlasov-Poisson system"
description: "Third-order fully discrete Active Flux method on Cartesian grids with a new positivity-preserving flux limiter that blends the Active Flux flux with a global Lax–Friedrichs flux through a four-way convex split of the update; tested on advection, a guiding-center model and the 1+1D Vlasov–Poisson system."
resource: "doi:10.1016/j.jcp.2024.113693"
source_kind: paper
authors: [Kiechle Y., Chudzik E., Helzel C.]
year: 2025
venue: "J. Comput. Phys. 524:113693"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Journal_of_Computational_Physics_Kiechle_A_positivity-preserving_Active_Flux_method_for_the_Vlasov-Po.pdf"
tags: [active-flux, positivity, bound-preserving, limiting, finite-volume]
timestamp: 2026-10-23T20:30:00Z
---

# Summary

Kiechle et al. (2025) build a fully discrete, third-order
[Active Flux](/methods/active-flux.md) (AF) method on Cartesian grids and a
new positivity-preserving flux limiter for it. The degrees of freedom are
cell averages plus point values at edge midpoints and corners, shared by
neighbouring cells. The cell averages are updated by a conservative
finite-volume formula whose fluxes are tensor-product Simpson rules in space
and time, over point values at $t^n$, $t^{n+1/2}$ and $t^{n+1}$. The point
values are evolved by tracing characteristics backwards with classical RK4
and evaluating the continuous piecewise-biquadratic AF reconstruction at the
footpoints.

On variable-coefficient advection (LeVeque's deformation test, a different
LeVeque test from the [solid-body rotation](/benchmarks/solid-body-rotation.md))
the unlimited method shows mild oscillations. The authors' earlier
bound-preserving reconstruction reduces them but is not exactly
[bound-preserving](/properties/bound-preservation.md), because Simpson's rule
is not exact for piecewise quadratics. The new limiter, in the spirit of the
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)
of Hu, Adams and Shu, replaces each interface flux by a convex combination
$\theta\,\hat f^{\mathrm{AF}}+(1-\theta)\,\hat f^{\mathrm{LF}}$ with a
first-order global [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md).
$\theta$ is chosen interface by interface from a split of the 2D cell update
into four one-sided states, which guarantees non-negative cell averages for
CFL $\le1/4$. Only the lower bound is enforced. The authors compare it with
the bound-preserving PAMPA flux limiter of Abgrall et al. (the preprint of
[Abgrall et al. (2026)](/sources/abgrall-2026.md)), which enforces both
bounds.

The method is then applied to a guiding-center model and, unsplit, to the
1+1D Vlasov–Poisson system, with one Poisson solve and one Vlasov step per
time step and a Taylor extension of the electric field in time built from
velocity moments. On the two-stream instability the observed order tends to
3 with and without the limiter (Table 1); the $L^1$ norm is conserved to
machine precision. The plasma-physics tests (Landau damping, multi-vortex
two-stream, bump-on-tail) are peripheral to this bundle.

# Version read

The archive file is the version of record (Elsevier typeset, open access CC
BY), 23 pages, all read; pp. 12–13 checked on the page images for Eqs.
(36)–(44). Title, the three authors, venue and DOI on page 1 match the
Crossref record. Ref. [29] is the authors' own conference paper on the
unlimited method. Every claim, equation and number on this page is that of
the version of record.

# Key claims

Registry notation: cell averages $\bar u_{i,j}$ (source $Q^n_{i,j}$, in §4
$F^n_{i,j}$), numerical fluxes $\hat f_{i\pm1/2,j}$, $\hat g_{i,j\pm1/2}$
(source $F$, $G$; in §4 $H$, $G$), global speeds $a^{(1)}$, $a^{(2)}$ (registry $a$
per direction). Page-local: $u_{i+1/2,j}$, $u_{i+1/2,j\pm1/2}$ the shared
point values at edge midpoints and corners; $\theta_{i-1/2,j}$ the flux-limiting
coefficient (source $\gamma$); $\mathsf s_x+\mathsf s_y=1$ the convex-split weights;
$u^{\pm}_{x,i}$, $u^{\pm}_{y,j}$ the four split states (source $Q^\pm_i$,
$Q^\pm_j$); $\epsilon$ the positivity floor (as in the source; page-local, not the weight regularization);
$\mathcal F$ the distribution function of §4 (source $f$); $\mathbb E$ the
second velocity moment.

1. In its simplest 1D linear-advection form AF is equivalent to van Leer's scheme V; Eymann and Roe proposed it as fully discrete, truly multidimensional, third order and compact in space and time (§1). **Stated**
2. The 2D AF cell-average update is the conservative finite-volume formula (2), with fluxes (5) given by the 2D Simpson rule over the space–time edge, weights $\frac1{36}(1,4,1;4,16,4;1,4,1)$ over corner and edge-midpoint values at $t^n$, $t^{n+1/2}$, $t^{n+1}$ (§2, Eq. (5)). **Stated**
3. The AF reconstruction in each cell is the biquadratic (6) that interpolates the eight boundary point values and has the cell average $\bar u_{i,j}$ (§2, Eq. (6)). **Stated**
4. For the colour equation (8) (divergence-free velocity) the exact solution is bound-preserving; Zhang and Shu note that discretising the conservative form (7) makes perfectly bound-preserving methods difficult (§3). **Stated**
5. Unlimited AF on LeVeque's deformation test shows "quite mild" oscillations near jumps (§3.1.1, Fig. 2). **Shown**
6. The bound-preserving piecewise-quadratic reconstruction of their ref. [13] (discontinuous across interfaces, old point values chosen upwind) reduces the oscillations but is not exactly bound-preserving, because Simpson's rule is not exact for piecewise quadratics (§3.1.1, Fig. 3). **Shown**
7. The new limiter uses $\hat f^{\mathrm{lim}}_{i-1/2,j}=\theta_{i-1/2,j}\hat f_{i-1/2,j}+(1-\theta_{i-1/2,j})\hat f^{\mathrm{LF}}_{i-1/2,j}$ (Eqs. (12)–(13)), with the global Lax–Friedrichs flux $\hat f^{\mathrm{LF}}_{i-1/2,j}=\tfrac12\big(f(\bar u_{i-1,j})+f(\bar u_{i,j})-a^{(1)}(\bar u_{i,j}-\bar u_{i-1,j})\big)$ (Eqs. (14)–(15)) and coefficients (22)–(24) derived from the convex split (16) and the sufficient condition (17) (§3.2). **Derived**
8. Convex split (16): with $\mathsf s_x+\mathsf s_y=1$, $\bar u^{n+1}_{i,j}=\tfrac{\mathsf s_x}2(u^-_{x,i}+u^+_{x,i})+\tfrac{\mathsf s_y}2(u^-_{y,j}+u^+_{y,j})$, $u^\mp_{x,i}=\bar u^n_{i,j}\pm\frac{2\Delta t}{\mathsf s_x\Delta x}\hat f_{i\mp1/2,j}$; positivity of the four split states suffices (17) (§3.2). **Derived**
9. The Lax–Friedrichs scheme is positivity-preserving for CFL $\le1/2$, but positivity of its split states (18) with $\mathsf s_x=\mathsf s_y=1/2$ is guaranteed only for CFL $\le1/4$ (§3.2). **Stated**
10. $\theta^-_{i-1/2,j}=(\epsilon-u^{\mathrm{LF},-}_{x,i})/(u^-_{x,i}-u^{\mathrm{LF},-}_{x,i})$ if $u^-_{x,i}<\epsilon$, else 1; $\theta^+_{i-1/2,j}$ the same from the right state of cell $i-1$; $\theta_{i-1/2,j}=\min(\theta^-,\theta^+)$, with $\epsilon=\max\{10^{-13},\min u_0\}$ (Eqs. (22)–(24)). By construction the limited scheme keeps the cell averages positive (§3.2). **Derived**
11. The limiter does not affect the order of accuracy for smooth solutions, as shown for general finite-volume methods by Hu et al.; the convergence study of §4.4 confirms it (§3.2; Table 1). **Stated** (cited) / **Shown**
12. For advection the limiter needs no bound-preserving reconstruction and so avoids computing local extrema of the reconstruction in each cell (§3.1.1). **Stated** (no timing)
13. Computing $\theta$ is sensitive to round-off; the implementation uses $\theta=\max(\min(\theta^--10^{-16},\theta^+-10^{-16},1),0)$ (Remark 3.1). **Stated**
14. The bound-preserving PAMPA flux limiter of Abgrall et al. is related but not equivalent: it enforces both bounds and needs bound-preserving point values; with a global speed $a^{(1)}$ in place of its local speed it gave more accurate results on the test problem (Remark 3.2, Fig. 5). **Shown**
15. On the guiding-center diocotron test, with predictor–corrector Poisson coupling (three Poisson solves per step on a mesh of spacing $\Delta x/2$), vortices form and merge (§3.3, Fig. 6). **Shown**
16. For Vlasov–Poisson, third order is obtained "in a truly multi dimensional way without the use of operator splitting techniques", with one Poisson and one Vlasov step per time step (§4, §5). **Shown** (Table 1)
17. A second-order $E_t$ and a first-order $E_{tt}$ suffice for the third-order Taylor approximation (34) of $E$ in time; $E_t=-\int v\mathcal F\,dv$, $E_{tt}=\partial_x\mathbb E-\rho E$ (§4.1, Eqs. (34)–(35), after Rossmanith and Seal). **Derived**
18. With CFL $:=\max\big(\max_j\lvert v_j\rvert\Delta t/\Delta x,\ \max_i\lvert E(x_i,t)\rvert\Delta t/\Delta v\big)\le1$ the characteristic footpoints stay in a neighbouring cell, so local quadratic Lagrange interpolation of $E$ suffices (§4.1). **Stated**
19. Two-stream convergence at $t=1$: unlimited $L^1$ errors $3.1813\times10^{-2}$ (32²) to $1.0538\times10^{-5}$ (512²), orders 2.7476, 2.8886, 2.9480, 2.9730; limited $3.3272\times10^{-2}$ to $1.1128\times10^{-5}$, orders 2.7398, 2.8841, 2.9461, 2.9722; limited at CFL 0.25, unlimited at CFL 0.5 (Table 1, §4.4.1). **Shown**
20. The method preserves the $L^1$ norm of $\mathcal F$ to machine precision, being conservative and positive (§1, §4.4). **Derived**
21. The limited two-stream solutions suppress negative values without otherwise disturbing the structure; the unlimited solution becomes negative (Figs. 10–11). **Shown**
22. AF has four degrees of freedom per cell (shared boundary point values) against 15 for the fifth-order DG of Rossmanith and Seal; at a comparable number of degrees of freedom it resolves filaments comparably (§4.4.1). **Shown** (visual comparison)
23. The 512² two-stream structure is "comparable with" a fifth-order WENO result with Runge–Kutta time stepping of their ref. [45] (§4.4.1). **Stated**
24. Weak Landau damping on 32×32: AF "outperforms" PFC and fourth-order ENO and compares well with cubic-spline semi-Lagrangian, by comparison with a figure of another paper; linear decay rate $-0.1533$ (§4.4.2, Fig. 13). **Shown** (cross-paper figure comparison)
25. Landau damping is run unlimited with CFL $\le0.75$; "as long as no negative cell averages arise, the limited and unlimited methods coincide" (§4.4.2). **Stated**
26. Multi-vortex two-stream: 8–9 vortices form independent of resolution and then merge, quickly at first, then slowly (§4.4.3, Figs. 16–18). **Shown**
27. Bump-on-tail: total energy is not preserved, which the authors relate to the difficulty of preserving both positivity and energy (§4.4.4, Fig. 20). **Shown**
28. Positivity can be guaranteed only for a reduced CFL number (§5). **Stated**

# Printed slips

- Eq. (6): the coefficient of $\xi\eta^2$ is printed "$x_{12}$" instead of $c_{12}$ (the following sentence defines $c_{ij}$, $i,j=0,1,2$).
- **Eq. (37)** (p. 12): $\partial_x\mathbb E(x_i,t^n)\approx\big(\mathbb E^n_{i-3/2}-8\mathbb E^n_{i-1/2}+8\mathbb E^n_{i+1/2}-\mathbb E^n_{i+3/2}\big)/(12\,\Delta x/2)$, "fourth order", with $i=\tfrac12,1,\dots,N_x+\tfrac12$ on a grid of spacing $\Delta x/2$. *(Compiler check, not in the sources: with $h=\Delta x/2$ the indices $i\pm1/2$ lie at $\pm h$ and $i\pm3/2$ at $\pm3h$; for $\mathbb E=x$ the printed numerator is $10h$, so the formula returns $10/12$ instead of 1. The fourth-order central difference $\big(\mathbb E(x-2h)-8\mathbb E(x-h)+8\mathbb E(x+h)-\mathbb E(x+2h)\big)/(12h)$ needs the outer indices $i\pm1$.)*
- **Eq. (44)** (p. 13): $\partial_{xx}\phi\approx\big(-\phi_{i-3/2}+16\phi_{i-1/2}-30\phi_i+16\phi_{i+1/2}-\phi_{i+3/2}\big)/(12\,\Delta x/2)$, "fourth order". *(Compiler check, not in the sources: the same index issue as Eq. (37), and the denominator lacks the square: a second derivative needs $12h^2$. With nodes $\pm h,\pm2h$ and $\phi=x^2$ the numerator is $24h^2$, giving 2; with the printed nodes $\pm h,\pm3h$ it is $14h^2$.)*
- Time levels of $E$: after Eq. (33) the text lists $\tau\in\{0,\Delta t/2,\Delta t\}$, Algorithm 1 lists $\tau\in\{\Delta t/4,\Delta t/2,\Delta t\}$; the $\Delta t/4$ is not explained.
- Eq. (35): $E_{tt}(x,t)=\partial_x\mathbb E(x,t^n)-\rho(x,t^n)E(x,t^n)$ has $t$ on the left and $t^n$ on the right.
- Ref. [30] prints the journal as "J. Numer. Anal. 33 (2) (1996)" with the SIAM DOI 10.1137/0733033 ("SIAM" missing). Ref. [44] prints "J. Comput. Phys. 273 (2014) 618–639" with the DOI "10.1137/140965326", a SIAM prefix that does not fit a JCP venue; this page does not resolve which of the two is wrong.
- Refs. [40] and [41] are the same work (Sonnendrücker, Roche, Bertrand, Ghizzo, J. Comput. Phys. 149 (1999) 201–220), printed with and without DOI.
- Typos: "reminder of the paper" (§3.2), "ony a grid" (§3.3), "128. × 128" (§4.4.3), "relay on" (§1), "ClearIy" (§4.4.1), "insure" (§3.2), a missing comma in "$\alpha=0.04$ $k=0.3$" (§4.4.4).

# Notation map

| Kiechle et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $C_{i,j}$, $Q^n_{i,j}$ | $I_{i,j}$, $\bar u_{i,j}$ | in §4 the cell averages are $F^n_{i,j}$ |
| $Q_{i+1/2,j}$, $Q_{i+1/2,j\pm1/2}$ | $u_{i+1/2,j}$, $u_{i+1/2,j\pm1/2}$ (local) | one shared value per point, no $u^\pm$ pair |
| $f$, $g$ (§2–3) | $f$, $g$ (flux functions) | **collision**: in §4 $f$ is the distribution function, here $\mathcal F$ |
| $F_{i\pm1/2,j}$, $G_{i,j\pm1/2}$; $H$ (§4) | $\hat f_{i\pm1/2,j}$, $\hat g_{i,j\pm1/2}$ | **collision**: §4 reuses $F$ for the distribution-function unknowns |
| $F^{LF}$, $G^{LF}$ | $\hat f^{\mathrm{LF}}$, $\hat g^{\mathrm{LF}}$ | global Lax–Friedrichs |
| $a$, $b$ (§3) | $v_1$, $v_2$ advection velocity (local) | not the speeds $a_x$, $a_y$ |
| $a_x$, $a_y$ | $a^{(1)}$, $a^{(2)}$: $a$ per direction, global | |
| $\alpha_x$, $\alpha_y$ | $\mathsf s_x$, $\mathsf s_y$ (local, as on the flux-limiter page) | convex-split weights; **collision**: Remark 3.2's $\alpha_{i-1/2,j}$ is a local wave speed |
| $Q^\pm_i$, $Q^\pm_j$, $Q^{LF,\pm}_i$ | $u^\pm_{x,i}$, $u^\pm_{y,j}$, $u^{\mathrm{LF},\pm}_{x,i}$ (local) | split states of (16), (18) |
| $\gamma_{i-1/2,j}$, $\gamma^\pm$ | $\theta_{i-1/2,j}$, $\theta^\pm$ | as on the flux-limiter page; **collision** with $\gamma$ and with the Landau decay rate $\gamma=-0.1533$ |
| $\epsilon$ | $\epsilon$ (local) | positivity floor, as on the flux-limiter page; not the weight regularization |
| $M_0$, $m_0$, $u^*$ | bounds and Lax–Friedrichs bar state of the PAMPA limiter | Remark 3.2 |
| $q^{rec}$, $c_{kl}$ | biquadratic AF reconstruction and its coefficients | reference cell $[-1,1]^2$ |
| $f(x,v,t)$ | $\mathcal F$ (local) | distribution function |
| $E$, $\phi$, $\Phi$ | electric field, potentials | §4: $\partial_{xx}\phi=\rho-\rho_0$, $E=\partial_x\phi$; §3.3: $-\Delta\Phi=\rho$, $E=-\nabla\Phi$ (signs differ) |
| $\rho$, $\rho u$, $\mathbb E$ | charge density, first and second velocity moments | $\rho$ is not a gas density |
| CFL | $\nu$ | phase-space definition of claim 18 |

# Reference list

The paper prints 47 references, numbered [1]–[47]. The list is merged
complete into the [bibliography](/bibliography.md), with `citedby`
including `kiechle-2025`. Refs. [40] and [41] are a printed duplicate and
are merged as one work. Ref. [1] (Abgrall & Barsukow, arXiv:2208.14476) is
the preprint of [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) and
ref. [3] (arXiv:2410.14292) the preprint of
[Abgrall et al. (2026)](/sources/abgrall-2026.md); both are kept as distinct
preprint entries. Ref. [2] (Abgrall, Barsukow & Klingenberg, arXiv:2310.00683)
is a different work from the ingested Abgrall et al. papers and takes a
disambiguated key. Refs. [11] and [14] are the ingested
[Calhoun et al. (2023)](/sources/calhoun-2023.md) and
[Chudzik et al. (2024)](/sources/chudzik-2024.md). The DOI–venue mismatch of
ref. [44] is recorded above. No item is unparseable; refs. [4] and [11]
print no page or article number.

# Pages created or updated

Chunk 10 (2026-10-23). This source is cited on:

* [Active Flux](/methods/active-flux.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [PAMPA scheme](/methods/pampa-scheme.md)
* [Positivity-preserving flux limiter (Hu–Adams–Shu)](/methods/positivity-preserving-flux-limiter.md)
* [Solid-body rotation](/benchmarks/solid-body-rotation.md)
