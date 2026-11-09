---
type: Method
title: "Target-matrix optimization (TMOP)"
description: "Mesh optimization by node movement that minimizes an integral of a quality metric of T = AW⁻¹, the Jacobian from target to physical element, with targets defined at every quadrature point of high-order elements; shape, size, alignment and combined metrics, barrier categories, Newton solution with safeguards, space-dependent limiting, simulation-driven targets and ALE triggers, and hr-adaptivity with nonconforming refinement."
status: established
aliases: [TMOP, target-matrix optimization paradigm, r-adaptivity, hr-adaptivity, high-order mesh optimization]
tags: [mesh-optimization, mesh-quality, target-matrix, high-order-mesh, adaptation]
timestamp: 2026-11-08T20:46:00Z
---

# Target-matrix optimization (TMOP)

TMOP builds on the algebraic [mesh quality metrics](/definitions/mesh-quality-metric.md)
of Knupp: a metric $\mu(\mathsf T)$ measures how the physical element differs
from a target element through $\mathsf T=\mathsf A\mathsf W^{-1}$
([notation](/notation.md)). The mesh topology is kept and the node positions
are optimized.

## High-order elements

[Dobrev et al. (2019)](/sources/dobrev-2019.md) extend TMOP to high-order
(isoparametric) meshes, whose quality varies inside an element: a target
Jacobian $\mathsf W$ with $\det\mathsf W>0$ is given at every quadrature point.
The objective is the variational form

$$F(\mathbf x)=\sum_E\int_{E_t}\mu(\mathsf T)\,d\mathbf x_t=\sum_E\sum_q w_q\det\mathsf W(\mathbf x_q)\,\mu\big(\mathsf T(\mathbf x_q)\big),$$

integrated over the target elements; minimizers exist for polyconvex metrics
with growth conditions, as in hyperelasticity.

**Metrics.** From the factorization of $\mathsf A$ into volume, orientation,
skew and aspect ratio: shape metrics, minimal when $\mathsf A$ is a scaled
rotation of $\mathsf W$, e.g. $\mu_2=|\mathsf T|^2/(2\det\mathsf T)-1$ in 2-D;
size metrics, minimal when $\det\mathsf A=\det\mathsf W$, e.g.
$\mu_{77}=\tfrac12(\det\mathsf T-1/\det\mathsf T)^2$; alignment metrics; and
combinations — shape+size, e.g. $\mu_7=|\mathsf T-\mathsf T^{-\mathsf T}|^2$,
minimal for a rotation of $\mathsf W$, and shape+size+alignment,
$\mu_{14}=|\mathsf T-\mathsf I|^2$, minimal only for $\mathsf T=\mathsf I$.
Barrier metrics are defined only for $\det\mathsf T>0$ and keep the mesh from
inverting.

**Solution.** Newton's method on $\partial F/\partial\mathbf x=0$ with a line
search that rejects steps creating $\det\mathsf T\le0$ or raising the objective
or the residual by more than 20 %. Too few quadrature points per direction
under-sample the quality of high-order maps and can invert elements (five
points fail and six succeed for a fourth-order mesh). Boundary nodes may
relax tangentially.

## Simulation-driven targets in ALE hydrodynamics

[Dobrev et al. (2020)](/sources/dobrev-2020.md) use TMOP as the remesh step
of high-order arbitrary Lagrangian–Eulerian shock hydrodynamics. Targets
adapt to discrete simulation fields (shock positions, materials, error
indicators), evaluated on intermediate meshes during the Newton iteration by
advection-based transfer. Several metrics are combined with each integral
normalized by its initial value, and a space-dependent limiting term keeps
nodes near their Lagrangian positions where the Lagrangian mesh already
resolves features and remap error should be small. TMOP metrics also define
adaptive ALE triggers: remeshing happens when quality falls past a
threshold.

## hr-adaptivity

A fixed topology cannot meet every size and aspect-ratio target.
[Dobrev et al. (2022)](/sources/dobrev-2022.md) add nonconforming
refinement driven by TMOP quality estimators: anisotropic refinement where
the aspect-ratio target is missed, isotropic where the size target is
missed, with derefinement of siblings, in an r–h loop. On a problem with an
exact solution, hr-adaptivity reaches a given accuracy with markedly fewer
degrees of freedom than r- or h-adaptivity alone and meets geometric
targets that r-adaptivity alone cannot.

TMOP complements the moving-barrier untangling of
[high-order mesh curving](/methods/high-order-mesh-curving.md) and the
equidistribution-based [moving mesh PDEs](/methods/moving-mesh-pde.md).

# Citations

- [Knupp (2001)](/sources/knupp-2001.md) — algebraic metrics and targets.
- [Dobrev et al. (2019)](/sources/dobrev-2019.md) — §2–§4, §6.
- [Dobrev et al. (2020)](/sources/dobrev-2020.md) — §3–§4.
- [Dobrev et al. (2022)](/sources/dobrev-2022.md) — method, conclusions.
