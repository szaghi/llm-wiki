---
type: Definition
title: "Linear stability of multirate methods and joint stability regions"
description: "Defines the scalar and 2D (Gear) test problems for multirate and GARK methods, their stability functions and scalar, real-2D and complex-2D A-, L-, A(α)- and L(α)-stability, the implication hierarchy between them, and the joint stability region used for IMEX multirate methods."
status: established
aliases: [scalar A-stability, 2D A-stability, Gear test problem, joint stability region, multirate stability function]
tags: [multirate, stability, imex, stiff]
timestamp: 2026-10-19T00:00:00Z
---

# Linear stability of multirate methods and joint stability regions

For a single-rate Runge–Kutta method the Dahlquist equation $y'=\lambda y$ and
its [stability function](/definitions/stability-function.md) $R(z)$ decide linear
stability, because the method commutes with diagonalization. A multirate or
[GARK](/methods/generalized-additive-runge-kutta.md) method treats the partitions
of $f=f^{\{\mathrm f\}}+f^{\{\mathrm s\}}$ differently, so its linear stability
depends on the basis, and one scalar test is not enough (Roberts et al. 2021, §3,
after Gear). The sources therefore use a **scalar** test problem with one
eigenvalue per partition, which models partitions whose Jacobians triangularize
simultaneously, and a **2D** test problem with coupling. Every argument $z$ is
scaled by the **macro step** $H$, so the fast base method sees $z^{\{\mathrm f\}}/m$.

## Scalar test problem

$$y'=\lambda^{\{\mathrm f\}}y+\lambda^{\{\mathrm s\}}y,\qquad \lambda^{\{\mathrm f\}},\lambda^{\{\mathrm s\}}\in\mathbb C^-=\{\operatorname{Re}z\le0\},\qquad z^{\{\mathrm f\}}=H\lambda^{\{\mathrm f\}},\ z^{\{\mathrm s\}}=H\lambda^{\{\mathrm s\}}.$$

The step multiplies $y_n$ by the two-variable function
$R_{\mathrm{mr}}(z^{\{\mathrm f\}},z^{\{\mathrm s\}})$ (page-local symbol; formula on
[GARK](/methods/generalized-additive-runge-kutta.md)), which for a multirate method
also depends on $m$. [Roberts et al. (2021)](/sources/roberts-2021.md) define
(Defs. 3.1–3.2), with
$\mathcal S_{\mathrm{mr}}=\{(z^{\{\mathrm f\}},z^{\{\mathrm s\}})\in\mathbb C^2:\lvert R_{\mathrm{mr}}\rvert\le1\}$
and the wedge $W(\alpha)=\{z\ne0:\lvert\arg(-z)\rvert<\alpha\}$:

- **scalar A-stable** if $\mathcal S_{\mathrm{mr}}\supseteq\mathbb C^-\times\mathbb C^-$;
- **scalar L-stable** if scalar A-stable and $R_{\mathrm{mr}}\to0$ as
  $z^{\{\mathrm f\}}\to\infty$ **and** as $z^{\{\mathrm s\}}\to\infty$, each variable
  separately (eq. 3.5);
- **scalar A($\alpha$)-stable** if $\mathcal S_{\mathrm{mr}}\supseteq W(\alpha)\times W(\alpha)$,
  and **scalar L($\alpha$)-stable** if in addition (3.5) holds.

These reduce to the single-rate notions of
[A-, L- and A($\alpha$)-stability](/properties/a-stability.md) when one partition
is empty.

**Theorem (imaginary-axes criterion; Roberts et al. 2021, Thm. 3.1).** A GARK
method is scalar A-stable if and only if
$\lvert R_{\mathrm{mr}}(i\rho^{\{\mathrm f\}},i\rho^{\{\mathrm s\}})\rvert\le1$ for all real
$\rho^{\{\mathrm f\}},\rho^{\{\mathrm s\}}$ (page-local) and $R_{\mathrm{mr}}$ is analytic on
$\mathbb C^-\times\mathbb C^-$. The proof uses the multivariate maximum principle;
the check drops from four real dimensions to two. The A($\alpha$) angle is found
by checking only $\partial W(\alpha)\times\partial W(\alpha)$ (Remark 3.1).

