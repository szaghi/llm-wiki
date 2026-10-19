---
type: Method
title: "Explicit–implicit–null (EIN) time marching"
description: "The explicit–implicit–null method adds and subtracts a linear constant-coefficient surrogate of the stiffest term, treats the added copy implicitly and everything else explicitly, so stiff nonlinear diffusion or dispersion needs only constant-coefficient linear solves; stability needs the surrogate above a scheme-dependent fraction, about 0.54 for ARS(4,4,3)."
status: established
aliases: [EIN, explicit-implicit-null, EIN-FD, EIN-LDG, add-and-subtract stabilization, explicit–implicit–null IMEX]
tags: [imex, stiff, stability, linear-algebra, exponential]
timestamp: 2026-10-20T05:00:00Z
---

# Explicit–implicit–null (EIN) time marching

For $y'=f(y)$ whose stiffest part is nonlinear, the explicit–implicit–null method
chooses a **linear** operator $g$ (page-local) with "the same scaling in wave number as
the most stiff term", and writes

$$y'=\underbrace{f(y)-g\,y}_{f^{\mathrm E}}+\underbrace{g\,y}_{f^{\mathrm I}},$$

then applies an [IMEX Runge–Kutta pair](/methods/imex-runge-kutta.md) with $g\,y$ implicit
and the rest, including the subtracted copy and every nonlinear term, explicit
([Tan et al. (2022)](/sources/tan-2022.md), §1, Eq. (1.4);
[Tan et al. (2025)](/sources/tan-2025.md), §1). The added and subtracted terms cancel
exactly ("null"), so the scheme is consistent for any $g$. If $g$ has constant
coefficients, every implicit stage is a linear constant-coefficient solve, cheap for
Fourier, multigrid or direct methods, and no Newton iteration is needed even when the
physical stiff term is nonlinear; the explicit stiff restriction $h=O(\Delta x^r)$ for an
$r$-th derivative disappears (Tan et al. 2022, §1). The price is a stability condition on
the size of $g$, and an error that grows with it.

The name is due to Duchemin & Eggers (2014), and the idea goes back to Douglas & Dupont
(1971). Earlier uses, all at low order, include level-set curvature motion, epitaxial
growth, Boltzmann equations with stiff sources and Cahn–Hilliard equations; at low order
EIN coincides with the "stabilization approach", but at high order the stabilizing term
it introduces is "much more complex" (Tan et al. 2022, §1, as recalled). Wang, Zhang,
Wang & Shu (2020) used EIN pairs up to order three with local DG for diffusion, with
stability analysis for orders one and two only (as recalled by Tan et al. 2022, §1).
[Buvoli & Southworth (2025)](/sources/buvoli-2025.md) (§2.3) list EIN among the
add-and-subtract IMEX approaches to nonlinear stiff terms and note that the added operator
may itself be nonlinear.

**Page-local notation.** $\vartheta$ is the **stabilization ratio**, the size of the
implicit surrogate relative to the largest coefficient of the stiff term it replaces
(Tan et al.'s $a_0$, with surrogate coefficient $a_1=a_0\max(\cdot)$; Caliari et al.'s
$\lambda$). $c_{\max}$ is that largest coefficient.

## Choice of the surrogate

* **Scalar higher-order PDEs** (Tan et al. 2022, §2): for nonlinear diffusion
  $u_t=(a(u)u_x)_x$ the surrogate is $\vartheta c_{\max}u_{xx}$ with
  $c_{\max}=\max a$; for third-order dispersive equations
  $\pm\vartheta c_{\max}u_{xxx}$, with the sign set by the wind direction, which must be
  fixed (§2.2); for fourth-order biharmonic-type equations
  $\vartheta c_{\max}u_{xxxx}$ (Eqs. (2.9), (2.12), (2.14)). In the nonlinear tests the
  coefficient is recomputed from $u_n$ at every step.
* **Compressible Navier–Stokes** (Tan et al. 2025, §3.4, Eq. (3.2)): a constant-coefficient
  Laplacian in computational coordinates, added to all four equations including
  continuity, with coefficient $\vartheta\lambda_\mu^{\max}$, where $\lambda_\mu^{\max}$
  (page-local) is the spectral radius of the viscous-flux Jacobian (Prop. 2.1). All
  physical viscous terms, with Sutherland viscosity and general equations of state, stay
  explicit. Leaving the continuity equation unstabilized is "far less stable" (Remark
  3.2, stated without data).
