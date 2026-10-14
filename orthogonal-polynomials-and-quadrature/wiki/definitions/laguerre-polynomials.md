---
type: Definition
title: "Laguerre and associated Laguerre polynomials"
description: "The polynomial solutions L_n of Laguerre's equation with L_n(0)=1, orthonormal on [0,inf) with weight exp(-x), and the associated polynomials L_n^{(m)}=(-1)^m d^m L_{n+m}/dx^m, orthogonal with weight x^m exp(-x) and norm (n+m)!/n!; explicit forms, special values and Laguerre functions."
status: established
aliases: [associated Laguerre polynomials, generalized Laguerre polynomials, Laguerre functions]
tags: [laguerre, classical-family, orthogonality, unbounded-interval, convention]
timestamp: 2026-10-14T00:00:00Z
---

# Laguerre and associated Laguerre polynomials

## Laguerre polynomials

Laguerre's equation $x\,y''+(1-x)\,y'+n\,y=0$ has a regular singular point at
$x=0$ with a repeated indicial root $0$, so it has only one Frobenius
solution, a power series with $a_{m+1}=(m-n)a_m/(m+1)^2$; for integer
$n\ge0$ it terminates. With $a_0=1$,
$$L_n(x)=\sum_{m=0}^n(-1)^m\frac{n!}{(m!)^2(n-m)!}\,x^m,\qquad L_n(0)=1$$
([Riley et al. (2006)](/sources/riley-2006.md), §18.7, eqs. 18.107–18.111,
pp. 616–617; [Arfken et al. (2013)](/sources/arfken-2013.md), §18.3,
eqs. 18.44, 18.53–18.54, pp. 889–891). Both books use this scale; Arfken et
al. note that "not all workers" do and that theirs agrees with AMS-55
(p. 890). The polynomials have no parity (Arfken et al., p. 892).
$$L_0=1,\quad L_1=1-x,\quad 2!\,L_2=x^2-4x+2,\quad 3!\,L_3=-x^3+9x^2-18x+6$$
(both books; Arfken et al., Table 18.2 to $n=6$, p. 891).

**Orthonormality.**
$$\int_0^\infty L_n(x)L_m(x)\,e^{-x}\,dx=\delta_{nm}$$
(Riley et al., eq. 18.113, p. 619, proved from the Rodrigues formula;
Arfken et al., eq. 18.55, p. 892, proof set as Exercise 18.3.3). The
expansion is $f=\sum c_nL_n$ with $c_n=\int_0^\infty fL_ne^{-x}dx$ (Riley et
al., p. 620). The **Laguerre functions** $e^{-x/2}L_n(x)$ are orthonormal with
unit weight on $[0,\infty)$ and satisfy
$x\varphi''+\varphi'+(n+\tfrac12-\tfrac x4)\varphi=0$ (Riley et al., p. 620;
Arfken et al., eqs. 18.56–18.57, p. 892).

Recurrences: $(n+1)L_{n+1}=(2n+1-x)L_n-nL_{n-1}$, $xL_n'=nL_n-nL_{n-1}$,
$L_{n-1}=L_{n-1}'-L_n'$ (Riley et al., eqs. 18.115–18.117, p. 620; Arfken
et al., eqs. 18.51–18.52, p. 890). Rodrigues formula
$L_n=\frac{e^x}{n!}\frac{d^n}{dx^n}(x^ne^{-x})$ and generating function
$e^{-xt/(1-t)}/(1-t)=\sum L_nt^n$: see
[Rodrigues formula](/results/rodrigues-formula.md) and
[generating functions](/results/generating-functions.md).

## Associated (generalized) Laguerre polynomials

For integers $n,m\ge0$,
$$L_n^{(m)}(x)=(-1)^m\frac{d^m}{dx^m}L_{n+m}(x)=\sum_{k=0}^n(-1)^k\frac{(n+m)!}{k!\,(n-k)!\,(k+m)!}\,x^k$$
solves $x\,y''+(m+1-x)\,y'+n\,y=0$, is a polynomial of degree $n$ and
reduces to $L_n$ for $m=0$ ([Riley et al. (2006)](/sources/riley-2006.md),
§18.8, eqs. 18.118–18.120, pp. 621–622, with $L_n^m$;
[Arfken et al. (2013)](/sources/arfken-2013.md), eqs. 18.58–18.59 and
18.69, pp. 892–894, with $L_n^k$). Both books define the sign factor
$(-1)^m$ and both footnote the other convention
$\frac{d^m}{dx^m}L_{n+m}$, which differs by $(-1)^m$ (Riley et al., p. 621;
Arfken et al., footnote 4, p. 892). The registry writes the upper index in
parentheses, $L_n^{(m)}$, to keep it apart from an exponent and from the
associated Legendre $P_\ell^m$; the books' $L_n^m$ and $L_n^k$ are the same
functions. Special value: $L_n^{(m)}(0)=\binom{n+m}{n}$ (Riley et al.,
p. 624; Arfken et al., eq. 18.64, p. 894).

**Orthogonality.** For fixed $m$,
$$\int_0^\infty L_n^{(m)}(x)L_k^{(m)}(x)\,x^me^{-x}\,dx=\frac{(n+m)!}{n!}\,\delta_{nk}$$
(Riley et al., eq. 18.122, p. 623; Arfken et al., eq. 18.71, p. 895). Each
$m$ thus defines its own orthogonal family on $[0,\infty)$ with weight
$x^me^{-x}$ (Arfken et al., p. 895). Riley et al. call
$x^{m/2}e^{-x/2}L_n^{(m)}$ the orthogonal associated Laguerre functions
(p. 623); Arfken et al. give the self-adjoint equations of
$e^{-x/2}x^{m/2}L_n^{(m)}$ and of $e^{-x/2}x^{(m+1)/2}L_n^{(m)}$, the latter
orthogonal with weight $x^{-1}$ (eqs. 18.73–18.75, p. 895), and use it for
the hydrogen-atom radial functions (Example 18.3.1, pp. 896–897).

Recurrences: $(n+1)L_{n+1}^{(m)}=(2n+m+1-x)L_n^{(m)}-(n+m)L_{n-1}^{(m)}$ and
$x\,\frac{d}{dx}L_n^{(m)}=nL_n^{(m)}-(n+m)L_{n-1}^{(m)}$ (Riley et al.,
eqs. 18.124–18.125, p. 624; Arfken et al., eq. 18.66, p. 894, gives the
first). Arfken et al. also print a generating function in the lower index,
$e^{-tx}(1+t)^\ell=\sum_{n}L_n^{(\ell-n)}(x)\,t^n$, from H. J. Weber
(2007) (eq. 18.60, p. 892; see
[generating functions](/results/generating-functions.md)).

Gauss–Laguerre quadrature, built on $L_n$, is on
[Gaussian quadrature](/methods/gaussian-quadrature.md).

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §§18.7–18.8, eqs. 18.107–18.125, pp. 616–624.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §18.3, eqs. 18.44–18.75, pp. 889–895; Example 18.3.1, pp. 896–897.
