---
type: Definition
title: "Fourier transform"
description: "Integral representation of a non-periodic, absolutely integrable function as a superposition of modes exp(i k x), obtained as the infinite-period limit of the complex Fourier series; defined here with the symmetric 1/sqrt(2 pi) normalization, with sine and cosine transforms for odd and even functions, the multidimensional pair, and (in exercises) sampled and periodized forms."
status: established
aliases: [Fourier integral, Fourier transform pair, Fourier inversion theorem, Fourier sine transform, Fourier cosine transform]
tags: [fourier-transform]
timestamp: 2026-10-13T00:00:00Z
---

# Fourier transform

## Definition and normalization

For $f$ with $\int_{-\infty}^{\infty}\lvert f\rvert\,\mathrm dx$ finite — the
only requirement the source places on $f$ — the **Fourier transform** and its
inverse are ([Riley et al. (2006)](/sources/riley-2006.md), eqs. 13.5–13.6)
$$\hat f(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} f(x)\,e^{-\mathrm i k x}\,\mathrm dx,\qquad
f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\hat f(k)\,e^{\mathrm i k x}\,\mathrm dk,$$
written $\hat f = \mathcal F[f]$; the same pair holds in $(t,\omega)$. The
factor $1/\sqrt{2\pi}$ "is clearly arbitrary, the only requirement being that
the product of the constants in (13.5) and (13.6) should equal $1/(2\pi)$";
the source chooses the symmetric split (§13.1, p. 435). This bundle adopts it
as canonical (see the [notation registry](/notation.md)). Every constant in
the [convolution theorem](/results/convolution-theorem.md), the
[Wiener–Khinchin theorem](/results/wiener-khinchin-theorem.md) and
[Parseval's theorem](/results/parseval-theorem.md) depends on it.

## Fourier's inversion theorem

Writing the complex [Fourier series](/definitions/fourier-series.md) of a
function of period $T$ with $\omega_m = 2\pi m/T$, the spacing
$\Delta\omega = 2\pi/T$ tends to zero as $T\to\infty$ and the sum becomes an
integral (eqs. 13.1–13.3, fig. 13.1), giving **Fourier's inversion theorem**
(eq. 13.4):
$$f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\mathrm d\omega\,e^{\mathrm i\omega t}\int_{-\infty}^{\infty}\mathrm du\,f(u)\,e^{-\mathrm i\omega u}.$$
The derivation is a limiting argument, not a proof: the existence of
$\hat f(\omega)$ as $T\to\infty$ "is assumed here without proof" (p. 435).

## Sine and cosine transforms

For odd $f$ the transform is odd in $\omega$ and reduces to the **Fourier sine
transform** pair (eqs. 13.35–13.36)
$$\hat f_s(\omega) = \sqrt{\frac2\pi}\int_0^\infty f(t)\sin\omega t\,\mathrm dt,\qquad f(t) = \sqrt{\frac2\pi}\int_0^\infty \hat f_s(\omega)\sin\omega t\,\mathrm d\omega,$$
with $\hat f(\omega) = -\mathrm i\,\hat f_s(\omega)$ for odd $f$. The pair needs
$f$ only for $t > 0$. The cosine pair $\hat f_c$ is the same with $\cos$, for
even $f$ (§13.1.6, pp. 445–446).

## Higher dimensions

In three dimensions (eqs. 13.49–13.50)
$$\hat f(\mathbf k) = \frac{1}{(2\pi)^{3/2}}\int f(\mathbf r)\,e^{-\mathrm i\mathbf k\cdot\mathbf r}\,\mathrm d^3 r,\qquad
f(\mathbf r) = \frac{1}{(2\pi)^{3/2}}\int \hat f(\mathbf k)\,e^{\mathrm i\mathbf k\cdot\mathbf r}\,\mathrm d^3 k,$$
"and similar relations ... exist for spaces of other dimensionalities". For a
spherically symmetric $f(r)$,
$\hat f(k) = (2\pi)^{-3/2}\int_0^\infty 4\pi r^2 f(r)\,\frac{\sin kr}{kr}\,\mathrm dr$
(worked example, p. 452); the axisymmetric two-dimensional analogue is a
Hankel-type integral with $J_0$ (eq. 13.52).

## Spread in $x$ and $k$

The transform of the normalized Gaussian of root mean square width
$\sigma_t$ is the Gaussian $\hat f(\omega) = (2\pi)^{-1/2}\exp(-\sigma_t^2\omega^2/2)$
(eq. 13.7), of root mean square width $\sigma_\omega = 1/\sigma_t$, so
$\sigma_\omega\sigma_t = 1$ independently of the width, and "in an obvious
notation" $\sigma_k\sigma_x = 1$ for a Gaussian wave packet (§13.1.1,
p. 436). The completion of the square that yields eq. 13.7 is made plausible,
not proved; the source defers the contour-integral justification to its
ch. 24. For the intensities $\lvert f\rvert^2$ and $\lvert\hat f\rvert^2$ the
product of the widths is $\tfrac12$ for the Gaussian, and the source states
without proof that every other distribution gives a larger product, the
Gaussian giving the minimum (p. 437).

