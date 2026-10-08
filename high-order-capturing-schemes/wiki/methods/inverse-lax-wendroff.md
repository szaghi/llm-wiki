---
type: Method
title: "Inverse Lax–Wendroff numerical boundary treatment"
description: "Ghost-point values for wide-stencil high-order finite differences on Cartesian grids cut by an arbitrary boundary: a Taylor expansion from the boundary point whose normal derivatives come from the boundary data through the PDE (inflow) or from extrapolation (outflow), stable under the periodic CFL limit for any cut-cell distance."
status: established
aliases: [ILW, simplified inverse Lax-Wendroff, SILW, inverse Lax-Wendroff procedure, cut-cell boundary treatment]
tags: [boundary-treatment, finite-difference, weno, stability, cut-cell]
timestamp: 2026-10-08T00:00:00Z
---

# Inverse Lax–Wendroff numerical boundary treatment

**The problem** ([Li, Shu & Zhang (2016)](/sources/li-2016.md), §1;
[Lu et al. (2016)](/sources/lu-2016.md), §1). A
[WENO](/methods/weno.md) or upwind-biased finite-difference stencil
needs values at ghost points beyond the boundary, and on a Cartesian
grid the boundary need not pass through grid points. Outflow ghost
values from Lagrange extrapolation are usually stable. Inflow is the
hard case, especially when the first grid point lies very close to the
boundary ($C_a \to 0$). This is the "cut-cell" problem, which leads to
instability or an extremely small time step. The alternatives are
body-fitted or overlapping meshes, embedded-boundary methods (second
order, then fifth order by Baeza et al. with filtered Lagrange
extrapolation), and immersed-boundary forcing. ILW resembles
immersed-boundary methods but does not change the PDE.

