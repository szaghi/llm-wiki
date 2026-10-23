---
type: Definition
title: "Runge–Kutta method"
description: "The s-stage one-step method defined by a Butcher tableau (A, b, c): its stage-value and stage-derivative forms, the row-sum convention, the explicit, diagonally implicit and fully implicit classes and their solve costs, reducibility, and the additive, multiderivative and mass-matrix generalizations used by the sources."
status: established
aliases: [RK method, Butcher tableau, implicit Runge–Kutta, IRK, explicit Runge–Kutta, ERK]
tags: [runge-kutta, explicit, implicit, order-conditions]
timestamp: 2026-10-20T06:18:00Z
---

# Runge–Kutta method

An $s$-stage **Runge–Kutta (RK) method** for $y'=f(t,y)$ advances $y_n$ to
$y_{n+1}\approx y(t_n+h)$ through $s$ stage values $Y_i$:

$$\begin{aligned}
Y_i&=y_n+h\sum_{j=1}^{s}a_{ij}\,f(t_n+c_jh,Y_j),\qquad i=1,\dots,s,\\
y_{n+1}&=y_n+h\sum_{i=1}^{s}b_i\,f(t_n+c_ih,Y_i).
\end{aligned}$$

The method is the **Butcher tableau** $(A,b,c)$, $A=(a_{ij})\in\mathbb R^{s\times s}$,
$b,c\in\mathbb R^s$, written $c\,|\,A$ over $b^\top$. All sources state it in
this form ([Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md), Eqs. (7)–(8);
[Biswas et al. (2023)](/sources/biswas-2023.md), Eqs. (2)–(3);
[Biswas et al. (2024)](/sources/biswas-2024.md), Eq. (1);
[Fekete et al. (2022)](/sources/fekete-2022.md), Eqs. (2)–(4);
[Reynolds et al. (2023)](/sources/reynolds-2023.md), Eq. (4)).

## Row-sum convention

The sources that develop RK theory assume $c=A\mathbf 1$, i.e.
$c_i=\sum_ja_{ij}$. Ketcheson & Ranocha (2023, §2.1) adopt it because it makes
the autonomous and non-autonomous forms of the method equivalent, so the
theory can be written for $y'=f(y)$; Biswas et al. (2023, Eq. (4)),
Biswas et al. (2024, §1.1) and [Biswas et al. (2025)](/sources/biswas-2025.md)
(§1.3, "stage consistency") assume it throughout, and then the method is
specified by $(A,b)$ alone. Under it the first stage-order residual
$\tau^{(1)}=A\mathbf 1-c$ vanishes (see [stage order](/definitions/stage-order.md)).
Fekete et al. (2022, §1) also assume it, and so do
[Zhang (2024)](/sources/zhang-2024.md) ("without loss of generality", §2) and
[Bazavov (2026)](/sources/bazavov-2026.md) (Eq. (6)). An explicit method then has
$s(s-1)/2+s=s(s+1)/2$ free coefficients, 136 for $s=16$ (Zhang 2024, §2). Reynolds et al. (2023) and
[Farrell et al. (2021)](/sources/farrell-2021.md) do not state it; additive
methods may deliberately have different abscissae per partition (Reynolds et
al. (2023), §2.2: $c^{\mathrm E}\neq c^{\mathrm I}$ is allowed, as needed by
SSP IMEX methods).

## Stage-value and stage-derivative forms

The registry form above uses stage values $Y_i$. An equivalent form uses stage
derivatives $k_i=f(t_n+c_ih,Y_i)$, with $Y_i=y_n+h\sum_ja_{ij}k_j$ and
$y_{n+1}=y_n+h\sum_ib_ik_i$. Farrell et al. (2021, Eqs. (3)–(4)) write the
problem in residual form $y'+F(t,y)=0$ (so $F=-f$) and solve for the $k_i$,
because $k_i$ approximates $u_t$ at $t_n+c_ih$ and Dirichlet data then enter
the stages as $\partial_tg(t_n+c_ih)$ (their Eq. (18)).
[Southworth et al. (2022)](/sources/southworth-2022.md) (Eqs. (1)–(4)) also use
stage derivatives, for $My'=\mathcal N(y,t)$. The two forms differ only in
which unknowns the nonlinear solver iterates on.
[Kirby & MacLachlan (2025)](/sources/kirby-2025.md) (§2.2, Eqs. (2.18)–(2.21)) offer both
in Irksome, together with Butcher's transformed unknowns $(A\otimes I)\mathbf k$
($\mathbf k$ the stacked stage derivatives, page-local), which move the stage coupling outside
the nonlinearity so that its Jacobian contribution is block diagonal; the stage-value form
skips the final mass-matrix solve for stiffly accurate tableaux. Irksome now imposes
Dirichlet data on the stage values by default instead of Farrell et al.'s derivative form
(§2.1; see [boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md)).

