---
type: Method
title: "Linear multistep methods"
description: "A k-step linear multistep method combines k past values and right-hand sides into one new value per step; its generating polynomials, the root and stability-region conditions, variable-step coefficients, the Adams and BDF families, and the energy, linearly implicit and IMEX variants the sources build on it."
status: established
aliases: [LMM, linear k-step method, multistep method, Adams methods, Adams–Bashforth, Adams–Moulton, variable-coefficient multistep method]
tags: [linear-multistep, stability, stiff, implicit, explicit, step-size-control]
timestamp: 2026-10-20T10:00:00Z
---

# Linear multistep methods

A **linear $k$-step method** computes $y_{n+k}$ from the $k$ previous values and right-hand sides,

$$\sum_{j=0}^k\alpha_jy_{n+j}=h\sum_{j=0}^k\beta_jf(t_{n+j},y_{n+j}),$$

with $\alpha_k\ne0$. It is explicit if $\beta_k=0$ and implicit otherwise. An implicit method
needs one nonlinear solve per step, whatever its order. A Runge–Kutta method of the same order
needs several stage solves, and a multistep method also has no internal stages. Its first and second **generating polynomials** are
$\varrho(\zeta)=\sum_j\alpha_j\zeta^j$ and $\sigma(\zeta)=\sum_j\beta_j\zeta^j$. The sources
write the method in this form ([Kemm (2024)](/sources/kemm-2024.md), Eq. (15);
[Akrivis et al. (2021)](/sources/akrivis-2021.md), arXiv v1, Eqs. (1.2)–(1.3)). Some sources index it
backwards from the new point ([Glandon et al. (2022)](/sources/glandon-2022.md), Eq. (2.1), with
$i=-1$ the new point and $\alpha_{-1}=1$). Others use a fixed-leading-coefficient form with
$+h\sum\beta$ ([Gardner et al. (2022)](/sources/gardner-2022.md), §2.1; see
[CVODE](/software/cvode.md)). All of them are translated here.

## Normalizations

The coefficients are fixed only up to a common factor, and the sources normalize them
differently:

- $\alpha_k=1$ (Glandon et al. 2022, Eq. (2.4); [Ma et al. (2026)](/sources/ma-2026.md), Eq. (2.2));
- $\sigma(\zeta)=\zeta^k$ for BDF, so that $\alpha_k=\sum_{j=1}^k1/j$, e.g. $\alpha_6=147/60$
  (Akrivis et al. 2021, §1–2).

Error constants depend on the normalization; see Qualifications.

## Order and consistency

The method has order $p$ when its local residual on smooth solutions is $O(h^{p+1})$. Glandon et
al. (2022, Thm. 3.3, Remark 3.5) state the conditions with variable steps. Let
$\theta_j=(t_{n+j}-t_{n+k-1})/h$ (page-local; $\theta_j=j-k+1$ for constant steps). The conditions
are then

$$\sum_{j=0}^k\alpha_j=0,\qquad\sum_{j=0}^k\alpha_j\theta_j^{\ell}=\ell\sum_{j=0}^k\beta_j\theta_j^{\ell-1},\quad\ell=1,\dots,p,$$

*(translated by the compiler from their backward-indexed form (3.3a), (3.3c))*. They are linear
in the coefficients and have Vandermonde structure. For $p\le k$ they can be solved with
$\alpha_j$ continuous in the $\beta_j$, the step fractions and $k-p$ free parameters (Remark 3.6,
citing earlier work).

## Stability

**Zero-stability.** The method is zero-stable when the roots of $\varrho$ lie in the closed unit
disc and those on the unit circle are simple (Glandon et al. 2022, §4, as recalled from
Hairer–Nørsett–Wanner). With variable steps this becomes a condition on products of
stability matrices, and it can fail for step-ratio sequences that are not smooth; see
[zero-stability](/definitions/zero-stability.md).

