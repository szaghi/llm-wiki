---
type: Method
title: "Separation of variables"
description: "Seek product solutions of a linear PDE so that it splits into ODEs coupled only through separation constants, choose the constants and the form of each factor from the boundary conditions, and superpose over the allowed constants, a sum for discrete values (Fourier, Bessel, Legendre expansions) or an integral for a continuum; in polar coordinates single-valuedness and regularity select the special functions."
status: established
aliases: [separated solutions, separation constants, eigenfunction expansion, normal modes]
tags: [separation-of-variables, superposition, special-functions, boundary-conditions]
timestamp: 2026-10-13T00:00:00Z
---

# Separation of variables

## Method

Seek $u = X(x)Y(y)Z(z)\mathcal T(t)$, a function **separable** in each
variable ([Riley et al. (2006)](/sources/riley-2006.md), eq. 21.1, p. 713).
For the [wave equation](/definitions/wave-equation.md), substituting and
dividing by $u$ gives
$$\frac{X''}{X} + \frac{Y''}{Y} + \frac{Z''}{Z} = \frac{1}{c^2}\frac{\mathcal T''}{\mathcal T}$$
(eq. 21.5, p. 714). Each term depends on a different variable, so each
equals a constant, the **separation constants**, linked by one algebraic
relation. The PDE is replaced by ODEs (eq. 21.6, p. 715). A PDE in $n$
variables gives $n - 1$ independent separation constants (p. 717). The book
notes that a separable solution is "likely" impossible for a general PDE,
but exists for the important ones (p. 714).

The sign of each constant, and whether a factor is written with
exponentials, trigonometric or hyperbolic functions, follow from the
boundary conditions. For the [diffusion equation](/definitions/diffusion-equation.md),
decay as $t \to \infty$ requires the constant $-k^2$ with $k$ real, giving
$(C_1\cos kx + C_2\sin kx)e^{-\kappa k^2t}$ (eqs. 21.9–21.12,
pp. 716–717). For $\nabla^2u = 0$ in the plane,
$(C_1\cosh kx + C_2\sinh kx)(C_3\cos ky + C_4\sin ky)$ (eqs. 21.13–21.15,
p. 717).

## Superposition

For a linear PDE, a sum of separated solutions over the allowed values of
the separation constants is a solution,
$u = \sum_n B_n X_n(x)Y_n(y)$ (eq. 21.16, p. 718). The remaining boundary
condition fixes the $B_n$. This is "possible provided that the functions
$X_n$ form a complete set", as do Fourier sine series or spherical
harmonics; completeness is cited from chapters not read (p. 718). If the
conditions allow a zero separation constant, that term has a different
form and must be derived from the separated ODEs (p. 718).

**Steady temperature in a plate** $0 \le y \le L_y$, $x \ge 0$, held at
$u = 0$ on $y = 0, L_y$ and at infinity, with $u(0,y) = g(y)$:
$$u = \sum_{n\ge1} B_n e^{-n\pi x/L_y}\sin\frac{n\pi y}{L_y}, \qquad B_n = \frac{2}{L_y}\int_0^{L_y} g(y)\sin\frac{n\pi y}{L_y}\,\mathrm dy$$
(eqs. 21.17–21.19, p. 719). The series is the Fourier sine series of the
odd periodic continuation of $g$. Where $g$ does not vanish at the
corners, the continuation jumps and the series converges to the mid-point
(p. 719). For a plate of finite length $L_x$, hyperbolic functions
$\sinh[n\pi(L_x - x)/L_y]$ meet $u(L_x,y) = 0$ directly (eqs. 21.20–21.22,
pp. 720–721). Data on several sides are handled by superposing problems
that each carry data on one side (pp. 721–722). Inhomogeneous boundary
conditions are first removed by subtracting a steady-state profile
(pp. 723–724; [homogeneous linear problems](/definitions/homogeneous-linear-problem.md)).

**Continuum.** If the boundary conditions leave the separation constant
free (an infinite range), the sum becomes an integral over it. Separation
then reproduces the Fourier-transform solution (pp. 724, 751; [integral
transform methods](/methods/integral-transform-methods.md)).

## Polar coordinates

With the Laplacian in plane polar, cylindrical and spherical polar
coordinates (eqs. 21.23–21.25, p. 725):

* **Plane polars, $\nabla^2u = 0$.** $\Phi'' = -n^2\Phi$, and
  single-valuedness forces integer $n$. The radial equation is an Euler
  equation, giving $r^{\pm n}$, or $\ln r$ and a constant for $n = 0$. The
  general solution is
  $u = C_1\ln r + C_2 + \sum_{n\ge1}(B_n\cos n\phi + B_n'\sin n\phi)(C_nr^n + C_n'r^{-n})$,
  with $C_1 = 0$ if the region contains the origin (eqs. 21.27–21.31,
  pp. 726–727).
* **Cylindrical polars.** $Z = e^{\pm kz}$, $\Phi$ trigonometric with
  integer order $n$, and the radial equation is Bessel's equation, with
  solutions $J_n(kr)$, $Y_n(kr)$. $Y_n$ is excluded on the axis (eqs.
  21.32–21.35, pp. 728–729). The coefficients follow from Bessel
  orthogonality (eq. 21.36, p. 730).
* **Spherical polars.** $R = r^{\ell}$ or $r^{-(\ell+1)}$. The polar
  equation is the associated Legendre equation, with solutions
  $P_\ell^n(\cos\theta)$, $Q_\ell^n(\cos\theta)$, $0 \le |n| \le \ell$, and
  $Q$ is excluded on the axis (eqs. 21.40–21.49, pp. 732–734). The angular
  factors are the spherical harmonics. They arise for every equation in
  which $\theta$ and $\phi$ enter only through $\nabla^2$ (p. 741).
* **Helmholtz equation** $\nabla^2U + k^2U = 0$ (from the wave and
  diffusion equations, eq. 21.53): the radial factors become $J_n(kr)$ in
  plane and cylindrical polars, and $r^{-1/2}J_{\ell+1/2}(kr)$ (spherical
  Bessel functions) in spherical polars (eqs. 21.55–21.57, pp. 738–741).

**Solution by expansion** (§21.3.3, pp. 741–744). Write the general
separated series, fix its coefficients where $u$ can be computed directly
(e.g. on an axis of symmetry), and invoke the
[uniqueness theorem](/results/uniqueness-theorem-poisson.md) to conclude
that the series is the solution everywhere. Worked example: the potential
of a uniform ring.

**Inhomogeneous equations** (§21.3.4, pp. 744–746). For an axisymmetric
$\nabla^2u = \psi$, expand $u = \sum_\ell R_\ell(r)P_\ell(\cos\theta)$ and
$\psi$ alike. Each $R_\ell$ then obeys the radial ODE
$r^{-2}(r^2R_\ell')' - \ell(\ell+1)r^{-2}R_\ell = \psi_\ell(r)$ (eq. 21.67).
The book prefers Green's functions for inhomogeneous problems (p. 744).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §21.1–21.3 (pp. 713–746).
