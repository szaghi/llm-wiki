---
type: Method
title: "Gaussian quadrature"
description: "Quadrature with nodes at the zeros of the degree-n polynomial orthogonal for the weight omega and weights chosen accordingly, integrating omega times polynomials of degree up to 2n-1 exactly; the general idea and the Legendre, Chebyshev, Laguerre and Hermite rules as Riley et al. present them, with what the founding sources prove and what they only assert."
status: established
aliases: [Gauss quadrature, Gaussian integration, Gauss–Laguerre quadrature, Gauss–Hermite quadrature, Christoffel numbers]
tags: [quadrature, gauss, nodes-and-weights, exactness]
timestamp: 2026-10-14T00:00:00Z
---

# Gaussian quadrature

## Idea

Equally spaced rules such as the
[trapezium and Simpson rules](/methods/trapezium-and-simpson-rules.md)
reproduce $f$ by linear or quadratic pieces and are exact only for such $f$.
Raising the interpolation degree raises the accuracy, but "the same effect
can be achieved with less effort by not insisting upon equally spaced points"
([Riley et al. (2006)](/sources/riley-2006.md), §27.4.3, p. 1005). A Gaussian
rule for the weight $\omega$ on $[a,b]$,
$$\int_a^bf(x)\,\omega(x)\,dx\approx\mathcal Q_n[f]=\sum_{j=1}^nw_j\,f(x_j),$$
takes as nodes $x_j$ the zeros of $p_n$, the degree-$n$ member of the
polynomials [orthogonal with respect to $\omega$](/definitions/orthogonal-polynomials.md),
and as weights the integrals of the Lagrange interpolant through those
nodes. Riley et al. describe the method as "mimicking the given function with
a weighted sum of mutually orthogonal polynomials" and state that the full
analysis "is too long to be given in full here" (p. 1005).

## Exactness and error

For Gauss–Legendre, Riley et al. state that "because of the particular
properties of Legendre polynomials, it can be shown that" the rule
"integrates exactly any polynomial of degree up to $2n-1$", and that the
error "is of the order of the $2n$th derivative" of the integrand
(pp. 1006–1007). Both statements are asserted, not proved, and the error is
not given as a formula; for the other weights the exactness is implied but
not stated. Weights, nodes and "quantitative estimates of the error" are
referred to books on numerical analysis and to Abramowitz and Stegun, from
which the tables are taken (p. 1009 and footnote).
[Arfken et al. (2013)](/sources/arfken-2013.md) do not treat Gaussian
quadrature in the sections read; their only mention is the motivation of an
exercise on the zeros of $P_n$ (Exercise 15.1.18, p. 724).

The reality, simplicity and interior location of the zeros of $p_n$, on which
the construction depends, are proved in neither source for a general
weight; Arfken et al. set the Legendre case as an exercise (see
[Legendre polynomials](/definitions/legendre-polynomials.md)), and the
Chebyshev nodes are explicit.

## The rules in Riley et al.

| Rule | $[a,b]$, $\omega$ | Nodes | Weights | Locator |
|---|---|---|---|---|
| Gauss–Legendre | $[-1,1]$, $1$ | zeros of $P_n$ | $\dfrac{2}{(1-x_j^2)[P_n'(x_j)]^2}$ | eqs. 27.41–27.43, Table 27.8, pp. 1006–1008 |
| Gauss–Chebyshev I | $[-1,1]$, $(1-x^2)^{-1/2}$ | $\cos\frac{(j-1/2)\pi}{n}$ | $\frac\pi n$ | eqs. 27.44–27.45, p. 1009 |
| Gauss–Chebyshev II | $[-1,1]$, $(1-x^2)^{1/2}$ | $\cos\frac{j\pi}{n+1}$ | $\frac{\pi}{n+1}\sin^2\frac{j\pi}{n+1}$ | eqs. 27.46–27.47, p. 1009 |
| Gauss–Laguerre | $[0,\infty)$, $e^{-x}$ | zeros of $L_n$ | tabulated | Table 27.9, p. 1010 |
| Gauss–Hermite | $(-\infty,\infty)$, $e^{-x^2}$ | zeros of $H_n$ | tabulated | Table 27.9, p. 1010 |

Details of the first three are on
[Gauss–Legendre quadrature](/methods/gauss-legendre-quadrature.md) and
[Gauss–Chebyshev quadrature](/methods/gauss-chebyshev-quadrature.md).

**Gauss–Laguerre and Gauss–Hermite.** A semi-infinite integrand with a
factor $e^{-\alpha x}$ is mapped by a change of variable to the weight
$e^{-x}$, so that "the handling of the exponential factor in the integrand is
effectively carried out analytically"; if the remaining factor is well
approximated by low-degree polynomials, "a modest number of points" suffices
(p. 1005). An explicit factor $e^{-\beta x^2}$ on $(-\infty,\infty)$ calls
for the Hermite rule (p. 1005). Table 27.9 gives ten-digit nodes and weights
for $n=2$–$7$ (Laguerre) and $n=2$–$9$ (Hermite), e.g. Laguerre $n=2$:
$x_j=0.58578\,64376,\ 3.41421\,35624$, $w_j=0.85355\,33906,\ 0.14644\,66094$;
Hermite $n=2$: $x_j=\pm0.70710\,67812$, $w_j=0.88622\,69255$ (p. 1010).
Riley et al. also describe, for integrals to $\infty$, the substitutions
$t=1/x$ (integrand decaying faster than $x^{-2}$) and $x=-\alpha^{-1}\ln\alpha t$
(asymptotic form $g(x)e^{-\alpha x}$), which map to a finite range, and say
that for linear or quadratic exponential decay the Gaussian rules are better
(pp. 1001–1002).

## Not in the founding sources

Gauss–Radau and Gauss–Lobatto rules, Gauss–Jacobi rules, the computation of
nodes and weights from the recurrence coefficients, and error formulae with
explicit constants are absent from both founding sources (registry symbols
reserved). They are left for sources that treat them.

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §27.4 (intro), pp. 1000–1002; §27.4.3, eqs. 27.41–27.47, pp. 1005–1010; Tables 27.8–27.9.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), Exercise 15.1.18, p. 724 (absence of the topic in the sections read).