**The procedure** (Tan and Shu 2010, as summarized by
[Li, Shu & Zhang (2016)](/sources/li-2016.md), §2.3). With
$x_0 = a + C_a h$, assign each ghost point by a Taylor expansion about
the boundary,
$$u_{-\varsigma} = \sum_{k=0}^{n_{\mathrm b}-1}\frac{u^{*(k)}\,\left((C_a - \varsigma)h\right)^k}{k!},$$
which is $n_{\mathrm b}$-th order if each $u^{*(k)}$ is order
$n_{\mathrm b} - k$. At an inflow boundary of $u_t + f(u)_x = 0$, the
PDE converts normal derivatives into time derivatives of the data
$g(t)$, the reverse of the Lax–Wendroff procedure, hence the name:
$$u^{*(0)} = g,\qquad u^{*(1)} = -\frac{g'}{f'(g)},\qquad u^{*(2)} = \frac{f'(g)\,g'' - 2f''(g)\,(g')^2}{f'(g)^3},\ \dots$$
(checked on the page image). At an outflow boundary,
$u_{N+\varsigma} = \sum_{j=1}^{n_{\mathrm b}}e_j\,u_{N+1-j}$ with Lagrange
coefficients $e_j = \prod_{l \ne j}\frac{l + \varsigma - 1}{l - j}$. In
multi-D the expansion runs along the boundary normal through each ghost
point, with tangential derivatives from the boundary data
([Lu et al. (2016)](/sources/lu-2016.md), §2.5). Near shocks a
WENO-type extrapolation replaces Lagrange
([Lu et al. (2016)](/sources/lu-2016.md), §3;
[weighted extrapolation](/methods/weighted-extrapolation.md)).

**Simplified ILW (SILW).** The algebra of high derivatives in
multi-D, for systems and for moving boundaries is heavy. SILW obtains
only the first $k_{\mathrm{ILW}}$ of the $u^{*(k)}$ by ILW and
extrapolates the rest from interior points alone. Including the
boundary data in that extrapolant makes the scheme *less* stable
([Li, Shu & Zhang (2016)](/sources/li-2016.md), §2.4).

## Stability

([Li, Shu & Zhang (2016)](/sources/li-2016.md), §§3–5; linear advection,
upwind-biased schemes of orders 3–13, which are the linear-weight
versions of WENO, with SSP-RK3.) Two analyses agree for both the
semi-discrete and the fully discrete schemes. The rigorous one is the
GKS normal-mode analysis of the two quarter-plane problems. The other
visualizes the eigenvalue spectrum of the full matrix.
* Full ILW is stable for every $C_a$ under the same CFL limit as the
  periodic problem. With $g = 0$ all ghost values vanish, so the
  initial–boundary-value problem is as stable as the Cauchy problem.
  Outflow extrapolation is also stable (Goldberg's theorem). That result is
  one-dimensional. On complex 2D domains, where ghost values come from
  interpolation along normals, straight Lagrange extrapolation can turn
  the scheme mildly unstable, as Tan and Shu also observed. This is a
  difference of scope, not a contradiction
  ([weighted extrapolation](/methods/weighted-extrapolation.md);
  [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §§5.2, 6).
* SILW needs $k_{\mathrm{ILW}}$ at least the threshold below, for all
  $C_a$, at the periodic limit $\nu_{\max}$ of SSP-RK3 (Tables 3.1–3.2,
  read from the page images):

  | order | 3 | 5 | 7 | 9 | 11 | 13 |
  |---|---|---|---|---|---|---|
  | $\nu_{\max}$ | 1.62 | 1.43 | 1.24 | 1.12 | 1.04 | 0.99 |
  | minimum $k_{\mathrm{ILW}}$ | 2 | 3 | 4 | 6 | 8 | 10 |

  Below the threshold, instability appears in bands of $C_a$, typically
  but not only small $C_a$. The numerical tests reproduce every
  threshold.
* Nonlinear problems can be more stable. For Burgers with fifth order,
  $k_{\mathrm{ILW}} = 2$ sufficed because the boundary state is small
  relative to the global wave speed, and $k_{\mathrm{ILW}} = 2$ is
  stable at fifth order for $\nu \le 1.02$.
* Time-dependent data inside Runge–Kutta stages must be matched as
  $u^{(1)} \sim g + \Delta t\,g'$ and
  $u^{(2)} \sim g + \tfrac12\Delta t\,g' + \tfrac14\Delta t^2 g''$
  (Carpenter et al.). The naive $g(t^n + \Delta t)$, $g(t^n + \Delta t/2)$
  drops to second order (§2.2;
  [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

## Convection–diffusion and Navier–Stokes

([Lu et al. (2016)](/sources/lu-2016.md).) For
$u_t + f(u)_x = \mu u_{xx}$ the two limits need opposite treatments.
Pure convection takes $u_x$ from ILW and $u_{xx}$ from extrapolation.
Pure diffusion takes $u_x$ from extrapolation and $u_{xx}$ from ILW,
$u^{\mathrm{ilw}}_{xx} = \frac1\mu\left(g' + f'(g)\,u^{\mathrm{ext}}_x\right)$.
The general case blends the two (eqs. 2.10–2.11, checked on the page image):
$$\theta_{\mathrm{ILW}} = \frac{f'(g)^2h^2}{f'(g)^2h^2 + 9\mu^2},\qquad
u_x = \theta_{\mathrm{ILW}}u^{\mathrm{ilw}}_x + (1 - \theta_{\mathrm{ILW}})u^{\mathrm{ext}}_x,\qquad
u_{xx} = (1 - \theta_{\mathrm{ILW}})u^{\mathrm{ilw}}_{xx} + \theta_{\mathrm{ILW}}u^{\mathrm{ext}}_{xx}.$$
* **Systems.** The convective matrix is diagonalized for the
  convection-dominated treatment, imposing characteristic inflow data.
  The diffusion matrix is diagonalized for the diffusion-dominated one,
  and the blending is done per diffusive characteristic field.
* **Navier–Stokes.** The system is incompletely parabolic: there is no
  diffusion in the mass equation. Following Strikwerda and
  Gustafsson–Sundström, it is treated as a hyperbolic equation plus a
  parabolic system. When more conditions are given than the Euler limit needs,
  they are taken in the order $E$, $\rho u$, $\rho$.
* **Results.** Tests run at third order with $C_a = 10^{-6}$. They are
  stable and third order from $\mathrm{Re} = 1$ to $10^6$, including
  mixed regimes and a 45° polygonal boundary. A Mach 3 flow past a
  cylinder on a Cartesian grid captures the bow shock with an isothermal
  no-slip wall.

**Scale dependence.** [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md)
(§1) note that the outflow WENO extrapolation weights of the ILW papers
are neither dimensionless nor scale-independent, which a later
modification overcame, and they propose dimensionless weights
([weighted extrapolation](/methods/weighted-extrapolation.md)).

# Citations

1. [Li, Shu & Zhang (2016)](/sources/li-2016.md), §§1–5 (§2.2–2.5 formulas and Tables 3.1–3.2 read from the page images).
2. [Lu et al. (2016)](/sources/lu-2016.md), §§1–4 (eqs. 2.10–2.11 read from the page image).
3. [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §1.
