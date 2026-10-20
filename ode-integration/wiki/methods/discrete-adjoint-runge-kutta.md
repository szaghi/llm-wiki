---
type: Method
title: "Discrete adjoints of Runge–Kutta and relaxation Runge–Kutta methods"
description: "The discrete tangent and adjoint of a Runge–Kutta time stepping are the forward and backward substitutions of its global block-triangular system and its transpose; for relaxation methods the relaxation parameter must be differentiated implicitly, which adds rank-one terms, keeps the adjoint consistent and makes it exactly time-symmetric on skew-symmetric linear problems."
status: established
aliases: [discrete adjoint, tangent linear model, discrete sensitivity, discretize-then-optimize, adjoint relaxation Runge–Kutta, linearized RRK, adjoint IDT]
tags: [runge-kutta, structure-preserving, verification, relaxation, adjoint]
timestamp: 2026-10-20T16:00:00Z
---

# Discrete adjoints of Runge–Kutta and relaxation Runge–Kutta methods

In discretize-then-optimize, the gradient of a cost with respect to controls or
initial data is computed from the **discrete adjoint** of the time stepping,
the transpose of its linearization ([Bencomo & Chan (2023)](/sources/bencomo-2023.md),
§1, Eqs. (1)–(5)). For a Runge–Kutta method the adjoint is a backward
recurrence with the same stage structure as the forward step; the discrete
adjoint of an RK method is consistent and is itself an RK scheme of the same
order (as recalled in §1 from Hager, Sandu and Walther). Bencomo & Chan
derive the tangent and the adjoint of
[relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md), in both
the IDT and the time-adjusted (RRK) variants.

