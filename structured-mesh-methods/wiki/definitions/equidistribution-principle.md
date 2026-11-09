---
type: Definition
title: "Equidistribution principle"
description: "Choose mesh points so that a positive monitor function, a measure of the solution error, is equalized over every cell: in one dimension the integral of the monitor up to x(ξ) is a fixed fraction ξ of its total; the principle underlies most adaptive and moving mesh equations."
status: established
aliases: [EP, de Boor equidistribution, monitor-function equidistribution]
tags: [adaptation, moving-mesh, monitor-function]
timestamp: 2026-11-08T20:24:00Z
---

# Equidistribution principle

Introduced by de Boor for boundary value problems of ordinary differential
equations, the **equidistribution principle** chooses the mesh so that a
monitor function $M(x,t)>0$ — a measure of the computational error, most
often the arc length $\sqrt{1+u_x^2}$ or a curvature measure — has the same
integral over every cell. In one dimension, with $\xi\in[0,1]$,

$$\int_0^{x(\xi,t)}M(x,t)\,dx=\xi\,\theta_M(t),\qquad \theta_M(t)=\int_0^1M\,dx,$$

and differentiating in $\xi$ gives the equivalent forms $M\,x_\xi=\theta_M$ and
$(M\,x_\xi)_\xi=0$ ([Huang, Ren & Russell 1994](/sources/huang-1994.md)). These
contain no node velocity; Huang et al. call them quasi-static and derive
from them the [moving mesh PDEs](/methods/moving-mesh-pde.md).

Weighting cell volume by a solution-dependent weight in a variational
generator is the multidimensional analogue: cells shrink where the weight is
large ([variational grid generation](/methods/variational-grid-generation.md);
[Brackbill & Saltzman 1982](/sources/brackbill-1982.md)). Monitors computed
from steep numerical solutions are sensitive to small mesh perturbations and
make equidistributed meshes oscillate; spatial smoothing of $M$ is the usual
remedy ([Huang et al. 1994](/sources/huang-1994.md)).

# Citations

- [Huang, Ren & Russell (1994)](/sources/huang-1994.md) — §2.
- [Brackbill & Saltzman (1982)](/sources/brackbill-1982.md) — weighted volume variation.
