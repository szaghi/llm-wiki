---
type: Definition
title: "Diffusion equation"
description: "The model parabolic equation, kappa times the laplacian of u equals u_t, derived from a gradient flux law and the divergence theorem over an arbitrary volume; it admits no travelling-wave general solution, but has the error-function similarity solution in x over the square root of t, decaying separated modes, and the Gaussian heat-kernel solution of the initial-value problem."
status: established
aliases: [heat equation, heat conduction equation]
tags: [model-equation, parabolic, similarity-solution]
timestamp: 2026-10-14T00:00:00Z
---

# Diffusion equation

$$\kappa\,\nabla^2 u = \partial_t u$$
describes the temperature in a region without heat sources, or the
concentration of a diffusing substance. $\kappa$ is the diffusivity
([Riley et al. (2006)](/sources/riley-2006.md), eq. 20.2, p. 678). It is
second order in space and first order in time, and
[parabolic](/definitions/second-order-pde-classification.md).
[Arfken et al. (2013)](/sources/arfken-2013.md) write it
$\partial_t u = \kappa\nabla^2 u$ with diffusivity $\kappa$ (their $a^2$),
and take it as the canonical parabolic form (§9.3, eq. 9.19, p. 410;
§9.7, eq. 9.98, p. 437). An anisotropic medium with constant diffusivities
along its principal axes reduces to the isotropic equation by rescaling each
coordinate (eqs. 9.96–9.97, p. 437).

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
  is uniform at $t = 0$ and zero at $x = 0$ (p. 697). Arfken et al. reach
  the same solution from $u = u(x/\sqrt t)$, "suggested by dimensional
  considerations and experimental data": the ODE
  $2\kappa u'' + (x/\sqrt t)\,u' = 0$ in that variable gives
  $u = \operatorname{erf}(\zeta)$ for initial data $-1$ for $x < 0$ and
  $+1$ for $x > 0$ (§9.7, eqs. 9.105–9.108, pp. 439–440).
* **Separated solutions.** $u = (C_1\cos kx + C_2\sin kx)\,e^{-\kappa k^2 t}$
  with real $k$ decays to zero as $t \to \infty$. The sign of the
  separation constant is chosen for that decay (eqs. 21.9–21.12,
  pp. 716–717; [separation of variables](/methods/separation-of-variables.md)).
  Arfken et al. agree and add the zero-constant solution $C_1x + C_2$
  (eqs. 9.99–9.101, pp. 437–438). A finite rod takes a discrete set of $k$;
  an infinite rod an integral over $k$ (eq. 9.102). For a rod held at
  $u = 0$ at $x = \pm1$ with $u_0 = 1$ inside, the cosine series of the
  solution converges absolutely for $t > 0$ and only conditionally at
  $t = 0$, because of the discontinuity at the ends (Example 9.7.1,
  eq. 9.103, pp. 438–439).
* **Initial-value problem on the line.**
  $u = \int K(x - x', t)\,u_0(x')\,\mathrm dx'$ with the Gaussian heat
  kernel $K$ (eq. 21.74, p. 750; [fundamental solution](/definitions/fundamental-solution.md),
  [integral transform methods](/methods/integral-transform-methods.md)).
  Arfken et al. obtain the same integral without a transform (§9.7,
  pp. 440–441). With constant coefficients, $\partial_x$ and $\partial_t$
  of a solution are solutions, which turns the error-function solution
  into the Gaussian $(\pi\kappa t)^{-1/2}\exp(-x^2/(4\kappa t))$ and its
  $x$-derivative (eqs. 9.109–9.110); the method "no longer works if any
  coefficient of the PDE depends on $t$ or $x$ explicitly" (p. 440).
  Translating the Gaussian and superposing with weight $u_0(x')$ gives
  $u = \pi^{-1/2}\int u_0(x - 2\sqrt{\kappa t}\,q)\,e^{-q^2}\,\mathrm dq$,
  Riley's eq. 21.74 after a change of variable (eqs. 9.111–9.114). For
  $u_0 = 1$ on $|x| < 1$ and $0$ elsewhere,
  $u = \tfrac12[\operatorname{erf}((x+1)/(2\sqrt{\kappa t})) - \operatorname{erf}((x-1)/(2\sqrt{\kappa t}))]$
  (Example 9.7.2, eq. 9.115, pp. 441–442).
* **Spherical symmetry.** For $u(r,t)$, the substitution $u = v/r$ turns
  $\partial_tu = \kappa(\partial_r^2u + 2r^{-1}\partial_ru)$ into the
  one-dimensional equation $\partial_tv = \kappa\,\partial_r^2v$ (Arfken et
  al., eqs. 9.116–9.118, p. 442). A quantity of heat released at the origin
  at $t = 0$ gives a temperature proportional to
  $t^{-3/2}\exp(-r^2/(4\kappa t))$, which at fixed $r$ rises from zero to a
  maximum at $t = r^2/(6\kappa)$ and decays: the maximum arrives later
  farther out (Example 9.7.3, eqs. 9.119–9.121, pp. 442–443; see
  [fundamental solution](/definitions/fundamental-solution.md)).
* **Half-line with fixed end value.** $u(0,t) = g$, $u(x,0) = 0$ gives
  $u = g[1 - \operatorname{erf}(x/\sqrt{4\kappa t})]$, and the total
  amount that has entered is $\int_0^\infty u\,\mathrm dx = 2g\sqrt{\kappa t/\pi}$
  (pp. 747–748).

## A misprinted solution in Arfken et al. (compiler's check)

For cylindrical symmetry, Arfken et al. seek $u = v(r/\sqrt t)$ for the
planar equation $\partial_tu = \kappa(\partial_r^2u + r^{-1}\partial_ru)$
and derive a correct first-order ODE for $v'$ (eqs. 9.122–9.125, p. 443).
Their eq. 9.126 then gives $v = C\,(\sqrt t/r)\exp(-r^2/(4\kappa t))$. That
expression is the integrated $v'$, not $v$. Substituted into the PDE it
leaves the residual
$(r^2/2 - \kappa t)\,e^{-r^2/(4\kappa t)}/(r^3\sqrt t) \ne 0$, so it is not
a solution (symbolic check by the compiler). The radially symmetric planar
solution is Riley et al.'s
$t^{-1}\exp(-r^2/(4\kappa t))$ (eq. 20.37, p. 698), which does satisfy the
equation. Eq. 9.123 also prints $\partial_r^2u = v'/t$ for $v''/t$, though
eq. 9.124 is correct. This is a defect of one source, found by derivation;
the two books do not make competing claims, so no `Contradictions` entry
is opened.

## Appropriate data

Dirichlet or Neumann data on an open boundary (Table 20.1, p. 705). An
insulated bar with a given initial temperature is parabolic, open,
Dirichlet at $t = 0$ with Neumann $\partial_x u = 0$ at the ends
(Exercise 20.23(a), answer p. 712).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.1.2 (pp. 678–679),
  §20.5 (pp. 695–698), §21.1 (pp. 716–717), §21.4 (pp. 747–750).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §9.3 (pp. 410–411),
  §9.7 (pp. 437–444).
