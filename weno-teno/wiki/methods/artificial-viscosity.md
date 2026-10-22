---
type: Method
title: "Artificial viscosity and spectral viscosity"
description: "Artificial viscosity controls oscillations by adding solution-dependent dissipation instead of overwriting the solution; the page covers the high-order Jameson–Schmidt–Turkel blend of finite-difference central schemes, the nonlinear blend of projection stabilization and isotropic viscosity in continuous finite elements, graph viscosity, and the damping of DG modes that acts as a modal filter."
status: established
aliases: [artificial diffusion, artificial diffusivity, artificial dissipation, nonlinear stabilization, spectral viscosity, modal filtering, damping, JST-type dissipation, Jameson–Schmidt–Turkel dissipation, graph viscosity]
tags: [limiting, dg, low-dissipation, finite-difference, weno]
timestamp: 2026-10-22T12:00:00Z
---

# Artificial viscosity and spectral viscosity

Artificial viscosity suppresses spurious oscillations by adding a
dissipative term whose strength depends on the solution, rather than by
replacing the solution in troubled cells as limiters do. In the sources of
this bundle it appears in four forms: a **blend of low- and high-order
dissipation** switched by a shock sensor, in finite-difference central
schemes ([Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md)) and in
continuous finite elements ([Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md));
a first-order **graph viscosity** that makes a low-order scheme
invariant-domain preserving ([Pazner (2021)](/sources/pazner-2021.md));
and a **damping of the modal coefficients** of a DG solution, which is the
high-order dissipation of spectral-viscosity and filtering methods
([Peng, Sun & Wu (2024)](/sources/peng-2024.md)). The JST-type, finite
element and modal forms are evaluated in every cell; the first two need a
[shock sensor](/definitions/troubled-cell-indicator.md) only to set the
weight of the low-order part.

## High-order Jameson–Schmidt–Turkel dissipation (finite differences)

**Odd-order schemes as central plus dissipation.**
[Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) (§3, Eqs.
(20)–(28)) start from the Lerat–Corre family of odd-order schemes, as
recalled: with $\Delta^mu_{i+1/2}$ the $m$-th undivided difference centred
at the interface (registry §10, here centred at $x_{i+1/2}$) and
$\mu f_{i+1/2}=\tfrac12(f_i+f_{i+1})$ (page-local), the interface flux
$$\hat f_{i+1/2}=\Big[\Big(1-\sum_{p=0}^{P}a_p\Delta^{2+2p}\Big)\mu f\Big]_{i+1/2}+\frac{a_P}{2}\,\lvert Q\rvert\,\Delta^{2P+3}u_{i+1/2}$$
(signs as the explicit members (25)–(28) print them; $P$, $a_p$, $Q$
page-local, $Q$ not the SBP matrix of the registry) is of order $2P+3$ on $2(P+2)+1$ points, with
$a_0=\tfrac16$, $a_1=-\tfrac1{30}$, $a_2=\tfrac1{140}$, $a_3=-\tfrac1{630}$.
It is a central difference of order $2(P+2)$ of the flux derivative plus an
artificial viscosity of order $2P+3$, whose leading truncation error is an
even derivative, $\frac{a_P}{2}\Delta x^{2P+3}\partial_x^{2(P+2)}u$, and
therefore dissipative (Eq. (24)); the dispersion error is exactly that of
the central scheme. $Q$ is a dissipation matrix: Roe's $\lvert A\rvert$, or
the spectral radius $a$ (Rusanov). The authors take the scalar $a$ to avoid
the non-unique and costly extension of Roe averaging to real and
multi-species gases (Eq. (29)).

