---
type: Definition
title: "Fourier series"
description: "Expansion of a periodic function of period L in the mutually orthogonal modes cos and sin of k_m x (real form) or exp(i k_m x) (complex form), with coefficients given by integrals over one period; symmetry of the function removes coefficient families, and a function on a finite range is expanded through a chosen periodic extension."
status: established
aliases: [trigonometric series, complex Fourier series, Fourier coefficients, half-range series, periodic extension]
tags: [fourier-series]
timestamp: 2026-10-14T00:00:00Z
---

# Fourier series

The **Fourier series** of a function $f(x)$ of period $L$ is its expansion in
sines and cosines of the wavenumbers $k_m = 2\pi m/L$
([Riley et al. (2006)](/sources/riley-2006.md), eq. 12.4):
$$f(x) = \frac{a_0}{2} + \sum_{m=1}^{\infty}\bigl[a_m\cos k_m x + b_m\sin k_m x\bigr],$$
with the **Fourier coefficients** (eqs. 12.5–12.6)
$$a_m = \frac2L\int_{x_0}^{x_0+L} f(x)\cos k_m x\,\mathrm dx,\qquad b_m = \frac2L\int_{x_0}^{x_0+L} f(x)\sin k_m x\,\mathrm dx,$$
where $x_0$ is arbitrary (often $0$ or $-L/2$). The factor $\tfrac12$ on $a_0$
makes the formula for $a_m$ hold at $m = 0$ as well. A function that may be
expanded this way is one satisfying the
[Dirichlet conditions](/definitions/dirichlet-conditions.md).
[Arfken et al. (2013)](/sources/arfken-2013.md) give the same expansion for
period $2\pi$ (eqs. 19.1–19.3) and for a period they write $2L$
(eqs. 19.10–19.12). Their $L$ is half the registry's period; after that
rescaling the coefficient formulas are identical.

## Orthogonality

The coefficient formulas follow from the orthogonality of the modes over one
period (eqs. 12.1–12.3), for integers $m, p \ge 0$:
$$\int_{x_0}^{x_0+L}\sin k_m x\cos k_p x\,\mathrm dx = 0,\qquad
\int_{x_0}^{x_0+L}\cos k_m x\cos k_p x\,\mathrm dx = \begin{cases}L & m=p=0\\ \tfrac12 L & m=p>0\\ 0 & m\ne p\end{cases},$$
and the same for $\sin\sin$ except that it vanishes for $m = p = 0$.
Multiplying the series by $\cos k_p x$ (or $\sin k_p x$), integrating over a
period and exchanging sum and integral isolates one coefficient (eq. 12.7);
the source does not discuss the legitimacy of that exchange.

Arfken et al. reach orthogonality and more through Sturm–Liouville theory
(§19.1, pp. 936–937). The problem $-y'' = \lambda y$ on $[0, 2\pi]$ with
periodic boundary conditions is Hermitian, so its eigenfunctions
$\cos mx$, $\sin mx$ (or $e^{\mathrm imx}$) form a complete set, and those of
different eigenvalue $m^2$ are orthogonal. The functions $e^{\mathrm imx}/\sqrt{2\pi}$
are orthonormal. Completeness gives the source's convergence statement:
expansions of square-integrable functions "will at least converge in the mean"
(see [convergence of Fourier series](/results/fourier-series-convergence.md)).
The modes are also orthogonal over $N$ equally spaced points, the basis of the
[discrete Fourier transform](/definitions/discrete-fourier-transform.md).

## Complex form

With $e^{\mathrm i u} = \cos u + \mathrm i\sin u$ the series is
(eqs. 12.9–12.10)
$$f(x) = \sum_{m=-\infty}^{\infty}\hat f_m\,e^{\mathrm i k_m x},\qquad \hat f_m = \frac1L\int_{x_0}^{x_0+L} f(x)\,e^{-\mathrm i k_m x}\,\mathrm dx,$$
derived from the orthogonality relation: $\int_{x_0}^{x_0+L} e^{-\mathrm i k_p x}e^{\mathrm i k_m x}\,\mathrm dx$
equals $L$ for $m = p$ and $0$ for $m \ne p$. The two forms are related by (eq. 12.11)
$$\hat f_m = \tfrac12(a_m - \mathrm i b_m),\qquad \hat f_{-m} = \tfrac12(a_m + \mathrm i b_m),$$
so that a real $f$ has $\hat f_{-m} = \hat f_m^{*}$ (§12.7, p. 425).
Arfken et al. print the same relations (eqs. 19.4–19.6) and ask for the
reality condition as exercise 19.1.3. Their series coefficient carries
$e^{-\mathrm imt}$ (p. 958), the registry's sign, although their Fourier
*transform* uses the opposite sign (see the
[Fourier transform](/definitions/fourier-transform.md)).

## Symmetry

(§12.3, pp. 419–420.)

