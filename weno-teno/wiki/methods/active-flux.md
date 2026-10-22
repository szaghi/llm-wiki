---
type: Method
title: "Active Flux"
description: "Active Flux evolves cell averages conservatively with fluxes from point values shared at cell interfaces, giving a globally continuous reconstruction without Riemann solvers; Abgrall and Barsukow extend it to arbitrary order through larger stencils, extra point values or extra moments."
status: established
aliases: [AF, active point value method, high-order Active Flux]
tags: [finite-volume, reconstruction, characteristic, limiting]
timestamp: 2026-10-21T12:00:00Z
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

## Qualifications

- One-dimensional only; multi-dimensional extensions are deferred (§1, §7).
- For the Euler equations variant B uses the third-order approximate evolution operator,
  so it is formally third order in time, which the authors liken to RK3 with a high-order
  spatial method (§4.5.3).
- The preprint prints the moment-difference error as $\mathcal O(\Delta x^n)$ (Eq. (111)),
  while its own §3.1 rule requires only order $n-1$; *compiler check, not in the sources:*
  MD5 is exact on $\mathbb P^4$ and not on $\mathbb P^5$, so its error is
  $\mathcal O(\Delta x^4)$ for the fifth-order method, consistent with §3.1.
- The Sod tests run 100 cells to $t=0.1$ with CFL $0.25$ (variant A), $0.5$ (B) and $0.01$
  (C); initial states and $\gamma$ are not printed (Figs. 19, 24, 28); see
  [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md).

# Citations

- [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) — §§1–7, Defs. 2.1, 2.2, 4.1, 5.1, Thms. 2.1, 2.2, 4.1, 4.2, Eqs. (11), (23)–(24), (37), (43), (47)–(49), (53), (100)–(115), Tables 1–2, Figs. 16–28 (author preprint).
