---
type: Definition
title: "Chebyshev polynomials"
description: "The polynomials T_n(cos theta)=cos(n theta) and U_n(cos theta)=sin((n+1)theta)/sin(theta), orthogonal on [-1,1] with weights (1-x^2)^{-1/2} and (1-x^2)^{1/2}; trigonometric and explicit forms, special values, the companion non-polynomial solutions V_n and W_n, their origin as Gegenbauer polynomials, and the equal-ripple (minimax) property used in numerical analysis."
status: established
aliases: [Chebyshev polynomials of the first kind, Chebyshev polynomials of the second kind, type I and type II Chebyshev polynomials, Tschebyscheff polynomials]
tags: [chebyshev, classical-family, orthogonality, approximation, gegenbauer]
timestamp: 2026-10-14T00:00:00Z
---

# Chebyshev polynomials

## Definition

Chebyshev's equation $(1-x^2)\,y''-x\,y'+n^2y=0$ becomes
$d^2y/d\theta^2+n^2y=0$ under $x=\cos\theta$, so its solutions for integer
$n\ge0$ are
$$T_n(x)=\cos(n\arccos x),\qquad V_n(x)=\sin(n\arccos x).$$
$T_n$ is a polynomial of degree $n$, the **Chebyshev polynomial of the first
kind**; $V_n$ is not a polynomial. The second-kind polynomials are
$$U_n(x)=\frac{V_{n+1}(x)}{(1-x^2)^{1/2}}=\frac{\sin(n+1)\theta}{\sin\theta},\qquad W_n(x)=\frac{T_{n+1}(x)}{(1-x^2)^{1/2}}=\frac{\cos(n+1)\theta}{\sin\theta},$$
with $U_n$ a polynomial of degree $n$ solving
$(1-x^2)y''-3xy'+n(n+2)y=0$ and $W_n$ not a polynomial
([Riley et al. (2006)](/sources/riley-2006.md), §18.4, eqs. 18.54–18.59,
pp. 595–598; [Arfken et al. (2013)](/sources/arfken-2013.md), §18.4,
eqs. 18.97–18.98, 18.104–18.110, pp. 903–904). Both books use the same
$T_n,U_n,V_n,W_n$. The general solution of Chebyshev's equation is
$c_1T_n+c_2\sqrt{1-x^2}\,U_{n-1}$ for $n\ge1$ and $c_1+c_2\arcsin x$ for
$n=0$ (Riley et al., p. 597). Both books stress that the equation is rare in
physics but that its solutions matter in numerical analysis (Riley et al.,
pp. 596, 599; Arfken et al., p. 899).

First members (both books; Arfken et al. Table 18.4 to $n=6$, p. 901):
$$T_0=1,\ T_1=x,\ T_2=2x^2-1,\ T_3=4x^3-3x;\qquad U_0=1,\ U_1=2x,\ U_2=4x^2-1,\ U_3=8x^3-4x.$$

Explicit forms. From $T_n+iV_n=(x+i\sqrt{1-x^2})^n$,
$T_n=x^n-\binom n2x^{n-2}(1-x^2)+\binom n4x^{n-4}(1-x^2)^2-\cdots$ (Riley et
al., eq. 18.56, p. 596; Arfken et al., eq. 18.112, p. 904). As power series
in $2x$ (Arfken et al., eqs. 18.114–18.115, p. 905):
$$T_n=\frac n2\sum_{m=0}^{\lfloor n/2\rfloor}(-1)^m\frac{(n-m-1)!}{m!\,(n-2m)!}(2x)^{n-2m}\ (n\ge1),\qquad U_n=\sum_{m=0}^{\lfloor n/2\rfloor}(-1)^m\frac{(n-m)!}{m!\,(n-2m)!}(2x)^{n-2m}.$$

## Special values and derivatives

$T_n(\pm1)=(\pm1)^n$, $T_{2n}(0)=(-1)^n$, $T_{2n+1}(0)=0$;
$U_n(1)=n+1$, $U_n(-1)=(-1)^n(n+1)$, $U_{2n}(0)=(-1)^n$, $U_{2n+1}(0)=0$;
both have parity $(-1)^n$ (Riley et al., pp. 597–598; Arfken et al.,
eqs. 18.100–18.101, p. 903). The trigonometric forms give the derivative
relations (Riley et al., p. 602):
$$T_n'(x)=n\,U_{n-1}(x),\qquad (1-x^2)\,U_n'(x)=x\,U_n(x)-(n+1)\,T_{n+1}(x),$$
and the cross relations $T_n=U_n-xU_{n-1}$,
$(1-x^2)U_n=xT_{n+1}-T_{n+2}$ (eqs. 18.71–18.72). Arfken et al. give
$(1-x^2)T_n'=-nxT_n+nT_{n-1}$ and $(1-x^2)U_n'=-nxU_n+(n+1)U_{n-1}$
(eqs. 18.95–18.96, pp. 901–902). The three-term recurrence
$T_{n+1}=2xT_n-T_{n-1}$ (same for $U_n$) is on
[three-term recurrences](/results/three-term-recurrences.md); Rodrigues
formulae and generating functions are on
[Rodrigues formula](/results/rodrigues-formula.md) and
[generating functions](/results/generating-functions.md).