For explicit methods Bazavov (2026, §3, Eqs. (23)–(29)) adds a third, bijective form in
which each stage is an increment of the previous one,
$Y_i=Y_{i-1}+h\sum_{j<i}(a_{ij}-a_{i-1,j})f(t_n+c_jh,Y_j)$, with the weights treated as an
extra row $a_{s+1,j}=b_j$, $c_{s+1}=1$. It resembles the Shu–Osher form but is not a
convex-combination form (Remark 1), and it exposes the structure of
[2N-storage methods](/methods/low-storage-runge-kutta.md).

## Classes by the structure of $A$

| Class | Structure of $A$ | Stage solves per step |
|---|---|---|
| explicit (ERK) | strictly lower triangular | none; one mass-matrix solve per stage if $M\neq I$ |
| diagonally implicit (DIRK) | lower triangular | $s$ sequential $d\times d$ systems |
| singly diagonally implicit (SDIRK) | DIRK with all $a_{ii}=\gamma$ | $s$ systems with one matrix |
| EDIRK | DIRK with $a_{11}=0$ | $s-1$ systems |
| fully implicit (FIRK) | dense | one coupled $(sd)\times(sd)$ system |

The classification and the cost column follow Farrell et al. (2021, §2.1, §2.3,
Eqs. (31)–(34)) and Biswas et al. (2024, §2.1). Farrell et al. (2021, Eq. (31))
show that, for the heat equation discretized with finite elements, the coupled
system is a Kronecker sum, $I_s\otimes M$ plus $hA$ tensored with the stiffness
matrix, and that for lower-triangular $A$ it is block lower triangular, so a
multiplicative block preconditioner solves a DIRK exactly in one sweep (§4.3).
Biswas et al. (2024, Def. 2.1) add the **GEDIRK** class: a DIRK whose abscissae
contain a zero, with $a_{jj}=0$ at the first such stage $j$; explicit
methods are GEDIRKs. How the coupled systems are solved is on
[solving the stage equations](/methods/implicit-stage-solvers.md); the DIRK
and fully implicit families have their own pages
([DIRK](/methods/diagonally-implicit-runge-kutta.md),
[fully implicit collocation methods](/methods/fully-implicit-runge-kutta.md)).

The choice of class trades cost against properties. DIRKs have
[stage order](/definitions/stage-order.md) at most 2, which drives
[order reduction](/definitions/order-reduction.md) on stiff problems
(Biswas et al. (2023), Thm. 2.2); fully implicit collocation methods reach
$p=2s$ and $q=s$ (Southworth et al. (2022), §2.1). Farrell et al. (2021, §1)
and Southworth et al. (2022, §1) both argue that the cost objection to fully
implicit methods is answered by preconditioning that reduces each step to a
few backward-Euler-type solves.

## Order, stability and their pages

The method has **order** $p$ when $y_{n+1}-y(t_n+h)=O(h^{p+1})$ for smooth
problems. Expanding the numerical solution as a
[B-series](/definitions/b-series.md) with coefficients the elementary weights
$\Phi(\tau)$ gives the [order conditions](/results/runge-kutta-order-conditions.md)
$\Phi(\tau)=1/\gamma(\tau)$ (Ketcheson & Ranocha (2023), §2.2). Applying the
method to $y'=\lambda y$ gives the
[stability function](/definitions/stability-function.md) $R(z)$, on which
[A-, L- and A($\alpha$)-stability](/properties/a-stability.md) are defined.
The structural properties of a tableau used across the bundle are
[stage order](/definitions/stage-order.md),
[weak stage order](/definitions/weak-stage-order.md),
[stiff accuracy](/properties/stiff-accuracy.md) ($a_{sj}=b_j$),
[symplecticity](/properties/symplecticity.md) and the SSP coefficient of
[strong-stability-preserving methods](/methods/strong-stability-preserving-runge-kutta.md).
A second weight vector $\hat b$ sharing $A$ defines an
[embedded pair](/methods/embedded-runge-kutta-pair.md) for error estimation
(Fekete et al. (2022), §2; Reynolds et al. (2023), §2.1).

## Reducibility

A tableau can describe a method that is equivalent to one with fewer stages.
Biswas et al. (2024, Def. 6.3) recall **S-reducibility** after Hairer–Wanner:
a partition of the stage indices into fewer than $s$ classes such that the rows
of $A$ summed over each class agree within a class. Two consequences are used
in method design:

* An $r$-confluent DIRK ($c_1=\dots=c_r$, $2\le r\le s$) satisfies the
  weak-stage-order equations but is S-reducible to a smaller scheme
  (Biswas et al. (2023), Lemma 4.4); in particular any DIRK with $c_1=c_2$ is
  S-reducible (Biswas et al. (2024), Remark 6.4). Constructions therefore avoid
  confluent leading abscissae.
* A DJ-irreducible DIRK has $b_s\neq0$ (Biswas et al. (2024), Remark 6.6).

Biswas et al. (2024, §3.1) observe that almost every irreducible scheme in the
literature that was not designed for weak stage order has $\mathcal Y=\mathbb R^s$,
where $\mathcal Y$ is the smallest $A^\top$-invariant subspace containing $b$; the exceptions include
explicit methods with a zero first-subdiagonal entry, such as the 8th-order
Prince–Dormand method.