## Sampling and periodization (exercises only)

The chapter's text has no discrete transform. Three exercises state results
for the reader to prove:

* **Poisson summation formula** (exercise 13.9). The impulse train satisfies
  $\sum_{p}\delta(t + pT) = \frac1T\sum_p e^{-2\pi\mathrm i pt/T}$, and for any
  $f$ and period $T$ (the source writes this second period as $X$)
  $$\sum_{p=-\infty}^{\infty} f(t + pT) = \frac{\sqrt{2\pi}}{T}\sum_{p=-\infty}^{\infty}\hat f\!\left(\frac{2\pi p}{T}\right)e^{2\pi\mathrm i pt/T}.$$
* **Sampled transform** (exercise 13.10). With $N$ samples $f_j = f(x_j)$,
  $x_j = jh$, $j = 0,\dots,N-1$, it states $\hat f\bigl(2\pi m/(Nh)\bigr) \approx h\,F_m$
  with $F_m = \frac{1}{\sqrt{2\pi}}\sum_{j=0}^{N-1} f_j\,e^{-2\pi\mathrm i jm/N}$, which it
  calls a *discrete Fourier transform* (the source samples a function of
  time). In the registry's reserved normalization
  $F_m = \frac{N}{\sqrt{2\pi}}\hat f^{N}_m$, and the sampled wavenumber is
  $\xi = kh = 2\pi m/N$. For the unit box on $0\le x<1$ sampled with $N = 8$,
  $h = 0.25$, it asks the reader to "note the relatively good agreement for
  $m < 4$ and the lack of agreement for larger values". The source gives no
  reason and does not name aliasing or a Nyquist limit.
* **Reconstruction from samples of the spectrum** (exercise 13.11). If $f$
  vanishes outside $\lvert t\rvert < T/2$, then $\hat f$ is determined exactly
  by its values at $\omega = 2\pi p/T$:
  $\hat f(\omega) = \sum_p \hat f(2\pi p/T)\,\mathrm{sinc}(p\pi - \omega T/2)$,
  $\mathrm{sinc}\,u = (\sin u)/u$, via the series coefficients
  $\hat f_p = \frac{\sqrt{2\pi}}{T}\hat f(2\pi p/T)$.

A dedicated page for the discrete Fourier transform waits for a source that
develops it.

# Examples

* One-sided exponential decay, $f = Ae^{-\gamma t}$ for $t\ge0$ and $0$ for
  $t<0$ ($\gamma > 0$): $\hat f(\omega) = \frac{A}{\sqrt{2\pi}(\gamma + \mathrm i\omega)}$ (p. 435).
* Fraunhofer diffraction: the far-field intensity in a direction is
  proportional to $\lvert\hat f\rvert^2$ of the aperture function evaluated at
  the transverse wavenumber of that direction (eqs. 13.8–13.10).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§13.1–13.1.2, 13.1.6, 13.1.10 (pp. 433–453); exercises 13.9–13.11 (pp. 461–462).
