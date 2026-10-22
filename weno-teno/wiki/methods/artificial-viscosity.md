---
type: Method
title: "Artificial viscosity and spectral viscosity"
description: "Artificial viscosity controls oscillations by adding solution-dependent dissipation instead of overwriting the solution; the page covers the nonlinear blend of high-order projection stabilization and low-order isotropic viscosity in continuous finite elements, and the damping of DG modes that acts as an exponential modal filter linked to spectral viscosity."
status: established
aliases: [artificial diffusion, artificial diffusivity, nonlinear stabilization, spectral viscosity, modal filtering, damping, JST-type dissipation]
tags: [limiting, dg, low-dissipation, weno]
timestamp: 2026-10-21T00:00:00Z
---

# Artificial viscosity and spectral viscosity

Artificial viscosity suppresses spurious oscillations by adding a
dissipative term whose strength depends on the solution, rather than by
replacing the solution in troubled cells as limiters do. In the sources of
this bundle it appears in two forms: a **nonlinear blend** of a high-order,
accuracy-preserving stabilization with a low-order isotropic viscosity in
continuous finite elements
([Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md)), and a **damping of the
modal coefficients** of a DG solution, which is the high-order dissipation of
spectral-viscosity and filtering methods
([Peng, Sun & Wu (2024)](/sources/peng-2024.md)). Both are evaluated in
every cell and need no [troubled-cell indicator](/definitions/troubled-cell-indicator.md)
to switch them on.

## Low- and high-order dissipation operators

[Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) (§3) stabilize the
Galerkin form of a scalar law with cellwise forms $s_h^e(u_h,w_h)$ added to
the weak form. Let $\mu_e$ denote the cellwise viscosity coefficient
(page-local; the source writes $\nu_e$, which the registry reserves for the
CFL number), $a_e=\lVert f'(u_h)\rVert_{L^\infty(K_e)}$ the local maximum wave
speed, $h_e$ the cell diameter and $N$ the polynomial degree.

- **Low order** (Eq. (4)): $s_h^{e,L}(u_h,w_h)=\mu_e\int_{K_e}\nabla w_h\cdot\nabla u_h\,dx$,
  $\mu_e=a_eh_e/(2N)$. Isotropic first-order viscosity with an
  $O(h^{1/2})$ consistency error (§3, §6).
- **High order, variational multiscale** (Eq. (5)):
  $\mu_e\int_{K_e}\nabla w_h\cdot(\nabla u_h-g_h)\,dx$, with $g_h$ a continuous
  ($L^2$-projected) approximation of $\nabla u_h$; consistency error
  $O(h^{N+1/2})$. It is equivalent in 1D to a consistent SUPG method (as
  recalled from Lohmann et al.), but it is not symmetric and "may produce
  entropy".
- **High order, symmetric projection form** (Eq. (7)):
  $\mu_e\int_{K_e}(\nabla w_h-g_h(w_h))\cdot(\nabla u_h-g_h(u_h))\,dx$, coercive
  and therefore truly dissipative; a local-projection stabilization.

## Nonlinear blending (JST design in finite elements)

The CG-WENO method of [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md)
blends the two with a cellwise factor $\varsigma_e\in[0,1]$ (page-local; the
source writes $\gamma_e$) (Eq. (8)):
$$s_h^e(u_h,w_h)=\omega_{\mathrm H}\,\varsigma_e\,\mu_e\int_{K_e}(\nabla w_h-\pi_h\nabla w_h)\cdot(\nabla u_h-\pi_h\nabla u_h)\,dx+(1-\varsigma_e)\,\mu_e\int_{K_e}\nabla w_h\cdot\nabla u_h\,dx,$$
with $\pi_h$ the $L^2$ projection of gradients and $\omega_{\mathrm H}\in[0,1]$
a scaling of the high-order part (page-local; 1 in all experiments).
$\varsigma_e=1$ in smooth cells (high-order dissipation only), $\varsigma_e\to0$
in troubled cells (low-order viscosity). The factor is the WENO-deviation
sensor defined on the [troubled-cell indicator](/definitions/troubled-cell-indicator.md)
page; the reconstruction is used only to compute it and never overwrites the
finite element solution, so the semi-discrete scheme keeps the structure of a
continuous Galerkin method (Rem. 2). The authors present the scheme as a
multidimensional, high-order finite element analogue of the
Jameson–Schmidt–Turkel blend of second- and fourth-difference dissipation,
and argue that a nonlinear artificial-diffusion structure is easier to
analyse than DG-WENO schemes that manipulate derivatives directly (§3, §8).
The full method is on
[dissipation-based WENO stabilization](/methods/weno-stabilized-continuous-galerkin.md).

