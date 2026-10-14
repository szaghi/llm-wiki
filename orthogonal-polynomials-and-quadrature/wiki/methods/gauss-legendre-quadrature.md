---
type: Method
title: "Gauss–Legendre quadrature"
description: "The n-point Gaussian rule for unit weight on [-1,1]: nodes at the zeros of P_n, weights 2/((1-x_j^2)P_n'(x_j)^2), stated exact for polynomials of degree up to 2n-1; derivation through the Lagrange interpolant, the affine map from [a,b], tabulated nodes and weights, and Riley's worked comparison with the trapezium and Simpson rules."
status: established
aliases: [Gauss-Legendre integration, Gauss–Legendre rule]
tags: [quadrature, gauss, legendre, nodes-and-weights]
timestamp: 2026-10-14T00:00:00Z
---

# Gauss–Legendre quadrature

## Rule

Map $[a,b]$ to $[-1,1]$ with $z=(2x-b-a)/(b-a)$:
$\int_a^bf(x)\,dx=\frac{b-a}{2}\int_{-1}^1g(z)\,dz$, $g(z)=f(x)$. The
$n$-point rule is
$$\int_{-1}^1g(x)\,dx\approx\sum_{j=1}^nw_j\,g(x_j),\qquad P_n(x_j)=0,\qquad w_j=\frac{2}{(1-x_j^2)\,[P_n'(x_j)]^2}$$
([Riley et al. (2006)](/sources/riley-2006.md), §27.4.3, eqs. 27.41–27.43,
p. 1006; weight formula checked on the page image).

## Derivation (Riley et al.)

The integrand is replaced by its degree-$(n-1)$ interpolant through the
nodes,
$$G(x)=\sum_{j=1}^n\frac{P_n(x)}{(x-x_j)\,P_n'(x_j)}\,g(x_j),$$
which matches $g$ at each node because
$\lim_{x\to x_k}P_n(x)/[(x-x_j)P_n'(x_j)]=\delta_{jk}$. The factor
$P_n(x)/[(x-x_j)P_n'(x_j)]$ is the Lagrange cardinal polynomial $\ell_j(x)$
of the nodes, so
$$w_j=\int_{-1}^1\ell_j(x)\,dx=\frac{1}{P_n'(x_j)}\int_{-1}^1\frac{P_n(x)}{x-x_j}\,dx,$$
which "can be shown, using the properties of Legendre polynomials", to equal
the closed form above (p. 1006). The reduction to the closed form is not
carried out. Riley et al. then state, without proof, that "because of the
particular properties of Legendre polynomials … (27.43) integrates exactly
any polynomial of degree up to $2n-1$", and that the error "is of the order
of the $2n$th derivative of $g$", so the rule is good for smooth $g$
(pp. 1006–1007).

**Remark on the argument (compiler's note).** The interpolation step alone
guarantees exactness only to degree $n-1$; the extra $n$ degrees come from
the orthogonality of $P_n$ to all polynomials of lower degree, which is the
"particular property" the text leaves unstated. The orthogonality is on
[Legendre polynomials](/definitions/legendre-polynomials.md); the standard
argument connecting the two is not in either founding source.

## Example and tabulation

For $n=3$: $P_3=\tfrac12(5x^3-3x)$ has zeros $0,\pm0.77460$, and the weight
formula gives $w=2/[1\cdot(-\tfrac32)^2]=\tfrac89$ at $0$ and
$2/[(1-0.6)(\tfrac62)^2]=\tfrac59$ at $\pm0.77460$ (Riley et al., p. 1007).
Table 27.8 gives ten-digit nodes and weights for $n=2$–$10$, $12$ and $20$,
e.g. $n=2$: $\pm0.57735\,02692$, $w=1$; $n=4$: $\pm0.33998\,10436$
($w=0.65214\,51549$), $\pm0.86113\,63116$ ($w=0.34785\,48451$) (p. 1008),
taken from Abramowitz and Stegun (footnote, p. 1009).

**Worked comparison** (Riley et al., p. 1007). For
$\int_0^1(1+x^2)^{-1}dx=\pi/4=0.78540$, three function evaluations give:
trapezium $0.7750$, Simpson $0.7833$, 3-point Gauss–Legendre $0.78527$. The
book concludes only that "a compromise has to be struck between the
accuracy … and the calculational labour".

## Relation to other pages

The rule is the $\omega=1$ case of
[Gaussian quadrature](/methods/gaussian-quadrature.md). Its nodes are the
zeros of $P_n$; that they are real, simple and interior is set by Arfken et
al. as an exercise motivated by this rule (Exercise 15.1.18, p. 724). The
Gauss–Lobatto and Gauss–Radau variants, which include one or both endpoints,
are not treated by either founding source.

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §27.4.3, eqs. 27.41–27.43, pp. 1005–1009; Table 27.8, p. 1008.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), Exercise 15.1.18, p. 724.
