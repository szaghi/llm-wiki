---
type: Definition
title: "Discrete Fourier transform"
description: "The transform between N equally spaced samples of one period and N discrete Fourier coefficients, built on the orthogonality of exp(2 pi i j m / N) over the points; it has shift and cyclic-convolution theorems like the continuous transform, a unitary matrix (in the symmetric normalization), Hermitian-symmetric coefficients for real samples, aliasing of modes m and m + N, and the fast Fourier transform as an O(N log N) evaluation."
status: established
aliases: [DFT, discrete Fourier coefficients, finite Fourier transform, discrete orthogonality, aliasing, fast Fourier transform, FFT]
tags: [discrete-fourier-transform, fourier-transform, aliasing]
timestamp: 2026-10-14T00:00:00Z
---

# Discrete Fourier transform

## Definition

Take $N$ equally spaced points on one period $L$, $x_j = x_0 + jh$ with
$h = L/N$, $j = 0, \dots, N-1$, and samples $f_j = f(x_j)$. In the registry
normalization the **discrete Fourier transform** and its inverse are
$$\hat f^{N}_m = \frac1N\sum_{j=0}^{N-1} f_j\,e^{-2\pi\mathrm i jm/N},\qquad
f_j = \sum_{m=0}^{N-1}\hat f^{N}_m\,e^{2\pi\mathrm i jm/N},\qquad m = 0,\dots,N-1$$
([Arfken et al. (2013)](/sources/arfken-2013.md), eqs. 20.121–20.122, with
$L = 2\pi$, $x_0 = 0$, and translated as below). The source introduces it for
"numerically determined Fourier transforms, which consist of values given at a
discrete set of points", where "integrations are therefore converted into
finite summations" (§20.6, p. 1002). Once $f(x_j)$ is written $f_j$, "that
substitution has pretty much decoupled the problem from the original interval
of definition": the transform maps one set of $N$ values onto another
(p. 1004). The inverse is verified by substituting one formula into the other
and using the discrete orthogonality below (p. 1004).

**Normalization and sign (a qualification, not a contradiction).** The two
sources that touch the discrete transform use three different constants and
signs. Arfken et al. use the symmetric $N^{-1/2}$ split and the $+$ sign of
their continuous transform ([Fourier transform](/definitions/fourier-transform.md)):
their coefficient of index $m$ is
$N^{-1/2}\sum_j e^{+2\pi\mathrm i jm/N} f_j = \sqrt N\,\hat f^{N}_{-m} = \sqrt N\,\hat f^{N}_{N-m}$,
and their inverse carries $N^{-1/2}$ and $e^{-2\pi\mathrm i jm/N}$.
[Riley et al. (2006)](/sources/riley-2006.md), exercise 13.10, use
$\frac{1}{\sqrt{2\pi}}\sum_j f_j e^{-2\pi\mathrm i jm/N} = \frac{N}{\sqrt{2\pi}}\hat f^{N}_m$,
scaled so that $h$ times it approximates the continuous transform. The
Source pages' Notation maps hold the symbol-level mapping. The registry's
$1/N$ makes $\hat f^{N}_m$ approximate the series coefficient $\hat f_m$. As a
compiler remark (not in either source): with $x_0 = 0$ it is exactly the
rectangle-rule value of
$\hat f_m = \frac1L\int_0^L f\,e^{-\mathrm ik_mx}\,\mathrm dx$ on the $N$
points. The mode $m$ has wavenumber $k_m = 2\pi m/L$ and scaled wavenumber
$\xi = k_m h = 2\pi m/N$.

## Discrete orthogonality

The modes $e^{2\pi\mathrm i jm/N}$ are orthogonal over the points, not only
over the period (§20.6, eqs. 20.117–20.120). The sum over the points is a
finite geometric series:
$$\sum_{j=0}^{N-1} e^{-2\pi\mathrm i jp/N}\,e^{2\pi\mathrm i jm/N} = \begin{cases} N, & m - p \text{ a multiple of } N,\\ 0, & \text{otherwise}.\end{cases}$$
Because $e^{2\pi\mathrm i j(m+N)/N} = e^{2\pi\mathrm i jm/N}$ at every point,
"only $N$ of them are linearly independent", and $m, p$ may be restricted to
$0,\dots,N-1$, where the sum is $N\delta_{mp}$ (p. 1003). Exercise 20.6.1
asks for the real forms: over $j$, $\cos(2\pi mj/N)\sin(2\pi pj/N)$ sums to
$0$; $\cos\cos$ sums to $N/2$ for $m = p \ne 0, N/2$, to $N$ for
$m = p \in\{0, N/2\}$, and to $0$ otherwise; $\sin\sin$ sums to $N/2$ for
$m = p \ne 0, N/2$ and to $0$ otherwise. A compiler remark: the "otherwise
$0$" holds for $0 \le m, p \le N/2$. Since $\cos(2\pi(N-p)j/N) = \cos(2\pi pj/N)$,
the pair $m$, $N - m$ is not orthogonal on the points.

## Properties

The source states that discrete transforms "have properties similar to those
of their continuous cousins" (p. 1004). In registry form:

