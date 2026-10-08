---
type: Method
title: "Unequal-stencil and adaptive-order WENO (WENO-ZQ, WENO-AO)"
description: "WENO reconstructions that blend one large centred high-order polynomial with small low-order ones through a weight-adjusted subtraction, so arbitrary positive linear weights keep full order: Zhu–Qiu's quartic plus two linear polynomials, and Balsara–Garain–Shu's adaptive-order WENO-AO(5,3), (7,3), (7,5,3), (9,5,3) with an r = 3 central WENO fallback."
status: established
aliases: [WENO-ZQ, WENO-AO, adaptive order WENO]
tags: [weno, adaptive-order, central-weno, legendre-basis]
timestamp: 2026-10-08T00:00:00Z
---

# Unequal-stencil and adaptive-order WENO (WENO-ZQ, WENO-AO)

**The device.** Let $P$ be the polynomial on a large centred stencil
and $p_k$ low-order polynomials on small stencils, with positive linear
weights $d_P + \sum_k d_k = 1$ chosen freely. The reconstruction
$$\frac{\omega_P}{d_P}\left(P - \sum_k d_k\,p_k\right) + \sum_k \omega_k\,p_k$$
reduces to $P$ when the nonlinear weights equal the linear ones, so the
order of $P$ is kept in smooth regions whatever the $d$'s, and reduces
to the small-stencil combination when $\omega_P \to 0$.

## WENO-ZQ

[Zhu & Qiu (2016)](/sources/zhu-2016.md): a quartic $P$ on five cells and
two linear polynomials on $\{I_{i-1}, I_i\}$ and $\{I_i, I_{i+1}\}$,
$d = (0.98, 0.01, 0.01)$ (any positive set summing to one is said not to
affect accuracy); Jiang–Shu-type indicators, the linear ones being
squared first differences;
$$\tau = \left(\frac{\vert\beta_P - \beta_1\vert + \vert\beta_P - \beta_2\vert}{2}\right)^2,\qquad \tilde\omega = d\left(1 + \frac{\tau}{\varepsilon + \beta}\right),\ \varepsilon = 10^{-6}$$
(eqs. 2.19–2.20, read from the page image), giving
$\omega - d = O(h^4)$ also when $f' = 0$. Near discontinuities the two
linear polynomials make the scheme "a TVD scheme with a van Albada-like
limiter". Fifth order is reached with three different linear weight sets,
with smaller errors and lower CPU time than WENO-JS for equal error.

## WENO-AO

[Balsara, Garain & Shu (2016)](/sources/balsara-2016.md) replace the two
linear polynomials by the three $r = 3$ central WENO (CWENO) stencils,
whose central stencil gets the largest weight — a combination they
report as extremely stable and extremum-preserving
([central WENO](/methods/central-weno.md)) — so the fallback is third
order and does not clip extrema. Weights for AO(5,3):
$\tau = \tfrac13\sum_{k=1}^{3}\vert\beta_P - \beta_k\vert$ and
$\tilde\omega = d\,(1 + \tau^2/(\beta + \varepsilon)^2)$, $\varepsilon \approx 10^{-12}$
(eqs. 3.6–3.9, read from the page image; a WENO-JS-type alternative is
"more stable", this one "more accurate"); linear weights from two
parameters, $d_P = \gamma_{\mathrm{Hi}}$ and the CWENO central share
$\gamma_{\mathrm{Lo}}$, both $0.85$ in the tests.
* **Higher orders** AO(7,3), AO(9,3), and **recursion** AO(7,5,3),
  AO(9,5,3): the AO(7,3) and AO(5,3) polynomials are hybridized again,
  with unsquared weights so that the switch away from seventh order is
  not too eager; a convexity condition is checked and violations fall
  back to AO(7,3).
* **Legendre basis.** Reconstructions are written in Legendre moments,
  and the indicators become sums of perfect squares of those moments,
  identical in form for every stencil of a given $r$ and nested across
  $r$, for $r = 3$–$9$ (to 17th order). This makes the indicators cheap:
  AO(5,3) costs less than WENO-JS5, AO(7,3) about as much, AO(9,3) about
  20 % more (Table 4).
* **No MP step and no steepener** are needed: the cubic and higher
  moments are suppressed when the large stencil is rough
  ([monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md)).
* **Results:** design order on advection, Burgers and 2D Euler, AO(5,3)
  more than half an order of magnitude more accurate than WENO-ZQ on
  advection; modified-wavenumber curves comparable to fourth- and
  sixth-order compact schemes; composite advection over 4000 points,
  Lax, blast waves, Shu–Osher, double Mach reflection
  ($1600 \times 400$), forward step and an oblique shock–vortex test.
  The authors relate AO to MOOD: both drop order for stability, but AO is
  *a priori*, one update per zone.

## Contradictions

**Is WENO-ZQ free of spurious extrema and clipping?**
* [Zhu & Qiu (2016)](/sources/zhu-2016.md): the scheme escapes
  "nonphysical oscillations adjacent strong shocks or contact
  discontinuities", and behaves like a TVD scheme with a van Albada-like
  limiter near them (their tests: Burgers, Euler smooth cases, Lax,
  Shu–Osher, blast waves, double Mach, forward step).
* [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §5.1, Fig. 3a:
  run as published ($d_P = 0.98$, eqs. 2.19–2.20) on the Jiang–Shu
  composite advection over ten periods, WENO-ZQ shows overshoots and
  undershoots; removing the square in its $\tau$ removes them but
  flattens the Gaussians and triangle — "inevitable" with a van Albada
  limiter, which clips extrema.
* *Compiler reading:* the two papers test different problems; Zhu and Qiu
  do not run the composite advection, Balsara et al. do. The disputed
  claim is general non-oscillation. **Open.**

# Citations

1. [Zhu & Qiu (2016)](/sources/zhu-2016.md), §§1–3.
2. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §§1–6.
