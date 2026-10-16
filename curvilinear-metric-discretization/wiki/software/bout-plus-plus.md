---
type: Software
title: "BOUT++"
description: "Finite-difference framework for plasma fluid equations in curvilinear geometry that stores fields in field-aligned coordinates and takes derivatives in the quasi-ballooning (shifted-metric) system; Seto et al. add a solver that inverts the perpendicular operator per toroidal mode in orthogonal flux coordinates for n = 0 and low n."
status: established
aliases: [BOUT, BOUT++ framework]
tags: [software, field-aligned-coordinates, shifted-metric, finite-difference, metric]
timestamp: 2026-10-16T00:00:00Z
---

# BOUT++

BOUT++ is a framework for three-dimensional plasma fluid equations solved as
initial-value problems by finite differences in curvilinear coordinates
(Dudson et al. 2009, cited by all three plasma sources of this bundle). This
page records what [Seto et al. (2023)](/sources/seto-2023.md), who extend
version 3.1, state about its coordinates and operators.

## Coordinates

* Three coordinate systems are used together (§2, pp. 2–4): fields are
  stored and advanced in time in [field-aligned coordinates](/definitions/field-aligned-coordinates.md);
  spatial derivatives, including those of the standard field solver, are
  taken in the quasi-ballooning system of the [shifted metric](/methods/shifted-metric.md);
  the new low-$n$ solver works in orthogonal
  [flux coordinates](/definitions/magnetic-flux-coordinates.md). Time
  integration is BDF through CVODE (p. 2).
* The transform between field-aligned and flux coordinates is an FFT in the
  toroidal direction with a phase factor $e^{\mp\mathrm i n_\varphi\chi}$, on
  shared $(\Psi,\vartheta)$ and $(\xi^1,\xi^2)$ grid points (eqs. (10)–(11),
  p. 3); the 2D solver therefore needs as many poloidal points as parallel
  points (p. 5).
* [Jiang et al. (2024)](/sources/jiang-2024.md) (p. 1) and
  [Liu et al. (2024)](/sources/liu-2024.md) (p. 3, for the twist-shift
  condition) cite BOUT++ as a field-aligned code.

## Operators and their discretization

* The vorticity–potential relation is a Helmholtz-type equation built from
  $\nabla_\perp^2$ and a first-order $\nabla_\perp$ term with axisymmetric
  coefficients; because the coefficients do not couple toroidal modes, it is
  solved for each toroidal mode separately (eq. (15), p. 4).
* **Standard (flute-ordered) solver:** dropping $\partial_2$ terms leaves a
  radial operator per mode, discretized with second-order central
  differences and solved by the Thomas algorithm (eq. (17), p. 4). Many
  BOUT++ edge simulations therefore set the $n_\varphi=0$ perturbations to
  zero and use toroidal wedges with $N\sim5$ "to avoid numerical
  instabilities from low-$n$ modes especially in diverted geometries" (p. 4).
* **Previous $n_\varphi=0$ solver:** a 2D problem in $(\xi^1,\xi^2)$, which
  coincides with the flux plane for axisymmetric fields; second-order,
  five-point stencil, PETSc GMRES with SOR preconditioning (eq. (18), p. 5).
* **Seto et al.'s solver:** the full operator for each mode
  $0\le n_\varphi\le n_{2D\max}$ in the orthogonal flux plane $(\Psi,\vartheta)$,
  written in expanded form with metric coefficients (eq. (19); App. A.2,
  pp. 15–16), discretized with fourth-order central differences on a 9-point
  star stencil and solved by PETSc GMRES with a Hypre AMG preconditioner,
  "more effective" than SOR (p. 5); higher modes keep the flute-ordered
  solver, and the two results are summed in Fourier space (eq. (20), p. 5).
  For consistency the perpendicular Laplacian and the gradient term in the
  evolution equations are evaluated in the same split way (p. 5). Accuracy
  of the flute ordering: see
  [field-aligned coordinates](/definitions/field-aligned-coordinates.md).

# Citations

* [Seto et al. (2023)](/sources/seto-2023.md), §1, p. 2; §2, pp. 2–4; §3, pp. 4–5; App. A, pp. 14–16.
* [Jiang et al. (2024)](/sources/jiang-2024.md), §I, p. 1.
* [Liu et al. (2024)](/sources/liu-2024.md), §II B, p. 3.
