---
type: Result
title: "Gibbs phenomenon"
description: "At a jump discontinuity the partial sums of a Fourier series overshoot the function; as more terms are added the overshoot moves arbitrarily close to the discontinuity (at a distance about pi/M for M terms) but never disappears; its size is proportional to the jump, and at a square-wave corner the peak is (2/pi) Si(pi) = 1.1789797... times the half-jump, an excess of about 18% of the half-jump."
status: established
aliases: [Gibbs' phenomenon, Gibbs overshoot, Gibbs oscillations]
tags: [fourier-series, discontinuity, convergence]
timestamp: 2026-10-14T00:00:00Z
---

# Gibbs phenomenon

At a point of finite discontinuity, the partial sums $S_M f$ of a
[Fourier series](/definitions/fourier-series.md) overshoot the function. "Although as more
terms are included the overshoot moves in position arbitrarily close to the
discontinuity, it never disappears even in the limit of an infinite number of
terms. This behaviour is known as Gibbs' phenomenon"
([Riley et al. (2006)](/sources/riley-2006.md), §12.4, pp. 420–421).

The source states one quantitative property: "the size of the overshoot is
proportional to the magnitude of the discontinuity".

[Arfken et al. (2013)](/sources/arfken-2013.md) agree and derive the size.
They define the phenomenon as "an overshoot, a peculiarity of the Fourier
series and other eigenfunction series at a simple discontinuity" (§19.3,
p. 957).

## Derivation (Arfken et al., §19.3)

**Partial sums as a kernel integral.** For period $2\pi$, summing the
geometric series of the modes in $S_Mf$ gives (eqs. 19.29–19.31)
$$S_Mf(x) = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(t)\,\frac{\sin\bigl[(M+\tfrac12)(x-t)\bigr]}{\sin\tfrac12(x-t)}\,\mathrm dt,$$
whose kernel "is in the large-[$M$] limit a Dirac delta distribution"
(p. 958; see [Dirac delta function](/definitions/dirac-delta-function.md)).

**Square wave.** For the [square wave](/benchmarks/square-wave.md) of values
$\pm A/2$ (the source's $\pm h/2$, eq. 19.32), near the jump at $x = 0$ and with
$u = (M+\tfrac12)s$ (eq. 19.37),
$$S_Mf(x) \approx \frac{A}{2\pi}\int_0^{(M+\frac12)x}\frac{\sin u}{(M+\tfrac12)\sin\bigl(u/(2M+1)\bigr)}\,\mathrm du.$$
$S_Mf(0) = 0$, the mean, for every $M$. The partial sum peaks where
$(M+\tfrac12)x = \pi$, i.e. at $x \approx \pi/M$: "the location of the
overshoot maximum will differ from $x = 0$ in a manner approximately inversely
proportional to the number of terms" (pp. 959–960). With
$\sin(u/(2M+1)) \approx u/(2M+1)$, the peak value is (eqs. 19.38–19.43)
$$S_Mf(x_{\max}) \approx \frac{A}{\pi}\int_0^\pi\frac{\sin u}{u}\,\mathrm du = \frac A2\cdot\frac2\pi\int_0^\pi\frac{\sin u}{u}\,\mathrm du = \frac A2\,(1.1789797\ldots).$$
Since $\int_0^\infty(\sin u/u)\,\mathrm du = \pi/2$, the integral to $\pi$ is
$\pi/2$ minus the tail $\int_\pi^\infty(\sin u/u)\,\mathrm du$. The tail is
negative (the source identifies it through the sine-integral function), so
the integral exceeds $\pi/2$ (eqs. 19.39–19.41). The source also shows this by an
alternating-lobe argument (eq. 19.42). The series therefore "tends to overshoot the positive corner of
the square wave by some 18% and to undershoot the negative corner by the same
amount" (p. 960). The 18% is relative to the half-jump $A/2$, the height of
the corner above the mean. As a compiler remark, the excess
$0.0894899\ldots\,A$ is about 9% of the full jump $A$. Exercise 19.3.3 gives
the constant to twelve figures, $1.178979744472$. The overshoot is
proportional to $A$, in agreement with Riley et al.

"The inclusion of more terms (increasing [$M$]) does nothing to remove this
overshoot but merely moves it closer to the point of discontinuity", and
because of it "the Fourier series representation may be highly unreliable for
precise numerical work, especially in the vicinity of a discontinuity"
(p. 961, fig. 19.11, 20 to 100 terms).

## Scope

* Riley et al. give no proof and no value of the overshoot ("A full discussion
  is not pursued here", p. 421), and they do not state it as a fraction of the
  jump. Arfken et al. supply the derivation and the value above. Their
  derivation is for the square wave, with the small-angle approximation of the
  kernel. The proportionality to the jump then carries the result to any
  jump, though the source does not state that generalization.
* Arfken et al. state that the phenomenon "is not limited to the Fourier
  series. It occurs with other eigenfunction expansions", citing Thompson
  (1992) (p. 961). Their reading list names the Lanczos convergence
  technique, "which suppresses the Gibbs phenomenon oscillations" (Lanczos,
  1956). The chapters read do not present it.
* The statement concerns partial sums. It coexists with
  [pointwise convergence](/results/fourier-series-convergence.md) to the
  midpoint *at* the jump: the overshoot is not at a fixed point but moves
  towards the jump as $M$ grows.
* The phenomenon is illustrated on the [square wave](/benchmarks/square-wave.md)
  with 1, 2, 3 and 20 terms (fig. 12.3). The overshoot marked in panel (d)
  (labelled delta there) is not quantified. Arfken et al. show it on the
  square wave (fig. 19.11) and on the [sawtooth wave](/benchmarks/sawtooth-wave.md)
  (fig. 19.2).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §12.4 (pp. 420–421), fig. 12.3.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §19.3 (eqs. 19.29–19.43, fig. 19.11, pp. 957–961), §19.1 (fig. 19.2, p. 938); exercise 19.3.3.
