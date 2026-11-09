---
type: Method
title: "Variational grid generation"
description: "Grids obtained by minimizing a weighted combination of integral measures of the mapping — smoothness (whose minimizer is Winslow's generator), orthogonality and weighted cell volume — whose Euler–Lagrange equations are solved by relaxation; a solution-dependent weight concentrates cells and reduces the error on singular problems."
status: established
aliases: [Brackbill–Saltzman method, adaptive zoning, variational mesh adaptation]
tags: [variational-generation, adaptation, grid-generation]
timestamp: 2026-11-08T20:24:00Z
---

# Variational grid generation

[Brackbill & Saltzman (1982)](/sources/brackbill-1982.md) measure mesh
properties by integrals of the mapping and control them by minimization:

$$I_s=\int_\Omega\big(|\nabla\xi|^2+|\nabla\eta|^2\big)\,d\mathbf x,\qquad I_o=\int_\Omega(\nabla\xi\cdot\nabla\eta)^2\,d\mathbf x,\qquad I_v=\int_\Omega w\,J\,d\mathbf x .$$

$I_s$ measures smoothness, and its minimizer is the Laplace (Winslow)
generator ([elliptic grid generation](/methods/elliptic-grid-generation.md));
$I_o$ measures orthogonality, with a volume-weighted variant
$\int(\nabla\xi\cdot\nabla\eta)^2J^3\,d\mathbf x$; $I_v$ measures the variation of
cell volume against a weight $w(\mathbf x)$. Minimizing $I_o$ or $I_v$ alone is
ill posed — an incompressible potential-flow deformation preserves every $J$,
and orthogonal meshes can be folded into other orthogonal meshes — so they
are added to $I_s$, which has a unique minimizer:

$$I=I_s+\lambda_v I_v+\lambda_o I_o,\qquad \lambda_v,\lambda_o>0 .$$

The Euler–Lagrange equations, written after interchanging dependent and
independent variables, are differenced and relaxed.

**Effects measured by the authors.** Raising $\lambda_v$ increases the volume
variation at the expense of smoothness (cell-volume ratio about 5 for a
weight ratio of 100), nearly independently of the direction of the weight
gradient; raising $\lambda_o$ improves orthogonality ($I_o$ from 4 to 0.006
at $\lambda_o=1000$). The volume-weighted orthogonality term is compatible with
volume control and so suits reducing the skewness of adaptive meshes; the
plain one is not.

**Adaptation.** With $w$ taken from the solution, a one-dimensional analysis
shows that the truncation error at a thin singular layer does not grow as
the layer thins, and in two dimensions the error of a singular problem falls
from 25 % to 3.5 % as $\lambda_v$ goes from 0 to 1 — under 5 %, up to a tenth of
the nonadaptive error. How to choose weights a priori, and why large
$\lambda$ is hard to reach, are left open. The same idea of equalizing a
weight drives the [equidistribution principle](/definitions/equidistribution-principle.md).

# Citations

- [Brackbill & Saltzman (1982)](/sources/brackbill-1982.md) — measures, variational problem, examples, conclusion.
