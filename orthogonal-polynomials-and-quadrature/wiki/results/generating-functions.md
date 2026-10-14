---
type: Result
title: "Generating functions of the classical polynomials and Bessel functions"
description: "Closed-form functions g(x,t) whose Taylor or Laurent coefficients in t are the Legendre, associated Legendre, Chebyshev, Gegenbauer, Hermite, Laguerre, associated Laguerre polynomials and the integer-order Bessel functions; how recurrences follow from them, and the two different Chebyshev T_n generating functions of the founding sources."
status: established
aliases: [generating function]
tags: [generating-function, recurrence, classical-family, bessel]
timestamp: 2026-10-14T00:00:00Z
---

# Generating functions of the classical polynomials and Bessel functions

## Definition and use

A generating function for $f_n(x)$ is a $g(x,t)$ with
$g(x,t)=\sum_nc_nf_n(x)\,t^n$, a Taylor series ($n\ge0$) or a Laurent series
($n\in\mathbb Z$); the constants $c_n$ allow a chosen scale, and different
$c_n$ give different $g$ for the same functions
([Arfken et al. (2013)](/sources/arfken-2013.md), §12.1, eq. 12.19, p. 555;
[Riley et al. (2006)](/sources/riley-2006.md), §18.1.2, p. 584, with
$c_n=1$ and $h$ for $t$). By the residue theorem
$c_nf_n(x)=\frac1{2\pi i}\oint g(x,t)\,t^{-n-1}dt$ (Arfken et al.,
eq. 12.20). Differentiating $g$ in $t$ and re-expanding gives recurrences
between $f_{n-1},f_n,f_{n+1}$; differentiating in $x$ gives derivative
relations (Arfken et al., Example 12.1.2, pp. 555–556; Riley et al.,
eqs. 18.16–18.21, pp. 584–585). For polynomials with a Rodrigues formula,
summing the Schlaefli integral against $t^n$ and evaluating by residues
constructs $g$; Arfken et al. carry this out for Legendre (Example 12.1.3,
pp. 557–558) and Laguerre (eqs. 18.47–18.49, pp. 889–890).

## Table

| Functions | Generating function | Locators |
|---|---|---|
| $P_n$ | $(1-2xt+t^2)^{-1/2}=\sum_{n\ge0}P_nt^n$ | Riley eq. 18.15, p. 584; Arfken eqs. 12.27, 15.6 |
| $P_{n+m}^m$ | $\dfrac{(-1)^m(2m-1)!!\,(1-x^2)^{m/2}}{(1-2xt+t^2)^{m+1/2}}=\sum_{n\ge0}P_{n+m}^m\,t^n$ | Arfken eq. 15.82, p. 743 (polynomial factors); Riley eq. 18.40, p. 592 (without $(-1)^m$) |
| $C_n^{(\lambda)}$ | $(1-2xt+t^2)^{-\lambda}=\sum_{n\ge0}C_n^{(\lambda)}t^n$ | Arfken eq. 18.85, p. 899 |
| $U_n$ | $(1-2xt+t^2)^{-1}=\sum_{n\ge0}U_nt^n$ | Riley eq. 18.64, p. 601; Arfken eq. 18.86, p. 899 |
| $T_n$ (Riley) | $\dfrac{1-xt}{1-2xt+t^2}=\sum_{n\ge0}T_nt^n$ | Riley eq. 18.63, p. 601 |
| $T_n$ (Arfken) | $\dfrac{1-t^2}{1-2xt+t^2}=T_0+2\sum_{n\ge1}T_nt^n$ | Arfken eq. 18.91, p. 900; Table 12.1, p. 559 |
| $H_n$ | $e^{2xt-t^2}=\sum_{n\ge0}H_n\,t^n/n!$ | Riley eq. 18.133, p. 627; Arfken eqs. 12.21, 18.2 |
| $L_n$ | $\dfrac{e^{-xt/(1-t)}}{1-t}=\sum_{n\ge0}L_nt^n$ | Riley eq. 18.114, p. 620; Arfken eq. 18.49, p. 890 |
| $L_n^{(m)}$ | $\dfrac{e^{-xt/(1-t)}}{(1-t)^{m+1}}=\sum_{n\ge0}L_n^{(m)}t^n$ | Riley eq. 18.123, p. 623 |
| $L_n^{(\ell-n)}$ | $e^{-tx}(1+t)^\ell=\sum_{n\ge0}L_n^{(\ell-n)}t^n$ | Arfken eq. 18.60, p. 892 (after Weber 2007) |
| $J_n$, $n\in\mathbb Z$ | $e^{(x/2)(t-1/t)}=\sum_{n=-\infty}^\infty J_nt^n$ | Riley eq. 18.98, p. 613; Arfken eq. 14.2, p. 644 |

