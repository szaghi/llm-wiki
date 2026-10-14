---
type: Definition
title: "Legendre polynomials"
description: "The polynomial solutions P_n of Legendre's equation, standardized by P_n(1)=1 and orthogonal with unit weight on [-1,1] with norm 2/(2n+1); explicit form, parity, special values, bound |P_n|<=1, Legendre series, and the second-kind functions Q_n."
status: established
aliases: [Legendre functions of the first kind, Legendre series, Legendre functions of the second kind]
tags: [legendre, classical-family, orthogonality, expansion]
timestamp: 2026-10-14T00:00:00Z
---

# Legendre polynomials

## Definition

Legendre's equation
$$(1-x^2)\,y''-2x\,y'+\ell(\ell+1)\,y=0$$
has regular singular points at $x=\pm1$ and $\infty$; its power-series
solutions about $x=0$ converge for $|x|<1$. For integer $\ell=n\ge0$ one of
the two series terminates and gives a polynomial of degree $n$; scaled so
that
$$P_n(1)=1,$$
it is the **Legendre polynomial** $P_n(x)$, valid for all finite $x$
([Riley et al. (2006)](/sources/riley-2006.md), §18.1.1, eqs. 18.1–18.4,
pp. 577–578; [Arfken et al. (2013)](/sources/arfken-2013.md), §15.1,
pp. 716–717, where the scale is set by the generating function, eq. 15.7).
The other series does not terminate and diverges at $x=\pm1$; this is why
regularity at both poles of a sphere ($\theta=0,\pi$ with $x=\cos\theta$)
forces $\ell$ to be an integer and selects $P_n$ (Riley et al., §18.1.2,
p. 580; Arfken et al., §15.1, p. 716).

The first members (both sources; Arfken et al. Table 15.1 to $n=8$, p. 719):
$$P_0=1,\quad P_1=x,\quad P_2=\tfrac12(3x^2-1),\quad P_3=\tfrac12(5x^3-3x),\quad P_4=\tfrac18(35x^4-30x^2+3).$$

Explicit form ([Arfken et al. (2013)](/sources/arfken-2013.md), eq. 15.14,
p. 718; proof left as an exercise):
$$P_n(x)=\sum_{k=0}^{\lfloor n/2\rfloor}(-1)^k\frac{(2n-2k)!}{2^n\,k!\,(n-k)!\,(n-2k)!}\,x^{n-2k},$$
so the leading coefficient is $k_n=(2n-1)!!/n!$ (eq. 15.13, p. 717).

## Basic properties

* **Parity.** $P_n(-x)=(-1)^nP_n(x)$, hence $P_n(-1)=(-1)^n$, $P_{2n+1}(0)=0$
  and $P_{2n}(0)=(-1)^n(2n-1)!!/(2n)!!$ (Arfken et al., eqs. 15.9–15.11,
  p. 717; Riley et al. state $P_n(-1)=(-1)^n$, p. 578).
* **Bound.** $|P_n(x)|\le1$ on $[-1,1]$, with the global maximum $1$ at
  $x=1$ (and at $x=-1$ for even $n$). Arfken et al. prove it by writing
  $P_n(\cos\theta)=\sum_m a_{nm}\cos m\theta$ with all $a_{nm}>0$ from the
  generating function (eqs. 15.27–15.28, p. 720). Riley et al. do not state
  the bound.
* **Zeros.** $P_n$ has $n$ real zeros in the interior of $[-1,1]$: stated
  by Arfken et al. only as an exercise, with the Rolle's-theorem argument as
  hint and Gauss–Legendre quadrature as motivation (Exercise 15.1.18,
  p. 724). Riley et al. use the zeros as the Gauss–Legendre nodes without
  proving that they are real and simple (see
  [Gauss–Legendre quadrature](/methods/gauss-legendre-quadrature.md)).
* **Rodrigues formula** $P_n=\frac{1}{2^nn!}\frac{d^n}{dx^n}(x^2-1)^n$, the
  **generating function** $(1-2xt+t^2)^{-1/2}=\sum_nP_nt^n$ and the
  **recurrence** $(n+1)P_{n+1}=(2n+1)xP_n-nP_{n-1}$ are on
  [Rodrigues formula](/results/rodrigues-formula.md),
  [generating functions](/results/generating-functions.md) and
  [three-term recurrences](/results/three-term-recurrences.md).

