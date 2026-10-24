---
type: Method
title: "Active Flux"
description: "Active Flux evolves cell averages conservatively with fluxes from point values shared at cell interfaces, giving a globally continuous reconstruction without Riemann solvers; the page covers arbitrary order in 1D and on 2D Cartesian grids, flux-vector-split point updates, bound-preserving limiting, adaptive refinement and bicharacteristic operators for systems."
status: established
aliases: [AF, active point value method, high-order Active Flux, Cartesian Active Flux, AF with evolution-Galerkin operators, PAMPA]
tags: [finite-volume, reconstruction, characteristic, limiting]
timestamp: 2026-10-23T20:30:00Z
---

# Active Flux

Active Flux (AF) is a method for $\partial_tu+\partial_xf(u)=0$ whose degrees of
freedom are the cell averages $\bar u_i$ **and** point values $u_{i+1/2}\approx u(x_{i+1/2})$
located at the cell interfaces and *shared* by the two adjacent cells. There is a
single value per interface (no $u^\pm_{i+1/2}$ pair), so the reconstruction is globally
continuous, and no Riemann solver is needed. The averages are updated by the exact
finite-volume balance with the interface point values as flux arguments; the point
values are evolved independently, by an upwind approximation of the evolution, and need
not be conservative (they may be evolved in primitive variables). Abgrall & Barsukow
(2023) state that the name really means "active point value at the cell interface"
([Abgrall & Barsukow (2023)](/sources/abgrall-2023.md), §1, §2).

## Traditional (third-order) Active Flux

As recalled by [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) (Def. 2.1, Eqs.
(3)–(11)), the reconstruction $u^{\mathrm{rec}}_i$ on $I_i$ (page-local symbol) is
continuous, takes the values $u_{i\pm1/2}$ at the interfaces and has mean $\bar u_i$; with
these three data it is a parabola, which is why every AF method in the literature before
their paper was at most third order (§2.1, §7). The semi-discretization is

$$\frac{d}{dt}\bar u_i=-\frac{f\big(u_{i+1/2}(t)\big)-f\big(u_{i-1/2}(t)\big)}{\Delta x},$$

with $u_{i+1/2}(t)$ the solution at $x_{i+1/2}$ of the initial value problem with data
$u^{\mathrm{rec}}$, up to $\mathcal O(t^3)$. The fully discrete original version integrates
the flux in time with Simpson's rule over point values at $t^n$, $t^{n+1/2}$, $t^{n+1}$
obtained from the same reconstruction (Eqs. (18)–(19)); for linear advection it is stable
up to $\nu=1$ (Eqs. (23)–(24)). The semi-discrete form of Abgrall (2020), with a
third-order finite difference for the point-value update and Runge–Kutta time stepping, has
stability limit $\nu=0.77$ (§2.1, Def. 2.2, Eqs. (14)–(17)). In that form the point
values obey $\frac{d}{dt}u_{i+1/2}=-\mathcal R(\dots)$, where $\mathcal R$ (page-local) is any
consistent approximation of $\partial_xf(u)$ at $x_{i+1/2}$ built from neighbouring point
values and averages.

The averages are conservative, so a Lax–Wendroff-type convergence result holds: Abgrall &
Barsukow report that "an analogue of a Lax–Wendroff theorem for Active Flux has been shown"
by Abgrall (2020) (§1; see [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)). They
also recall that AF on Cartesian grids is vorticity preserving and low-Mach compliant for
linear acoustics, whereas a fully multi-dimensional Godunov method with the exact acoustic
Riemann solver has neither property (§1, §2.1).

## Three routes to arbitrary order

[Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) give three extensions, each tied to
an interpretation of AF; all are one-dimensional.

**(A) Larger stencils — AF as coupled finite volume / finite difference (§3).** The
degrees of freedom stay the traditional ones. The point values are updated by method of
lines with linear finite differences that mix point values and averages,

$$\frac1{\Delta x}\sum_{j=-\ell}^{\ell}\Big(b^{(0)}_j\bar u_{i+j}+b_{j+1/2}u_{i+j+1/2}\Big)=\partial_xu(x_{i+1/2})+\mathcal O(\Delta x^p),$$

(Eq. (37); coefficients $b$ page-local). Each formula (FD1, FD3a–c, FD4a–b, FD5a–c, FD6,
FD7a, FD7c) uses one degree of freedom more than needed and carries one free parameter,
tuned for stability with SSP-RK3. Upwinding splits the Jacobian:
$\frac{d}{dt}u_{i+1/2}=-\big(A(\check u_{i+1/2})^+D+A(\check u_{i+1/2})^-D^*\big)$, with
$D$ the mixed formula, $D^*$ its mirror, $\check u_{i+1/2}$ the state chosen for upwinding
(all page-local) and $A^\pm=R\,\mathrm{diag}\big(\max\{\lambda_l,0\}\big)L$,
$R\,\mathrm{diag}\big(\min\{\lambda_l,0\}\big)L$ for systems (Eqs. (46)–(49)). An order-$n$ AF method needs only an order-$(n-1)$ derivative
approximation (§3.1). Example: FD1 is
$\partial_xu(x_{i+1/2})\approx\big[(\mathsf a-2)u_{i-1/2}+(2-2\mathsf a)\bar u_i+\mathsf a\,u_{i+1/2}\big]/\Delta x$,
first order in general and second order for $\mathsf a=4$ (Eq. (43), Table 1;
*compiler check, not in the sources:* inserting $1$, $x$, $x^2$ confirms exactness on
$\mathbb P^2$ exactly when $\mathsf a=4$). Maximal SSP-RK3 CFL numbers at the optimal
parameter range from $0.45$ (FD3c) to $1$ (FD1, FD3b); e.g. FD5b $0.713$, FD6 $0.73$,
FD7a $0.657$, FD7c $0.62$ (Tables 1–2). Orders 3–7 are observed on linear advection and
on Burgers before shock formation (Figs. 16, 18).