## Orthogonality

$$\int_{-1}^1\frac{T_nT_m}{\sqrt{1-x^2}}\,dx=\begin{cases}0&n\ne m\\ \pi&n=m=0\\ \pi/2&n=m\ge1\end{cases},\qquad \int_{-1}^1U_nU_m\sqrt{1-x^2}\,dx=\frac\pi2\,\delta_{nm},$$
both evaluated with $x=\cos\theta$ (Riley et al., eqs. 18.61–18.62,
pp. 599–600; Arfken et al., eqs. 18.116, 18.118, p. 907). Arfken et al. add
the analogous relations for $V_n$ (weight $(1-x^2)^{-1/2}$, value $0$ at
$n=m=0$) and $W_n$ (weight $(1-x^2)^{1/2}$) (eqs. 18.117, 18.119). The
Chebyshev series is $f=\tfrac12c_0+\sum_{n\ge1}c_nT_n$ with
$c_n=\frac2\pi\int_{-1}^1fT_n(1-x^2)^{-1/2}dx$, and $f=\sum c_nU_n$ with
$c_n=\frac2\pi\int_{-1}^1fU_n(1-x^2)^{1/2}dx$ (Riley et al., pp. 600–601).

## Origin as Gegenbauer polynomials

Arfken et al. introduce the Chebyshev polynomials through the generating
function of the **Gegenbauer (ultraspherical) polynomials**
$$(1-2xt+t^2)^{-\lambda}=\sum_{n=0}^\infty C_n^{(\lambda)}(x)\,t^n,$$
which gives $P_n$ for $\lambda=\tfrac12$ and $U_n=C_n^{(1)}$ for
$\lambda=1$; $T_n$ comes from the limit
$T_n=\tfrac n2\lim_{\lambda\to0}C_n^{(\lambda)}/\lambda$ for $n\ge1$,
$T_0=1$ (eqs. 18.85–18.90, pp. 899–900, with their $\alpha$ for
$\lambda$). The $C_n^{(\lambda)}$ satisfy
$(1-x^2)y''-(2\lambda+1)xy'+n(n+2\lambda)y=0$ (eq. 18.99, p. 903). Neither
book states their weight, norm or recurrence; Riley et al. do not mention
them.

## Use in numerical analysis

* **Equal ripple.** $T_n$ ($n>0$) oscillates between $+1$ and $-1$ on
  $[-1,1]$ (Arfken et al., p. 905, Fig. 18.6 for $T_{12}$). Arfken et al.
  argue that if a Chebyshev series is truncated where successive terms
  decrease rapidly, the error is approximately the first omitted $T_n$, so
  it is negligible at the zeros of $T_n$ and has equal, alternating maxima
  at its extrema between them: the error "satisf[ies] a minimax principle"
  (p. 905). This is a heuristic argument, not a theorem; the book proves no
  best-approximation property. Example 18.4.1 (p. 906) compares four-term
  Taylor, Legendre and Chebyshev approximations of $e^x$ on $[-1,1]$: the
  Chebyshev error maxima are comparable in size, whereas the Legendre error
  is largest at $\pm1$.
* **Quadrature.** Riley et al. motivate the polynomials by Gauss–Chebyshev
  integration of integrands containing $(1-x^2)^{\pm1/2}$ (p. 599), whose
  nodes and weights have closed forms: see
  [Gauss–Chebyshev quadrature](/methods/gauss-chebyshev-quadrature.md).
* **Hypergeometric form.** $T_m(x)=F(m,-m,\tfrac12;(1-x)/2)$ (Riley et al.,
  §18.10.1, pp. 630–631, proved there).

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §18.4, eqs. 18.54–18.72, pp. 595–602; §18.10.1, pp. 630–631.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §18.4, eqs. 18.85–18.119, pp. 899–907; Example 18.4.1, p. 906.