**Page-local notation.** Step $n$ maps $y_n$ to $y_{n+1}$ with stages
$Y_{n,i}$, $f_{n,i}=f(t_n+c_ih,Y_{n,i})$, Jacobians
$J_{n,i}=\partial f/\partial y(t_n+c_ih,Y_{n,i})$, relaxation parameter
$\gamma_n$, and $N$ steps up to $T$. Tangent variables are $\delta_n$,
$\delta_{n,i}$; adjoint variables $\mu_n$, $\mu_{n,i}$ (not $\lambda$, which is
the registry's eigenvalue); source terms $w_n$, $w_{n,i}$. $\eta''$ is the
Hessian of the entropy. Bencomo & Chan index the step that ends at $y_k$ by $k$
and write $\lambda_k$, $\Lambda_{k,i}$ for the adjoint; the formulas below are
shifted accordingly.

## The time stepping as one global system

Bencomo & Chan (2023, §2.1, Eqs. (6)–(10), appendix), following Rothauge,
collect all solutions and stages in one vector
$(y_0,Y_{0,\cdot},y_1,\dots,y_N)$ and write the whole integration as
$\mathsf E(\bar y)=0$ with a block lower-triangular, unit-diagonal linear part
and a block lower-triangular nonlinear part. The Jacobian of $\mathsf E$ solved
by forward substitution is the **tangent** recurrence

$$\delta_{n+1}=\delta_n+h\sum_ib_iJ_{n,i}\delta_{n,i}+w_{n+1},\qquad \delta_{n,i}=\delta_n+h\sum_ja_{ij}J_{n,j}\delta_{n,j}+w_{n,i};$$

its transpose solved by back substitution is the **adjoint** recurrence

$$\mu_n=\mu_{n+1}+\sum_i\mu_{n,i}+w_n,\qquad \mu_{n,i}=hJ_{n,i}^\top\Big(b_i\mu_{n+1}+\sum_ja_{ji}\mu_{n,j}\Big)+w_{n,i}.$$

The adjoint stages are multiplier variables, not Runge–Kutta stage values; the
authors do not rewrite them in Hager's Runge–Kutta form (§2.1).

## Differentiating the relaxation parameter

$\gamma_n$ is defined implicitly by the relaxation equation
$r_n(\gamma)=\eta(y_n+\gamma d_n)-\eta(y_n)-\gamma e_n=0$ and depends on $y_n$
and the stages $Y_{n,\cdot}$ only. Implicit differentiation gives
$\nabla_{y_n}\gamma_n=-(\partial r_n/\partial\gamma)^{-1}(\partial r_n/\partial y_n)^\top$
and the same for each stage (Bencomo & Chan (2023), §2.2.1, Eqs. (13)–(14)),
with, writing $y^{\gamma}_{n+1}$ for the relaxed solution,

$$\begin{aligned}
\frac{\partial r_n}{\partial\gamma}&=h\sum_ib_i\big(\eta'(y^{\gamma}_{n+1})-\eta'(Y_{n,i})\big)^\top f_{n,i},\qquad
\frac{\partial r_n}{\partial y_n}=\eta'(y^{\gamma}_{n+1})^\top-\eta'(y_n)^\top,\\
\frac{\partial r_n}{\partial Y_{n,j}}&=\gamma_nb_jh\Big[\big(\eta'(y^{\gamma}_{n+1})-\eta'(Y_{n,j})\big)^\top J_{n,j}-f_{n,j}^\top\eta''(Y_{n,j})\Big].
\end{aligned}$$

The proper linearization therefore needs, per step, $y_n$, $y_{n+1}$, the
stages, $f$ and its Jacobian, and the gradient and Hessian of $\eta$ (p. 10).

**Linearized and adjoint IDT** (Lemmas 1–2, Eqs. (15)–(17)). The stage
recurrences are those of RK; the updates become

$$\begin{aligned}
\delta_{n+1}&=\delta_n+\gamma_nh\sum_ib_iJ_{n,i}\delta_{n,i}+\rho_n\,h\sum_ib_if_{n,i}+w_{n+1},\qquad \rho_n=\nabla_{y_n}\gamma_n^\top\delta_n+\sum_i\nabla_{Y_{n,i}}\gamma_n^\top\delta_{n,i},\\
\mu_n&=\mu_{n+1}+\sum_i\mu_{n,i}+\xi_n\nabla_{y_n}\gamma_n+w_n,\qquad \xi_n=h\sum_ib_if_{n,i}^\top\mu_{n+1},\\
\mu_{n,i}&=hJ_{n,i}^\top\Big(\gamma_nb_i\mu_{n+1}+\sum_ja_{ji}\mu_{n,j}\Big)+\xi_n\nabla_{Y_{n,i}}\gamma_n+w_{n,i}.
\end{aligned}$$

The scalars $\rho_n$ and $\xi_n$ come from rank-one blocks of the Jacobian, so
the cost structure of the RK adjoint is kept. Treating $\gamma_n$ as a constant
instead gives the RK formulas with $b\mapsto\gamma_nb$, which "will have
negative consequences" (p. 8).

**Linearized and adjoint RRK** (Lemmas 3–4). The time-adjusted variant reaches
$T$ by a final IDT step of corrected length $h^*=T-t_{N-1}$ (page-local $h^*$,
Eq. (24)), which depends on every earlier $\gamma_n$. The first $N-1$ tangent
steps are IDT steps; the last uses $h^*$ and adds the stage correction
$-\rho_*h\sum_ja_{ij}f_{N-1,j}$ with $\rho_*=\sum_{n<N-1}\rho_n$, accumulated
cheaply. In the adjoint, the first reverse step is the IDT adjoint with $h^*$,
and the remaining ones replace $\xi_n$ by $\xi_n-\xi_*$, where
$\xi_*=h\sum_i\sum_ja_{ji}f_{N-1,i}^\top\mu_{N-1,j}$ comes from the first
reverse step.

## Results on skew-symmetric linear problems

For $y'=Sy$ with $S$ skew-symmetric and $\eta(y)=\tfrac12\lVert y\rVert^2$:

* **Theorems 1 and 3.** IDT and RRK commute with linearization: the
  linearized scheme started from $\delta_0=y_0$ without sources reproduces
  $\delta_n=y_n$, because $\rho_n=0$ (Eqs. (19)–(21)), for any baseline RK.
* **Theorems 2 and 4 (time symmetry).** If the baseline is explicit or
  diagonally implicit, the adjoint started from $\mu_N=y_N$ without sources
  returns $\mu_n=y_n$ for every $n$, up to round-off; all adjoint stages vanish.
  The continuous adjoint of a skew-symmetric system has the same property
  (Eqs. (22)–(23)). Whether it holds for fully implicit baselines is not
  addressed.

The authors warn that this "adjoint" (transpose of the linearized global
system) and "time symmetry" (the adjoint step reverses the forward step) are
not the adjoint method $\psi^*_h=\psi_{-h}^{-1}$ or the time-symmetric methods
of geometric integration (§2.2.2; see
[symplecticity](/properties/symplecticity.md)).

## Numerical evidence

Baselines: Heun RK2, SSPRK(3,3), classical RK4, Alexander's three-stage
third-order DIRK with $a_{ii}=0.435866521508459$ (§3.2).

* **Derivative checks** (finite differences, Eq. (28)). On the nonlinear
  pendulum ($h=0.1$, $T=200$), only the full linearization converges at $O(h)$
  for orders 2–4; the $\gamma$-constant and $h^*$-constant variants stall, the
  latter at smaller errors. On 1D compressible Euler with entropy-stable DG
  and RRK4 (CFL 1 and 1.5) the same holds, but there the $h^*$-constant error
  is the larger (Figs. 1–2).
* **Consistency and accuracy.** Against an RK4 reference adjoint with
  $h=10^{-5}$, the properly linearized RRK adjoint converges at the method's
  order and is the most accurate adjoint tested, more accurate than the plain
  RK adjoint; the $\gamma$-constant variant also reaches the optimal order;
  the $h^*$-constant variant loses one order (Fig. 4).
* **Long time.** On the pendulum to $T=200$ with RK4 at $h=0.9$ the
  $\gamma$-constant adjoint grows substantially and the plain RK4 adjoint is
  highly inaccurate, partly because its forward solution dissipates energy
  (Figs. 5–6).
* **Time symmetry.** On a random $10\times10$ skew-symmetric system to
  $T\approx133.46$, RRK gives $\lVert\mu_0-y_0\rVert/\lVert y_0\rVert\sim10^{-14}$
  for RK2, RK3, RK4 and DIRK3, while plain RK and $\gamma$-constant RRK do
  not. The error of the non-symmetric variants converges at order 5 for RK4
  and 3 for RK2, one above the method order, which the authors cannot explain
  (Fig. 7).

## Qualifications

* Bencomo & Chan state that Eberhard & Bischof (1999) and Alexe & Sandu (2009)
  found differentiation through adaptive step selection non-physical or
  inconsistent, and that for relaxation "the opposite is true" (§1, §3.4).
  Their evidence is numerical, on one ODE (Fig. 4), and their end-of-interval
  treatment is "similar to" those works.
* **Printed slips** (arXiv v1 read; compiler checks of the PDF): the appendix
  version of the RRK adjoint update has $+\xi_*$ where Lemma 4 and the
  appendix's own block matrix give $-\xi_*$; the appendix $\xi_*$ lacks a
  transpose; pp. 15–16 call "IDT" matrix systems that contain the $h^*$ terms
  of RRK; the Fig. 4(b) legend reads "RRK4 ($\gamma$-const)" in the RK3 panel;
  Theorem 3 omits the hypothesis $\eta=\tfrac12\lVert y\rVert^2$ stated in
  Theorem 1.

# Citations

- [Bencomo & Chan (2023)](/sources/bencomo-2023.md) — §1 (Eqs. (1)–(5)), §2.1 (Eqs. (6)–(10)), §2.2 (Eqs. (11)–(12)), §2.2.1 (Eqs. (13)–(17), Lemmas 1–2), §2.2.2 (Theorems 1–2, Eqs. (19)–(23)), §2.2.3 (Eq. (24), Lemmas 3–4, Theorems 3–4), §3 (Eq. (28), Figs. 1–7), appendix.
