---
type: Definition
title: "Dirichlet, Neumann and Cauchy boundary conditions"
description: "Dirichlet data prescribe the solution, Neumann data its normal derivative, Cauchy data both, on an open or a closed boundary (which may lie partly at infinity); a condition is homogeneous when it survives scaling of the solution, and prescribing both Dirichlet and Neumann data for Poisson's equation overdetermines it."
status: established
aliases: [Dirichlet condition, Neumann condition, Cauchy condition, Cauchy data, open boundary, closed boundary]
tags: [boundary-conditions, well-posedness]
timestamp: 2026-10-13T00:00:00Z
---

# Dirichlet, Neumann and Cauchy boundary conditions

For a second-order PDE the data are specified on a boundary $\Gamma$ (a
curve in two variables, a surface in more) bordering or enclosing the
region of solution ([Riley et al. (2006)](/sources/riley-2006.md), §20.6.2,
p. 702):

* **Dirichlet:** $u = g$ is specified at each point of the boundary.
* **Neumann:** $\partial_n u = \nabla u\cdot\hat{\mathbf n} = h$ is
  specified at each point of the boundary.
* **Cauchy:** both $u = g$ and $\partial_n u = h$ are specified at each
  point of the boundary.

For a problem in $(x,t)$ with the data on $t = 0$, Cauchy data are the
initial displacement and velocity, $u(x,0) = u_0(x)$ and
$\partial_t u(x,0) = u_1(x)$ (§20.4, p. 694; see
[d'Alembert's formula](/results/dalembert-formula.md)).

**Open and closed boundaries.** Whether a type of condition is appropriate
depends on the equation type and on whether the region is bounded by a
closed or an open curve (or surface). Part of a closed boundary may lie at
infinity if conditions are imposed on $u$ or $\partial_n u$ there, most
often $u \to 0$ or $\partial_n u \to 0$ (p. 705). The pairing of equation
type and data is [boundary data by equation type](/results/boundary-data-by-equation-type.md).

**Homogeneous conditions.** A boundary condition is homogeneous if,
whenever $u$ satisfies it, so does $C_1u$ for every constant
$C_1$, typically $u = 0$ or $\partial_n u = 0$ (§20.3.2, p. 685;
§21.5, p. 752; see [homogeneous linear problems](/definitions/homogeneous-linear-problem.md)).

**Overdetermination.** For Poisson's equation, specifying both Dirichlet
and Neumann data on the same closed boundary "overdetermines the problem
and leads to there being no solution" in general (§21.5.2, p. 754).
Neumann data must moreover satisfy a compatibility condition with the
source (eq. 21.105; see [Green's functions for PDEs](/methods/greens-functions-for-pdes.md)).
For hyperbolic equations, Cauchy data on a curve that meets a
characteristic twice can overdetermine the problem (p. 705; see
[characteristic curves](/definitions/characteristic-curve.md)).

**ODE analogue.** An $n$th-order ODE needs $n$ conditions to fix its $n$
constants: the values at $n$ points, or $y, y', \dots, y^{(n-1)}$ at one
point (one-point, or initial, conditions), or combinations in between.
Fewer leave parameters undetermined, more usually admit no solution
(§14.1, p. 470; §15.2.5, p. 515).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §14.1 (p. 470), §20.3.2
  (p. 685), §20.6.2 (pp. 702–705), §21.5.2 (p. 754).
