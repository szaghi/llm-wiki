---
type: Definition
title: "B-convergence"
description: "B-convergence of order r: for problems with a one-sided Lipschitz bound, the global error is bounded by C h^r with C and the admissible step depending on the one-sided constant and solution derivatives but not on the stiffness; the page states the definition, Dahlquist's 1963 stiffness-independent bound for the trapezoidal rule, the related stiff order, the deferred-correction proof and its ROW and weak-stage-order lineage."
status: established
aliases: [B-convergent, B-convergence order, stiffness-independent convergence]
tags: [stiff, order-reduction, stability, implicit, b-convergence]
timestamp: 2026-10-29T18:13:00Z
---

# B-convergence

**B-convergence** is convergence with error bounds that do not depend on the
stiffness. Consider $y'=f(t,y)$ with a **one-sided Lipschitz condition**

$$\big\langle f(t,y)-f(t,\tilde y),\,y-\tilde y\big\rangle\le\mu\,\lVert y-\tilde y\rVert^2$$

($\mu$ page-local, the one-sided Lipschitz constant; $\mu\le0$ is the dissipative
case). A method is **B-convergent of order $r$** if its global error satisfies
$\lVert y_n-y(t_n)\rVert\le C\,h^r$ for all $h\in(0,h_0)$, where $C$ and $h_0$
depend on $\mu$, on the final time and on derivatives of the exact solution, but
not on the classical Lipschitz constant $\Lambda$ of $f$ ($\Lambda$ page-local;
for a stiff problem $\Lambda\gg\lvert\mu\rvert$). This is the reading of
[Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md), Remark 4.1,
after Frank–Schneid–Ueberhuber and Kraaijevanger. A classical convergence bound,
whose constant grows like $e^{\Lambda T}$ or whose step restriction scales like
$1/\Lambda$, says nothing in the stiff regime; a B-convergence bound does.

B-convergence is the convergence counterpart of B-stability, the contractivity
notion defined for the same one-sided Lipschitz class with $\mu\le0$ (see
[A-, L- and algebraic stability](/properties/a-stability.md))
*(compiler gloss; the sources do not relate the two notions)*. The B-convergence
order of a method can be lower than its classical order $p$; that gap is
[order reduction](/definitions/order-reduction.md) measured uniformly in the
stiffness.

## Dahlquist's error bounds for the trapezoidal rule

[Dahlquist (1963)](/sources/dahlquist-1963.md) (§3) proves, for the trapezoidal rule, a global
error bound whose step restriction comes from a one-sided constant and not from
$\lvert h\,\partial f/\partial y\rvert$. He does not use the term B-convergence. In registry
notation, with page-local symbols:

- **Hypotheses.** A solution $y\in C^3$ on $[t_0,\infty)$; $f$ and $J=\partial f/\partial y$
  bounded and uniformly continuous in a tube of radius $\delta$ around it (Conditions A–B). The
  error $e$ of a perturbed solution satisfies $e'=g(t,e)=f(t,y(t)+e)-f(t,y(t))$. Condition
  C$'_\lambda$ asks for a symmetric matrix $\Sigma(t)$ with $\kappa_0^2\lvert z\rvert^2\le z^\top\Sigma(t)z\le\kappa_1^2\lvert z\rvert^2$
  and bounded $\partial\Sigma/\partial t$ such that a discrete analogue $W$ of the derivative of
  $e^\top\Sigma(t)e$ along the error equation satisfies
  $W\le2\mu_\Sigma\big(\lvert e\rvert^2+\lvert\tfrac12hg\rvert^2\big)$ (Eqs. (3.17)–(3.19)); $\mu_\Sigma$
  is Dahlquist's $\lambda$, and $\mu'_\Sigma$ its scaled version ($\mu_\Sigma/\kappa_0^2$ or
  $\mu_\Sigma/\kappa_1^2$ by sign). Malkin's theorem supplies such a $\Sigma$ when the linearized
  error equation is uniformly asymptotically stable (pp. 34–35).
- **Solvability.** If $h\mu'_\Sigma<1$ (no restriction when $\mu_\Sigma\le0$), the implicit step
  has at most one solution in the tube (Lemma 3.1), $I-\tfrac12hJ$ is non-singular there
  (Lemma 3.2), and a solution exists, proved by continuation in the step size rather than by
  fixed-point iteration (Lemma 3.3).
