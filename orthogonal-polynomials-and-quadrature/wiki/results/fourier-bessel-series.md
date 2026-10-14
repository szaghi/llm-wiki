---
type: Result
title: "Fourier–Bessel series"
description: "For fixed order nu, the functions J_nu(alpha_{nu,k} rho/a), k=1,2,..., are orthogonal on [0,a] with weight rho and norm (a^2/2) J_{nu+1}^2(alpha_{nu,k}); the Lommel-type boundary identity behind it, the Dirichlet and Neumann variants, and the expansion coefficients."
status: established
aliases: [Bessel series, Bessel function orthogonality, Lommel integrals, Dini series]
tags: [bessel, orthogonality, expansion, zeros]
timestamp: 2026-10-14T00:00:00Z
---

# Fourier–Bessel series

## The boundary identity

$f=J_\nu(kx)$ and $g=J_\nu(k'x)$ satisfy
$x^2f''+xf'+(k^2x^2-\nu^2)f=0$ and the same with $k'$, so
$\frac{d}{dx}\big[x(fg'-gf')\big]=(k^2-k'^2)\,x\,fg$ and
$$\int_a^bx\,J_\nu(kx)J_\nu(k'x)\,dx=\frac{\Big[x\big(k'J_\nu(kx)J_\nu'(k'x)-kJ_\nu(k'x)J_\nu'(kx)\big)\Big]_a^b}{k^2-k'^2}$$
([Riley et al. (2006)](/sources/riley-2006.md), §18.5.3, eqs. 18.84–18.88,
pp. 608–609; [Arfken et al. (2013)](/sources/arfken-2013.md), §14.2,
eqs. 14.41–14.43, p. 661, as a case of their Sturm–Liouville identity, and
Exercise 14.2.1, p. 665, where it and the normalization integral are called
the first and second Lommel integrals). The weight is $x$, from the
Sturm–Liouville form with $p=x$; there is no "natural" interval, so
orthogonality needs boundary conditions, and the boundary term vanishes
automatically at $x=0$ (Riley et al., p. 608; Arfken et al., p. 661 and
footnote 3, for $\nu\ge-1$).

## Orthogonality and normalization on $[0,a]$

Choosing $k=\alpha_{\nu,i}/a$, $k'=\alpha_{\nu,j}/a$ (Dirichlet condition
$J_\nu(ka)=0$) kills the boundary term:
$$\int_0^a\rho\,J_\nu\Big(\alpha_{\nu,i}\frac\rho a\Big)J_\nu\Big(\alpha_{\nu,j}\frac\rho a\Big)\,d\rho=\frac{a^2}{2}\big[J_{\nu+1}(\alpha_{\nu,i})\big]^2\delta_{ij}.$$
The normalization comes from the limit $k'\to k$ by l'Hôpital's rule
(Arfken et al., eqs. 14.44–14.46, pp. 661–663) or by direct integration,
$\int J_\nu^2(kx)\,x\,dx=\tfrac12\big[(x^2-\nu^2/k^2)J_\nu^2(kx)+x^2J_\nu'^2(kx)\big]$
(Riley et al., eq. 18.89, p. 610), together with $J_\nu'(\alpha_{\nu,i})=-J_{\nu+1}(\alpha_{\nu,i})$
at a zero. All members share the order $\nu$ and differ in the scale of the
argument; the weight $\rho$ is uniform weight over the disc of radius $a$
(Arfken et al., p. 662, Fig. 14.6). Arfken et al. state the results for
$\nu>-1$ (eq. 14.47; Exercise 14.2.3); Riley et al. for "a given
(non-negative) order $\nu$" (p. 610).

**Neumann variant.** With $k=\beta_{\nu,j}/a$, zeros of $J_\nu'$, the set is
again orthogonal, with norm
$\frac{a^2}2\big(1-\nu^2/\beta_{\nu,j}^2\big)\big[J_\nu(\beta_{\nu,j})\big]^2$
(Arfken et al., Exercises 14.2.2 and 14.2.5, pp. 665–666; Riley et al. note
the derivative condition, p. 609).

## Expansion

$$f(\rho)=\sum_{j=1}^\infty c_j\,J_\nu\Big(\alpha_{\nu,j}\frac\rho a\Big),\qquad c_j=\frac{2}{a^2\big[J_{\nu+1}(\alpha_{\nu,j})\big]^2}\int_0^af(\rho)\,J_\nu\Big(\alpha_{\nu,j}\frac\rho a\Big)\rho\,d\rho,$$
assuming completeness, which neither book proves (Arfken et al.,
eqs. 14.47–14.48, p. 663, "If we assume that the set … is complete";
Riley et al., eqs. 18.90–18.91, p. 610, for functions obeying the Dirichlet
conditions, indexed from $n=0$ with $\alpha_n$ the scale factors). The
boundary condition need only be imposed at $\rho=a$ (Riley et al., p. 610).
Arfken et al. use the double trigonometric–Bessel series for the potential
in a cylinder (Example 14.2.1, pp. 663–665) and set as exercises the
Parseval relation $\int_0^1f^2x\,dx=\tfrac12\sum_na_n^2J_{m+1}^2(\alpha_{m,n})$
and the sum $\sum_n\alpha_{m,n}^{-2}=1/[4(m+1)]$ (Exercises 14.2.7–14.2.8,
p. 666).

The spherical analogue, with weight $r^2$ and the zeros of $j_\ell$, is on
[spherical Bessel functions](/definitions/spherical-bessel-functions.md).

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §18.5.3, eqs. 18.84–18.91, pp. 608–611.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §14.2, eqs. 14.41–14.56, pp. 661–665; Exercises 14.2.1–14.2.8, pp. 665–666.
