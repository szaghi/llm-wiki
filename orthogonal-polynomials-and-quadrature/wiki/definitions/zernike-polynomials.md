---
type: Definition
title: "Zernike polynomials and the Fourier–Zernike basis"
description: "The radial polynomials R_n^m(r) (0<=m<=n, n-m even) and the real Zernike functions R_n^|m|(r)cos(m phi) or sin(|m| phi) on the unit disc, whose r^|m| factor builds in the regularity of analytic functions at the origin; their product with a Fourier series in a periodic coordinate is the Fourier–Zernike spectral basis, with exponential radial convergence measured in one code."
status: established
aliases: [Zernike polynomials, radial Zernike polynomials, Zernike functions, Fourier–Zernike basis, Fourier-Zernike basis]
tags: [zernike, unit-disc, spectral-basis, axis-regularity, spectral-convergence, jacobi]
timestamp: 2026-10-16T00:00:00Z
---

# Zernike polynomials and the Fourier–Zernike basis

## Definition

On the unit disc, with polar coordinates $(r,\phi)$, $0\le r\le1$, the
**radial Zernike polynomial** of degree $n$ and azimuthal order $m$,
integers with $0\le m\le n$ and $n-m$ even, is
$$R_n^m(r)=\sum_{j=0}^{(n-m)/2}\frac{(-1)^j\,(n-j)!}{j!\,\big[\tfrac{n+m}{2}-j\big]!\,\big[\tfrac{n-m}{2}-j\big]!}\,r^{\,n-2j},$$
and the **real Zernike function** of signed order $m$, $\lvert m\rvert\le n$,
$n-\lvert m\rvert$ even, is
$$Z_n^m(r,\phi)=\begin{cases}R_n^{\lvert m\rvert}(r)\cos(m\phi), & m\ge0,\\ R_n^{\lvert m\rvert}(r)\sin(\lvert m\rvert\phi), & m<0.\end{cases}$$
Panici et al. give both definitions, call $R_n^{\lvert m\rvert}$ "the shifted
Jacobi polynomial", and cite Zernike & Stratton (1934) and Sakai & Redekopp
(2009) for the basis
([Panici et al. (2023)](/sources/panici-2023.md), §3.2, eqs. 3.18–3.19,
p. 7).

**Printed slip.** The paper's eq. 3.19 prints the last factorial of the
denominator as $\big[(l-\lvert m\rvert)/2+s\big]!$ (its $l$, $s$ are our
$n$, $j$). With $+j$ the sum does not give the radial Zernike polynomials:
for $n=2$, $m=0$ it gives $2r^2-\tfrac12$ instead of $2r^2-1$. The formula
above, with $-j$, is the standard one. It satisfies $R_n^m(1)=1$ and the
Jacobi relation and orthogonality stated below, which the compiler checked
symbolically for every $n\le8$ (hypothesis-grade compiler check, not a
statement of the source).

**Structure.** Every power in $R_n^m$ is $r^{\,n-2j}=r^{\,m}\,r^{\,2[(n-m)/2-j]}$,
so $R_n^m(r)=r^m\times$ (a polynomial in $r^2$ of degree $(n-m)/2$). This is
the property the source uses: a Zernike coefficient of azimuthal order $m$
"necessarily has a radial dependence that scales as $\rho^m$" (their $\rho$
is our $r$; §3.2, p. 7).

## Regularity at the origin

An analytic function $f(r,\phi)$ on the disc, expanded in a Fourier series
in $\phi$, has azimuthal coefficients of the form
$$f_m(r)=r^{\lvert m\rvert}\left(b_{m,0}+b_{m,2}\,r^2+b_{m,4}\,r^4+\cdots\right),$$
which the source states after Lewis & Bellan (1990) (eq. 3.21, p. 7). A
truncated expansion in the $Z_n^m$ meets this condition term by term, so it
contains only modes that are regular at the origin: "ensuring only physical
modes are included in the spectrum" ([Panici et al. (2023)](/sources/panici-2023.md),
§3.2, p. 7; §2, p. 3). A representation by Fourier series in $\phi$ with
coefficients known only at discrete radii does not impose it. The source
shows this as a diagnostic: for an equilibrium computed both ways, the
Fourier coefficients divided by $r^{\lvert m\rvert}$ stay roughly constant as
$r\to0$ for the Fourier–Zernike solution and diverge, beyond $10^{10}$ for
high-order modes, for the finite-difference solution (§5.1, Fig. 4,
pp. 11–12; the magnitude is read from the figure).

