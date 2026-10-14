---
type: Definition
title: "Fourier transform"
description: "Integral representation of a non-periodic, absolutely integrable function as a superposition of modes exp(i k x), obtained as the infinite-period limit of the complex Fourier series; defined here with the symmetric 1/sqrt(2 pi) normalization, with sine and cosine transforms for odd and even functions, the multidimensional pair, and (in exercises) sampled and periodized forms."
status: established
aliases: [Fourier integral, Fourier transform pair, Fourier inversion theorem, Fourier sine transform, Fourier cosine transform]
tags: [fourier-transform]
timestamp: 2026-10-14T00:00:00Z
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

**Qualification: Arfken et al.'s sign.**
[Arfken et al. (2013)](/sources/arfken-2013.md) use the same symmetric constant
with the **opposite sign** of the exponent (eqs. 20.6, 20.10, 20.23–20.26).
Their forward transform is
$$\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} f(t)\,e^{+\mathrm i\omega t}\,\mathrm dt = \hat f(-\omega),$$
and their inverse carries $e^{-\mathrm i\omega t}$. They keep the $1/\sqrt{2\pi}$ "because
it causes the transform and its inverse to have formulas that are more
symmetrical". They warn that "the notation for this transform is not entirely
universal": some writers omit the prefactor, and periodic systems use the
kernel $\exp(2\pi\mathrm i\omega t/a_0)$ with $a_0$ a lattice constant. "These
differences in notation do not change the mathematics, but cause formulas to
differ by powers of $2\pi$ or $a_0$. Caution is therefore advised when
combining material from different sources" (p. 965). In §20.5 they use the
pair "most physicists" use for signals, $\int f e^{-\mathrm i\omega t}\,\mathrm dt$
forward and $\frac{1}{2\pi}\int\cdot\,e^{\mathrm i\omega t}\,\mathrm d\omega$ back
(eqs. 20.100–20.101), which yields $\sqrt{2\pi}\,\hat f(\omega)$ in registry terms.
The two books therefore differ in convention only, and every Arfken et al.
formula on these pages is mapped. Their remark that the inverse differs from
the forward transform only by the sign of the exponent, so that "two
successive applications of the Fourier transform" are not the transform
followed by its inverse (p. 970), holds under either sign.

**Existence (qualification).** Riley et al. place one requirement on $f$, a
finite $\int\lvert f\rvert$. Arfken et al. restrict the chapter "to functions
for which the indicated operations can be carried out" (p. 964). In §20.10 they
recall that a Fourier-transformable function "had to satisfy the Dirichlet
conditions", with a transform that vanishes as $\omega\to\infty$ (eq. 20.199),
the delta function excepted, whose transform is bounded. For the
[Parseval relation](/results/parseval-theorem.md) they take $f$ square
integrable (p. 988). These are different sufficient settings, not
incompatible claims.

## Fourier's inversion theorem

Writing the complex [Fourier series](/definitions/fourier-series.md) of a
function of period $T$ with $\omega_m = 2\pi m/T$, the spacing
$\Delta\omega = 2\pi/T$ tends to zero as $T\to\infty$ and the sum becomes an
integral (eqs. 13.1–13.3, fig. 13.1), giving **Fourier's inversion theorem**
(eq. 13.4):
$$f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\mathrm d\omega\,e^{\mathrm i\omega t}\int_{-\infty}^{\infty}\mathrm du\,f(u)\,e^{-\mathrm i\omega u}.$$
The derivation is a limiting argument, not a proof: the existence of
$\hat f(\omega)$ as $T\to\infty$ "is assumed here without proof" (p. 435).

Arfken et al. reach the same **Fourier integral** (eq. 20.22) by a different
route. They write $f$ against the delta sequence
$\frac{1}{2\pi}\int_{-n}^{n}e^{\mathrm i\omega t}\,\mathrm d\omega$ (eq. 20.20),
exchange the integrations and let $n\to\infty$ (eq. 20.21). They state that the
derivation "did not provide a rigorous justification for the reversal of the
order of integration and the passage to the infinite-$n$ limit" and refer to
Sneddon (p. 970). Both sources therefore give a limiting argument and neither
gives a proof.

## Symmetry and reality

(Arfken et al.) Even functions have real transforms and odd functions
imaginary ones; a function that is neither has a complex transform (footnote,
p. 970). This is consistent with Riley et al.'s $\hat f = -\mathrm i\hat f_s$ for
odd $f$. $f$ is real if and only if $\hat f(-k) = \hat f(k)^*$, and pure
imaginary if and only if $\hat f(-k) = -\hat f(k)^*$ (exercise 20.2.1, a
statement independent of the sign convention).

## Sine and cosine transforms

