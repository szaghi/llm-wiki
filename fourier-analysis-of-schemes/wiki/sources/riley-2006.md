---
type: Source
title: "Riley, Hobson & Bence (2006) — Mathematical Methods for Physics and Engineering (3rd ed.)"
description: "Undergraduate textbook of mathematical methods; read for this bundle in its chapters on Fourier series, integral transforms (Fourier and Laplace) and the finite-difference sections of numerical methods, which supply the series and transform definitions, convergence and Gibbs statements, Parseval, convolution and correlation theorems, Laplace operational rules, basic difference operators, and illustrated (not analysed) instabilities of forward Euler and Milne's method."
resource: "doi:10.1017/CBO9780511810763"
source_kind: book
authors: [Riley K.F., Hobson M.P., Bence S.J.]
year: 2006
venue: "Cambridge University Press (3rd ed.)"
local_file: "/home/stefano/papers/mosaic/fourier-analysis-of-schemes/2006-CUP-Riley-101017CBO9780511810763.pdf"
tags: [textbook, fourier-series, fourier-transform, laplace-transform, finite-difference, stability]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A general textbook of mathematical methods in 31 chapters (index from p. 1305).
Its identity was verified from the title and copyright pages: third edition,
Cambridge University Press 2006, hardback ISBN 978-0-521-86153-3, paperback
978-0-521-67971-8. The DOI was verified on Crossref (monograph, edition 3).
The PDF is a scanned print with a text layer, and PDF page = printed page + 30.

**Scoped read.** For this bundle the compiler read the preface, the contents,
**ch. 12** (Fourier series, pp. 415–432), **ch. 13** (Integral transforms,
pp. 433–467, including all exercises and hints) and **§§27.5–27.6** (Finite
differences; Differential equations, pp. 1019–1028). Nothing else was read.
In particular the following were not read: ch. 15, where Laplace transforms
solve ODEs; ch. 17, the general theory of orthogonal expansions to which
§12.1 defers; ch. 24, contour integration, cited for eq. 13.7 and the
inversion of the exponential-decay transform; ch. 25, the inverse Laplace
transform by contour integration; and §27.7 onward, higher-order equations and
the numerical solution of PDEs. Any Fourier or stability content of those
parts is outside this ingestion.

What the chapters read **do not** contain is as important for this bundle.
There is no von Neumann stability analysis, no amplification factor of a
Fourier mode, no modified wavenumber, and no dispersion or dissipation
analysis of a difference scheme. The discrete Fourier transform, the Poisson
summation formula and spectral sampling appear only as exercises
(13.9–13.11). The stability content of §27.6 is two illustrated observations,
for forward Euler and for Milne's method, on one test equation.

Merged into the 21 concept pages listed in the audit below.

# Key claims

1. **Dirichlet conditions** (§12.1, p. 415). Periodic; single-valued and
   continuous except for finitely many finite discontinuities; finitely many
   extrema per period; $\int\lvert f\rvert$ over a period converges. Their
   sufficiency for a Fourier expansion is "stated without proof" (p. 416).
2. **Fourier series** (eqs. 12.4–12.6, 12.9–12.11): real and complex forms, the
   coefficients as integrals over a period, orthogonality (eqs. 12.1–12.3), and
   $\hat f_m = \tfrac12(a_m - \mathrm ib_m)$. Symmetry rules, including the
   quarter-period rules (§12.3).
3. **Periodic extension** (§12.5): an extension discontinuous at an end-point
   converges there to the mean, not to the end value (pp. 422–424).
4. **Convergence at a discontinuity** (§12.4, p. 420): to the mean of the
   one-sided limits, stated without proof.
5. **Gibbs phenomenon** (§12.4, p. 421): the overshoot moves arbitrarily
   close to the jump and never disappears; it is proportional to the jump. No
   proof and no numerical value are given.
6. **Term-by-term integration and differentiation** (§12.6, p. 424), the
   latter requiring $f$ continuous and periodic and $f'$ Dirichlet.
7. **Parseval for series** (eq. 12.13) and its two-function form (§12.8),
   with $\sum m^{-4} = \pi^4/90$ (p. 427).
8. **Fourier transform** with the symmetric $1/\sqrt{2\pi}$ normalization
   (eqs. 13.5–13.6). The inversion theorem (eq. 13.4) is reached by an
   infinite-period limit; existence is "assumed here without proof" (p. 435).
9. **Gaussian** (eq. 13.7): its transform is a Gaussian, and
   $\sigma_\omega\sigma_t = 1$ (p. 436).
10. **Dirac delta** (eqs. 13.11–13.27): sifting, scaling, composition,
    derivative, Heaviside $H' = \delta$, the Fourier representation (13.24) and
    the sinc limit (13.26).
