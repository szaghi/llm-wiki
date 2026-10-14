---
type: Definition
title: "Laplace transform"
description: "The one-sided transform of f(t) on t >= 0 with kernel exp(-s t), defined for s above an abscissa of convergence (existing for functions of exponential order); linear, unique up to a null function (Lerch), inverted from a table of standard transforms or by the Bromwich contour integral, and the tool for initial-value problems because it turns derivatives into algebraic terms carrying the initial data."
status: established
aliases: [Laplace transformation, inverse Laplace transform, table of Laplace transforms]
tags: [laplace-transform, initial-value-problem]
timestamp: 2026-10-14T00:00:00Z
---

# Laplace transform

## Definition

For $f(t)$ given on $t > 0$ the **Laplace transform** is
([Riley et al. (2006)](/sources/riley-2006.md), eq. 13.53)
$$\mathcal L\{f\}(s) = \int_0^\infty f(t)\,e^{-st}\,\mathrm dt,$$
provided the integral exists. The source motivates it twice: functions such
as $f(t) = t$ that do not decay have no Fourier transform, and an
initial-value problem needs $f$ only for $t > 0$ (§13.2, p. 453). It assumes
$s$ real, noting that "complex values would have to be considered in a more
detailed study". For a given $f$ there is typically a real $s_0$ such that the
integral exists for $s > s_0$ and diverges for $s \le s_0$.

[Arfken et al. (2013)](/sources/arfken-2013.md) give the same definition
(eq. 20.126) and a sufficient condition for existence (eq. 20.127). If, for
some $s_0$ and $t_0 \ge 0$, $\lvert e^{-s_0t}f(t)\rvert$ stays below a fixed
bound for all $t > t_0$, then $f$ is "of exponential order" and its transform
exists for $s > s_0$. The transform fails
to exist for $e^{t^2}$, which is not of exponential order, and for a strong
enough singularity at $t = 0$, as for $t^p$ with $p \le -1$ (p. 1008). They also
take $s$ "real and positive" in general and note that "it is possible to let
$s$ become complex", provided its real part is positive. They call this transform one-sided,
as against the two-sided integral over $(-\infty, \infty)$, and record that some
authors add a factor $s$ to it (footnote 6, p. 1008). For a transform of a
function of exponential order, $\mathcal L\{f\}(s)\to0$ as $s\to\infty$, so "if
$f(s)$ behaves asymptotically for large $s$ as a positive power of $s$, then no
inverse transform can exist" (p. 1010). The delta function, with
$\mathcal L\{\delta\} = 1$, lies outside that class; exercise 20.7.7 asks the
reader to "comment on this fiasco".

The transform is linear (eq. 13.54):
$\mathcal L\{af_1 + bf_2\} = a\,\mathcal L\{f_1\} + b\,\mathcal L\{f_2\}$, where $a$
and $b$ are constants.

## Inversion

Inversion "is not an easy operation". The general inversion formula needs
complex-variable theory and is deferred to the source's ch. 25, outside this
bundle's reading. In practice an inverse is found by matching against a table
of standard transforms (table 13.1), often after partial fractions. The source
states that "for all practical purposes" the inverse is unique and linear
(eq. 13.56). Its footnote adds that this "is not strictly true, since two
functions can differ from one another at a finite number of isolated points
but have the same Laplace transform" (p. 454).

Arfken et al. agree and name the result **Lerch's theorem**. Two functions
with the same transform differ by a null function, one whose integral from
$0$ to $t_0$ vanishes for every $t_0 > 0$, so they may differ at isolated
points (p. 1011). They list three ways to invert: tables (with
partial fractions and the operational rules), the contour integral below, and
numerical inversion (citing Krylov and Skoblya). Of tables they add that
"there is some justification for suspecting that these tables are probably of
more value in solving textbook exercises than in solving real-world problems"
(p. 1011).

**Bromwich integral** (Arfken et al., §20.10, eq. 20.203). The inversion
formula that Riley et al. defer to their ch. 25 is
$$f(t) = \frac{1}{2\pi\mathrm i}\int_{\beta-\mathrm i\infty}^{\beta+\mathrm i\infty}e^{st}\,\mathcal L\{f\}(s)\,\mathrm ds,$$
with the real abscissa $\beta$ to the right of every singularity of
$\mathcal L\{f\}$. The source derives it by applying the Fourier
integral to $e^{-\beta t}f(t)$ and substituting $s = \beta + \mathrm iu$. When
$\mathcal L\{f\}$ has only isolated singularities, no branch points, and is small
at large $\lvert s\rvert$, closing the contour in the left half-plane gives
$f(t)$ as the sum of the residues of $e^{st}\mathcal L\{f\}$ (eq. 20.204). The
derivation "is not presented as a rigorous one … although it can be made
rigorous", and any inverse "can always be checked" by transforming it back
(p. 1042).

