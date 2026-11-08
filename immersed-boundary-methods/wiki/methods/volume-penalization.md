---
type: Method
title: "Volume penalization (Brinkman penalization)"
description: "Fictitious-domain immersed boundary method that solves the flow equations in the whole domain and models the body as a porous medium of vanishing permeability through a penalty term on its volume; the L2 (Darcy) and H1 (Brinkman) penalizations, their convergence as the penalty parameter vanishes, and force computation from the penalty term."
status: established
aliases: [Brinkman penalization, penalization method, L2 penalization, H1 penalization, porous-medium fictitious domain]
tags: [immersed-boundary, penalization, fictitious-domain, continuous-forcing, incompressible]
timestamp: 2026-11-08T18:32:00Z
---

# Volume penalization (Brinkman penalization)

The incompressible Navier–Stokes equations in $\Omega_f$ with no-slip on
$\Gamma$ are replaced by equations on the whole $\Omega=\Omega_f\cup\Omega_s$ with
a penalty term in the body ([Angot et al. 1999](/sources/angot-1999.md), §3).
Two penalizations are analysed.

**$L^2$ penalization** (a damping term on the velocity):

$$\frac{\partial\mathbf u_\eta}{\partial t}+\mathbf u_\eta\cdot\nabla\mathbf u_\eta-\frac{1}{Re}\Delta\mathbf u_\eta+\nabla p_\eta+\frac{1}{\eta}\chi_s\mathbf u_\eta=\mathbf f_0 .$$

The expansion $\mathbf u_\eta=\mathbf u+\eta\tilde{\mathbf u}$ gives $\mathbf u=\mathbf 0$ in
$\Omega_s$ and the Navier–Stokes solution in $\Omega_f$; in the body
$\tilde{\mathbf u}$ obeys a Darcy law with a Neumann pressure condition, so the
obstacle is a porous medium (Remark 3.1).

**$H^1$ penalization** penalizes the whole linear part, time derivative and
viscous term included,
$(1+\eta^{-1}\chi_s)\partial_t\mathbf u_\eta+\dots-\nabla\cdot\big((1+\eta^{-1}\chi_s)\boldsymbol\Sigma(\mathbf u_\eta,p_\eta)\big)+\eta^{-1}\chi_s\mathbf u_\eta$,
and $\tilde{\mathbf u}$ obeys a Brinkman equation in the body with a
stress-Neumann condition (Remark 3.2).

The idea predates the analysis: Arquis and Caltagirone (1984) penalized the
volume of a porous body in a Brinkman model with variable permeability, and
the point forcing of Peskin and of [Goldstein et al. (1993)](/sources/goldstein-1993.md)
"has to be extended to the volume of the body to give correct physical
solutions at high Reynolds numbers" (Angot et al. 1999, §1, citing Peskin 1982).

## Convergence and forces

[Angot et al. (1999)](/sources/angot-1999.md) prove in 2-D that
$\mathbf u_\eta\to\mathbf u$ as $\eta\to0$, with $\mathbf u|_{\Omega_f}$ the unique weak
Navier–Stokes solution and $\mathbf u=\mathbf 0$ in $\Omega_s$, and give error estimates
of order $\eta^{1/4}$ in the fluid for the $L^2$ penalization and a sharper one
for the $H^1$ penalization ([convergence of volume penalization](/results/convergence-of-volume-penalization.md)).
Under a compatibility condition the weak limit of $\eta^{-1}\chi_s\mathbf u_\eta$
is the force density on the obstacle, so drag and lift follow from
integrating the penalty term over the body volume (Theorem 4.3).

## Practice

On a square cylinder in a channel aligned with a $320\times80$ grid, the
penalized solution with $\eta=10^{-8}$ is indistinguishable from the Dirichlet
reference at $Re=40$ and $Re=80$; a large $\eta$ delays convection and
underestimates the Strouhal number; the pressure is continuous through the
obstacle; and the $H^1$ penalization brings no practical gain because the
discretized penalized viscous term effectively changes the body volume
(Angot et al. 1999, §6). Since $\eta$ can be taken as small as needed, the
penalty error is negligible compared with the discretization error (§7).

## Relation to feedback forcing

[Mittal & Iaccarino (2005)](/sources/mittal-2005.md) note that the Brinkman
force $-(\mu/K)\mathbf u$, with permeability $K$ infinite in the fluid and zero in the
solid (dimensionless, $K\leftrightarrow\eta$ and $\chi_s$ marks where $K$ is small), is feedback forcing with $\alpha_f=0$ and $\beta_f=-\mu/K$, subject to the same
stiffness from the large variation of $K$; in practice $K$ is large but finite in
the fluid, small in the solid and smoothed across $\Gamma$, which leaves an error
in the wall velocity. They contrast it with the fictitious-domain method of
Glowinski et al., which treats the solid as a fluid under a rigidity
constraint.

## Compressible penalization

- **Pressure-tight and non-stiff.** [Reiss (2022)](/sources/reiss-2022.md)
  replaces the stiff velocity penalty that must balance large pressure
  gradients by a reduced volume fraction $\phi_v$ in the body (lowered by six to
  eight orders of magnitude) that scales mass, momentum and energy alike, with
  a non-conservative pressure term $p\,\nabla\phi_v$ as in quasi-one-dimensional gas
  dynamics. The speed of sound and hence the CFL condition are unchanged,
  convective and viscous fluxes vanish inside the body (pressure-tight),
  $\phi_v$ alone gives a slip wall and an added Darcy friction gives no-slip;
  mass and energy are conserved and the skew-symmetry of the energy-conserving
  interior scheme is kept. Tests: acoustics, a cylinder, a supersonic wedge, a
  confined blast wave.
- **Porosity and cost.** [Ménez et al. (2023)](/sources/menez-2023.md) use
  the compressible Brinkman form with a permeability $\eta$ treated implicitly and
  a porosity $\phi_p$ in the continuity equation needed for correct wave
  reflection (after Liu and Vasilyev); since the spectral radius grows as
  $\phi_p$ decreases, accuracy costs time step. An adiabatic condition with an
  implicit source term borrows the ghost-cell framework (zero normal
  temperature gradient through two image points). Penalization is first order
  in space, as is the continuous-forcing method they compare, but much cheaper;
  a new porosity model reproduces shock reflection at the accuracy of
  $\phi_p=0.01$ with the cost divided by 36.

## Beyond fluid mechanics

[Munschy et al. (2024)](/sources/munschy-2024.md) model a plasma-facing wall
in a 1D-1V kinetic Vlasov–Poisson computation with immersed boundary conditions
by penalization — sink and thermalization terms in a masked wall region, with
or without current flowing inside the material — and recover the kinetic
sheath physics, finding ion and electron heat transmission factors 60 % and
35 % larger than usually predicted; the aim is a wall treatment for
gyrokinetic codes whose mesh cannot resolve the sheath.

# Citations

- [Goldstein et al. (1993)](/sources/goldstein-1993.md) — introduction (point forcing that Angot et al. contrast).
- [Angot et al. (1999)](/sources/angot-1999.md) — §1, §3–§7.
- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — continuous-forcing section (rigid boundaries).
- [Reiss (2022)](/sources/reiss-2022.md) — §1–§4.
- [Ménez et al. (2023)](/sources/menez-2023.md) — §2–§4.
- [Munschy et al. (2024)](/sources/munschy-2024.md) — §1–§2, conclusions.
