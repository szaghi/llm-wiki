---
type: Property
title: "A-, L-, A(α)- and algebraic stability"
description: "Linear stability classes of one-step and linear multistep methods: A-stability (the stability region contains the left half-plane), L- and strong A-stability (damping at infinity), A(α)- and L(α)-stability on a sector, and the nonlinear notions of B-, algebraic and G-stability; with the facts the sources state about collocation, DIRK, Rosenbrock, TASE, IMEX, multirate, BDF and linearly implicit multistep methods."
status: established
aliases: [A-stable, L-stable, A(alpha)-stability, L(alpha)-stability, strong A-stability, strongly A-stable, B-stability, algebraic stability, unconditional linear stability, unconditionally stable, absolute stability, stability angle]
tags: [stability, stiff, implicit, runge-kutta]
timestamp: 2026-10-20T10:00:00Z
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
* **Strong A-stability:** A-stability and $\lvert R(\infty)\rvert<1$, with $R(\infty)$ the limit
  along the negative real axis ([Conte et al. (2024)](/sources/conte-2024.md), §2). It sits
  between A- and L-stability.
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
  §2.1; [Taddei et al. (2026)](/sources/taddei-2026.md), §1.1). The multistep classes are in the
  section *Linear multistep methods* below.
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
  The route needs $A$ invertible. For a stiffly accurate implicit tableau of
  type II, whose first stage is explicit and whose $A$ is therefore singular,
  A-stability and stiff accuracy do not give L-stability.
  [Orlando et al. (2025)](/sources/orlando-2025-b.md) (§3.1, Eq. (32)) recall the
  supplementary condition $\mathbf e_s^\top\hat A^{-1}a=0$, with $\hat A$ the
  invertible lower block of the tableau and $a$ its first column below the
  diagonal (page-local). They state that all implicit tableaux of their
  [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) schemes are L-stable.
  [Taddei et al. (2026)](/sources/taddei-2026.md) (§1.1, §3.1) use Radau IIA
  as A-stable, L-stable and stiffly accurate, so that the step value is the
  last stage.
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
* **TASE–Runge–Kutta with the Calvo–Montijano–Rández operators:** TRK2 is strongly
  A-stable with $R(\infty)=0.5$, TRK3 is L($\alpha$)-stable with $\alpha=89.02^\circ$, and
  TRK4 is strongly A($\alpha$)-stable with $\alpha=87.34^\circ$ and $R(\infty)=0.27$, all with
  the exact Jacobian (Conte et al. (2024), §2, Table 1, as recalled from Calvo et al.).
  When the operator uses a matrix $W\ne J$ (page-local), stability is no longer a property of
  $R$ alone. Write $J=W+(J-W)$ and let $\lambda$ and $\lambda'$ be paired eigenvalues of $W$
  and of $J-W$ ($\lambda'$ page-local). The scalar test becomes two-parametric, with
  $R=P\big(\hat T(h\lambda)(1+\lambda'/\lambda)\big)$ for $P$ the explicit stability
  polynomial and $\hat T$ the scalar TASE map. "Unconditional stability" for every $h>0$ then
  holds iff all generalized eigenvalues of $(W,J-W)$ lie in a limiting diagram, when $W$ and
  $J-W$ are simultaneously diagonalizable. With real ratios $\lambda'/\lambda$ the method is
  unconditionally stable if every ratio is at most 1, 0.5743 or 0.7445 for $p=2,3,4$ (§3, Lemma 3.4, Thms. 3.6, 4.5, Remark 4.2;
  0.7445 as printed, the reader of the source recomputes 0.7451). In
  general only a weighted field-of-values condition is sufficient (Thms. 5.5–5.6). See
  [TASE operators](/methods/tase-operators.md).
* **Implicit ADER-DG:** [Popov (2024)](/sources/popov-2024.md) (§1.2, Figs. 1–2)
  concludes that the Gauss–Legendre ADER-DG solver iterated to convergence is A-stable
  from plotted stability regions for degrees $1\le\mathsf M\le60$, and "L-stable; more
  precisely — L1-stable" from a rank computation for $\mathsf M\le80$ showing that $R$ has
  numerator degree $\mathsf M$ and denominator degree $\mathsf M+1$, so
  $\lvert R(z)\rvert\sim\lvert z\rvert^{-1}$. Both are inferred for finitely many degrees,
  not proved; "L1-stable" is not a separate class here but L-stability with
  $R=\mathcal O(\lvert z\rvert^{-1})$. *(Compiler check, not in the sources:* numerically
  this $R$ equals the $(\mathsf M,\mathsf M+1)$ subdiagonal Padé approximant for
  $\mathsf M\le12$; if that holds at every degree, the Padé fact above gives both properties
  at every degree; details on [ADER](/methods/ader-time-integration.md).)
* **Spectral deferred correction with $K$ sweeps:** Picard SDC is never A-stable, and the
  diagonal (parallel) preconditioner MIN-SR-NS is not A-stable for any $K$. For four
  Radau-right nodes, MIN-SR-S "appears" A-stable for $K\ge3$ and MIN-SR-FLEX "seems"
  A-stable for every $K$, with regions close to those of serial LU-SDC; MIN-SR-FLEX with five
  Lobatto nodes and $K=4$ is not (not shown). All of this is read from plots
  ([Čaklović et al. 2025](/sources/caklovic-2025.md), §3.2, Figs. 5–9, §5). They also
  report that the collocation update can remove the apparent A-stability of some
  preconditioners (Remark 2.1). See [parallel SDC](/methods/parallel-sdc.md).
* **Parareal propagators:** [Jin et al. (2025)](/sources/jin-2025.md) (§2.1, Remark 2.3)
  require of the fine propagator $\lvert R\rvert<1$ on the negative real axis and strong
  stability $\lvert R(\infty)\rvert<1$; fine propagators with $\lvert R(\infty)\rvert=1$,
  such as Crank–Nicolson and the Gauss methods, make Parareal converge only for a bounded
  spectrum and enough fine steps per slice, and are "seldom used". Their optimized coarse
  propagators are consistent and strongly stable by construction (Prop. 3.3). The two-,
  three- and four-stage Lobatto IIIC methods have the $(0,2)$, $(1,3)$ and $(2,4)$ Padé
  approximants and three-stage Radau IIA the $(2,3)$ one (Table 4.1). See
  [Parareal](/methods/parareal.md).
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

## Linear multistep methods

For a [linear multistep method](/methods/linear-multistep-method.md) there is no single stability
function. The stability region is the set of $z=h\lambda$ for which all roots of
$\varrho(\zeta)-z\sigma(\zeta)=0$ satisfy $\lvert\zeta\rvert\le1$, with multiple roots strictly
inside ([Glandon et al. (2022)](/sources/glandon-2022.md), §4, Eq. (4.3), as recalled from
Hairer–Wanner §V). Its boundary is traced by $z=\varrho(e^{i\phi})/\sigma(e^{i\phi})$ ($\phi$
page-local; Eq. (4.4)). A-, A($\alpha$)- and L-type notions are then defined with this region in
place of $\mathcal S$. At $z=0$ the root condition is
[zero-stability](/definitions/zero-stability.md).

**Stability angles.** [BDF](/methods/backward-differentiation-formula.md) is A-stable for $k=1,2$
and A($\alpha$)-stable for $3\le k\le6$:

| $k$ | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| $\alpha$ | $86.03^\circ$ | $73.35^\circ$ | $51.84^\circ$ | $17.84^\circ$ |

([Akrivis et al. (2021)](/sources/akrivis-2021.md), arXiv v1, §1, for $k\le6$; Glandon et al. (2022),
Table 6.1, for $k\le5$, in agreement.) The optimized
[linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md) of Glandon
et al. reach $87.78^\circ$, $78.07^\circ$ and $73.00^\circ$ (Limm) and $87.39^\circ$,
$77.91^\circ$ and $70.32^\circ$ (Limm-W) at orders 3–5, and are A-stable at orders 1–2 (Table
6.1, Fig. 6.1).

**Damping at infinity.** The analogue of $R(\infty)=0$ is that all roots $\zeta(z)\to0$ as
$z\to-\infty$. For BDF, $\sigma(\zeta)=\zeta^k$ gives it. For the Limm methods Glandon et al.
impose that $\sigma(0)$ vanishes (in their notation; §6). They call this "a condition for
L-stability". Their orders 3–5 are only A($\alpha$)-stable, so the property is damping at
infinity, not L-stability. Their convergence theorem assumes the stability matrix to be strictly
stable at $0$ and at $\infty$ (Assumption 5.2).

**A-stability and G-stability.** A-stability of a multistep method is equivalent to
[G-stability](/properties/g-stability.md) of its one-leg twin (Dahlquist; recalled by Akrivis et
al. (2021), Lemma 2.1, and [Ma et al. (2026)](/sources/ma-2026.md), §2.2). Energy proofs for BDF
rest on this equivalence. For BDF3–BDF6, which are not A-stable, the auxiliary pair of the
[multiplier technique](/methods/multiplier-energy-technique.md) must be A-stable in place of the
method itself.

**Why the barrier matters in practice.** [Taddei et al. (2026)](/sources/taddei-2026.md) (§1.1)
cite Dahlquist's second barrier as the reason that higher-order BDF cannot be A- and L-stable.
They use Radau IIA instead for high-order fluid–structure interaction.

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
* Popov (2024), Čaklović et al. (2025) and, for the ODE regions of explicit ADER and DeC,
  Han Veiga et al. (2021) establish their stability claims by plotting regions; none
  proves A-stability. Popov's sampled degrees ($\le60$) and Čaklović et al.'s node sets
  are the scope of the claims.
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
- [Akrivis et al. (2021)](/sources/akrivis-2021.md) — arXiv v1: §1 (BDF stability angles), Lemma 2.1 (A- and G-stability).
- [Glandon et al. (2022)](/sources/glandon-2022.md) — §4 (Eqs. (4.3)–(4.4)), Assumption 5.2, §6, Table 6.1, Fig. 6.1 (multistep stability region, BDF and Limm angles, damping at infinity).
- [Conte et al. (2024)](/sources/conte-2024.md) — §2 (Table 1, strong A-stability), §3 (Lemma 3.4, Thm. 3.6), Thm. 4.5, Remark 4.2, Thms. 5.5–5.6.
- [Orlando et al. (2025)](/sources/orlando-2025-b.md) — §3.1 (Eq. (32), L-stability of stiffly accurate type II tableaux).
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §1.1, §3.1 (Dahlquist barrier, Radau IIA properties).
- [Ma et al. (2026)](/sources/ma-2026.md) — §2.2 (A- and G-stability).
- [Popov (2024)](/sources/popov-2024.md) — §1.2 (Eq. (15), Figs. 1–2; A- and "L1"-stability from plots and rank checks).
- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — Remark 2.1; §3.2 (Figs. 5–9); §5.
- [Jin et al. (2025)](/sources/jin-2025.md) — §2.1 (properties (P1)–(P3)), Remark 2.3, Prop. 3.3, Remark 3.1, Table 4.1.
