---
type: Method
title: "Mixed-precision explicit Runge–Kutta methods"
description: "Mixed-precision explicit Runge–Kutta methods evaluate most right-hand sides in low precision and only one or two per step in high precision; written in delta form with low-precision Jacobian actions, Runge–Kutta–Chebyshev methods keep their first or second order instead of stagnating at the low-precision roundoff."
status: established
aliases: [order-preserving mixed precision, q-order-preserving scheme, mixed-precision RKC, mixed-precision Runge–Kutta–Chebyshev, low-precision time integration, bfloat16 time stepping]
tags: [explicit, runge-kutta, stabilized, stability, stiff, round-off, mixed-precision]
timestamp: 2026-10-20T16:00:00Z
---

# Mixed-precision explicit Runge–Kutta methods

A **mixed-precision** Runge–Kutta method performs part of its arithmetic in a
low-precision format (bfloat16, fp16 or fp32, with unit roundoff $u$, page-local) and
the rest in fp64. The aim is to keep the convergence order of the method while most
of the work is done cheaply. [Croci & Rosilho de Souza (2022)](/sources/croci-2022.md)
build such methods from
[stabilized explicit Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md):
a Runge–Kutta–Chebyshev (RKC) step of order $p\le2$ uses $s\gg p$ stages, and all but
one or two of its right-hand-side evaluations only buy stability, so they can be
computed in low precision. The authors present these as, to their knowledge, the
first explicit mixed-precision methods that preserve order (§3).

## Why naïve reduced precision fails

For a linear problem $y'=Ly$ and a method of order $p$, the heuristic analysis of
Croci & Rosilho de Souza (§3.1, Eqs. (15)–(17)) gives:

| Implementation | Global error |
|---|---|
| all operations in precision $u$ | $\mathcal O(uh^{-1}+h^p)$: diverges as $h\to0$ |
| "standard" mixed precision: products with $L$ in low precision, vector operations in high | $\mathcal O(u+h^p)$: stagnates at a level proportional to $u$ |
| first $\tilde q$ products with $L$ in high precision | $\mathcal O(uh^{\tilde q}+h^p)$ |

(page-local: $\tilde q$ the preserved order, not the stage order $q$; the source writes $q$). The last line converges at rate $p$
until $h\propto u^{1/(p-\tilde q)}$ and at rate $\tilde q$ below. The table assumes that
high-precision operations are exact (Assumption 3.1).

**Definition 3.1.** A mixed-precision implementation of a method of order $p$ is
**$\tilde q$-order-preserving**, $1\le\tilde q\le p$, if it converges with order $\tilde q$
when the high-precision operations are taken as exact; an implementation that
stagnates or diverges as $h\to0$ is not order-preserving.

**Terminology.** Croci & Rosilho de Souza call this precision-induced loss of order
"an order-reduction phenomenon or even stagnation" (§3). It is not the stiff
[order reduction](/definitions/order-reduction.md) of this bundle, which comes from
stiffness, boundary data or low stage order in exact arithmetic; the
precision-induced loss occurs for non-stiff problems and disappears in exact
arithmetic.

## Order-preserving constructions

**Linear problems** (§3.1, Eqs. (14), (18)). Write the stability polynomial as the
Taylor part up to degree $p$ plus a correction of higher degree. The mixed-precision
step computes the exact Taylor part up to degree $\tilde q$ in high precision and the
stabilizing correction of degree $\tilde q+1,\dots,s$ in low precision, with low-precision
products $\hat L_k$ (page-local) applied to $L^{\tilde q}y_n$.

**Nonlinear problems: RKC in delta form** (§3.2, Eqs. (20)–(25)). In the RKC
recurrence (see [stabilized explicit Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md))
each evaluation $f(y_n+d_j)$ is replaced by $f(y_n)+\widehat{\Delta f}_j$, where
$f(y_n)$ is computed once per step in high precision and $\widehat{\Delta f}_j$ is a
low-precision approximation of $\Delta f_j=f(y_n+d_j)-f(y_n)$. Theorem 3.3 (Eqs.
(57)–(58)) gives:

