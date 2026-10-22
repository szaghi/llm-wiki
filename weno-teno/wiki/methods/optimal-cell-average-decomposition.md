---
type: Method
title: "Optimal cell-average decomposition"
description: "The cell-average decomposition writes a cell average as a positive quadrature that includes the interface points and sets the bound-preserving CFL number of Zhang–Shu schemes; the page states the optimization problem, the proofs that the Gauss–Lobatto decomposition is optimal in 1D and for Q^N, and the optimal and quasi-optimal decompositions for P^N."
status: established
aliases: [cell average decomposition, CAD, OCAD, optimal CAD, quasi-optimal CAD, convex decomposition of the cell average]
tags: [bound-preserving, positivity, dg, finite-volume]
timestamp: 2026-10-22T12:00:00Z
---

# Optimal cell-average decomposition

In the Zhang–Shu route to [bound preservation](/properties/bound-preservation.md),
the cell average $\bar u_i$ of a degree-$N$ polynomial (a DG solution or a
finite-volume reconstruction) is written as a convex combination of point
values that includes the interface traces. This **cell-average
decomposition** (CAD) turns the high-order cell-average update into a
convex combination of first-order bound-preserving updates, and its
smallest boundary weight $\varpi$ sets the bound-preserving CFL number.
[Cui, Ding & Wu (2024)](/sources/cui-2024.md) pose and solve the problem of
the decomposition that maximizes this CFL number, the **optimal CAD**
(OCAD).

## Feasible decompositions and the BP CFL condition

**1D** ([Cui et al. (2024)](/sources/cui-2024.md), Def. 1.1). On
$I_i$, a decomposition
$$\bar p_i=\varpi^-\,p(x_{i-1/2})+\varpi^+\,p(x_{i+1/2})+\sum_{s=1}^{S}\mathsf w_s\,p(x^{(s)})$$
is **feasible** for $\mathbb P^N$ if (i) it is exact for every
$p\in\mathbb P^N$, (ii) all weights are positive (they sum to one), and
(iii) the internal nodes $x^{(s)}$ lie in $I_i$. With a first-order scheme
that is BP under $a\Delta t/\Delta x\le c_0$ ($c_0$ page-local: 1 for
Lax–Friedrichs, 1/2 for HLL and HLLC, §7), the high-order update is BP
under $a\Delta t/\Delta x\le c_0\min\{\varpi^-,\varpi^+\}$ (Eq. (1.10)),
provided the point values are in $G$. The 1D OCAD problem is to maximize
$\min\{\varpi^-,\varpi^+\}$: equivalently, to find the positive quadrature
of degree $\ge N$ containing both endpoints with the largest smaller
endpoint weight (Problem 1.2).

**2D Cartesian cells** (Def. 1.3, Eq. (1.11)). Boundary weights
$\varpi_1^\pm$, $\varpi_2^\pm$ multiply the edge averages (discretized by
$Q$-point Gauss quadrature, Eq. (1.12)), internal weights $\mathsf w_s$
multiply interior point values, for $\mathbb V^N=\mathbb P^N$ (total
degree) or $\mathbb Q^N$ (tensor degree). The BP condition is
$\Delta t\le c_0\min\{\varpi_1^\pm\Delta x/a^{(1)},\ \varpi_2^\pm\Delta y/a^{(2)}\}$
(Eq. (1.13)), and the 2D OCAD maximizes the right-hand side (Problem 1.4).

**The classic decomposition** (Zhang and Shu, as recalled in §1, Eqs.
(1.6), (1.14)). In 1D, the $L$-point Gauss–Lobatto rule with
$L=\lceil(N+3)/2\rceil$, whose endpoint weights are
$\mathsf w^{\mathrm{GL}}_0=\mathsf w^{\mathrm{GL}}_{L-1}=1/(L(L-1))$. In 2D,
the tensor product of Gauss and Gauss–Lobatto rules blended with weights
proportional to $a^{(1)}/\Delta x$ and $a^{(2)}/\Delta y$, which gives
$$\Delta t\Big(\frac{a^{(1)}}{\Delta x}+\frac{a^{(2)}}{\Delta y}\Big)\le c_0\,\mathsf w^{\mathrm{GL}}_0 .$$
[Wu & Shu (2023)](/sources/wu-2023-b.md) use the same Gauss–Lobatto bound
for their bound-preserving MHD schemes (Thm 6.2, $\lambda\le\widehat\omega_1$
in their notation).

## Results

