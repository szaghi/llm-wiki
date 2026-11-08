---
type: Method
title: "Direct (discrete-time) forcing"
description: "Discrete-forcing immersed boundary method in which the force at a forcing point is solved from the discretized momentum equation so that the updated velocity equals a target value reconstructed from the boundary velocity; free of gains and of the stiffness of feedback forcing, with accuracy set by the velocity reconstruction and conservation of cut cells restored by a mass source."
status: established
aliases: [discrete-time forcing, Mohd-Yusof forcing, direct momentum forcing, discrete forcing]
tags: [immersed-boundary, discrete-forcing, sharp-interface, incompressible, reconstruction]
timestamp: 2026-11-08T17:31:00Z
---

# Direct (discrete-time) forcing

Write one time step of the momentum equation with forcing as
$(\mathbf u^{n+1}-\mathbf u^n)/\Delta t=\mathbf{RHS}^{n+1/2}+\mathbf f^{n+1/2}$, with
$\mathbf{RHS}$ collecting convection, diffusion and the pressure gradient. Asking
which force yields $\mathbf u^{n+1}=\mathbf V^{n+1}$ at a forcing point gives

$$\mathbf f^{n+1/2}=\frac{\mathbf V^{n+1}-\mathbf u^n}{\Delta t}-\mathbf{RHS}^{n+1/2}$$

there and $\mathbf f=\mathbf 0$ elsewhere. The forcing is *direct*: the boundary
value is imposed at every step "without any dynamical process", whatever the
flow frequencies; there are no free constants, no extra CPU cost and, with
each term taken at the appropriate time level, no effect on the stability of
the time integrator ([Fadlun et al. 2000](/sources/fadlun-2000.md), §2.2,
after Mohd-Yusof 1997). Fadlun et al. integrated a vortex-ring case at CFL
$1.5$, close to the limit $\sqrt3$ of their third-order Runge–Kutta scheme,
where [feedback forcing](/methods/feedback-forcing.md) was stable only to
CFL $0.025$ (§2.4).

In a fractional-step method [Kim et al. (2001)](/sources/kim-2001.md),
§2.2, determine $\mathbf f$ so that the *intermediate* velocity satisfies the
boundary condition, which costs $O(\Delta t^2)$ in the boundary value and keeps
overall second-order accuracy; the force is computed from a provisional
explicit discretization (RK3 convection, forward-Euler diffusion).

## The target velocity: where accuracy is decided

Forcing points rarely lie on $\Gamma$ (on a staggered grid never for all
components), so the target $\mathbf V$ must be reconstructed from
$\mathbf u_\Gamma$ and fluid values. [Fadlun et al. (2000)](/sources/fadlun-2000.md),
§2.3, compare three choices on a vortex-ring grid study ($49\times97$ to
$385\times769$):

| reconstruction | observed order |
|---|---|
| stepwise: force the grid point nearest to $\Gamma$ as if it lay on it | below first |
| volume-fraction weighting of the force by the solid fraction of the cell | first (boundary velocity underestimated) |
| linear interpolation between $\mathbf u_\Gamma$ on $\Gamma$ and the second grid point, imposed at the first grid point outside the body | second |

The accuracy "is independent of" the forcing law (feedback or direct);
the efficiency is not (§2.3–2.4). The linear profile requires the grid to be
fine near the wall; the interpolation direction (streamwise or transverse) is
arbitrary.

[Kim et al. (2001)](/sources/kim-2001.md), §2.2, apply the force only on or
inside the body. At a forcing point inside the body the target is the mirror
of the outside velocity, obtained by bilinear interpolation using the no-slip
value at the wall-normal intersection, or by linear interpolation along a grid
line that switches from the first to the second outside point when the forcing
point is far from $\Gamma$. The simple extrapolation $\mathbf V=-(h_\Gamma/y_A)\tilde{\mathbf u}_A$
diverged in a test with $h_\Gamma/y_A=100$; the switched formula never did.

## Mass source

With the no-slip value imposed on the faces of a cell cut by $\Gamma$, the
fluid part of the cell no longer conserves mass. [Kim et al. (2001)](/sources/kim-2001.md),
§2.3, add a mass source/sink $q_m$ at the centre of each such cell
($\nabla\cdot\mathbf u=q_m$), computed from the difference between the fluxes of
the full cell and of its fluid part with the provisional velocities; $q_m$
sums to zero over the domain. In decaying-vortex tests with boundaries
parallel and oblique to the grid, the error with the mass source is "much
smaller" than without and comparable with a computation without immersed
boundary, at second order in space ([discrete conservation](/properties/discrete-conservation.md)).

## Results reported

Vortex ring from a curvilinear nozzle against the authors' experiment,
axisymmetric and 3-D [flow past a sphere](/benchmarks/flow-past-sphere.md)
for $Re=100$–$1000$, and LES of a motored piston–cylinder assembly, "the
first example of an immersed boundary simulation with an LES turbulence
model" (Fadlun et al. 2000, §3); [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
at $Re=40$ and $100$ and flow past a sphere (Kim et al. 2001, §3), with forces
obtained by integrating the momentum forcing.

# Citations

- [Fadlun et al. (2000)](/sources/fadlun-2000.md) — §1, §2.2–2.4, §3.
- [Kim et al. (2001)](/sources/kim-2001.md) — §1, §2.2, §2.3, §3.