## The Fourier–Zernike basis

For a domain that is a disc times a circle, with periodic coordinate
$\zeta$, the source expands each unknown $u(r,\phi,\zeta)$ (the
flux-surface coordinates and a stream function of a stellarator
equilibrium) as
$$u(r,\phi,\zeta)=\sum_{m=-M}^{M}\;\sum_{k=-K}^{K}\;\sum_{n=0}^{L}c_{nmk}\,Z_n^m(r,\phi)\,\mathcal F_k(\zeta),$$
with $\mathcal F_k(\zeta)=\cos(k\zeta)$ for $k\ge0$ and $\sin(\lvert k\rvert\zeta)$
for $k<0$. The source's toroidal functions carry the number of field periods
as a factor of $\zeta$, and its $\zeta$ spans one field period (eqs. 3.16c,
3.17, 3.20, pp. 6–7). The triple sum is printed over the full box; only pairs
$(n,m)$ with $n\ge\lvert m\rvert$ and $n-\lvert m\rvert$ even define a $Z_n^m$.
Which pairs are kept for given $L$ and $M$ is set by a **Zernike indexing
scheme**, ANSI or Fringe, which "affects the radial resolution for a given
$L$ and $M$" (Table 2, p. 17, citing Loomis 1978 and Genberg et al. 2002).
Because radial and azimuthal modes are coupled in this basis, raising $M$
also raises the radial resolution (App. C, p. 30). The source names the two
schemes but does not define them.

The source uses the basis pseudospectrally: the residual equations are
evaluated "on a collocation grid" and the coefficients $c_{nmk}$ are found
by a Newton-type nonlinear solve (§3.2, p. 8). It does not specify the
collocation nodes or a quadrature rule; the only trace of the node set is
that the measured error has local minima on the collocation surfaces
(§5.3.2, p. 15; App. C, p. 30).

## Convergence

The source expects exponential convergence of a spectral representation of
a smooth solution, citing Boyd (2001), and therefore exponential convergence
in both the angular and the radial resolution for the Fourier–Zernike
basis, against first-order (algebraic) radial convergence for a
representation by Fourier series on radial finite-difference surfaces
(§5.2, p. 12; Table 1, p. 14). On an axisymmetric D-shaped equilibrium at
fixed $M=16$ it measures:

* Fourier–Zernike basis, $L=16,\dots,24$: the normalized force-balance
  error follows the fit $\exp(-0.61L-0.01)$, a straight line on semi-log
  axes, falling from about $5\times10^{-5}$ to about $4\times10^{-7}$
  (Fig. 8, p. 14);
* radial finite differences, about $16$ to $1024$ radial grid points: the
  error follows the log–log fit slope $-1.02$, first order (Fig. 7,
  p. 14).

At higher resolution on a 3-D case the error "begins to not decrease
uniformly" around $L=M=K=16$ (App. C, p. 30, Fig. 22). These are
measurements on one code and one error metric; the source states no
convergence theorem.

## Related facts not stated by the source

The following standard facts are supplied by the compiler and
hypothesis-grade: no ingested source of this bundle states them. They were
checked symbolically for all $n\le8$.

* **Jacobi form.** For $0\le m\le n$, $n-m$ even,
  $$R_n^m(r)=(-1)^{(n-m)/2}\,r^m\,P_{(n-m)/2}^{(m,0)}\!\left(1-2r^2\right),$$
  which makes precise the source's "shifted Jacobi polynomial": $r^{-m}R_n^m$
  is a Jacobi polynomial in the variable $1-2r^2$.
* **Orthogonality.** At fixed $m$,
  $$\int_0^1R_n^m(r)\,R_{n'}^m(r)\,r\,dr=\frac{\delta_{nn'}}{2(n+1)},$$
  so the $Z_n^m$ are orthogonal on the disc with the area element
  $r\,dr\,d\phi$. The source cites Genberg et al. (2002), *Orthogonality of
  Zernike polynomials*, without stating the relation.

For orthogonal polynomials of one variable see
[orthogonal polynomials with respect to a weight function](/definitions/orthogonal-polynomials.md).

# Citations

1. [Panici et al. (2023)](/sources/panici-2023.md), §2, p. 3; §3.2, eqs. 3.16–3.21, pp. 6–8; §5.1, Fig. 4, pp. 11–12; §5.2, Table 1, Figs. 7–8, pp. 12–14; §5.3.2, p. 15; Table 2, p. 17; App. C, Fig. 22, pp. 29–30.