**The adaptive blend** (§3, Eqs. (30)–(35)). The scheme adds a
second-order dissipation switched by the sensor $\Xi_i$ (page-local) of the
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) page
(Ducros × Jameson × Bhagatwala–Lele), in Jameson–Schmidt–Turkel form:
$$\mathcal D_{i+1/2}=a_{i+1/2}\Big[\varepsilon_2\,\Delta^1u+(-1)^{P+1}\varepsilon_{2(P+2)}\,\Delta^{2P+3}u\Big]_{i+1/2},\qquad
\varepsilon_{2,i+1/2}=k_2\max(\Xi_i,\Xi_{i+1}),\quad
\varepsilon_{2(P+2),i+1/2}=\max\big(0,\ k_{2(P+2)}-k_\varepsilon\,\varepsilon_{2,i+1/2}\big)$$
($\mathcal D$, $\varepsilon_2$, $\varepsilon_{2(P+2)}$, $k_2$,
$k_{2(P+2)}$, $k_\varepsilon$ page-local; the source's JST notation
$\varepsilon^{(2)}$, $\varepsilon^{(4)}$). Where the sensor is on, the
second-order term grows and the high-order one is switched off; with
$k_2=0$ and $k_{2(P+2)}=\lvert a_P\rvert/2$ the odd-order upwind scheme is
recovered. The production scheme is the ninth-order member, $P=3$:
$$\mathcal D=a\big[\varepsilon_2\Delta^1u+\varepsilon_{10}\Delta^9u\big],\qquad \varepsilon_{10}=\max\big(0,\ k_{10}-\tfrac1{105}\varepsilon_2\big),$$
with $k_2=1$ and $k_{10}=1/1260$, the upwind value $\lvert a_3\rvert/2$, by
default, and $k_2=2$, $k_{10}=1/630$ on the shock tubes. The design aim is a
truncation error dominated by dissipation, which limits both spurious
oscillations and the activation of the low-order term (§1).

**Evidence** (§4–§5). The ninth-order dissipation acts only above a
reduced wavenumber $\vartheta\approx0.35\pi$, fewer than six points per
wavelength, and leaves larger scales almost untouched (Fig. 1;
[numerical dissipation](/definitions/numerical-dissipation.md)). On the
[isentropic vortex](/benchmarks/isentropic-vortex.md) ninth order appears
only when the CFL number is below about 0.0125, because the third-order
Runge–Kutta error dominates otherwise (§4.1). On the compressible
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) (Re 1600,
$M=0.1$–1, $64^3$–$1024^3$) the scheme behaves as an implicit LES without
energy pile-up, and the order of the dissipation matters more than that of
the convective flux: third-order dissipation with up to tenth-order
convective fluxes gives nearly identical results, while ninth-order
dissipation on $64^3$ is close to third order on $256^3$ (§5.2, Fig. 11).

## Low- and high-order dissipation operators (continuous finite elements)

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

**Nonlinear blending (JST design in finite elements).** The CG-WENO method
of [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) blends the two with a
cellwise factor $\varsigma_e\in[0,1]$ (page-local; the source writes
$\gamma_e$) (Eq. (8)):
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
Sciacovelli et al. also call their finite-difference scheme above a JST
form: both sources keep a high-order dissipation everywhere and trade it,
through a sensor, for a first-order one at shocks.

**Consistency** (§6, labelled "preliminary" by the authors). For steady
advection–reaction, the stabilization has, in the worst case, an $O(h^{1/2})$
consistency error; for $u\in C^{N+1}$ and exponent 2 in the sensor,
$\sqrt{s_h(I_hu;I_hu,I_hu)}=O(h^{N+1/2})$, which the authors call optimal for
general meshes. Polynomials of degree $\le N$ are reproduced exactly
(Rem. 6). An a priori estimate follows under an assumed, unverified
Lipschitz-type condition.

## Graph viscosity (first-order, invariant-domain preserving)

The low-order scheme of [convex limiting](/methods/convex-limiting.md) is an
algebraic artificial viscosity. [Pazner (2021)](/sources/pazner-2021.md)
(§3.1, Eqs. (32)–(35), after Guermond and Popov) adds to a nodal
discretization with coefficients $c_{ij}$ the viscosity
$$d_{ij}=\max\big\{a_{\max}(u_i,u_j,n_{ij})\lVert c_{ij}\rVert,\ a_{\max}(u_j,u_i,n_{ji})\lVert c_{ji}\rVert\big\},\qquad d_{ii}=-\sum_{j\ne i}d_{ij},$$
with $n_{ij}=c_{ij}/\lVert c_{ij}\rVert$ and $a_{\max}$ an upper bound of the
maximum wave speed of the Riemann problem (page-local $c_{ij}$, $d_{ij}$,
$a_{\max}$), which makes the forward-Euler update a convex combination of
bar states. Every connection of the stencil adds viscosity, so on the
dense DGSEM operator, which couples each node to $O(N)$ others, the
low-order method grows more diffusive with $N$ at fixed degrees of
freedom; on a sparsified operator with an $O(1)$ stencil it does not
($N=3,7,15,31$ on 128 degrees of freedom, §3.4, Fig. 1). The modal
smoothness indicator Pazner uses to relax the limiter bounds is taken from
Persson and Peraire's shock-capturing work (§4.4).

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

