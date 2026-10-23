---
type: Method
title: "Optimal cell-average decomposition"
description: "The cell-average decomposition writes a cell average as a positive quadrature that includes the interface points and sets the bound-preserving CFL number of Zhang–Shu schemes; the page states the optimization problem, the proofs that the Gauss–Lobatto decomposition is optimal in 1D and for Q^N, and the optimal and quasi-optimal decompositions for P^N."
status: established
aliases: [cell average decomposition, CAD, OCAD, optimal CAD, quasi-optimal CAD, convex decomposition of the cell average]
tags: [bound-preserving, positivity, dg, finite-volume]
timestamp: 2026-10-23T23:55:00Z
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
(1.6), (1.14)). In 1D, the $N_{\mathrm{GL}}$-point Gauss–Lobatto rule with
$N_{\mathrm{GL}}=\lceil(N+3)/2\rceil$, whose endpoint weights are
$\mathsf w^{\mathrm{GL}}_0=\mathsf w^{\mathrm{GL}}_{N_{\mathrm{GL}}-1}=1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$. In 2D,
the tensor product of Gauss and Gauss–Lobatto rules blended with weights
proportional to $a^{(1)}/\Delta x$ and $a^{(2)}/\Delta y$, which gives
$$\Delta t\Big(\frac{a^{(1)}}{\Delta x}+\frac{a^{(2)}}{\Delta y}\Big)\le c_0\,\mathsf w^{\mathrm{GL}}_0 .$$
[Wu & Shu (2023)](/sources/wu-2023-b.md) use the same Gauss–Lobatto bound
for their bound-preserving MHD schemes (Thm 6.2, $\lambda\le\widehat\omega_1$
in their notation).

## Results

**1D optimality** ([Cui et al. (2024)](/sources/cui-2024.md), Thm 2.3).
For every $N\ge1$ the Gauss–Lobatto decomposition is the 1D OCAD, with
unique optimal boundary weights $\varpi_\star^\pm=1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$. The proof
tests the constraint "$\bar p-\varpi^-p(x_{i-1/2})-\varpi^+p(x_{i+1/2})\ge0$ for
all non-negative $p\in\mathbb P^N$" with
$p^\star=\prod_{\ell=1}^{N_{\mathrm{GL}}-2}(x-x^{\mathrm{GL}}_\ell)^2$, which has degree
$2(N_{\mathrm{GL}}-2)\le N$ and vanishes at the internal nodes. This confirms a claim of
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
$N_{\mathrm{GL}}=\lceil(N+3)/2\rceil$ and $Q\ge(N+1)/2$, is an OCAD for every $N$ and every
$\varkappa$, with $\varpi_\star=1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$ (Thm 4.1).

**$\mathbb P^N$.** The classic decomposition is optimal only at
$\varkappa=\pm1$ (Thms 5.1–5.2); for $\varkappa\in(-1,1)$ its boundary
weights lie in the interior of the feasible set (Rem. 5.3). Analytic OCADs
are given for $N\le7$, with far fewer internal nodes than the classic one
in symmetric reduced form: 1 node for $\mathbb P^{2,3}$, 2 for
$\mathbb P^{4,5}$, 4 for $\mathbb P^{6,7}$ (Thms 5.7–5.17, Table 2). At
$\varkappa=0$:

| $N$ | classic $1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$ | optimal $\varpi_\star(0,\mathbb P^N)$ | linear-stability CFL $1/(2N+1)$ |
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

## Optimal decompositions in later sources

Two sources of the bundle use the optimal decomposition of Cui, Ding & Wu
in new schemes and print the closed forms of $\varpi_\star(\varkappa)$
beyond $\mathbb P^{2,3}$.