11. **Transform properties** (eqs. 13.28–13.32), listed without proof except
    differentiation. The scaling rule is printed without $\lvert a\rvert$.
12. **Sine and cosine transforms** (eqs. 13.35–13.36). **Higher-dimensional
    transforms** (eqs. 13.47–13.52).
13. **Convolution** (eq. 13.37) and the **convolution theorem**
    $\mathcal F[f*g] = \sqrt{2\pi}\hat f\hat g$ (eq. 13.38), with its converse
    (eq. 13.39). Deconvolution is described, with a warning about its practical
    imprecision (p. 449).
14. **Cross-correlation** (eq. 13.40), non-commutative (eq. 13.41), and the
    **Wiener–Khinchin theorem** (eq. 13.42, spelled "Wiener–Kinchin"). The
    energy spectrum $\sqrt{2\pi}\lvert\hat f\rvert^2$ (p. 450).
15. **Parseval for transforms** (eqs. 13.44–13.46). The series form "is in fact
    a special case". In the damped-oscillator example (p. 451) the transform is
    computed without the $1/\sqrt{2\pi}$ of eq. 13.5, though it says "Using the
    usual definition"; the conclusion is hedged "to within a constant".
16. **Laplace transform** (eq. 13.53): $s$ real, abscissa $s_0$, table 13.1,
    inversion by table, uniqueness "for all practical purposes" (footnote,
    p. 454).
17. **Laplace operational rules**: derivatives (eqs. 13.57–13.58, printed
    "for $s > 0$"), integral (13.59), shifts (13.60 and p. 457), (13.61)–(13.63),
    convolution theorem (13.64).
18. **Exercises with stated results**: Poisson summation (13.9); the sampled
    "discrete Fourier transform"
    $F_m = \frac{1}{\sqrt{2\pi}}\sum_{j=0}^{N-1}f_je^{-2\pi\mathrm ijm/N}$ with
    $\hat f(2\pi m/(Nh)) \approx hF_m$, and poor agreement for $m \ge N/2$
    noted without explanation (13.10); reconstruction of $\hat f$ from samples
    for a time-limited $f$ (13.11); impulse response by Laplace transform
    (13.24); the limit $s\,\mathcal L\{f\}\to A$ (13.25).
19. **Difference operators** (§27.5): $D_0$ with error $\approx (h^2/6)f^{(3)}_j$
    (eq. 27.57); $D_\pm$ with error $\approx (h/2)f^{(2)}_j$ of opposite signs
    (eq. 27.58); $D_+D_-$ with error $\approx (h^2/12)f^{(4)}_j$ (eq. 27.59).
    Differences are exact for low-degree polynomials.
20. **Forward Euler on $\mathrm dy/\mathrm dt = -y$** (eq. 27.63, table 27.10).
    The solution oscillates for $\Delta t > 1$ and diverges for $\Delta t > 2$.
    The source states: "a necessary condition for non-divergence is
    $\lvert\lambda\rvert < 1$, i.e. $0 < h < 2$, though in no way does this
    ensure accuracy" (p. 1021). Scope: this one linear test equation.
21. **Milne's method** (eqs. 27.64–27.65, table 27.11). It soon "runs into
    difficulties", which the source attributes to rounding errors exciting the
    growing solution of $\mathrm dy/\mathrm dt = +y$. The difficulties are
    "only illustrated, rather than analysed"; summary: "(i) insufficiently
    precise approximations to the derivatives and (ii) inherent instability due
    to rounding errors" (pp. 1022–1023).
22. **Out of scope, read but not compiled**: Taylor-series solution
    (§27.6.2), the Adams method and predictor–corrector schemes (§27.6.3),
    Runge–Kutta of orders 2–4 (§27.6.4, eqs. 27.76–27.80, the third- and
    fourth-order schemes "given without derivation"), and isoclines (§27.6.5).
    None carries a Fourier-analysis or stability statement, and scheme design
    is out of this bundle's scope. The Fraunhofer-diffraction, uncertainty
    principle and amplitude-modulation applications of ch. 13 are kept only as
    examples.

# Notation map