## Orthogonality and Legendre series

$$\int_{-1}^1P_n(x)P_m(x)\,dx=\frac{2}{2n+1}\,\delta_{nm}.$$
Riley et al. prove orthogonality directly from the differential equation and
the norm from the Rodrigues formula through $K_n=\int_{-1}^1(1-x^2)^n\,dx=2^{2n+1}(n!)^2/(2n+1)!$
([Riley et al. (2006)](/sources/riley-2006.md), eqs. 18.11–18.12,
pp. 582–583); Arfken et al. obtain the norm by squaring the generating
function and integrating, giving $\frac1t\ln\frac{1+t}{1-t}=2\sum_nt^{2n}/(2n+1)$
([Arfken et al. (2013)](/sources/arfken-2013.md), eqs. 15.33–15.38,
p. 725). With $x=\cos\theta$, the weight becomes $\sin\theta\,d\theta$
(eq. 15.32). A function on $[-1,1]$ has the **Legendre series**
$$f(x)=\sum_{n=0}^\infty c_nP_n(x),\qquad c_n=\frac{2n+1}{2}\int_{-1}^1f(x)P_n(x)\,dx$$
(Riley et al., eqs. 18.13–18.14, p. 583; Arfken et al., eqs. 15.39–15.40,
p. 726). In particular $\int_{-1}^1P_n\,dx=0$ for $n\ne0$ (Riley et al.,
p. 583). Arfken et al.'s Example 18.4.1 compares a four-term Legendre series
of $e^x$ with a Chebyshev and a Taylor expansion; the Legendre error is
largest at $x=\pm1$ (§18.4, p. 906; see
[Chebyshev polynomials](/definitions/chebyshev-polynomials.md)).

The polynomials are the $m=0$ case of the
[associated Legendre functions](/definitions/associated-legendre-functions.md)
and, through the generating function, the coefficients of the
[expansion of the inverse distance](/results/legendre-expansion-of-inverse-distance.md).

## Legendre functions of the second kind $Q_n$

For integer $n$ the non-terminating solution, scaled so that it obeys the
same recurrences as $P_n$, is $Q_n$:
$$Q_0=\tfrac12\ln\frac{1+x}{1-x},\qquad Q_1=\tfrac x2\ln\frac{1+x}{1-x}-1,\qquad Q_2=P_2\,\tfrac12\ln\frac{1+x}{1-x}-\tfrac{3x}{2}$$
([Riley et al. (2006)](/sources/riley-2006.md), eqs. 18.5–18.8, pp. 579–580,
via the Wronskian method; [Arfken et al. (2013)](/sources/arfken-2013.md),
eqs. 15.154–15.157, pp. 766–767, via the second-solution integral
$Q_n=P_n\int^x dx/[(1-x^2)P_n^2]$). The general solution for integer $n$ is
$c_1P_n+c_2Q_n$ (Riley et al., eq. 18.7). $Q_n$ is singular at $x=\pm1$, has
parity $(-1)^{n+1}$ and is finite at $x=0$ (Arfken et al., p. 769).

**Scope difference.** Riley et al. treat $Q_n$ as a series converging only
for $|x|<1$ (p. 580, with a footnote pointing to a series in negative powers
for $|x|>1$). Arfken et al. extend the closed form beyond $|x|>1$ by
replacing $\ln\frac{1+x}{1-x}$ with $\ln\frac{x+1}{x-1}$, which removes a
$\pm i\pi P_n$ contribution, and note $Q_n(\infty)=0$ (pp. 767–769). The two
statements concern different ranges and do not conflict.

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §18.1, eqs. 18.1–18.27, pp. 577–586.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §15.1, eqs. 15.5–15.30, pp. 716–721; §15.2, eqs. 15.31–15.40, pp. 724–726; §15.6, eqs. 15.153–15.166, pp. 766–770; Exercise 15.1.18, p. 724.
