---
type: Result
title: "Uniqueness theorem for Poisson's equation"
description: "A real C2 solution of the laplacian of u equals psi in a region, with either u or its normal derivative prescribed on the whole boundary (possibly including a sphere at infinity), is unique, up to an additive constant in the Neumann case; the proof applies Green's first theorem to the difference of two solutions (an energy argument), which also gives uniqueness for the laplacian of u minus k^2 u = 0."
status: established
aliases: [uniqueness theorem, energy method]
tags: [uniqueness, elliptic, well-posedness]
timestamp: 2026-10-13T00:00:00Z
---

# Uniqueness theorem for Poisson's equation

**Statement.** If $u$ is real, its first and second partial derivatives
are continuous in $\Omega$ and on $\partial\Omega$, $\nabla^2u = \psi$ in
$\Omega$, and either $u = g$ or $\partial_nu = h$ on $\partial\Omega$,
then $u$ is unique, at least to within an additive constant
([Riley et al. (2006)](/sources/riley-2006.md), §20.7, p. 706). The
boundary may include a hypothetical sphere of indefinitely large radius on
which $u$ or $\partial_nu$ is prescribed to be arbitrarily small (p. 706).

**Proof** (p. 706). The difference $v$ of two solutions satisfies
$\nabla^2v = 0$ in $\Omega$, and $v = 0$ or $\partial_nv = 0$ on
$\partial\Omega$. Green's first theorem with both functions equal to $v$
gives
$$\int_\Omega\left[v\nabla^2v + \lvert\nabla v\rvert^2\right]\mathrm dV = \oint_{\partial\Omega}v\,\partial_nv\,\mathrm dS.$$
Both the right-hand side and the first term on the left vanish, so
$\int_\Omega|\nabla v|^2\,\mathrm dV = 0$ and $v$ is constant. Dirichlet
data on (some part of) $\partial\Omega$ make the constant zero. Under
Neumann data the solutions may differ by an arbitrary constant. Green's
first theorem is from Ch. 11 (not read).

**Uses.** Any solution that fits the data, found by whatever means, is the
solution. This justifies the method of images ([Green's functions for
PDEs](/methods/greens-functions-for-pdes.md)) and solution by expansion
([separation of variables](/methods/separation-of-variables.md), §21.3.3)
(pp. 706, 741–744). "Often the same general method" proves uniqueness for
other equations and boundary conditions (p. 707). Exercise 20.25 (p. 711)
applies it to $\nabla^2u - k^2u = 0$ (the book's Klein–Gordon form). The
extra term $k^2\int|v|^2\,\mathrm dV$ forces $v = 0$ under Dirichlet or
Neumann data alike (hint, p. 712).

**Scope.** Elliptic, linear, classical ($C^2$) solutions. The chapters read
contain no uniqueness theorem for the wave or diffusion equation. For those
only the [boundary-data table](/results/boundary-data-by-equation-type.md)
is asserted.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.7 (pp. 705–707),
  Exercise 20.25 (pp. 711–712), §21.3.3 (pp. 741–744).