**Linear stability.** For $y'=\lambda y$ and $z=h\lambda$ the characteristic equation is
$\varrho(\zeta)-z\sigma(\zeta)=0$. The stability region $\mathcal S$ is the set of $z$ for which
all roots satisfy $\lvert\zeta_j(z)\rvert\le1$, with multiple roots strictly inside. Its boundary
is traced by the boundary locus $z=\varrho(e^{i\phi})/\sigma(e^{i\phi})$ (Glandon et al. 2022,
Eqs. (4.3)–(4.4); $\phi$ page-local). This is a root condition, not a condition
$\lvert R(z)\rvert\le1$ on a [stability function](/definitions/stability-function.md). For
$\beta$-coefficients depending on the step ratios the polynomials depend on them too
(Remark 4.1).

**Barriers and stability classes.** A-stable linear multistep methods have order at most 2, as
recalled by [Farrell et al. (2021)](/sources/farrell-2021.md) (§2.1), [Southworth et al. (2022)](/sources/southworth-2022.md)
(§2.1) and [Taddei et al. (2026)](/sources/taddei-2026.md) (§1.1); this is Dahlquist's second
barrier. Higher-order stiff multistep methods are therefore only A($\alpha$)-stable; see
[A-stability](/properties/a-stability.md) for the angles of BDF and of the linearly implicit
methods below. A-stability of a method is equivalent to [G-stability](/properties/g-stability.md)
of its one-leg twin (Akrivis et al. 2021, Lemma 2.1, as recalled from Dahlquist).

## Families

- **Backward differentiation formulas** ($\sigma(\zeta)=\zeta^k$ up to normalization), order $k$,
  the standard stiff family; see [BDF](/methods/backward-differentiation-formula.md).
- **Adams methods.** $\varrho(\zeta)=\zeta^k-\zeta^{k-1}$. Adams–Bashforth is explicit
  ($\beta_k=0$, order $k$), written $y_{n+1}=y_n+h\sum_j\beta_jf_{n-j}$ by Kemm (2024, Eq. (16)).
  Adams–Moulton is implicit (order $k+1$). Glandon et al. (2022, Table 6.1) tabulate the error
  constants of both. CVODE uses Adams–Moulton of orders 1–12 for nonstiff problems (Gardner et
  al. 2022, §2.1).
- **Linearly implicit multistep methods (Limm, Limm-W)** add a Jacobian term so that each step
  needs one linear solve instead of a nonlinear one (Glandon et al. 2022); see
  [linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md).
- **IMEX multistep methods** treat a stiff part with an implicit method (usually BDF) and the
  rest by explicit extrapolation (Ma et al. 2026; [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md));
  see [IMEX linear multistep methods](/methods/imex-linear-multistep-methods.md).
- **Modified Patankar multistep methods (MPLM).** [Izzo et al. (2025)](/sources/izzo-2025.md)
  take explicit methods whose coefficients of the past values and right-hand sides are all
  nonnegative (in the registry form with $\alpha_k=1$: $-\alpha_j\ge0$ and $\beta_j\ge0$ for
  $j<k$) and weight each production and destruction term of a
  [production–destruction system](/definitions/production-destruction-system.md) by a ratio
  of the new value to a positive denominator. Each step is one linear M-matrix system, so the
  scheme is positive and conservative for every $h$, and it has order $p$ iff the
  denominators approximate $y(t_n)$ to $\mathcal O(h^p)$ (Def. 2.1, Lemmas 2.2–2.3, Thms.
  3.1–3.6). Their base methods of orders 2–6 (Table 1) include leapfrog,
  $y_{n+2}=y_n+2hf(y_{n+1})$, and methods $y_{n+k}=y_n+h\sum_j\beta_jf(t_{n+j},y_{n+j})$
  for $k=5,7,10$; all roots of $\varrho$ lie on the unit circle, so they are zero-stable but
  only weakly stable, and every one has some $\beta_j>0$ with $\alpha_j=0$, so its SSP
  coefficient as a classical method is 0 *(compiler check of their Table 1)*. The
  convergence proof is a discrete Gronwall argument that uses the nonnegativity of the
  $\alpha$-coefficients rather than the root condition (Thm. 3.5). See
  [modified Patankar methods](/methods/modified-patankar-methods.md).

