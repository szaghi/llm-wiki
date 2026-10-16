---
okf_version: "0.1"
---

# orthogonal-polynomials-and-quadrature — Knowledge Bundle

Orthogonal polynomials and the special functions built on them, as the bases and quadratures of numerical methods: Legendre, Chebyshev, Jacobi, Hermite and Laguerre polynomials, associated Legendre functions and spherical harmonics, Bessel functions, three-term recurrences, Rodrigues formulae, Gauss, Gauss-Radau and Gauss-Lobatto quadrature, and their use in spectral, DG and multipole methods.

**Start here:** the [Notation registry](/notation.md), which is normative
for every page, and the [update log](/log.md).

**Corpus:** 3 sources. Two textbooks read in scope:
[Riley et al. (2006)](/sources/riley-2006.md), Ch. 18 and §27.4, and
[Arfken et al. (2013)](/sources/arfken-2013.md), §12.1, Chs. 14–15 and
§§18.1, 18.3, 18.4. One paper, [Panici et al. (2023)](/sources/panici-2023.md),
read for its Zernike (Fourier–Zernike) spectral basis and its radial
convergence. Gauss–Radau, Gauss–Lobatto, Jacobi polynomials,
Lebesgue constants and nodal bases are in scope but not yet covered by any
source; their symbols are reserved in the registry. The
[bibliography](/bibliography.md) lists the 86 works the three sources cite.

## Reading guide

1. **The general object.**
   [Orthogonal polynomials with respect to a weight function](/definitions/orthogonal-polynomials.md)
   — weight, interval, norm, orthogonal expansion, and the table of the
   classical families with their weights and norms.
2. **The three structural results every family shares.**
   [Rodrigues formula](/results/rodrigues-formula.md) (the general
   Sturm–Liouville construction),
   [generating functions](/results/generating-functions.md), and
   [three-term recurrences](/results/three-term-recurrences.md), the
   evaluation route both books recommend.
3. **The families on $[-1,1]$, the bases of spectral and DG methods.**
   [Legendre polynomials](/definitions/legendre-polynomials.md) (with
   $Q_n$), then [Chebyshev polynomials](/definitions/chebyshev-polynomials.md)
   (with the Gegenbauer generating function and the minimax remark).
4. **Quadrature.** [Gaussian quadrature](/methods/gaussian-quadrature.md)
   (idea, exactness as stated, the Laguerre and Hermite rules), then
   [Gauss–Legendre quadrature](/methods/gauss-legendre-quadrature.md) and
   [Gauss–Chebyshev quadrature](/methods/gauss-chebyshev-quadrature.md); the
   equally spaced contrast is
   [trapezium and Simpson rules](/methods/trapezium-and-simpson-rules.md).
   The quadrature pages rest on Riley et al. alone.
5. **Functions on the sphere and multipoles.**
   [Associated Legendre functions](/definitions/associated-legendre-functions.md)
   (read the Condon–Shortley convention section first),
   [spherical harmonics](/definitions/spherical-harmonics.md), the
   [addition theorem](/results/spherical-harmonic-addition-theorem.md), and
   the [Legendre expansion of the inverse distance](/results/legendre-expansion-of-inverse-distance.md).
6. **Unbounded intervals.**
   [Laguerre and associated Laguerre polynomials](/definitions/laguerre-polynomials.md)
   on $[0,\infty)$ and [Hermite polynomials](/definitions/hermite-polynomials.md)
   on the real line.
7. **Bessel functions.** [Bessel functions](/definitions/bessel-functions.md)
   (series, recurrences, zeros, asymptotics),
   [Fourier–Bessel series](/results/fourier-bessel-series.md), and
   [spherical Bessel functions](/definitions/spherical-bessel-functions.md).
8. **The unit disc.** [Zernike polynomials and the Fourier–Zernike basis](/definitions/zernike-polynomials.md)
   (radial polynomials, regularity at the origin, a measured exponential
   radial convergence; rests on one paper, with compiler-supplied
   hypothesis-grade Jacobi and orthogonality relations).

## Conventions to watch

* $P_\ell^m$ carries the Condon–Shortley factor $(-1)^m$ (Arfken et al.);
  Riley et al.'s $P_\ell^m$ lacks it, but the two books' $Y_\ell^m$ agree.
* $H_n$ is the physicists' Hermite polynomial in both books.
* The two books print different, equally valid generating functions for
  $T_n$.
* Panici et al.'s printed formula for the radial Zernike polynomial (their
  eq. 3.19) has a sign slip; use the formula on the Zernike page.

## Folders

* [Definitions](/definitions/index.md) · [Methods](/methods/index.md) ·
  [Results](/results/index.md) · [Sources](/sources/index.md)
* [Operators](/operators/index.md), [Properties](/properties/index.md),
  [Benchmarks](/benchmarks/index.md), [Software](/software/index.md): empty.
