---
type: Method
title: "Discontinuous Galerkin method"
description: "The discontinuous Galerkin (DG) semi-discretization of a conservation law with piecewise polynomials of degree N coupled only through numerical fluxes, its Runge–Kutta time stepping and CFL limit, the cell-average update behind bound preservation, and the stabilization families the sources attach to it."
status: established
aliases: [DG, RKDG, Runge–Kutta discontinuous Galerkin, modal DG, nodal DG]
tags: [dg, numerical-flux, limiting, bound-preserving]
timestamp: 2026-10-21T12:00:00Z
---

# Discontinuous Galerkin method

The discontinuous Galerkin (DG) method approximates the solution of
$\partial_tu+\partial_xf(u)=0$ by a function $u_h$ whose restriction to every
cell $I_i$ is a polynomial, $u_h\vert_{I_i}\in\mathbb P^N$, with no continuity
across interfaces. Cells interact only through a two-point numerical flux
$h(u^-,u^+)$ at the interfaces. The design order is $N+1$. For a scalar law
the flux is monotone, and for a system it is an approximate Riemann solver.
With an explicit Runge–Kutta stepper the scheme is called RKDG
([Peng, Sun & Wu (2024)](/sources/peng-2024.md), §2.1, citing Reed–Hill and
Cockburn–Shu).

## Semi-discrete weak form

Multiplying by a test function $v\in\mathbb P^N(I_i)$ and integrating by
parts on $I_i$ gives Peng et al.'s Eq. (2.2):

$$\int_{I_i}\partial_tu_h\,v\,dx=\int_{I_i}f(u_h)\,\partial_xv\,dx-\hat f_{i+1/2}\,v^-_{i+1/2}+\hat f_{i-1/2}\,v^+_{i-1/2},\qquad \hat f_{i+1/2}=h\big(u^-_{i+1/2},u^+_{i+1/2}\big),$$

for all $v\in\mathbb P^N(I_i)$. Here $v^-_{i+1/2}$ is the trace from cell $i$
and $v^+_{i-1/2}$ the trace from cell $i$ at its left face, so both are inner
traces of $I_i$. The ODE system is written $\frac{d}{dt}u_h=\mathcal L(u_h)$.
In several dimensions, on an element $K$ with
$u_h\vert_K\in\mathbb P^N(K)$ (total degree $\le N$), the volume term becomes
$\int_Kf(u_h):\nabla v$ and the boundary term a sum of face integrals of
$h$ against the outward normal (Peng et al. (2024), Eq. (3.3)). Tensor-product
spaces $\mathbb Q^N$ on Cartesian cells are the other common choice
([Cui, Ding & Wu (2024)](/sources/cui-2024.md), §1, §7).

Two families of bases appear in the sources:

- **Modal bases.** These are orthogonal (scaled Legendre) bases, in which the
  zeroth coefficient is the cell average. The OEDG damping step of Peng et
  al. is diagonal in such a basis
  ([OEDG](/methods/oedg.md)).
- **Nodal bases.** These are Lagrange bases at Legendre–Gauss–Lobatto nodes
  $\xi_j$ with collocated quadrature. The result is the
  [DGSEM](/methods/dgsem.md), whose mass matrix is diagonal and whose
  derivative matrix is a
  [summation-by-parts operator](/operators/summation-by-parts-operator.md)
  ([Ranocha et al. (2023)](/sources/ranocha-2023.md), Ex. 2.3;
  [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md),
  §2.1). The nodal setting is the basis of
  [flux differencing](/methods/flux-differencing.md) and of the
  [entropy-stable](/properties/entropy-stability.md) DG schemes.

## Time stepping and the CFL limit