* **Exponential analogue** ([Caliari et al. (2024)](/sources/caliari-2024.md), §3,
  Eq. (11)): for advection–diffusion–reaction with variable coefficients the linear part
  of an [exponential integrator](/methods/exponential-integrators.md) is the
  constant-coefficient operator $\vartheta\sum_\mu c^{\max}_{\mu}\partial_{x_\mu}^2+\bar w\cdot\nabla$
  (page-local: $c^{\max}_\mu$ the maximal diagonal diffusion entries, $\bar w$ the mean
  effective velocity, which must include the advection hidden in the variable diffusion),
  and all the rest goes into the explicitly treated remainder. Its matrix functions are
  then pointwise in Fourier space, or Kronecker-structured for finite differences. The
  authors call this the exponential analogue of the EIN approach of Wang et al. (§1, §3).
  See also [Lawson methods](/methods/lawson-methods.md).

## Stability: a threshold on the ratio

On a Fourier mode the scheme sees the split scalar problem
$y'=(1-\vartheta)\lambda y+\vartheta\lambda y$, with the first part explicit and the second
implicit, for $\lambda$ on the spectral ray of the stiff operator: negative real for
diffusion and biharmonic terms, imaginary for dispersion. Unconditional stability means
stability for every step on that ray *(compiler's formulation of the Fourier analyses;
Tan et al. (2022, Remark 3.4) point the same way)*. Too small a $\vartheta$ leaves an
explicit anti-diffusion that is unstable at large $h\lambda$.

| Scheme | Threshold on $\vartheta$ | Basis | Source |
|---|---|---|---|
| ARS(4,4,3), diffusion, dispersion and biharmonic models; fourth-order finite differences and $P^2$ local DG | $\ge0.54$ | sampled von Neumann search | Tan et al. 2022, Props. 3.1–3.2 |
| ARS(4,4,3), linearized 2D compressible Navier–Stokes about a fluid at rest, ideal and van der Waals gas | $\ge0.54$, plus convective Courant number $\le1.2$ | sampled eigenvalue search | Tan et al. 2025, Prop. 3.1 |
| IMEX backward–forward Euler; second-order IMEX of Wang et al. | $\ge\frac12$ | quoted | Caliari et al. 2024, Remark 2.1 |
| exponential Euler; second-order exponential RK with $\phi_2$, $c_2=1$ | $\ge\frac12$ | proved | Caliari et al. 2024, Thms. 2.1, 2.4 |
| second-order exponential RK with $\phi_1$ only, $c_2=1$ | $\ge\frac13$ | proved | Thm. 2.5 |
| Lawson2a, Lawson2b | $\ge0.301$ | proved, bound computed numerically | Thm. 2.6 |
| Lawson–Euler | $\ge0.218$ | proved, bound computed numerically | Thm. 2.2 |
| stabilized Lawson–Euler, stabilized Lawson2 ($\alpha=0.327$) | $\ge1/(2e)\approx0.184$, $\ge0.183$ | proved, bound computed numerically | Thms. 2.3, 2.7 |

The exponential and Lawson thresholds come from closed-form stability functions on the
heat equation (see [stability function](/definitions/stability-function.md)); Caliari et
al. conclude that exponential and especially Lawson schemes tolerate a smaller implicit
fraction than "similarly constructed" IMEX schemes (abstract, §2).

**The ARS(4,4,3) threshold is numerical.** Tan et al. (2022, §3) compute the
amplification factor (finite differences) or the $3\times3$ amplification matrix (DG)
and test $\lvert G\rvert\le1+10^{-10}$ (page-local $G$) on sampled wave numbers for
$h/\Delta x^r=10^{-10},10^{-9},\dots,10^{10}$; the smallest admissible ratio is $0.54$,
"somewhat surprisingly" the same for $r=2,3,4$ and for both discretizations, resolved to
two decimals (Props. 3.1–3.2). They state, without details, that the threshold also holds
for other spatial orders and in 2D and 3D, and that it depends on the IMEX pair but seems
insensitive to the spatial discretization (Remarks 3.1, 3.3, 3.4). Tan et al. (2025, §3.5)
note that the scalar result does not transfer to the Navier–Stokes system, because the
inviscid and viscous Jacobians are not simultaneously diagonalizable, and repeat the
search for the linearized system with tolerance $1+10^{-5}$: pure convection is stable for
Courant numbers up to 1.2, pure diffusion is unconditionally stable for $\vartheta\ge0.54$
"regardless of the values of $\mu$ and $Pr$", and the combined maximal Courant number
depends on both parameters and is not monotone in $\vartheta$ (Fig. 3.1). *Both thresholds
are hypothesis-grade:* they come from sampled searches, not proofs, and the system result
covers only perturbations of a fluid at rest; flows far from rest may need a larger
surrogate or a smaller step (Remark 3.1).

