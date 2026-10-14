---
type: Method
title: "Series solutions of linear ODEs (Frobenius' method)"
description: "About an ordinary or regular singular point of y'' + a1 y' + a0 y = 0, substitute a power series times (x - x0)^nu: the lowest power gives the indicial equation for nu, the rest a recurrence for the coefficients; Fuchs' theorem guarantees at least one such solution, a second follows from the Wronskian and carries a logarithm when the indicial roots coincide or differ by an integer, and the regular solution is the one kept on the axis or at the origin when separated PDEs produce Bessel and Legendre equations."
status: established
aliases: [Frobenius method, power-series solution, indicial equation, Fuchs' theorem, regular singular point, irregular singular point, ordinary point]
tags: [ode, series-solution, singular-points, special-functions]
timestamp: 2026-10-14T00:00:00Z
---

# Series solutions of linear ODEs (Frobenius' method)

The radial and polar equations produced by [separation of
variables](/methods/separation-of-variables.md) in curvilinear coordinates
(Bessel's, Legendre's) have no closed-form solution in elementary
functions. They are solved by power series, and which series is admissible
is decided by the singular points of the equation. This page records the
method as [Arfken et al. (2013)](/sources/arfken-2013.md) present it (§7.4–7.6,
pp. 343–369); it is kept to what the PDE pages use.

## Singular points

Write the homogeneous equation as
$$y'' + a_1(x)\,y' + a_0(x)\,y = 0$$
(eq. 7.19, p. 344). A point $x_0$ is **ordinary** if $a_1$ and $a_0$ are
finite there, **singular** otherwise. A singular point is **regular** if
$(x - x_0)a_1$ and $(x - x_0)^2a_0$ stay finite, **irregular** (an essential
singularity) if not. The point at infinity is classified by setting
$x = 1/z$ and examining $z \to 0$ (eqs. 7.20–7.22, p. 344). Bessel's
equation $x^2y'' + xy' + (x^2 - n^2)y = 0$ has a regular singular point at
$0$ and an irregular one at $\infty$; Legendre's has regular singular points
at $\pm1$ and $\infty$ (Example 7.4.1 and Table 7.1, pp. 344–345).

## The method

Substitute
$$y = \sum_{j=0}^{\infty}C_j\,(x - x_0)^{\nu + j}, \qquad C_0 \ne 0$$
(eqs. 7.28, 7.38, pp. 347, 350). The coefficient of the lowest power gives
the **indicial equation** for $\nu$; the remaining powers give a
**recurrence relation** for the $C_j$ (pp. 347–348). For $y'' + \omega^2y = 0$
the indicial roots are $\nu = 0, 1$, and the two series are $\cos\omega x$
and $\omega^{-1}\sin\omega x$ (eqs. 7.30–7.37, pp. 347–349). For Bessel's
equation they are $\nu = \pm n$; $\nu = n$ gives
$$J_n(x) = \sum_{j=0}^{\infty}\frac{(-1)^j}{j!\,(n + j)!}\left(\frac x2\right)^{n + 2j}$$
(eqs. 7.43–7.49, pp. 352–353), and for integer $n$ the root $\nu = -n$
makes the recurrence blow up, so it gives no second series (p. 353).

Two cautions accompany the method (p. 350): substitute the series back
into the equation, and check its convergence, since a formal series can
satisfy the equation and still diverge where it is needed (Legendre's
equation is the example). A series about $x_0$ can be expected to diverge
at the distance of the nearest singularity of the equation in the complex
plane (p. 350).

**Fuchs' theorem** (stated, p. 355). About an ordinary point or a regular
singular point there is always at least one power-series solution. About
an irregular singular point the method may fail: $y'' - 6x^{-3}y = 0$ has
no admissible indicial root, and $y'' + x^{-2}y' - b^2x^{-2}y = 0$ yields a
series that diverges for every $x \ne 0$ (eqs. 7.50–7.53, pp. 354–355).
The book does not prove the theorem.

**Number of series solutions** (p. 355). Equal indicial roots give one
series solution. Roots differing by a non-integer give two. Roots
differing by an integer: the larger gives a solution, the smaller may or
may not.

## The second solution

The [Wronskian](/definitions/wronskian.md) obeys Abel's formula, which turns
one solution into a second:
$$y_2(x) = y_1(x)\int^{x}\frac{\exp\left(-\int^{q}a_1(q')\,\mathrm dq'\right)}{y_1(q)^2}\,\mathrm dq$$
(eq. 7.67, p. 363); this is the reduction of order of [structure of linear
ODE solutions](/results/linear-ode-solution-structure.md). Expanding it
about a regular singular point with indicial roots differing by a
non-negative integer shows the form
$$y_2 = y_1\ln|x - x_0| + \sum_j C_j'(x - x_0)^{\nu_2 + j},$$
the logarithm being present unless one coefficient vanishes by accident
(eqs. 7.69–7.82, pp. 364–366). For Bessel's equation with $n = 0$ this
reproduces, up to scale and a multiple of $J_0$, the Neumann function $Y_0$
(Example 7.6.4, pp. 366–367). The first solution "usually converges at the
origin" and is called **regular**; the second, divergent there through the
logarithm and the negative powers, **irregular** (p. 369).

The simplest regular singular point is that of the Euler equation, where
the series has one term: $y = x^\nu$, with the auxiliary roots as indicial
roots, and $x^\nu\ln x$ for a repeated root ([Riley et al. (2006)](/sources/riley-2006.md),
eqs. 15.36–15.38, pp. 503–505; Arfken et al., eqs. 7.50 and 7.52, p. 354,
and Exercise 7.6.26, p. 374).

## Use in the PDE pages

The choice of solutions in curvilinear separation is this choice of the
regular solution. On the axis of a cylinder only $J_n$ is kept, $Y_n$ being
singular there (Riley et al., pp. 728–729; Arfken et al., Example 9.4.3,
p. 424). In spherical coordinates the Legendre solutions must be regular
at $\cos\theta = \pm1$, which fixes the separation constant to
$\ell(\ell+1)$ (Arfken et al., pp. 425–426), and only $r^\ell$ or $j_\ell$
are kept at the origin (p. 430). Arfken et al. also note a parity rule:
when the operator is even under $x \to -x$, the solutions can be chosen even
and odd (pp. 351, 353).

# Citations

* [Arfken et al. (2013)](/sources/arfken-2013.md), §7.4 (pp. 343–346),
  §7.5 (pp. 346–358), §7.6 (pp. 358–369), Exercise 7.6.26 (p. 374),
  §9.4 (pp. 424–430).
* [Riley et al. (2006)](/sources/riley-2006.md), §15.2.1 (pp. 503–505),
  §21.3.1 (pp. 728–729).