Peng et al. (2024) write the $s$-stage, $r$th-order explicit Runge–Kutta
method in Shu–Osher form,
$u_h^{n,\ell+1}=\sum_{m\le\ell}\big(c_{\ell m}u_h^{n,m}+\Delta t\,d_{\ell m}\mathcal L(u_h^{n,m})\big)$
with $\sum_mc_{\ell m}=1$ (page-local coefficients $c_{\ell m}$, $d_{\ell m}$;
§2.1). The [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) members are the
convex combinations of forward-Euler steps. Rueda-Ramírez et al. (2022) use
three-stage SSP-RK3 at CFL 0.5 in all their tests (§5). Wu & Shu (2023) use
SSP-RK3 at CFL 0.15 ([Wu & Shu (2023)](/sources/wu-2023-b.md), §7).

Cui et al. (2024), Remark 7.7, cite the linear-stability restriction of
$\mathbb P^N$-DG with an $(N+1)$-stage Runge–Kutta method as an empirical
formula. In 2D it reads

$$\Delta t\Big(\frac{a^{(1)}}{\Delta x}+\frac{a^{(2)}}{\Delta y}\Big)\le\frac1{2N+1},$$

with $a^{(d)}$ the maximum wave speed in direction $d$. Peng et al. (2024)
run their OEDG tests at CFL $1/(2N+1)$ (§5). Peng et al.'s Prop. 4.6,
collected from the RKDG stability literature, states for $r$th-order
$r$-stage Runge–Kutta on linear problems that the $L^2$ stability estimate
$\|u_h^{n+1}\|^2\le(1+C_s\Delta t)\|u_h^n\|^2$ (their Assumption 4.5,
page-local constant $C_s$) holds under $\Delta t\le C\,\Delta x^{\kappa}$
with the following exponents:

- $\kappa=1+1/r$ for $r\equiv1\pmod 4$;
- $\kappa=1+1/(r+1)$ for $r\equiv2\pmod4$;
- $\kappa=1$ and $C_s=0$ for $r\equiv3\pmod4$;
- $\kappa=1$ and $C_s=0$ after combining two or three steps for $r\equiv0\pmod4$.

## The cell-average update

Taking $v=1$ in the weak form gives the update of the cell average. It is
identical to a finite-volume scheme. In 1D with forward Euler it reads
$\bar u_i^{n+1}=\bar u_i^n-\frac{\Delta t}{\Delta x}\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big)$
(Cui et al. (2024), Eq. (1.5)). In multi-D the face integrals are evaluated
by Gauss quadrature (Eq. (7.2); Wu & Shu (2023), Eqs. (6.6)–(6.8)). This
identity is the hinge of the Zhang–Shu bound-preserving framework:

