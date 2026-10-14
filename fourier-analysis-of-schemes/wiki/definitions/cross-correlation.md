---
type: Definition
title: "Cross-correlation and energy spectrum"
description: "The cross-correlation of f and g, the integral of conj(f(x)) g(x + z) over x, measures their similarity as one is displaced by z; it is associative and distributive but not commutative, and the auto-correlation of f is the inverse transform of sqrt(2 pi) |f-hat|^2, which defines the energy spectrum."
status: established
aliases: [cross-correlation function, auto-correlation function, autocorrelation, energy spectrum, power spectrum]
tags: [fourier-transform, spectrum]
timestamp: 2026-10-13T00:00:00Z
---

# Cross-correlation and energy spectrum

The **cross-correlation** of $f$ and $g$ is
([Riley et al. (2006)](/sources/riley-2006.md), eq. 13.40)
$$C_{fg}(z) = (f\otimes g)(z) = \int_{-\infty}^{\infty} f^*(x)\,g(x + z)\,\mathrm dx.$$
Despite its formal similarity to [convolution](/definitions/convolution.md),
its use is different: it measures how similar $f$ and $g$ are as one is
displaced by $z$ relative to the other. It is associative and distributive,
but not commutative (eq. 13.41):
$$(f\otimes g)(z) = \bigl[(g\otimes f)(-z)\bigr]^*.$$

With $g = f$ it is the **auto-correlation** (eq. 13.43)
$$C_{ff}(z) = \int_{-\infty}^{\infty} f^*(x)\,f(x+z)\,\mathrm dx.$$
By the [Wiener–Khinchin theorem](/results/wiener-khinchin-theorem.md),
$C_{ff}$ is the inverse Fourier transform of $\sqrt{2\pi}\,\lvert\hat f(k)\rvert^2$,
"which is in turn called the **energy spectrum** of $f$" (p. 450). In the
damped-oscillator example the source reads $\lvert\hat f(\omega)\rvert^2$ as
"the energy content per unit frequency interval" (p. 451). The two statements
differ by the constant $\sqrt{2\pi}$; the source does not reconcile them, and
the example itself is computed without the $1/\sqrt{2\pi}$ of the definition
(see [Parseval's theorem](/results/parseval-theorem.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §13.1.8 (pp. 449–450), §13.1.9 (p. 451).
