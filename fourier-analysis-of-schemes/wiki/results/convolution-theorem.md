---
type: Result
title: "Convolution theorem"
description: "The Fourier transform of a convolution is sqrt(2 pi) times the product of the transforms, and the transform of a product is 1/sqrt(2 pi) times the convolution of the transforms (constants of the unitary normalization); the Laplace transform of the one-sided convolution is the plain product of the Laplace transforms."
status: established
aliases: [Fourier convolution theorem, Laplace convolution theorem, Borel's theorem]
tags: [fourier-transform, laplace-transform, convolution]
timestamp: 2026-10-13T00:00:00Z
---

# Convolution theorem

## Fourier form

For the [convolution](/definitions/convolution.md) $f * g$ and the unitary
[Fourier transform](/definitions/fourier-transform.md)
([Riley et al. (2006)](/sources/riley-2006.md), eqs. 13.38–13.39):
$$\mathcal F[f * g] = \sqrt{2\pi}\,\hat f(k)\,\hat g(k),\qquad \mathcal F[f\,g] = \frac{1}{\sqrt{2\pi}}\,(\hat f * \hat g)(k).$$
The first is proved by exchanging the order of integration and substituting
$u = z - x$ (p. 448). The second "may be proved similarly" and is not written
out. The factors $\sqrt{2\pi}$ and $1/\sqrt{2\pi}$ belong to the symmetric
normalization. Under a non-symmetric pair the constants move, and a source
using one is mapped in its Notation map.

## Laplace form

For the one-sided convolution $\int_0^t f(u)\,g(t-u)\,\mathrm du$
(eq. 13.64):
$$\mathcal L\!\left[\int_0^t f(u)\,g(t - u)\,\mathrm du\right] = \mathcal L\{f\}(s)\,\mathcal L\{g\}(s),$$
so $\mathcal L^{-1}\bigl[\mathcal L\{f\}\,\mathcal L\{g\}\bigr] = f * g$. It is
proved by substituting $u + v = t$ and swapping the order of integration over
the wedge $0 \le u \le t$ (fig. 13.7, p. 458). No constant appears.

## Uses in the source

* Deconvolution: divide transforms (see [convolution](/definitions/convolution.md)).
* Two wide slits as the convolution of two deltas with a box gives the same
  transform as direct integration (p. 448).
* Exercise 13.12 writes a sampled signal passed through a triangular filter as
  a convolution and evaluates it with the theorem and the $\mathrm{sinc}^2$
  transform of a triangle (exercise 13.4). Exercise 13.27 checks the Laplace form on
  a box.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §13.1.7 (pp. 447–449), §13.2.2 (pp. 457–458); exercises 13.4, 13.12, 13.27.
