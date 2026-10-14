---
type: Definition
title: "Bessel functions"
description: "Solutions of Bessel's equation x^2y''+xy'+(x^2-nu^2)y=0: the regular J_nu (Frobenius series), the second-kind Y_nu, the Hankel functions, and the modified I_nu and K_nu; series, recurrences, integral representations, zeros, Wronskians and large-argument asymptotics as numerics uses them."
status: established
aliases: [Bessel functions of the first kind, Neumann functions, Weber functions, Hankel functions, modified Bessel functions, cylinder functions]
tags: [bessel, cylinder-functions, special-functions, asymptotics, zeros]
timestamp: 2026-10-14T00:00:00Z
---

# Bessel functions

## First kind $J_\nu$

Bessel's equation $x^2y''+xy'+(x^2-\nu^2)y=0$ has a regular singular point
at $x=0$ (indicial roots $\pm\nu$) and an essential singularity at
$x=\infty$. The Frobenius solution for the root $+\nu$, scaled by
$1/[2^\nu\Gamma(\nu+1)]$, is
$$J_\nu(x)=\sum_{s=0}^\infty\frac{(-1)^s}{s!\,\Gamma(\nu+s+1)}\Big(\frac x2\Big)^{\nu+2s}$$
([Riley et al. (2006)](/sources/riley-2006.md), §18.5.1, eqs. 18.73–18.79,
pp. 602–604; [Arfken et al. (2013)](/sources/arfken-2013.md), §14.1,
eq. 14.6, p. 645). For $\nu\ge0$ the series converges for all $x$ and is
"a practical way to evaluate $J_\nu(x)$" for small $x$ (Arfken et al.,
p. 645). For non-integer $\nu$, $J_\nu$ and $J_{-\nu}$ are independent; for
integer $n$, $J_{-n}=(-1)^nJ_n$ (Riley et al., p. 606; Arfken et al.,
eq. 14.5, p. 645). Half-integer orders are elementary:
$J_{1/2}=\sqrt{2/\pi x}\,\sin x$, $J_{-1/2}=\sqrt{2/\pi x}\,\cos x$ (Riley et
al., p. 605). For integer order the generating function
$e^{(x/2)(t-1/t)}=\sum_{n=-\infty}^{\infty}J_nt^n$ holds (Riley et al.,
eq. 18.98, p. 613; Arfken et al., eq. 14.2, p. 644); see
[generating functions](/results/generating-functions.md).

**Recurrences** (both books; Riley et al. derive them from the series for
any $\nu$, Arfken et al. from the generating function for integer $n$ and
then extend):
$$J_{\nu-1}+J_{\nu+1}=\frac{2\nu}{x}J_\nu,\qquad J_{\nu-1}-J_{\nu+1}=2J_\nu',\qquad \frac{d}{dx}\big[x^{\pm\nu}J_\nu\big]=\pm x^{\pm\nu}J_{\nu\mp1}$$
(Riley et al., eqs. 18.92–18.97, pp. 611–612; Arfken et al., eqs.
14.7–14.12, p. 646). Arfken et al. prove the converse: any functions obeying
the first two relations solve Bessel's equation (eqs. 14.13–14.14,
pp. 646–647). The first relation is a three-term recurrence in $\nu$ that
generates every integer $J_n$ from $J_0$ and $J_1$ (Arfken et al., p. 646);
neither book discusses its numerical stability.

**Integral representation** for integer $n$:
$J_n(x)=\frac1\pi\int_0^\pi\cos(n\theta-x\sin\theta)\,d\theta$, and
$J_0(x)=\frac1{2\pi}\int_0^{2\pi}e^{ix\cos\theta}d\theta$ (Riley et al.,
eq. 18.99, p. 613; Arfken et al., eqs. 14.18–14.20, p. 647). Arfken et al.
extend it to non-integer $\nu$ with the Schlaefli contour (eqs. 14.37–14.40,
pp. 653–654).

**Zeros.** There is no closed formula for the zeros of $J_n$; they are found
numerically and tabulated. Arfken et al. list the first five zeros of
$J_0,\dots,J_5$ and of $J_0',\dots,J_5'$ (Table 14.1, p. 648; e.g.
$\alpha_{0,1}=2.4048$, $\alpha_{1,1}=3.8317$) and point to AMS-55 and to
Beattie (1958) for 700 zeros (p. 648 and footnote 2). They set as exercises
that between two consecutive zeros of $J_n$ there is exactly one zero of
$J_{n+1}$ (Exercise 14.1.11, p. 656) and that $J_\nu$, $\nu>-1$, has no
complex zeros (Exercise 14.2.4, p. 665). The zeros fix the scales of the
orthogonal Bessel sets: see [Fourier–Bessel series](/results/fourier-bessel-series.md).

## Second kind $Y_\nu$ and Hankel functions