1. A [cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
   writes $\bar u_i$ as a convex combination of point values that includes
   the interface traces.
2. The [scaling limiter](/methods/zhang-shu-scaling-limiter.md)
   $\tilde u_h=\theta(u_h-\bar u)+\bar u$ puts those point values in $G$.
3. The update is then a convex combination of first-order bound-preserving
   steps under a CFL condition proportional to the boundary weight
   $\varpi$.

Cui et al. (2024) prove that the classical Gauss–Lobatto decomposition is
optimal in 1D and on $\mathbb Q^N$. On $\mathbb P^N$ it is not, and the
optimal bound-preserving CFL number for balanced directional wave speeds,
$a^{(1)}/\Delta x=a^{(2)}/\Delta y$ (their anisotropy parameter set to zero), is
1.5–1.75 times the classical one.
For example, it is $1/4$ against $1/6$ for $N=2,3$ (Table 1). With a
Lax–Friedrichs flux ($c_0=1$), the optimal bound-preserving CFL number is
weaker than $1/(2N+1)$ for every $N\le9$ except $N=8$ (Remark 7.7). See
[bound preservation](/properties/bound-preservation.md).

Wu & Shu (2023) apply the same cell-average route to multicomponent ideal
MHD. There the bound-preserving property of the DG cell average requires a
discrete divergence-free condition on $B$. They obtain it with a locally
divergence-free DG basis plus a discretized Godunov-symmetrization source
term. The resulting high-order scheme is provably bound-preserving under
$(1+\varepsilon_B)\nu_W\le\mathsf w^{\mathrm{GL}}_1$ (Thm 6.4). Here
$\nu_W$ is their two-directional CFL number, $\mathsf w^{\mathrm{GL}}_1$ the
first weight of the $\lceil(N+3)/2\rceil$-point Gauss–Lobatto rule, and
$\varepsilon_B$ the ratio of the normal-$B$ jump terms to the viscosity
parameters (all three page-local). Their tests use the third-order case
$N=2$. See
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

## Stabilization of discontinuous solutions

Unmodified DG oscillates at discontinuities, and the sources attach four
distinct remedies.

- **Limiters that overwrite troubled cells.** A
  [troubled-cell indicator](/definitions/troubled-cell-indicator.md) flags
  cells, and a WENO or Hermite-WENO reconstruction replaces the polynomial
  there. Cui et al. (2024) apply the Qiu–Shu WENO limiter before the
  bound-preserving limiter in their Examples 3–5 (§8). Wu & Shu (2023) apply
  a locally divergence-free WENO limiter in cells flagged by the KXRCF
  indicator (§7).
- **Blending with a low-order scheme.** The nodal DG update is convexly
  blended with a compatible subcell finite-volume update, element by element
  or interface by interface, with a priori or a posteriori blending
  coefficients
  ([subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
  [convex limiting](/methods/convex-limiting.md); Rueda-Ramírez et al.
  (2022)).
- **Damping and filtering.** Oscillation-free DG adds stiff damping terms to
  the semi-discrete system. The [OEDG](/methods/oedg.md) method of Peng et al.
  (2024) instead solves the damping step exactly after each Runge–Kutta stage
  as a modal filter. This preserves the cell average and the scale and
  evolution invariance. For linear advection it keeps the optimal
  fully-discrete $L^2$ estimate $O(\Delta x^{N+1}+\Delta t^r)$ under
  $N>d/2$, $r>d/2+1$, a stable underlying RKDG scheme and a lower bound on
  the deviation of $u_h$ from its average (Thm 4.1).
- **Artificial viscosity.** See [artificial viscosity](/methods/artificial-viscosity.md).

[Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) contrast the first remedy
with their continuous-Galerkin scheme, which never modifies the finite
element solution. They use the HWENO reconstruction only to compute a
blending factor between high- and low-order stabilization, and they propose
this as an alternative to WENO limiters for DG (§1, Remark 2;
[WENO-stabilized continuous Galerkin](/methods/weno-stabilized-continuous-galerkin.md)).
Their claim that the hybrid is "easier to analyze than DG-WENO schemes" is
stated, not demonstrated (§8).

## Accuracy

Peng et al. (2024) observe optimal order $N+1$ for advection, Burgers and
1D Euler. They also observe order $N+2$ superconvergence of cell averages and
downwind point values for OEDG (Table 1). This superconvergence is proved
only for semi-discrete oscillation-free DG, not for the fully discrete OEDG
(§5.1). Cui et al. (2024) observe order $N+1$ for $N=2,4,6,8$ with the
scaling limiter active (Tables 3–6). At equal accuracy the optimal
decomposition cuts CPU time by 20–50 % (§8).

## Qualifications

- The CFL bound $1/(2N+1)$ is cited by Cui et al. (2024) as an empirical
  formula, not a theorem.
- The sources use different symbols for the degree: Peng et al. and Cui et
  al. write $k$, Ranocha et al. write $p$, Wu & Shu write $K$, and
  Rueda-Ramírez et al. write $N$. All are translated to $N$ here.

# Citations

- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — §2.1 Eq. (2.2), Eq. (3.3), Prop. 4.6, Thm 4.1, §5.1 Table 1.
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — Eq. (1.5), Eq. (7.2), Thm 7.1, Remark 7.7, Table 1, §8.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — Eqs. (6.6)–(6.8), Thm 6.4, §7.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §1, Remark 2, §8.
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2, Ex. 2.3.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1, §5.