**Link to coupled-stiff-limit stability** *(compiler computation, not in the sources)*.
In the two-variable notation of [stability function](/definitions/stability-function.md),
with the implicit argument first, the EIN test asks
$\lvert R(\vartheta z,(1-\vartheta)z)\rvert\le1$ along the ray. Its stiff end is the
coupled stiff limit of Buvoli & Southworth (2025, Eqs. (4.24)–(4.26)) at the real ratio
$\kappa=(1-\vartheta)/\vartheta$ (page-local), and $\lvert\kappa\rvert\le1$ exactly when
$\vartheta\ge\frac12$. A pair stable in the coupled stiff limit therefore has a bounded
stiff end for every $\vartheta\ge\frac12$; IMEX backward–forward Euler, with limit
$-\kappa$, has exactly the threshold $\frac12$ quoted by Caliari et al. ARS(4,4,3) is not
such a pair. From the tableau on [IMEX Runge–Kutta](/methods/imex-runge-kutta.md),
$\lim_{\lvert z_1\rvert\to\infty}R(z_1,\kappa z_1)=\tfrac{29}{18}\kappa-\tfrac16\kappa^2-\tfrac{19}6\kappa^3-\tfrac7{18}\kappa^4$,
which is $-\tfrac{19}9$ at $\kappa=1$ and has modulus at most 1 on the EIN range only for
$\kappa\le0.8652$, i.e. $\vartheta\ge0.5361$. Sampling the diffusive and dispersive rays
up to $\lvert z\rvert=10^{12}$ gives $\max\lvert R\rvert\le1$ for $\vartheta=0.54$ and the
maximum at the stiff end for $\vartheta\le0.53$. The 0.54 of Tan et al. is thus the
stiff-limit threshold $0.536$ resolved to two decimals, which fits the instability at 0.53
appearing only where $h/\Delta x^r$ is large.

## Accuracy: the ratio should be small but not necessarily minimal

The two equal added terms are treated differently, one implicitly and one explicitly, so a
larger surrogate means a larger splitting error (Tan et al. 2022, §3). On linear diffusion
with finite differences at 1280 cells the $L^1$ error is $3.16\times10^{-10}$ (order 2.96)
for $\vartheta=0.54$, blow-up for $0.53$, and $2.47\times10^{-6}$ for $\vartheta=10$ (§4.1.1,
Table 4.1); on nonlinear convection–diffusion $\vartheta=10$ costs a factor $10^3$–$10^4$ in error
(Tables 4.3–4.4), while on generalized KdV the penalty is mild (Tables 4.13–4.14). The
instability at $0.53$ appears only on fine meshes, where $h/\Delta x^r$ is large, and several
2D runs show no instability yet on the meshes used (§4.1.2, §4.3.2). Tan et al. (2025, §4) use
exactly $\vartheta=0.54$ in all tests.

Caliari et al. (2024) refine the "as small as stability permits" rule they attribute to Wang
et al.: on 1D diffusion and diffusion–reaction every method becomes more accurate as
$\vartheta$ decreases and the bounds are sharp (§4, Figs. 2–4), but on 2D and 3D
advection–diffusion–reaction a cheap coarse-grid scan picks values above the bound, e.g.
0.57 for the second-order IMEX scheme against its bound 0.5 and 0.57 for stabilized
Lawson2 against 0.183 (§3, §5, Tables 2–3). The scan on $2^6$ points agrees closely with one
on $2^8$ (§5.1).

## Cost

* **Navier–Stokes, finite differences** (Tan et al. 2025, §4.4.1, Tables 4.6–4.7): with a
  direct sparse solver (PARDISO), serial Fortran, on a $160^2$ manufactured problem, the EIN
  scheme takes 69 time units for all three viscosity levels, while explicit SSPRK(3,3) with
  its parabolic step limit takes 106, 502 and 1015, ratios 1.54, 7.28 and 14.71 as the
  viscosity parameter grows from 0.1 to 1; refining from $160^2$ to $320^2$ at fixed
  viscosity raises the ratio from 7.28 to 19.39. The CPU-time units are not printed.
