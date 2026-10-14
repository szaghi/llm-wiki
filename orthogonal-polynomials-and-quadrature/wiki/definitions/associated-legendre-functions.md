---
type: Definition
title: "Associated Legendre functions"
description: "The regular solutions P_l^m of the associated Legendre equation for integers 0<=|m|<=l, built as (1-x^2)^{m/2} times the m-th derivative of P_l; orthogonal in l at fixed m with norm 2(l+m)!/((2l+1)(l-m)!); the two founding sources differ by the Condon–Shortley factor (-1)^m."
status: established
aliases: [associated Legendre polynomials, Ferrers functions, Condon-Shortley phase]
tags: [legendre, associated-legendre, sphere, orthogonality, convention]
timestamp: 2026-10-14T00:00:00Z
---

# Associated Legendre functions

## Definition

The associated Legendre equation
$$(1-x^2)\,y''-2x\,y'+\Big[\ell(\ell+1)-\frac{m^2}{1-x^2}\Big]y=0$$
arises from separating $\nabla^2$ in spherical polar coordinates with
$x=\cos\theta$; it reduces to Legendre's equation for $m=0$. If $u$ solves
Legendre's equation, $(1-x^2)^{|m|/2}\,d^{|m|}u/dx^{|m|}$ solves the
associated equation ([Riley et al. (2006)](/sources/riley-2006.md), §18.2,
eqs. 18.28–18.30, pp. 587–588; [Arfken et al. (2013)](/sources/arfken-2013.md),
§15.4, eqs. 15.68–15.77, pp. 741–742). Solutions regular at $x=\pm1$ exist
only for integer $\ell\ge|m|$; in registry notation they are
$$P_\ell^m(x)=(-1)^m(1-x^2)^{m/2}\frac{d^m}{dx^m}P_\ell(x)=\frac{(-1)^m}{2^\ell\ell!}(1-x^2)^{m/2}\frac{d^{\ell+m}}{dx^{\ell+m}}(x^2-1)^\ell,\qquad 0\le m\le\ell,$$
and the second form extends the definition to $-\ell\le m<0$, with
$$P_\ell^{-m}(x)=(-1)^m\frac{(\ell-m)!}{(\ell+m)!}\,P_\ell^m(x)$$
(Arfken et al., eqs. 15.79–15.81, p. 743; Riley et al., eqs. 18.32–18.35,
pp. 588–589, proved there). $P_\ell^m=0$ for $|m|>\ell$; $P_\ell^m$ is a
polynomial for even $m$ and carries $(1-x^2)^{1/2}$ for odd $m$. The second-kind
functions $Q_\ell^m$ are defined the same way from $Q_\ell$ and are singular
at $x=\pm1$ (Riley et al., eq. 18.32, p. 589).

## Convention: the Condon–Shortley phase

The two founding sources define $P_\ell^m$ with opposite signs for odd $m$:

* [Arfken et al. (2013)](/sources/arfken-2013.md) include $(-1)^m$
  (eq. 15.78, p. 743) "to maintain agreement with AMS-55 … the most widely
  accepted notational standard", and call the resulting signs of $Y_\ell^m$
  the Condon–Shortley phase (p. 758). They note that Jackson's
  *Electrodynamics* omits the factor (footnote 3, p. 743). Their table starts
  $P_1^1=-(1-x^2)^{1/2}$ (Table 15.3, p. 745).
* [Riley et al. (2006)](/sources/riley-2006.md) define
  $(1-x^2)^{m/2}\,d^mP_\ell/dx^m$ **without** the factor (eq. 18.32, p. 588);
  their table starts $P_1^1=(1-x^2)^{1/2}$ (p. 589), and they put $(-1)^m$
  into the spherical harmonic instead (eq. 18.45). A footnote records a
  third convention, $P_\ell^{-m}=P_\ell^m$ with $m$ replaced by $|m|$
  (p. 588).

