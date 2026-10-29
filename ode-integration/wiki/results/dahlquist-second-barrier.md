---
type: Result
title: "Dahlquist's order barrier for A-stable multistep methods"
description: "Dahlquist (1963) proves that an A-stable linear multistep method has order at most 2, that no explicit one is A-stable, and that among A-stable methods the trapezoidal rule alone attains the smallest error constant 1/12; the page gives the criterion, the proof, the escapes and how later sources recall it."
status: established
aliases: [second Dahlquist barrier, order barrier for A-stable linear multistep methods]
tags: [linear-multistep, stability, stiff, order-conditions]
timestamp: 2026-10-29T18:00:00Z
---

# Dahlquist's order barrier for A-stable multistep methods

**Theorem** ([Dahlquist (1963)](/sources/dahlquist-1963.md), §2, Thm. 2.2, p. 31). "The order,
$p$, of an A-stable linear multistep method cannot exceed 2. The smallest error constant,
$c^*=\frac1{12}$, is obtained for the trapezoidal rule, $k=1$." The trapezoidal rule is
moreover the only linear multistep method with $p=2$ and $c^*=\frac1{12}$ among the A-stable
ones (p. 32). The companion Theorem 2.1 states that "an explicit $k$-step method cannot be
A-stable" (p. 30). Later sources call the order bound the "second Dahlquist barrier"
([Taddei et al. (2026)](/sources/taddei-2026.md), §1.1;
[Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md), §2); the 1963 paper does not use that
name.

## Setting and definitions

The method is the [linear multistep method](/methods/linear-multistep-method.md)
$\sum_{j=0}^k\alpha_jy_{n+j}=h\sum_{j=0}^k\beta_jf(t_{n+j},y_{n+j})$, $\alpha_k\ne0$, with
generating polynomials $\varrho$, $\sigma$, assumed to have no common divisor (§1, Eqs.
(1.2)–(1.3)). Dahlquist's definitions (§1, pp. 28–29), in registry notation (his $x$, $q$ are
$y$, $\lambda$):

- **Order and error constant.** Let $\mathcal L_h\varphi(t)=\sum_j\alpha_j\varphi(t+jh)-h\sum_j\beta_j\varphi'(t+jh)$
  (page-local). The order $p$ is the largest integer for which $\mathcal L_h$ annihilates all
  polynomials of degree $p$; then $\mathcal L_h\varphi\sim-c\,h^{p+1}\varphi^{(p+1)}$ as $h\to0$,
  and the **error constant** is $c^*=c/\sigma(1)$. Consistency is $\varrho(1)=0$,
  $\varrho'(1)=\sigma(1)$ (Eq. (1.6)), and with $\zeta=e^h$
  $$\log\zeta-\frac{\varrho(\zeta)}{\sigma(\zeta)}\sim c^*(\zeta-1)^{p+1},\qquad\zeta\to1\qquad(1.7).$$
  With this sign convention the trapezoidal rule has $c^*=+\frac1{12}$.
- **A-stability.** "A $k$-step method is called A-stable, if all solutions of (1.2) tend to
  zero, as $n\to\infty$, when the method is applied with fixed positive $h$ to any differential
  equation of the form $dx/dt=qx$, where $q$ is a complex constant with negative real part."
  See [A-stability](/properties/a-stability.md) for this definition beside the region form.

## The criterion

**Lemma 2.1** (p. 30). A $k$-step method is A-stable iff $\varrho(\zeta)/\sigma(\zeta)$ is
regular and has non-negative real part for $\lvert\zeta\rvert>1$.

The proof uses the characteristic equation $\varrho(\zeta)-z\sigma(\zeta)=0$ (Eq. (2.1)):
A-stability means that $\operatorname{Re}z<0$ forces $\lvert\zeta\rvert<1$, equivalently that a
root with $\lvert\zeta\rvert\ge1$ forces $\operatorname{Re}z\ge0$, and $z=\varrho/\sigma$ on the
roots. A zero of $\sigma$ outside the unit disc would be a pole of $\varrho/\sigma$, incompatible
with a non-negative real part around it; simple zeros of $\sigma$ on $\lvert\zeta\rvert=1$ are
allowed. Theorem 2.1 follows: for an explicit method ($\beta_k=0$) $\varrho/\sigma$ grows like
$b\zeta^m$, $b\ne0$, $m\ge1$, at infinity, which cannot keep a non-negative real part outside
the unit circle.