**Theorem (E-polynomial; Roberts et al. 2021, Thm. 3.2).** Write
$R_{\mathrm{mr}}=P_{\mathrm{mr}}/Q_{\mathrm{mr}}$ and

$$E\big(\rho^{\{\mathrm f\}},\rho^{\{\mathrm s\}}\big)=Q_{\mathrm{mr}}(i\rho^{\{\mathrm f\}},i\rho^{\{\mathrm s\}})\,Q_{\mathrm{mr}}(-i\rho^{\{\mathrm f\}},-i\rho^{\{\mathrm s\}})-P_{\mathrm{mr}}(i\rho^{\{\mathrm f\}},i\rho^{\{\mathrm s\}})\,P_{\mathrm{mr}}(-i\rho^{\{\mathrm f\}},-i\rho^{\{\mathrm s\}}).$$

The scalar stability region contains the imaginary axes if and only if
$E\ge0$ on $\mathbb R^2$; this generalizes the single-rate E-polynomial of
Hairer–Wanner as recalled by Roberts et al.

## 2D (Gear) test problem

$$\begin{bmatrix}y^{\{\mathrm f\}}\\ y^{\{\mathrm s\}}\end{bmatrix}'=\begin{bmatrix}\lambda^{\{\mathrm f\}}&\eta^{\{\mathrm s\}}\\ \eta^{\{\mathrm f\}}&\lambda^{\{\mathrm s\}}\end{bmatrix}\begin{bmatrix}y^{\{\mathrm f\}}\\ y^{\{\mathrm s\}}\end{bmatrix}$$

(Roberts et al. 2021, eq. 3.7; $\eta^{\{\cdot\}}$ the coupling entries,
page-local). The admissible set $\mathbb M$ (page-local) holds the matrices with
bounded exact solutions (eigenvalues with non-positive real part, regular on the
imaginary axis) and $\lambda^{\{\mathrm f\}},\lambda^{\{\mathrm s\}}\in\mathbb C^-$. The
**real** variant takes real $\lambda^{\{\mathrm f\}},\lambda^{\{\mathrm s\}}\le0$ with
$\eta^{\{\mathrm f\}}\eta^{\{\mathrm s\}}\le\lambda^{\{\mathrm f\}}\lambda^{\{\mathrm s\}}$.
One step multiplies the state by a $2\times2$ stability matrix $\mathbf R_2(Z)$,
$Z=H\cdot(\text{test matrix})$, built from the four GARK blocks (eq. 3.8).

- **Complex 2D A-stable** (Def. 3.3): $\mathbf R_2(Z)$ is **power bounded** for every
  $Z\in\mathbb M$ (a spectral radius at most one is not enough).
- **Real 2D A-stable** (Def. 3.4): the same for real $Z\in\mathbb M\cap\mathbb R^{2\times2}$.

On the skew test matrix $\begin{bmatrix}0&\eta\\-\eta&0\end{bmatrix}$ the matrix
$\mathbf R_2$ depends only on the coupling blocks $A^{\{\mathrm f,\mathrm s\}}$,
$A^{\{\mathrm s,\mathrm f\}}$ and the weights, not on the base methods (eq. 3.10).
This is the lever of the decoupled-method barrier on
[multirate A-stability barriers](/results/multirate-a-stability-barriers.md).

The two tests are linked by the identity
$R_{\mathrm{mr}}(z^{\{\mathrm f\}},z^{\{\mathrm s\}})=[1\ 1]\,\mathbf R_2\!\begin{pmatrix}z^{\{\mathrm f\}}&z^{\{\mathrm f\}}\\ z^{\{\mathrm s\}}&z^{\{\mathrm s\}}\end{pmatrix}\begin{bmatrix}\alpha\\1-\alpha\end{bmatrix}$
for any $\alpha\in\mathbb C$ (eq. 3.13; $\alpha$ page-local), so $R_{\mathrm{mr}}$ is an
eigenvalue of that $\mathbf R_2$.

## Hierarchy

Roberts et al. (2021, Thm. 3.3, Fig. 3.1) prove or state:

- complex 2D A-stable ⇒ scalar A-stable (Thm. 3.3) and ⇒ real 2D A-stable;
- algebraically stable ⇒ scalar A-stable;
- scalar L ⇒ scalar A ⇒ scalar A($\alpha$); scalar L ⇒ scalar L($\alpha$) ⇒ scalar A($\alpha$).

