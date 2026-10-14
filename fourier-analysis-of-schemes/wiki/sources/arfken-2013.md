---
type: Source
title: "Arfken, Weber & Harris (2013) — Mathematical Methods for Physicists (7th ed.)"
description: "Graduate textbook of mathematical methods; read for this bundle in its chapters on Fourier series and integral transforms, which corroborate the founding source's series, transform, Parseval, convolution and Laplace results under a different sign convention, and add the quantified Gibbs overshoot, coefficient-decay rules, transform solutions of the wave, heat and Poisson equations, the Bromwich inversion, and the discrete Fourier transform with aliasing and the FFT."
resource: "doi:10.1016/C2009-0-30629-7"
source_kind: book
authors: [Arfken G.B., Weber H.J., Harris F.E.]
year: 2013
venue: "Academic Press (7th ed.)"
local_file: "/home/stefano/papers/mosaic/fourier-analysis-of-schemes/2013-AcademicPress-Arfken-101016C20090306297.pdf"
tags: [textbook, fourier-series, fourier-transform, discrete-fourier-transform, laplace-transform]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

A general textbook of mathematical methods for physicists in 23 chapters. Its
identity was verified from the title and copyright pages: seventh edition,
© 2013 Elsevier Inc., Academic Press. The DOI (doi:10.1016/C2009-0-30629-7)
and ISBN 978-0-12-384654-9 were verified on Crossref. The PDF is an ebook
conversion with a good text layer, and its page numbers differ from the
printed ones by a drifting offset (+3 in ch. 20). Every locator on these pages
is a printed page. Equations whose text layer was ambiguous were checked on
rendered page images: the DFT pair (p. 1004) and the aliasing example
(p. 1006).

