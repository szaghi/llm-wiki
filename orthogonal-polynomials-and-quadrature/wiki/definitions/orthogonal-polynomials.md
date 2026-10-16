---
type: Definition
title: "Orthogonal polynomials with respect to a weight function"
description: "A sequence of polynomials p_n of exact degree n with zero weighted inner product on an interval; defines weight function, norm h_n, the orthogonal expansion and its coefficients, and the Sturm–Liouville origin of the classical families."
status: established
aliases: [orthogonal polynomial sequence, weight function, orthogonal expansion, generalized Fourier series]
tags: [orthogonality, weight-function, expansion, sturm-liouville]
timestamp: 2026-10-16T00:00:00Z
---

# Orthogonal polynomials with respect to a weight function

## Definition

Let $\omega(x)>0$ on $(a,b)$, the **weight function**, with
$\langle f,g\rangle_\omega=\int_a^b f(x)g(x)\,\omega(x)\,dx$. A sequence
$p_0,p_1,p_2,\dots$ with $p_n$ a polynomial of exact degree $n$ is
**orthogonal** with respect to $\omega$ on $[a,b]$ when
$$\langle p_n,p_m\rangle_\omega=h_n\,\delta_{nm},$$
with $h_n>0$ the **norm constant**. Riley et al. state the definition in
exactly this form for the polynomials on which Gaussian quadrature rests
([Riley et al. (2006)](/sources/riley-2006.md), §27.4.3, p. 1005, with their
$F_n$, $w$, $k_n$). Orthogonality fixes each $p_n$ only up to a constant
factor; each classical family fixes it by a **standardization**
($P_n(1)=1$, $L_n(0)=1$, leading coefficient $2^n$ for $H_n$, …), and the
standardization determines $h_n$ and every recurrence coefficient
([Arfken et al. (2013)](/sources/arfken-2013.md), §12.1, p. 555 on the scale
factor $c_n$; §15.1, p. 716; §18.3, p. 890). Arfken et al. note that several
families are standardized differently by different authors (Laguerre,
§18.3, p. 890; Chebyshev, §18.4, p. 900).

## Origin in Sturm–Liouville problems

