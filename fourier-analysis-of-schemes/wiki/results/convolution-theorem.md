---
type: Result
title: "Convolution theorem"
description: "The Fourier transform of a convolution is sqrt(2 pi) times the product of the transforms, and the transform of a product is 1/sqrt(2 pi) times the convolution of the transforms (constants of the unitary normalization); the Laplace transform of the one-sided convolution is the plain product of the Laplace transforms."
status: established
aliases: [Fourier convolution theorem, Laplace convolution theorem, Borel's theorem]
tags: [fourier-transform, laplace-transform, convolution]
timestamp: 2026-10-14T00:00:00Z
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

[Arfken et al. (2013)](/sources/arfken-2013.md) prove the first form the same
way: they split the exponential and substitute $z = x - y$ (eq. 20.70,
pp. 986–987). Their convolution carries a factor $1/\sqrt{2\pi}$
(see [convolution](/definitions/convolution.md)), so they print the theorem
without a constant, and its inversion expresses the unnormalized convolution
integral as the inverse-transform integral of the product of the transforms
(eq. 20.71). After mapping the constant (and the sign, to which the theorem is
insensitive), both statements are the registry's
$\mathcal F[f*g] = \sqrt{2\pi}\,\hat f\hat g$. They also write out the
product form that Riley et al. leave as "may be proved similarly",
(eq. 20.93), which in registry form is $\mathcal F[fg] = (2\pi)^{-1/2}\hat f*\hat g$.
That form "will be useful only if $f$ and $g$ individually have Fourier
transforms". When $f$ has none but has a Maclaurin series,
$\mathcal F[fg] = f(\mathrm i\,\mathrm d/\mathrm dk)\,\hat g$ instead
(eq. 20.94, mapped). For a
triple convolution $\mathcal F[f*g*h] = 2\pi\,\hat f\hat g\hat h$ in any order
(eqs. 20.83–20.85, mapped). In the source's words the theorem trades
"geometric complexity for oscillational complexity": the factors of the
transformed integrand share one argument (p. 987).

## Laplace form

For the one-sided convolution $\int_0^t f(u)\,g(t-u)\,\mathrm du$
(eq. 13.64):
$$\mathcal L\!\left[\int_0^t f(u)\,g(t - u)\,\mathrm du\right] = \mathcal L\{f\}(s)\,\mathcal L\{g\}(s),$$
so $\mathcal L^{-1}\bigl[\mathcal L\{f\}\,\mathcal L\{g\}\bigr] = f * g$. It is
proved by substituting $u + v = t$ and swapping the order of integration over
the wedge $0 \le u \le t$ (fig. 13.7, p. 458). No constant appears.
Arfken et al. prove it by the change of variables $t = x + y$ with unit
Jacobian (eqs. 20.185–20.189, p. 1035). They use it to write the response of a
driven, damped oscillator as the convolution of the force with the response to
an impulse (eq. 20.193): "the transform of the response (output) appears as
the product of two factors, one describing the driving force (input) and the
other describing the dynamical system" (p. 1037).

## Discrete form

For $N$ samples, the cyclic convolution $c_j = \sum_{p=0}^{N-1}f_pg_{j-p}$ has
$\hat c^{N}_m = N\,\hat f^{N}_m\hat g^{N}_m$ in registry normalization
(Arfken et al., eqs. 20.124–20.125; see
[discrete Fourier transform](/definitions/discrete-fourier-transform.md)).

## Uses in the source

* Deconvolution: divide transforms (see [convolution](/definitions/convolution.md)).
* Two wide slits as the convolution of two deltas with a box gives the same
  transform as direct integration (p. 448).
* Arfken et al.: the potential of a charge density, two-centre overlap
  integrals and the interaction energy of two charge distributions, the last
  reducing a six-fold integral to a three-fold one (Examples 20.4.1–20.4.3).
  The Parseval relation is the theorem at zero argument
  ([Parseval's theorem](/results/parseval-theorem.md)).
* Exercise 13.12 writes a sampled signal passed through a triangular filter as
  a convolution and evaluates it with the theorem and the $\mathrm{sinc}^2$
  transform of a triangle (exercise 13.4). Exercise 13.27 checks the Laplace form on
  a box.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §13.1.7 (pp. 447–449), §13.2.2 (pp. 457–458); exercises 13.4, 13.12, 13.27.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §20.4 (eqs. 20.68–20.94, pp. 985–992), §20.6 (eqs. 20.124–20.125, p. 1005), §20.9 (eqs. 20.185–20.193, pp. 1034–1037).