## Explicit multistep methods for low-dissipation semidiscretizations

Kemm (2024) uses Adams–Bashforth (AB) as the alternative to explicit Runge–Kutta methods for
low-Mach and all-Mach finite-volume schemes. In those schemes the acoustic viscosity scales with
the flow speed, and the semidiscrete spectrum fills ellipses between the upwind circle and a
segment of the imaginary axis (§3.3, Fig. 1). Its findings:

- **Linear stability.** The integrator must be stable on the convex hull of those ellipses,
  which needs an imaginary-axis segment in its region. Among minimal-stage Runge–Kutta methods
  only RK3 and RK4 have one; among AB methods order 3 or more is needed (root-locus curves for
  $k=1,\dots,5$, §3.3, Fig. 2). AB needs a Courant number that shrinks with the order, but only
  one flux evaluation per step, so its cost is stated to be "nearly identical" to Runge–Kutta of
  the same order (§3.3; not quantified).
- **Numerical behaviour.** With a nonlinear limiter, AB3 and often AB2 behave clearly better
  than Heun's RK3 on noisy uniform flow, a subsonic cylinder, a Mach 20 blunt body and a
  Richtmyer–Meshkov instability (§4.1–§4.4, Figs. 3–12). With first order in space, RK3 behaves
  as linear theory predicts (Fig. 5). On an Elling test all RK and AB runs fail, and on a
  Kelvin–Helmholtz instability RK and AB are indistinguishable (§4.5).
- **Explanation offered.** Every explicit RK step starts with a forward-Euler stage, which is
  unstable for these semidiscretizations, while a multistep method has no internal stage
  (§1, §3.1, §5). The paper does not prove this; see Qualifications and
  [internal stability](/definitions/internal-stability.md).
- **Implementation.** Variable-step AB is implemented with variable coefficients (after
  Hairer–Nørsett–Wanner), and the method starts with lower-order AB from a first explicit Euler
  step (§3.2, §4).

Kemm also argues that SSP theory for Runge–Kutta and multistep methods does not apply here,
because it rests on the strong stability of forward Euler, which these schemes lack (§3.1–§3.2;
see [strong-stability-preserving Runge–Kutta](/methods/strong-stability-preserving-runge-kutta.md)).

## Variable steps and implementation

Variable-step multistep methods are variable-coefficient methods: every $\alpha_j$ and $\beta_j$
depends on the recent step ratios $r_n=h_n/h_{n-1}$ (Glandon et al. 2022, Assumption 3.1, §3;
Gardner et al. 2022, §2.1). The practical consequences recorded by the sources:

- **History storage.** Glandon et al. (2022, §7, Eqs. (7.6)–(7.8)) keep divided differences of
  past values and right-hand sides and update them recursively, a form similar to Nordsieck
  vectors. A local error estimate uses one more past value than the method itself.
- **Step-ratio restrictions.** Stability of variable-step methods needs bounded step ratios, and
  sometimes bounded variation of the ratios; see [zero-stability](/definitions/zero-stability.md)
  and [variable-step BDF2 stability](/results/variable-step-bdf2-stability.md).
- **Step-size and order control** for multistep methods is on
  [step-size control](/methods/step-size-control.md). Two of its rules: steps grow only after
  $k$ successful steps at the current size (Glandon et al. 2022, Remark 7.3), and a restart
  begins again at first order and loses the error history ([Reynolds et al. (2023)](/sources/reynolds-2023.md),
  §5.1.3).
- **Starting values.** A $k$-step method needs $k$ starting values. The sources use a
  self-starting variable-order sequence (Glandon et al. 2022, Remark 7.2), lower-order methods
  (Kemm 2024, §4; García-Archilla & Novo 2023, IMEX Euler for the first step), or IMEX
  Runge–Kutta at a much smaller step (Ma et al. 2026, §4).

## Energy analysis for parabolic problems