## Limiters read as artificial viscosity

[Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) state that the
non-oscillatory limiter of the first moment in their hybrid Hermite WENO
scheme "simply induces artificial viscosity": at $\mathrm{Re}=1000$ fewer
cells are flagged than at $\mathrm{Re}=\infty$, and the discontinuities are
slightly sharper (Ex. 4.2, §5). The evidence is a qualitative comparison of
the same scheme at two Reynolds numbers. [Fu (2023)](/sources/fu-2023.md)
lists, among hybrid uses of the TENO discontinuity indicator, an adaptive
artificial viscosity for a quintic-spline scheme (§3.4, ref. [183] there);
the review gives no formula.

## Positions against artificial viscosity

- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) (§1) reject
  artificial-viscosity shock capturing for DG (Persson–Peraire and later
  variants, as recalled) in hyperbolic problems: it lowers performance,
  needs non-physical boundary conditions for the added viscous terms, and
  at strong shocks may need enough viscosity to cut the explicit time step
  significantly. They blend with subcell finite volumes instead
  ([subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)),
  and note that an earlier entropy-stable DG computation of the Io–plasma
  interaction needed artificial dissipation, which their hybrid scheme does
  without (§6.4).
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) fit
  discontinuities with the moving mesh and need neither artificial
  viscosity nor limiters nor WENO reconstruction (§I;
  [implicit shock tracking](/methods/implicit-shock-tracking.md)).
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) take the
  opposite line for turbulent flows: a high-order dissipation applied
  everywhere serves as the subgrid regularization of an implicit LES, and
  the low-order part is confined by the sensor (§3, §5).

## Qualifications

- **Printed slips in Sciacovelli et al. (arXiv v1).** The text defines
  $k_\varepsilon=a_0/a_P$, but Eqs. (33)–(35) print the factors
  $\tfrac15$, $\tfrac3{70}$, $\tfrac1{105}$, which equal $\lvert a_P/a_0\rvert$
  *(compiler check, not in the sources: $\tfrac{1/30}{1/6}=\tfrac15$, $\tfrac{1/140}{1/6}=\tfrac3{70}$, $\tfrac{1/630}{1/6}=\tfrac1{105}$)*;
  the equations, not the sentence, are what the scheme uses. Eq. (23)
  prints the dissipation with $-\frac{a_P}{2}$, while the explicit members
  (25)–(28) carry the sign of $+\frac{a_P}{2}$ (e.g. $+\frac1{12}$ for
  $a_0=\frac16$); the page follows the explicit members. The variable
  $\tilde w$ of Eqs. (23)–(29) is not defined.
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
  Sciacovelli et al. prove no stability or accuracy theorem; their
  evidence is numerical.

# Citations

- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — arXiv v1: §1; §3 (Eqs. (20)–(35), Fig. 1); §4.1; §5.2 (Fig. 11).
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — arXiv v1: §3 (Eqs. (4)–(8)); Rem. 2; §6 (Eqs. (16)–(18), Rem. 6); §7.3–§7.4; §8.
- [Pazner (2021)](/sources/pazner-2021.md) — arXiv v1: §3.1 (Eqs. (32)–(35)); §3.4 (Fig. 1); §4.4.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: §1, §1.2 (Eq. (1.2)); §2.2 (Eqs. (2.9)–(2.12)); Rems. 2.2–2.3.
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — Ex. 4.2; §5 (first-moment limiter read as artificial viscosity).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — arXiv v1: §1; §6.4.
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — author manuscript: §I.
- [Fu (2023)](/sources/fu-2023.md) — §3.4 (adaptive artificial viscosity among hybrid TENO uses, named only).
