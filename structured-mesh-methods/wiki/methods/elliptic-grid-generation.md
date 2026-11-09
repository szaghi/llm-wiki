---
type: Method
title: "Elliptic grid generation"
description: "Curvilinear coordinates taken as solutions of Laplace or Poisson equations in the physical domain with Dirichlet data on all boundaries, inverted into a quasilinear elliptic system for the physical coordinates on the computational square (Winslow); extended to multiply connected regions with control functions for line spacing (Thompson–Thames–Mastin) and automatic boundary spacing and orthogonality (Steger–Sorenson)."
status: established
aliases: [Winslow generator, TTM method, Thompson–Thames–Mastin method, Poisson grid generation, inverse Laplace equations]
tags: [elliptic-generation, grid-generation, control-functions, clustering]
timestamp: 2026-11-08T20:24:00Z
---

# Elliptic grid generation

## The inverse Laplace system

[Winslow (1966)](/sources/winslow-1966.md) built meshes by treating mesh
lines as equipotentials: the curvilinear coordinates satisfy
$\nabla^2\xi=0$, $\nabla^2\eta=0$ in $\Omega$, whose averaging property makes
the mesh smooth. Interchanging dependent and independent variables (with
$J=x_\xi y_\eta-x_\eta y_\xi\ne0$) gives the quasilinear elliptic system on the
computational square

$$g_{22}\,\mathbf x_{\xi\xi}-2g_{12}\,\mathbf x_{\xi\eta}+g_{11}\,\mathbf x_{\eta\eta}=0,\qquad g_{11}=\mathbf x_\xi\cdot\mathbf x_\xi,\ g_{12}=\mathbf x_\xi\cdot\mathbf x_\eta,\ g_{22}=\mathbf x_\eta\cdot\mathbf x_\eta,$$

solved by successive over-relaxation as a sequence of linear problems with
recomputed coefficients. Winslow notes that the simpler Laplace equations in
the computational variables (each point the mean of its neighbours) work for
convex regions but crowd lines, or push them outside, near a concave
boundary — the inverted form does not.

## Multiply connected regions and spacing control

[Thompson, Thames & Mastin (1974)](/sources/thompson-1974.md) extend the
method to regions containing any number of bodies: one coordinate is
constant on each body contour, branch cuts between contours map to the sides
of the rectangular computational domain, and the boundary point
distribution is free. Spacing in the interior is controlled by
nonhomogeneous terms, $\nabla^2\xi^i=P^i$; with $P^i>0$ the coordinates
are subharmonic and lines move toward a contour. They suggest making the
control functions depend on solution gradients, the seed of
solution-adaptive coordinates. In computational variables the Poisson form
reads

$$g_{22}\,\mathbf x_{\xi\xi}-2g_{12}\,\mathbf x_{\xi\eta}+g_{11}\,\mathbf x_{\eta\eta}=-J^2\big(P\,\mathbf x_\xi+Q\,\mathbf x_\eta\big).$$

## Automatic clustering and orthogonality at a boundary

[Steger & Sorenson (1979)](/sources/steger-1979.md) remove the guesswork in
choosing $P$ and $Q$: the control functions decay exponentially away from the
inner boundary, $P=P_1(\xi)e^{-a(\eta-\eta_1)}$, $Q=Q_1(\xi)e^{-b(\eta-\eta_1)}$,
and $P_1,Q_1$ are found iteratively so that the generator, evaluated on the
boundary, honours a prescribed first spacing $\Delta s$ and a prescribed
intersection angle (orthogonality). The forcing derivatives are differenced
one-sidedly and the updates under-relaxed for stability; airfoil grids with
$\Delta s$ down to $10^{-5}$ chord, as viscous flow needs, are produced.

## Properties and limits

Elliptic generators give smooth grids and a one-to-one map for convex
computational domains, with boundary slope discontinuities smoothed inside;
they need boundary data on the whole closed boundary and an iterative
solution. Thompson, Warsi and Mastin (1982, Sections G and K) survey the
variants and the control-function choices; the variational view of the
Laplace generator as the minimizer of a smoothness functional is on
[variational grid generation](/methods/variational-grid-generation.md).

# Citations

- [Winslow (1966)](/sources/winslow-1966.md) — Appendix.
- [Thompson, Thames & Mastin (1974)](/sources/thompson-1974.md) — transformation and spacing control.
- [Steger & Sorenson (1979)](/sources/steger-1979.md) — whole note.
- [Thompson, Warsi & Mastin (1982)](/sources/thompson-1982.md) — Sections G, K.
