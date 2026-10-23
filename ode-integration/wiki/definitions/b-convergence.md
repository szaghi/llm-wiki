---
type: Definition
title: "B-convergence"
description: "B-convergence of order r: for problems with a one-sided Lipschitz bound, the global error is bounded by C h^r with C and the admissible step depending on the one-sided constant and solution derivatives but not on the stiffness; the page states the definition, the deferred-correction proof and its ROW and weak-stage-order lineage."
status: established
aliases: [B-convergent, B-convergence order, stiffness-independent convergence]
tags: [stiff, order-reduction, stability, implicit, b-convergence]
timestamp: 2026-10-19T11:55:00Z
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

- [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) — §1; Thm. 3.1 (Eq. (3.7), case (iv)); Cor. 4.1 (Eq. (4.18)); Remarks 4.1–4.2 (Eq. (4.19)); §6.1, §6.5, §6.7 (Tables 6.1, 6.5, 6.6).
- [Biswas et al. (2024)](/sources/biswas-2024.md) — keywords; §2.2 (local error uniform in $z$); §2.3 (Scholz, Hundsdorfer, Burrage–Hundsdorfer–Verwer, as recalled).
- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 (Eq. (1.4), Scholz and Ostermann–Roche conditions); §2 (Eqs. (2.5)–(2.13), error constant $C_1/z$); Table 1.