- if $\widehat{\Delta f}_j=\Delta f_j+\mathcal O(\epsilon h)$ for a small constant
  $\epsilon$ (page-local), the scheme with RKC1 or RKC2 coefficients satisfies
  $y_{n+1}=y_n+hf(y_n)+\mathcal O(\epsilon h^2+h^2)$: it is 1-order-preserving, with
  one high-precision and $s-1$ low-precision evaluations per step;
- if $\widehat{\Delta f}_j=\Delta f_j+\mathcal O(h^2)$, the scheme with RKC2
  coefficients reproduces $y_n+hf+\frac12h^2f'f+\mathcal O(h^3)$: it is
  2-order-preserving.

The second condition amplifies rounding errors by a factor $\mathcal O(s^2)$ more
than the first when $h$ is far from the convergence regime (Remark 3.7, Eqs.
(29)–(30), (82)–(83)). The **hybrid scheme** (Eq. (25)) therefore uses the
second-order approximation only when the increment is close to its first-order
prediction, $\lVert d_j-c_jhf(y_n)\rVert_2\le\lVert d_j\rVert_2$, and the first-order
one otherwise; it costs two high-precision evaluations per step. Running only the
first stage in high precision and all later evaluations of $f$ in low precision
stagnates, because every $f(y_n+d_j)$ enters the $\mathcal O(h)$ term (Remark 3.3).
The authors could not construct recurrence-based methods that preserve more than
order two (Remark 3.2).

**Computing $\widehat{\Delta f}_j$** (§3.3, Eqs. (26)–(39)), for $f(y)=Ly+g(y)$ with
$g$ the nonlinear part (page-local):

- *cheap nonlinearity:* $\widehat{\Delta f}_j=\hat Ld_j+g(y_n+d_j)-g(y_n)$, error
  $\mathcal O(uh)$;
- *expensive nonlinearity:* a low-precision Jacobian action, analytic, by automatic
  differentiation, or by the finite difference
  $\widehat{\Delta f}_j=\hat Ld_j+\delta^{-1}\bigl(g(y_n+\delta d_j)-g(y_n)\bigr)$
  with $\delta=\sqrt u/h$ (page-local), error $\mathcal O(\sqrt uh+h^2)$, i.e. the
  first-order condition with $\epsilon=\sqrt u$ (Eq. (33), Lemma A.1).

The construction mirrors the linearized RKC of Verwer, $f(y_n+d_j)\approx f(y_n)+J_nd_j$;
approximating the Jacobian action is "crucial to maintain stability" (§3.2).

**Multirate RKC** (§4.2, Eqs. (98)–(103), Thm. 4.3). The same replacement in the outer
and inner recurrences of the [multirate RKC](/methods/multirate-runge-kutta-chebyshev.md) of
Abdulle, Grote & Rosilho de Souza gives
a 1-order-preserving mixed-precision multirate method with one high-precision
evaluation of the fast and of the slow part per step.

## Cost

With $\chi$ the cost ratio of a high-precision to a low-precision evaluation
(page-local), a $\tilde q$-order-preserving $s$-stage method saves the fraction

$$\varrho=\frac{(s-\tilde q)(\chi-1)}{s\chi}$$

of the work (§3.4, Eq. (40)), approaching $1-1/\chi$ for many stages. Examples (§3.1):
classical RK4 with $\tilde q=2$ in fp64/fp16 saves 37.5% for sparse operators
($\chi=4$) and about 47% for dense ones ($\chi=16$), keeping order 4 down to
$h\propto u^{1/2}\approx0.022$; a 64-stage RKC2 with $\tilde q=1$ saves about 74% (sparse) and 92%
(dense). A $\tilde q$-order-preserving scheme stores $\tilde q$ extra vectors.

## Stability

For mixed-precision RKC with a symmetric nonpositive definite Jacobian, Croci &
Rosilho de Souza prove one-step error recursions whose constants depend neither on $s$
nor on the stiffness, under an assumption on the size of the computed increments
(Thms. 3.4–3.5); a worst-case bound for the rounding errors guarantees boundedness only
for $s^2u=\mathcal O(1)$ (Thm. 3.6). A rigorous stability proof is stated to be out of
reach (§3.6). The analysis is on [internal stability](/definitions/internal-stability.md).