The registry follows Arfken et al. Riley's functions are
$(-1)^mP_\ell^m$ in registry notation; every Riley formula below is
translated accordingly. Because Riley moves the factor into $Y_\ell^m$, the
spherical harmonics of the two books are identical (see
[spherical harmonics](/definitions/spherical-harmonics.md)). The relation
for $P_\ell^{-m}$ has the same printed form in both books; it holds in
either convention, since flipping the sign of $P_\ell^{\pm m}$ for odd $m$
multiplies both sides by $-1$ (compiler's check).

## Orthogonality

For fixed $m$, with unit weight,
$$\int_{-1}^1P_\ell^m(x)\,P_k^m(x)\,dx=\frac{2}{2\ell+1}\frac{(\ell+m)!}{(\ell-m)!}\,\delta_{\ell k}$$
(Riley et al., eqs. 18.36–18.37, pp. 590–591, via the Rodrigues formula and
$K_\ell$; Arfken et al., eqs. 15.104–15.105, pp. 747–748, by repeated
integration by parts). The two values of $m$ must be equal. A second
relation holds at fixed $\ell$ with weight $(1-x^2)^{-1}$:
$\int_{-1}^1P_\ell^mP_\ell^k(1-x^2)^{-1}dx=\frac{(\ell+m)!}{m(\ell-m)!}\delta_{mk}$
for $m,k\ge1$; both books call it of no practical use, because the
azimuthal factor already separates different $m$ (Riley et al., eq. 18.39,
p. 591, stated for $|m|\ne|k|$; Arfken et al., eq. 15.107, p. 748). The
expansion of a function at fixed $m$ is
$f=\sum_{\ell\ge m}c_\ell P_\ell^m$ with
$c_\ell=\frac{2\ell+1}{2}\frac{(\ell-m)!}{(\ell+m)!}\int_{-1}^1fP_\ell^m\,dx$
(Riley et al., eq. 18.38, p. 591).

## Recurrences and evaluation

In registry notation (Arfken et al., eqs. 15.84, 15.87–15.92, p. 744; Riley
et al., eqs. 18.41–18.44, p. 592, translated by the factor $(-1)^m$):
$$\begin{aligned}
(\ell-m+1)\,P_{\ell+1}^m&=(2\ell+1)\,x\,P_\ell^m-(\ell+m)\,P_{\ell-1}^m,\\
P_\ell^{m+1}&=-\frac{2mx}{(1-x^2)^{1/2}}\,P_\ell^m-(\ell+m)(\ell-m+1)\,P_\ell^{m-1},\\
(2\ell+1)(1-x^2)^{1/2}\,P_\ell^m&=P_{\ell-1}^{m+1}-P_{\ell+1}^{m+1},\\
(1-x^2)^{1/2}\,\frac{dP_\ell^m}{dx}&=\tfrac12(\ell+m)(\ell-m+1)\,P_\ell^{m-1}-\tfrac12P_\ell^{m+1}.
\end{aligned}$$
The first is the same in both conventions, since it keeps $m$ fixed; the
others change sign term by term between the books, and the compiler checked
that Riley's printed forms map onto Arfken's under $P_\ell^m\to(-1)^mP_\ell^m$
(for the second: $m(m-1)-\ell(\ell+1)=-(\ell+m)(\ell-m+1)$). Riley et al.
state that, with their definition, the relations hold for negative as well
as non-negative $m$ (p. 592).

Arfken et al. give a stable starting point and recursion in $\ell$ at fixed
$m$ (Example 15.4.1, p. 745):
$$P_m^m=(-1)^m(2m-1)!!\,(1-x^2)^{m/2},\qquad P_{m+1}^m=(2m+1)\,x\,P_m^m,$$
then the first relation above for $\ell>m+1$. They do not discuss rounding
error. The polynomial factors $P_\ell^m/(1-x^2)^{m/2}$ have the generating
function $(-1)^m(2m-1)!!\,(1-2xt+t^2)^{-m-1/2}=\sum_sP_{s+m}^m\,t^s/(1-x^2)^{m/2}$
(eq. 15.82, p. 743), the same as Riley's eq. 18.40 up to $(-1)^m$
(p. 592; $(2m)!/(2^mm!)=(2m-1)!!$).

## Special values

$P_\ell^m(-x)=(-1)^{\ell+m}P_\ell^m(x)$; $P_\ell^m(\pm1)=0$ for $m\ne0$;
$P_\ell^m(0)=(-1)^{(\ell+m)/2}(\ell+m-1)!!/(\ell-m)!!$ for $\ell+m$ even
and $0$ otherwise ([Arfken et al. (2013)](/sources/arfken-2013.md),
eqs. 15.95–15.96, p. 746). These carry the registry's phase.

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §18.2, eqs. 18.28–18.44, pp. 587–593.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §15.4, eqs. 15.68–15.107, pp. 741–748; Table 15.3, p. 745; Example 15.4.1, p. 745.
