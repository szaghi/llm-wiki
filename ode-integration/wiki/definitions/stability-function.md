---
type: Definition
title: "Stability function, stability polynomial and stability region"
description: "The stability function R(z) is the factor by which a one-step method multiplies the solution of y' = λy per step; it is rational for implicit methods and a polynomial P(z) for explicit ones, its order and degree structure constrain the method, and its region of absolute stability decides the linearly stable step sizes for method-of-lines systems."
status: established
aliases: [linear stability function, amplification factor, stability polynomial, region of absolute stability, stability domain, linear stability region]
tags: [stability, runge-kutta, explicit, implicit]
timestamp: 2026-10-19T12:00:00Z
---

# Stability function, stability polynomial and stability region

Applied to the Dahlquist test equation $y'=\lambda y$, a
[Runge–Kutta method](/definitions/runge-kutta-method.md) gives
$y_{n+1}=R(z)\,y_n$, $z=h\lambda$, with **stability function**

$$R(z)=1+z\,b^\top(I-zA)^{-1}\mathbf 1=\frac{\det(I-zA+z\mathbf 1b^\top)}{\det(I-zA)}$$

([Biswas et al. (2023)](/sources/biswas-2023.md), Eq. (9);
[Biswas et al. (2024)](/sources/biswas-2024.md), Eq. (5)). For an explicit
method $A$ is nilpotent and $R$ is the **stability polynomial**

$$P(z)=1+\sum_{j=1}^{s}\theta_jz^j,\qquad \theta_j=b^\top A^{j-1}\mathbf 1,$$

of degree at most $s$ ([Biswas et al. (2025)](/sources/biswas-2025.md), §1;
[Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md), Eqs. (1)–(2)).
Order $p$ forces $\theta_j=1/j!$ for $j\le p$, so an explicit method has
$s-p$ free coefficients in $P$ (Hedayati Nasab et al. (2021), Eq. (3)); these
are the tall-tree [order conditions](/results/runge-kutta-order-conditions.md)
$T(p)$. The **region of absolute stability** is
$\mathcal S=\{z\in\mathbb C:\lvert R(z)\rvert\le1\}$.

## Method of lines: the step-size condition

For a semi-discretization $y'=Ly$ with diagonalizable $L$, linear stability
requires $h\lambda\in\mathcal S$ for every eigenvalue $\lambda$ of $L$; for a
given spectrum this fixes a maximal stable step, a function of the free
coefficients of $P$ (Hedayati Nasab et al. (2021), Eqs. (4)–(5)). Choosing
those coefficients to maximize the stable step for a given spectrum is the
subject of [optimal stability polynomials](/methods/optimal-stability-polynomial.md):
for flux-reconstruction DG spectra on six element types, the maximal stable
step grows about linearly with $s$, and the step per stage keeps increasing
beyond $s=16$ for orders 3 and 4 (§6). Eigenvalue analysis is only a necessary
condition when $L$ is not normal
([Sun et al. (2022)](/sources/sun-2022.md), §1); for inner-product norms the
energy approach of [strong stability](/properties/strong-stability.md) replaces
it.

[Fekete et al. (2022)](/sources/fekete-2022.md) (Defs. 1–4) characterize
$\mathcal S$ by four radii: real-axis inclusion (largest interval on the
negative real axis in $\mathcal S$), imaginary-axis inclusion (largest
$[-i\beta,i\beta]\subset\mathcal S$), circle contractivity (largest $r$ with
the disk $\lvert z+r\rvert\le r$ in $\mathcal S$) and the radius of absolute
monotonicity (largest $r$ such that $R$ and all its derivatives are
nonnegative on $(-r,0]$). The last one is the linear counterpart of the SSP
coefficient; see [SSP methods](/methods/strong-stability-preserving-runge-kutta.md).

## Structure of rational stability functions

Write $R=N/D$ with coprime polynomials (page-local $N$, $D$). Biswas et al.
(2024) use three facts:

* **Order barriers** (as recalled from Hairer–Wanner Thms. IV.3.11, IV.4.18
  and Nørsett–Wolfbrandt): if $N/D=e^z+O(z^{p+1})$ then
  $p\le\deg N+\deg D$; if all poles are real, $p\le\deg N+1$ (Thm. 3.7). The
  first is attained by Padé approximants; DIRKs have real poles $1/a_{ii}$.
* **Degree bound** (Thm. 3.8): $\deg N,\deg D\le\dim\mathcal Y$, where
  $\mathcal Y$ is the smallest $A^\top$-invariant subspace
  containing $b$. With the order barriers this gives
  $\lfloor(p+1+\delta_{\mathrm{SA}})/2\rfloor\le\dim\mathcal Y$, and
  $p\le\dim\mathcal Y+1-\delta_{\mathrm{SA}}$ for DIRKs, with
  $\delta_{\mathrm{SA}}=1$ for [stiffly accurate](/properties/stiff-accuracy.md)
  methods with invertible $A$ and 0 otherwise (page-local; Thm. 3.9).
* **Orthogonal-polynomial form** (Lemma 5.2): if $p\ge\dim\mathcal Y$, $R$ is
  determined by the coefficients of the minimal polynomial of $\mathcal Y$ in
  a family of polynomials orthogonal for the functional with moments
  $1/(n+1)!$.

