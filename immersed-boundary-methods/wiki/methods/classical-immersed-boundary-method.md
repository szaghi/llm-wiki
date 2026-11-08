---
type: Method
title: "Classical (Peskin) immersed boundary method"
description: "Peskin's formulation of fluid–structure interaction: an elastic structure described in Lagrangian coordinates exerts a force density that is spread to a fixed Eulerian grid with a regularized delta function and moves at the interpolated fluid velocity; its derivation, discretization, time stepping and the stiffness that limits explicit force computation."
status: established
aliases: [Peskin's method, immersed boundary method (Peskin), IB method for fluid–structure interaction, continuous forcing with elastic boundaries]
tags: [immersed-boundary, fluid-structure-interaction, delta-function, diffuse-interface, incompressible, stiffness]
timestamp: 2026-11-08T17:31:00Z
---

# Classical (Peskin) immersed boundary method

## Formulation

A viscous incompressible fluid fills $\Omega$; an elastic structure with
material coordinates $\mathbf s$ and configuration $\mathbf X(\mathbf s,t)$ is
immersed in it, with fluid of the same kind on both sides of a membrane. The
equations of motion are ([Peskin 2002](/sources/peskin-2002.md), §2–3;
[Peskin 1972](/sources/peskin-1972.md), §II):

$$\begin{aligned}
\rho\Big(\frac{\partial\mathbf u}{\partial t}+\mathbf u\cdot\nabla\mathbf u\Big)+\nabla p&=\mu\Delta\mathbf u+\mathbf f, \qquad \nabla\cdot\mathbf u=0,\\
\mathbf f(\mathbf x,t)&=\int\mathbf F(\mathbf s,t)\,\delta(\mathbf x-\mathbf X(\mathbf s,t))\,d\mathbf s,\\
\frac{\partial\mathbf X}{\partial t}(\mathbf s,t)&=\mathbf u(\mathbf X(\mathbf s,t),t)=\int\mathbf u(\mathbf x,t)\,\delta(\mathbf x-\mathbf X(\mathbf s,t))\,d\mathbf x,\\
\mathbf F&=-\frac{\wp\mathcal E}{\wp\mathbf X}.
\end{aligned}$$

The fluid equations are purely Eulerian, the elasticity law purely
Lagrangian, and the two interaction equations carry the delta function: "the
$\delta$ function makes its appearance under an integral sign when fluid
quantities are mapped into boundary quantities and vice versa" (Peskin 1972,
§II). Peskin (2002, §2) derives the system from the principle of least
action, introducing the Eulerian velocity through a pseudo-velocity and the
delta function, and adds viscosity afterwards; a non-uniform density is
spread from the Lagrangian mass density by the same kernel. For a surface
(membrane) the force density is singular like a one-dimensional delta on
$\Gamma$, and the formulation is equivalent to stress-jump conditions across
$\Gamma$ (Peskin 2002, §3, citing Peskin and Printz 1993 and Lai and Li 2001).
A fibre material with energy density depending on fibre strain gives
$\mathbf F=\partial_s(T\boldsymbol\tau)$, a force in the osculating plane of the
fibres (Peskin 2002, §2).

In 1972 the force law was a table of links between boundary points (and fixed
points in space), each with stiffness $k_s$ and rest length $\ell_0$ and
tension $T=k_s(\ell-\ell_0)$; cord-like links carry tension only when
stretched, rod-like links both ways, a nearly rigid fixed body is tied to
fixed points by stiff links of zero rest length, and a muscle is a link with
variable rest length (Peskin 1972, §III.C).

## Discretization

- Eulerian grid of width $h$, Lagrangian grid fine enough that markers are
  less than $h/2$ apart "to avoid leaks" (Peskin 2002, §4).
- Fluid operators: Chorin's fractional step with a discrete projection on a
  periodic box, central $D_0$ gradient and divergence (wide stencil, decoupled
  even–odd chains) and successive over-relaxation in 1972; in 2002 the tight
  Laplacian $L_h$ and the skew-symmetric advection $S_h(\mathbf u)$.
- Coupling by the [spreading and interpolation operators](/operators/spreading-and-interpolation.md)
  with a [regularized delta function](/operators/regularized-delta-function.md).
- Time stepping (2002): a second-order Runge–Kutta scheme with a preliminary
  half step (mixed forward/backward Euler) and a final midpoint/trapezoidal
  step, Navier–Stokes partly implicit (Peskin 2002, §7, after Lai and Peskin 2000).

## Stiffness

Because $\mathbf f$ is $O(h^{-1})$ near $\Gamma$ even when $\mathbf F=O(1)$, and a
displacement of order $h$ changes $\mathbf F$ by $O(1)$, forces computed from
the configuration at the start of the step are unstable unless $\Delta t$ is
very small (Peskin 1972, §IV, Fig. 2: the boundary overshoots equilibrium in a
single jump). Peskin's 1972 remedy computes the force from a predicted
configuration $\mathbf X^*=\mathbf X^n+\mathbf u^n(\mathbf X^n)\Delta t+(h_\Gamma/h^2)\mathbf F^*\Delta t^2$
that depends on the force itself, and solves the resulting fixed point
$\mathbf F^*=\mathbf F(\hat{\mathbf X}(\mathbf F^*))$ by under-relaxation; it is stable
at the same $\Delta t$ and viscosity (Fig. 5). Thirty years later the scheme
"is explicit in the computation of the elastic force", which "results in a
severe restriction on the time step" in most applications (Peskin 2002, §8,
citing Tu and Peskin 1992, Mayo and Peskin 1993, Stockie and Wetton 1999).

## Applications listed in the sources

Natural mitral valve in 2-D on a $20\times20$ grid, 2000 steps per beat and
about 5000 s on a CDC 6600 per beat, with the viscosity raised a hundredfold
because the cell-Reynolds condition $hRe<2$ of the fluid solver forbids the
physiological $Re\approx2000$ (Peskin 1972, §V). Peskin (2002, §9) lists
natural and prosthetic valves, a three-dimensional whole-heart model,
platelet aggregation, swimming of eels, sperm and bacteria, biofilms, the
cochlea, valveless pumping, flapping filaments, sails, parachutes and insect
flight.

## Qualifications

- Formally second order in space with smooth fields, the method is first
  order for problems with true immersed boundaries
  ([first-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md)).
- Volume enclosed by a closed membrane is not conserved exactly (Peskin 2002, §8).
- Goldstein et al. (1993, introduction) and Fadlun et al. (2000, §1) note that
  computing rigid-body forces through stiff springs is as complex as for
  elastic boundaries, which motivated prescribing the boundary position
  instead ([feedback forcing](/methods/feedback-forcing.md),
  [direct forcing](/methods/direct-forcing.md)).

# Citations

- [Peskin (1972)](/sources/peskin-1972.md) — §II–§VI.
- [Goldstein et al. (1993)](/sources/goldstein-1993.md) — introduction.
- [LeVeque & Li (1994)](/sources/leveque-1994.md) — §1 (IB as motivation of the IIM).
- [Fadlun et al. (2000)](/sources/fadlun-2000.md) — §1.
- [Peskin (2002)](/sources/peskin-2002.md) — §2–§9.
