---
type: Result
title: "Fully discrete cell entropy inequality of third-order Runge–Kutta DG"
description: "Wei and Shu prove a cell-by-cell square-entropy inequality for explicit third-order Runge–Kutta DG on Burgers' equation (P2, P3) and on strictly convex scalar laws (P1) under a time step proportional to the mesh width, for the three-stage family with third abscissa 1 and positive weights, which contains Kutta's method and excludes SSP-RK3."
status: established
aliases: [cell entropy inequality, local square entropy inequality, fully discrete local entropy inequality, splitting miracle, Wei–Shu theorem, RKDG entropy stability]
tags: [entropy-stability, strong-stability, runge-kutta, explicit, structure-preserving]
timestamp: 2026-10-20T16:00:00Z
---

# Fully discrete cell entropy inequality of third-order Runge–Kutta DG

For a scalar conservation law $\partial_tu+\partial_xF(u)=0$ with a convex entropy, an
**entropy inequality** of a fully discrete scheme can be global, a bound on the total
entropy as on [entropy stability](/properties/entropy-stability.md), or **local**: in
every cell $I_j$ of length $\Delta x_j$ (page-local),

$$\int_{I_j}\frac{\eta(u^{n+1})-\eta(u^n)}{h}\,dx+\hat G_{j+\frac12}-\hat G_{j-\frac12}\le0,$$

with a numerical entropy flux $\hat G$ that is consistent and depends only on nearby
cells (page-local $\hat G$, $u^n$ the DG solution at $t_n$)
([Wei & Shu 2026](/sources/wei-2026.md), §1, Eqs. (4)–(5)). With the square entropy
$\eta(u)=u^2/2$ this is the **cell square-entropy inequality**; summed over cells with
periodic or compactly supported data it gives $L^2$ stability,
$\lVert u^{n+1}\rVert\le\lVert u^n\rVert$, i.e.
[strong stability](/properties/strong-stability.md) for a nonlinear problem. Wei and Shu
prove the cell inequality for explicit Runge–Kutta discontinuous Galerkin (RKDG) methods of
third order under the standard CFL condition $h\le C\Delta x$, on nonuniform meshes,
without any smoothness assumption on the solution. They call it the first such proof for
explicit RKDG of order above one on a nonlinear conservation law (§1).

## Setting

The DG method uses piecewise polynomials of degree $k$ with the global Lax–Friedrichs flux
of viscosity $\alpha$, the maximum of $\lvert u\rvert$ over the point values for Burgers
($\max\lvert F'\rvert$ over the point values for the $P^1$ case of App. A; recomputed at
each stage), giving on each cell the ODE
$u'=\Delta x_j^{-1}\mathcal H[u]$ with point values $\mathcal H[u]$ that are quadratic
forms of the point values for Burgers (page-local $\alpha$, $\mathcal H$; §2, Eqs.
(7)–(11)). The mesh ratio is $\mu_j=h/\Delta x_j$ (page-local). Jiang and Shu proved the
**semi-discrete** cell square-entropy inequality for DG of any degree and any $F$; it
carries over to the fully discrete scheme for implicit
[algebraically stable](/properties/a-stability.md) Runge–Kutta methods, as Wei and Shu
recall (§1). The explicit case is the open one.

## The Runge–Kutta family

The time integrators are the explicit three-stage third-order methods with
$c_3=a_{31}+a_{32}=1$ and positive weights. In Butcher's parameterization by $c_2$
(Wei & Shu write $\omega=a_{21}$; §2, Eq. (12)),

$$\begin{aligned}
a_{21}&=c_2,\qquad a_{31}=\frac{1-3c_2(1-c_2)}{c_2(3c_2-2)},\qquad a_{32}=-\frac{1-c_2}{c_2(3c_2-2)},\\
b_1&=1-\frac{3c_2+1}{6c_2},\qquad b_2=\frac1{6c_2(1-c_2)},\qquad b_3=\frac{2-3c_2}{6(1-c_2)},
\end{aligned}$$

