---
type: Method
title: "Zhang–Shu scaling limiter"
description: "The Zhang–Shu limiter scales a high-order polynomial linearly toward its cell average until the point values used by a cell-average decomposition lie in the admissible set; it conserves the cell average and, with a BP first-order flux and a CFL bound, makes the cell-average update bound-preserving."
status: established
aliases: [scaling limiter, bound-preserving limiter, positivity-preserving limiter, maximum-principle-satisfying limiter, BP limiter, simplified BP limiter]
tags: [bound-preserving, positivity, limiting, dg, finite-volume]
timestamp: 2026-10-21T12:00:00Z
---

# Zhang–Shu scaling limiter

The Zhang–Shu limiter is the third ingredient of the cell-average route to
[bound preservation](/properties/bound-preservation.md). Given the
degree-$N$ polynomial $u_h$ of cell $I_i$ (DG solution or finite-volume
reconstruction) with cell average $\bar u_i\in G$, it replaces $u_h$ by
$$\tilde u_h=\theta\,(u_h-\bar u_i)+\bar u_i,\qquad 0\le\theta\le1,$$
with $\theta$ the largest factor for which the point values on a prescribed
point set lie in $G$. The cell average is unchanged, so conservation is
kept, and because $G$ is convex and $\bar u_i\in G$, a $\theta$ that works
always exists (at worst $\theta=0$). Combined with a BP first-order flux and
the CFL condition of a
[cell-average decomposition](/methods/optimal-cell-average-decomposition.md),
the next cell average stays in $G$
([Cui, Ding & Wu (2024)](/sources/cui-2024.md), §1, Eqs. (1.7)–(1.8);
Rem. 7.3; [Wu & Shu (2023)](/sources/wu-2023-b.md), App. B).

## Scalar bounds

For a scalar law with $G=[U_{\min},U_{\max}]$,
[Cui et al. (2024)](/sources/cui-2024.md) recall (Rem. 7.3, Eq. (7.15))
$$\theta=\min\Big\{\Big\lvert\frac{U_{\max}-\bar u_i}{p^{\max}-\bar u_i}\Big\rvert,\ \Big\lvert\frac{U_{\min}-\bar u_i}{p^{\min}-\bar u_i}\Big\rvert,\ 1\Big\},$$
where $p^{\max}$, $p^{\min}$ are the maximum and minimum of $u_h$ over the
point set $\Theta_i$ = edge Gauss points $\cup$ internal nodes of the
decomposition (page-local $\Theta_i$). The source prints $\delta$ for the
factor; it is the registry's $\theta$.

## Systems: successive scalings

For gas dynamics the constraints are enforced one after another, each
scaling acting on the result of the previous one, with the density first:

- **Euler, positivity of $\rho$ and $\rho e$** ([Cui et al. (2024)](/sources/cui-2024.md),
  Rem. 8.1). Density: $\hat\rho=\theta_1(\rho_h-\bar\rho_i)+\bar\rho_i$,
  $\theta_1=\min\{\lvert(\bar\rho_i-\varepsilon_1)/(\bar\rho_i-\rho_{\min,i})\rvert,1\}$,
  $\varepsilon_1=\min\{10^{-13},\bar\rho_i\}$; then a second factor
  $\theta_2$ built in the same way from $\rho e$ scales the whole state
  vector. Here $\varepsilon_1$, $\varepsilon_2$ are round-off floors
  (page-local), not WENO regularizations.
- **Multicomponent MHD** ([Wu & Shu (2023)](/sources/wu-2023-b.md), App. B):
  three successive scalings — density, mass fractions (from negative
  partial densities), and the concave function
  $g(u)=E-\tfrac12\big(\lvert\rho v\rvert^2/\rho+\lvert B\rvert^2\big)$,
  used in place of the pressure, which is not concave in $u$ when $\gamma$
  depends on the mass fractions (Eq. (6.3)).

