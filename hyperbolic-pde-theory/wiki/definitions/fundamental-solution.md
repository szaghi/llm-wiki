---
type: Definition
title: "Fundamental solution"
description: "A solution of the operator equation with a unit point source and no boundary conditions beyond behaviour at infinity: -1/(4 pi |x-x'|) for the Laplacian in three dimensions, (1/2 pi) ln|x-x'| plus a constant in two, and the Gaussian heat kernel for the one-dimensional diffusion equation; Green's functions are built from it."
status: established
aliases: [free-space Green's function, heat kernel, point-source solution]
tags: [greens-function, laplace, diffusion]
timestamp: 2026-10-13T00:00:00Z
---

# Fundamental solution

The **fundamental solution** $E(\mathbf x, \mathbf x')$ of $\mathcal L$
satisfies $\mathcal L E = \delta(\mathbf x - \mathbf x')$ and has the
singularity required at $\mathbf x = \mathbf x'$, without necessarily
obeying the boundary conditions of a given problem
([Riley et al. (2006)](/sources/riley-2006.md), §21.5.3, pp. 756–757). A
[Green's function](/methods/greens-functions-for-pdes.md) is a fundamental
solution plus a solution of the homogeneous equation chosen to satisfy the
boundary conditions.

## Laplacian

**Three dimensions.** Integrating $\nabla^2 E_3 = \delta$ over a sphere
centred on $\mathbf x'$, using the divergence theorem and spherical
symmetry, gives $4\pi r^2\,\mathrm dE_3/\mathrm dr = 1$. With
$E_3 \to 0$ as $|\mathbf x| \to \infty$,
$$E_3(\mathbf x - \mathbf x') = -\frac{1}{4\pi\lvert\mathbf x - \mathbf x'\rvert}$$
(eqs. 21.87–21.90, p. 757). It is also the full Green's function for the
condition $u \to 0$ at infinity, which turns the solution of Poisson's
equation into a volume integral over the source (eq. 21.91, p. 758; the
electrostatic potential of a charge distribution).

**Two dimensions.**
$$E_2(\mathbf x - \mathbf x') = \frac{1}{2\pi}\ln\lvert\mathbf x - \mathbf x'\rvert + \text{const}$$
(eq. 21.93, p. 758). It cannot be made to vanish at infinity, and the
constant need not vanish.

## Diffusion equation

For $\kappa\,\partial_x^2 u = \partial_t u$ on the whole line, the Fourier
transform gives $u(x,t) = \int K(x - x', t)\,u_0(x')\,\mathrm dx'$ with
$$K(x,t) = \frac{1}{\sqrt{4\pi\kappa t}}\exp\left(-\frac{x^2}{4\kappa t}\right),$$
which the book calls the Green's function of the problem (pp. 749–750; see
[integral transform methods](/methods/integral-transform-methods.md)). A
point source $u_0 = \delta(x - x')$ evolves into $K(x - x', t)$. Its width
grows as $\sqrt t$, which is characteristic of diffusion, and the area
under it is constant (p. 750, Fig. 21.10). The radially symmetric heat
pulse in a thin sheet, (amplitude)$\,t^{-1}\exp(-r^2/(4\kappa t))$, is the
two-dimensional analogue (eq. 20.37, p. 698).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.5 (p. 698), §21.4
  (pp. 749–750), §21.5.3 (pp. 756–758).
