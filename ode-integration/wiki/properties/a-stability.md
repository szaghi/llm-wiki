---
type: Property
title: "A-, L-, A(α)- and algebraic stability"
description: "Linear stability classes of one-step methods: A-stability (the stability region contains the left half-plane), L-stability (A-stability plus damping at infinity), A(α)- and L(α)-stability on a sector, and the nonlinear notions of B- and algebraic stability; with the facts the sources state about collocation, DIRK, Rosenbrock and multirate methods."
status: established
aliases: [A-stable, L-stable, A(alpha)-stability, L(alpha)-stability, B-stability, algebraic stability, unconditional linear stability, unconditionally stable, absolute stability]
tags: [stability, stiff, implicit, runge-kutta]
timestamp: 2026-10-19T20:00:00Z
---

# A-, L-, A(α)- and algebraic stability

Let $R(z)$ be the [stability function](/definitions/stability-function.md) of
a one-step method and $\mathcal S=\{z:\lvert R(z)\rvert\le1\}$.

* **A-stability:** $\mathcal S\supseteq\mathbb C^-=\{z:\operatorname{Re}z\le0\}$.
  The numerical solution of $y'=\lambda y$, $\operatorname{Re}\lambda<0$, then
  decays for every $h>0$, which is how
  [Farrell et al. (2021)](/sources/farrell-2021.md) (§2.1) state it.
  [Bassenne et al. (2021)](/sources/bassenne-2021.md) (Def. 3.1) use the same
  region definition and call such methods "unconditionally stable".
* **L-stability:** A-stability and $R(\infty)=0$
  (Farrell et al. (2021), §2.1; [Steinebach (2023)](/sources/steinebach-2023.md),
  §2: $\lvert R(z)\rvert<1$ for $\operatorname{Re}z<0$ and $R(\infty)=0$).
* **A($\alpha$)-stability:** $\mathcal S\supseteq W(\alpha)=\{z\neq0:\lvert\arg(-z)\rvert<\alpha\}$;
  **L($\alpha$)-stability** adds $R(\infty)=0$
  ([Roberts et al. (2021)](/sources/roberts-2021.md), Def. 3.2, there for the
  multirate stability function).

Explicit methods have polynomial $R$ and are never A-stable. A-stability
matters when the step is chosen for accuracy rather than for stability: an
explicit method for the heat equation needs $h=O(\Delta x^2)$, an A-stable one
allows $h=O(\Delta x)$; DAEs are "infinitely stiff", so A- and L-stability are
needed there; and for the wave equation the damping of L-stable methods is a
weakness (Farrell et al. (2021), §2.1, §4.3).

## An asymptotic definition, for methods without a stability function

[Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) (Def. 5.1,
after Dahlquist and Quarteroni et al.) define stability through the limit of the
sequence, not through $R$: a method is *absolutely stable* at $z=h\lambda$ if its
solution of $y'=\lambda y$, $y(0)=1$, satisfies $\lim_{n\to\infty}\lvert y_n\rvert=0$
for that fixed $h$; it is A-stable if this holds for every $z$ with
$\operatorname{Re}z<0$ (open half-plane). The convention differs from the one above:

- For a one-step method with stability function $R$, $y_n=R(z)^n$, so the
  asymptotic definition asks $\lvert R(z)\rvert<1$ on the open half-plane, which for a
  non-constant rational $R$ is equivalent to $\mathcal S\supseteq\mathbb C^-$ by the
  maximum principle and continuity *(compiler check, not in the sources)*.
- It also applies to methods that have no one-step recurrence. The authors need it
  for their [deferred-correction](/methods/deferred-correction.md) schemes DC$2j$,
  for which $y_n=\big(\tfrac{2+z}{2-z}\big)^{n-j}P_j(n)$ with a polynomial $P_j$ of
  degree $j$ in $n$ (Lemma 5.2), and which they prove A-stable for every order
  $2j$ (Thm. 5.1).
