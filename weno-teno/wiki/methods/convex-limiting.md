---
type: Method
title: "Convex limiting and invariant-domain-preserving schemes"
description: "Convex limiting blends a high-order update with a bound-preserving low-order update, adding as much antidiffusive flux as target bounds allow; the page gives the FCT form, the Zalesak limiter, Guermond–Popov bar states and invariant-domain bounds, element- versus subcell-wise blending, and the equivalence of subcell Rusanov finite volumes with sparse IDP DG."
status: established
aliases: [flux-corrected transport, FCT, algebraic flux correction, AFC, invariant-domain-preserving limiting, IDP limiting, a posteriori blending, Zalesak limiter]
tags: [limiting, bound-preserving, positivity, dg, entropy-stable]
timestamp: 2026-10-21T00:00:00Z
---

# Convex limiting and invariant-domain-preserving schemes

Convex limiting starts from a low-order update that is
[bound-preserving](/properties/bound-preservation.md) by construction and adds
to it as much of the difference "high-order minus low-order" as a set of
target bounds allows. The result is a convex combination of the two updates
(per element, per node or per interface), so it stays conservative and
inherits whatever convex constraints the bounds encode. The family descends
from flux-corrected transport (Boris–Book, Zalesak, Löhner, Kuzmin) and the
invariant-domain-preserving (IDP) methods of Guermond and Popov, as recalled
by [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
(§2.4) and [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) (§1, algebraic
flux correction).

## FCT form

Rueda-Ramírez et al. write the forward-Euler step (to which SSP Runge–Kutta
stages reduce, being convex combinations of Euler steps) as
$$u^{n+1}_{ij}=u^{\mathrm{FV},n+1}_{ij}+\sum_{k\in\mathcal N(ij)\setminus\{ij\}}\big(1-\alpha_{(ij,k)}\big)\,\Delta f^{\mathrm{ad}}_{(ij,k)},\qquad
\Delta f^{\mathrm{ad}}_{(i,i+1)j}=-\frac{\Delta t}{J_{ij}\mathsf w_i}\Big(\hat f^{\mathrm{DG}}_{(i,i+1)j}-\hat f^{\mathrm{FV}}_{(i,i+1)j}\Big)$$
(Eqs. (26)–(27)), with $\mathcal N(ij)$ the five-point low-order stencil of
node $ij$ (page-local), $\Delta f^{\mathrm{ad}}$ the mass-weighted
antidiffusive flux (page-local; the source writes $\bar f$), $J_{ij}$ the
element Jacobian and $\mathsf w_i$ the LGL weight. The blending coefficient
$\alpha$ is the weight of the **low-order** scheme ($\alpha=0$ pure
high-order, $\alpha=1$ pure low-order), the opposite of the FCT convention in
which the limiter value 1 means full antidiffusion; in this form $(1-\alpha)$
multiplies the antidiffusive flux.

## Target bounds

Rueda-Ramírez et al. (§2.4, §5) use three kinds:

1. **Local min/max bounds** (Eqs. (23)–(24)):
   $\min_{k\in\mathcal N(ij)}\rho(u^\star_k)\le\rho_{ij}\le\max_{k\in\mathcal N(ij)}\rho(u^\star_k)$,
   with $u^\star=u^n$ or $u^\star=u^{\mathrm{FV},n+1}$ when the low-order
   scheme is monotone (page-local $u^\star$).
2. **Bar states** (Guermond–Popov, Eq. (25)). Between nodes $a$ and $b$,
   $$\breve u_{ab}=\tfrac12(u_a+u_b)+\frac{1}{2a_{ab}}\big(f_n(u_a)-f_n(u_b)\big),$$
   with $f_n$ the flux normal to the subcell interface and $a_{ab}$ an upper
   bound of the maximum wave speed of the 1D Riemann problem between the
   two states (page-local $\breve u$, $f_n$; the source writes $\bar u$ and
   leaves the normal projection implicit). Bar states preserve every convex
   invariant of the system and supply the targets $u^\star_k=\breve u_{(ij,k)}$.
   For Euler, the density bounds
   $\min_k\breve\rho_{(ij,k)}\le\rho_{ij}\le\max_k\breve\rho_{(ij,k)}$
   (Eq. (47)) together with a local minimum principle on the modified
   specific entropy $e\rho^{1-\gamma}$ (Eq. (48)) guarantee positivity of
   density and pressure and a discrete entropy inequality (as recalled
   from Guermond et al.). The modified entropy is preferred to
   $s=\ln(p\rho^{-\gamma})$ because it is cheaper and better suited to
   Newton's method.
3. **Bounds relative to the low-order solution** (after Rueda-Ramírez &
   Gassner, Eq. (43)): $\rho_{ij}\ge\beta_{\mathrm{FV}}\rho^{\mathrm{FV}}_{ij}$,
   $p_{ij}\ge\beta_{\mathrm{FV}}p^{\mathrm{FV}}_{ij}$ with
   $\beta_{\mathrm{FV}}=0.1$ (page-local).

## Computing the blending coefficient

- **Linear bounds, subcell-wise: Zalesak-type limiter** (Eq. (28)). With
  $P^\pm$ the sums of the positive and negative antidiffusive contributions
  to the bounded quantity,
  $$\alpha^{+}_{ij}=1-\min\Big(1,\frac{\rho^{\max}_{ij}-\rho(u^{\mathrm{FV},n+1}_{ij})}{P^+}\Big),\qquad
  \alpha^{-}_{ij}=1-\min\Big(1,\frac{\rho^{\min}_{ij}-\rho(u^{\mathrm{FV},n+1}_{ij})}{P^-}\Big),$$
  $\tilde\alpha_{ij}=\max(\alpha^-_{ij},\alpha^+_{ij})$, and the interface
  takes the larger of its two nodal values,
  $\alpha_{(i,m)j}=\max(\tilde\alpha_{ij},\tilde\alpha_{mj})$.
- **Nonlinear convex bounds, subcell-wise** (Eq. (29), after Guermond et al.
  and Pazner). Solve $2d$ scalar nonlinear problems per node ($d$ the
  dimension) so that every provisional state
  $u^{\mathrm{FV},n+1}_{ij}+\Gamma(1-\tilde\alpha_{ij})\Delta f^{\mathrm{ad}}_{(ij,k)}$,
  $\Gamma=2d$, satisfies the bound; this guarantees the bound for the full
  update. Newton–bisection or Newton–secant solvers are used.
- **Element-wise.** Each element takes the maximum of its nodal
  coefficients. Linear constraints are then solved in closed form from the
  FCT form; nonlinear convex constraints need a nonlinear solve.

Subcell-wise coefficients are stricter per interface, because each must
guarantee the bound independently of the others, yet on an under-resolved
Kelvin–Helmholtz instability they add about three orders of magnitude less
low-order method than element-wise blending (§5.2.1, Fig. 4; see
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).

## Sparse IDP DG is subcell Rusanov finite volumes

[Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) prove that the
subcell finite-volume scheme of Hennemann et al. on LGL subcells, with
first-order reconstruction and the Rusanov (local
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md)) flux, **is** the
low-order sparse IDP scheme of Pazner,
$$m_i\,\dot u_i=\sum_{j\in\mathcal N(i)}\hat c_{ij}\cdot f(u_j)+\sum_{j\in\mathcal N(i)}\hat d_{ij}(u_j-u_i),\qquad\hat d_{ij}=\lVert\hat c_{ij}\rVert\,a_{ij},$$
a graph-viscosity form (Prop. 1, Eqs. (30)–(33); $m_i$, $\hat c_{ij}$,
$\hat d_{ij}$ page-local). The factor $\tfrac12$ in $\hat c$ is Pazner's
sparsified derivative matrix (Eq. (34)), and the subcell metrics of
Hennemann et al. solve Pazner's conservation condition
$\sum_j\hat c_{ij}=0$ exactly and analytically, so the SVD-based
minimisation of Pazner's construction is not needed (Prop. 2, Eqs.
(35)–(36)). The equivalence is why the bar-state bounds can always be met
for that low-order scheme: on the Mach 4 bow shock they hold to machine
precision (§5.2.2).