A-stable consistent methods exist (p. 30): the trapezoidal rule $\varrho=\zeta-1$,
$\sigma=\frac12(\zeta+1)$ (Eq. (2.2)); $\varrho=\zeta-1$, $\sigma=\zeta$ (backward Euler, unnamed
in the paper); and $\varrho=\zeta^k-1$, $\sigma=\frac12k(\zeta^k+1)$ for every positive integer
$k$.

## Proof of the barrier

(§2, pp. 31–32.) Let $w=(\zeta+1)/(\zeta-1)$ (page-local; it maps $\lvert\zeta\rvert>1$ onto
$\operatorname{Re}w>0$), and define the polynomials
$r(w)=\big(\tfrac{w-1}2\big)^k\varrho(\zeta(w))$ and $s(w)=\big(\tfrac{w-1}2\big)^k\sigma(\zeta(w))$
(page-local), of degrees at most $k-1$ and $k$. The method is A-stable iff $r/s$ is regular with
non-negative real part in $\operatorname{Re}w>0$, and (1.7) becomes
$\log\frac{w+1}{w-1}-\frac{r(w)}{s(w)}\sim c^*\big(\frac2w\big)^{p+1}$ as $w\to\infty$. If $p\ge2$,

$$\frac{r(w)}{s(w)}=\frac2w+\Big(\frac23-8c'\Big)w^{-3}+O(w^{-4}),\qquad c'=\begin{cases}c^*,&p=2,\\0,&p>2.\end{cases}\qquad(2.3)$$

A variant of the Riesz–Herglotz representation of functions with non-negative real part in the
right half-plane (cited from Achieser–Glazman, "suggested by P. D. Lax") gives
$r(w)/s(w)=\int_{-\infty}^{\infty}d\omega(\tau)/(w-i\tau)$ with $\omega$ bounded and
non-decreasing (page-local $\omega$, $\tau$), so that for real $x>0$

$$\frac{x\,r(x)}{s(x)}=\int_{-\infty}^{\infty}\frac{x^2\,d\omega(\tau)}{x^2+\tau^2}\qquad(2.5)$$

is non-decreasing in $x$. A positive coefficient of $w^{-3}$ in (2.3) would make it decrease
for large $x$; hence $\frac23-8c'\le0$, so $c'\ge\frac1{12}>0$, which excludes $p>2$ and gives
$c^*\ge\frac1{12}$ at $p=2$. The trapezoidal rule has $r/s=2/w$, so $c^*=\frac1{12}$. For
uniqueness, $c'=\frac1{12}$ forces $d\omega=0$ away from $\tau=0$, so $r/s=2/w$, and coprimality
fixes $\varrho$, $\sigma$ up to a constant factor.

Dahlquist (1963, §2, p. 29) states that a preliminary upper bound for the order of an A-stable
method was obtained in his earlier paper (Theorem 4 there) and that the least upper bound "is
equal to 2".

## Scope and escapes

- **Linear multistep methods only.** "The theorems of this section are proved for linear
  multistep methods only" (p. 33). Dahlquist's own example of an A-stable procedure of order 4
  outside the class is Richardson extrapolation of the trapezoidal rule with the extrapolated
  values not fed back; feeding them back destroys A-stability
  ([extrapolation methods](/methods/extrapolation-methods.md)). He also notes that the classical
  fourth-order Runge–Kutta method is not A-stable, since its factor
  $1+z+z^2/2!+z^3/3!+z^4/4!$ tends to infinity as $z\to-\infty$ (pp. 32–33).
- **A-stable Runge–Kutta methods of every order.** Later sources contrast the barrier with
  implicit Runge–Kutta methods: A-stable Runge–Kutta methods exist of every order
  ([Farrell et al. (2021)](/sources/farrell-2021.md), §2.1), and Taddei et al. (2026, §1.1)
  give the barrier as their reason to use Radau IIA rather than higher-order BDF; see
  [fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md).
- **Weaker stability on a sector.** BDF of orders 3–6 are only A($\alpha$)-stable
  ([BDF](/methods/backward-differentiation-formula.md)). Dahlquist (1963, p. 29) points to
  Robertson's "less extreme approach": two-step third-order methods whose solutions decay "in a
  large portion of the complex plane" for $z$, though not in the whole half-plane.
- **Methods that are neither Runge–Kutta nor multistep.** The deferred-correction schemes of
  [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) are A-stable, in the
  asymptotic sense, at every even order; see [A-stability](/properties/a-stability.md).
- **Nonlinear problems.** For the optimal method, the trapezoidal rule, Dahlquist (1963, §3)
  proves error bounds under a one-sided Lyapunov condition that stay bounded for all times
  without a restriction from $\lvert h\,\partial f/\partial y\rvert$, which he calls "a
  generalization of the A-stability property" (pp. 40–41); see
  [B-convergence](/definitions/b-convergence.md).

## How later sources recall it

[Southworth et al. (2022)](/sources/southworth-2022.md) (§2.1), Farrell et al. (2021, §2.1),
Taddei et al. (2026, §1.1) and Abu-Labdeh et al. (2023, §2) state the order bound $p\le2$. None
of them recalls the error-constant part ($c^*\ge\frac1{12}$, equality only for the trapezoidal
rule) or Theorem 2.1.
[Akrivis et al. (2021)](/sources/akrivis-2021.md) (Lemma 2.1, as recalled from Dahlquist) and
[Ma et al. (2026)](/sources/ma-2026.md) (§2.2) use the equivalence of A-stability of a multistep
method with [G-stability](/properties/g-stability.md) of its one-leg twin; the condition stated
there is, like Lemma 2.1, a positive-real-part condition on a quotient with $\varrho$ in the
numerator outside the unit disc.

## Qualifications

- **Error-constant sign.** Dahlquist defines $c$ through $\mathcal L_h\varphi\sim-c\,h^{p+1}\varphi^{(p+1)}$,
  which makes the trapezoidal constant $+\frac1{12}$. A convention with a plus sign gives
  $-\frac1{12}$ for the same method. *(Compiler check, not in the sources:
  $y(t+h)-y(t)-\frac h2\big(y'(t+h)+y'(t)\big)=-\frac1{12}h^3y'''(t)+O(h^4)$, so $c=\frac1{12}$
  and, with $\sigma(1)=1$, $c^*=\frac1{12}$.)*
- **Imaginary axis.** The definition asks for decay on the open half-plane only. In a note added
  in proof Dahlquist (1963, p. 43) derives that an A-stable method applied with purely imaginary
  $\lambda$ has bounded solutions: the roots of (2.1) satisfy $\lvert\zeta\rvert\le1$, and those
  of unit modulus are simple.
- **Recalled bound for stable methods.** Dahlquist (1963, p. 28) also recalls from Henrici a
  bound on the order of methods with "a certain stability property", which is recorded on
  [zero-stability](/definitions/zero-stability.md).

# Citations

- [Dahlquist (1963)](/sources/dahlquist-1963.md) — §1 (Eqs. (1.2)–(1.8), definitions, pp. 28–29); §2 (Lemma 2.1, Thm. 2.1, examples (2.2), p. 30; Thm. 2.2 and proof, Eqs. (2.3)–(2.5), pp. 31–32; RK4 and Richardson extrapolation, pp. 32–33); §3 (pp. 40–41); note added in proof (p. 43).
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §1.1 ("second Dahlquist barrier", Radau IIA).
- [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) — §2 ("second Dahlquist barrier").
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §2.1 (order bound; A-stable RK of every order).
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §2.1 (order bound).
- [Akrivis et al. (2021)](/sources/akrivis-2021.md) — arXiv v1: Lemma 2.1 (A- and G-stability).
- [Ma et al. (2026)](/sources/ma-2026.md) — §2.2 (A- and G-stability).
- [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) — Def. 5.1, Thm. 5.1 (A-stable deferred correction).