* **Exponential reformulation** (Caliari et al. 2024, §5–6, Figs. 6, 8–9): with FFT or
  Kronecker-structured exponentials the reformulated schemes beat the same integrators on
  the full operator (Krylov-type matrix functions or BiCGStab solves), up to a factor of
  about 15 in 3D, and often beat IMEX schemes.

## Relation to other ways of linearizing the implicit part

[Semi-implicit IMEX methods](/methods/semi-implicit-imex-runge-kutta.md) and
[nonlinearly partitioned Runge–Kutta methods](/methods/nonlinearly-partitioned-runge-kutta.md)
freeze the state-dependent coefficients of the stiff term at explicit values, so each stage
solves a linear system whose matrix changes with the state; Tan et al. (2025, §1) cite
semi-implicit methods as "the other" strategy. EIN keeps the matrix constant, can factor it
once (for a fixed surrogate) and needs no structure of the nonlinearity, but needs a
threshold and pays an error that grows with the surrogate *(compiler comparison)*.
[Rosenbrock methods](/methods/rosenbrock-wanner-method.md) linearize with the exact Jacobian
at every step.

## Qualifications

* **Temporal order not isolated.** Tan et al. (2025) claim "designed third order accuracy",
  but with $h\propto\Delta x$ their tables show orders 4–5 where spatial errors dominate, and
  about 3 only on the manufactured problems (Tables 4.1–4.5); the authors attribute the
  higher orders to the "small time error of the problem itself" (§4). Tan et al. (2022)
  assert the third order of the pair without verifying it in time.
* **"Solved only once".** Tan et al. (2022, §1) say the implicit matrix needs to be inverted
  only once; in their nonlinear tests the surrogate coefficient is recomputed from $u_n$ at
  every step, so the matrix changes from step to step, though it stays linear and
  constant-coefficient in space. Tan et al. (2025) do not say whether their coefficient is
  updated.
* **Unreconciled numbers.** Fig. 3.1 of Tan et al. (2025) shows maximal Courant numbers near
  1.8 at small viscosity for one background state, against the bound 1.2 of the pure
  convection limit (Eq. (3.8)); the paper does not reconcile them, though 1.2 is a minimum
  over sampled states.
* **Baselines.** The CPU comparison of Tan et al. (2025) is against a fully explicit scheme
  only; the advantage over a standard IMEX scheme with implicit nonlinear viscosity is
  argued, not measured. Caliari et al. (2024) compare with two IMEX schemes, both of
  threshold $\frac12$.
* **Printed slips.** Tan et al. (2022) introduce their von Neumann lemmas as necessary and
  sufficient but state them as sufficient, and print the domain of their Zakharov–Kuznetsov
  test as $(\pi,\pi)^2$; Tan et al. (2025) switch the viscous-flux subscript from $\mu$ to
  $\nu$, a letter they also use for $h/\Delta x^2$ (reader's checks, recorded on the Source
  pages).

# Citations

- [Tan et al. (2022)](/sources/tan-2022.md) — §1 (Eq. (1.4)); §2 (Eqs. (2.9), (2.12), (2.14), (2.16)–(2.17)); §3 (Lemmas 3.1–3.2, Props. 3.1–3.2, Remarks 3.1–3.4); §4 (Tables 4.1–4.26).
- [Tan et al. (2025)](/sources/tan-2025.md) — §1; §2 (Props. 2.1–2.2); §3.4 (Eqs. (3.2)–(3.5), Remark 3.2); §3.5 (Eqs. (3.8)–(3.10), Prop. 3.1, Remark 3.1, Fig. 3.1); §4 (Eq. (4.1), Tables 4.1–4.7); §5.
- [Caliari et al. (2024)](/sources/caliari-2024.md) — §1; §2 (Thms. 2.1–2.7, Remarks 2.1–2.2, Table 1); §3 (Eq. (11)); §4 (Figs. 2–4); §5 (Tables 2–3, Figs. 5–9); §6.
- [Buvoli & Southworth (2025)](/sources/buvoli-2025.md) — §2.3 (EIN as add-and-subtract IMEX), Eqs. (4.24)–(4.26).
