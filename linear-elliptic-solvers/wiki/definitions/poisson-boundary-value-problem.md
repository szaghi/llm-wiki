---
type: Definition
title: "Poisson boundary-value problem"
description: "Poisson's equation nabla^2 u = f (Laplace for f = 0, Helmholtz with + kappa^2 u) on a region bounded by one or several surfaces, possibly at infinity, with Dirichlet or Neumann data; Neumann data must satisfy the Gauss consistency condition and fix u only up to a constant, and imposing both kinds overdetermines the problem."
status: established
aliases: [Poisson equation, Laplace equation, Helmholtz equation, Dirichlet problem, Neumann problem, Neumann compatibility condition, free-space boundary condition]
tags: [poisson, elliptic, boundary-conditions]
timestamp: 2026-10-13T00:00:00Z
---

# Poisson boundary-value problem

**Equations.** Poisson's equation $\nabla^2u=f$ in a region $\Omega$ of
any dimension; Laplace's equation is $f=0$; Helmholtz's operator is
$\nabla^2+\kappa^2$ ([Riley et al. (2006)](/sources/riley-2006.md),
§21.5, eqs. 21.76, 21.80, pp. 751–754). A problem is inhomogeneous if a
multiple of a solution is not a solution; the inhomogeneity may sit in the
equation or in the boundary conditions, and a change of variable usually
moves it from one to the other (p. 752).

**Region and boundary.** $\partial\Omega$ may have several disconnected
parts — e.g. the gap between two closed surfaces — with $\hat{\mathbf n}$
always pointing out of $\Omega$. An exterior problem is treated by taking
an outer sphere of radius tending to infinity (fig. 21.11, p. 754).

**Boundary conditions** (p. 754; classified in §20.6.2, not read):

* **Dirichlet:** $u=g_{\mathrm D}$ on $\partial\Omega$.
* **Neumann:** $\partial_nu=g_{\mathrm N}$ on $\partial\Omega$.
* Specifying both on the same surface "in general" overdetermines the
  problem and leaves no solution.

**Neumann consistency.** A solution exists only if
$$\oint_{\partial\Omega}g_{\mathrm N}\,\mathrm dS=\int_\Omega f\,\mathrm dV\quad\text{(eq. 21.105)},$$
by the divergence theorem (the analogue of Gauss's theorem), and Neumann
data fix $u$ only up to an additive constant — a uniqueness result proved
in §20.7, outside the scope read (p. 765).

**Free-space (isolated) problem.** $u\to0$ as $\lvert\mathbf r\rvert\to\infty$
on all of $\mathbb R^3$ is solved by convolution with the fundamental
solution of the [Green's function](/definitions/greens-function.md) page; in
two dimensions the logarithmic fundamental solution does not decay, so the
condition at infinity cannot be imposed in the same form (p. 758).

Solution routes in the source: the
[representation formula](/results/greens-representation-formula.md) with
Dirichlet or Neumann Green's functions built by the
[method of images](/methods/method-of-images.md), and, discretely, the
[five-point Laplacian](/operators/five-point-laplacian.md) with
[relaxation](/methods/laplace-relaxation.md). Separation of variables and
transform methods (§§21.1–21.4) were not read.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §21.5 (pp. 751–754),
  §21.5.3 (p. 758), §21.5.4 (p. 765).