and $b_1,b_2,b_3>0$ iff $\tfrac13<c_2<\tfrac23$. **Kutta's third-order method**,
$c_2=\tfrac12$, $a_{31}=-1$, $a_{32}=2$, $b=(\tfrac16,\tfrac23,\tfrac16)$, is in the
family. **SSP-RK3** (Shu–Osher, $c=(0,1,\tfrac12)$) is not, since $c_3=\tfrac12$; nor is
Heun's third-order method, $c_3=\tfrac23$ *(compiler check, not in the sources, of the family with Eq. (12):
the weights sum to 1, $b^\top c=\tfrac12$, and $c_2=\tfrac12$ reproduces Kutta's
tableau)*. The exclusion is not an artefact of the proof: the authors' companion paper
shows by a counterexample that RKDG with $P^2$ elements and "a class of third-order
Runge-Kutta methods including the popular SSP Runge-Kutta (SSP-RK3)" is not $L^2$ stable
on Burgers under $h\sim\Delta x$, so no cell square-entropy inequality can hold there
(§1, recalled from Wei & Shu, submitted). On linear problems all three-stage third-order
methods coincide and the inequality holds for every one of them and every $P^k$
(Remark 1).

## The proof

**Energy identity.** For any Runge–Kutta method, on cell $I_j$ with stage values $Y_i$
(Eq. (13), from Ketcheson),

$$\lVert u^{n+1}\rVert_j^2-\lVert u^n\rVert_j^2=2\mu_j\sum_ib_i\langle Y_i,\mathcal H[Y_i]\rangle_j+\mu_j^2\sum_{i,l}b_i(b_l-2a_{il})\langle\mathcal H[Y_i],\mathcal H[Y_l]\rangle_j .$$

The first sum is bounded stage by stage by the Jiang–Shu semi-discrete argument: for
Burgers, under two CFL conditions that keep the stage maxima within $[\alpha/2,3\alpha/2]$,
each stage contributes a flux difference plus a negative jump term
$-\frac\alpha{12}(\llbracket Y_i\rrbracket^2_{j-1/2}+\llbracket Y_i\rrbracket^2_{j+1/2})$, and the
numerical entropy flux is the $b$-weighted sum of the stage entropy fluxes, consistent
because $\sum_ib_i=1$ (Eqs. (14)–(21)). The second sum is the obstacle: it is a quadratic
form of indefinite sign.

**The "splitting miracle"** (Thm. 1, Eq. (22)). If $a_{31}+a_{32}=1$, then with
$\mathcal H_i=\mathcal H[Y_i]$

$$\sum_{i,l}b_i(b_l-2a_{il})\langle\mathcal H_i,\mathcal H_l\rangle=-\frac{1-c_2}{12c_2^2}\lVert\mathcal H_1-\mathcal H_2\rVert^2-\frac{c_2}{12(1-c_2)^2}\lVert\mathcal H_2-\mathcal H_3\rVert^2+\frac{4-9c_2+9c_2^2}{36(1-c_2)^2}\Bigl\lVert\bigl(\tfrac1{c_2}-1\bigr)\mathcal H_1-\tfrac1{c_2}\mathcal H_2+\mathcal H_3\Bigr\rVert^2 .$$

The identity uses only the Runge–Kutta coefficients, so it holds for every nonlinear ODE
right-hand side, not only for DG (§1). The first two terms are negative squares of first
temporal differences, of size $O(\mu_j)$; the third is a positive square of a second
difference, of size $O(\mu_j^2)$; it is the nonlinear analogue of the temporal-difference
splitting used for linear problems by Xu, Zhang, Shu and Wang (Remark 1). The identity is
verified symbolically *(compiler check, not in the sources: the difference of the two
sides vanishes identically in $c_2$ for the parameterization above; the coefficient
$4-9c_2+9c_2^2$ is positive for all real $c_2$)*.