- **Bound** (Thm. 3.1, Eq. (3.35)).
  $$\lvert y_n-y(t_n)\rvert\le\Phi(t_n,h)\,\frac{\kappa_1}{\kappa_0}\,(1-h\mu'_\Sigma)^{-1/2},\qquad\Phi(t,h)=\epsilon_0e^{\rho(t-h)}+q^*\frac{1-e^{\rho t}}{1-e^{\rho h}},\qquad\rho=\frac1{2h}\log\frac{1+h\mu'_\Sigma}{1-h\mu'_\Sigma},$$
  with $\epsilon_0$ the initial error bound and $q^*$ a bound for the per-step perturbations plus
  the local truncation error, which is below $h^3\sup\lvert y'''\rvert/12$ (Eq. (3.32)).
- **Consequence.** For $\mu_\Sigma<0$ the bound stays bounded as $t\to\infty$, the step can be
  chosen from the local truncation error and the rate of change of the Lyapunov function alone,
  and the error stays bounded "even when $\lvert h\,\partial f/\partial x\rvert$ is large":
  "This is a generalization of the A-stability property" (pp. 40–41). His earlier bounds "are
  based on the assumption $\frac12h\lvert\partial f/\partial x\rvert<1$" (p. 40). For
  $\mu_\Sigma=0$, $\Phi$ grows linearly in $t$; Theorems 3.2–3.3 cover this borderline under a
  stronger condition, with $y'=-y^3$ as the example that satisfies it but no condition with
  negative $\mu_\Sigma$ (pp. 41–42).

The bound depends on $h$ through $q^*$; the paper states no convergence order. The Lyapunov
construction is also recorded on [G-stability](/properties/g-stability.md).

## Stiff order

[Hochbruck & Ostermann (2010)](/sources/hochbruck-2010.md) (§1, p. 212) measure all orders of
their survey as **stiff order**: a method has stiff order $p$ "(for a particular class of
problems) if the global error on finite time intervals can be uniformly bounded by $Ch^p$, where
$C$ is a constant that depends on the length of the time interval and on the chosen class of
problems, but neither on the stiffness nor on the step size $h$"; the classical order "is always
an upper bound to the stiff order". Their classes are defined by semigroup assumptions on the
linear part (e.g. analytic semigroups for parabolic problems); see
[exponential Runge–Kutta stiff order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md)
and [order reduction](/definitions/order-reduction.md). They recall from Strehmel–Weiner that
two-stage second-order exponential Runge–Kutta families are "B-consistent of order one" and the
Strehmel–Weiner four-stage scheme B-consistent of order two (§2.3, Exs. 2.18–2.19).

[Curtiss & Hirschfelder (1952)](/sources/curtiss-1952.md) (§3, Eqs. (16), (19)) print, for their
BDF-type schemes on the scalar [stiff](/definitions/stiffness.md) model equation, asymptotic
errors proportional to the coefficient $a$ (page-local; small $\lvert a/h\rvert$ is their
stiffness condition) times powers of the step; they state no bound or order uniform in $a$, and
the signs of the printed asymptotes are discussed on
[BDF](/methods/backward-differentiation-formula.md).

## B-convergence of deferred correction

Koyaguerebo-Imé & Bourgault (2022) prove B-convergence of every level of their
[deferred-correction](/methods/deferred-correction.md) hierarchy DC$2j$ built on the
implicit midpoint rule.

**Corollary 4.1.** Let $f:\mathbb R^d\to\mathbb R^d$ satisfy the one-sided
Lipschitz condition. Then the DC$2j$ solution satisfies

$$\lvert y^{[2j]}_n-y(t_n)\rvert\le C\,h^{2j},\qquad h\in(0,h_0),\qquad h_0=\begin{cases}2/\mu,&\mu>0,\\+\infty,&\mu\le0,\end{cases}$$

with $C$ independent of any global Lipschitz constant (Eq. (4.18); $y^{[2j]}_n$
denotes the level-$2j$ solution, page-local).

**Error form** (Remark 4.2, Eq. (4.19)). The proof of Thm. 3.1(iv) gives

$$\lVert y^{[2j+2]}_n-y(t_n)\rVert\le c\,C\Big(\frac{2+\mu h}{2-\mu h}\Big)^{n}h^{2j+2},\qquad n\ge j+1,\quad -2\le\mu h<2,$$

($c$ a page-local constant). The factor is the amplification factor of the
implicit midpoint rule evaluated at $\mu h$. For $\mu<0$ and moderate $h$ it is
small, so large steps give very accurate solutions even though $C$, which carries
derivatives of $y$ of order $2j+3$, can be very large. In the asymptotic regime,
the authors add, "a non B-convergent method can be competitive with respect to a
B-convergent one for sufficiently small time steps".

**Evidence** (§6). On the Bernoulli equation $y'=-0.1y-1000y^{20}$, $y(0)=1$,
with $\mu=-0.1$ for positive solutions and $\Lambda\approx2\times10^4$, the DC
schemes are accurate at $h=1$ (DC6 error $1.8\times10^{-4}$, DC10
$1.3\times10^{-4}$; BDF6 $6.1\times10^{-2}$) while explicit RK4 is unstable for
$h\ge2.03\times10^{-3}$ (§6.1, Table 6.1). The design orders, however, appear
only for $h\Lambda<2$: "Large time steps provide accurate approximations (as
expected from B-convergent methods), but asymptotic convergences are observed only
for $k\mu<2$" (§6.7, their $k\mu$ being $h\Lambda$ here). The
[Robertson problem](/benchmarks/robertson-problem.md) is presented as the test that
"addresses B-convergence", since its Jacobian has real negative eigenvalues of large
magnitude (§6.5).

## Order barriers for Rosenbrock methods and the weak-stage-order lineage

The [Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md)
$y'=\lambda(y-g)+g'$ has one-sided Lipschitz constant $\operatorname{Re}\lambda\le0$
and classical Lipschitz constant $\lvert\lambda\rvert$, so an error bound uniform in
$\lambda$ on it is a B-convergence statement for the scalar linear case
*(compiler check, not in the sources)*. The sources trace the stiff order conditions to this setting:

- [Biswas et al. (2024)](/sources/biswas-2024.md), §2.2–2.3, study the local error
  "uniformly in $z$", covering the stiff limit $h\to0$, $\lambda\to-\infty$,
  $z=h\lambda\to-\infty$. The local error is then at least of order $q+1$
  ($q$ the [stage order](/definitions/stage-order.md)) and in general not
  $p+1$; [weak stage order](/definitions/weak-stage-order.md) $q_{\mathrm w}$ makes it
  $\mathcal O(h^{q_{\mathrm w}+1})$ uniformly in $z$.
- As recalled by Biswas et al. (2024, §2.3), Scholz turned the Ostermann–Roche
  conditions into conditions on the coefficients by expanding in
  $H=z/(1-\gamma z)$ (page-local; possible only for singly diagonally implicit structure), "developed
  B-convergence order barriers (up to order 4) for ROW methods", and constructed
  schemes with $p=q_{\mathrm w}=4$. Hundsdorfer proved an $\mathcal O(h^{q+1})$
  rate for linearly implicit Runge–Kutta schemes on linear ODEs under a
  generalization of the same conditions, and Burrage–Hundsdorfer–Verwer used them for
  improved convergence estimates (§2.3 and footnote 1, as recalled). "B-convergence"
  is one of the paper's keywords.
- [Steinebach (2023)](/sources/steinebach-2023.md), §1–2, imposes Scholz's two
  conditions $C_2(H)=C_3(H)=0$ on [Rodas5P](/methods/rodas5p.md) so that the order
  on Prothero–Robinson is "independent on $\lambda$". He also reports that Scholz's
  error-constant estimate is not sharp: for L-stable methods the constant behaves
  like $C_1/z$, so at fixed large $\lvert\lambda\rvert$ Rodas4P and Rodas4P2 show
  order $p-1=3$ although they satisfy both conditions (§2, Table 1). See
  [Rosenbrock–Wanner methods](/methods/rosenbrock-wanner-method.md).

## Qualifications

- **"Independent of the Lipschitz constant" is partly nominal.** In the proof of
  Corollary 4.1, $C$ depends on a bound of the Jacobian $\partial f/\partial y$ on a
  compact set containing the solution. The authors themselves call the
  independence "somewhat artificial", because $y''=f_t+\frac{\partial f}{\partial y}y'$
  ties the solution derivatives that enter $C$ to the Jacobian (Remark 4.1).
- **Step restriction dropped in the corollary.** Theorem 3.1(iv) needs
  $-2\le\mu h<2$; Corollary 4.1 states $h_0=+\infty$ for $\mu\le0$ without the
  lower bound $\mu h\ge-2$ (for the Bernoulli test, $h\le20$). This is a printed
  inconsistency of Koyaguerebo-Imé & Bourgault (2022) *(compiler check, not in the sources)*.
- **B-convergence is not B-stability.** The introduction of Koyaguerebo-Imé &
  Bourgault (2022, §1) announces that each DC scheme "is B-stable"; the body proves
  B-convergence (Cor. 4.1) and no contractivity result.
- **Observed orders are pre-asymptotic.** On the Bernoulli test DC4 shows orders
  3.33–3.79 and the highest levels fall below design, and on the
  [Van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md) DC2 and DC4 show
  order 0 down to $h=7.5\times10^{-6}$ (Tables 6.1, 6.6). The proved bound holds
  with a constant that is large in these regimes, so the theorem and the tables are
  compatible, but the numerics do not show the stiffness-independent order itself.

# Citations

- [Dahlquist (1963)](/sources/dahlquist-1963.md) — §3 (Conditions A, B, C$'_\lambda$, C$''_0$; Eqs. (3.17)–(3.19), (3.32), (3.35); Lemmas 3.1–3.3; Thms. 3.1–3.3; pp. 34–42).
- [Hochbruck & Ostermann (2010)](/sources/hochbruck-2010.md) — §1, p. 212 (stiff order); §2.3, Exs. 2.18–2.19 (B-consistency, as recalled).
- [Curtiss & Hirschfelder (1952)](/sources/curtiss-1952.md) — §3, Eqs. (16), (19).

- [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) — §1; Thm. 3.1 (Eq. (3.7), case (iv)); Cor. 4.1 (Eq. (4.18)); Remarks 4.1–4.2 (Eq. (4.19)); §6.1, §6.5, §6.7 (Tables 6.1, 6.5, 6.6).
- [Biswas et al. (2024)](/sources/biswas-2024.md) — keywords; §2.2 (local error uniform in $z$); §2.3 (Scholz, Hundsdorfer, Burrage–Hundsdorfer–Verwer, as recalled).
- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 (Eq. (1.4), Scholz and Ostermann–Roche conditions); §2 (Eqs. (2.5)–(2.13), error constant $C_1/z$); Table 1.