## Standard transforms (table 13.1)

| $f(t)$ | $\mathcal L\{f\}(s)$ | $s_0$ |
|---|---|---|
| $c$ | $c/s$ | $0$ |
| $c\,t^p$ | $c\,p!/s^{p+1}$ | $0$ |
| $\sin bt$, $\cos bt$ | $b/(s^2+b^2)$, $s/(s^2+b^2)$ | $0$ |
| $e^{at}$, $t^pe^{at}$ | $1/(s-a)$, $p!/(s-a)^{p+1}$ | $a$ |
| $\sinh at$, $\cosh at$ | $a/(s^2-a^2)$, $s/(s^2-a^2)$ | $\lvert a\rvert$ |
| $e^{at}\sin bt$, $e^{at}\cos bt$ | $b/[(s-a)^2+b^2]$, $(s-a)/[(s-a)^2+b^2]$ | $a$ |
| $t^{1/2}$, $t^{-1/2}$ | $\tfrac12(\pi/s^3)^{1/2}$, $(\pi/s)^{1/2}$ | $0$ |
| $\delta(t - t_0)$ | $e^{-st_0}$ | $0$ |
| $H(t - t_0)$ | $e^{-st_0}/s$ | $0$ |

Here $a$, $b$, $c$ are constants and $p = 0, 1, 2, \dots$; each entry holds
for $s > s_0$.

Arfken et al.'s table 20.1 agrees with every entry it shares with this table,
and gives $t^p$ for real $p > -1$ as $\Gamma(p+1)/s^{p+1}$ (eq. 20.136), which
contains both entries $t^{\pm1/2}$. It adds the following ($s_0 = 0$):

| $f(t)$ | $\mathcal L\{f\}(s)$ | Eq. |
|---|---|---|
| $t\cos bt$ | $(s^2 - b^2)/(s^2 + b^2)^2$ | 20.177 |
| $t\sin bt$ | $2bs/(s^2 + b^2)^2$ | 20.178 |
| $J_0(bt)$ | $(s^2 + b^2)^{-1/2}$ | 20.182 |

## Role in initial-value problems

The transform turns a derivative into an algebraic term carrying the initial
data, $\mathcal L\{f'\} = s\,\mathcal L\{f\} - f(0)$; the full set of rules is on
[Laplace transform properties](/results/laplace-transform-properties.md). The
source's application to differential equations is in its ch. 15 and the
contour inversion in ch. 25. Neither was read for this bundle.

Arfken et al. (§20.8) make that application in the chapter read. Linear ODEs
with constant coefficients, and coupled systems of them, "transform to
simultaneous linear algebraic equations". The initial values enter through the
derivative rule, "different than for the Fourier transform", because of "the
finite lower limit ($t = 0$) of the integral defining the transform", which
"makes the Laplace transform more powerful for obtaining solutions to
differential equations subject to initial conditions" (p. 1016). Their
examples are the free, damped and driven oscillator and Euler's equations for
free precession. Beyond constant coefficients "the Laplace transform may still
be applied, but there is no guarantee that it will be helpful" (Bessel's
equation, p. 1027). Neither source makes any stability use of the Laplace
transform in the chapters read.
Exercise 13.24 asks for the impulse response (Green's function) of
$\gamma^{-1}\,\mathrm dy/\mathrm dt + y = \delta(t)$, first by a limit of
rectangular pulses and then "much more directly" by transforming the equation
and using table 13.1; its stated answer is $y(t) = \gamma\,e^{-\gamma t}$
(the source writes the time constant $\gamma^{-1}$ as $T$ and the unknown as
$x$). Arfken et al. treat the same idea for a damped oscillator. The response
to an impulsive force is the free damped oscillation launched with the
impulse as initial momentum (eq. 20.194), and the response to any force is the
convolution of the force with it (eq. 20.193; see the
[convolution theorem](/results/convolution-theorem.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §13.2 (pp. 453–455), table 13.1, exercise 13.24 (p. 465).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §20.1 (eq. 20.7, p. 965), §20.7 (eqs. 20.126–20.141, table 20.1, pp. 1008–1012), §20.8 (pp. 1016–1027), §20.9 (eqs. 20.193–20.194, p. 1036), §20.10 (eqs. 20.198–20.204, pp. 1038–1042); exercise 20.7.7.