- It is weaker: it allows transient growth $\lvert y_n\rvert>\lvert y_0\rvert$ before
  the decay, through $P_j(n)$, and no bound uniform in $n$ and $z$ is given. The
  region definition guarantees $\lvert y_{n+1}\rvert\le\lvert y_n\rvert$ at every
  step. The DC$2j$ factor $(2+z)/(2-z)\to-1$ as $\lvert z\rvert\to\infty$, so there
  is no damping at infinity *(compiler check, not in the sources)*.

"A-stable at every order" in this sense does not conflict with the order barriers
for A-stable methods below, since DC$2j$ ($j\ge1$) is neither a Runge–Kutta method
(Remark 2.3) nor a linear multistep method *(compiler check, not in the sources)*. Farrell et al.'s phrase
"decays for every $h>0$" is the asymptotic form of the definition, which is
equivalent to the region form for one-step methods as just shown.

## Checking A-stability

By the maximum principle, a rational $R$ is A-stable iff it has no poles in
$\mathbb C^-$ and $\lvert R(iy)\rvert\le1$ for all real $y$. Roberts et al.
(2021, Thms. 3.1–3.2) prove the two-variable version for multirate methods and
generalize the single-rate E-polynomial test of Hairer–Wanner §IV.3: with
$R=N/D$, the imaginary-axis condition is
$E(y)=\lvert D(iy)\rvert^2-\lvert N(iy)\rvert^2\ge0$ for all real $y$
(single-rate form as recalled). [Biswas et al. (2023)](/sources/biswas-2023.md)
(§5, constraints (C.5)–(C.6)) impose $a_{ii}\ge0$, which places the DIRK poles
$1/a_{ii}$ in the right half-plane, and $\lvert R(iy)\rvert\le1$ on a finite
sample of the imaginary axis during optimization, then verify A-stability a
posteriori (Fig. 1). Remark 3.1 of Roberts et al. (2021) reduces an
A($\alpha$) check to the boundary of the sector. Bassenne et al. (2021, §3.2,
Cor. 3.4.1, citing Zlatev et al.) use the same two-part test for explicit
Runge–Kutta methods preconditioned by [TASE operators](/methods/tase-operators.md):
analyticity in $\mathbb C^-$ is proved, since all poles lie at $z=2^i/\vartheta>0$
($\vartheta$ the TASE parameter), while $\lvert R(iy)\rvert\le1$ is checked by dense
sampling only (Fig. 4).

## Facts stated by the sources