**Domination near the origin.** After the jumps are extracted by mean-value arguments,
it remains to show that the positive second-difference term is dominated by the negative
first-difference terms for small scaled point values (Thms. 2, 4). The ratio is a ratio of
polynomials with singular lines through the origin, where both vanish: for $P^2$ the lines
of constant data and of the point-value ratio $(1,-\tfrac32,1)$ (Lemma 1), for $P^3$ three
lines (Lemma 5, Cor. 1). Thin pyramids around each line are handled by local expansion
(Lemmas 2–3, 7–9), the rest of a sphere by compactness. For $P^3$ one step needs a
Gröbner-basis certificate computed with Buchberger's algorithm (Lemma 6). The constant of
the last CFL condition comes from compactness and is not computed (§3).

## Results

- **Theorem 3 ($P^2$) and Theorem 5 ($P^3$)**, Burgers' equation: for every method of the
  family there is $C>0$, depending only on $c_2$, such that $\max_j\mu_j\le C/\alpha$
  implies the cell square-entropy inequality with entropy flux
  $\hat G_{j+1/2}=\sum_ib_i\hat G^{(i)}_{j+1/2}$ (§3).
- **Theorem A.2 ($P^1$)**, any strictly convex $F$ that extends to an entire function:
  the same statement with a constant depending on $\lVert u\rVert_\infty$ and $c_2$; the
  small parameter is $\mu_j$ itself because $F$ is not homogeneous (App. A).
- The **positivity of all weights** is used in the CFL condition that makes the summed
  jump terms nonpositive, $\max\mu_j\le\min_ib_i/(6C\alpha)$ (page-local $C$; (CFL3)).
- No numerical experiments are reported; the paper is a proof.

## Relation to other entropy guarantees

- **SSP route.** An [SSP method](/methods/strong-stability-preserving-runge-kutta.md)
  inherits any convex-functional bound that forward Euler satisfies. Here the SSP
  property does not decide: SSP-RK3, the standard SSP method of RKDG, is the one shown to
  fail, and the positive result holds for non-SSP methods such as Kutta's (§1).
- **Relaxation.** Wei and Shu state that
  [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md) methods give no local
  entropy inequality, "since the relaxation constant is defined globally but not
  locally" (§1). The "local relaxation" of Al Jahdali et al. computes one root per cell
  but applies their minimum as one scalar, and no ingested source claims a cell entropy
  inequality for it *(compiler remark, not in the sources)*.
- **Energy method.** The identity behind the proof is the Runge–Kutta energy identity
  of the [energy method](/methods/runge-kutta-energy-method.md), extended from linear
  operators to a nonlinear right-hand side through the splitting of the quadratic form.

## Qualifications

- **Scope.** One space dimension, scalar laws, global Lax–Friedrichs flux, square
  entropy; $P^2$ and $P^3$ for Burgers only, $P^1$ for strictly convex entire fluxes; the
  CFL constants exist but are not evaluated.
- **Printed slips** (author manuscript of 5 September 2025). The relaxation sentence of
  §1 cites reference [4], a book on interpolation, where Ketcheson's relaxation paper,
  their [9], is meant. In the proof of Lemma 2 the first component of the substituted
  point is printed $s+sX-3sY$, whereas the definition of the pyramid,
  $s(1,-\tfrac32,1)+sX(-1,0,1)+sY(3,4,3)$, gives $s-sX+3sY$ *(compiler check of the printed definition)*. The proofs of
  Lemmas 7–8 sum to 3 where four components exist, and the proof of Lemma 1 writes
  $V=\frac{U+V}2$ for $V=\frac{U+W}2$. None changes a result.

# Citations

- [Wei & Shu (2026)](/sources/wei-2026.md) — §1, §2 (Eqs. (4)–(13)), §3 (Eqs. (14)–(22), Thm. 1, Remark 1, Thms. 2–5, CFL1–CFL4), §4 (Lemmas 1–3), §5 (Lemmas 4–9, Cor. 1), App. A (Thm. A.2, Lemmas A.4, A.6); author manuscript.
- [Al Jahdali et al. (2022)](/sources/aljahdali-2022.md) — §2 (global and local relaxation).
