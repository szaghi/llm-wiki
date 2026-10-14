---
type: Result
title: "Rodrigues formula"
description: "For a Sturm–Liouville equation p y''+q y'+lambda y=0 with p quadratic and q linear, the degree-n polynomial solution is proportional to (1/omega) d^n/dx^n [omega p^n], omega the weight; the general proof (Arfken §12.1) and the formulae of the Legendre, associated Legendre, Chebyshev, Hermite and Laguerre families, with the scale factors that fix each standardization."
status: established
aliases: [Rodrigues formulas, Rodrigues' formula, Schlaefli integral]
tags: [rodrigues, classical-family, sturm-liouville]
timestamp: 2026-10-14T00:00:00Z
---

# Rodrigues formula

## Statement

Let $p(x)$ be of degree at most 2 and $q(x)$ of degree at most 1, and let
$\omega$ be the weight that makes $p\,y''+q\,y'+\lambda y=0$ self-adjoint,
$(\omega p)'=\omega q$. Then for each $n$ the polynomial
$$y_n(x)=\frac{1}{\omega(x)}\frac{d^n}{dx^n}\Big[\omega(x)\,p(x)^n\Big]$$
has degree $n$ and solves the equation with $\lambda_n=-n(n-1)\tfrac{p''}{2}-n\,q'$
([Arfken et al. (2013)](/sources/arfken-2013.md), §12.1, eqs. 12.1–12.16,
pp. 551–554). The proof differentiates $p(\omega p^n)'=\omega p^n[(n-1)p'+q]$
$n+1$ times with Leibniz's rule, which leaves only three terms because $p$
is quadratic and $q$ linear, and then moves the factors $1/\omega$ through
the derivatives using $(\omega p)'=\omega q$. Degree $n$ follows because each
derivative of $\omega$ produces $\omega/p^j$ times a polynomial and the
factors $p^j$ cancel. The formula fixes the polynomial only up to a constant;
each family multiplies it by a conventional factor (Arfken et al.,
pp. 554, 721).

**Schlaefli integral.** By Cauchy's formula,
$y_n(x)=\frac{1}{\omega(x)}\frac{n!}{2\pi i}\oint_C\frac{\omega(z)p(z)^n}{(z-x)^{n+1}}dz$
with $C$ enclosing $x$ inside a region where $\omega p^n$ is analytic
(eq. 12.18, p. 554). Summing it against $t^n$ produces generating functions
(eq. 12.25; see [generating functions](/results/generating-functions.md)).

[Riley et al. (2006)](/sources/riley-2006.md) give no general statement;
they prove each family's formula separately, either by differentiating
$(x^2-1)u'-2\ell xu=0$ with $u=(x^2-1)^\ell$ (Legendre, §18.1.2, p. 581) or
with Leibniz's theorem against the explicit series (Laguerre, Hermite), and
state the Chebyshev formulae "may be proved in an analogous manner" (p. 599).

## The classical formulae

All are stated in both books unless marked.

| Family | $p$, $\omega$ | Formula | Locators |
|---|---|---|---|
| Legendre | $1-x^2$, $1$ | $P_n=\dfrac{1}{2^nn!}\dfrac{d^n}{dx^n}(x^2-1)^n$ | Riley eq. 18.9, p. 581; Arfken eq. 15.30, p. 721 |
| Hermite | $1$, $e^{-x^2}$ | $H_n=(-1)^ne^{x^2}\dfrac{d^n}{dx^n}e^{-x^2}$ | Riley eq. 18.130, p. 626; Arfken eqs. 12.17, 18.8, pp. 554, 874 |
| Laguerre | $x$, $e^{-x}$ | $L_n=\dfrac{e^x}{n!}\dfrac{d^n}{dx^n}\big(x^ne^{-x}\big)$ | Riley eq. 18.112, p. 618; Arfken eq. 18.46, p. 889 |
| associated Laguerre | $x$, $x^me^{-x}$ | $L_n^{(m)}=\dfrac{e^xx^{-m}}{n!}\dfrac{d^n}{dx^n}\big(x^{n+m}e^{-x}\big)$ | Riley eq. 18.121, p. 622; Arfken eq. 18.72, p. 895 |
| Chebyshev I | $1-x^2$, $(1-x^2)^{-1/2}$ | $T_n=\dfrac{(-1)^n(1-x^2)^{1/2}}{(2n-1)!!}\dfrac{d^n}{dx^n}(1-x^2)^{n-1/2}$ | Riley p. 599; Arfken Table 12.1, p. 559, eq. 18.102, p. 903 |
| Chebyshev II | $1-x^2$, $(1-x^2)^{1/2}$ | $U_n=\dfrac{(-1)^n(n+1)}{(2n+1)!!\,(1-x^2)^{1/2}}\dfrac{d^n}{dx^n}(1-x^2)^{n+1/2}$ | Riley p. 599; Arfken Table 12.1, eq. 18.103 |
| associated Legendre | — | $P_\ell^m=\dfrac{(-1)^m}{2^\ell\ell!}(1-x^2)^{m/2}\dfrac{d^{\ell+m}}{dx^{\ell+m}}(x^2-1)^\ell$ | Arfken eq. 15.80, p. 743 (with the phase); Riley p. 588 (without it) |

**Equivalent printed forms for Chebyshev.** Riley et al. print the prefactors
as $\sqrt\pi/[2^n(n-\tfrac12)!]$ and $\sqrt\pi(n+1)/[2^{n+1}(n+\tfrac12)!]$
(checked on the page image, p. 599); Arfken et al. print
$\pi^{1/2}/[2^n\Gamma(n+\tfrac12)]$ in eq. 18.102 and $1/(2n-1)!!$ in Table
12.1. They agree, since $\Gamma(n+\tfrac12)=(n-\tfrac12)!=(2n-1)!!\sqrt\pi/2^n$
and $\Gamma(n+\tfrac32)=(2n+1)!!\sqrt\pi/2^{n+1}$ (compiler's check). The
table above uses the double-factorial form.

**Laguerre in Arfken's general form.** For $L_n$ the general formula with
$p=x$, $\omega=e^{-x}$ gives $e^x\frac{d^n}{dx^n}(x^ne^{-x})$, and Arfken et
al. insert $1/n!$ to reach $L_n(0)=1$ (p. 889); for $H_n$ they insert
$(-1)^n$ for the conventional sign (p. 554). These factors are the
standardization, not part of the theorem.

## Uses

The formulae give the norms by $n$-fold integration by parts: for Legendre
$\int_{-1}^1P_n^2dx=\frac{(2n)!}{2^{2n}(n!)^2}\int_{-1}^1(1-x^2)^ndx=\frac{2}{2n+1}$
(Riley et al., eq. 18.11, p. 582), and similarly for $L_n$, $L_n^{(m)}$, $H_n$
and $P_\ell^m$ (Riley et al., eqs. 18.113, 18.122, 18.132, 18.37; Arfken et
al., eqs. 15.97–15.104). They also show that the leading coefficient of
$P_n$ is $(2n-1)!!/n!$ (Arfken et al., p. 721).

# Citations

1. [Arfken et al. (2013)](/sources/arfken-2013.md), §12.1, eqs. 12.1–12.18, pp. 551–554; Table 12.1, p. 559; eqs. 15.30, 15.80, 18.8, 18.46, 18.72, 18.102–18.103.
2. [Riley et al. (2006)](/sources/riley-2006.md), eqs. 18.9–18.11, pp. 581–582; p. 599; eqs. 18.112, 18.121, 18.130.