**1D optimality** ([Cui et al. (2024)](/sources/cui-2024.md), Thm 2.3).
For every $N\ge1$ the Gauss–Lobatto decomposition is the 1D OCAD, with
unique optimal boundary weights $\varpi_\star^\pm=1/(L(L-1))$. The proof
tests the constraint "$\bar p-\varpi^-p(x_{i-1/2})-\varpi^+p(x_{i+1/2})\ge0$ for
all non-negative $p\in\mathbb P^N$" with
$p^\star=\prod_{\ell=1}^{L-2}(x-x^{\mathrm{GL}}_\ell)^2$, which has degree
$2(L-2)\le N$ and vanishes at the internal nodes. This confirms a claim of
Zhang and Shu, who had checked it only for $N=2,3$ (as recalled after
Thm 2.3).

**2D general theory on Cartesian cells.**
- An OCAD exists for any $\mathbb V^N$ (Thm 3.4): Carathéodory's theorem
  bounds the internal nodes by $\dim\mathbb V^N+1$ (Lemma 3.1), and the
  set of feasible boundary weights is compact (Lemma 3.3) and convex
  (Lemma 3.5).
- A symmetric OCAD with $\varpi_1\Delta x/a^{(1)}=\varpi_2\Delta y/a^{(2)}$
  always exists on $[-1,1]^2$ (Thm 3.12). Let
  $\varkappa=\dfrac{a^{(1)}/\Delta x-a^{(2)}/\Delta y}{a^{(1)}/\Delta x+a^{(2)}/\Delta y}\in[-1,1]$
  denote the anisotropy parameter (page-local; the source writes
  $\theta$). Then $\varpi_1=\tfrac12\varpi(1+\varkappa)$,
  $\varpi_2=\tfrac12\varpi(1-\varkappa)$, the problem reduces to one
  scalar $\varpi_\star(\varkappa,\mathbb V^N)$, and the optimal condition is
  $$\Delta t\Big(\frac{a^{(1)}}{\Delta x}+\frac{a^{(2)}}{\Delta y}\Big)\le c_0\,\varpi_\star(\varkappa,\mathbb V^N)\qquad\text{(Eq. (3.38))}.$$
- $\varpi_\star$ is non-increasing in $N$, equal for $\mathbb V^{2n}$ and
  $\mathbb V^{2n+1}$, and even in $\varkappa$ (Lemmas 3.14–3.18).
