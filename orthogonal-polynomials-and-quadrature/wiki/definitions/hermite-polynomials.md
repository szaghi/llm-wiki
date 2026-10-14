---
type: Definition
title: "Hermite polynomials"
description: "The polynomial solutions H_n of Hermite's equation y''-2xy'+2ny=0 with leading coefficient 2^n (the physicists' standardization), orthogonal on the whole real line with weight exp(-x^2) and norm 2^n n! sqrt(pi); explicit form, parity, special values and the Hermite functions exp(-x^2/2)H_n."
status: established
aliases: [physicists' Hermite polynomials, Hermite functions]
tags: [hermite, classical-family, orthogonality, unbounded-interval]
timestamp: 2026-10-14T00:00:00Z
---

# Hermite polynomials

## Definition

Hermite's equation
$$y''-2x\,y'+2n\,y=0$$
has an essential singularity at $x=\infty$ and an ordinary point at $x=0$;
its power-series coefficients obey $a_{m+2}=-2(n-m)a_m/[(m+1)(m+2)]$, so for
integer $n\ge0$ one series terminates in a polynomial of degree $n$. With the
leading coefficient fixed at $2^n$,
$$H_n(x)=\sum_{m=0}^{\lfloor n/2\rfloor}(-1)^m\frac{n!}{m!\,(n-2m)!}\,(2x)^{n-2m}$$
([Riley et al. (2006)](/sources/riley-2006.md), §18.9, eqs. 18.126–18.129,
pp. 624–625; [Arfken et al. (2013)](/sources/arfken-2013.md), §18.1,
eqs. 18.1 and 18.9, pp. 871 and 875, where the generating function
$e^{-t^2+2tx}=\sum_nH_nt^n/n!$ is taken as the definition). Both books use
this "physicists'" standardization; neither mentions the polynomials
$\mathit{He}_n$ orthogonal with weight $e^{-x^2/2}$ (registry symbol reserved).

$$H_0=1,\quad H_1=2x,\quad H_2=4x^2-2,\quad H_3=8x^3-12x,\quad H_4=16x^4-48x^2+12,\quad H_5=32x^5-160x^3+120x$$
(Arfken et al., Table 18.1 to $n=6$, p. 873).

**Printed slip in Riley et al.** The list on p. 625 prints
$H_3(x)=8x^2-12x$ (checked on the page image). Riley's own series
(eq. 18.129) gives $8x^3-12x$, as does Arfken et al.'s Table 18.1; the
exponent is a typesetting error, not a different convention. It is recorded
here and on the [Source page](/sources/riley-2006.md) rather than corrected
silently.

## Properties

* **Parity and special values.** $H_n(-x)=(-1)^nH_n(x)$,
  $H_{2n}(0)=(-1)^n(2n)!/n!$, $H_{2n+1}(0)=0$ (Riley et al., pp. 625, 628;
  Arfken et al., eqs. 18.6–18.7, p. 874).
* **Recurrences.** $H_{n+1}=2xH_n-2nH_{n-1}$ and $H_n'=2nH_{n-1}$ (Riley
  et al., eqs. 18.134–18.135, p. 628, proofs set as Exercise 18.5; Arfken et
  al., eqs. 18.3–18.4, p. 872, derived from the generating function). Riley
  et al. note that the first gives a simple way to evaluate $H_n(x_0)$ from
  $H_0$ and $H_1$ (p. 628). See
  [three-term recurrences](/results/three-term-recurrences.md).
* **Rodrigues formula** $H_n=(-1)^ne^{x^2}\frac{d^n}{dx^n}e^{-x^2}$ (Riley
  et al., eq. 18.130, p. 626; Arfken et al., eq. 18.8, p. 874); see
  [Rodrigues formula](/results/rodrigues-formula.md).

## Orthogonality

$$\int_{-\infty}^{\infty}H_n(x)H_m(x)\,e^{-x^2}\,dx=2^n\,n!\,\sqrt\pi\;\delta_{nm}.$$
Riley et al. obtain the norm from the Rodrigues formula and
$d^nH_n/dx^n=2^nn!$ (eq. 18.132, p. 627); Arfken et al. from the product of
two generating functions integrated against $e^{-x^2}$ (eqs. 18.11–18.15,
pp. 875–876). The expansion is $f=\sum c_nH_n$ with
$c_n=(2^nn!\sqrt\pi)^{-1}\int fH_ne^{-x^2}dx$ (Riley et al., p. 627).

**Hermite functions.** $\varphi_n(x)=e^{-x^2/2}H_n(x)$ are orthogonal with
unit weight on $(-\infty,\infty)$ and satisfy the self-adjoint equation
$\varphi_n''+(2n+1-x^2)\varphi_n=0$; they are proportional to the
harmonic-oscillator eigenfunctions (Riley et al., p. 627; Arfken et al.,
eqs. 18.12–18.13, pp. 875–876). Neither founding source normalizes them to
unit norm in the sections read.

**Hypergeometric form.** $H_{2n}$ and $H_{2n+1}/x$ are confluent
hypergeometric functions $M(-n,\tfrac12;x^2)$ and $M(-n,\tfrac32;x^2)$ up to
factors (Riley et al., §18.11.1, p. 634).

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §18.9, eqs. 18.126–18.135, pp. 624–628; §18.11.1, p. 634; Exercise 18.5, pp. 641–642.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §18.1, eqs. 18.1–18.15, pp. 871–876; §12.1, Example 12.1.2, pp. 555–556.