For $y'=Ly$ with $-L$ self-adjoint and positive definite, energy proofs for multistep methods
test the scheme with $y_{n+k}$, or with $y_{n+k}-\sum_j\mu_jy_{n+k-j}$. A G-norm then
telescopes. The technique is on [multiplier energy technique](/methods/multiplier-energy-technique.md)
and [G-stability](/properties/g-stability.md). It is the route by which Akrivis et al. (2021)
prove stability of six-step BDF ([BDF6 energy stability](/results/bdf6-energy-stability.md)),
[Akrivis et al. (2024)](/sources/akrivis-2024.md) prove stability of variable-step BDF2, and
Ma et al. (2026) prove uniform accuracy of IMEX-BDF.

## Qualifications

- **Backward-indexed coefficients.** Izzo et al. (2025, Eq. (2.7)) write the method as
  $y_n=\sum_{r=1}^k\bar\alpha_ry_{n-r}+h\sum_{r=1}^k\bar\beta_rf(y_{n-r})$ (page-local bars;
  $\bar\alpha_r=-\alpha_{k-r}$, $\bar\beta_r=\beta_{k-r}$ with $\alpha_k=1$) with order
  conditions $\sum_r\bar\alpha_r=1$, $\sum_r(r^q\bar\alpha_r-qr^{q-1}\bar\beta_r)=0$. They print
  the three-step second-order SSP scheme with $\bar\beta=(0,\tfrac32,0)$, which is only first
  order; $\bar\beta=(\tfrac32,0,0)$, i.e. $y_n=\tfrac34y_{n-1}+\tfrac14y_{n-3}+\tfrac32hf(y_{n-1})$,
  is second order *(compiler check of p. 4 against (2.7))*.

- **Error-constant normalization.** Glandon et al. (2022, Table 6.1) list BDF error constants as
  $1/(k+1)$, which is the constant divided by $\sigma(1)$. Their Limm constants come from
  Eq. (7.3) with $\alpha_k=1$ and are not divided by $\sigma(1)$. The caption does not state the
  normalization, so comparisons across rows can mix the two; for $k=1$ they coincide.
- **"Unstable first stage" is a hypothesis.** Kemm's (2024) explanation of the AB/RK difference
  is supported only by experiments, and his own first-order-in-space test shows RK3 behaving
  as linear theory predicts. The paper gives no internal-stability or nonlinear-stability
  analysis. Two further points of his tests are unexplained: AB2's root locus does not cover the
  imaginary axis yet AB2 behaves well (Fig. 3), and AB3 ran at Courant number 0.1 against 0.65
  for RK3 on the blunt body (§4.3).

# Citations

- [Glandon et al. (2022)](/sources/glandon-2022.md) — §2 (Eq. (2.1)), §3 (Assumption 3.1, Thm. 3.3, Remarks 3.5–3.6), §4 (Eqs. (4.2)–(4.4), Remark 4.1), §7 (Eqs. (7.6)–(7.8), Remarks 7.2–7.3), Table 6.1.
- [Kemm (2024)](/sources/kemm-2024.md) — §1, §3.1–§3.3 (Eqs. (15)–(16), Figs. 1–2), §4 (Figs. 3–14), §5.
- [Akrivis et al. (2021)](/sources/akrivis-2021.md) — arXiv v1: §1–2 (Eqs. (1.2)–(1.3), Lemma 2.1).
- [Akrivis et al. (2024)](/sources/akrivis-2024.md) — §1.
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) — §2–3 (starting step).
- [Ma et al. (2026)](/sources/ma-2026.md) — Eq. (2.2), §2.2, §4.
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §1.1 (Dahlquist barrier).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.1 (fixed-leading-coefficient form, CVODE families).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §5.1.3 (restart at first order).
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §2.1 (Dahlquist barrier).
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §2.1 (Dahlquist barrier).
- [Izzo et al. (2025)](/sources/izzo-2025.md) — §2 (Def. 2.1, Eq. (2.7)), §3 (Thms. 3.1–3.6), Table 1, §5; arXiv v1.
