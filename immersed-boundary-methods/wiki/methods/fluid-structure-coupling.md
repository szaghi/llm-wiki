---
type: Method
title: "Fluid–structure coupling in immersed boundary methods"
description: "How immersed boundary methods couple the flow with a moving or deforming structure: monolithic versus partitioned schemes, loose (explicit) versus strong (iterated or implicit) coupling, the added-mass instability and density-ratio limits, convergence acceleration, the cost of strongly coupled methods and its reduction, and the solid models (fibres, finite elements, material points) the sources couple."
status: established
aliases: [FSI coupling, strong coupling, loose coupling, weak coupling, added-mass instability, partitioned FSI]
tags: [fluid-structure-interaction, coupling, stability, added-mass, moving-boundary]
timestamp: 2026-11-08T18:10:00Z
---

# Fluid–structure coupling in immersed boundary methods

In fluid–structure interaction (FSI) the body's motion is unknown: the flow
loads the structure, and the structure's position and velocity set the
boundary condition of the flow. [Sotiropoulos & Yang (2014)](/sources/sotiropoulos-2014.md),
§4, organize the coupling strategies as follows.

- **Monolithic**: fluid and structure in one system; unconditionally stable,
  but software modularity is lost.
- **Partitioned, loose (weak) coupling**: each solver is called once per step,
  sequentially, with interface data from the previous step. It is widely used
  in aeronautics but suffers an **artificial added-mass instability** for light
  structures in incompressible flow: the added mass tends to a constant as
  $\Delta t\to0$ in incompressible flow and scales with $\Delta t$ in compressible
  flow (Causin et al., cited). [Uhlmann (2005)](/sources/uhlmann-2005.md), §4,
  finds explicit coupling of particles stable only for $\rho_p/\rho_f\gtrsim1.05$
  (discs) and $1.2$ (spheres), independent of $\Delta t$.
- **Partitioned, strong coupling**: sub-iterations each step until the
  interface conditions hold — block Gauss–Seidel or Jacobi iterations with
  under-relaxation $\omega$, fixed or updated by Aitken's $\Delta^2$ method or steepest
  descent (Borazjani et al.'s CURVIB scheme), or Newton–Raphson/block-Newton
  iterations, possibly Jacobian-free (§4.3–4.4).

[Griffith & Patankar (2020)](/sources/griffith-2020.md) observe that immersed
formulations "do not appear to suffer from instabilities related to the added
mass effect, even when explicit coupling strategies are used", but that stiff
structures or large penalty parameters force small time steps, and that the
scalable solvers implicit coupling needs are still lacking.

## Cost of strong coupling

[Nair & Goza (2022)](/sources/nair-2022.md) note that strongly coupled
immersed-boundary methods — stable over a wide range of mass ratios and large
deformations — solve, at every FSI iteration, linear systems as large as the
flow grid, although the nonlinear constraint involves only the interface
points. Block-LU reformulations (Goza and Colonius, building on the
[IB projection method](/methods/immersed-boundary-projection-method.md))
restrict iterations to interface variables but embed a large system inside the
small one. Their remedy precomputes the matrix that encapsulates the large
system on a fixed sub-domain enveloping the body's range of motion and
interpolates the sub-domain interpolation operator to the moving body, so each
step solves only small systems, as stationary-body methods do. Lift and
deflection stay within 1–2 % of the exact-operator results with an
order-of-magnitude speed-up per step for rigid, torsionally mounted and
deformable bodies in 2-D.

## Structural models coupled

| structural model | coupling | source |
|---|---|---|
| elastic fibres, Lagrangian markers | [classical IB](/methods/classical-immersed-boundary-method.md) spreading and interpolation | [Peskin (2002)](/sources/peskin-2002.md) |
| finite-element continuum (immersed finite element, IBFE) | delta-function coupling at quadrature points; adjoint operators with Gaussian quadrature (Griffith and Luo) | [Griffith & Patankar (2020)](/sources/griffith-2020.md) |
| prescribed kinematics | distributed Lagrange multipliers; frictional and spring-like penalty forces | Griffith & Patankar (2020) |
| rigid, torsional, deformable bodies | strongly coupled projection method | [Nair & Goza (2022)](/sources/nair-2022.md) |
| material point method (fracture, fragments) | velocity imposed in boundary cells located from particles, reaction force returned to particles | [Ni et al. (2022)](/sources/ni-2022.md) |

[Ni et al. (2022)](/sources/ni-2022.md), §5, couple a finite-volume shock
solver to the material point method with a "Lagrangian continuous-forcing"
immersed boundary: boundary cells are found from the particle distribution
(thin fragments and isolated particles included), their fluid velocity is set
to the structure velocity from the nodal momentum at every Runge–Kutta stage —
equivalent to an Eulerian force $\rho\,\Delta\mathbf u/(\alpha_k\Delta t)$ — and the
reaction force is returned evenly to the particles in the cell. No interface
reconstruction or normal is needed, and the velocity condition holds exactly.
They argue that penalty forcing with a smoothed delta over-constrains the
system when there are more boundary particles than grid points in the kernel
support, producing oscillations that erase velocity-sensitive features such as
Mach reflection.

# Citations

- [Uhlmann (2005)](/sources/uhlmann-2005.md) — §4.
- [Peskin (2002)](/sources/peskin-2002.md) — §2–§3.
- [Sotiropoulos & Yang (2014)](/sources/sotiropoulos-2014.md) — §4.
- [Griffith & Patankar (2020)](/sources/griffith-2020.md) — introduction, formulations.
- [Nair & Goza (2022)](/sources/nair-2022.md) — §1–§4.
- [Ni et al. (2022)](/sources/ni-2022.md) — §1, §5, §6.
