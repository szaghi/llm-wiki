---
type: Result
title: "Wiener–Khinchin theorem"
description: "The Fourier transform of the cross-correlation of f and g is sqrt(2 pi) times conj(f-hat) times g-hat, so the auto-correlation of f is the inverse transform of the energy spectrum sqrt(2 pi) |f-hat|^2; the converse gives the transform of conj(f) g as the cross-correlation of the transforms."
status: established
aliases: [Wiener–Kinchin theorem, Wiener-Khintchine theorem, correlation theorem]
tags: [fourier-transform, spectrum]
timestamp: 2026-10-13T00:00:00Z
---

# Wiener–Khinchin theorem

For the [cross-correlation](/definitions/cross-correlation.md)
$C_{fg}(z) = \int f^*(x)\,g(x+z)\,\mathrm dx$ and the unitary
[Fourier transform](/definitions/fourier-transform.md)
([Riley et al. (2006)](/sources/riley-2006.md), eq. 13.42):
$$\hat C_{fg}(k) = \sqrt{2\pi}\,\hat f^*(k)\,\hat g(k),$$
proved like the [convolution theorem](/results/convolution-theorem.md) with the
substitution $u = x + z$ (p. 450). The converse, stated without its
derivation, is $\mathcal F[f^* g] = \frac{1}{\sqrt{2\pi}}\,\hat f\otimes\hat g$.
The source spells the name "Wiener–Kinchin".

## Consequences

* With $g = f$: the auto-correlation $C_{ff}$ is the inverse transform of
  $\sqrt{2\pi}\,\lvert\hat f(k)\rvert^2$, the energy spectrum (p. 450).
* Inverting gives (eq. 13.44)
  $C_{fg}(z) = \int_{-\infty}^{\infty}\hat f^*(k)\,\hat g(k)\,e^{\mathrm ikz}\,\mathrm dk$;
  at $z = 0$ this is the multiplication theorem, the general form of
  [Parseval's theorem](/results/parseval-theorem.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §13.1.8 (pp. 449–450), §13.1.9 (eq. 13.44, p. 451).
