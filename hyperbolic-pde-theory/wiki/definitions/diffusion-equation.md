---
type: Definition
title: "Diffusion equation"
description: "The model parabolic equation, kappa times the laplacian of u equals u_t, derived from a gradient flux law and the divergence theorem over an arbitrary volume; it admits no travelling-wave general solution, but has the error-function similarity solution in x over the square root of t, decaying separated modes, and the Gaussian heat-kernel solution of the initial-value problem."
status: established
aliases: [heat equation, heat conduction equation]
tags: [model-equation, parabolic, similarity-solution]
timestamp: 2026-10-13T00:00:00Z
---

# Diffusion equation

$$\kappa\,\nabla^2 u = \partial_t u$$
describes the temperature in a region without heat sources, or the
concentration of a diffusing substance. $\kappa$ is the diffusivity
([Riley et al. (2006)](/sources/riley-2006.md), eq. 20.2, p. 678). It is
second order in space and first order in time, and
[parabolic](/definitions/second-order-pde-classification.md).

**Derivation.** The heat flow per unit area is proportional to minus the
temperature gradient. The heat leaving an arbitrary volume through its
surface is converted to a volume integral by the divergence theorem and
equated to minus the rate of change of the heat content. Since the volume
is arbitrary, the integrands agree, giving the equation with $\kappa$ equal
to conductivity over (specific heat $\times$ density) (eqs. 20.3–20.4,
pp. 678). With variable material properties the spatial term becomes a
divergence $\nabla\cdot(\alpha\nabla u)$, and a distributed heat source
adds a source term (pp. 678–679). The steady state $\partial_t u = 0$ is
[Laplace's equation](/definitions/laplace-and-poisson-equations.md)
(p. 679).

## Solutions

* **No combination-variable solution.** Since $u$ is differentiated a
  different number of times in $x$ and $t$, $u = F(ax + bt)$ cannot
  work (§20.5, p. 696; contrast the [wave equation](/definitions/wave-equation.md)).
  Setting both sides equal to a constant gives the polynomial solution
  $u = C_1(x^2/(2\kappa) + t) + C_2x + C_3$ (eq. 20.35, p. 696).
* **Similarity solution.** $\kappa$ has dimensions length$^2$/time, so
  $x^2/(\kappa t)$ is dimensionless. Seeking $u$ as a function of it alone
  reduces the PDE to an ODE, whose solution is
  $$u(x,t) = C_1\int_{\zeta_0}^{\zeta} e^{-q^2}\,\mathrm dq, \qquad \zeta = \frac{x}{2\sqrt{\kappa t}}$$
  (eq. 20.36, p. 697), i.e. an [error function](/notation.md) for
  $\zeta_0 = 0$. A level of $u$ moves a distance proportional to
  $\sqrt t$, "a typical diffusion process". For $x, t \ge 0$ the solution
  is uniform at $t = 0$ and zero at $x = 0$ (p. 697).
* **Separated solutions.** $u = (C_1\cos kx + C_2\sin kx)\,e^{-\kappa k^2 t}$
  with real $k$ decays to zero as $t \to \infty$. The sign of the
  separation constant is chosen for that decay (eqs. 21.9–21.12,
  pp. 716–717; [separation of variables](/methods/separation-of-variables.md)).
* **Initial-value problem on the line.**
  $u = \int K(x - x', t)\,u_0(x')\,\mathrm dx'$ with the Gaussian heat
  kernel $K$ (eq. 21.74, p. 750; [fundamental solution](/definitions/fundamental-solution.md),
  [integral transform methods](/methods/integral-transform-methods.md)).
* **Half-line with fixed end value.** $u(0,t) = g$, $u(x,0) = 0$ gives
  $u = g[1 - \operatorname{erf}(x/\sqrt{4\kappa t})]$, and the total
  amount that has entered is $\int_0^\infty u\,\mathrm dx = 2g\sqrt{\kappa t/\pi}$
  (pp. 747–748).

## Appropriate data

Dirichlet or Neumann data on an open boundary (Table 20.1, p. 705). An
insulated bar with a given initial temperature is parabolic, open,
Dirichlet at $t = 0$ with Neumann $\partial_x u = 0$ at the ends
(Exercise 20.23(a), answer p. 712).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.1.2 (pp. 678–679),
  §20.5 (pp. 695–698), §21.1 (pp. 716–717), §21.4 (pp. 747–750).