For odd $f$ the transform is odd in $\omega$ and reduces to the **Fourier sine
transform** pair (eqs. 13.35–13.36)
$$\hat f_s(\omega) = \sqrt{\frac2\pi}\int_0^\infty f(t)\sin\omega t\,\mathrm dt,\qquad f(t) = \sqrt{\frac2\pi}\int_0^\infty \hat f_s(\omega)\sin\omega t\,\mathrm d\omega,$$
with $\hat f(\omega) = -\mathrm i\,\hat f_s(\omega)$ for odd $f$. The pair needs
$f$ only for $t > 0$. The cosine pair $\hat f_c$ is the same with $\cos$, for
even $f$ (§13.1.6, pp. 445–446). Arfken et al. print the identical sine and
cosine pairs (eqs. 20.27–20.30, unaffected by the sign convention). Because
they use data for $t \ge 0$ only, the inverses describe an odd (sine) or even
(cosine) continuation for $t < 0$ (p. 971). On a half-line the sine transform
imposes a Dirichlet condition at $x = 0$ and the cosine transform a Neumann
condition (p. 985).

## Higher dimensions

In three dimensions (eqs. 13.49–13.50)
$$\hat f(\mathbf k) = \frac{1}{(2\pi)^{3/2}}\int f(\mathbf r)\,e^{-\mathrm i\mathbf k\cdot\mathbf r}\,\mathrm d^3 r,\qquad
f(\mathbf r) = \frac{1}{(2\pi)^{3/2}}\int \hat f(\mathbf k)\,e^{\mathrm i\mathbf k\cdot\mathbf r}\,\mathrm d^3 k,$$
"and similar relations ... exist for spaces of other dimensionalities". For a
spherically symmetric $f(r)$,
$\hat f(k) = (2\pi)^{-3/2}\int_0^\infty 4\pi r^2 f(r)\,\frac{\sin kr}{kr}\,\mathrm dr$
(worked example, p. 452); the axisymmetric two-dimensional analogue is a
Hankel-type integral with $J_0$ (eq. 13.52). Arfken et al. print the same
three-dimensional pair with their sign (eqs. 20.36–20.37). They ask for the
radial form as a sine transform (exercise 20.2.16) and the two-dimensional
radial form as a zero-order Hankel transform (exercise 20.2.15), both in
agreement with Riley et al. They add the transforms of
$e^{-\gamma r}/r$, $1/r$ and $1/r^2$: $(2\pi)^{-3/2}\,4\pi/(k^2+\gamma^2)$,
$(2\pi)^{-3/2}\,4\pi/k^2$ and $(\pi/2)^{1/2}/k$ (eqs. 20.41–20.43).

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

Arfken et al. obtain the Gaussian pair
$\mathcal F[e^{-at^2}] = (2a)^{-1/2}e^{-\omega^2/4a}$, $a > 0$ (eq. 20.19, which
the sign does not affect). Their derivation also completes the square, but it
justifies the shift of the integration path by a contour argument: the
displaced and real-axis paths enclose no singularity (fig. 20.3, pp. 968–969).
They state the same inverse relation of widths. For $e^{-\gamma\lvert t\rvert}$,
with transform $(2/\pi)^{1/2}\gamma/(\gamma^2+\omega^2)$, "the more localized
is $f(t)$, the less localized will be" its transform (eq. 20.13, p. 967). For a
wave train of $p$ cycles of $\sin\omega_ct$ the central maximum of the spectrum
has half-width $\omega_c/p$ (eq. 20.35). "The inverse relationship between
frequency spread and pulse length is a fundamental property of finite wave
distributions", and its quantum form is the uncertainty principle
(Example 20.2.4, pp. 971–973).

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

The discrete transform is developed by Arfken et al. (§20.6) and has its own
page, [discrete Fourier transform](/definitions/discrete-fourier-transform.md).
That page maps $F_m$ of exercise 13.10 onto the registry normalization and
records the compiler's reading of the unexplained disagreement for
$m \ge N/2$ as aliasing (hypothesis).

# Examples

* One-sided exponential decay, $f = Ae^{-\gamma t}$ for $t\ge0$ and $0$ for
  $t<0$ ($\gamma > 0$): $\hat f(\omega) = \frac{A}{\sqrt{2\pi}(\gamma + \mathrm i\omega)}$ (p. 435).
* Two-sided decay $e^{-\gamma\lvert t\rvert}$: the real transform
  $(2/\pi)^{1/2}\gamma/(\gamma^2+\omega^2)$. Transforming that Lorentzian again
  returns $e^{-\gamma\lvert\omega\rvert}$ by contour integration, and the inverse
  formula gives an integral representation of $e^{-\gamma\lvert t\rvert}$ free of
  absolute values (Arfken et al., Examples 20.2.1, 20.2.3, eqs. 20.13–20.17,
  20.24).
* Fraunhofer diffraction: the far-field intensity in a direction is
  proportional to $\lvert\hat f\rvert^2$ of the aperture function evaluated at
  the transverse wavenumber of that direction (eqs. 13.8–13.10).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§13.1–13.1.2, 13.1.6, 13.1.10 (pp. 433–453); exercises 13.9–13.11 (pp. 461–462).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §§20.1–20.2 (eqs. 20.6–20.47, pp. 963–975), §20.3 (p. 985), §20.4 (p. 988), §20.5 (eqs. 20.100–20.101, pp. 997–998), §20.10 (eq. 20.199, p. 1038); exercises 20.2.1, 20.2.15, 20.2.16.
