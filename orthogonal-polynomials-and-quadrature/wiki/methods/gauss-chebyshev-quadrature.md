---
type: Method
title: "Gauss–Chebyshev quadrature"
description: "Gaussian rules for the weights (1-x^2)^{-1/2} and (1-x^2)^{1/2} on [-1,1], with closed-form nodes cos((j-1/2)pi/n), cos(j pi/(n+1)) and weights pi/n, pi/(n+1) sin^2(j pi/(n+1)); the endpoint singularity is absorbed by the weight."
status: established
aliases: [Gauss-Chebyshev integration, Chebyshev–Gauss quadrature]
tags: [quadrature, gauss, chebyshev, nodes-and-weights]
timestamp: 2026-10-14T00:00:00Z
---

# Gauss–Chebyshev quadrature

## First kind

For integrands with a factor $(1-x^2)^{-1/2}$,
$$\int_{-1}^1\frac{f(x)}{\sqrt{1-x^2}}\,dx\approx\sum_{j=1}^nw_jf(x_j),\qquad x_j=\cos\frac{(j-\frac12)\pi}{n},\qquad w_j=\frac\pi n,\quad j=1,\dots,n,$$
the nodes being the zeros of $T_n$
([Riley et al. (2006)](/sources/riley-2006.md), §27.4.3, eqs. 27.44–27.45,
p. 1009; checked on the page image). "For any given $n$, all points are
weighted equally and … no special action is required to deal with the
integrable singularities at $x=\pm1$; they are dealt with automatically
through the weight function" (p. 1009). That the $x_j$ are the zeros of
$T_n$ follows from $T_n(\cos\theta)=\cos n\theta$ (see
[Chebyshev polynomials](/definitions/chebyshev-polynomials.md)); the book
states it without derivation.

## Second kind

For integrands with a factor $(1-x^2)^{1/2}$, based on $U_n$,
$$\int_{-1}^1f(x)\sqrt{1-x^2}\,dx\approx\sum_{j=1}^nw_jf(x_j),\qquad x_j=\cos\frac{j\pi}{n+1},\qquad w_j=\frac{\pi}{n+1}\sin^2\frac{j\pi}{n+1}$$
(Riley et al., eqs. 27.46–27.47, p. 1009). The nodes are the zeros of
$U_n(\cos\theta)=\sin(n+1)\theta/\sin\theta$ (compiler's identification;
the book says only that the rule is "based on" $U_n$).

## Scope and evidence

Riley et al. present both rules as further Gaussian procedures, give the
node and weight formulae "compactly for all $n$", and offer no proof of the
weights and no error statement for them (p. 1009); the exactness of the
general Gaussian rule is asserted on
[Gaussian quadrature](/methods/gaussian-quadrature.md). They motivate the
Chebyshev polynomials themselves by this rule (§18.4.1, p. 599).
[Arfken et al. (2013)](/sources/arfken-2013.md) give the orthogonality
integrals with these weights (eqs. 18.116, 18.118, p. 907) but no quadrature.
The rule is single-source.

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §27.4.3, eqs. 27.44–27.47, p. 1009; §18.4.1, p. 599.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §18.4, eqs. 18.116, 18.118, p. 907 (orthogonality only).