**Scoped read.** For this bundle the compiler read the preface and contents,
**ch. 19** (Fourier series, pp. 935–962) and **ch. 20** (Integral transforms,
pp. 963–1046), in full, with all exercises and both chapter reading lists.
Nothing else was read. The text defers to chapters outside the scope: ch. 5
(Bessel's inequality), ch. 11 (contour integration and residues), ch. 12
(dispersion relations), ch. 14 (Bessel functions) and ch. 16 (the
spherical-wave expansion). Their content is not compiled here.

What the chapters read **do not** contain is as important for this bundle. As
in the founding source, there is no von Neumann stability analysis, no
amplification factor of a mode, no modified wavenumber, no dispersion or
dissipation analysis of a difference scheme, and no difference scheme at all.
The book has no numerical-methods chapter. Its numerical content in scope is
the discrete Fourier transform (§20.6), the operation count of the FFT, and the
warning that Fourier series near a discontinuity are "highly unreliable for
precise numerical work". The Laplace transform is used for initial-value
problems and never for stability.

**Conventions differ from the founding source and the registry.** The Fourier
transform has the same symmetric $1/\sqrt{2\pi}$ but the opposite sign
($e^{+\mathrm i\omega t}$ forward). The DFT uses $N^{-1/2}$ and the same $+$
sign. The Fourier convolution carries a factor $1/\sqrt{2\pi}$. The Laplace
transform is written $f(s) = \mathcal L\{F(t)\}$, with lowercase for the
transform. Every difference is mapped below. None is a difference of claim.

Merged into 15 concept pages (2 created, 13 updated) and the notation
registry, listed in the audit below. No contradiction with the founding source was found.
Qualifications are recorded on the pages concerned.

# Key claims

1. **Fourier series** for period $2\pi$ and $2L$ (eqs. 19.1–19.6, 19.10–19.12):
   coefficient formulas identical to Riley et al.'s after rescaling; series
   coefficient with $e^{-\mathrm int}$ (p. 958).
2. **Dirichlet conditions** (§19.1, pp. 935–936): finitely many finite
   discontinuities and finitely many extrema on the period; "sufficient but not
   necessary" (footnote 1); "piecewise regular".
3. **Sturm–Liouville basis** (pp. 936–937): $-y'' = \lambda y$ with periodic
   conditions is Hermitian, so the modes are complete and orthogonal, and
   expansions of $L^2$ functions "converge in the mean".
4. **Convergence at a jump** to the mean (eq. 19.7), proof referred to
   Jeffreys and Jeffreys or Carslaw; uniform convergence if $f$ is continuous
   with a finite jump in $f'$ (citing Churchill, p. 937).
5. **Term-by-term integration** always permissible for integrable $f$, with
   uniformly convergent result (eqs. 19.15–19.17, p. 942). **Differentiation**
   "permissible if the series to be differentiated is uniformly convergent"
   (p. 944), with the sawtooth (divergent, eq. 19.20) and the triangular wave
   (eqs. 19.21–19.23) as examples.
6. **Coefficient decay** (p. 951, citing Raisbeek 1955): $O(1/m)$ for
   discontinuous $f$ (conditional convergence), $1/m^2$ for continuous $f$ with
   discontinuous derivatives (absolute convergence).
7. **Travelling waves** (pp. 939–940): equal phase velocity of all harmonics
   corresponds to a medium responding equally at all frequencies, "by no means
   always true" in physical media; superposition needs linearity. Power
   spectrum $a_m^2 + b_m^2$, phase-invariant (exercise 19.1.2).
8. **Gibbs phenomenon** (§19.3, eqs. 19.29–19.43): partial sums as an integral
   with a kernel that tends to $\delta$; on the square wave the peak lies near
   $x \approx \pi/M$ and has height $1.1789797\ldots$ times the half-jump, "some
   18%" overshoot (exercise 19.3.3: $1.178979744472$). It persists as terms
   are added, makes Fourier series "highly unreliable for precise numerical work"
   near a discontinuity, and occurs in other eigenfunction expansions (citing
   Thompson 1992).
9. **Fourier transform** with symmetric $1/\sqrt{2\pi}$ and kernel
   $e^{+\mathrm i\omega t}$ (eqs. 20.6, 20.10, 20.23–20.30); explicit warning
   that conventions differ by powers of $2\pi$ (p. 965); §20.5 uses the
   non-symmetric pair with $e^{-\mathrm i\omega t}$ (eqs. 20.100–20.101).
10. **Fourier integral** from a delta sequence, explicitly non-rigorous
    (eqs. 20.20–20.22, p. 970).
11. **Transforms**: $e^{-\alpha\lvert t\rvert}$, $\delta$, the Lorentzian, the Gaussian
    (by a contour shift), the finite wave train with half-width $\omega_0/N$
    (Examples 20.2.1–20.2.4), Yukawa, Coulomb and other 3-D transforms
    (Example 20.2.5).
12. **Properties** (eqs. 20.48–20.56): translation, scale, sign change,
    conjugation, gradient, Laplacian, derivatives; $t^nf$ (exercise 20.3.5).
13. **PDEs in transform space** (Examples 20.3.1–20.3.3): wave equation
    (d'Alembert form), heat equation (Gaussian kernel), Poisson Green's
    function; the method's limits (pp. 984–985).
14. **Convolution theorem** with normalized convolution (eqs. 20.68–20.71),
    transform of a product (eq. 20.93), multiple convolutions
    (eqs. 20.83–20.88).
15. **Parseval relation** ("Rayleigh's theorem"), $L^2$ existence, unitarity of
    the transform operator (eqs. 20.73–20.78, pp. 987–988).
16. **Transfer functions and causality** (§20.5, eqs. 20.102–20.113).
17. **Discrete Fourier transform** (§20.6): orthogonality over equally spaced
    points (eqs. 20.115–20.120); the unitary pair (eqs. 20.121–20.122); shift
    and cyclic-convolution theorems (eqs. 20.123–20.125); unitarity of the
    matrices (p. 1005); aliasing, defined on $\cos 3x$ against $\cos x$ at
    $N = 4$ (Example 20.6.1); Hermitian symmetry of real data as aliasing
    (exercise 20.6.3); FFT cost $N^2 \to (N/2)\log_2N$ (pp. 1006–1007).
18. **Laplace transform** (eqs. 20.126–20.141): existence for functions of
    exponential order; Lerch's theorem; table 20.1;
    $\lim_{s\to\infty}\mathcal L\{f\} = 0$ (p. 1010); $\mathcal L\{\delta\} = 1$ by
    one-sided delta sequences.
19. **Laplace properties** (eqs. 20.147–20.184, table 20.2), Heaviside
    shifting theorem (p. 1023), initial-value limit (exercise 20.7.1), periodic
    functions (exercise 20.8.20), constant-coefficient ODEs to algebra
    (§20.8).
20. **Laplace convolution** (eqs. 20.185–20.189) and impulse response of the
    driven oscillator (eqs. 20.193–20.194).
21. **Bromwich integral** (eqs. 20.198–20.204), a plausibility derivation
    "that can be made rigorous" (p. 1042).
22. **Read but not compiled.** Summation of Fourier series by power series
    (Example 19.1.3) and Clausen functions (exercises 19.1.14–19.1.16).
    Electrostatics and string-vibration exercises (19.2.11–19.2.21). Hankel
    and Mellin transforms (eqs. 20.8–20.9). Momentum-space quantum mechanics
    (§20.4). Circuit and nuclear-decay exercises. Bessel-equation and special-
    function Laplace transforms (Example 20.8.7, exercises 20.8.10–20.8.24).
    These are applications without a Fourier-analysis claim in this bundle's
    scope.

# Notation map

| Arfken et al. | Registry | Note |
|---|---|---|
| $n$ (series index) | $m$ | |
| $a_n$, $b_n$, $c_n$ | $a_m$, $b_m$, $\hat f_m$ | same normalization and sign as the registry |
| $L$ in eqs. 19.10–19.12 | $L/2$ | Arfken's period is $2L$; the registry's $L$ is the period |
| $f_r(x)$, $r$ (§19.3) | $S_Mf$, $M$ | partial sum through $\lvert m\rvert \le M$ |
| $p = r + \frac12$, $\xi = ps$ (§19.3) | $M + \frac12$, $u$ | $\xi$ and $p$ have other registry meanings |
| $h$ (square-wave height) | $A$ | $h$ is the grid spacing |
| $v$ (phase velocity) | $c_0$ | |
| $g(\omega) = \frac{1}{\sqrt{2\pi}}\int f e^{\mathrm i\omega t}\mathrm dt$ | $\hat f(-\omega)$ | same constant, opposite sign; inverse carries $e^{-\mathrm i\omega t}$ |
| $g(\mathbf k)$, $[\cdot]^T$ (3-D) | $\hat f(-\mathbf k)$, $\mathcal F$ | |
| $g_c$, $g_s$ | $\hat f_c$, $\hat f_s$ | identical formulas (sign-independent) |
| $F(t)$, $G(t)$ (§20.4, transform variable $t$) | $\hat f(-k)$, $\hat g(-k)$ | |
| $(f*g)(x) = \frac{1}{\sqrt{2\pi}}\int g(y)f(x-y)\,\mathrm dy$ | $(2\pi)^{-1/2}(f*g)(x)$ | normalized convolution; theorem without constant |
| $F(\omega) = \int f e^{-\mathrm i\omega t}\,\mathrm dt$ (§20.5) | $\sqrt{2\pi}\,\hat f(\omega)$ | non-symmetric pair, registry sign |
| $\varphi(\omega)$, $\Phi(t)$ (transfer function, response) | (prose only) | not registered |
| $\alpha$ in $e^{-\alpha\lvert t\rvert}$, $e^{-\alpha r}/r$ | $\gamma$ | $\alpha$ is the exponential-multiplication constant |
| $\omega_0$, $N$ (finite wave train) | $\omega_c$, $p$ | $N$ is the number of samples |
| $\Delta\omega$ (half-width, eq. 20.35) | (prose only) | $\Delta$ is reserved for steps |
| $y(x,t)$, $\psi(x,t)$ (PDE unknowns) | $\varphi(x,t)$ | |
| $a^2$ (heat equation) | $\nu$ | diffusivity |
| $\alpha$, $y$ (spatial transform variables, §20.3) | $k$ | |
| $G(\mathbf r, \mathbf r')$ | $\mathcal G(\mathbf r, \mathbf r_0)$ | $G$ is the amplification factor |
| $K$, $Q$, $D$ (exercise 20.3.6) | $\kappa_0$; $Q/D \to -1$ | point-source case of $\varphi'' - \kappa_0^2\varphi = \delta$ |
| $x_k = 2\pi k/N$, $k$, $f_k$ (§20.6) | $x_j$, $j$, $f_j$ | $L = 2\pi$, $h = 2\pi/N$ |
| $p$, $q$ (DFT indices) | $m$, $p$ | |
| $g_p = N^{-1/2}\sum_k e^{2\pi\mathrm ikp/N}f_k$ | $\sqrt N\,\hat f^N_{-p} = \sqrt N\,\hat f^N_{N-p}$ | registry: $1/N$ and $e^{-2\pi\mathrm ijm/N}$ |
| $[f*g]_k = N^{-1/2}\sum_j f_jg_{k-j}$ | $N^{-1/2}c_j$, $c_j = \sum_p f_pg_{j-p}$ | cyclic |
| $x$ in $\frac12(e^{\mathrm i\pi x/2} + e^{3\mathrm i\pi x/2})$ (Example 20.6.1) | $j$ | the printed exponent uses the point index |
| $f(s) = \mathcal L\{F(t)\}$ | $\mathcal L\{f\}(s)$ | Arfken: lowercase transform, capital function |
| $F(+0)$ | $f(+0)$ | one-sided limit |
| $u(t - k)$ | $H(t - t_0)$ | value at the jump unspecified in Arfken |
| $k$ (constants in tables 20.1–20.2) | $a$, $b$ | $k$ is the wavenumber |
| $\Gamma(n+1)$ | $\Gamma(p+1)$ | |
| $\beta$, $s = \beta + \mathrm iu$ | $\beta$ | Bromwich abscissa |
| $N(t)$ (null function) | (prose only) | |
| $F_1 * F_2$ (Laplace) | $f * g$, one-sided | |
| $\mathrm{si}(x)$ | (prose only) | sine integral |

# Audit

Created in this run (2026-10-14):

* Created [Discrete Fourier transform](/definitions/discrete-fourier-transform.md)
* Created [Sawtooth wave](/benchmarks/sawtooth-wave.md)

Updated in this run (2026-10-14):

* Updated [Notation registry](/notation.md): discrete symbols $\xi$ and $\hat f^N_m$ now in use; added $\varphi(x,t)$, $c_0$, $\nu$, $\mathcal G$, $\mathbf r_0$, $\Gamma$, $\beta$
* Updated [Fourier series](/definitions/fourier-series.md)
* Updated [Dirichlet conditions](/definitions/dirichlet-conditions.md)
* Updated [Fourier transform](/definitions/fourier-transform.md)
* Updated [Dirac delta function](/definitions/dirac-delta-function.md)
* Updated [Convolution](/definitions/convolution.md)
* Updated [Laplace transform](/definitions/laplace-transform.md)
* Updated [Convergence of Fourier series](/results/fourier-series-convergence.md)
* Updated [Gibbs phenomenon](/results/gibbs-phenomenon.md)
* Updated [Parseval's theorem](/results/parseval-theorem.md)
* Updated [Convolution theorem](/results/convolution-theorem.md)
* Updated [Fourier transform properties](/results/fourier-transform-properties.md)
* Updated [Laplace transform properties](/results/laplace-transform-properties.md)
* Updated [Square wave](/benchmarks/square-wave.md)
* Updated [Riley, Hobson & Bence (2006)](/sources/riley-2006.md): audit lines only

Not touched: cross-correlation, Wiener–Khinchin (Arfken et al. do not treat
correlation in the chapters read), the difference operators, the two time
integrators and the exponential-decay benchmark (no counterpart in the
chapters read).

# Citations

The chapter-end "Additional Readings" of chs. 19 and 20 are the reference
list. They were merged complete into the [bibliography](/bibliography.md):
7 works for ch. 19 and 18 for ch. 20, with Jeffreys and Jeffreys (1972) in
both. The works cited in footnotes and in the text of the chapters read were
merged as well: Robinson (1953), Van Name (1954), Raisbeek (1955), Thompson
(1992), Cooley and Tukey (1965), Bergland (1969), Press et al. (1996), Menzel
(1955), Olson (1943) and Bohn and Flynn (1978). That makes 34 cited works.