## The two Chebyshev $T_n$ generating functions

The founding sources print different generating functions for $T_n$. Both
are correct: they are different weighted sums of the same polynomials.
Their difference is
$$\frac{1-t^2}{1-2xt+t^2}-\frac{1-xt}{1-2xt+t^2}=\frac{t(x-t)}{1-2xt+t^2}=\sum_{n\ge1}T_n\,t^n,$$
which is consistent with Arfken's form minus Riley's form,
$\big(T_0+2\sum_{n\ge1}T_nt^n\big)-\sum_{n\ge0}T_nt^n$ (compiler's check,
using $T_0=1$). Arfken et al. derive theirs as the $\lambda\to0$ limit of the
Gegenbauer generating function, which forces the special treatment of $n=0$
(eqs. 18.87–18.91, p. 900). Riley et al. call the Chebyshev generating
functions "of less practical use", since the trigonometric forms give most
results more easily (p. 601). This is a difference of convention, recorded
on both Source pages; it is not a contradiction.

## Consequences used elsewhere

* Legendre: $P_n(1)=1$ from $g(1,t)=1/(1-t)$; parity from
  $g(-x,-t)=g(x,t)$; $P_{2n}(0)$ from $g(0,t)$ (Arfken et al.,
  eqs. 15.7–15.11, pp. 716–717; Riley et al., p. 585).
* Legendre norm by integrating $g^2$ (Arfken et al., eqs. 15.33–15.38; Riley
  et al., Exercise 18.4, p. 641).
* The physical reading of the Legendre generating function as the inverse
  distance between two points: see
  [Legendre expansion of the inverse distance](/results/legendre-expansion-of-inverse-distance.md).
* Bessel: $J_n(-x)=(-1)^nJ_n(x)$, the addition theorem
  $J_n(u+v)=\sum_sJ_s(u)J_{n-s}(v)$ and the Jacobi–Anger expansion
  $e^{i\rho\cos\varphi}=\sum_mi^mJ_m(\rho)e^{im\varphi}$, all set as
  exercises (Arfken et al., Exercises 14.1.2–14.1.5, pp. 654–655); the
  integral representation $J_n=\frac1\pi\int_0^\pi\cos(n\theta-x\sin\theta)d\theta$
  (Riley et al., pp. 613–614; Arfken et al., eqs. 14.16–14.18, p. 647).

Recurrences derived this way are collected on
[three-term recurrences](/results/three-term-recurrences.md).

# Citations

1. [Arfken et al. (2013)](/sources/arfken-2013.md), §12.1, eqs. 12.19–12.27, pp. 555–559; eqs. 14.2, 15.6, 15.82, 18.2, 18.49, 18.60, 18.85–18.91; Exercises 14.1.2–14.1.5, pp. 654–655.
2. [Riley et al. (2006)](/sources/riley-2006.md), eqs. 18.15–18.21, pp. 584–585; eqs. 18.40, 18.63–18.64, 18.98, 18.114, 18.123, 18.133.