**(B) Further point values — AF as enriched finite volume (§4).** Add $k$ point values
inside each cell at $x_i+\Delta x\,\xi_j$, $\xi_j\in[-\tfrac12,\tfrac12]$ (page-local
positions, not quadrature nodes); the reconstruction lies in $\mathbb P^{k+2}$, stays
$C^0$, and the order is $n=k+3$. Theorem 4.1 reduces the mixed point/average interpolation
to ordinary interpolation: with $p_1$ interpolating the point data and $p_2$ vanishing at
them and equal to $1$ at one further point, and $\bar y$ the prescribed average (page-local
polynomials and datum), $p=p_1+p_2\,\big(\Delta x\,\bar y-\int p_1\big)/\int p_2$, unique when $\int p_2\ne0$.
**Theorem 4.2:** if the interpolation points are symmetric about the cell centre and their
number $n-1$ is odd, then $\int p_2=0$ and no reconstruction exists, so even-order variant-B
schemes with symmetric interior points are impossible (asymmetric placement is stated to
allow them). The update keeps the characteristic-based evolution (exact for linear
advection; a fixed-point foot-point iteration for scalar nonlinear laws; the third-order
approximate evolution operator of Barsukow (2021) for systems) and the leap-frog-type time
integration with Gauss–Lobatto flux quadrature in time (Eqs. (83)–(96)). Fifth order is
stable for all $\nu\in(0,1]$ provided the interior points sit near the interfaces,
$\xi_1=-\xi_2\gtrsim0.4$ (Fig. 20); 5th and 7th order are observed on linear advection and
Burgers (Figs. 21, 23).

