---
type: Definition
title: "Dirac delta function"
description: "The generalized function defined by the sifting property, with its scaling and composition rules, its derivative, the Heaviside step as its integral, its Fourier representation as a uniform superposition of all modes, and its limiting representation by the band-limited sinc kernel."
status: established
aliases: [delta function, Dirac δ-function, Heaviside step function, unit step]
tags: [fourier-transform, generalized-function]
timestamp: 2026-10-13T00:00:00Z
---

# Dirac delta function

## Defining property

The **Dirac delta function** satisfies $\delta(t) = 0$ for $t \ne 0$ (eq. 13.11),
and its fundamental defining property is the sifting relation
([Riley et al. (2006)](/sources/riley-2006.md), eq. 13.12)
$$\int f(t)\,\delta(t - a)\,\mathrm dt = f(a)$$
when the range of integration includes $t = a$, and zero otherwise. From it
(eqs. 13.13–13.19):
$$\int_{-a}^{b}\delta(t)\,\mathrm dt = 1\ (a,b>0),\qquad \delta(-t) = \delta(t),\qquad \delta(at) = \frac{\delta(t)}{\lvert a\rvert},\qquad t\,\delta(t) = 0,$$
$$\delta(\phi(t)) = \sum_i\frac{\delta(t - t_i)}{\lvert \phi'(t_i)\rvert}\ \text{over the zeros } t_i \text{ of } \phi,\qquad \int_{-\infty}^{\infty} f(t)\,\delta'(t)\,\mathrm dt = -f'(0).$$
The source states that "a rigorous mathematical definition exists" but does
not give it (§13.1.3, p. 439). In three dimensions
$\delta(\mathbf r - \mathbf r_0) = \delta(x - x_0)\delta(y-y_0)\delta(z-z_0)$ (eq. 13.21).

## Heaviside step

The **Heaviside step** $H(t)$ is $1$ for $t > 0$ and $0$ for $t < 0$, with the
usual choice $H(0) = \tfrac12$ (eq. 13.22), and $H'(t) = \delta(t)$
(eq. 13.23, proved by integration by parts against a test function).

## Fourier representation

Inserting the transform into [Fourier's inversion theorem](/definitions/fourier-transform.md)
gives (eq. 13.24)
$$\delta(t - u) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{\mathrm i\omega(t-u)}\,\mathrm d\omega,$$
"a complete spectrum of harmonic waves, all frequencies having the same
amplitude and all waves being in phase at $t = u$" (p. 442). Hence
$\hat\delta(\omega) = 1/\sqrt{2\pi}$ (eq. 13.27), and $\delta$ is real. In three
dimensions $\delta(\mathbf r) = (2\pi)^{-3}\int e^{\mathrm i\mathbf k\cdot\mathbf r}\,\mathrm d^3k$ (eq. 13.51).

## Band-limited approximation

Truncating the uniform spectrum to $\lvert\omega\rvert \le \Omega$ gives
$f_\Omega(t) = \frac{2\Omega}{\sqrt{2\pi}}\,\mathrm{sinc}(\Omega t)$ (eq. 13.25,
fig. 13.4), which grows and narrows at $t = 0$ as $\Omega$ grows, so that
(eq. 13.26)
$$\delta(t) = \lim_{\Omega\to\infty}\frac{\sin\Omega t}{\pi t}.$$
Limits of rectangular, triangular or Gaussian distributions are "equally
valid" representations, provided the area is known and no undefined operation
is carried out on $\delta$ while a non-explicit representation is used
(p. 443).

## Uses

Convolution with a sum of deltas leaves a copy of the other function at each
delta (§13.1.7, p. 447; see [convolution](/definitions/convolution.md)), and
the periodic impulse train has a uniform Fourier series (exercise 13.9; see
[Fourier transform](/definitions/fourier-transform.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§13.1.3–13.1.4 (pp. 439–443), §13.1.10 (eq. 13.51).
