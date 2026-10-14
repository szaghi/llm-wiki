---
type: Definition
title: "Fundamental solution"
description: "A solution of the operator equation with a unit point source and no boundary conditions beyond behaviour at infinity: -1/(4 pi |x-x'|) for the Laplacian in three dimensions, (1/2 pi) ln|x-x'| plus a constant in two, and the Gaussian heat kernel for the one-dimensional diffusion equation; Green's functions are built from it."
status: established
aliases: [free-space Green's function, heat kernel, point-source solution]
tags: [greens-function, laplace, diffusion]
timestamp: 2026-10-14T00:00:00Z
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

[Arfken et al. (2013)](/sources/arfken-2013.md) reach the same kernel
without a transform. Differentiating the error-function solution in $x$
gives the Gaussian solution, and superposing its translates with weight
$u_0$ gives the initial-value solution with the prefactor
$(4\pi\kappa t)^{-1/2}$, i.e. $K$ (§9.7, eqs. 9.109–9.114, pp. 440–441;
see [diffusion equation](/definitions/diffusion-equation.md)). They
describe the result in Riley's terms: the initial distribution "spreads
out over time and is damped by the Gaussian weight function" (p. 441).

**Three dimensions** (Arfken et al., Example 9.7.3, pp. 442–443). Heat
released at the origin at $t = 0$ in an infinite medium gives a
temperature proportional to $t^{-3/2}\exp(-r^2/(4\kappa t))$, its constant
fixed by conservation of the heat content (eq. 9.120). Combining their
constants, $u = \left(\int u\,\mathrm dV\right)(4\pi\kappa t)^{-3/2}\exp(-r^2/(4\kappa t))$,
the three-dimensional heat kernel (the normalised form is the compiler's
rewriting). For the planar radially symmetric case, Arfken et al.'s eq.
9.126 is misprinted; Riley's $t^{-1}$ form above is the solution (see the
compiler's check on the [diffusion equation](/definitions/diffusion-equation.md)
page).

The fundamental solutions of the Laplacian are not in the chapters of
Arfken et al. read here (their Green's-function chapter, Ch. 10, is not
part of this ingestion).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.5 (p. 698), §21.4
  (pp. 749–750), §21.5.3 (pp. 756–758).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §9.7 (pp. 440–443).