**Consistency** (§6, labelled "preliminary" by the authors). For steady
advection–reaction, the stabilization has, in the worst case, an $O(h^{1/2})$
consistency error; for $u\in C^{N+1}$ and exponent 2 in the sensor,
$\sqrt{s_h(I_hu;I_hu,I_hu)}=O(h^{N+1/2})$, which the authors call optimal for
general meshes. Polynomials of degree $\le N$ are reproduced exactly
(Rem. 6). An a priori estimate follows under an assumed, unverified
Lipschitz-type condition.

## Damping of DG modes as a modal filter

The oscillation-free DG method (Lu, Liu & Shu, as recalled by
[Peng, Sun & Wu (2024)](/sources/peng-2024.md), §1, Eq. (1.2)) adds damping
terms that penalise the deviation of $u_h$ from its lower-order $L^2$
projections, similar in flavour to local projection stabilization. For
discontinuous solutions these terms are very stiff, forcing small explicit
steps or exponential Runge–Kutta integrators. [OEDG](/methods/oedg.md)
splits the damping off and solves it exactly after every stage: with
coefficients frozen at the stage solution and a Legendre basis, the damping
ODE is diagonal and each modal coefficient of degree $l\ge1$ is multiplied by
$$\exp\Big(-\frac{a_i\Delta t}{\Delta x_i}\sum_{m=0}^{l}\sigma_i^m\Big),$$
while the cell average is untouched ($a_i$ the local wave speed at the cell
average, $\sigma_i^m$ dimensionless damping coefficients built from jumps of
the $m$th derivatives; page-local) (Eqs. (2.9)–(2.12)). Higher modes are
damped more, so the damping operator is an exponential **modal filter** with
solution-dependent strength, which links oscillation-free damping to spectral
viscosity and spectral filtering (Rem. 2.3, §1.2). Conservation and the
non-increase of the elementwise $L^2$ norm follow at once (Rems. 2.2–2.3).

## Other uses in the corpus

[Fu (2023)](/sources/fu-2023.md) lists, among hybrid uses of the TENO
discontinuity indicator, an adaptive artificial viscosity for a quintic-spline
scheme (§3.4, ref. [183] there); the review gives no formula.

## Qualifications

- Kuzmin & Vedral analyse only the steady linear advection–reaction problem;
  the observed $L^1$ rate on uniform meshes is $N+1$, against the "optimal"
  $N+1/2$ of the general-mesh estimate (§6–§7).
- In their solid-body-rotation test the high-order-only stabilization has a
  smaller $L^1$ error than the blended method (e.g. $1.47\times10^{-2}$
  against $2.68\times10^{-2}$ for $N=1$) but large overshoots; "superior" in
  the paper means bounded and non-oscillatory, not more accurate (§7.3).
- The dissipation-based schemes do not by themselves guarantee bounds;
  Kuzmin & Vedral suggest algebraic flux correction on top when strict
  bounds are required (§7.4; [convex limiting](/methods/convex-limiting.md)).

# Citations

- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — arXiv v1: §3 (Eqs. (4)–(8)); Rem. 2; §6 (Eqs. (16)–(18), Rem. 6); §7.3–§7.4; §8.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: §1, §1.2 (Eq. (1.2)); §2.2 (Eqs. (2.9)–(2.12)); Rems. 2.2–2.3.
- [Fu (2023)](/sources/fu-2023.md) — §3.4 (adaptive artificial viscosity among hybrid TENO uses, named only).
