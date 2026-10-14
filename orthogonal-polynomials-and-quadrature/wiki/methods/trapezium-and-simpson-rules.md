---
type: Method
title: "Trapezium and Simpson rules"
description: "The equally spaced composite rules that approximate f by straight lines or parabolas on strips of width h: trapezium error about (b-a)h^2<f''>/12, exact for linear f; Simpson error about (b-a)h^4<f''''>/180, using an even number of strips; derived by Taylor expansion about strip midpoints."
status: established
aliases: [trapezoidal rule, composite trapezium rule, Simpson's rule, Newton–Cotes rules, equally spaced quadrature]
tags: [quadrature, equally-spaced, error-estimate]
timestamp: 2026-10-14T00:00:00Z
---

# Trapezium and Simpson rules

## Setting

$[a,b]$ is divided into $N$ strips of width $h=(b-a)/N$ with points
$x_i=a+ih$, $i=0,\dots,N$, $f_i=f(x_i)$ and strip midpoints $x_{i+1/2}$. The
exact strip integral, expanded about the midpoint, is
$$\int_{-h/2}^{h/2}f(x_{i+1/2}+y)\,dy=\sum_{k\ \mathrm{even}}f^{(k)}_{i+1/2}\,\frac{2}{(k+1)!}\Big(\frac h2\Big)^{k+1},$$
in which only even derivatives survive
([Riley et al. (2006)](/sources/riley-2006.md), §27.4, eqs. 27.34–27.35,
pp. 1000–1001). Riley et al. present these rules as the "more elementary
methods" before Gaussian integration and do not use the name Newton–Cotes;
the bundle groups them under that name as the equally spaced contrast to
[Gaussian quadrature](/methods/gaussian-quadrature.md).

## Trapezium rule

$$I\approx\frac h2\big(f_0+2f_1+\dots+2f_{N-1}+f_N\big),$$
exact only for linear $f$. Expanding $f_i$, $f_{i+1}$ about $x_{i+1/2}$ gives
the strip error $\Delta A_i=A_i^{\mathrm{estim}}-A_i^{\mathrm{exact}}\approx\frac1{12}h^3f''_{i+1/2}$
and the total
$$E[f]\approx\frac{1}{12}(b-a)\,h^2\,\langle f''\rangle$$
with $\langle f''\rangle$ an average over $[a,b]$ (Riley et al., §27.4.1,
eqs. 27.36–27.38, pp. 1002–1003). The worked example
$\int_0^2(x^2-3x+4)\,dx$ with $h=0.5$ gives $4.75$ against $4\tfrac23$: the
error $\tfrac1{12}$ is predicted exactly, because the Taylor series of a
quadratic terminates (pp. 1003–1004).

## Simpson's rule

Strips are taken in pairs ($N$ even) and $f$ is replaced on each pair by
the parabola through $f_{i-1},f_i,f_{i+1}$, giving
$A_i\approx\frac h3(f_{i-1}+4f_i+f_{i+1})$ and
$$I\approx\frac h3\Big(f_0+f_N+4\sum_{m\ \mathrm{odd}}f_m+2\sum_{m\ \mathrm{even}}f_m\Big),\qquad E[f]\approx\frac{(b-a)}{180}\,h^4\,\langle f^{(4)}\rangle$$
(Riley et al., §27.4.2, eqs. 27.39–27.40, p. 1004; the error "can be shown"
by the trapezium-rule procedure and is not derived). The coefficients of
the local parabola never need to be computed (p. 1004).

## Comparison with Gaussian rules

With three function evaluations on $\int_0^1(1+x^2)^{-1}dx=0.78540$,
trapezium gives $0.7750$, Simpson $0.7833$, Gauss–Legendre $0.78527$ (Riley
et al., p. 1007; see
[Gauss–Legendre quadrature](/methods/gauss-legendre-quadrature.md)). The
book calls the trapezium rule exact for linear and Simpson's rule for
quadratic $f$ (p. 1005), whereas the 3-point Gauss rule is stated exact to
degree 5. Simpson's rule is in fact exact for cubics, since its leading
error involves $f^{(4)}$; Riley et al. say only that the parabolic rule is
exact for quadratic $f$ (p. 1005), so the cubic exactness is the compiler's
reading of their error term.

[Arfken et al. (2013)](/sources/arfken-2013.md) do not treat these rules in
the sections read.

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §27.4, eqs. 27.34–27.40, pp. 1000–1005; worked examples pp. 1003–1004, 1007.