## Generalizations

* **Mass-matrix problems.** ARKODE treats $M(t)y'=f(t,y)$ with nonsingular,
  $y$-independent $M$ by applying the tableau to $y'=M^{-1}f$
  (Reynolds et al. (2023), Eqs. (1), (5)–(6)). Farrell et al. (2021, Eq. (9))
  go further and transform a general semidiscrete variational form
  $G(t,u,u_t;v)=0$ stage by stage, which covers Sobolev equations and DAEs;
  see [differential-algebraic equations](/definitions/differential-algebraic-equation.md).
* **Additive and partitioned methods.** Each part $f^{[\nu]}$ of a split
  right-hand side gets its own tableau; partitioned RK methods are a subset of
  additive RK methods (Ketcheson & Ranocha (2023), §3.1). See
  [IMEX and additive RK](/methods/imex-runge-kutta.md) and
  [GARK](/methods/generalized-additive-runge-kutta.md).
* **Multiderivative methods.** [Gottlieb et al. (2022)](/sources/gottlieb-2022.md)
  (Eqs. (8)–(9)) add a second tableau $(\dot a_{ij})$ multiplying
  $h^2\dot f(Y_j)$, $\dot f=f'f$, with weights the last rows (stiffly accurate
  by construction); see [multiderivative RK](/methods/multiderivative-runge-kutta.md).
  The same paper uses an implicit **Shu–Osher form** in which the stage matrix
  is recovered as $A=R^{-1}D$ from convex-combination coefficients (§2.2).
* **Linearly implicit methods.** Rosenbrock–Wanner methods replace the
  nonlinear stage solves by linear ones with the Jacobian in the stage
  equations; see [ROW methods](/methods/rosenbrock-wanner-method.md).

## Qualifications

* Notation differs by source: Biswas et al. (2023, 2024, 2025) write
  $\Delta t$, stage values $g_i$ and $\vec e$ for $\mathbf 1$; Farrell et al.
  (2021) write $\Delta t$, $A_{ij}$ or $a_{ij}$ and stage derivatives, with
  $h$ reserved for the mesh size; Fekete et al. (2022) write $\Delta t$ and
  $Y_i$; Reynolds et al. (2023) write $h_n$ and stage values $z_i$. Each
  Source page maps these to the registry.
* Abscissae need not lie in $[0,1]$. The weak-stage-order DIRKs of Biswas et
  al. (2023, App. A) impose only $c_j\ge0$ and have $c_j$ up to about 4.17,
  while the explicit methods of Biswas et al. (2025, Eq. (3.3)) impose
  $0\le c_i\le1$. The sources do not discuss whether $c_j>1$ affects the
  evaluation of time-dependent forcing or boundary data.
* Farrell et al. (2021) print the stage index range as $1\le i\le n$ in their
  Eq. (4), and their Eq. (15) omits the factor $\Delta t$ in the update; their
  Eq. (3) has the correct form.
* Zhang (2024) writes $\tau$ for the one-vertex tree, not a generic tree, and
  Bazavov (2026) writes $A_i$, $B_i$ for scalar 2N-storage coefficients and $\alpha_{ij}$ for
  the increment form above, which clash with the registry's Butcher matrix and Shu–Osher
  coefficients; their Source pages translate them.

# Citations

- [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md) — §2.1, Eqs. (6)–(8) (tableau, row-sum convention); §2.2 (order via B-series); §3.1 (additive and partitioned RK).
- [Biswas et al. (2023)](/sources/biswas-2023.md) — Eqs. (1)–(4); Thm. 2.2 (DIRK stage order); Lemma 4.4 ($r$-confluent DIRKs are S-reducible); App. A (abscissae outside $[0,1]$).
- [Biswas et al. (2024)](/sources/biswas-2024.md) — Eq. (1), §1.1, §2.1 (classes), Def. 2.1 (GEDIRK), §3.1, Def. 6.3, Remarks 6.4 and 6.6 (reducibility).
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1.3 (stage consistency), Eq. (3.3) (abscissae in $[0,1]$).
- [Farrell et al. (2021)](/sources/farrell-2021.md) — Eqs. (1)–(9), (18), (31)–(34); §2.3, §4.3 (stage-derivative form, solve structure).
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — Eqs. (8)–(11) (two-derivative RK, implicit Shu–Osher form).
- [Fekete et al. (2022)](/sources/fekete-2022.md) — Eqs. (2)–(4) (explicit RK and embedded pair).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — Eqs. (1), (4)–(7) (ERK, ARK, mass matrix).
- [Southworth et al. (2022)](/sources/southworth-2022.md) — Eqs. (1)–(4), §2.1 (stage-derivative form; DIRK versus fully implicit orders).
- [Zhang (2024)](/sources/zhang-2024.md) — §2 (row-sum convention, parameter count).
- [Bazavov (2026)](/sources/bazavov-2026.md) — Eq. (6); §3 (Eqs. (23)–(29), Remark 1).
- [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) — §2.1 (stage-value boundary data), §2.2 (Eqs. (2.18)–(2.21), stage formulations).