* **Shift.** The cyclically shifted samples $f_{j-p}$ have coefficients
  $e^{-2\pi\mathrm i pm/N}\hat f^{N}_m$ (eq. 20.123, which uses the periodicity
  of $f_j$). This is the discrete form of the translation rule on
  [Fourier transform properties](/results/fourier-transform-properties.md).
* **Cyclic convolution.** If $c_j = \sum_{p=0}^{N-1} f_p\,g_{j-p}$, indices
  taken modulo $N$, then $\hat c^{N}_m = N\,\hat f^{N}_m\,\hat g^{N}_m$. The
  source defines its discrete convolution with a factor $N^{-1/2}$, so in its
  normalization the transform of the convolution is the plain product of the
  transforms (eqs. 20.124–20.125), "completely analogous with the
  convolution theorem for the continuous transform". The constant $N$ here
  belongs to the registry normalization (see the
  [convolution theorem](/results/convolution-theorem.md)).
* **Unitarity.** The transform and its inverse are $N\times N$ matrices with
  entries proportional to complex exponentials, and in the source's symmetric
  normalization they are unitary (p. 1005). In the registry normalization this
  reads $\frac1N\sum_j\lvert f_j\rvert^2 = \sum_m\lvert\hat f^{N}_m\rvert^2$. That
  rewriting is the compiler's, not printed in the source. It is the discrete
  counterpart of [Parseval's theorem](/results/parseval-theorem.md) for series.
* **Real and imaginary samples** (exercise 20.6.3). If every $f_j$ is real,
  $\hat f^{N}_{N-m} = (\hat f^{N}_m)^*$. If every $f_j$ is pure imaginary,
  $\hat f^{N}_{N-m} = -(\hat f^{N}_m)^*$. The source writes these in its own
  normalization, and the sign map leaves them unchanged.

## Aliasing

"Situations in which the behavior at one wavelength or frequency is mistaken
for that at another is called **aliasing**" (Example 20.6.1, p. 1006). The
example samples $\cos 3x$ at $N = 4$ points $x = 0, \pi/2, \pi, 3\pi/2$. The
values $(1, 0, -1, 0)$ are those of $\cos x$ as well, "so neither our discrete
transform nor any information derived therefrom can properly reflect any
difference in behavior" between the two. The coefficients are
$\hat f^{4}_1 = \hat f^{4}_3 = \tfrac12$ and $0$ otherwise (the source's
$(0,1,0,1)$). The resulting expression is correct at the points, but over the
whole period "it cannot distinguish between $\cos x$, $\cos 3x$, or any linear
combination of the two with unit overall weight". The remedy is to "use point
sets of sufficient size to accommodate the expected extent of oscillatory
character". The note to exercise 20.6.3 calls the Hermitian symmetry of real
data "an illustration of aliasing": an amplitude at the frequency of $m$
implies an equal amplitude at that of $N - m$.

In terms of $\xi$ (a compiler restatement of p. 1003): grid modes whose
scaled wavenumbers differ by a multiple of $2\pi$ are the same grid function,
since $e^{\mathrm ij(\xi + 2\pi)} = e^{\mathrm ij\xi}$.

**Compiler's notes (hypothesis).**

* The source prints the interpolating expression as
  $\tfrac12(e^{\mathrm i\pi x/2} + e^{3\mathrm i\pi x/2})$, with $x$ read as the
  point index. Its own inverse (20.122) at $x_j = \pi j/2$ gives
  $\tfrac12(e^{-\mathrm ix} + e^{-3\mathrm ix})$. The two agree at the points
  because the samples are real. Off the points both are complex, not $\cos x$:
  the index range $0,\dots,N-1$ places the second mode at $m = 3$ rather than
  at $m = -1$.
* Riley et al.'s exercise 13.10 notes poor agreement between the sampled
  transform and $\hat f$ for $m \ge N/2$ and gives no reason (see
  [Fourier transform](/definitions/fourier-transform.md)). The compiler reads
  it as this aliasing. By the real-data symmetry, the coefficients for
  $m > N/2$ repeat those of $N - m$, which belong to the negative wavenumber
  $-2\pi(N-m)/(Nh)$, not to $2\pi m/(Nh)$. Arfken et al. do not discuss that
  exercise.

## Fast Fourier transform

The **fast Fourier transform** is "a particular way of factoring and
rearranging the terms in the sums of the discrete Fourier transform" that
exploits the many duplicate entries of the transform matrix (p. 1006). The
source credits it to Cooley and Tukey (1965). A direct evaluation needs about
$N^2$ multiplications. For $N$ a power of 2 the Cooley–Tukey technique needs
$(N/2)\log_2 N$, a factor of over 200 fewer at $N = 1024$ (pp. 1006–1007). The
source gives no algorithm. It refers to Cooley and Tukey, Bergland (1969),
*Numerical Recipes* and Hamming, and Hamming also for "errors and limitations
in the use of the discrete Fourier transform" (p. 1005).

# Citations

* [Arfken et al. (2013)](/sources/arfken-2013.md), §20.6 (eqs. 20.115–20.125, Example 20.6.1, pp. 1002–1007); exercises 20.6.1–20.6.3 (p. 1007).
* [Riley et al. (2006)](/sources/riley-2006.md), exercise 13.10 (pp. 461–462): the sampled transform and its normalization.
