---
type: Source
title: "Taira & Colonius (2007) — The immersed boundary method: a projection approach"
description: "Treats immersed-boundary forces as Lagrange multipliers of the no-slip constraint alongside the pressure, so the discretized system is a KKT system solved by a block-LU fractional step whose single projection removes divergence and slip together; no gains, CFL up to about one, second order in time and better than first order in space."
resource: "doi:10.1016/j.jcp.2007.03.005"
source_kind: paper
authors: [Taira K., Colonius T.]
year: 2007
venue: "J. Comput. Phys. 225(2):2118-2137"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2007_Crossref_Journal_of_Computational_Physics_Taira_The_immersed_boundary_method_A_projection_approach.pdf"
tags: [projection, lagrange-multiplier, delta-function, incompressible, immersed-boundary]
timestamp: 2026-11-08T18:08:00Z
---

# Summary

Taira and Colonius regard the boundary forces of the immersed boundary
method as Lagrange multipliers for the no-slip constraint, in the same way
the pressure enforces incompressibility, and solve the combined system with
Perot's algebraic fractional step — the
[immersed boundary projection method](/methods/immersed-boundary-projection-method.md).
Regularization and interpolation operators built from a 3-point
[regularized delta function](/operators/regularized-delta-function.md) are
made transposes of each other ([spreading and interpolation](/operators/spreading-and-interpolation.md)),
so the modified Poisson system is symmetric positive-definite. No
constitutive law or gain is needed; no-slip and continuity hold exactly at
the new time level.

# Version read

Version of record, J. Comput. Phys. 225, 2118–2137 (2007), 20 pages. §§1–4
read in full; §5 for convergence rates and the cylinder comparisons.
Page-1 title and authors match Crossref.

# Key claims

1. For rigid bodies the gains of spring and feedback forcing are ad hoc and large gains make the equations stiff (§1). **Stated**
2. The discretized Navier–Stokes equations with no-slip form a Karush–Kuhn–Tucker system in which pressure and force are Lagrange multipliers; grouping them yields the form of the plain fractional-step system (§3). **Derived**
3. The block-LU fractional step with an $N$-th order approximation $B^N$ of $A^{-1}$ has a splitting error that cannot be absorbed by the multipliers; $N=3$ is recommended (§3, §5). **Derived**/**Shown**
4. With $E=H^{\mathsf T}$ (after scaling the force) the Poisson-like system is symmetric positive-definite and solved by conjugate gradients (§3). **Derived**
5. Lagrangian points should be spaced about one grid width apart (§3). **Stated**
6. Spring forcing corresponds to a $(3,3)$ block in their system; large spring constants force CFL numbers of $O(10^{-3})$–$O(10^{-1})$, whereas the projection method runs at CFL up to 1 (§4.1, §5). **Stated**/**Shown**
7. Direct forcing imposes no-slip on the intermediate velocity only (§4.2). **Stated**
8. The distributed Lagrange multiplier method applies separate projections for divergence and slip; here one projection removes both (§4.4). **Stated**
9. Second order in time; in space $L^\infty$ first order and $L^2$ second order (1-D Stokes) or about 1.5 (2-D concentric cylinders) (§5). **Shown**
10. Cylinder at $Re=20$, $40$ (wake length, separation angle, drag) and $200$ (lift, drag, Strouhal number) agrees with the literature; an impulsively started cylinder demonstrates moving bodies (§5). **Shown**

# Notation map

| Taira & Colonius (2007) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$ (velocity flux), $u$ | $\mathbf u$ (stored as face fluxes) | registry $\mathbf q$ is conserved variables |
| $\phi$ (pressure) | $\mathbf p$ | |
| $\tilde f$, $f$ | $\tilde{\mathbf f}$, $\mathbf f$ | transformed and physical force |
| $H$, $E$ | $\mathcal S$, $\mathcal J$ (discrete) | regularization, interpolation |
| $\xi_k$, $\partial B$ | $\mathbf X_\ell$, $\Gamma$ | |
| $u_B$ | $\mathbf u_\Gamma$ | |
| $\lambda$ | $\boldsymbol\lambda$ | multipliers |

# Reference list

39 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 2 (2026-11-08), list updated in chunk 3 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Classical (Peskin) immersed boundary method](/methods/classical-immersed-boundary-method.md)
- [Direct (discrete-time) forcing](/methods/direct-forcing.md)
- [Feedback forcing](/methods/feedback-forcing.md)
- [Immersed boundary projection method](/methods/immersed-boundary-projection-method.md)
- [Regularized delta function $\delta_h$](/operators/regularized-delta-function.md)
- [Spreading and interpolation operators $\mathcal S$, $\mathcal J$](/operators/spreading-and-interpolation.md)
- [Discrete conservation](/properties/discrete-conservation.md)
- [First-order accuracy of regularized-delta forcing at interfaces](/results/first-order-accuracy-of-regularized-delta-forcing.md)