For explicit methods the same chain reads
$p\le\deg P\le\dim\mathcal Y\le s-\dim\mathcal K_{q_{\mathrm w}}$, with $\mathcal K_{q_{\mathrm w}}$ the Krylov space of
stage-order residuals that [weak stage order](/definitions/weak-stage-order.md)
makes orthogonal to $b$. Hence weak stage order $q_{\mathrm w}$ forces the
highest $q_{\mathrm w}-1$ coefficients of $P$ to vanish, dual to order $p$
fixing the lowest $p+1$, and explicit methods with the minimum number of
stages for given $(p,q_{\mathrm w})$ have $P(z)=\sum_{j=0}^pz^j/j!$ exactly
(Biswas et al. (2025), Lemma 2.1, Thm. 2.6, §7).

## Padé approximations

The $(m,k)$ Padé approximation of $e^z$ (numerator degree $m$, denominator
degree $k$, as Sun et al. (2022) use the labels) has order $m+k$. Sun et al.
(2022, §1) recall: the diagonal $(s,s)$ approximations are A-stable and are
the stability functions of the Gauss collocation methods; the first and second
subdiagonals are A-stable; the others are not. The diagonal coefficients are
$N(z)=\sum_{i=0}^s\frac{s!\,(2s-i)!}{(2s)!\,i!\,(s-i)!}z^i$, $D(z)=N(-z)$ (Eq.
(5.1)). The $(0,3)$ approximation is A($\alpha$)-stable with
$\alpha\approx88.23^\circ$ (Ex. 4.5). Since their energy analysis uses only
$R$, it applies to any linear one-step method with rational $R$, without a
tableau (§3); the unconditional energy law of diagonal Padé schemes is on
[diagonal Padé strong stability](/results/diagonal-pade-strong-stability.md).

## Stability functions of other method families

* **Rosenbrock–Wanner methods.** [Steinebach (2023)](/sources/steinebach-2023.md)
  (Eq. (2.14)) writes $R$ as a polynomial of degree $s$ in $z/(1-\gamma z)$
  whose coefficients are sums of products of the method coefficients (Scholz's
  sums). The embedded method of Rodas5 is not A-stable (Fig. 1), which can
  force step reductions for eigenvalues near the imaginary axis; Rodas5P and
  its embedded method are A-stable (Fig. 2). See [Rodas5P](/methods/rodas5p.md).
* **Deferred correction and ADER.** [Han Veiga et al. (2021)](/sources/hanveiga-2021.md)
  (§5.1, Fig. 2) compute the regions of explicit ADER and explicit DeC
  numerically on a grid of $z$: they coincide for orders 2–5, do not depend on
  the node family (equispaced, Gauss–Legendre, Gauss–Lobatto) and grow with
  order. An analytic treatment "is not feasible" because it leads to
  polynomial inequalities of degree $p(p+1)$. See
  [deferred correction](/methods/deferred-correction.md) and
  [ADER](/methods/ader-time-integration.md).
* **Multirate, IMEX and splitting methods** need several scaled eigenvalues or
  a matrix test problem; see
  [linear stability of multirate methods](/definitions/multirate-linear-stability.md).
  The internal stability function $(I-zA)^{-1}\mathbf 1$ of the stages enters
  their formulas ([Roberts et al. (2021)](/sources/roberts-2021.md), §3.4).

Classes of $\mathcal S$ — A-, L-, A($\alpha$)-stability — are on
[A-stability](/properties/a-stability.md).

## Qualifications

* Notation varies: Fekete et al. (2022) write $\psi(z)$, Hedayati Nasab et al.
  (2021) $P_{s,q}(z)$ with coefficients $\gamma_j$ and order $q$, Han Veiga et
  al. (2021) $\phi(z)$, Sun et al. (2022) $Q(Z)^{-1}P(Z)$ with $s$ the
  polynomial degree rather than the stage count.
* Fekete et al. (2022, Def. 1) print the real-axis inclusion with a symmetric
  segment $[-\beta,\beta]$; for an explicit method this gives zero, and the
  intended segment is $[-\beta,0]$.
* Han Veiga et al. (2021, §5.1) print the region as $\{z:\phi(z)<1\}$
  without modulus and call their computation of the bounded regions of
  explicit methods an "A-stability" study; the explicit ADER and DeC schemes
  are not A-stable.
* Hedayati Nasab et al. (2021, §5) remove eigenvalues with positive real part
  at machine-precision level before optimizing, an ad hoc choice; they also do
  not analyse internal stability of their 16-stage methods.

# Citations

- [Biswas et al. (2023)](/sources/biswas-2023.md) — Eq. (9).
- [Biswas et al. (2024)](/sources/biswas-2024.md) — Eq. (5), Thms. 3.7–3.9, Lemma 5.2.
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1, Lemma 2.1, Thm. 2.6, §7.
- [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) — Eqs. (1)–(5), §5, §6.
- [Sun et al. (2022)](/sources/sun-2022.md) — §1, §3, Eq. (5.1), Ex. 4.5.
- [Fekete et al. (2022)](/sources/fekete-2022.md) — Defs. 1–4.
- [Steinebach (2023)](/sources/steinebach-2023.md) — Eq. (2.14), Figs. 1–2.
- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §5.1, Fig. 2.
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §3.4 (internal stability function).