## Related flux limiters

Parametrized positivity- and maximum-principle-preserving flux limiters
(Xu; Hu, Adams & Shu) belong to the same idea — limiting a high-order flux
toward a first-order bound-preserving one — and are recalled as background
by [Wu & Shu (2023)](/sources/wu-2023-b.md) (§1), together with the
Guermond–Popov invariant-domain framework. In the finite-difference papers
of the corpus the Hu–Adams–Shu limiter is the source of positivity for
near-vacuum and Mach 2000 jet computations: TENO-AA
([Fu (2021)](/sources/fu-2021.md), §5.7) and TENO-THINC
([Takagi et al. (2022)](/sources/takagi-2022.md), §4.9); neither paper
describes the limiter.

## Qualifications

- **Bounds that a low-order scheme cannot meet.** The bar-state bounds are
  specific to the Rusanov / graph-Laplacian dissipation. When HLLE or a
  second-order subcell reconstruction replaces it, the bounds are no longer
  guaranteed attainable; Rueda-Ramírez et al. keep them "in the absence of
  better bounds" and the blending returns the solution closest to them
  (§4 item (3), §5.2.3). Those variants are not provably IDP.
- **Entropy stability.** A provable entropy inequality for the blended
  semi-discretization exists for element-wise blending of entropy-stable DG
  with entropy-stable finite volumes; for subcell-wise blending the proof
  is "still missing" (§4 item (2)); see
  [entropy stability](/properties/entropy-stability.md).
- **Order barrier of local bounds.** [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md)
  state that local discrete maximum principles impose a second-order
  accuracy barrier and that global-DMP limiters "may fail to prevent
  nonphysical solution behavior" (§1); they propose AFC on top of their
  [dissipation-based WENO stabilization](/methods/weno-stabilized-continuous-galerkin.md)
  when strict bounds or entropy inequalities are required (§7.4). No
  source of the corpus measures the accuracy cost of the bar-state bounds.

# Citations

- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §2.4 (Eqs. (23)–(29)); §3 (Props. 1–2, Eqs. (30)–(36)); §4 items (2)–(3); §5.2.1 (Eq. (43), Fig. 4); §5.2.2 (Eqs. (47)–(48)); §5.2.3.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — arXiv v1: §1 (AFC, order barrier of local bounds); §7.4.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §1 (flux-correction limiters and invariant-domain methods recalled).
- [Fu (2021)](/sources/fu-2021.md) — arXiv v1: §5.7 (Hu–Adams–Shu limiter used).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.9 (Hu–Adams–Shu limiter used).
