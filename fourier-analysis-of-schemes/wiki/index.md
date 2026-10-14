---
okf_version: "0.1"
---

# fourier-analysis-of-schemes — Knowledge Bundle

Fourier series and transforms and their use on discretizations: convergence, Gibbs phenomenon, Parseval, the discrete Fourier transform, von Neumann stability, modified wavenumber, numerical dispersion and dissipation, spectral resolution of finite-difference and finite-volume schemes.

**Start here:** the [Notation registry](/notation.md), which is normative
for every page. It fixes the symmetric $1/\sqrt{2\pi}$ transform pair with
forward kernel $e^{-\mathrm ikx}$, the $1/N$ discrete coefficient
$\hat f^N_m$ and the scaled wavenumber $\xi = kh$, and reserves $\tilde\xi$
and $G$ for later sources. Sources with other conventions are mapped in their
Notation maps. The [update log](/log.md) records every change.

**Corpus:** 2 sources, both scoped reads of textbooks:
[Riley, Hobson & Bence (2006)](/sources/riley-2006.md), chs. 12, 13 and
§§27.5–27.6, and [Arfken, Weber & Harris (2013)](/sources/arfken-2013.md),
chs. 19 and 20. They supply the continuum tools and the discrete Fourier
transform, and most results now carry two citations. The Fourier analysis of
schemes proper (von Neumann stability, modified wavenumber, dispersion and
dissipation) has no page yet. Neither book treats it, so it waits for its
sources.

## Reading guide

**1. Representing a function by modes.**

* [Fourier series](/definitions/fourier-series.md): periodic functions, coefficients, symmetry, periodic extension.
* [Dirichlet conditions](/definitions/dirichlet-conditions.md): when an expansion exists.
* [Fourier transform](/definitions/fourier-transform.md): the non-periodic limit and its normalization (and the sign convention on which the two sources differ), with the sampling exercises (Poisson summation, a sampled transform).
* [Discrete Fourier transform](/definitions/discrete-fourier-transform.md): $N$ samples to $N$ coefficients, discrete orthogonality, aliasing and the FFT. It is the bundle's first discrete Fourier object.

**2. How well the modes represent the function.**

* [Convergence of Fourier series](/results/fourier-series-convergence.md): pointwise, at jumps, term by term.
* [Gibbs phenomenon](/results/gibbs-phenomenon.md): the persistent overshoot at a jump, about 18% of the half-jump.
* [Square wave](/benchmarks/square-wave.md) and [sawtooth wave](/benchmarks/sawtooth-wave.md): the test functions for both.

**3. Energy and products in mode space.**

* [Parseval's theorem](/results/parseval-theorem.md)
* [Convolution](/definitions/convolution.md) and the [convolution theorem](/results/convolution-theorem.md)
* [Cross-correlation and energy spectrum](/definitions/cross-correlation.md) and the [Wiener–Khinchin theorem](/results/wiener-khinchin-theorem.md)
* [Fourier transform properties](/results/fourier-transform-properties.md): differentiation is multiplication by $\mathrm ik$, the exact symbol any difference operator is later compared against. The page also gives the exact mode evolution of the wave and heat equations.
* [Dirac delta function](/definitions/dirac-delta-function.md): the uniform spectrum and its band-limited approximation.

**4. Initial-value problems.**

* [Laplace transform](/definitions/laplace-transform.md) and [its properties](/results/laplace-transform-properties.md): derivatives become algebra carrying the initial data, and the Bromwich integral inverts the transform.

**5. Discretization: the objects later Fourier analysis acts on.**

* Operators: [central difference $D_0$](/operators/central-difference.md), [one-sided differences $D_\pm$](/operators/one-sided-differences.md), [second difference $D_+D_-$](/operators/second-central-difference.md). Each page gives its Taylor truncation error.
* [Exponential-decay test equation](/benchmarks/exponential-decay-test-equation.md), with [forward Euler](/methods/forward-euler-method.md) (non-divergence for $0 < \Delta t < 2$ as printed) and [Milne's method](/methods/milne-central-difference-method.md) (parasitic growth). These are the only stability statements so far: illustrated in the source, not analysed. The compiler notes on both pages are hypotheses.

The [bibliography](/bibliography.md) holds the citation record.
