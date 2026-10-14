---
type: Definition
title: "Laplace transform"
description: "The one-sided transform of f(t) on t >= 0 with kernel exp(-s t), defined for real s above an abscissa of convergence; linear, unique up to values at isolated points, inverted in practice from a table of standard transforms, and the tool for initial-value problems because it turns derivatives into algebraic terms carrying the initial data."
status: established
aliases: [Laplace transformation, inverse Laplace transform, table of Laplace transforms]
tags: [laplace-transform, initial-value-problem]
timestamp: 2026-10-13T00:00:00Z
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

## Role in initial-value problems

The transform turns a derivative into an algebraic term carrying the initial
data, $\mathcal L\{f'\} = s\,\mathcal L\{f\} - f(0)$; the full set of rules is on
[Laplace transform properties](/results/laplace-transform-properties.md). The
source's application to differential equations is in its ch. 15 and the
contour inversion in ch. 25. Neither was read for this bundle, and no
stability use of the Laplace transform appears in the chapters read.
Exercise 13.24 asks for the impulse response (Green's function) of
$\gamma^{-1}\,\mathrm dy/\mathrm dt + y = \delta(t)$, first by a limit of
rectangular pulses and then "much more directly" by transforming the equation
and using table 13.1; its stated answer is $y(t) = \gamma\,e^{-\gamma t}$
(the source writes the time constant $\gamma^{-1}$ as $T$ and the unknown as
$x$).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §13.2 (pp. 453–455), table 13.1, exercise 13.24 (p. 465).