$$Y_\nu(x)=\frac{J_\nu(x)\cos\nu\pi-J_{-\nu}(x)}{\sin\nu\pi},\qquad Y_n=\lim_{\nu\to n}Y_\nu,$$
(Riley et al., eqs. 18.81–18.82, p. 607; Arfken et al., eqs. 14.57–14.60,
pp. 667–668). Both books call it the Bessel function of the second kind, or
Weber/Neumann function; Arfken et al. note that earlier editions wrote
$N_\nu$ (footnote 1, p. 644). $J_\nu$ and $Y_\nu$ are independent for every
$\nu$ and $Y_\nu$ is singular at $x=0$; for integer $n$ it contains
$\frac2\pi J_n\ln\frac x2$ (Arfken et al., eqs. 14.61–14.62, p. 668; Riley et
al., Exercise 18.22, p. 645). $Y_\nu$ satisfies the same recurrences as
$J_\nu$ (Riley et al., p. 612; Arfken et al., p. 669). Wronskian:
$J_\nu Y_\nu'-J_\nu'Y_\nu=2/(\pi x)$, and
$J_\nu J_{-\nu}'-J_\nu'J_{-\nu}=-2\sin\nu\pi/(\pi x)$ (Arfken et al.,
eqs. 14.67–14.71, pp. 670–671), which vanishes for integer $\nu$.

$H_\nu^{(1)}=J_\nu+iY_\nu$ and $H_\nu^{(2)}=J_\nu-iY_\nu$ (Riley et al.,
p. 607; Arfken et al., eqs. 14.76–14.77, p. 675), complex conjugates for
real $x$, with the same recurrences (eqs. 14.83–14.84). Arfken et al. give
their contour-integral representations (eqs. 14.90–14.91, p. 676).

## Modified Bessel functions $I_\nu$, $K_\nu$

Only Arfken et al. treat them. They solve
$x^2y''+xy'-(x^2+\nu^2)y=0$:
$$I_\nu(x)=i^{-\nu}J_\nu(ix)=\sum_{s=0}^\infty\frac{1}{s!\,\Gamma(s+\nu+1)}\Big(\frac x2\Big)^{\nu+2s},\qquad K_\nu(x)=\frac\pi2\,i^{\nu+1}H_\nu^{(1)}(ix)=\frac\pi2\,\frac{I_{-\nu}(x)-I_\nu(x)}{\sin\nu\pi}$$
([Arfken et al. (2013)](/sources/arfken-2013.md), §14.5, eqs. 14.97–14.107,
pp. 680–683, following AMS-55). $I_\nu$ is finite at $0$ and grows like
$e^x/\sqrt{2\pi x}$; $K_\nu$ is singular at $0$ and decays like
$\sqrt{\pi/2x}\,e^{-x}$ (eqs. 14.127, 14.143). $K_\nu$ does not obey the
same recurrences as $I_\nu$:
$I_{\nu-1}-I_{\nu+1}=\frac{2\nu}xI_\nu$ but
$K_{\nu-1}-K_{\nu+1}=-\frac{2\nu}xK_\nu$ (eqs. 14.104, 14.108); Arfken et
al. note that some authors add a factor $\cos\nu\pi$ to $K_\nu$ to equalize
them, at the price of $K_\nu=0$ for half-integer $\nu$ (p. 683).

## Large-argument asymptotics

From the steepest-descent evaluation of the Hankel contour integrals,
$H_\nu^{(1,2)}(z)\sim\sqrt{2/\pi z}\,e^{\pm i(z-\nu\pi/2-\pi/4)}$, and
$$J_\nu(z)=\sqrt{\frac2{\pi z}}\Big[A_\nu(z)\cos\big(z-\tfrac{(2\nu+1)\pi}{4}\big)-B_\nu(z)\sin\big(z-\tfrac{(2\nu+1)\pi}{4}\big)\Big],$$
with $Y_\nu$ the same with $\cos\to\sin$, $\sin\to-\cos$, and
$A_\nu\sim1-\frac{(4\nu^2-1)(4\nu^2-9)}{2!(8z)^2}+\dots$,
$B_\nu\sim\frac{4\nu^2-1}{8z}-\dots$, valid for
$-\pi<\arg z<\pi$ ([Arfken et al. (2013)](/sources/arfken-2013.md), §14.6,
eqs. 14.125–14.141, pp. 689–693, where the two asymptotic series are
written $P_\nu$, $Q_\nu$; the registry's $A_\nu$, $B_\nu$ avoid the
Legendre symbols). The
series are asymptotic, not convergent; they terminate for half-integer
$\nu$, where they are exact (pp. 692, 694). The leading term
$J_n(x)\approx\sqrt{2/\pi x}\cos(x-\frac{(2n+1)\pi}{4})$ is accurate when
$8x\gg4n^2-1$; it is "nearly quantitative" for $J_0$ above $x\approx5$, but
for larger order "the asymptotic region may be far out" (eqs.
14.144–14.145, p. 694). Asymptotically the zeros of $J_n$ and $Y_n$
alternate (p. 693); by the leading term their spacing tends to $\pi$
(compiler's reading of eq. 14.144; the book states the $\pi$ spacing only
for the roots of a coaxial-guide combination of $J_0$ and $Y_0$,
Exercise 14.3.10, pp. 673–674). Riley et al. do not treat asymptotic forms in the chapter read.

Spherical Bessel functions $j_\ell=\sqrt{\pi/2x}\,J_{\ell+1/2}$ are on
[spherical Bessel functions](/definitions/spherical-bessel-functions.md).

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §18.5, eqs. 18.73–18.100, pp. 602–614; Exercise 18.22, p. 645.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §§14.1, 14.3–14.6, eqs. 14.1–14.40, 14.57–14.145, pp. 643–695; Table 14.1, p. 648.