## Numerical evidence

Low precision is emulated in software (libchopping); P1 finite elements with mass
lumping (FEniCS) discretize nonlinear reaction–diffusion in 1D–3D, a heat equation on
a graded L-shaped domain (for the multirate method), the 1D
[Brusselator](/benchmarks/brusselator.md) and a 4-Laplace diffusion problem (§5):

- standard and order-preserving mixed-precision RKC1 and RKC2 in bfloat16/fp64 are
  stable on the 2D heat equation up to $s=512$, "as stable as the high-precision
  implementation" (§5.2.1, Fig. 1);
- on linear 3D heat, computing $\tilde q$ products in high precision recovers order
  $\tilde q$ for RK4, $\tilde q=0,\dots,3$; with $\tilde q=1$ the error drops by up to four
  orders of magnitude against the non-preserving method (§5.2.2, Fig. 2);
- on the nonlinear problems the order-preserving RKC1, RKC2 and multirate RKC1
  recover their full order, while standard mixed precision stagnates at about $10u$
  (reaction–diffusion and the L-shaped heat problem), $100u$ (Brusselator, less than one
  correct digit) and $0.1u$ (4-Laplace diffusion); order-preserving
  methods are 2–8 orders of magnitude more accurate (§5.2.2, Figs. 3–6);
- the rounding error of the order-preserving schemes stays at or below the time
  discretization error for all stage counts tested (§5.2.3, Figs. 7–9).

No run times are reported. An operation count (Remark 5.3) compares, for 3D
reaction–diffusion with $s=33$, implicit Euler with Newton and multigrid-preconditioned
CG, about 54 high-precision product equivalents per step (see
[implicit stage solvers](/methods/implicit-stage-solvers.md)), with one high-precision
and 32 half-precision products for order-preserving RKC1.

## Relation to other mixed-precision schemes

Earlier mixed-precision Runge–Kutta methods are implicit: Grant and Burnett et al.
solve the implicit stages in reduced precision and recover the order with additional
high-precision explicit stages, analysed as additive Runge–Kutta methods by B-series,
without a general stability analysis; Hairer et al. store implicit coefficients in
quadruple precision for long Hamiltonian integrations; all as recalled by Croci &
Rosilho de Souza (§1). The extension to ROCK2/ROCK4, to stochastic SK-ROCK and to
incompressible Navier–Stokes as an index-2 DAE via projection RKC is stated, not
carried out (Remarks 3.4–3.6, Example 3.1).

## Qualifications

- **Cost claims are models.** The abstract's "essentially as cheap as their fully
  low-precision equivalent" rests on flop counts with emulated arithmetic; no
  measured timings exist (§5.1.5).
- **Theory versus experiment.** The stability guarantee covers $s\lesssim16$ in
  bfloat16 ($u\approx3.9\times10^{-3}$), while experiments run stably to $s=512$.
- **Priority.** The claim to be the first explicit order-preserving mixed-precision
  methods is the authors'; the perturbed-Runge–Kutta framework of Grant, which also
  covers explicit perturbations, is not compared in detail.
- **Printed slips** (arXiv v2): the text writes the damping symbol where the accuracy
  constant $\epsilon$ is meant ("$\varepsilon=u$", §3.3); the proof of Thm. 3.5 refers
  to Thm. 4.3 instead of Thm. 3.4; Remark 5.3 names Problem 3 where Problem 1 is meant;
  Figs. 10–11 captions say "vs $\Delta t$" for axes in $\Delta x$.

# Citations

- [Croci & Rosilho de Souza (2022)](/sources/croci-2022.md) — §1, §2.1–2.2, §3 (Def. 3.1, Remarks 3.1–3.7), §3.1 (Eqs. 14–19), §3.2 (Eqs. 20–25, Thm. 3.3), §3.3 (Eqs. 26–39, Lemma A.1), §3.4 (Eq. 40), §3.5–3.6 (Thms. 3.4–3.6), §4.2 (Thm. 4.3), §5 (Figs. 1–11, Remark 5.3).