**(C) Further moments — AF as coupled finite element / finite difference (§5).** Add the
normalized moments $u^{(\ell)}_i=\mathcal N_\ell\int_{-\Delta x/2}^{\Delta x/2}x^\ell u(t,x_i+x)\,dx$,
$\mathcal N_\ell=(\ell+1)2^\ell/\Delta x^{\ell+1}$ (page-local, not the registry's stencil value $u^{(k)}$; $u^{(0)}_i=\bar u_i$), updated by
their exact evolution equations (Eq. (100)), which close for linear flux, so that the
accuracy is set entirely by the point-value update (Eq. (103)). The point values use
"moment differences" — derivatives of the in-cell reconstruction at the interface: MD3
(equal to FD1 with $\mathsf a=4$), MD5, MD7 (Eqs. (111)–(115)). The stencil is compact but
the CFL is small: with SSP-RK3, MD5 is stable for $\nu\le0.13$ and MD7 for $\nu\le0.066$
(§5.3).

The authors' comparison (§7): variant B has the best stability and the closest time
integration to the original AF; variant C keeps a compact stencil and is the best
candidate for further extensions but has the smallest CFL; variants A and C apply to any
hyperbolic system and need no Riemann solver; no variant dominates. A fourth route, Roe's
(2021) storage of interface derivatives up to order $s$ (page-local), gives a $C^s$
reconstruction of degree $2s+2$ with order at most $2s+3$ (§6).

## Limiting and transonic upwinding

Limiting only reduces the order of the point-value update; the average update is never
limited, which the authors state does not exclude oscillations (§2.2). For monotone data,
the parabola through $u_{i\pm1/2}$ with mean $\bar u_i$ is monotone iff
$\mathsf r_i=(u_{i+1/2}-\bar u_i)/(\bar u_i-u_{i-1/2})\in[\tfrac12,2]$ (page-local ratio, not the TVD slope ratio $r_i$; Thm. 2.1,
recalled from Barsukow 2021); outside that range a monotone power-law reconstruction is
used (Thm. 2.2, Eqs. (27)–(30)), and it is the last fallback of all three variants
(§§3.4, 4.4, 5.4). The [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md) is
stated to be incompatible with prescribed interface values (§2.2). Early AF fails in the
transonic case: for Burgers with data $2$ / $-1$ a wrong upwind estimate keeps the point
values stationary while the average grows without bound, because a continuous
reconstruction can self-steepen into a shock within one step (§2.3, Eqs. (32)–(35)). The
fix chooses among several characteristic foot points the one of largest speed modulus;
variants A and C use a switch (Eq. (53)) that degrades accuracy at sonic points (§3.3).

## Generalized Active Flux with flux vector splitting

[Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) (arXiv v3) work with the
"generalized" (method-of-lines) AF of Abgrall and Barsukow: the averages follow the
semi-discrete balance above, the point values a finite-difference-like update, both
advanced with [SSP-RK3](/methods/ssp-runge-kutta.md). Their thesis is that, against the
earlier view that any stable consistent point-value formula will do, nonlinear problems
impose further conditions (§2). The update they criticise is the **Jacobian splitting**
$\frac{d}{dt}u_{i+1/2}=-\big[A^+(u_{i+1/2})D^+_{i+1/2}+A^-(u_{i+1/2})D^-_{i+1/2}\big]$,
$A^\pm=R\Lambda^\pm L$, with the upwind derivatives of the cell parabolas (Eqs. (6)–(8))
$$D^+_{i+1/2}=\frac{2u_{i-1/2}-6\bar u_i+4u_{i+1/2}}{\Delta x},\qquad
D^-_{i+1/2}=\frac{-4u_{i+1/2}+6\bar u_{i+1}-2u_{i+3/2}}{\Delta x}$$
(page-local $D^\pm$). It has two defects (§2.1, §3.2):

- **Stagnation.** For Burgers' equation with $u_{i-1/2}=2$, $u_{i+1/2}=-1$ at the initial
  discontinuity both upwind derivatives vanish, the point values freeze and $\bar u_i$
  grows linearly in time, a spike (Example 5.1). This is the transonic failure recalled
  above from Abgrall & Barsukow (2023), on the same data; [bound-preserving
  limiting](/properties/bound-preservation.md) of the average alone does not remove it.
- **Mesh alignment.** In 2D, on a grid-aligned quasi-one-dimensional Sod problem
  ($100\times2$ cells), the corner and horizontal-edge values decouple from the
  vertical-edge values and the averages, and the density deviates strongly between contact
  and shock (Example 5.7, Figs. 10–11); the authors call the reason "complicated".

The cure is a [flux vector splitting](/methods/flux-vector-splitting.md) of the
point-value update (§2.2, Eqs. (9)–(11)): with $f=f^++f^-$, the eigenvalues of
$\partial f^+/\partial u$ non-negative and those of $\partial f^-/\partial u$
non-positive, $f^\pm$ is evaluated at the two interfaces and at the cell centre, where the
parabola gives $u_i=(-u_{i-1/2}+6\bar u_i-u_{i+1/2})/4$, and the parabola through these
three values is differentiated at the interface,
$$\frac{d}{dt}u_{i+1/2}=-\frac{f^+_{i-1/2}-4f^+_i+3f^+_{i+1/2}}{\Delta x}-\frac{-3f^-_{i+1/2}+4f^-_{i+1}-f^-_{i+3/2}}{\Delta x},$$
two third-order differences; the continuous reconstruction is kept. Three splittings are
used: local [Lax–Friedrichs](/methods/lax-friedrichs-flux.md), with $a_{i+1/2}$ the
largest spectral radius over $u_{i-1/2},u_i,u_{i+1/2},u_{i+1},u_{i+3/2}$ (Eq. (12));
the upwind splitting $f^\pm=\tfrac12(f\pm\lvert A\rvert u)$, which for the Euler equations
is Steger–Warming and for linear systems reduces exactly to the Jacobian splitting, so
there the two methods coincide (§2.2.2); and van Leer–Hänel (§2.2.3). In 2D the corner
values take the splitting in both directions and the edge values the splitting in the
normal direction and a central difference along the edge (Eqs. (22)–(23)); the averages
use Simpson's rule along each edge (Eq. (20)). On smooth Euler tests the Jacobian,
Lax–Friedrichs and van Leer–Hänel variants reach third order, Steger–Warming about second
(near-vacuum vortex, Example 5.6; 1D accuracy test, Example D.1), which the authors
relate to the non-differentiability of its split fluxes (Remark 2.1). Maximal CFL
numbers, found experimentally, depend on the splitting, e.g. about $0.47$ (Jacobian),
$0.43$ (Lax–Friedrichs), $0.32$ (Steger–Warming), $0.18$ (van Leer–Hänel) on the 1D
accuracy test (Example D.1), and are "not related to the BP property" (Remark 5.1). The
authors judge Lax–Friedrichs splitting the best in CFL number and non-oscillatory
behaviour for strong discontinuities (Remark 2.2, Conclusion), and do not recommend the
power-law reconstruction for generalized AF, which oscillates more than their limiting and
drops the CFL number to $0.1$ (Example D.3).

**Bound preservation.** Duan et al. call an AF method bound preserving if averages *and*
point values starting in $G$ stay in $G$ (Def. 4.1). The averages are limited by
[convex limiting](/methods/convex-limiting.md) against a first-order local
Lax–Friedrichs flux, the point values by a
[Zhang–Shu-type](/methods/zhang-shu-scaling-limiter.md) blend with a first-order
Lax–Friedrichs point update on a staggered stencil, and the non-convex cell-centre value
$u_i$ is scaled toward $\bar u_i$ at each stage (Remarks 4.3–4.4). Limiting the averages
alone is not enough: on a 2D advection test $[0,1]$ is kept only with both limiters active
(Example 5.4, Table 1). Proposition 4.2 (2D) and Theorem C.1 (1D) give the maximum
principle for scalar laws and positive density and pressure for the Euler equations under
the time-step conditions of the first-order average and point-value schemes, which on
uniform meshes hold for
$\Delta t\le\frac14\min\{\Delta x/\lVert a^{(1)}\rVert_\infty,\Delta y/\lVert a^{(2)}\rVert_\infty\}$ in
2D and $\Delta t\le\Delta x/(2\lVert a\rVert_\infty)$ in 1D (Remarks 4.5,
C.1; $a^{(d)}$ the spectral radius in direction $d$); details on
[bound preservation](/properties/bound-preservation.md). A Jameson–Ducros product sensor
pushes the flux further toward the first-order one behind strong shocks
([troubled-cell indicators](/definitions/troubled-cell-indicator.md)). With these
ingredients the scheme runs the LeBlanc tube, the Woodward–Colella blast waves and the
Sedov problem, which fail without limiting (Examples 5.2, 5.3, 5.8), and Mach 80 and
2000 jets (Example 5.10), and on the forward-facing step at the same mesh resolves the Kelvin–Helmholtz
roll-ups better than $\mathbb P^2$ RKDG with the TVB limiter, with fewer degrees of
freedom (Example 5.9); on the double Mach reflection the roll-ups are comparable, with
"4 versus 6" degrees of freedom per cell (Example D.7).

## Two-dimensional Cartesian Active Flux

[Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) recall the fully discrete
Cartesian AF of Eymann–Roe, Barsukow et al. and Helzel et al. for
$\partial_tu+\partial_xf(u)+\partial_yg(u)=0$ (§2, Eqs. (1)–(3), Fig. 1; arXiv v2). The degrees
of freedom of cell $(i,j)$ at $t^n$ are the average $\bar u_{i,j}$ and point values at the four
corners $u_{i\pm1/2,j\pm1/2}$ and the four edge midpoints $u_{i\pm1/2,j}$, $u_{i,j\pm1/2}$. An edge
value is shared by two cells and a corner value by four, so each cell owns four degrees of
freedom: one average and three point values. On the reference cell a biquadratic polynomial
(nine coefficients, including the product of the two squared coordinates) interpolates the eight boundary values
and has mean $\bar u_{i,j}$; the global reconstruction is continuous and piecewise
biquadratic. The averages are updated by

$$\bar u^{n+1}_{i,j}=\bar u^n_{i,j}-\frac{\Delta t}{\Delta x}\big(\hat f_{i+1/2,j}-\hat f_{i-1/2,j}\big)-\frac{\Delta t}{\Delta y}\big(\hat g_{i,j+1/2}-\hat g_{i,j-1/2}\big),$$

where $\hat f_{i+1/2,j}$ is a $3\times3$ tensor Simpson rule in space along the edge and in time,
with weights $\tfrac1{36}(1,4,1)\otimes(1,4,1)$ on the edge endpoints and midpoint at $t^n$,
$t^{n+1/2}$, $t^{n+1}$ (Eq. (2)). The point values at $t^{n+1/2}$ serve only the flux; those at
$t^{n+1}$ also build the next reconstruction. The time integration is this one-step space–time
quadrature with an evolution operator for the point values, not the method-of-lines AF of the
previous section. The evolution operators recalled are:

- **Linear advection** with velocity $(v_1,v_2)$: exact characteristic tracing of the
  reconstruction (Eqs. (4)–(5)). With $\nu=\max(\lvert v_1\rvert\Delta t/\Delta x,\lvert v_2\rvert\Delta t/\Delta y)$
  the tracing needs $\nu\le1$, but linear stability is stricter and the authors run
  with $\nu\le0.75$, from Helzel et al. (Eq. (6), §2.1).
- **Burgers' equation** $\partial_tu+\partial_x(u^2/2)+\partial_y(u^2/2)=0$: a fixed-point
  iteration on the implicit characteristic relation $u(x,y,t)=u\big(x-u\,t,\,y-u\,t,0\big)$ that
  gains one order per iteration, so two iterations from a first-order guess give third order,
  the maximum the quadratic reconstruction allows (Eqs. (7)–(10)). The pointwise guess
  $u^{(0)}=u^n$ at the same location is unstable where the characteristic speed changes sign; a
  guess from the mean of the adjacent cell averages is stable (§2.2).
- **Linear acoustics**: the Eymann–Roe evolution operator, which assumes constant vorticity and
  evaluates exactly on the piecewise biquadratic data a weighted mean over a disc of radius
  $ct$ (Eqs. (11)–(14)). The time step keeps the circle around an edge midpoint inside the two
  adjacent cells, $\max(c\Delta t/\Delta x,c\Delta t/\Delta y)\le\tfrac12$ (Eq. (15)); the
  authors report this as necessary and, by Helzel et al., sufficient for linear stability on a
  regular Cartesian grid (§2.3).

These two-dimensional fully discrete limits ($0.75$, $\tfrac12$) and the one-dimensional limits
recalled by Abgrall & Barsukow ($\nu=1$ for the original scheme, $0.77$ for the semi-discrete
RK version) belong to different schemes (two-dimensional fully discrete against
one-dimensional); they are not competing values for one method. The same holds for the limits
$0.279$ (EG2) and $0.154$ (EG4) of Chudzik et al. below, which belong to other point-value
operators, and for the semi-discrete orders 3–7 of Barsukow et al. below.

Calhoun et al. also recall Barsukow's result that the Cartesian AF for acoustics with the exact
evolution operator is stationarity preserving: it adds no dissipation to discrete
representations of all stationary states (§1). The Eymann–Roe operator they use does not have
this property (§4.6). [Chudzik, Helzel & Lukáčová-Medvid'ová (2024)](/sources/chudzik-2024.md)
recall the same result (§2.1, §5.3) and the same fully discrete Cartesian scheme with the
$\tfrac1{36}$ Simpson flux (Eq. (38)); they list three acoustic operators used before them: the
Eymann–Roe formula, exact for constant vorticity (Eq. (4)); the Fan–Roe formula, exact for general
data (Eq. (6)); and Barsukow et al.'s radial-derivative form of the exact formula, which
integrates over a disc of radius $ct$ and needs no differentiation across interfaces (Eq. (7)).
They write the stability condition of the exact operators as
$\max(c\Delta t/\Delta x,c\Delta t/\Delta y)\le\tfrac12$, which their earlier work showed is
sufficient for linear stability (§2.1, Fig. 3).

## Arbitrary order on Cartesian grids

[Barsukow, Chandrashekar, Klingenberg & Lechner (2026)](/sources/barsukow-2026.md)
(arXiv v2) build a semi-discrete generalized AF of arbitrary order $N+1$ ($N$ the degree of
the reconstruction) on 2D Cartesian grids, as a hybrid finite element–finite volume
method in the sense of variant (C) above (§3, Def. 1). The degrees of freedom of a cell
are point values at its four nodes and at $N-1$ points on each edge, shared with the
neighbours, so that the reconstruction is a unique degree-$N$ polynomial on each edge and
globally $C^0$, plus moments $\frac{(k+1)2^k(l+1)2^l}{\Delta x\Delta y}\int_{I_{ij}}\hat x^k\hat y^lu\,dx$
of the cell ($\hat x$, $\hat y$ the reference coordinates in $[-\tfrac12,\tfrac12]$,
page-local), the average always among them (Eqs. (7)–(12)). Two reconstruction spaces are
used (§3.3):

- tensor-like $\mathbb Q^N$, with $(N-1)^2$ moments, which reduces to the biquadratic
  third-order Cartesian AF above for $N=2$;
- a minimal space, the serendipity space $\mathbb P^N\oplus\mathrm{span}\{\hat x^N\hat y,\hat x\hat y^N\}$
  for $N\ge4$ (with $\hat x^2\hat y^2$ added for $N=2,3$), with the moments against
  $\mathbb P^{N-4}$; its dimension is $8+1$, $12+1$, $17$, $23$, $30$ for orders $3$–$7$
  (Table 2). Unisolvence was checked with Mathematica up to order 7, while $\mathbb P^N$
  alone is not unisolvent (checked for $N=5,6$; §3.3.2).

Point values are updated by the Jacobian splitting with one-sided derivatives of the
upwind cell's reconstruction (tangential derivatives on edges are continuous and not
upwinded), moments by the weak form with Gauss or Gauss–Lobatto quadrature on the
reconstruction (Eqs. (30)–(36), Def. 2). **The edge points must be Gauss–Legendre points.**
A numerical eigenvalue analysis of the semi-discrete operator for linear advection
(orders 3–7, periodic $3^2$, $5^2$, $10^2$ grids, angles in $[0,\pi/2]$ in steps
$\pi/64$) finds non-positive real parts, with semisimple eigenvalues on the imaginary
axis up to tolerances $5\times10^{-13}$–$5\times10^{-12}$, only for Gauss edge points;
uniform and Gauss–Lobatto points give eigenvalues with positive real part at orders 4–7
(§4.1). This parallels Abgrall & Barsukow's 1D finding that interior points must move
toward the interfaces (variant B above). With SSP-RK3 the maximal CFL numbers of the
minimal method, defined at equal velocity components $a_x=a_y$ (Eq. (42)), are $0.27$,
$0.20$, $0.17$, $0.12$, $0.088$ for orders 3–7 (Table 3); the stable region in the plane
of the directional CFL numbers $(a_x\Delta t/\Delta x,\,a_y\Delta t/\Delta y)$ is close to a disc at orders 3–4 and close to a square at order 5
(Eqs. (43)–(46), Fig. 8). The tensor-like method has smaller but less
direction-dependent limits (Fig. 9). On a Gaussian advected diagonally, with the CFL
number reduced so that the time error does not dominate, the final $L^1$ orders of the
averages are $2.98$, $4.02$, $4.98$, $6.01$, $7.00$ (Table 4); a linear-acoustics sine wave
([linear acoustics tests](/benchmarks/linear-acoustics-tests.md)) and a Mach $0.1$
[Gresho vortex](/benchmarks/gresho-vortex.md) are compared qualitatively (§5.2–5.3). Only
smooth problems are run; limiting is left to future work, with Duan et al. above named
for third order (§5, §6). The authors recall that the multiple Runge–Kutta stages widen
the effective stencil of generalized AF, which Roe linked to a reduced maximal CFL
number, against the one-stage classical AF (§1).

## Bicharacteristic evolution operators for systems

Exact evolution formulas exist only for a few linear systems, acoustics above all.
[Chudzik et al. (2024)](/sources/chudzik-2024.md) update the point values of the Cartesian AF
with **approximate evolution operators from the method of bicharacteristics**, the
evolution-Galerkin (EG) operators of Lukáčová-Medvid'ová, Morton and Warnecke, and so extend
third-order AF to systems for which no exact formula is available (§1, §4). The
bicharacteristic representation of a linear system $\partial_tu+\sum_dA^{(d)}\partial_{x_d}u=0$
writes the value at the apex $P=(x,y,t^{n+1})$ of a cone as an average, over all directions of
the unit circle, of characteristic variables taken at the footpoints at $t^n$, plus a mantle
integral of the off-diagonal terms (Eqs. (17)–(20)). The authors write acoustics as
$\partial_tp+c\nabla\cdot v=0$, $\partial_tv+c\nabla p=0$ (Eq. (1)). Let $\varphi$ be the angle
on the base circle, $Q(\varphi)=(x+c\Delta t\cos\varphi,\,y+c\Delta t\sin\varphi,\,t^n)$ its
points and $P'=(x,y,t^n)$ its centre (page-local symbols). Trapezoidal integration in time,
Butler's trapezoidal integration of the pressure equation along the cone axis, a lemma on
periodic integrands and the midpoint rule remove the mantle terms to third order, which leaves
the **EG2** operator (Eq. (28)):

$$\begin{aligned}
p(P)&\approx\frac1\pi\int_0^{2\pi}\big(p-v_1\cos\varphi-v_2\sin\varphi\big)(Q(\varphi))\,d\varphi-p(P'),\\
v_1(P)&\approx\frac1\pi\int_0^{2\pi}\Big(-p\cos\varphi+v_1\big(2\cos^2\varphi-\tfrac12\big)+2v_2\sin\varphi\cos\varphi\Big)(Q(\varphi))\,d\varphi,\\
v_2(P)&\approx\frac1\pi\int_0^{2\pi}\Big(-p\sin\varphi+2v_1\sin\varphi\cos\varphi+v_2\big(2\sin^2\varphi-\tfrac12\big)\Big)(Q(\varphi))\,d\varphi .
\end{aligned}$$

EG2 integrates only over the base circle, while the exact representation also integrates over
the mantle of the cone and Eq. (7) over a disc; on the AF reconstruction the circle integrals
are evaluated exactly, quadrant by quadrant (Appendix A, Eqs. (40)–(42)).
**Theorem 4.1:** an AF method for two-dimensional acoustics that updates the point values with
EG2 is third order in space and time for sufficiently smooth initial data (§4.1).

**Linear stability.** On a doubly periodic $16\times16$ grid the authors compute the eigenvalues
of the one-step matrix acting on the $12$ unknowns per cell (three variables, four degrees of
freedom) (§5.1, Table 2, Appendix A). With $\nu=\max(c\Delta t/\Delta x,c\Delta t/\Delta y)$:

| point-value operator | order | stable for | spectral radius just above the limit |
|---|---|---|---|
| exact, Eq. (7); Eymann–Roe, Eq. (4), exact for constant vorticity | 3 | $\nu\le0.5$ (§5.1, not in Table 2) | — |
| EG2, Eq. (28) | 3 | $\nu\le0.279$ | $1.002909442688$ at $\nu=0.28$ |
| EG4 | 2 | $\nu\le0.154$ | $1.000007260910$ at $\nu=0.155$ |
| EG1, EG3 | 2 | unstable | $1.000098641879$, $1.000049320939$ at $\nu=0.01$ |

The norms of the powers of the one-step matrix stay bounded up to $100$ steps at $\nu=0.279$ for
the exact and EG2 operators (Figs. 5–6). The authors call EG2 "the best candidate" for AF (§5.1)
and note the reversal against piecewise-constant finite volumes, where EG3 had outperformed
the other EG operators (Remark 4.2).

**Accuracy on non-irrotational data.** On a new periodic acoustic test whose velocity is not
curl-free (Example 5.1, $t=0.1$, $L^1$, $64^2$–$256^2$), EG2 at $\nu=0.267$ gives observed
orders $2.92$ ($p$), $2.97$ ($v_1$, $v_2$); the Eymann–Roe operator at $\nu=0.457$ gives $2.99$
in $p$ but $2.00$ in the velocity; the exact operator (7) gives $2.99$ in $p$ and $2.44$ in the
velocity (Tables 3–4). With the exact operator the velocity order between $64^2$ and $128^2$
depends on the final time, from $1.9997$ at $t=0.4$ to $2.9969$ at $t=0.9$ (Table 5); the
authors note that Samani and Roe reported a similar effect (§5.2). On the stationary vortex the
exact operator keeps the discrete steady state, EG2 does not but is more accurate than
Eymann–Roe up to $t=100$ (Example 5.2, Figs. 8–10).

**Maxwell equations.** The source-free two-dimensional Maxwell equations decouple into two
acoustic systems after a scaling of the fields by $\sqrt\epsilon$, $\sqrt\mu$ (Eqs. (10)–(14)),
and both divergences become curls of the acoustic velocities. **Theorem 3.1:** AF for the
source-free 2D Maxwell equations is obtained by solving two acoustic systems; with the exact
operator (7) it is third order and its solutions satisfy $\nabla\cdot\mathbf E=0$,
$\nabla\cdot\mathbf B=0$ (§3; page-local field symbols). The proof rests on curl preservation
by the acoustic solver, argued from the stationarity-preservation result. The convergence study
on Gaussian plane waves ($t=0.1$, $\nu=0.457$, $64^2$–$256^2$) prints $L^1$ orders at $256^2$ of
$2.9862$ and $2.9927$ for the out-of-plane components and $2.3797$, $2.7694$ for the in-plane
components (Table 1).

**Linearised Euler equations.** With the EG2 operator for the linearised Euler equations in
primitive variables $(\rho,v_1,v_2,p)$, frozen at a state with sound speed $c'$ and velocity
$(v'_1,v'_2)$ (page-local primes, Eqs. (31)–(33)), the circles have radius $c'\Delta t$ and are
centred at the upstream point $(x-v'_1\Delta t,\,y-v'_2\Delta t)$. The authors describe the result
as the first unsplit AF method for the linearised Euler equations (§6, Conclusions). An exact
operator would need derivatives of the reconstruction across interfaces, while EG2 only needs
exact integrals on circle segments (Remark 6.1). The observed stability limit is the acoustic
one, $\max(\lvert v'_1\rvert+c',\lvert v'_2\rvert+c')\Delta t/\Delta x\le0.279$, in all tests
(empirical, §6). Density advection gives $L^1$ orders $2.988$ and $2.991$ at $256^2$, with
$p,v_1,v_2$ constant to machine precision; a smooth two-pulse problem gives $2.97$–$2.98$ in all
variables (Tables 6–7).

**Nonlinear Euler equations.** The averages of the conserved variables are updated by the
Simpson finite-volume formula; the point values of the **primitive** variables are updated by the
linearised EG2 operator, linearised locally at each point and iterated (§7, Algorithm 1). The
half-step value is iterated $L+1$ times over $\Delta t/2$ with the Jacobians frozen at the previous
iterate, and its last iterate starts the same iteration over $\Delta t$. The primitive averages
needed for the primitive reconstruction come from the conservative reconstruction evaluated at
the cell centre and Simpson's rule over the nine nodes. The method ignores the curvature of the
characteristic cone, which Barsukow showed must be accounted for to reach third order for 1D
nonlinear systems, so full third order is not expected (§7). Observed $L^1$ orders: $2.987$ on
density advection with $L=0$ (Table 8); on the Kadioglu–Klein–Minion smooth vortex, measured
against the next finer grid, $2.62$–$2.83$ with $L=0$ (falling to $2.43$ at $512^2$) and $2.65$,
$2.89$, $2.93$, $2.82$ with $L=1$ (Table 9, density, $\nu\le0.275$). The
[Gresho vortex](/benchmarks/gresho-vortex.md) and a
[two-dimensional Riemann problem](/benchmarks/two-dimensional-riemann-problems.md) are run
without limiters (Examples 7.2, 7.4); every computation of the paper is unlimited (§5.4, §7).
The implementation is in [ForestClaw](/software/forestclaw.md).

## Adaptive mesh refinement

[Calhoun et al. (2023)](/sources/calhoun-2023.md) present what they call the first
implementation of AF on adaptively refined Cartesian grids (Abstract), as a solver in
ForestClaw: quadtree patch-based AMR on p4est, fixed-size patches ($16\times16$ in all tests),
refinement ratio 2 and adjacent quadrants differing by at most one level (§3). The
AF-specific ingredients are:

- **Coarse to fine:** the coarse biquadratic reconstruction is evaluated at the fine
  point-value locations, and the fine averages are computed by the 2D Simpson rule, which is
  exact for the reconstruction, so the four fine averages sum exactly to the coarse one and
  conservation holds (§3.1, Fig. 4).
- **Fine to coarse:** the coarse average is the mean of the four fine averages; coarse point
  values are copied from the fine vertex values, and fine edge values at no coarse location
  are discarded (Fig. 3).
- **Subcycling** with $\Delta t_{\ell+1}=\Delta t_\ell/2$ on level $\ell$, without time
  interpolation of coarse ghost data, unlike Berger–Oliger–Colella: two ghost layers are
  reconstructed, the first one is advanced together with the interior, and at synchronized
  time levels the ghost data are replaced by averaged or interpolated neighbour data (§3.2,
  Figs. 5–6).
- **Refluxing** à la Berger–Colella: at coarse–fine interfaces coarse and fine cells are both
  updated with the fluxes of the finer grid (§3.2).

The tests (smoothed-disc advection, solid-body rotation, swirl flow, 2D Burgers, acoustics)
show third-order $L^1$ convergence on AMR grids. Refinement that follows the solution gives
the accuracy of the uniform grid at the finest level (smoothed disc: $8.47\times10^{-6}$ and
$1.07\times10^{-6}$ on levels 3–5 and 3–6 against $8.45\times10^{-6}$ and $1.07\times10^{-6}$ on
uniform levels 5 and 6; observed orders $2.98$–$2.99$), while fixed diagonal refinement matches
the coarser uniform grid (Table 1). Subcycling does not change the swirl-flow accuracy
significantly (Table 3). For 2D Burgers after shock formation, unlimited AF oscillates along
the curve where the characteristic speed changes sign; the bound-preserving limiter of Helzel
et al., applied where the refinement criterion holds, removes the oscillations (§4.4, Fig. 12).
With the stationarity-preserving acoustic operator of Barsukow et al., the AMR solver becomes
unstable; with the Eymann–Roe operator the stationary vortex stays accurate to $t=100$ on
levels 3–5 although the scheme is not stationarity preserving (§4.6, Conclusions).

### Constant states for variable-velocity transport

For $\partial_tu+\partial_x(v_1u)+\partial_y(v_2u)=0$ with divergence-free velocity, Calhoun et
al. introduce AF variants that preserve constant states (§4.2–4.3). For solid-body rotation
the characteristics are traced exactly, and the flux of a constant state through an $x$-edge
depends only on $y$ and through a $y$-edge only on $x$, so the flux differences cancel
(Remark 4.1). For a time-dependent swirl with stream function $\Psi(x,y,t)$ (page-local), the
velocities are discrete differences of $\Psi$,

$$v_1(x,y,t)=-\frac{\Psi(x,y+\Delta y/2,t)-\Psi(x,y-\Delta y/2,t)}{\Delta y},\qquad v_2(x,y,t)=\frac{\Psi(x+\Delta x/2,y,t)-\Psi(x-\Delta x/2,y,t)}{\Delta x},$$

(Eq. (25)), and the flux freezes the velocity at the edge midpoint while Simpson's rule
integrates the point values (Eqs. (26)–(28)). **Theorem 4.2:** this AF preserves constant
states on regular Cartesian grids, because the update of a constant reduces to differences of
$\Psi$ at the four cell corners that cancel. **Corollary 4.3:** constant states are also
preserved on AMR grids with global time stepping, since the coarse flux at a coarse–fine edge
equals the mean of the two fine fluxes. With subcycling the intermediate-time fine fluxes are
not balanced by coarse fluxes: constant data on levels 3–4 have error $10^{-13}$ at $t=1$ with
subcycling against about $10^{-16}$ without (§4.3). See
[free-stream preservation](/properties/free-stream-preservation.md).

## Positivity-preserving flux limiting of the fully discrete method

[Kiechle, Chudzik & Helzel (2025)](/sources/kiechle-2025.md) use the fully discrete
Cartesian AF above (Simpson fluxes in space and time, point values by backward
characteristic tracing with classical RK4) for variable-coefficient advection in
divergence-free velocity fields, a guiding-centre model and the 1+1-dimensional
Vlasov–Poisson system (§2–4). The earlier bound-preserving reconstruction of Chudzik,
Helzel & Kerkmann (2021), discontinuous across interfaces, reduces the oscillations of the unlimited scheme but is
not exactly bound preserving, because Simpson's rule is not exact for piecewise quadratic
functions (§3.1.1). Their limiter instead blends each interface flux with a global
Lax–Friedrichs flux, the coefficient chosen from a four-way convex split of the 2D update;
nonnegative averages are guaranteed for CFL numbers up to $\tfrac14$
([positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)).
On the Vlasov–Poisson two-stream instability the limited and unlimited schemes both
converge with order $2.97$ (Table 1). Kiechle et al. compare it with the PAMPA flux limiter
below, which preserves both bounds (Remark 3.2).

## PAMPA: bound preservation by blending

[Abgrall et al. (2026)](/sources/abgrall-2026.md) work with the
[PAMPA scheme](/methods/pampa-scheme.md), Abgrall's method-of-lines relative of
Active Flux with the same degrees of freedom (averages and shared interface point
values) and the same parabola on each cell. The point values are evolved by
upwind residuals $a^\pm$ times the one-sided derivatives of the two cell parabolas
at the node, the Jacobian split $R\Lambda^\pm L$ for systems (§2, Eqs. (2.6)–(2.9)).
Unlike the limiting of Abgrall & Barsukow (2023) described above, which only
lowers the order of the point-value update and never limits the averages, they limit both a priori: the
average flux is blended with a local Lax–Friedrichs flux, and each of the two
residuals of a point value is blended separately with a first-order residual that
mixes the point value and the adjacent average. Both updates are then convex
combinations of bar-state-type intermediate states, and closed-form coefficients
make the scheme bound preserving for scalar laws and positivity preserving for
the Euler equations (Props. 3.1–3.2, §3.4). They state that their scheme does not
show the transonic difficulties met by
[Duan, Barsukow & Klingenberg's](/sources/duan-2025.md) generalized
Active Flux, which needed careful flux vector splitting (section above), and that it
needs no explicit reconstruction inside the cell (§1, Ex. 2, Conclusions). The
Burgers self-steepening shock of the transonic discussion above is their
Example 2 ([Burgers tests](/benchmarks/burgers-equation-tests.md)).

## Qualifications

- Abgrall & Barsukow's arbitrary-order variants are one-dimensional; multi-dimensional
  extensions are deferred (§1, §7). Barsukow et al. (2026) supply the 2D Cartesian
  extension for smooth problems only, with stability shown by numerical spectra on small
  periodic grids up to order 7 and unisolvence checked by computer algebra up to order 7,
  without a proof for general $N$ (§4.1, §3.3.2). The Cartesian AMR method of Calhoun et
  al. is third order.
- The link of AF to van Leer's 1977 paper "Towards the ultimate conservative difference
  scheme. IV" is stated with different strength: Kiechle et al. call AF "in its simplest
  form for one-dimensional linear advection" "equivalent with van Leer's scheme V"
  presented there (§1), Barsukow et al. say AF was "inspired by van Leer's scheme V" (§1),
  and Duan et al. that it "was inspired by" that paper, without naming a scheme
  (Introduction). All three cite the same paper; no source disputes another.
- Duan et al.'s bound-preservation theorem assumes the time-step condition at every
  Runge–Kutta stage, while the limiter is evaluated at $t^n$; their implementation halves
  $\Delta t$ and restarts the step when a stage violates it (Remark 4.2). Their van
  Leer–Hänel splitting is printed in a single form, with no case distinction in the Mach
  number, and the paper does not discuss $\lvert M\rvert\ge1$; for $M>1$ the printed mass
  component of $f^-$, $-\tfrac14\rho c(M-1)^2$, is nonzero, so the printed form alone does
  not give $f^-=0$ in supersonic flow *(compiler check, not in the sources)*.
- Barsukow et al. print the exact acoustics solution with $v=\tfrac1c\sin(2\pi ct)(\cos2\pi x,\cos2\pi y)$
  for $p=\tfrac1c\cos(2\pi ct)(\sin2\pi x+\sin2\pi y)$, which does not satisfy
  $\partial_tp+c\nabla\cdot v=0$ (their system, with $\partial_tv+c\nabla p=0$); a minus sign
  on $v$, or on $p$ as Calhoun et al. (2023) print it (Eq. (31)), is needed *(compiler
  check, not in the sources)*. The comparison at $t=5$, where $v=0$, is unaffected (§5.2).
- Calhoun et al.'s Table 4 (acoustics, arXiv v2) prints observed orders for the AMR rows that
  do not follow from its own errors: $\log_2(1.64\times10^{-4}/2.06\times10^{-5})=2.99$ for $p$
  and $\log_2(3.33\times10^{-5}/3.87\times10^{-6})=3.11$ for $v$, against the printed $3.1045$ and
  $2.8564$; the uniform rows agree within rounding *(compiler check, not in the sources)*.
  The errors themselves show third order.
- Calhoun et al.'s §4.2 speaks of the error "after a half rotation" while Table 2 is at $t=2$,
  one full period of their rotation (§4.2, Table 2).
- For the Euler equations variant B uses the third-order approximate evolution operator,
  so it is formally third order in time, which the authors liken to RK3 with a high-order
  spatial method (§4.5.3).
- The preprint prints the moment-difference error as $\mathcal O(\Delta x^n)$ (Eq. (111)),
  while its own §3.1 rule requires only order $n-1$; *compiler check, not in the sources:*
  MD5 is exact on $\mathbb P^4$ and not on $\mathbb P^5$, so its error is
  $\mathcal O(\Delta x^4)$ for the fifth-order method, consistent with §3.1.
- Chudzik et al.'s Theorem 3.1 states third order for Maxwell AF with the exact operator,
  while their Table 1 prints in-plane orders that fall with refinement, $2.5720\to2.3797$ and
  $2.8878\to2.7694$, without comment (§3.1); the theorem's divergence claim names no discrete
  divergence and no divergence errors are shown. The exact operator also loses velocity order
  on Example 5.1 (Tables 4–5).
- Chudzik et al. correct a coefficient of the Kadioglu–Klein–Minion vortex pressure polynomial
  (degree 36): $-\tfrac{269}{15}r^{30}$, not $-\tfrac{259}{15}r^{30}$ (Example 7.3). *(Compiler
  check, not in the sources.)* Integrating $dp/dr=\rho v_\varphi^2/r$ with
  $v_\varphi=1024(1-r)^6r^6$ and $\rho=\rho_c+\tfrac12(1-r^2)^6$, the $r^{30}$ coefficient divided
  by $1024^2$ is $-\tfrac{269}{15}$ and the polynomial has degree 36.
- Chudzik et al. call the linearised-Euler advection cases $v'_1=v'_2=0.5$ and $1$ (with $c'=1$)
  "supersonic" and "subsonic" respectively (Example 6.2); with speeds $0.71$ and $1.41$ the order
  is reversed *(compiler check, not in the sources)*. Their §7 prints the flux at a node with the
  components of the conserved state instead of the $x$-flux (Eq. (38) context).
- The Sod tests run 100 cells to $t=0.1$ with CFL $0.25$ (variant A), $0.5$ (B) and $0.01$
  (C); initial states and $\gamma$ are not printed (Figs. 19, 24, 28); see
  [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md).

# Citations

- [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) — §§1–7, Defs. 2.1, 2.2, 4.1, 5.1, Thms. 2.1, 2.2, 4.1, 4.2, Eqs. (11), (23)–(24), (37), (43), (47)–(49), (53), (100)–(115), Tables 1–2, Figs. 16–28 (author preprint).
- [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) — §§1–4, Eqs. (1)–(15), (25)–(28), Remark 4.1, Thm. 4.2, Cor. 4.3, Tables 1–4, Figs. 3–6, 12, 16 (arXiv v2).
- [Abgrall et al. (2026)](/sources/abgrall-2026.md) — §1; §2, Eqs. (2.6)–(2.9); §3, Props. 3.1–3.2; §3.4; Ex. 2.
- [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) — arXiv v3: §§2–4, Eqs. (6)–(12), (20)–(24), Def. 4.1, Prop. 4.2, Thm. C.1, Remarks 2.1–2.2, 4.2–4.5, 5.1, C.1; Examples 5.1–5.10, D.1, D.3, D.7; Table 1.
- [Barsukow et al. (2026)](/sources/barsukow-2026.md) — arXiv v2: §1; §3, Eqs. (7)–(36), Defs. 1–2, Table 2; §4.1–4.2, Eqs. (42)–(46), Table 3, Figs. 8–9; §5, Table 4; §6.
- [Kiechle, Chudzik & Helzel (2025)](/sources/kiechle-2025.md) — §1; §2, Eqs. (2)–(6); §3.1.1; §3.2, Remark 3.2; §4.4.1, Table 1.
- [Chudzik, Helzel & Lukáčová-Medvid'ová (2024)](/sources/chudzik-2024.md) — §§1–7, Eqs. (1), (4), (6), (7), (10)–(14), (17)–(20), (28), (31)–(33), (38), Thms. 3.1, 4.1, Remarks 4.2, 6.1, Algorithm 1, Tables 1–9, Examples 5.1–5.2, 6.2–6.3, 7.1–7.4, Appendix A.