* $f$ odd: all $a_m = 0$ (sine series). $f$ even: all $b_m = 0$ (cosine series).
* $f$ even about $L/4$, i.e. $f(L/4 - x) = f(x - L/4)$: $a_{2p+1} = 0$ and $b_{2p} = 0$.
* $f$ odd about $L/4$: $a_{2p} = 0$ and $b_{2p+1} = 0$.

The source calls the quarter-period results "less obvious" and less used; it
derives them from the substitution $s = x - L/4$. Arfken et al. state the
even and odd cases, with coefficients computed from half a period (the
"Fourier cosine and Fourier sine series", eqs. 19.13–19.14, p. 941), and do
not treat the quarter-period rules.

## Non-periodic functions: periodic extension

A function wanted only on a finite range is first continued outside it to a
periodic function, whose series then represents it on that range only (§12.5,
pp. 422–424). The continuation is a choice. Continuing $f$ given on $0 < x \le L/2$
as an odd or an even function gives a sine-only or cosine-only series of
period $L$ (fig. 12.4). The source adds a constraint: the continuation
"must not be discontinuous at the end-points of the interval of interest; if
it is the series will not converge to the required value there" (p. 422).
Example: $f(x) = x^2$ on $0 < x \le 2$, continued evenly to period 4, gives
$$x^2 = \frac43 + 16\sum_{m=1}^\infty\frac{(-1)^m}{\pi^2 m^2}\cos\frac{\pi m x}{2},$$
whereas the odd continuation gives a sine series that converges to $0$, not to
$f(\pm 2) = \pm 4$, at $x = \pm 2$ (pp. 423–424; exercise 12.18). The choice of
continuation also sets the decay rate of the coefficients. Exercise 12.8 asks
for the faster-converging of the even and odd series of $x\sin x$ on
$[0,\pi]$ and states that it converges as $m^{-3}$. Exercise 12.6 asks which
of the sine and cosine series of $1 - x$ on $[0, 1]$ "would be better for
numerical evaluation", relating the answer to the continuations.

Arfken et al. agree. A non-periodic function still has an expansion, but it
depends on how the interval is chosen, and "because no information outside
the expansion interval was used … we can have no realistic expectation that
the expansion will produce there a reasonable approximation" (p. 940). Their
Example 19.1.2 expands $x$ on $[0, \pi]$ as a sine series, a cosine series
and a power series. All three agree on $[0, \pi]$ and differ outside it
(fig. 19.3; see [sawtooth wave](/benchmarks/sawtooth-wave.md)).

## Travelling waves and harmonics

Arfken et al. read the modes as waves (§19.1, pp. 939–940). Replacing $x$ by
$x - c_0t$ makes each term a wave of wavenumber $k_m$ moving at the phase
speed $c_0$. Mode $m = 1$ is the fundamental and $m > 1$ are its harmonics.
The substitution "carries the implicit assumption that the wave form retains
the same shape as it moves forward". That holds because every term has the
same phase velocity, which corresponds to "the notion that the medium … can
respond equally well to forces at all frequencies". The source adds in a
footnote: "For waves in physical media, this assumption is by no means always
true". Components the medium cannot follow are attenuated, and resonant ones
are enhanced. Superposing the response mode by mode needs the problem to be
linear: "in nonlinear problems an overall solution is not a superposition of
component solutions". Whether the harmonics "were there all along" is, in the
source's view, a matter of the chosen expansion. Exercise 19.1.2 writes the
series with amplitudes $\alpha_m = (a_m^2 + b_m^2)^{1/2}$ and phases. As a
function of $m$, $\alpha_m^2$ is "what is called the power spectrum", and it
is invariant under a shift of the phases.

# Examples

* Square wave: see [square wave](/benchmarks/square-wave.md) (eq. 12.8).
* $f(x) = x$ on $-2 < x < 2$: $\hat f_m = \frac{2\mathrm i(-1)^m}{\pi m}$ for $m \ne 0$, $\hat f_0 = 0$ (eq. 12.12). This is the [sawtooth wave](/benchmarks/sawtooth-wave.md), Arfken et al.'s Example 19.1.1.
* Full-wave rectifier, $\lvert\sin x\rvert$ (expanded on period $2\pi$): an even function with only even harmonics, $\frac2\pi - \frac4\pi\sum_{m=2,4,\dots}\frac{\cos mx}{m^2-1}$ (Arfken et al., eq. 19.28, written there in $\omega t$). Its coefficients fall as $m^{-2}$, against $m^{-1}$ for the discontinuous square wave (p. 951).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§12.1–12.3, 12.5, 12.7 (pp. 415–425); exercises 12.6, 12.8, 12.18.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §19.1 (eqs. 19.1–19.6, 19.10–19.14, Example 19.1.2, pp. 935–941), §19.2 (eqs. 19.27–19.28, pp. 950–951), §19.3 (p. 958); exercises 19.1.2, 19.1.3.
