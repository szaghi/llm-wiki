---
type: Definition
title: "Dirac delta function"
description: "The generalized function defined by the sifting property, with its scaling and composition rules, its derivative, the Heaviside step as its integral, its Fourier representation as a uniform superposition of all modes, and its limiting representation by the band-limited sinc kernel."
status: established
aliases: [delta function, Dirac δ-function, Heaviside step function, unit step]
tags: [fourier-transform, generalized-function]
timestamp: 2026-10-14T00:00:00Z
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
[Arfken et al. (2013)](/sources/arfken-2013.md) write the step $u(t - t_0)$ and
leave its value at the jump unspecified (eq. 20.137). A compiler remark: their
eq. 20.146,
$\int_0^\infty \sin(tx)/x\,\mathrm dx = \frac\pi2[2u(t) - 1]$, gives the value $0$
they state at $t = 0$ only with $u(0) = \tfrac12$, the registry's choice.

## Fourier representation

Inserting the transform into [Fourier's inversion theorem](/definitions/fourier-transform.md)
gives (eq. 13.24)
$$\delta(t - u) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{\mathrm i\omega(t-u)}\,\mathrm d\omega,$$
"a complete spectrum of harmonic waves, all frequencies having the same
amplitude and all waves being in phase at $t = u$" (p. 442). Hence
$\hat\delta(\omega) = 1/\sqrt{2\pi}$ (eq. 13.27), and $\delta$ is real. In three
dimensions $\delta(\mathbf r) = (2\pi)^{-3}\int e^{\mathrm i\mathbf k\cdot\mathbf r}\,\mathrm d^3k$ (eq. 13.51).
Arfken et al. agree: the transform of $\delta$ is $1/\sqrt{2\pi}$ for all
$\omega$, "the ultimately localized $f(t)$", whose transform is "completely
delocalized" (eq. 20.14, p. 967). Their exercise 20.2.7 gives the sine and
cosine forms
$\delta(t - u) = \frac2\pi\int_0^\infty\sin\omega t\sin\omega u\,\mathrm d\omega = \frac2\pi\int_0^\infty\cos\omega t\cos\omega u\,\mathrm d\omega$
for $t, u > 0$.

On a period the representation is a Fourier series. On $(-\pi, \pi)$,
$\delta(x - u) = \frac{1}{2\pi} + \frac1\pi\sum_{m\ge1}\cos m(x - u) = \frac{1}{2\pi}\sum_{m=-\infty}^{\infty}e^{\mathrm im(x-u)}$
(Arfken et al., exercises 19.1.11, 19.2.2–19.2.3), Riley et al.'s impulse
train with $T = 2\pi$. Truncated at $\lvert m\rvert \le M$, this sum is the
kernel of the Fourier partial sum, which "is in the large-[$M$] limit a Dirac
delta distribution" (eq. 19.31, p. 958; see
[Gibbs phenomenon](/results/gibbs-phenomenon.md)).

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

Arfken et al. use the same band-limited sequence,
$\delta_n(t) = \frac{1}{2\pi}\int_{-n}^{n}e^{\mathrm i\omega t}\,\mathrm d\omega$,
"particularly useful in Fourier analysis", to derive the Fourier integral
(eq. 20.20). Their exercises 20.2.5–20.2.6 show that the rectangular and the
Gaussian sequences give the same integral representation, and 20.2.4 that the
triangular pulse is another delta sequence. The two sources agree.

## Laplace transform

(Arfken et al., eqs. 20.139–20.140, pp. 1010–1011.) For $t_0 > 0$,
$\mathcal L\{\delta(t - t_0)\} = e^{-st_0}$, as in Riley et al.'s table 13.1. At
$t_0 = 0$ the one-sided integral needs care. Consistent results follow from
delta sequences lying entirely in $t \ge 0$, which give
$\mathcal L\{\delta(t)\} = 1$. The source calls $\delta$ in this role the
*impulse function*.

## Uses

Convolution with a sum of deltas leaves a copy of the other function at each
delta (§13.1.7, p. 447; see [convolution](/definitions/convolution.md)), and
the periodic impulse train has a uniform Fourier series (exercise 13.9; see
[Fourier transform](/definitions/fourier-transform.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§13.1.3–13.1.4 (pp. 439–443), §13.1.10 (eq. 13.51).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §19.3 (eq. 19.31, p. 958), §20.2 (eqs. 20.14, 20.20, pp. 967–969), §20.7 (eqs. 20.137–20.140, 20.146, pp. 1010–1014); exercises 19.1.11, 19.2.2–19.2.4, 20.2.4–20.2.7.
