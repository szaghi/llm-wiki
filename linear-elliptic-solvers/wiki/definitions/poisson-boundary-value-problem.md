---
type: Definition
title: "Poisson boundary-value problem"
description: "Poisson's equation nabla^2 u = f (Laplace for f = 0, Helmholtz with + kappa^2 u) on a region bounded by one or several surfaces, possibly at infinity, with Dirichlet or Neumann data; Neumann data must satisfy the Gauss consistency condition and fix u only up to a constant, and imposing both kinds overdetermines the problem."
status: established
aliases: [Poisson equation, Laplace equation, Helmholtz equation, Dirichlet problem, Neumann problem, Neumann compatibility condition, free-space boundary condition]
tags: [poisson, elliptic, boundary-conditions]
timestamp: 2026-10-14T00:00:00Z
---

# Poisson boundary-value problem

**Equations.** Poisson's equation $\nabla^2u=f$ in a region $\Omega$ of
any dimension; Laplace's equation is $f=0$; Helmholtz's operator is
$\nabla^2+\kappa^2$ ([Riley et al. (2006)](/sources/riley-2006.md),
§21.5, eqs. 21.76, 21.80, pp. 751–754). A problem is inhomogeneous if a
multiple of a solution is not a solution; the inhomogeneity may sit in the
equation or in the boundary conditions, and a change of variable usually
moves it from one to the other (p. 752). [Arfken et al. (2013)](/sources/arfken-2013.md)
open their Green's-function chapter with the electrostatic form, which
puts $-\nabla^2$ on the left and the charge density over the vacuum
permittivity on the right, so that the registry's $f$ is minus that ratio
(eq. 10.1, p. 447), and also treat the modified Helmholtz operator
$\nabla^2-\kappa^2$ (table 10.1, p. 463). A boundary condition is
homogeneous if it survives multiplication of the solution by a constant
($u=0$, $\partial_nu=0$, or a combination $c_1u+c_2\partial_nu=0$; not
$u=c\neq0$) (footnote 1, p. 448).

**Region and boundary.** $\partial\Omega$ may have several disconnected
parts — e.g. the gap between two closed surfaces — with $\hat{\mathbf n}$
always pointing out of $\Omega$. An exterior problem is treated by taking
an outer sphere of radius tending to infinity (fig. 21.11, p. 754).

**Boundary conditions** (p. 754; classified in §20.6.2, not read):

* **Dirichlet:** $u=g_{\mathrm D}$ on $\partial\Omega$.
* **Neumann:** $\partial_nu=g_{\mathrm N}$ on $\partial\Omega$.
* Arfken et al. use the same two names for the homogeneous end conditions
  $u=0$ and $u'=0$ of a one-dimensional problem, and note that periodic
  conditions also make Sturm–Liouville boundary terms vanish (§8.2,
  p. 385).
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
condition at infinity cannot be imposed in the same form (p. 758). Arfken et
al. agree on both points: for a charge distribution in otherwise empty
space the solution is the Coulomb integral (eqs. 10.2–10.4, p. 447), and in
one and two dimensions the boundary condition of the fundamental solution
is left "arbitrary" (table 10.1, p. 463). They add that the free-space
kernel is "preliminary": conductors or other boundaries add contributions
that depend on $f$ (p. 448).

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
* [Arfken et al. (2013)](/sources/arfken-2013.md), §8.2 (p. 385), Ch. 10
  introduction (pp. 447–448), §10.2 (p. 463).