Concavity is what lets a factor computed from point values alone work:
for concave $g$ and $\theta\in[0,1]$,
$g\big(\theta(u-\bar u_i)+\bar u_i\big)\ge(1-\theta)\,g(\bar u_i)+\theta\,g(u)$,
so the factor $\theta=\big(g(\bar u_i)-\varepsilon\big)/\big(g(\bar u_i)-\min g\big)$,
the form Wu & Shu print for their third scaling (App. B), keeps
$g\ge\varepsilon$ at every point of the set *(compiler check, not in the
sources: the inequality is the definition of concavity)*. The
[geometric quasilinearization](/methods/geometric-quasilinearization.md)
representation is the sources' tool for constraints that are not concave.

## Point sets and the simplified limiter

The point set is that of the decomposition: Gauss–Lobatto points in 1D and
the tensor Gauss / Gauss–Lobatto points of the classic 2D decomposition
([Wu & Shu (2023)](/sources/wu-2023-b.md), Thm 6.2, condition (6.12)), or
the edge Gauss points plus the internal nodes of an optimal decomposition
([Cui et al. (2024)](/sources/cui-2024.md), Rem. 7.3), which has far fewer
internal nodes and therefore a cheaper limiter. In the **simplified BP
limiter** recalled by Cui et al. (Rem. 7.4, Eqs. (7.16)–(7.18)), the
internal nodes are replaced by the single state
$$\Pi_{ij}=\frac{1}{1-2\varpi}\Big(\bar u_{ij}-\varpi\Big[\tfrac{1+\varkappa}{2}\sum_q\mathsf w^{\mathrm G}_q\big(u^+_{i-1/2,q}+u^-_{i+1/2,q}\big)+\tfrac{1-\varkappa}{2}\sum_q\mathsf w^{\mathrm G}_q\big(u^+_{q,j-1/2}+u^-_{q,j+1/2}\big)\Big]\Big),$$
computed from the cell average and the edge Gauss values alone
($\mathsf w^{\mathrm G}_q$ the Gauss weights, $\varkappa$ the anisotropy
parameter of the decomposition page, both page-local; $u^\pm$ the traces at
the edge Gauss points). The limiter then enforces $G$ at the edge points
and at $\Pi_{ij}$.

## Time stepping and accuracy

The limiter is applied after every stage of an
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) or SSP multistep method,
which preserves the property because each stage is a convex combination of
forward-Euler steps ([Cui et al. (2024)](/sources/cui-2024.md), Rem. 7.9;
[Wu & Shu (2023)](/sources/wu-2023-b.md), §6.2). That the limiter keeps the
design order is cited, not shown, by Wu & Shu (App. B); Cui et al. show
order $N+1$ numerically for $\mathbb P^2$, $\mathbb P^4$, $\mathbb P^6$ and
$\mathbb P^8$ DG with the limiter on 2D linear advection, with errors very
close to those of the classic decomposition (Ex. 1, Tables 3–6).
In both sources a separate WENO limiter acts first in troubled cells
flagged by a [troubled-cell indicator](/definitions/troubled-cell-indicator.md)
(KXRCF in Wu & Shu, §7; the Qiu–Shu WENO limiter in Cui et al., Ex. 3–5);
the scaling limiter controls bounds, not oscillations.

## Qualifications

- **Incompatible with prescribed interface values.**
  [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) note that the
  scaling limiter cannot be used in [Active Flux](/methods/active-flux.md),
  whose reconstruction must interpolate given interface point values; they
  use power-law limiters that keep continuity instead (discussion after
  Thm 2.2).
- **Missing caps in one printing.** The arXiv v1 of Wu & Shu (2023) prints
  the density factor of App. B as $(\bar\rho-\varepsilon_1)/(\bar\rho-\min\rho)$
  without $\min\{1,\cdot\}$ (and the mass-fraction factor without a cap),
  so as printed it can exceed one; the text says the limiter acts only "if
  this happens", i.e. on violation. Cui et al. print the cap.
- **Scope.** The guarantee is on cell averages and on the chosen point set;
  between points the polynomial may leave $G$.

# Citations

- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §1 (Eqs. (1.7)–(1.8)); Rems. 7.3, 7.4, 7.9 (Eqs. (7.15)–(7.18)); Rem. 8.1; Ex. 1 (Tables 3–6), Ex. 3–5.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: Thm 6.2 (Eq. (6.12)); §6.2; App. B; §7.
- [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) — author preprint, discussion after Thm 2.2 (scaling limiter incompatible with prescribed interface values).
