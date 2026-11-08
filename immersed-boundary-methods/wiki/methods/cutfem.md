---
type: Method
title: "CutFEM (cut finite element method)"
description: "Unfitted finite element framework in which the geometry is represented on a background mesh (typically by a level set), boundary and interface conditions are imposed weakly by Nitsche's method, and ghost-penalty stabilization on faces of cut elements makes accuracy and conditioning independent of how the boundary cuts the mesh."
status: established
aliases: [cut finite element method, unfitted Nitsche method, Nitsche fictitious domain method]
tags: [cutfem, finite-element, nitsche, ghost-penalty, unfitted, level-set, small-cell]
timestamp: 2026-11-08T18:10:00Z
---

# CutFEM (cut finite element method)

[Burman et al. (2015)](/sources/burman-2015.md) describe CutFEM as an
attempt to make the discretization "as independent as possible of the
geometric description" while keeping the accuracy and robustness of a
standard finite element method. The domain, or an interface, is represented
on a background mesh, for instance by a level set $\phi$; the same mesh carries
the approximation; boundary and interface conditions enter the variational
form; and stabilization makes both the error and the condition number
independent of the mesh–boundary intersection and of the physical
parameters (§1).

## Ingredients

- **Nitsche's method** imposes Dirichlet and interface conditions weakly,
  consistently and symmetrically, with a penalty term scaled by $h^{-1}$ (§2).
- **Interface problems** (after Hansbo and Hansbo): each element cut by
  $\Gamma$ carries two sets of basis functions, restrictions of the standard
  ones to the two sides — "two new separate meshes with doubling" of the cut
  elements — so the solution may jump inside an element. Averages on $\Gamma$ use
  weights $\kappa_i=|K_i|/|K|$ (the volume fractions of the cut element), which
  are cut-dependent and not robust for large coefficient contrast; weights that
  include the coefficients restore robustness to contrast (§2.1, §3).
- **Ghost penalty.** In a fictitious-domain (boundary) problem a cut element
  can intersect $\Omega$ arbitrarily little, the inverse inequality behind
  Nitsche's method fails, and the system can become arbitrarily ill
  conditioned — the finite-element form of the
  [small-cell problem](/definitions/small-cell-problem.md). The ghost penalty
  $j(u,v)=\sum_{F}\gamma\,h\,(\,[\partial_{n_F}u],[\partial_{n_F}v]\,)_F$ over the faces
  $F$ of cut elements penalizes gradient jumps and "extends the coercivity from
  the physical domain to the mesh domain"; coercivity, optimal error estimates
  and a condition number scaling like that of a fitted mesh then hold with
  constants independent of the cut (§2.2, §3).
- **Geometry and quadrature**: the level set is reconstructed piecewise
  linearly and integrals over cut elements use a sub-triangulation (§4); the
  open-source libCutFEM builds on FEniCS/DOLFIN (§5).

## Problems covered

Poisson interface problems, including the perfect-conductor limit of infinite
diffusion in one subdomain, vanishing diffusion, heat sources, spring-type
(compliant) interfaces, transport along a crack, PDEs on embedded surfaces
(Laplace–Beltrami, with a ghost penalty scaled for codimension one) and coupled
bulk–surface problems, and the Stokes equations in a fictitious domain with
ghost penalties for velocity and pressure; illustrated on "popcorn" and
Olympic-rings geometries (§2–§6).

## Relation to other methods

CutFEM is a finite-element [immersed boundary method](/definitions/immersed-boundary-method.md)
with a sharp representation of $\Gamma$ (the integrals are taken over the exact
cut geometry up to the level-set reconstruction). The weights $|K_i|/|K|$ and
the small-intersection problem are the finite-element counterparts of the
volume fraction $\kappa$ and the small cells of the
[cut-cell method](/methods/cut-cell-method.md); the ghost penalty plays the
role that [redistribution](/methods/redistribution.md) and cell merging play
there.

## Criticism

[Main & Scovazzi (2018)](/sources/main-2018.md), §1, list the costs that
motivate the [shifted boundary method](/methods/shifted-boundary-method.md):
cut-element geometry and quadrature take a non-negligible share of run time,
and the ghost penalty, while it cures small cut elements, may be delicate in
nonlinear problems, affect conditioning and enlarge the stencil of low-order
elements.

# Citations

- [Burman et al. (2015)](/sources/burman-2015.md) — §1–§6.
- [Main & Scovazzi (2018)](/sources/main-2018.md) — §1.