Both sources obtain the classical families as the polynomial eigenfunctions
of a second-order equation
$$p(x)\,y''+q(x)\,y'+\lambda y=0,\qquad p(x)=\alpha x^2+\beta x+\gamma,\quad q(x)=\mu x+\nu,$$
which has a polynomial solution of degree $n$ only for
$\lambda_n=-n(n-1)\alpha-n\mu$ (Arfken et al., §12.1, eqs. 12.1–12.5,
pp. 551–552; here $\alpha,\beta,\gamma,\mu,\nu$ are local coefficients, not
registry symbols). Multiplying by the weight
$$\omega(x)=\frac{1}{p(x)}\exp\!\int^x\frac{q(s)}{p(s)}\,ds$$
makes the equation self-adjoint, $(\omega p\,y')'+\lambda\omega y=0$ (eqs.
12.6–12.8, p. 552), and orthogonality on $[a,b]$ with weight $\omega$
follows when the boundary terms $\omega p\,(y_ny_m'-y_my_n')$ vanish at both
ends. Riley et al. derive the orthogonality of each family the same way, from
the Sturm–Liouville forms of their §17.4, and also prove it directly from
the Rodrigues formulae ([Riley et al. (2006)](/sources/riley-2006.md),
§§18.1.2, 18.2.2, 18.4.1, 18.5.3, 18.7.1, 18.8.1, 18.9.1). The general
Rodrigues formula that this setting yields is on
[Rodrigues formula](/results/rodrigues-formula.md).

## The classical families

| Family | $[a,b]$ | $\omega(x)$ | $h_n$ | Page |
|---|---|---|---|---|
| Legendre $P_n$ | $[-1,1]$ | $1$ | $\frac{2}{2n+1}$ | [Legendre polynomials](/definitions/legendre-polynomials.md) |
| Chebyshev $T_n$ | $[-1,1]$ | $(1-x^2)^{-1/2}$ | $\pi$ ($n=0$), $\pi/2$ ($n\ge1$) | [Chebyshev polynomials](/definitions/chebyshev-polynomials.md) |
| Chebyshev $U_n$ | $[-1,1]$ | $(1-x^2)^{1/2}$ | $\pi/2$ | [Chebyshev polynomials](/definitions/chebyshev-polynomials.md) |
| Laguerre $L_n$ | $[0,\infty)$ | $e^{-x}$ | $1$ | [Laguerre polynomials](/definitions/laguerre-polynomials.md) |
| associated Laguerre $L_n^{(m)}$ | $[0,\infty)$ | $x^me^{-x}$ | $\frac{(n+m)!}{n!}$ | [Laguerre polynomials](/definitions/laguerre-polynomials.md) |
| Hermite $H_n$ | $(-\infty,\infty)$ | $e^{-x^2}$ | $2^nn!\sqrt\pi$ | [Hermite polynomials](/definitions/hermite-polynomials.md) |

All entries are stated in both sources (Riley et al. eqs. 18.11, 18.62,
p. 600, 18.113, 18.122, 18.132; Arfken et al. eqs. 15.38, 18.15, 18.55,
18.71, 18.116, 18.118). The Gegenbauer polynomials $C_n^{(\lambda)}$ appear
in Arfken et al. only through their generating function (see
[Chebyshev polynomials](/definitions/chebyshev-polynomials.md)); the Jacobi
polynomials $P_n^{(\alpha,\beta)}$ are in neither founding source.

Associated Legendre functions with fixed $m$ are orthogonal in $\ell$ with
unit weight, but they are polynomials only for even $m$; the polynomial
factor $P_\ell^m/(1-x^2)^{m/2}$ is orthogonal with weight $(1-x^2)^m$
([Arfken et al. (2013)](/sources/arfken-2013.md), eq. 15.106, p. 748). See
[associated Legendre functions](/definitions/associated-legendre-functions.md).
Bessel functions are orthogonal in the scale of their argument, not in their
order: see [Fourier–Bessel series](/results/fourier-bessel-series.md).
On the unit disc, the radial Zernike polynomials are $r^m$ times a polynomial
in $r^2$; Panici et al. call them shifted Jacobi polynomials and use them, with
$\cos m\phi$ and $\sin m\phi$, as a spectral basis that is regular at the
origin ([Panici et al. (2023)](/sources/panici-2023.md), §3.2, eqs. 3.18–3.21,
p. 7). See [Zernike polynomials](/definitions/zernike-polynomials.md).

## Orthogonal expansion

A function on $[a,b]$ is expanded as $f=\sum_n c_np_n$ with
$$c_n=\frac{\langle f,p_n\rangle_\omega}{h_n},$$
obtained by multiplying by $p_m\omega$ and integrating term by term. Riley
et al. state the expansion for "any reasonable function", meaning one that
obeys the Dirichlet conditions of their chapter 12, and appeal to the
completeness of Sturm–Liouville eigenfunctions without proving it for any
family ([Riley et al. (2006)](/sources/riley-2006.md), eqs. 18.13–18.14,
p. 583, and the expansions in §§18.4.1, 18.7.1, 18.8.1, 18.9.1). Arfken et
al. add that orthogonality makes the expansion unique, so that a truncated
Legendre series rearranged in powers of $x$ is a unique polynomial
([Arfken et al. (2013)](/sources/arfken-2013.md), §15.2, eqs. 15.39–15.40,
p. 726). Neither founding source states a convergence rate for any
orthogonal expansion; Arfken et al.'s only accuracy statement is the
qualitative minimax remark for Chebyshev series (see
[Chebyshev polynomials](/definitions/chebyshev-polynomials.md)). Panici et
al. state, citing Boyd (2001) and without proof, that a spectral
representation of a smooth solution converges exponentially in its
resolution, and measure exponential convergence in the radial degree of a
Zernike basis
([Panici et al. (2023)](/sources/panici-2023.md), §5.2, Table 1, Fig. 8,
pp. 12–14; see [Zernike polynomials](/definitions/zernike-polynomials.md)).

**Gram–Schmidt.** Arfken et al. set as an exercise that Gram–Schmidt
orthogonalization of $1,x,x^2,\dots$ with unit weight on $[-1,1]$ gives
multiples of the Legendre polynomials (Exercise 15.2.2, p. 731); the text
does not develop the construction for a general weight.

## What the sources do not contain

Neither founding source states the general three-term recurrence of an
arbitrary orthogonal polynomial sequence, the interlacing or simplicity of
the zeros of a general $p_n$, or the Christoffel–Darboux formula. Each
family's recurrence is stated separately (see
[three-term recurrences](/results/three-term-recurrences.md)), and the
reality and location of the zeros are used only for Gaussian quadrature
(see [Gaussian quadrature](/methods/gaussian-quadrature.md)).

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §27.4.3, p. 1005; §18.1.2, eqs. 18.12–18.14, pp. 583–584; §§18.4.1, 18.7.1, 18.8.1, 18.9.1.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §12.1, eqs. 12.1–12.8, pp. 551–552; §15.2, eqs. 15.31–15.40, pp. 724–726; eq. 15.106, p. 748; §§18.1, 18.3, 18.4.
3. [Panici et al. (2023)](/sources/panici-2023.md), §3.2, eqs. 3.18–3.21, p. 7; §5.2, Table 1, Fig. 8, pp. 12–14.
