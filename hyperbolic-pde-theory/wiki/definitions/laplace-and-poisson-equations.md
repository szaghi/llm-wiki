---
type: Definition
title: "Laplace and Poisson equations"
description: "The model elliptic equations, laplacian of u equals zero or a given source: steady states of diffusion and potentials of gravity, electrostatics and irrotational flow; closed-boundary Dirichlet or Neumann data fix the solution (up to a constant for Neumann), the two-dimensional general solution is F(x+iy)+G(x-iy), and separated, Green's-function and image solutions are available."
status: established
aliases: [Laplace equation, Poisson equation, potential equation]
tags: [model-equation, elliptic, potential-theory]
timestamp: 2026-10-13T00:00:00Z
---

# Laplace and Poisson equations

**Laplace's equation** $\nabla^2 u = 0$ is the steady state of the
[diffusion equation](/definitions/diffusion-equation.md). It also describes
the gravitational potential in empty space, the electrostatic potential in
a charge-free region, and the velocity potential of incompressible flow
without sources, sinks or vortices
([Riley et al. (2006)](/sources/riley-2006.md), eq. 20.5, p. 679).
**Poisson's equation** $\nabla^2 u = \psi(\mathbf x)$ covers the same
situations with sources present; $\psi$ is the source density, usually
carrying physical constants (eq. 20.6, p. 679). Both are
[elliptic](/definitions/second-order-pde-classification.md).

## Results compiled in this bundle

* **Appropriate data:** Dirichlet or Neumann data on a closed boundary,
  possibly at infinity (Table 20.1 and p. 705; [boundary data by equation
  type](/results/boundary-data-by-equation-type.md)).
* **Uniqueness:** Dirichlet data fix the solution, Neumann data fix it up
  to an additive constant ([uniqueness theorem](/results/uniqueness-theorem-poisson.md)).
* **Two-dimensional general solution:** $u = F(x + iy) + G(x - iy)$
  (p. 690). A particular integral is added for Poisson's equation, e.g.
  $x^3 + y^3$ for $\psi = 6(x+y)$ (p. 692; [general solution of
  constant-coefficient second-order equations](/methods/constant-coefficient-second-order-general-solution.md)).
* **Separated solutions** in Cartesian, plane polar, cylindrical and
  spherical coordinates, with Bessel and Legendre functions in the curved
  cases ([separation of variables](/methods/separation-of-variables.md)).
* **Point-source solutions** $E_3$, $E_2$ ([fundamental solution](/definitions/fundamental-solution.md)),
  and Dirichlet and Neumann Green's functions by the method of images,
  including the Poisson integral for the disc ([Green's functions for
  PDEs](/methods/greens-functions-for-pdes.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.1.3–20.1.4
  (p. 679), §20.3.3 (pp. 690–692), §20.7 (pp. 705–707), §21.3 (pp. 725–746),
  §21.5 (pp. 751–767).