- Upper bound and optimality criteria. With
  $\phi(p;\varkappa)=\bar p\big/\big[(1+\varkappa)\langle p\rangle^x+(1-\varkappa)\langle p\rangle^y\big]$
  ($\langle p\rangle^x$, $\langle p\rangle^y$ the averaged edge means,
  page-local), $\varpi_\star\le\inf_{p\ge0}\phi(p;\varkappa)$ (Lemma 3.20).
  A feasible symmetric CAD is optimal if some nonzero
  $q_\star\in\mathbb V^{\lfloor N/2\rfloor}$ vanishes at all its internal
  nodes (criterion #3, Thm 3.26); then $q_\star^2$ is a critical
  non-negative polynomial.
- The sum-of-squares bound has the closed form
  $\inf_q\phi(q^2;\varkappa)=1/\lVert M^{-1/2}M_\varkappa M^{-1/2}\rVert_2$,
  the smallest root of $\det(M-\phi M_\varkappa)$, with $M$ the cell Gram
  matrix and $M_\varkappa$ the weighted edge Gram matrix of a monomial
  basis of $\mathbb V^{\lfloor N/2\rfloor}$ (Thm 3.29; $M$ here is not the
  DG mass matrix of the registry).

**$\mathbb Q^N$.** The classic tensor decomposition, with
$L=\lceil(N+3)/2\rceil$ and $Q\ge(N+1)/2$, is an OCAD for every $N$ and every
$\varkappa$, with $\varpi_\star=1/(L(L-1))$ (Thm 4.1).

**$\mathbb P^N$.** The classic decomposition is optimal only at
$\varkappa=\pm1$ (Thms 5.1–5.2); for $\varkappa\in(-1,1)$ its boundary
weights lie in the interior of the feasible set (Rem. 5.3). Analytic OCADs
are given for $N\le7$, with far fewer internal nodes than the classic one
in symmetric reduced form: 1 node for $\mathbb P^{2,3}$, 2 for
$\mathbb P^{4,5}$, 4 for $\mathbb P^{6,7}$ (Thms 5.7–5.17, Table 2). At
$\varkappa=0$:

| $N$ | classic $1/(L(L-1))$ | optimal $\varpi_\star(0,\mathbb P^N)$ | linear-stability CFL $1/(2N+1)$ |
|---|---|---|---|
| 1 | 1/2 | 1/2 | 1/3 |
| 2, 3 | 1/6 | 1/4 | 1/5, 1/7 |
| 4, 5 | 1/12 | $2-\sqrt{14}/2\approx0.1292$ | 1/9, 1/11 |
| 6, 7 | 1/20 | $1-\sqrt{30}/6\approx0.08713$ | 1/13, 1/15 |
| 8, 9 | 1/30 | 0.05767 (numerical) | 1/17, 1/19 |

(Table 1, Thms 5.7, 5.9, 5.10, App. C; the classic and optimal entries were
recomputed from the printed formulas, *compiler check, not in the
sources*.) For $\mathbb P^{2,3}$ and any $\varkappa$ the closed form is
$\varpi_\star=1/(4+2\lvert\varkappa\rvert)$ with a single internal node
(Thm 5.13). For $N\ge8$ the OCAD is computed by solving a nonlinear moment
system (5.35) with MATLAB `fsolve`, continued in $\varkappa$ from the
analytic $\varkappa=-1$ solution (Alg. 5.20); existence is not proved there,
and App. C tabulates $\varkappa=0$ values up to $N=15$.

**Quasi-optimal decomposition** (Thm 6.1). A convex combination of the
$\varkappa=\pm1$ and $\varkappa=0$ OCADs is feasible, has weight
$$\varpi^Q_\star=\frac{\varpi_{\star,0}\,\mathsf w^{\mathrm{GL}}_0}{\varpi_{\star,0}\lvert\varkappa\rvert+\mathsf w^{\mathrm{GL}}_0(1-\lvert\varkappa\rvert)},\qquad\varpi_{\star,0}=\varpi_\star(0,\mathbb P^N),$$
coincides with the OCAD for $\mathbb P^{2,3}$, and stays above 95% of the
optimum for $\mathbb P^4$–$\mathbb P^9$, while the classic decomposition can
fall to 57–65% of it (§6, Fig. 11).

## Use in bound-preserving DG

[Cui et al. (2024)](/sources/cui-2024.md) prove that $\mathbb P^N$-DG with
any feasible symmetric CAD keeps $\bar u^{n+1}_{ij}\in G$ under
$\Delta t(a^{(1)}/\Delta x+a^{(2)}/\Delta y)\le\varpi c_0$, provided the edge
Gauss-point values and the internal-node average
$\Pi_{ij}=\frac{1}{1-2\varpi}\sum_s\mathsf w_s\,p_{ij}(x^{(s)},y^{(s)})$ are in
$G$ (Thm 7.1). Since $\Pi_{ij}$ can be computed from the cell average and
the interface values alone (Eq. (7.16)), a "simplified" limiter needs only
the boundary weight, not the internal nodes (Rem. 7.4); the
[Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md) page
gives both variants. With $c_0=1$ the optimal BP CFL number is weaker than
the linear-stability CFL $1/(2N+1)$ for every $N\le9$ except $N=8$, so the
stability step alone then guarantees bound preservation; with $c_0=1/2$
(HLL/HLLC) the BP bound dominates but is much milder than the classic one
(Rem. 7.7, Fig. 12).

**Numerical evidence** (§8). With global Lax–Friedrichs fluxes, SSP-RK3 and
SSP multistep methods, the optimal and quasi-optimal decompositions keep
order $N+1$ for $N=2,4,6,8$ on 2D linear advection with errors very close to
the classic ones, and cut CPU time by 20–50%: e.g. $\mathbb P^8$ on $14^2$
cells, 44.91 s against 92.61 s; $\mathbb P^4$ shock–vortex interaction at
low density, 1299.55 min (optimal), 1327.45 min (quasi-optimal), 1772.26 min
(classic); $\mathbb P^4$ relativistic jet, 297.26, 334.59 and 414.19 h
(Tables 3–10). The code breaks down without the BP limiter on the
[shock–vortex interaction](/benchmarks/shock-vortex-interaction.md) and the
relativistic jet (§8.3, §8.5).

## Classic decompositions in other sources

Two further sources of the bundle prove bound preservation with the classic
Gauss–Lobatto decomposition, and their CFL numbers show what the optimal
one would change.

- **Finite-volume Hermite WENO for Navier–Stokes**
  ([Fan, Zhang & Qiu (2021)](/sources/fan-2021.md), §3.1–§3.2, Eqs.
  (3.9)–(3.12), (3.26)–(3.30)). For a reconstruction of degree $k$ they use
  the $L$-point Gauss–Lobatto rule with $L=\lceil(k+3)/2\rceil$ (the smallest $L$ with $2L-3\ge k$,
  *compiler check, not in the sources*), and endpoint weight
  $\varpi=1/(L(L-1))$ ($L=4$, $\varpi=1/12$, for their quintic 1D
  reconstruction, which is also their time-step constant). The internal
  part of the decomposition is replaced by the residual, whose components
  are, by the mean-value theorem, values of the reconstruction's components
  at (not necessarily equal) points inside the cell,
  $(\bar u_i-\varpi u^+_{i-1/2}-\varpi u^-_{i+1/2})/(1-2\varpi)$ (Eq. (3.10)),
  which is the 1D form of the internal-node average $\Pi_{ij}$ above. In 2D
  the tensor Gauss / Gauss–Lobatto decomposition is weighted by
  $\Delta t/\Delta x$ and $\Delta t/\Delta y$ (Eq. (3.26)), and the CFL
  condition is $\Delta t(1/\Delta x+1/\Delta y)\max a^{\mathrm{NS}}<\varpi$
  with the viscous Lax–Friedrichs coefficient $a^{\mathrm{NS}}$ of the
  [bound preservation](/properties/bound-preservation.md) page (Eq. (3.30)),
  the classic condition with one wave speed in both directions *(compiler
  remark, not in the sources)*.
- **DGSEM on unstructured quadrilaterals** ([Renac (2021)](/sources/renac-2021.md),
  Thm 6.1, Rem. 6.1, App. A). The decomposition is the DGSEM's own
  quadrature on its $N+1$ Gauss–Lobatto collocation nodes, with endpoint
  weight $\mathsf w_0=2/(N(N+1))$ on $[-1,1]$, i.e. $1/(N(N+1))$ on the unit
  interval, combined with sub-triangle decompositions of the element and
  the minimum of the Jacobian over the element boundary; the CFL bound is
  $1/(2N(N+1))$ for a first-order scheme with $c_0=1/2$ (Eq. (66)). Renac
  calls it not optimal (Rem. 6.1). For $N\ge2$ the endpoint weight of the
  $N+1$ collocation nodes is smaller than that of the minimal rule with
  $L=\lceil(N+3)/2\rceil$ points (for $N=3$: $1/12$ against $1/6$), so a
  decomposition that is not tied to the collocation nodes would already
  double the bound there *(compiler check, not in the sources)*.

## Qualifications

- Optimality is within decompositions of the Zhang–Shu form, whose boundary
  nodes are the edge Gauss points; a different edge quadrature or flux
  treatment changes the problem.
- For $\mathbb P^{4..7}$ part of the feasibility conditions is checked
  graphically (Figs. 7–8); for $N\ge8$ the result rests on a numerical
  solve.
- The linear-stability CFL $1/(2N+1)$ is cited by the source as an
  empirical formula for a $(N+1)$-stage RK DG method, while the tests use
  SSP-RK3 and SSP multistep methods: the comparison of Rem. 7.7 is
  indicative.
- Printed slips of arXiv v1 that touch this page: Rem. 5.3 / Eq. (5.6)
  prints the coefficients $\frac{1+\theta}{2}$ and $\frac{1-\theta}{2}$
  ($\theta$ the source's $\varkappa$) swapped relative to the
  $\varkappa=\mp1$ decompositions they multiply, while the construction of
  Thm 6.1 uses them consistently *(compiler check, not in the sources: the
  $\langle p\rangle^y$ coefficients of Eqs. (4.1), (5.1) and (5.4) compared)*;
  the proof of Thm 7.1 prints $a_2/\Delta x$ for $a_2/\Delta y$, against the
  source's own definition (3.34) of the anisotropy.

# Citations

- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §1 (Defs 1.1, 1.3; Problems 1.2, 1.4; Eqs. (1.6), (1.10), (1.13)–(1.15)); Thm 2.3; §3 (Lemmas 3.1–3.20, Thms 3.4, 3.12, 3.26, 3.29); Thm 4.1; §5 (Thms 5.1–5.17, Alg. 5.20); Thm 6.1 and Fig. 11; §7 (Thm 7.1, Rems. 7.4, 7.7); §8 (Tables 1–10); App. C.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: Thm 6.2 (Gauss–Lobatto BP CFL condition).
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §3.1–§3.2 (Eqs. (3.9)–(3.12), (3.26)–(3.30)).
- [Renac (2021)](/sources/renac-2021.md) — arXiv v3: Thm 6.1 (Eq. (66)), Rem. 6.1, App. A.