"In general, no implication arrows are reversible." Two counterexamples show that
the scalar and the real 2D notions are independent:

- the GARK tableau with rows $(1\,|\,0)$, $(1\,|\,1)$ and weights $(1\,|\,1)$ is
  scalar L-stable and algebraically stable, but on the matrix
  $\begin{bmatrix}-1&1\\-10&-1\end{bmatrix}$ its $\mathbf R_2$ has spectral radius
  $(\sqrt5+3)/4>1$, so it is only conditionally stable in 2D (§3.3);
- a GARK method whose base is only A(45°)-stable has
  $\lvert R_{\mathrm{mr}}(-4+8i,0)\rvert=\sqrt{17}/4>1$ yet is stated to be real-2D
  A-stable (eq. 3.12): the real 2D test cannot see base-method instabilities off
  the real axis, which is why the complex variant is needed.

## Joint stability region (IMEX multirate)

For a three-way split $y'=f^{\mathrm I}+f^{\mathrm E}+f^{\{\mathrm f\}}$ (slow stiff,
slow nonstiff, fast) [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md)
(§3, eq. 3.3) use $y'=(\lambda^{\{\mathrm f\}}+\lambda^{\mathrm E}+\lambda^{\mathrm I})y$
with all $z=H\lambda$, solve the fast problem exactly by variation of constants,
and obtain a three-variable stability function
$R_{\mathrm{mr}}(z^{\{\mathrm f\}},z^{\mathrm E},z^{\mathrm I})$ built from
$\phi$-functions of $\Delta c_iz^{\{\mathrm f\}}$ (formula on
[IMEX-MRI-GARK](/methods/imex-mri-gark.md)). Extending Zharovsky et al., as
recalled there, they define the **joint stability region**

$$\mathcal J_{\alpha,\beta}=\Big\{z^{\mathrm E}\in\mathbb C^-:\ \lvert R_{\mathrm{mr}}(z^{\{\mathrm f\}},z^{\mathrm E},z^{\mathrm I})\rvert\le1\ \ \forall z^{\{\mathrm f\}}\in S_\alpha,\ \forall z^{\mathrm I}\in S_\beta\Big\},\qquad S_\alpha=\{z\in\mathbb C^-:\lvert\arg z-\pi\rvert\le\alpha\}.$$

It is the region of admissible explicit arguments that stays valid for every fast
eigenvalue in a sector of half-angle $\alpha$ and every slow stiff eigenvalue in a
sector of half-angle $\beta$ ($\alpha$, $\beta$ page-local). The authors call it
"artificially restrictive", because the stiff partitions will not in practice be
infinitely stiffer than $f^{\mathrm E}$. They use it to optimize IMEX-MRI-GARK3b
and to reject IMEX-MRI-GARK4, whose joint region is empty.

## Qualifications

- Both sources assume simultaneously diagonalizable (scalar) or $2\times2$ model
  coupling; Roberts et al. mention a block generalization (eq. 3.11) and Skelboe's
  more general one without pursuing them.
- Roberts et al. use the macro step for both scaled eigenvalues; Chinomona &
  Reynolds do the same for all three. Single-rate pages scale by the step $h$.
- The sector notation differs: Roberts et al. use the open wedge
  $\lvert\arg(-z)\rvert<\alpha$, Chinomona & Reynolds the closed sector
  $\lvert\arg z-\pi\rvert\le\alpha$. Chinomona & Reynolds' prose (p. 16 of the
  version read) swaps $\alpha$ and $\beta$ relative to their own definition and to
  their §4.1 usage ($\alpha$ fast, $\beta$ implicit); the definition is the one
  given here.
- Chinomona & Reynolds print the $\phi$-functions without the $1/(k-1)!$ factor;
  their $\varphi_{k+1}$ equals $k!\,\phi_{k+1}$ in the registry convention.

# Citations

- [Roberts et al. (2021)](/sources/roberts-2021.md) — §3 (eqs. 3.3–3.13, Defs. 3.1–3.4, Thms. 3.1–3.3, Remarks 3.1–3.2, Fig. 3.1).
- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §3 (eqs. 3.1–3.3, joint stability region), §4.1, Fig. 1.