| Riley et al. | Registry | Note |
|---|---|---|
| $r$ (series index) | $m$ | mode index |
| $2\pi r/L$ | $k_m$ | wavenumber of mode $m$ |
| $a_r$, $b_r$ | $a_m$, $b_m$ | same normalization |
| $c_r$ | $\hat f_m$ | complex series coefficient, same normalization |
| $\gamma_r$ | $\hat g_m$ | coefficients of $g$ (§12.8) |
| $\omega_r = 2\pi r/T$; $\omega = 2\pi/T$ (eq. 12.8) | $\omega_m$; $\omega_1$ | |
| $\tilde f(\omega)$, $\tilde f(k)$ | $\hat f(\omega)$, $\hat f(k)$ | same symmetric normalization and sign |
| $\mathcal F[f]$ | $\mathcal F[f]$ | |
| $\tilde f_s$ | $\hat f_s$ | sine transform |
| $\bar f(s)$, $\mathcal L[f(t)]$ | $\mathcal L\{f\}(s)$ | overbar not used; braces, not brackets |
| $\Delta t$, $\Delta\omega$, $\Delta x$, $\Delta k$ (spreads, §13.1.1) | $\sigma_t$, $\sigma_\omega$, $\sigma_x$, $\sigma_k$ | $\Delta$ is reserved for steps |
| $\tau$ (Gaussian width, §13.1.1) | $\sigma_t$ | |
| $\tau$ (sample spacing, ex. 13.10) | $h$ | samples written in $x$ |
| $n$ (sample index), $k$ (DFT index), $F_k$ (ex. 13.10) | $j$, $m$, $F_m = \frac{N}{\sqrt{2\pi}}\hat f^{N}_m$ | registry DFT reserved |
| $X$ (period, ex. 13.9) | $T$ | |
| $\lambda$ (decay rate, p. 435) | $\gamma$ | |
| $h(z)$ (observed distribution) | $q(z)$ | $h$ is the grid spacing |
| $C(z)$, $a(z)$ | $C_{fg}(z)$, $C_{ff}(z)$ | cross- and auto-correlation |
| $h(t)$ in $\delta(h(t))$ | $\phi(t)$ | |
| $\phi$, $K$ (ex. 13.5) | $\varphi$, $\kappa_0$ | |
| $\omega_c$ | $\omega_c$ | carrier frequency |
| $n$ (integer in Laplace table, Poisson sums) | $p$ | $n$ is reserved for time levels |
| $x_i$, $f_i$, $f_i^{(n)}$ (§27.5) | $x_j$, $f_j$, $f^{(p)}_j$ | spatial grid |
| $(f_{i+1}-f_{i-1})/(2h)$ etc. | $D_0 f_j$, $D_\pm f_j$, $D_+D_-f_j$ | operator symbols are the registry's |
| $x$, $h$, $y_i$ (ODE, §27.6) | $t$, $\Delta t$, $y^n$ | ODE in time |
| $f(x, y)$ (ODE right-hand side) | $F(t, y)$ | |
| $\lambda$ in $y_{i+1} = \lambda y_i$ (p. 1021) | $G$ | one-step amplification factor |
| $T$, $x$ (ex. 13.24) | $\gamma^{-1}$, $y$ | |

# Audit

Created in this run (2026-10-13):

* Created [Notation registry](/notation.md)
* Created [Dirichlet conditions](/definitions/dirichlet-conditions.md)
* Created [Fourier series](/definitions/fourier-series.md)
* Created [Fourier transform](/definitions/fourier-transform.md)
* Created [Dirac delta function](/definitions/dirac-delta-function.md)
* Created [Convolution](/definitions/convolution.md)
* Created [Cross-correlation and energy spectrum](/definitions/cross-correlation.md)
* Created [Laplace transform](/definitions/laplace-transform.md)
* Created [Convergence of Fourier series](/results/fourier-series-convergence.md)
* Created [Gibbs phenomenon](/results/gibbs-phenomenon.md)
* Created [Parseval's theorem](/results/parseval-theorem.md)
* Created [Convolution theorem](/results/convolution-theorem.md)
* Created [Wiener–Khinchin theorem](/results/wiener-khinchin-theorem.md)
* Created [Fourier transform properties](/results/fourier-transform-properties.md)
* Created [Laplace transform properties](/results/laplace-transform-properties.md)
* Created [Central first difference $D_0$](/operators/central-difference.md)
* Created [One-sided first differences $D_+$, $D_-$](/operators/one-sided-differences.md)
* Created [Second central difference $D_+D_-$](/operators/second-central-difference.md)
* Created [Forward Euler method](/methods/forward-euler-method.md)
* Created [Milne's central-difference method](/methods/milne-central-difference-method.md)
* Created [Square wave](/benchmarks/square-wave.md)
* Created [Exponential-decay test equation](/benchmarks/exponential-decay-test-equation.md)

# Citations

The chapters read print no reference list and cite no external work by name.
The only attribution is a footnote crediting the plane-wave approach of
eq. 13.8 to Fresnel, without a reference, and §27.6.3 refers the reader to
"more specialist texts" without naming any. The bibliography therefore holds
only this source.