* **Multistep methods:** A-stable linear multistep methods have order at most
  2 (Dahlquist's second barrier), whereas A-stable RK methods exist of every
  order (Farrell et al. (2021), §2.1; [Southworth et al. (2022)](/sources/southworth-2022.md),
  §2.1).
* **Collocation families** (Farrell et al. (2021), §3.2, as recalled):
  Gauss–Legendre is A- and B-stable but not L-stable; Radau IIA is L-stable;
  Lobatto IIIC is A-, L- and B-stable. Its two-stage tableau is
  $c=(0,1)$, $A=\begin{pmatrix}1/2&-1/2\\1/2&1/2\end{pmatrix}$, $b=(1/2,1/2)$.
  See [fully implicit collocation methods](/methods/fully-implicit-runge-kutta.md).
* **Structure of $A$:** an A-stable, irreducible method with invertible $A$
  has all eigenvalues of $A$ in the open right half-plane (Southworth et al.
  (2022), §2.2, citing Hairer–Wanner). This is the assumption behind their
  preconditioners for [the stage equations](/methods/implicit-stage-solvers.md).
* **Stiff accuracy:** a [stiffly accurate](/properties/stiff-accuracy.md)
  method with invertible $A$ has $R(\infty)=0$, so A-stability implies
  L-stability (Biswas et al. (2023), §5; Steinebach (2023), §3). The
  weak-stage-order DIRKs of Biswas et al. (2023) and Rodas5P are L-stable by
  this route.
* **Padé approximations:** diagonal and first two subdiagonal approximations
  are A-stable; the $(0,3)$ approximation is A($\alpha$)-stable with
  $\alpha\approx88.23^\circ$ ([Sun et al. (2022)](/sources/sun-2022.md), §1,
  Ex. 4.5).
* **Linear systems:** for $y'=Ly$ with $L$ seminegative in an inner product,
  A-stability implies $\lVert R(hL)\rVert\le1$ for all $h$ (von Neumann's
  lemma, as recalled by Sun et al. (2022), §1, from Hairer–Wanner §IV.11),
  even for non-normal $L$. Southworth et al. (2022, §2.2) use the related
  fact that $\lVert e^{tL}\rVert\le1$ for all $t\ge0$ iff the field of values
  of $L$ lies in $\mathbb C^-$. See [strong stability](/properties/strong-stability.md).
* **$\theta$-method:** $R(z)=\big(1+(1-\theta)z\big)/(1-\theta z)$ is A-stable iff
  $\theta\ge\tfrac12$; Bassenne et al. (2021, Lemma 3.3) obtain it as explicit Euler
  applied to the first-order TASE system.
* **Explicit methods made A-stable by preconditioning:** explicit Runge–Kutta
  methods of $s\le4$ stages and order $s$, applied to a system preconditioned by a
  TASE operator of order $p\le\min(2,s)$, are A-stable (proved for $p=1$ under a
  sufficient condition on the parameter, numerical for $p=2$); for $p>2$ they are
  "nearly unconditionally stable", with $\max\lvert R(iy)\rvert\approx1.02$
  (Bassenne et al. (2021), Thm. 3.2, §2.6, §3.2, Figs. 1–4). This does not contradict
  the statement above that explicit methods are never A-stable: the preconditioned
  scheme solves linear systems at every stage and is linearly implicit, with a
  rational $R$ *(compiler check, not in the sources)*.
* **Rosenbrock methods:** Rodas5P and its embedded method are A-stable; the
  embedded method of Rodas5 is not (Steinebach (2023), Figs. 1–2).
* **Multirate methods:** a scalar test with one eigenvalue per partition
  gives scalar A-, L-, A($\alpha$)- and L($\alpha$)-stability; a $2\times2$
  test problem gives real and complex 2D A-stability. Complex-2D A-stability
  implies scalar A-stability, algebraic stability implies scalar A-stability,
  and no other implication holds in general (Roberts et al. (2021), Thm. 3.3,
  Fig. 3.1). No decoupled method is A-stable for the real 2D test (Thm. 3.4),
  and an internally consistent multirate method of order exactly one is scalar
  A-stable for only finitely many multirate ratios $m$ (Thm. 5.1). The
  compound-fast SDIRK-based methods are L($\alpha$)-stable with $\alpha$ about
  $83^\circ$, $86.8^\circ$ and $81.2^\circ$ at orders 2, 3, 4, nearly
  independent of $m$ (Table 5.1). See
  [linear stability of multirate methods](/definitions/multirate-linear-stability.md)
  and [multirate A-stability barriers](/results/multirate-a-stability-barriers.md).

## B- and algebraic stability

**B-stability** is the discrete analogue of contractivity: for problems whose
solutions satisfy $\lVert y(t_2)-\hat y(t_2)\rVert\le\lVert y(t_1)-\hat y(t_1)\rVert$
for $t_1\le t_2$, two numerical solutions do not separate either (Farrell et
al. (2021), §2.1). **Algebraic stability** is the algebraic condition on the
tableau under which this holds; its standard form is $b_i\ge0$ and
$\operatorname{diag}(b)A+A^\top\operatorname{diag}(b)-bb^\top$ positive
semidefinite *(standard definition supplied by the compiler; the sources use
the notion without restating it)*. The sources use it as follows:

* Gauss–Legendre and Lobatto IIIC are B-stable (Farrell et al. (2021), §3.2);
  algebraic stability of collocation methods gives $L^2$-stability of the
  corresponding Padé schemes (Sun et al. (2022), §1).
* Algebraic stability implies scalar A-stability for multirate GARK methods,
  but a method can be algebraically and scalar L-stable and still be only
  conditionally stable for the 2D test problem: the GARK method with tableau
  $1\,|\,0$; $1\,|\,1$, $b=(1\,|\,1)$ has spectral radius
  $(\sqrt5+3)/4>1$ on $H\Lambda=\begin{pmatrix}-1&1\\-10&-1\end{pmatrix}$
  (Roberts et al. (2021), §3.3).
* The new coupled and decoupled multirate backward Euler methods are scalar
  L-stable and algebraically stable for all $m$; the multirate implicit
  midpoint methods keep the algebraic stability, symmetry and symplecticity of
  implicit midpoint (Roberts et al. (2021), §5.1–5.2).

## Qualifications

* Steinebach (2023, §1) calls methods with $R(\infty)=0$ "stiffly stable";
  this is not Gear's region-based definition of stiff stability, and the
  property is what the other sources call damping at infinity (with
  A-stability: L-stability).
* [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) (§5.1) call their computation of bounded stability
  regions of explicit ADER and DeC an "A-stability" study; the methods are not
  A-stable ([stability function](/definitions/stability-function.md)).
* Farrell et al. (2021) state A-stability in the open half-plane
  ($\operatorname{Re}\lambda<0$, decay for every $h>0$), which is equivalent
  to the closed-half-plane form for rational $R$ by continuity
  *(compiler check, not in the sources)*.
* "Nearly unconditionally stable" (Bassenne et al. (2021), §2.6) is not a stability
  class: it names a method whose region misses small parts of $\mathbb C^-$ near the
  imaginary axis.
* Koyaguerebo-Imé & Bourgault (2022, §1) announce B-stability of their
  deferred-correction schemes but prove only [B-convergence](/definitions/b-convergence.md)
  (Cor. 4.1); the page records no B-stability result for them.
* Multirate stability depends on the basis in which the partitions are
  written, so a single scalar test equation does not settle it (Roberts et al.
  (2021), §3, after Gear).

# Citations

- [Farrell et al. (2021)](/sources/farrell-2021.md) — §2.1 (A-, L-, B-stability, Dahlquist barrier, heuristics), §3.2 (collocation families, Lobatto IIIC tableau), §4.3.
- [Steinebach (2023)](/sources/steinebach-2023.md) — §1, §2, §3, Figs. 1–2 (L-stability, "stiffly stable", Rodas5 and Rodas5P).
- [Roberts et al. (2021)](/sources/roberts-2021.md) — Defs. 3.1–3.2, Thms. 3.1–3.4, Remark 3.1, Fig. 3.1, §3.3, Thm. 5.1, §5.1–5.2, Table 5.1.
- [Sun et al. (2022)](/sources/sun-2022.md) — §1 (Padé A-stability, von Neumann lemma, algebraic stability), Ex. 4.5.
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §2.1 (Dahlquist barrier), §2.2 (eigenvalues of $A$, field of values).
- [Biswas et al. (2023)](/sources/biswas-2023.md) — §5 (constraints (C.5)–(C.6), A- and L-stability of the new DIRKs), Fig. 1.
- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §5.1 (terminology of the ADER/DeC stability study).
- [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) — §1; Remark 2.3; Def. 5.1, Lemma 5.2, Thm. 5.1 (asymptotic A-stability of DC$2j$).
- [Bassenne et al. (2021)](/sources/bassenne-2021.md) — Def. 3.1, Lemma 3.3, Thm. 3.2, Cor. 3.4.1, §2.6, §3.2, Figs. 1–4 (A-stability of explicit methods with TASE preconditioning).