- **Relativistic MHD, central DG on overlapping meshes**
  ([Ding & Wu (2024)](/sources/ding-2024-b.md), §4.3, §4.6, Eqs.
  (53)–(60), Cors. 4.1–4.2). A central-DG solution of one mesh is
  discontinuous inside the cells of the other, so they split each target
  cell into four quarter cells and apply a general feasible symmetric
  decomposition (Eq. (53)) on each. The cell average becomes the sum of
  an internal part and two boundary parts, one on the interior lines
  $x_i$, $y_j$, with traces from both sides, and one on the outer boundary
  (Eq. (59)); the bound-preserving CFL condition is $\varpi/2$, with
  normal-field-jump factors in the wave speeds
  ([bound preservation](/properties/bound-preservation.md)). With the
  classic decomposition the condition is $1/(2N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$
  (Cor. 4.1); with the optimal one $\varpi_\star(\varkappa,\mathbb P^N)/2$
  (Cor. 4.2), with
  $$\varpi_\star=\Big[\tfrac{14}3+\tfrac23\sqrt{78\varkappa^2+46}\,\cos\Big(\tfrac13\arccos\frac{1476\varkappa^2-244}{(78\varkappa^2+46)^{3/2}}\Big)\Big]^{-1}\quad(N=4,5),$$
  $$\varpi_\star=\Big[\tfrac{20}3+2\lvert\varkappa\rvert+\tfrac23\sqrt{126\varkappa^2+96\lvert\varkappa\rvert+94}\,\cos\Big(\tfrac13\arccos\frac{864\lvert\varkappa\rvert^3+2916\varkappa^2+288\lvert\varkappa\rvert-532}{(126\varkappa^2+96\lvert\varkappa\rvert+94)^{3/2}}\Big)\Big]^{-1}\quad(N=6,7),$$
  and $1/(4+2\lvert\varkappa\rvert)$ for $N=2,3$, $\tfrac12$ for $N=1$
  (their $\delta$ is the registry's $\varkappa$). At $\varkappa=0$ the two
  formulas give $0.129171=2-\sqrt{14}/2$ and $0.087129=1-\sqrt{30}/6$, the
  table values above, and at $\lvert\varkappa\rvert=1$ the $N=4,5$ formula
  gives $1/12$, the classic weight, as Thms 5.1–5.2 require *(compiler
  check, not in the sources)*. For $\mathbb P^2$ the optimal
  decomposition has one internal node at $\varkappa=0$, the two nodes
  $(\pm\sqrt{2\lvert\varkappa\rvert/(3+3\lvert\varkappa\rvert)},0)$ merging,
  against $2Q(N_{\mathrm{GL}}-2)=6$ for the classic one with $Q=N_{\mathrm{GL}}=3$
  (Eqs. (54)–(56)), so the limiter needs fewer points, the reason they use
  it in all 2D tests (§4.6). In practice $\alpha_\ell=1$ and, for
  $\Delta x=\Delta y$, $\varkappa=0$, because the normal-field jumps stay
  small (Remark 9).
- **Sixth-order Hermite WENO** ([Fan & Wu (2024)](/sources/fan-2024.md),
  §2.4, Eq. after (2.53), Thm 11, arXiv v1). For the $\mathbb P^5$
  reconstruction of their oscillation-eliminating Hermite WENO they use
  the $N=4,5$ decomposition (their anisotropy $\theta$ is the registry's
  $\varkappa$), with weights $\varpi_\star$,
  $\mathsf w_1=\frac{5(1-4\varpi_\star+2\lvert\varkappa\rvert\varpi_\star)^2}{9(1-6\varpi_\star+4\lvert\varkappa\rvert\varpi_\star)}$,
  $\mathsf w_2=1-2\varpi_\star-\mathsf w_1$ and explicit internal points, and
  obtain the bound-preserving condition
  $\Delta t\big(a^{(1)}/\Delta x+a^{(2)}/\Delta y\big)\le\varpi_\star$,
  $2-\sqrt{14}/2\approx0.1292$ at $\varkappa=0$ against $1/12$ for the
  classic decomposition (p. 31). In 1D they keep the Gauss–Lobatto rule,
  which is optimal there (§2.4).

## Classic decompositions in other sources

Five further sources of the bundle prove bound preservation with classic
decompositions, and their CFL numbers show what an optimal one would
change.

- **Finite-volume Hermite WENO for Navier–Stokes**
  ([Fan, Zhang & Qiu (2021)](/sources/fan-2021.md), §3.1–§3.2, Eqs.
  (3.9)–(3.12), (3.26)–(3.30)). For a reconstruction of degree $k$ they use
  the $N_{\mathrm{GL}}$-point Gauss–Lobatto rule with $N_{\mathrm{GL}}=\lceil(k+3)/2\rceil$ (the smallest $N_{\mathrm{GL}}$ with $2N_{\mathrm{GL}}-3\ge k$,
  *compiler check, not in the sources*), and endpoint weight
  $\varpi=1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$ ($N_{\mathrm{GL}}=4$, $\varpi=1/12$, for their quintic 1D
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
  check, not in the sources: compare with the classic 2D condition
  above)*.
- **Finite-difference WENO for Navier–Stokes**
  ([Fan, Zhang & Qiu (2022)](/sources/fan-2022.md), §3.2, Theorem 1,
  Eqs. (3.6)–(3.11)). A finite-difference scheme has no polynomial in the
  cell, so they read it, after Shu and Osher, as a formal finite-volume
  scheme for the auxiliary functions of the two split variables, whose
  "cell averages" are the point values of the split variables
  ([positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md)).
  The update of $u_i$ is split into two halves, one per interface; each
  half needs the decomposition of one split variable's cell average with
  only one endpoint, written with a degree-$2r$ interpolating polynomial
  (used in the proof only) and the $N_{\mathrm{GL}}$-point Gauss–Lobatto rule,
  $N_{\mathrm{GL}}=\lceil(2r+3)/2\rceil$, so that $2N_{\mathrm{GL}}-3\ge2r$. Each half is a convex
  combination if $\frac{\Delta t}{\Delta x}a^{\mathrm{NS}}_{i+1/2}\le\frac12\varpi$,
  $\varpi=1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$, which gives the bound
  $\frac{\Delta t}{\Delta x}\max_ia^{\mathrm{NS}}_{i+1/2}\le\frac1{2N_{\mathrm{GL}}(N_{\mathrm{GL}}-1)}$
  (Eq. (3.10); $a^{\mathrm{NS}}$ the viscous Lax–Friedrichs coefficient, the source's $\beta$).
  This is $1/24$ for fifth-order WENO ($r=2$, $N_{\mathrm{GL}}=4$) and $1/40$ for
  seventh order ($r=3$, $N_{\mathrm{GL}}=5$), half the finite-volume bound with the same
  number of Gauss–Lobatto points, because each half-update uses half of
  the point value *(compiler check, not in the sources)*. In 2D the update
  is the average of two doubled 1D updates, so the bound applies to
  $2\Delta t$ in each direction, $\frac{\Delta t}{\Delta x}\max a^{\mathrm{NS},(1)}\le\frac1{4N_{\mathrm{GL}}(N_{\mathrm{GL}}-1)}$
  and the same in $y$ *(compiler check, not in the sources; the paper
  does not write the 2D bound)*. The diffusion-only variant of their §4
  carries $\frac1{4N_{\mathrm{GL}}(N_{\mathrm{GL}}-1)}$ already in 1D (Theorem 2), where they print
  $N_{\mathrm{GL}}=\lceil2r+3\rceil$; the proof "following the same lines" needs
  $\lceil(2r+3)/2\rceil$.
- **DGSEM on unstructured quadrilaterals** ([Renac (2021)](/sources/renac-2021.md),
  Thm 6.1, Rem. 6.1, App. A). The decomposition is the DGSEM's own
  quadrature on its $N+1$ Gauss–Lobatto collocation nodes, with endpoint
  weight $\mathsf w_0=2/(N(N+1))$ on $[-1,1]$, i.e. $1/(N(N+1))$ on the unit
  interval, combined with sub-triangle decompositions of the element and
  the minimum of the Jacobian over the element boundary; the CFL bound is
  $1/(2N(N+1))$ for a first-order scheme with $c_0=1/2$ (Eq. (66)). Renac
  calls it not optimal (Rem. 6.1). For $N\ge2$ the endpoint weight of the
  $N+1$ collocation nodes is smaller than that of the minimal rule with
  $N_{\mathrm{GL}}=\lceil(N+3)/2\rceil$ points (for $N=3$: $1/12$ against $1/6$), so a
  decomposition that is not tied to the collocation nodes would already
  double the bound there *(compiler check, not in the sources)*.

- **Triangles** ([Chen & Wu (2022)](/sources/chen-2022-b.md), Rem. 3.4,
  Eqs. (44), (58)–(59), after Zhang, Xia & Shu). On any triangle a
  positive quadrature exact for $\mathbb P^N$ contains the $Q$ Gauss points
  of each edge, with weight $\frac23\mathsf w^{\mathrm{GL}}_0\,\mathsf w^{\mathrm G}_q$ per
  edge point ($\mathsf w^{\mathrm{GL}}_0=1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$, $N_{\mathrm{GL}}=\lceil(N+3)/2\rceil$,
  $\mathsf w^{\mathrm G}_q$ the edge Gauss weights), and positive interior weights that
  sum to $1-2\mathsf w^{\mathrm{GL}}_0$; it is obtained from the rectangle
  rule by a transformation the paper calls "Dubinar transform" (as
  printed; Rem. 3.4). The remainder
  $\big(\bar u_K-\frac23\mathsf w^{\mathrm{GL}}_0\sum_{j,q}\mathsf w^{\mathrm G}_qu(x^{(jq)})\big)/(1-2\mathsf w^{\mathrm{GL}}_0)$
  is therefore a convex combination of interior values, the triangle form
  of the internal-node average $\Pi_{ij}$ above. The decomposition is used
  only in the proof and in the definition of the limiter; the interior
  points are never evaluated. For their quadratic ($N=2$) reconstruction,
  $\mathsf w^{\mathrm{GL}}_0=1/6$, and the BP condition with the HLL flux is
  $\Delta t\,\hat a\,\lvert e\rvert/\lvert K\rvert\le\frac23\cdot\frac16$ on every
  edge $e$ of triangle $K$ (Thm 3.1, Eq. (57); $\hat a$ the edge spectral
  radius, page-local). The paper applies it to
  [special relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md).
- **LDG for reacting flows** ([Du & Yang (2022)](/sources/du-2022-b.md),
  Thm 4.1, Thms 5.4–5.6, Rem. 5.1). In 1D the $N_{\mathrm{GL}}$-point Gauss–Lobatto
  rule with $N_{\mathrm{GL}}$ the smallest integer with $2N_{\mathrm{GL}}-3\ge N$ and endpoint weight
  $1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$; on polygonal cells a cell quadrature that contains all edge
  Gauss points, with the condition
  $\Delta t\frac{\lvert e_i\rvert}{\lvert K\rvert}\max a^{\mathrm R}\le\min_{\nu,i}a_{\nu,i}/b_\nu$
  ($a_{\nu,i}$ the normalized cell weights of the edge points, $b_\nu$ the
  edge Gauss weights, page-local); on rectangles the tensor Gauss /
  Gauss–Lobatto rule, $\Delta t(1/\Delta x+1/\Delta y)\max a^{\mathrm R}\le1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$,
  recalled from Zhang (2017). The wave speed $a^{\mathrm R}$ there is a viscous
  Lax–Friedrichs penalty (page-local, the symbol of the
  [bound preservation](/properties/bound-preservation.md) page), and their
  exponential time integrator multiplies the bound by
  $\min\alpha_{jl}/\beta_{jl}$ over its Shu–Osher coefficients (page-local $\alpha_{jl}$, $\beta_{jl}$; Thm 4.3,
  Eq. (4.17)), $\approx0.793$ *(compiler check, not in the sources:
  $\alpha_{21}/\beta_{21}=\alpha_{32}/\beta_{32}=0.79298$, $\alpha_{10}/\beta_{10}=1.41404$,
  the others infinite)*.

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

- **A printed exponent.** Fan & Wu print the argument of the arccos as
  $(1476\varkappa^2-244)/(78\varkappa^2+46)$, without the exponent $3/2$
  that Ding & Wu print; at $\varkappa=0$ the printed argument is
  $-244/46\approx-5.30$, outside the domain of the arccos, while with the
  exponent it is $-0.782$ and the formula returns their own value
  $2-\sqrt{14}/2$ *(compiler check, not in the sources)*.
- Ding & Wu's tests run at a step above the proved bound
  ([bound preservation](/properties/bound-preservation.md), Qualifications).

# Citations

- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §1 (Defs 1.1, 1.3; Problems 1.2, 1.4; Eqs. (1.6), (1.10), (1.13)–(1.15)); Thm 2.3; §3 (Lemmas 3.1–3.20, Thms 3.4, 3.12, 3.26, 3.29); Thm 4.1; §5 (Thms 5.1–5.17, Alg. 5.20); Thm 6.1 and Fig. 11; §7 (Thm 7.1, Rems. 7.4, 7.7); §8 (Tables 1–10); App. C.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: Thm 6.2 (Gauss–Lobatto BP CFL condition).
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §3.1–§3.2 (Eqs. (3.9)–(3.12), (3.26)–(3.30)).
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §3.2, Eqs. (3.6)–(3.11), Theorem 1; §3.4, Eq. (3.23); §4.2, Theorem 2.
- [Renac (2021)](/sources/renac-2021.md) — arXiv v3: Thm 6.1 (Eq. (66)), Rem. 6.1, App. A.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — arXiv v1: Rem. 3.4 (Eq. (44)); Thm 3.1 (Eqs. (57)–(59)).
- [Du & Yang (2022)](/sources/du-2022-b.md) — Thm 4.1; Thm 4.3 (Eq. (4.17)); Thms 5.4–5.6; Rem. 5.1.
- [Ding & Wu (2024)](/sources/ding-2024-b.md) — §4.3 (Eqs. (53)–(60), Fig. 2); §4.6 (Cors. 4.1–4.2, Eqs. (54)–(56), (76)–(77), Fig. 1, Remark 9).
- [Fan & Wu (2024)](/sources/fan-2024.md) — arXiv v1: §2.4, Eqs. (2.52)–(2.57), Thm 11, Remark 5.
