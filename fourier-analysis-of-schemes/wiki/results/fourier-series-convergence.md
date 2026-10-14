---
type: Result
title: "Convergence of Fourier series"
description: "Under the Dirichlet conditions the Fourier series converges to f at points of continuity and to the mean of the one-sided limits at a finite discontinuity (stated without proof); term-by-term integration converges to the integral, and term-by-term differentiation converges to f' when f is continuous and periodic and f' satisfies the Dirichlet conditions."
status: established
aliases: [pointwise convergence of Fourier series, term-by-term differentiation, term-by-term integration, midpoint convergence at a jump]
tags: [fourier-series, convergence, discontinuity]
timestamp: 2026-10-14T00:00:00Z
---

# Convergence of Fourier series

## Pointwise convergence

If $f$ satisfies the [Dirichlet conditions](/definitions/dirichlet-conditions.md),
its [Fourier series](/definitions/fourier-series.md) converges to $f(x)$ at
every point where $f$ is continuous
([Riley et al. (2006)](/sources/riley-2006.md), §12.1, p. 416). At a point
$x_d$ of finite discontinuity it converges to the mean of the one-sided limits
(§12.4, p. 420):
$$\frac12\lim_{\epsilon\to0}\bigl[f(x_d + \epsilon) + f(x_d - \epsilon)\bigr].$$
Both statements are made **without proof**; the second is introduced with "we
state without proof". The series "itself does not produce a discontinuous
function". Near the jump the partial sums overshoot: see
[Gibbs phenomenon](/results/gibbs-phenomenon.md).

[Arfken et al. (2013)](/sources/arfken-2013.md) state the same mean-value limit
(eq. 19.7) and refer its proof to Jeffreys and Jeffreys or to Carslaw
(§19.1, p. 937). Exercise 19.3.1 asks the reader to derive it from the
partial-sum kernel of the Gibbs analysis, identifying part of the integrand as
a Dirac delta function. The [sawtooth wave](/benchmarks/sawtooth-wave.md)
illustrates it: every partial sum passes through $0$ at the jump (p. 938).

## Convergence in the mean and uniform convergence

(Arfken et al., §19.1, pp. 936–937.) Because the modes are the complete
eigenfunctions of a Hermitian Sturm–Liouville problem, the Fourier expansion
of a square-integrable function "will at least converge in the mean", and
"the representation of a function by an orthogonal expansion is only
guaranteed to converge in the mean". With discontinuities "there is no unique
value to which the expansion must converge"; for Fourier series the value at
the jump is the mean above. The source adds, citing Churchill, that if $f$ is
continuous but its first derivative has a finite discontinuity, the series
converges **uniformly**. Riley et al. state neither result in the chapters
read.

Consequence for periodic extensions: if the extension of a function given on a
finite range jumps at an end-point, the series converges there to the mean,
not to the end value. The odd extension of $x^2$ on $(0,2]$ converges to $0$
at $x = \pm 2$ (§12.5, pp. 423–424; exercise 12.18).

## Term-by-term integration and differentiation

(§12.6, p. 424, stated without proof.)

* The series of $f$ integrated term by term converges to the integral of $f$,
  up to a constant of integration to be determined separately.
* If $f$ is continuous for all $x$ and periodic, the series differentiated
  term by term converges to $f'$, **provided** $f'$ itself satisfies the
  Dirichlet conditions.

Arfken et al. (§19.1, pp. 942–944) agree on integration and go further.
Integration divides each coefficient by $m$, "a convergent Fourier series may
always be integrated term by term, the resulting series converging uniformly
to the integral of the original function", and this "may be valid even if the
original series … is not itself convergent. The function $f(x)$ need only be
integrable" (citing Jeffreys and Jeffreys). The integrated series is not
itself a Fourier series when $a_0 \ne 0$, because of the term $a_0x/2$;
subtracting that term leaves one (eqs. 19.16–19.17). On differentiation "the
word is caution". The source's examples are the
[sawtooth wave](/benchmarks/sawtooth-wave.md), whose differentiated series
diverges (eq. 19.20), and the continuous triangular wave, whose differentiated
series is that of the [square wave](/benchmarks/square-wave.md)
(eqs. 19.21–19.23). Its rule: "In general, term-by-term differentiation is
permissible if the series to be differentiated is uniformly convergent"
(p. 944).

**Qualification: two different sufficient conditions.** Riley et al. require
$f$ continuous and periodic with $f'$ satisfying the Dirichlet conditions.
Arfken et al. require uniform convergence of "the series to be
differentiated". Neither source says the other's condition fails, and both
sources' examples satisfy both conditions or fail both, so this is recorded
as a qualification, not a contradiction.

**Compiler's note (hypothesis).** Read literally, as uniform convergence of
the original series, Arfken et al.'s condition is not sufficient. The series
$\sum_m \sin(m^2x)/m^2$ converges uniformly, but its term-by-term derivative
$\sum_m\cos(m^2x)$ has terms that do not tend to zero, so it diverges. The
classical theorem asks for uniform convergence of the differentiated series.
A source on real analysis would settle the reading.

The continuity requirement matters: exercise 12.10 asks why the series of
$e^x$ on $(-1,1)$ cannot be differentiated term by term to recover $e^x$. Its
periodic extension is discontinuous at $x = \pm1$. Exercise 12.7 shows the
sine series of $1 - x$ on $[0,1]$ differentiated term by term "does not
converge" (answer, p. 431).

## Rate of decay of coefficients

Riley et al.'s chapter states no general theorem linking smoothness to the
decay rate of $a_m, b_m$. The link appears only in exercises: 12.8 asks the
reader to pick, "by sketching the function and considering its derivative",
the faster-converging extension of $x\sin x$, and states a convergence
$\sim m^{-3}$ for it.

Arfken et al. (§19.2, p. 951) state the link as what "we can expect", drawn
from two examples and a reference (Raisbeek, 1955), without proof:

* if $f$ has discontinuities, the $m$-th coefficient decreases as $O(1/m)$, and
  "convergence is conditional only" (the [square wave](/benchmarks/square-wave.md));
* if $f$ is continuous, possibly with discontinuous derivatives, it decreases
  as $1/m^2$, "that is, absolute convergence" (the full-wave rectifier).

Exercise 19.1.4 adds that the coefficients of a square-integrable $f$ tend to
zero, by Bessel's inequality. The two sources do not conflict: Riley et al.
give no rule, and Arfken et al. give a heuristic one.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§12.1, 12.4–12.6 (pp. 416–424); exercises 12.7, 12.8, 12.10, 12.18 and answers (pp. 428–431).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §19.1 (eqs. 19.7, 19.15–19.23, pp. 936–944), §19.2 (p. 951); exercises 19.1.4, 19.3.1.
